import json
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
            
            # test all the nested classes as well
            schemaName = getSchemaNameFromEndpoint(endpoint, self.spec)
            schema = getSchemaFromEndpoint(endpoint, self.spec)
            
            requiredProps = set()

            # dictionary with key base class and 
            nestedProps = set()
            
            for _class,_prop in getObjectsRecursion(schemaName, schema):
                for propName, propInfo in _prop.items():
                    # if property is not nested
                    if '-' in _class:
                        try:
                            if propInfo['type'] == "array":
                                if propInfo['items'].get('nullable') == False:
                                    requiredProps.add(propName)
                            else:
                                if propInfo.get('nullable') == False:
                                    requiredProps.add(propName)
                        except KeyError:
                            continue    

            for propAccessor, propInfo in getNestedObjectsAccessorRecursion(schemaName, schema):
                for propName, details in propInfo.items():
                    try:
                        if details['type'] == "array":
                            if details['items'].get('nullable') == False:
                                nestedProps.add(propAccessor)
                        else:
                            if propInfo.get('nullable') == False:
                                nestedProps.add(propAccessor)
                    except KeyError:
                        continue

            # turn nestedProps accessors to getter function calls
            splitProps = [ accessor.split('.') for accessor in nestedProps ]
            toGetters = [ list(map(lambda x: x + '()', accessorList)) for accessorList in splitProps ]
            nestedProps = [ '.'.join(gettersList) for gettersList in toGetters ]
        
            print(nestedProps)
            
            render = testTemplate.render(functionName=functionName, 
                                     returnFormat=returnFormat, 
                                     returnType=returnType,
                                     requiredProps=requiredProps)
            
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
        
     