import re
import inflect

def kebabToCamel(s):
    iterchars = iter(s.split("-"))
    result = s.split("-")[0]
    next(iterchars)
    
    for word in iterchars:
        result += word[0].upper() + word[1:]
    
    return result

def dotToCamel(s):
    if "." not in s:
        return s
    
    splitString = (s.split("."))
    camelCaseArray = [word[0].upper() + word[1:] if index > 0 else word for index, word in enumerate(splitString)]
    
    if splitString[0] in splitString[1]:
        del splitString[0]
    
    return ''.join(camelCaseArray)

def makeParamName(s):
    return dotToCamel(kebabToCamel(s)).strip('_')
    
def makeFunctionName(s):
    onlyAlphabetic = re.sub(r'[^a-zA-Z ]', '', s)
    words = onlyAlphabetic.strip(".").split()
    
    capitalizedWords = [w.capitalize() for w in words]
    functionName = ''.join(capitalizedWords)
    
    return functionName

def makeClassName(s):
    camel = makeParamName(makeSingular(s))
    pascal = camel[0].upper() + camel[1:]
    
    return pascal

def getObjectsRecursion(key,dictionary):
    for item in dictionary["allOf"]:
        for k,v in item.items():
            if k == "properties":
                for k1,v1 in v.items():
                    yield (key, {k1:v1})
                    # k1:v1 is a property:value pair
                    # if v1 is an object, get its properties to make a class out of it later
                    if v1.get("allOf") != None:
                        for k2,v2 in getObjectsRecursion(k1, v1):
                            yield (k2,v2)
                break
            
def getNestedObjectsAccessorRecursion(key,dictionary):
    for item in dictionary["allOf"]:
        for k,v in item.items():
            if k == "properties":
                for k1,v1 in v.items():
                    # if this prop is already nested within another
                    if '-' not in key:
                        yield (f'{key}.{k1}', {k1:v1})
                        # if v1 is a nested object with more objects within it
                    if v1.get("allOf") != None:
                        if '-' not in key:
                            for k2,v2 in getNestedObjectsAccessorRecursion(f'{key}.{k1}', v1):
                                yield (k2,v2) 
                        else: 
                            for k2,v2 in getNestedObjectsAccessorRecursion(k1, v1):
                                yield (k2,v2)
                break
            
def makeSingular(s):
    p = inflect.engine()
    
    singular = not bool(p.singular_noun(s))    
    singularVersion = p.singular_noun(s) if not singular else s
    
    return singularVersion

def constructEndpointFunctionName(endpointPath):
    noLeadingSlash = endpointPath[1:]
                        
    # this contains all the strings between slashes
    splitBySlash = noLeadingSlash.split("/")
    urlParams = [makeClassName(s[1:-1]) for s in splitBySlash if '{' in s]
    nonParams = [s for s in splitBySlash if '{' not in s]
                        
    functionName = nonParams[-1]
                        
    if len(urlParams) > 0:
        functionName += 'By'
        functionName += 'And'.join(urlParams)
        
    return functionName

def getClassSchemaMappingsFromSpec(paths, schemas):
    classes = {}
                            
    # collect and construct base class names using endpoint paths
    for pathName, info in paths.items():
        if "?_view" not in pathName and '{' not in pathName:
            noLeadingSlash = pathName[1:]
                                
            # this contains all the strings between slashes
            splitBySlash = noLeadingSlash.split("/")
            urlParams = [makeClassName(s[1:-1]) for s in splitBySlash if '{' in s]
            nonParams = [s for s in splitBySlash if '{' not in s]
                                
            returnObjectType = info["get"]["responses"]["200"]["content"]["application/json"]["schema"]["properties"]["items"]["items"]["$ref"].split("/")[-1]
            className = makeClassName(nonParams[-1])
            className = makeSingular(className)
                    
            classes[returnObjectType] = className
                    
    # collecting nested attributes
    for schema, schemaInfo in schemas.items():
        if "-default" in schema:
            for _class,_prop in getObjectsRecursion(schema, schemaInfo):
                # only get nested object attributes (they don't have dashes)
                if '-' not in _class:
                    className = makeSingular(makeClassName(_class))
                            
                    # making sure we don't overwrite base classes
                    # with nested ones of the same name
                    if className not in classes:
                        classes[_class] = makeSingular(className)
                                
    return classes

def getSchemaFromEndpoint(endpoint, spec):
    schemaRef = spec["paths"][endpoint]["get"]["responses"]["200"]["content"]["application/json"]["schema"]["properties"]["items"]["items"]["$ref"]
    schemaName = schemaRef.split('/')[-1]
    
    schema = spec["components"]["schemas"][schemaName]
    
    return schema

def getSchemaNameFromEndpoint(endpoint, spec):
    schemaRef = spec["paths"][endpoint]["get"]["responses"]["200"]["content"]["application/json"]["schema"]["properties"]["items"]["items"]["$ref"]
    schemaName = schemaRef.split('/')[-1]
    
    return schemaName
