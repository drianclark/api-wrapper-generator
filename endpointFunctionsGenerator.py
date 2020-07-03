import json
import jsonref
from inspect import cleandoc
from prance import ResolvingParser
from helpers import dotToCamel, kebabToCamel, makeFunctionName, makeParamName

class EndpointFunctionsGenerator:
    # apiSpec is a json file
    def __init__(self, apiSpec, outFile):
        self.apiSpec = apiSpec
        self.outFile = outFile
        self.API_URL = "https://environment.data.gov.uk"
        
        with open(self.apiSpec) as f:
            specs = jsonref.load(f)
            paths = specs["paths"]
            self.serverURL = self.API_URL + specs["servers"][0]["url"]
            
        # specs = ResolvingParser(self.apiSpec).specification
        # paths = specs["paths"]
        # self.serverURL = self.API_URL + specs["servers"][0]["url"]
        # print(paths)


        # for endpoint, methodObject in paths.items():
            # print(endpoint)
            # for method, info in methodObject.items():
                # print(method)
                # print(info)
               
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
        def initialiseFile():
            with open(self.outFile, 'w') as f:
                f.write("import requests\n\n")
        
        def generateEndpointFunction(name, url, params):
            requiredParams = []
            optionalParams = []
                
            for p in params:
                if "name" in p:
                    if (("required" in p) and (p["required"] == "true" or p["required"] == True)):
                        requiredParams.append(((p["name"]), makeParamName(p["name"])))
                        
                    else:
                        optionalParams.append((p["name"], f"{makeParamName(p['name'])}=None"))
            
            print(requiredParams)
            print(optionalParams)

            paramsString = ""
                    
            for original, camelised in optionalParams:
                paramName = camelised.split("=")[0]
                paramsString += f"""\
    if {paramName} != None:
        parameters["{original}"] = {paramName}
"""
            paramField = ",\n".join([camelised for _,camelised in requiredParams] + [camelised for _,camelised in optionalParams])
            functionString = f"""
def {name}(
{paramField}):
    
    parameters = {{}}
                
{paramsString}
    r = requests.get(
        '{url}', params=parameters
    )

    items = r.json()
    return items
    
"""
            return functionString 
    
        initialiseFile()
        
        for endpoint, endpointInfo in self.endpoints.items():
            print(endpoint)
            
            functionString = generateEndpointFunction(endpointInfo["name"],
                                     self.serverURL + next(path for path in endpointInfo["paths"] if "?" not in path),
                                     endpointInfo["parameters"])
            
            with open(self.outFile, 'a') as f:
                f.write(functionString)
            
e = EndpointFunctionsGenerator("hydrology-oas.json", "test.py")
e.generateEndpointFunctions()