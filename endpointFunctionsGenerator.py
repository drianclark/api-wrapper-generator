import json
from helpers import dotToCamel, kebabToCamel, makeFunctionName

class EndpointFunctionsGenerator:
    # apiSpec is a json file
    def __init__(self, apiSpec, outFile):
        self.apiSpec = apiSpec
        self.outFile = outFile
        
        with open(self.apiSpec) as f:
            specs = json.load(f)
            paths = specs["paths"]
            self.serverURL = specs["servers"][0]["url"]

                            
        self.endpoints = {}
                        
        for endpoint, endpointInfo in paths.items():
                            
            # --- collecting all distinct endpoints, ignoring the _view params ---
            if "?_view" not in endpoint:
                self.endpoints[endpoint] = {}
                self.endpoints[endpoint]["paths"] = [endpoint]
                self.endpoints[endpoint]["parameters"] = endpointInfo["parameters"]
                self.endpoints[endpoint]["parameters"] += endpointInfo["get"]["parameters"]
                self.endpoints[endpoint]["name"] = makeFunctionName(endpointInfo["description"])
            else:
                # get base endpoint, which is the string before the '?'
                baseEndpoint = endpoint.split('?',1)[0]
                self.endpoints[baseEndpoint]["paths"].append(endpoint)
                
    def generateEndpointFunctions(self):
        def generateEndpointFunction(name, url, params):
            requiredParams = []
            optionalParams = []
                
            for p in params:
                if "name" in p:
                    if (("required" in p) and p["required"] == "true"):
                        requiredParams.append(p["name"])
                        
                    else:
                        optionalParams.append(f"{p['name']}=None")
                    
            requiredParams = list(map(kebabToCamel, requiredParams))
            optionalParams = list(map(kebabToCamel, optionalParams))
            requiredParams = list(map(dotToCamel, requiredParams))
            optionalParams = list(map(dotToCamel, optionalParams))

                
            paramsString = ""
                    
            for p in optionalParams:
                try:
                    paramName = p.split("=")[0]
                    paramsString += f"""if {paramName} != None:
                    parameters["{paramName}"] = {paramName} 
                    
                """
                except KeyError:
                    pass
                
            functionString = f"""def {name}({', '.join(requiredParams + optionalParams)}):

                parameters = {{}}
                
                {paramsString}

                r = requests.get(
                    f'{url}', params=parameters
                )

                items = r.json()

                return items
            """
                    
            return functionString 
    
        for _, endpointInfo in self.endpoints.items():
            f = generateEndpointFunction(endpointInfo["name"],
                                     self.serverURL + next(path for path in endpointInfo["paths"] if "?" not in path),
                                     endpointInfo["parameters"])
            print(f)
            
e = EndpointFunctionsGenerator("hydrology-oas.json", "test.py")
e.generateEndpointFunctions()