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
    return dotToCamel(kebabToCamel(s))
    
def makeFunctionName(s):
    onlyAlphabetic = re.sub(r'[^a-zA-Z ]', '', s)
    words = onlyAlphabetic.strip(".").split()
    
    capitalizedWords = [w.capitalize() for w in words]
    functionName = ''.join(capitalizedWords)
    
    return functionName