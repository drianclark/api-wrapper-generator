def kebabToCamel(s):
    iterchars = iter(s.split("-"))
    result = s.split("-")[0]
    next(iterchars)
    
    for word in iterchars:
        result += word.capitalize()
    
    return result

def dotToCamel(s):
    if "." not in s:
        return s
    
    splitString = (s.split(".", 1))
    if splitString[0] in splitString[1]:
        return splitString[1]
    else:
        return splitString[0] + splitString[1][0].upper() + splitString[1][1:]
    
def makeFunctionName(s):
    words = s.strip(".").split()
    capitalizedWords = [w.capitalize() for w in words]
    functionName = ''.join(capitalizedWords)
    
    return functionName