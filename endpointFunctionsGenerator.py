import json
import jsonref
import os
from pprint import pprint
from jinja2 import Template, Environment, FileSystemLoader
from prance import ResolvingParser
from helpers import dotToCamel, kebabToCamel, makeFunctionName, makeParamName

class EndpointFunctionsGenerator:
    # apiSpec is a json file
    def __init__(self, apiSpec, outFile, directory='renders'):
        self.apiSpec = apiSpec
        self.outFile = outFile
        self.directory = directory
        self.API_URL = "https://environment.data.gov.uk"
        
        with open(self.apiSpec) as f:
            specs = jsonref.load(f)
            paths = specs["paths"]
            self.serverURL = self.API_URL + specs["servers"][0]["url"]
            
        self.endpoints = {}
                        
        for endpoint, endpointInfo in paths.items():
            # collecting all distinct endpoints, ignoring the _view params
            if "?_view" not in endpoint:
                self.endpoints[endpoint] = {}
                self.endpoints[endpoint]["paths"] = [endpoint]
                self.endpoints[endpoint]["name"] = makeFunctionName(endpointInfo["description"])
                
                parameters = endpointInfo["parameters"]
                parameters += endpointInfo["get"]["parameters"]
                    
                self.endpoints[endpoint]["requiredParameters"] = set()
                self.endpoints[endpoint]["optionalParameters"] = set()
                required = self.endpoints[endpoint]["requiredParameters"]
                optional = self.endpoints[endpoint]["optionalParameters"]
                                
                # collecting required and optional parameters as tuples
                #    (api parameter name, camelised parameter name)
                
                for p in parameters:
                    if "name" in p:
                        paramName = p["name"]
                        
                        if (("required" in paramName) and (p["required"] == "true" or p["required"] == True)):
                            required.add((paramName,makeParamName(paramName)))
                                
                        else:
                            optional.add((paramName, makeParamName(paramName)))  
            else:
                # get base endpoint, which is the string before the '?'
                baseEndpoint = endpoint.split('?',1)[0]
                self.endpoints[baseEndpoint]["paths"].append(endpoint)
                self.endpoints[baseEndpoint]["optionalParameters"].add(("view","view"))
                
    def generateEndpointFunctions(self):
        def generateEndpointFunction(name, requiredParams, optionalParams, url):
            env = Environment(loader=FileSystemLoader('templates'))
            template = env.get_template('endpointFunctionTemplate.txt')
            
            requiredParamsField = [p[1] for p in requiredParams]
            optionalParamsField = [p[1] + "=None" for p in optionalParams]
            paramsField = ',\n'.join(requiredParamsField + optionalParamsField)
            
            render = template.render(name=name,
                                     paramsField=paramsField, 
                                     optionalParams=optionalParams, 
                                     url=url)
            
            return render
                
        generateEndpointFunction(self.endpoints["/data/readings"]["name"],
                                 self.endpoints["/data/readings"]["requiredParameters"],
                                 self.endpoints["/data/readings"]["optionalParameters"],
                                 "https://environment.data.gov.uk/hydrology/data/readings")
        
        functionStrings = []
        
        for endpoint, endpointInfo in self.endpoints.items():
            functionStrings.append(generateEndpointFunction(endpointInfo["name"],
                                                            endpointInfo["requiredParameters"],
                                                            endpointInfo["optionalParameters"],
                                                            self.serverURL + endpoint))
        
        
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('endpointFunctionsTemplate.txt')
        
        endpointFunctions = template.render(functionStrings=functionStrings)    
        
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)     
            
        with open(f'{self.directory}/{self.outFile}', 'w') as f:
            f.write(endpointFunctions)   
        