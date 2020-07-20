import json
import os
from collections import defaultdict
from pprint import pprint
from jinja2 import Template, Environment, FileSystemLoader
from helpers import makeClassName

class ClassesGenerator:
    def __init__(self, spec, directory='renders'):
        self.spec = spec
        self.directory = directory
                
    def generateClasses(self):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('classTemplate.txt')
        
        classProps = defaultdict(list)
        
        with open(self.spec) as f:
            jsonSpec = json.load(f)
            
        paths = jsonSpec["paths"]
        schemas = jsonSpec["components"]["schemas"]
            
        # collecting properties of each schema, including nested object properties
        for schema, schemaInfo in schemas.items():
            if "-default" in schema:
                for _class,_prop in getObjectsRecursion(schema, schemaInfo):
                    classProps[_class].append(_prop)
                
        # pprint(classProps, indent=2)
        
        # collect schema names using endpoint paths
        for pathName, info in paths.items():
            if "?_view" not in pathName:
                noLeadingSlash = pathName[1:]
                # this contains all the strings between slashes
                splitBySlash = noLeadingSlash.split("/")
                urlParams = [s for s in splitBySlash if '{' in s]
                nonParams = [s for s in splitBySlash if '{' not in s]
                
                returnType = info["get"]["responses"]["200"]["content"]["application/json"]["schema"]["properties"]["items"]["type"]
                returnObjectType = info["get"]["responses"]["200"]["content"]["application/json"]["schema"]["properties"]["items"]["items"]["$ref"].split("/")[-1]
                
                print(returnObjectType)
                
        # for schema, props in classProps.items():
        #     try:
        #         className = self.classes[schema]
                
        #     except KeyError:
        #         print(f'{schema} not in configuration file. Will name class {className}.')
        #         className = makeClassName(schema)
                
        #     objectAttributes = set()
        #     for prop in props:
        #         for propName, propInfo in prop.items():
        #             if propName in list(classProps.keys()):
        #                 objectAttributes.add(propName)
            
        #     # print(objectAttributes)
                    
        #     render = template.render(className=className, properties=props, objectAttributes=objectAttributes, packageName=self.directory)

        #     if not os.path.exists(self.directory):
        #         os.makedirs(self.directory)
            
        #     with open(f'{self.directory}/{className}.py', 'w') as f:
        #         f.write(render)

            # for prop, propData in properties.items():
            #     if "allOf" in propData:
            #         for 
            #for property in properties
                # recursively check
                    # if it has "allOf"
                    # then see if type is object
                    #   then create a class for object
                    #   make sure to add the correct class constructor calls in the 
                    #   class containing the object
                    #   as well as add the import statements
            

c = ClassesGenerator("hydrology-oas.json")


def getObjectsRecursion(key,dictionary):
    for item in dictionary["allOf"]:
        for k,v in item.items():
            if k == "properties":
                for k1,v1 in v.items():
                    yield (key, {k1:v1})
                    # print(key)
                    # print({k1:v1})
                    # print()
                    # if v1 is an object, get its properties to make a class out of it later
                    if v1.get("allOf") != None:
                        for k2,v2 in getObjectsRecursion(k1, v1):
                            # print(k2)
                            # print(v2)
                            # print()
                            yield (k2,v2)
                break
                
