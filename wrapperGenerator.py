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
        
        with open(self.spec) as f:
            jsonSpec = json.load(f)
                
        self.paths = jsonSpec["paths"]
        self.schemas = jsonSpec["components"]["schemas"]

        try:
            self.classesGenerator = ClassesGenerator(self.config, self.spec, self.packageName) 
            self.functionsGenerator = EndpointFunctionsGenerator(self.config, self.spec, f'{self.packageName}.py', self.packageName)
        
        except FileNotFoundError:
            self.initialiseConfigSetup()
        
    def initialiseConfigSetup(self):
        
        if os.path.exists(self.config):
            with open(self.config) as f:
                print(f"\nFound config file: {self.config}\n")
                pprint(json.load(f), indent=2)
                print()
                    
                configConfirmationQ = [
                    {
                        'type': 'list',
                        'name': 'config_confirmation',
                        'message': 'Would you like to use the configuration displayed above?',
                        'choices': ['Yes', 'No']
                    }
                ]
                    
                confirmed = prompt(configConfirmationQ)['config_confirmation']
                    
                if confirmed == 'No':
                    print('Entering configuration setup')
                    print()
                        
                    confirmOverwriteQ = [
                        {
                            'type': 'list',
                            'name': 'confirm_overwrite',
                            'message': f'WARNING: This will overwrite the configuration file {self.config}',
                            'choices': ['Proceed', 'Cancel']
                        }
                    ]
                        
                    confirmOverwrite = prompt(confirmOverwriteQ)['confirm_overwrite']
                        
                    if confirmOverwrite == 'Cancel':
                        return
                        
                    else:                    
                        self.configSetup()
                    
        else:
            print("\nConfig file not found. Initialising configuration setup\n")
            self.configSetup()

    def configSetup(self):        
        def baseClassesEditMenu(baseClasses):
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
        
        def endpointClassMappingMenu(baseClasses, endpointClassMappings):
            endpointClassChoices = [f'{endpoint}: {classMapping}' for endpoint, classMapping 
                                    in endpointClassMappings.items()]
            
            endpointClassChoices += [Separator(), 'Finish']
            
            endpointClassMappingQuestion = [
                {
                    'type': 'list',
                    'name': 'endpointChoice',
                    'message': 'Here, you can edit the return types for each endpoint',
                    'choices': endpointClassChoices
                }   
            ]
            
            endpointChoice = prompt(endpointClassMappingQuestion)['endpointChoice'].split(':')[0]
            if endpointChoice == 'Finish':
                return 'Finish'
            
            returnTypeQuestion = [
                {
                    'type': 'list',
                    'name': 'return_type',
                    'message': 'Does this endpoint return an array or a single object?',
                    'choices': ['array', 'object', Separator(), 'Cancel']
                }   
            ]
            
            returnType = prompt(returnTypeQuestion)['return_type']
            
            if returnType == 'Cancel':
                return
            
            classMappingQuestion = [
                {
                    'type': 'list',
                    'name': 'class_mapping',
                    'message': 'To which class does this endpoint map to?',
                    'choices': list(baseClasses.keys()) + [Separator(), 'Cancel']
                }   
            ]
            
            classMapping = prompt(classMappingQuestion)['class_mapping']

            if classMapping == 'Cancel':
                return
            
            newClassMapping = classMapping if returnType == 'object' else f'[{classMapping}]'
            endpointClassMappings[endpointChoice] = newClassMapping
            
            print(endpointClassMappings)
            
        def showBaseClasses(baseClasses):
            print('---------------------------------')
            print('Base Classes\n')
                    
            for className, schemaName in baseClasses.items():
                print(f'{className}: {schemaName}')
                
            print()
        
        def addBaseClassMenu(baseClasses, schemaNames):
            classNameQuestion = [
                {
                    'type': 'input',
                    'name': 'className',
                    'message': 'What would you like to name the new base class? Type c to cancel.'
                }
            ]
            
            className = prompt(classNameQuestion)['className']
            
            if className == 'c':
                return
            
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
            
        def renameBaseClassMenu(baseClasses, renameMap):
            baseClassChoice = [
                {
                    'type': 'list',
                    'name': 'base_class',
                    'message': 'Which class would you like to rename?',
                    'choices': list(baseClasses.keys()) + [Separator(), 'Cancel']
                }
            ]
            
            classToRename = prompt(baseClassChoice)['base_class']
            
            if classToRename == 'Cancel':
                return
            
            newNameQuestion = [
                {
                    'type': 'input',
                    'name': 'new_name',
                    'message': f'What would you like to rename class {classToRename} to?'
                }
            ]
            
            newName = prompt(newNameQuestion)['new_name']            
            baseClasses[newName] = baseClasses[classToRename]
            
            # if renaming a class that's already been renamed,
            # the key in renameMap should remain as the original class name
            # instead of making a new entry
            if classToRename in renameMap.values():
                for original, rename in renameMap.items():
                    if classToRename == rename:
                        renameMap[original] = newName    
            else:
                renameMap[classToRename] = newName
                
            if newName != classToRename:
                del baseClasses[classToRename]
            
        def remapBaseClassMenu(baseClasses, schemaNames):
            classToRemapQuestion = [
                {
                    'type': 'list',
                    'name': 'remap_class',
                    'message': 'Which class would you like to change the mapping for?',
                    'choices': list(baseClasses.keys()) + [Separator(), 'Cancel']
                }
            ]
                
            classToRemap = prompt(classToRemapQuestion)['remap_class']
            
            if classToRemap == 'Cancel':
                return
                
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
                    'choices': list(baseClasses.keys()) + [Separator(), 'Cancel']
                }
            ]
            
            classToDelete = prompt(baseClassChoice)['delete_class']
            
            if classToDelete == 'Cancel':
                return
            
            del baseClasses[classToDelete]
            
        def showNestedClasses(nestedClasses):
            print('---------------------------------')
            print("Auto detected nested classes:\n")
            
            for className, schemaName in nestedClasses.items():
                print(f'{className}: {schemaName}')
            
            print()
                
            proceed = [
                {
                    'type': 'list',
                    'message': '',
                    'name': 'continue',
                    'choices': ['Proceed']
                }
            ]

            proceedConfirmation = prompt(proceed)['continue']
            
        # auto detect schema-class mappings and schema names
        classMappings = self.getClassSchemaMappingsFromSpec()
        schemaNames = self.getSchemaNameFromSpec()        
        
        # base classes are the classes with a corresponding component schema (not nested within one)
        baseClasses = {}
        
        # nested classes are those found within the base classes
        nestedClasses = {}
        
        # keep track of renamed classes for future reference
        renameMap = {}
        
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
            
        # auto detect endpoint-class mappings
        endpointClassMappings = self.getEndpointClassMappingsFromSpec(baseClasses, renameMap)
                
        while True:
            action = baseClassesEditMenu(baseClasses)
            
            if action == 'Proceed':
                break
            
            elif action == 'Add a base class':
                addBaseClassMenu(baseClasses, schemaNames)
                
            elif action == 'Rename a base class':
                renameBaseClassMenu(baseClasses, renameMap)
                print(renameMap)
                
            elif action == 'Delete a base class':
                deleteBaseClassMenu(baseClasses)
                
            elif action == 'Change a base class mapping':
                remapBaseClassMenu(baseClasses, schemaNames)
                
            showBaseClasses(baseClasses)
            
        showNestedClasses(nestedClasses)
        
        while True:
            action = endpointClassMappingMenu(baseClasses, endpointClassMappings)
            
            if action == 'Finish':
                break
        
        print("Generating config file")
        self.writeConfigurationToFile(baseClasses, endpointClassMappings)
        print(f"Generated config file: {self.config}")
        
    def getClassSchemaMappingsFromSpec(self):
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
            if "?_view" not in pathName and '{' not in pathName:
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
    
    def getEndpointClassMappingsFromSpec(self, baseClasses, renameMap):
        endpointClassMappings = {}
        
        for pathName, pathInfo in self.paths.items():
            if "?_view" not in pathName:
                metadataType = pathInfo["get"]["responses"]["200"]["content"]["application/json"]["schema"]["properties"]["meta"]["$ref"]
                returnType = 'array' if 'list' in metadataType else 'object'
                
                noLeadingSlash = pathName[1:]
                splitBySlash = noLeadingSlash.split("/")
                className = makeClassName([s for s in splitBySlash if '{' not in s][-1])
                
                # if this class name has been renamed, change it to what it's been renamed as
                try:
                    className = renameMap[className]
                except KeyError:
                    pass
                                
                mapping = className if returnType == 'object' else f'[{className}]'
                endpointClassMappings[pathName] = mapping
        
        return endpointClassMappings
    
    def writeConfigurationToFile(self, baseClasses, endpointClassMappings):
        config = {
            'classes': baseClasses,
            'returnTypes': endpointClassMappings
        }
                
        with open(self.config, 'w') as f:
            json.dump(config, f, indent=2)
                                    
    def generateWrapper(self):
        
        # create output directory for package
        if not os.path.exists(self.packageName):
            os.makedirs(self.packageName)
            
        # create __init__.py
        f = open(f'{self.packageName}/__init__.py','w+')
        f.close()
            
        self.classesGenerator.generateClasses()
        self.functionsGenerator.generateEndpointFunctions()
        
w = WrapperGenerator('hydrology-oas.json')
                
if __name__ == '__main__':
    w.initialiseConfigSetup()
    
    