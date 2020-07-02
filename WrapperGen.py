from prance import ResolvingParser
import json

# specs = ResolvingParser("spotify-mt-oas3.yaml").specification

# paths = specs["paths"]

# for endpoint, methodObject in paths.items():
#     # print(endpoint)
#     for method, info in methodObject.items():
#         # print(method)
#         # print(info)
def kebabToCamel(s):
    iterchars = iter(s.split("-"))
    result = s.split("-")[0]
    next(iterchars)
    
    for word in iterchars:
        result += word.capitalize()
    
    return result

def dotToCamel(s):
    if "." not in s:
        return s
    
    splitString = (s.split(".", 1))
    if splitString[0] in splitString[1]:
        return splitString[1]
    else:
        return splitString[0] + splitString[1][0].upper() + splitString[1][1:]

with open("hydrology-oas.json") as f:
    specs = json.load(f)
    paths = specs["paths"]
    
    endpoints = {}
    
    for endpoint, endpointInfo in paths.items():
        
        # --- collecting all distinct endpoints, ignoring the _view params ---
        if "?_view" not in endpoint:
            endpoints[endpoint] = {}
            endpoints[endpoint]["paths"] = [endpoint]
            endpoints[endpoint]["parameters"] = endpointInfo["get"]["parameters"]
        else:
            # get base endpoint, which is the string before the '?'
            baseEndpoint = endpoint.split('?',1)[0]
            endpoints[baseEndpoint]["paths"].append(endpoint)
            
        # ---
        
        for param in endpointInfo["get"]["parameters"]:
            for k,v in param.items():
                print(f"{k}: {v}")
            
        print()
            

    
"""
write a function that takes an input:
    1. a function name
    2. endpoint url
    3. list of parameters
    
and returns the function in correct python syntax
""" 

def generateEndpointFunction(name, url, params):
    requiredParams = []
    optionalParams = []
    
    for p in params:
        if "name" in p:
            if ("required" not in p or (p["required"] == "true")):
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
    
    with open("test.py", "w") as f:
        f.write(functionString)
        
    return functionString 