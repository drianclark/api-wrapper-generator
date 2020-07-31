import json
from pprint import pprint
from helpers import constructEndpointFunctionName
from jinja2 import Template, Environment, FileSystemLoader

class TestsGenerator:
    
    # use config to find schema-class and endpoint-class mappings
    
    def __init__(self, packageName, config):
        self.packageName = packageName
        
        with open(config) as f:
            configObject = json.load(f)
            
        self.schemaMappings = configObject["classes"]
        self.endpointMappings = configObject["returnTypes"]
        
    def createEndpointFunctionsTests(self):
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
        for endpoint, returnType in self.endpointMappings.items():
            tests.append(createEndpointFunctionTest(endpoint, returnType))
            
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('endpointFunctionTestsTemplate.txt')
            
        render = template.render(tests=tests)
        
        with open(f'test_{self.packageName}.py', 'w') as f:
            f.write(render)
        
t = TestsGenerator('renders', 'wrapper_config.json')
        
     