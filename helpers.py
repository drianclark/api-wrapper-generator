import re

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
    camel = makeParamName(s)
    pascal = camel[0].upper() + camel[1:]
    
    return pascal

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