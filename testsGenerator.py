import json
import re
from pprint import pprint
from helpers import constructEndpointFunctionName, getClassSchemaMappingsFromSpec, getObjectsRecursion, makeClassName, makeSingular, getSchemaFromEndpoint, getSchemaNameFromEndpoint, getNestedObjectsAccessorRecursion
from jinja2 import Template, Environment, FileSystemLoader

class TestsGenerator:
    
    # use config to find schema-class and endpoint-class mappings
    
    def __init__(self, packageName, config, spec):
        self.packageName = packageName
        
        with open(config) as f:
            configObject = json.load(f)
            
        self.schemaMappings = configObject["classes"]
        self.endpointMappings = configObject["returnTypes"]
        
        with open(spec) as f:
            jsonSpec = json.load(f)
            self.spec = jsonSpec
            
        paths = jsonSpec["paths"]
        schemas = jsonSpec["components"]["schemas"]
        
        self.nestedClasses = set()
        for schema, className in self.schemaMappings.items():
            for _class,_prop in getObjectsRecursion(schema, schemas[schema]):
                if '-' not in _class:
                    self.nestedClasses.add(makeSingular(makeClassName(_class)))
    
    def generateFunctionsTests(self):
        def generateFunctionTest(endpoint, returnType):
            env = Environment(loader=FileSystemLoader('templates'))
            testTemplate = env.get_template('endpointFunctionTestTemplate.txt')
                        
            # construct the function name using the endpoint path
            functionName = constructEndpointFunctionName(endpoint)
            returnFormat = 'list' if '[' in returnType else 'object'
            # removing brackets if present
            returnType = returnType[1:-1] if '[' in returnType else returnType
            
            schemaName = getSchemaNameFromEndpoint(endpoint, self.spec)
            schema = getSchemaFromEndpoint(endpoint, self.spec)
            
            # dictionary with key base class and value return type
            requiredProps = []
            optionalProps = []
            # list of dictionaries for each prop
            requiredNestedProps = []
            optionalNestedProps = []
            
            for _class,_prop in getObjectsRecursion(schemaName, schema):
                for propName, propInfo in _prop.items():
                    propObject = {}
                    propObject["attribute"] = propName
                    # if property is not nested
                    if '-' in _class:
                        try:
                            if propInfo['type'] == "array":
                                propObject["type"] = "list"
                                
                                itemsType = propInfo["items"]["type"]
                                
                                if itemsType == "object":
                                    propObject["contentType"] = makeClassName(propName)
                                elif itemsType == "string":
                                    propObject["contentType"] = "str"
                                elif itemsType == "number":
                                    propObject["contentType"] = "(int, float)"
                                    
                                if propInfo["items"].get("nullable") == False:
                                    requiredProps.append(propObject)
                                else:
                                    optionalProps.append(propObject)
                            else:
                                propType = propInfo["type"]
                            
                                if propType == "object":
                                    propObject["type"] = makeClassName(propName)
                                elif propType == "string":
                                    propObject["type"] = "str"
                                elif propType == "number":
                                    propObject["type"] = "(int, float)"
                                
                                if propInfo.get('nullable') == False:
                                    requiredProps.append(propObject)
                                else: 
                                    optionalProps.append(propObject)
                        except KeyError:
                            continue    

            for propAccessor, propInfo in getNestedObjectsAccessorRecursion(schemaName, schema):
                attribute = re.sub(r'[^a-zA-Z]', '', propAccessor) # e.g. stationmeasures
                existsParam = re.sub(r'[^a-zA-Z.]', '', propAccessor) # e.g. station.measures
                accessor = '.'.join(list(map(lambda x: x + '()', propAccessor.split('.')))) # e.g. station().measures()
                parentAccessor = accessor[0:accessor.rfind('.')] # drop everything after (including) the last '.' in the accessor
                parent = re.sub(r'[^a-zA-Z.]', '', parentAccessor)  # in station.measures, station is parent
                childAccessor = accessor[accessor.rfind('.')+1:]    # and measures is child
                child = re.sub(r'[^a-zA-Z.]', '', childAccessor)
                
                for propName, details in propInfo.items():
                    propObject = {}
                    try:
                        propObject['attribute'] = attribute
                        propObject['existsParam'] = existsParam
                        propObject['accessor'] = accessor
                        propObject['parentAccessor'] = parentAccessor
                        propObject['childAccessor'] = childAccessor
                        propObject['parent'] = parent
                        propObject['child'] = child
                        
                        if details['type'] == "array":
                            propObject['type'] = "list"
                            
                            itemsType = details["items"]["type"]
                                
                            if itemsType == "object":
                                propObject["contentType"] = makeClassName(propAccessor.split('.')[-1])
                            elif itemsType == "string":
                                propObject["contentType"] = "str"
                            elif itemsType == "number":
                                propObject["contentType"] = "(int, float)"


                            if details['items'].get('nullable') == False:
                                requiredNestedProps.append(propObject)
                            else:
                                optionalNestedProps.append(propObject)
                        else:
                            propType = details["type"]
                            
                            if propType == "object":
                                propObject["type"] = makeClassName(propAccessor.split('.')[-1])
                            elif propType == "string":
                                propObject["type"] = "str"
                            elif propType == "number":
                                propObject["type"] = "(int, float)"
                                
                            if details.get('nullable') == False:
                                requiredNestedProps.append(propObject)
                            else:
                                optionalNestedProps.append(propObject)

                    except KeyError:
                        continue
            
            render = testTemplate.render(functionName=functionName, 
                                     returnFormat=returnFormat, 
                                     returnType=returnType,
                                     requiredProps=requiredProps,
                                     optionalProps=optionalProps,
                                     requiredNestedProps=requiredNestedProps,
                                     optionalNestedProps=optionalNestedProps
                                    )
            
            return render

        tests = []
        classes = set()
        for endpoint, returnType in self.endpointMappings.items():
            if '{' not in endpoint:
                tests.append(generateFunctionTest(endpoint, returnType))
                returnType = returnType[1:-1] if '[' in returnType else returnType
                classes.add(returnType)
                
        imports = classes.union(self.nestedClasses)
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('endpointFunctionTestsTemplate.txt')
            
        render = template.render(tests=tests,
                                 imports=imports,
                                 packageName=self.packageName)
        
        # for each class, find which endpoint returns that class
        # execute that endpoint
        # test the result against the expected attributes and types
        
        with open(f'test_{self.packageName}.py', 'w') as f:
            f.write(render)
            
        
t = TestsGenerator('renders', 'wrapper_config.json', 'hydrology-oas.json')
        
     