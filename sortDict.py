import operator
#sorted representation of dictionary
trialDict = {}
trialDict['a'] = {'a':'sd', 'b':'we'}
trialDict['b'] = {'a':'re'}
trialDict['c'] = {'we':'we','e':'we','q':'e'}

mydict = {}
for i,j in trialDict.items():
    mydict[i] = len(j)

print sorted(mydict.items(), key=operator.itemgetter(1))
