from prance import ResolvingParser
from helpers import kebabToCamel, dotToCamel, makeFunctionName
from endpointFunctionsGenerator import EndpointFunctionsGenerator
from classesGenerator import ClassesGenerator
import json

class WrapperGenerator:
    
    def __init__(self, apiSpec, outFile, config):
        self.spec = apiSpec
        self.config = config
        self.outFile = outFile
        self.outputFolder = '/render'

        classesGenerator = ClassesGenerator(self.config, self.spec) 
        functionsGenerator = EndpointFunctionsGenerator(self.spec, self.outFile)
        
    