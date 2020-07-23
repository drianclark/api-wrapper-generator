import json

with open("hydrology-oas.json") as f:
    jsonSpec = json.load(f)
                
paths = jsonSpec["paths"]
schemas = jsonSpec["components"]["schemas"]

for path, pathInfo in paths.items():
    afterEndSlash = list(filter(lambda s: '{' not in s, path.split('/')))[-1]
    removeParams = afterEndSlash.split('?')[0]
    
    print(removeParams)
    
    