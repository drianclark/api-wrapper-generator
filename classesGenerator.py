import json
import os
import inflect
from collections import defaultdict
from pprint import pprint
from jinja2 import Template, Environment, FileSystemLoader
from helpers import makeClassName, makeSingular, getObjectsRecursion

p = inflect.engine()
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
            
        # collecting the properties for each schema
        for schema, className in self.classes.items():
            for _class,_prop in getObjectsRecursion(schema, schemas[schema]):
                classProps[makeSingular(_class)].append(_prop)
        
        for schema, props in classProps.items():
            
            # BASE CLASS CASE
            try:
                className = self.classes[schema]
                
                # if there is a nested class of the same name,
                # include its properties to the base class props
                if className.lower() in classProps:
                    props += classProps[className.lower()]
                    
            # NESTED CLASS CLASE
            except KeyError:
                className = makeClassName(schema)
                # print(className)
                
                # if there is a nested class of the same name, ignore it
                # because we've already added its props to the base class
                if className in self.classes.values():
                    continue
            
            objectAttributes = set()
            for prop in props:
                for propName, propInfo in prop.items():
                    # if prop is a nested class, add it to objectAttributes
                    if makeSingular(propName) in list(classProps.keys()):
                        objectAttributes.add(makeSingular(propName))
            
            render = template.render(className=className, properties=props, objectAttributes=objectAttributes, packageName=self.directory)

            if not os.path.exists(self.directory):
                os.makedirs(self.directory)
            
            with open(f'{self.directory}/{className}.py', 'w') as f:
                f.write(render)
