import json
from pprint import pprint
from helpers import constructEndpointFunctionName, getClassSchemaMappingsFromSpec, getObjectsRecursion, makeClassName, makeSingular
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
            
        paths = jsonSpec["paths"]
        schemas = jsonSpec["components"]["schemas"]
        
        self.nestedClasses = set()
        for schema, className in self.schemaMappings.items():
            for _class,_prop in getObjectsRecursion(schema, schemas[schema]):
                if '-' not in _class:
                    self.nestedClasses.add(makeSingular(makeClassName(_class)))
                
        print(self.nestedClasses)
        
    def generateFunctionsTests(self):
        def createEndpointFunctionTest(endpoint, returnType):
            env = Environment(loader=FileSystemLoader('templates'))
            template = env.get_template('endpointFunctionTestTemplate.txt')
                        
            # construct the function name using the endpoint path
            functionName = constructEndpointFunctionName(endpoint)
            returnFormat = 'list' if '[' in returnType else 'object'
            # removing brackets if present
            returnType = returnType[1:-1] if '[' in returnType else returnType
            
            render = template.render(functionName=functionName, 
                                     returnFormat=returnFormat, 
                                     returnType=returnType)
            
            return render

        tests = []
        classes = set()
        for endpoint, returnType in self.endpointMappings.items():
            if '{' not in endpoint:
                tests.append(createEndpointFunctionTest(endpoint, returnType))
                returnType = returnType[1:-1] if '[' in returnType else returnType
                classes.add(returnType)
                
        imports = classes.union(self.nestedClasses)
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('endpointFunctionTestsTemplate.txt')
            
        render = template.render(tests=tests,
                                 imports=imports,
                                 packageName=self.packageName)
    
        with open(f'test_{self.packageName}.py', 'w') as f:
            f.write(render)
        
t = TestsGenerator('renders', 'wrapper_config.json', 'hydrology-oas.json')
        
     