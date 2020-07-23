from __future__ import print_function, unicode_literals
import json
import os
from PyInquirer import prompt, print_json
from collections import defaultdict
from pprint import pprint
from jinja2 import Template, Environment, FileSystemLoader
from helpers import makeClassName, getObjectsRecursion

class ClassesGenerator:
    def __init__(self, spec, directory='renders', config='wrapper_config.json'):
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
                    
            
        # collect and construct class names using endpoint paths
        for pathName, info in paths.items():
            if "?_view" not in pathName:
                noLeadingSlash = pathName[1:]
                    
                # this contains all the strings between slashes
                splitBySlash = noLeadingSlash.split("/")
                urlParams = [makeClassName(s[1:-1]) for s in splitBySlash if '{' in s]
                nonParams = [s for s in splitBySlash if '{' not in s]
                    
                returnType = info["get"]["responses"]["200"]["content"]["application/json"]["schema"]["properties"]["items"]["type"]
                returnObjectType = info["get"]["responses"]["200"]["content"]["application/json"]["schema"]["properties"]["items"]["items"]["$ref"].split("/")[-1]
                    
                className = nonParams[-1]
                        
                print(className)
            
        for schema,className in self.classes.items():
        # access the schema in the spec
            for _class,_prop in getObjectsRecursion(schema, schemas[schema]):
                classProps[_class].append(_prop)
                
        for schema, props in classProps.items():
            try:
                className = self.classes[schema]
                
            except KeyError:
                print(f'{schema} not in configuration file. Will name class {className}.')
                className = makeClassName(schema)
                
            objectAttributes = set()
            for prop in props:
                for propName, propInfo in prop.items():
                    if propName in list(classProps.keys()):
                        objectAttributes.add(propName)
            
            # print(objectAttributes)
                    
            render = template.render(className=className, properties=props, objectAttributes=objectAttributes, packageName=self.directory)

            if not os.path.exists(self.directory):
                os.makedirs(self.directory)
            
            with open(f'{self.directory}/{className}.py', 'w') as f:
                f.write(render)

c = ClassesGenerator("classes_conf.json", "hydrology-oas.json")