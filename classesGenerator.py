import json
import os
from collections import defaultdict
from pprint import pprint
from jinja2 import Template, Environment, FileSystemLoader
from helpers import makeClassName

class ClassesGenerator:
    def __init__(self, config, spec, directory='renders'):
        self.spec = spec
        self.directory = directory
        
        with open(config) as f:
            self.classes = json.load(f)["classes"]
            # print(self.classes)
                
    def generateClasses(self):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('classTemplate.txt')
        
        classProps = defaultdict(list)
        
        with open(self.spec) as f:
            schemas = json.load(f)["components"]["schemas"]
            
    # print(schemas)
        for schema, className in self.classes.items():
        # access the schema in the spec
            for _class,_prop in getObjectsRecursion(schema, schemas[schema]):
                classProps[_class].append(_prop)
                
        # pprint(classProps, indent=2)
                    
        for schema, props in classProps.items():
            try:
                className = self.classes[schema]
                
            except KeyError:
                className = makeClassName(schema)
                print(f'{schema} not in configuration file. Will name class {className}.')
                
            objectAttributes = set()
            for prop in props:
                for propName, propInfo in prop.items():
                    if propName in list(classProps.keys()):
                        objectAttributes.add(propName)
            
                    
            render = template.render(className=className, properties=props, objectAttributes=objectAttributes, packageName=self.directory)

            if not os.path.exists(self.directory):
                os.makedirs(self.directory)
            
            with open(f'{self.directory}/{className}.py', 'w') as f:
                f.write(render)

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
                
