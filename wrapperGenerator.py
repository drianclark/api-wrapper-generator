import os
import json
from endpointFunctionsGenerator import EndpointFunctionsGenerator
from classesGenerator import ClassesGenerator
from helpers import getObjectsRecursion, makeClassName
from pprint import pprint
from PyInquirer import prompt, print_json, Separator

class WrapperGenerator:
    
    def __init__(self, apiSpec, packageName='renders', config='wrapper_config.json'):
        self.spec = apiSpec
        self.config = config
        self.packageName = packageName

        # self.classesGenerator = ClassesGenerator(self.config, self.spec, self.packageName) 
        # self.functionsGenerator = EndpointFunctionsGenerator(self.config, self.spec, f'{self.packageName}.py', self.packageName)
        with open(self.spec) as f:
            jsonSpec = json.load(f)
                
        self.paths = jsonSpec["paths"]
        self.schemas = jsonSpec["components"]["schemas"]
        
        if os.path.exists(config):
            print("config exists")
            with open(self.config) as f:
                print(f"Found config file: {config}")
                self.classes = json.load(f)["classes"]
        else:
            print("\nConfig file not found. Initialising configuration setup\n")
            self.configSetup()

    def configSetup(self):
        def showBaseClasses(baseClasses):
            print('---------------------------------')
            print('Base Classes\n')
                
            for className, schemaName in baseClasses.items():
                print(f'{className}: {schemaName}')
            
            print()
        
        def mainMenu(baseClasses):
            actionQs = [
                {
                    'type': 'list',
                    'name': 'actions',
                    'message': 'What would you like to do?',
                    'choices': [
                        'Add a base class',
                        'Rename a base class',
                        'Change a base class mapping',
                        'Delete a base class',
                        Separator(),
                        'Proceed'
                    ]
                }
            ]
            
            # if there are no base classes, only allow the option of adding one
            if len(baseClasses) == 0:
                actionQs[0]['choices'] = ['Add a base class']

            action = prompt(actionQs)["actions"]
            return action
        
        def addBaseClassMenu(baseClasses, schemaNames):
            classNameQuestion = [
                {
                    'type': 'input',
                    'name': 'className',
                    'message': 'What would you like to name the new base class?'
                }
            ]
            
            className = prompt(classNameQuestion)['className']
            
            schemaMappingQuestion = [
                {
                    'type': 'list',
                    'name': 'schema_mapping',
                    'message': 'Which schema maps to this class?',
                    'choices': schemaNames
                }   
            ]
            
            schema = prompt(schemaMappingQuestion)['schema_mapping']
            
            baseClasses[className] = schema
            
        def renameBaseClassMenu(baseClasses):
            baseClassChoice = [
                {
                    'type': 'list',
                    'name': 'base_class',
                    'message': 'Which class would you like to rename?',
                    'choices': baseClasses
                }
            ]
            
            classToRename = prompt(baseClassChoice)['base_class']
            
            newNameQuestion = [
                {
                    'type': 'input',
                    'name': 'new_name',
                    'message': f'What would you like to rename class {classToRename} to?'
                }
            ]
            
            newName = prompt(newNameQuestion)['new_name']
            
            baseClasses[newName] = baseClasses[classToRename]
            del baseClasses[classToRename]
            
        def remapBaseClassMenu(baseClasses, schemaNames):
            classToRemapQuestion = [
                {
                    'type': 'list',
                    'name': 'remap_class',
                    'message': 'Which class would you like to change the mapping for?',
                    'choices': baseClasses
                }
            ]
                
            classToRemap = prompt(classToRemapQuestion)['remap_class']
                
            schemaMappingQuestion = [
                {
                    'type': 'list',
                    'name': 'schema_mapping',
                    'message': 'Which schema maps to this class?',
                    'choices': schemaNames
                }   
            ]
                
            schema = prompt(schemaMappingQuestion)['schema_mapping']
                
            baseClasses[classToRemap] = schema
            
        def deleteBaseClassMenu(baseClasses):
            baseClassChoice = [
                {
                    'type': 'list',
                    'name': 'delete_class',
                    'message': 'Which class would you like to delete?',
                    'choices': baseClasses
                }
            ]
            
            classToDelete = prompt(baseClassChoice)['delete_class']
            
            del baseClasses[classToDelete]
            
        # get auto detected schema-class mappings
        classMappings = self.getClassMappingsFromSpec()
        schemaNames = self.getSchemaNameFromSpec()
        
        # base classes are the classes with a corresponding component schema (not nested within one)
        baseClasses = {}
        
        # nested classes are those found within the base classes
        nestedClasses = {}
        
        for className, schemaName in classMappings.items():
            if '-' in schemaName:
                baseClasses[className] = schemaName
            else:
                nestedClasses[className] = schemaName

                
        if len(baseClasses) == 0:
            print('No base classes detected')
            
        else:
            print('---------------------------------')
            print('Auto-detected base classes: \n')
            
            for className, schemaName in baseClasses.items():
                print(f'{className}: {schemaName}')
                
            print()
                
        while True:
            action = mainMenu(baseClasses)
            
            if action == 'Proceed':
                break
            
            elif action == 'Add a base class':
                addBaseClassMenu(baseClasses, schemaNames)
                
            elif action == 'Rename a base class':
                renameBaseClassMenu(baseClasses)
                
            elif action == 'Delete a base class':
                deleteBaseClassMenu(baseClasses)
                
            elif action == 'Change a base class mapping':
                remapBaseClassMenu(baseClasses, schemaNames)
                
            showBaseClasses(baseClasses)
            
        
    def getClassMappingsFromSpec(self):
        classes = {}
        
        # collecting properties of each schema, including nested object properties
        for schema, schemaInfo in self.schemas.items():
            if "-default" in schema:
                for _class,_prop in getObjectsRecursion(schema, schemaInfo):
                    # only get nested object attributes (they don't have dashes)
                    if '-' not in _class:
                        classes[makeClassName(_class)] = _class
                        
        # collect and construct class names using endpoint paths
        for pathName, info in self.paths.items():
            if "?_view" not in pathName:
                noLeadingSlash = pathName[1:]
                            
                # this contains all the strings between slashes
                splitBySlash = noLeadingSlash.split("/")
                urlParams = [makeClassName(s[1:-1]) for s in splitBySlash if '{' in s]
                nonParams = [s for s in splitBySlash if '{' not in s]
                            
                returnObjectType = info["get"]["responses"]["200"]["content"]["application/json"]["schema"]["properties"]["items"]["items"]["$ref"].split("/")[-1]
                className = makeClassName(nonParams[-1])
                
                classes[className] = returnObjectType
                
        return classes
    
    def getSchemaNameFromSpec(self):
        # get schema names with '-' in them
        schemaNames = list(filter(lambda s: '-' in s, self.schemas.keys()))
            
        return schemaNames
                                    
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
                
    
    