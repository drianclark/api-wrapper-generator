from prance import ResolvingParser
import json

# specs = ResolvingParser("spotify-mt-oas3.yaml").specification

# paths = specs["paths"]

# for endpoint, methodObject in paths.items():
#     # print(endpoint)
#     for method, info in methodObject.items():
#         # print(method)
#         # print(info)
        
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
    3. http method
    4. list of parameters
    
and returns the function in correct python syntax
""" 

def generateEndpointFunction(name, url, method, params):
    return f"""def {name}({', '.join(params)}):

    r = requests.{method}(
        f'{url}', params=params
    )

    items = r.json()

    return items
"""