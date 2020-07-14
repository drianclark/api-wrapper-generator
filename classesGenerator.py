import json
from collections import defaultdict
from pprint import pprint
from jinja2 import Template, Environment, FileSystemLoader

class ClassesGenerator:
    def __init__(self, config, spec):
        self.spec = spec
        
        with open(config) as f:
            self.classes = json.load(f)["classes"]
            print(self.classes)
            
    
                
    def generateClasses(self):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('classTemplate.txt')
        
        classProps = defaultdict(list)
        
        with open(self.spec) as f:
            schemas = json.load(f)["components"]["schemas"]
            
        # print(schemas)
        for entry in self.classes:
            for schema,className in entry.items():
            # access the schema in the spec
                for _class,_prop in getObjectsRecursion(schema, schemas[schema]):
                    classProps[_class].append(_prop)
                    print(_class)
                    print()
                    pprint(_prop, indent=2)
        
        # pprint(classProps, indent=2)
                # allOf = schemas[schema]["allOf"]
                # for item in allOf:
                #     for k,v in item.items():
                #         if k == "properties":
                #             properties = v
                #             break
                        
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
                
                # render = template.render(className=className, properties=properties)
                # for k,v in properties.items():
                #     for k1,v1 in id_generator(v):
                #         if k1 == "type":
                #             yield k
                #         elif isinstance(v1, dict):
                #             for id_val in id_generator(v1):
                #                 yield id_val
                    
                # with open(f'{className}.py', 'w') as f:
                #     f.write(render)
                # print(json.dumps(properties, indent=2))
            

c = ClassesGenerator("classes_conf.json", "hydrology-oas.json")


def getObjectsRecursion(key,dictionary):
    for item in dictionary["allOf"]:
        for k,v in item.items():
            if k == "properties":
                for k1,v1 in v.items():
                    yield (key, v)
                    # if v1 is an object, get its properties to make a class out of it later
                    if v1.get("allOf") != None:
                        for k2,v2 in getObjectsRecursion(k1, v1):
                            yield (k2,v2)

                        
                break
                
                
with open("hydrology-oas.json") as f:
    schemas = json.load(f)["components"]["schemas"]