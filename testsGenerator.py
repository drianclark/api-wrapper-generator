import json

class TestsGenerator:
    
    # use config to find schema-class and endpoint-class mappings
    
    def __init__(self, packageName, config):
        self.packageName = packageName
        
        with open(config) as f:
            configObject = json.load(f)
            
        self.schemaMappings = configObject["classes"]
        self.endpointMappings = configObject["returnTypes"]
        
    def createEndpointFunctionTest(self):
        
     