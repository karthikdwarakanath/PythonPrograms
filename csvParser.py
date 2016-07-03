# John,Smith,john.smith@gmail.com,Los Angeles,1
# Jane,Roberts,janer@msn.com,"San Francisco, CA",0
# "Alexandra ""Alex""",Menendez,alex.menendez@gmail.com,Miami,1
# """Alexandra Alex"""
# John|Smith|john.smith@gmail.com|Los Angeles|1
# Jane|Roberts|janer@msn.com|San Francisco, CA|0
# Alexandra "Alex"|Menendez|alex.menendez@gmail.com|Miami|1
# "Alexandra Alex"
#

def csvParser(inputString):
    i = 0
    n = len(inputString)
    ignoreComma = False
    resultString = ''
    while i < n:
        if inputString[i] == ',' and not ignoreComma:
            resultString  += '|'
            i = i+1
        elif inputString[i] == '\"' and not ignoreComma:
            if inputString[i+1] != '\"':
                ignoreComma = True
                i = i+1
            else:
                i = i+1
        elif inputString[i] == '\"' and ignoreComma:
            ignoreComma = False
            i = i+1
        else:
            resultString += inputString[i]
            i = i+1
    return resultString

print csvParser('John,Smith,john.smith@gmail.com,Los Angeles,1')
print csvParser('Jane,Roberts,janer@msn.com,"San Francisco, CA",0')
print csvParser('"Alexandra ""Alex""",Menendez,alex.menendez@gmail.com,Miami,1')
