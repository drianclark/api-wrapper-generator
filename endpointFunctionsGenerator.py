import json
import jsonref
import os
from pprint import pprint
from jinja2 import Template, Environment, FileSystemLoader
from prance import ResolvingParser
from helpers import dotToCamel, kebabToCamel, makeFunctionName, makeParamName, makeClassName, constructEndpointFunctionName

class EndpointFunctionsGenerator:
    # apiSpec is a json file
    def __init__(self, config, apiSpec, outFile, directory='renders'):
        self.apiSpec = apiSpec
        self.outFile = outFile
        self.directory = directory
        # self.API_URL = "https://environment.data.gov.uk"
        self.API_URL = "https://hydrology-test.epimorphics.net"
        
        with open(config) as f:
            self.mappings = json.load(f)["returnTypes"]
        
        with open(self.apiSpec) as f:
            specs = jsonref.load(f)
            paths = specs["paths"]
            self.serverURL = self.API_URL + specs["servers"][0]["url"]
            
        self.endpoints = {}
            
        for endpoint, endpointInfo in paths.items():
            
            # collecting all distinct endpoints, ignoring the _view params
            # and creating a dictionary for each
            
            if "?_view" not in endpoint:    # for default views
                
                """
                    For endpoint '/id/measures/{measure}/readings':
                        constructEndpointFunctionName(endpoint) => readingsByMeasure
                        
                    This endpoint naming pattern may not hold across different APIs
                """
                functionName = constructEndpointFunctionName(endpoint)
                        
                self.endpoints[endpoint] = {}
                self.endpoints[endpoint]["paths"] = [endpoint]
                self.endpoints[endpoint]["name"] = functionName
                
                """
                 url parameters and parameters embedded within the endpoint path, e.g.
                 the last id in '/id/measures/{id}' are stored in different parts
                 of the spec
                """
                parameters = endpointInfo["parameters"]
                parameters += endpointInfo["get"]["parameters"]
                    
                # using set() to get rid of duplicates
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
                            
            # adding the "view" parameter to endpoints that should have it
            else:
                # get base endpoint, which is the string before the '?'
                baseEndpoint = endpoint.split('?',1)[0]
                self.endpoints[baseEndpoint]["paths"].append(endpoint)
                self.endpoints[baseEndpoint]["optionalParameters"].add(("view","view"))
                
    def generateEndpointFunctions(self):
        def generateEndpointFunction(endpoint, name, requiredParams, optionalParams, url):
            env = Environment(loader=FileSystemLoader('templates'))
            template = env.get_template('endpointFunctionTemplate.txt')
            
            requiredParamsField = [p[1] for p in requiredParams]
            optionalParamsField = [p[1] + "=None" for p in optionalParams]
            
            """
            paramsField is inserted in the argument field, e.g.
            
            def someFunction({paramsField}):
            """
            paramsField = ',\n'.join(requiredParamsField + optionalParamsField)
            returnType = self.mappings[endpoint]
            
            # generates the code for one function
            render = template.render(name=name,
                                     paramsField=paramsField, 
                                     optionalParams=optionalParams, 
                                     url=url,
                                     returnType=returnType)
            
            return render
                
        functionStrings = []
        
        for endpoint, endpointInfo in self.endpoints.items():
            functionStrings.append(generateEndpointFunction(endpoint,
                                                            endpointInfo["name"],
                                                            endpointInfo["requiredParameters"],
                                                            endpointInfo["optionalParameters"],
                                                            self.serverURL + endpoint))
        
        
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('endpointFunctionsTemplate.txt')
        # mappings specified to know what to import
        mappings = set([c for c in self.mappings.values() if '[' not in c])
        
        # generates the contents of the generate endpoint functions file
        endpointFunctions = template.render(functionStrings=functionStrings, packageName=self.directory, mappings=mappings)    
        
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)     
            
        with open(f'{self.directory}/{self.outFile}', 'w') as f:
            f.write(endpointFunctions)   
        