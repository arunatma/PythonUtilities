# A certain encoding system converts a sentence to a coded word.  The coded 
# word contains predetermined set of characters.  
# Let us say if "w" "i" "n" are the only characters in the coded system (of 
# base 3), with "w" coded as 2, "i" as 1 and "n" as 0
# Then, the word "iii" will have an index of (1 * 3^2 + 1 * 3 + 1) = 13 
# A base can be any positive number other than 1
# 0 cannot occupy the first position in a coded word.
# Given a coded word, find the minimum index possible for the same (irrespective
# of any base)
# Example:
# Input: 11001      Output: 25
# Input: cats       Output: 75

#inList = [1, 2, 3, 4, 3]
inList = list("cats")
noDups = set(inList)

uniqueElements = list(noDups)
minBase = len(uniqueElements)
numElems = len(inList)

superScripts = range(0, numElems)

weights = [minBase**x for x in superScripts[::-1]]

indexer = dict()
for i in superScripts:
    if(i == 0):
        indexer[inList[i]] = 1
    else:
        if not inList[i] in indexer.keys():
            if (len(indexer.keys()) == 1):
                indexer[inList[i]] = 0
            else:
                indexer[inList[i]] = max(indexer.values()) + 1
        
positionValues = [indexer[key] for key in inList]

finalValue = sum ([x * y for x,y in zip(positionValues, weights)])
   
print inList
print indexer    
print minBase
print superScripts
print positionValues
print weights
 
print finalValue