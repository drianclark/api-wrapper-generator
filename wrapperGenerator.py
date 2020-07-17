import os
from endpointFunctionsGenerator import EndpointFunctionsGenerator
from classesGenerator import ClassesGenerator

class WrapperGenerator:
    
    def __init__(self, apiSpec, config, packageName='renders'):
        self.spec = apiSpec
        self.config = config
        self.packageName = packageName

        self.classesGenerator = ClassesGenerator(self.config, self.spec, self.packageName) 
        self.functionsGenerator = EndpointFunctionsGenerator(self.config, self.spec, f'{self.packageName}.py', self.packageName)

    def generateWrapper(self):
        
        # create output directory for package
        if not os.path.exists(self.packageName):
            os.makedirs(self.packageName)
            
        # create __init__.py
        f = open(f'{self.packageName}/__init__.py','w+')
        f.close()
            
        self.classesGenerator.generateClasses()
        self.functionsGenerator.generateEndpointFunctions()
        
w = WrapperGenerator('hydrology-oas.json', 'classes_conf.json')
                
    
    