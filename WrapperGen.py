from prance import ResolvingParser

specs = ResolvingParser("spotify-mt-oas3.yaml").specification

paths = specs["paths"]

for endpoint, methodObject in paths.items():
    print(endpoint)
    for method, info in methodObject.items():
        print(method)
        print(info)
    
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