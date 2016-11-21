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

def getMinIndex(codeWord):
    # Minimum index is possible only if it starts with 1. Then assign numbers 
    # from 0, 2, 3... to different digits from left to right.  If a digit 
    # repeats, whose value is already assigned, use the same assigned value.
    numElems = len(codeWord)
    uniqueElements = list(set(codeWord))
    base = len(uniqueElements)
    exponents = range(0, numElems)
    weights = [base**x for x in exponents[::-1]]

    valueDict = dict()
    for i in exponents:
        if(i == 0):
            valueDict[codeWord[i]] = 1
        else:
            if not codeWord[i] in valueDict.keys():
                if (len(valueDict.keys()) == 1):
                    valueDict[codeWord[i]] = 0
                else:
                    valueDict[codeWord[i]] = max(valueDict.values()) + 1

    positionValues = [valueDict[key] for key in codeWord]

    minIndex = sum ([x * y for x,y in zip(positionValues, weights)])
       
    return(minIndex)
   
# Function Call   
index = getMinIndex("cats")
print (index)
