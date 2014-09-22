# This pyton file has functions to change the names of variables in source file

###############################################################################
# camelCase
# CamelCase
# spinal-case or lisp-case or kebab-case
# Train-Case
# snake_case
# SNAKE_CASE
# ALLCAPS
# allsmalls
###############################################################################

def getFromLowerCamel(theWord):
    """ Return a list of lower cased words, given a lowerCamel word """
    wordsAndSpaces = re.split(r"([a-z][a-z0-9]+|[A-Z][a-z0-9]+)", theWord)
    mixedWords = filter(lambda x: x != '', wordsAndSpaces)
    lowerCasedList = map(lambda x: x.lower(), mixedWords)
    return lowerCasedList

def getFromUpperCamel(theWord):
    """ Return a list of lower cased words, given an UpperCamel word """
    wordsAndSpaces = re.split(r"([A-Z][a-z0-9]+|[A-Z][a-z0-9]+)", theWord)
    mixedWords = filter(lambda x: x != '', wordsAndSpaces)
    lowerCasedList = map(lambda x: x.lower(), mixedWords)
    return lowerCasedList

def getFromSpinal(theWord):
    """ Return a list of lower cased words, given a spinal-cased word """
    wordsAndSpaces = re.split(r"-", theWord)
    mixedWords = filter(lambda x: x != '', wordsAndSpaces)
    lowerCasedList = map(lambda x: x.lower(), mixedWords)
    return lowerCasedList

def getFromTrain(theWord):
    """ Return a list of lower cased words, given a Train-Cased word """
    return (getFromSpinal(theWord))
    
def getFromLowerSnake(theWord):
    """ Return a list of lower cased words, given a snake_cased word """
    wordsAndSpaces = re.split(r"_", theWord)
    mixedWords = filter(lambda x: x != '', wordsAndSpaces)
    lowerCasedList = map(lambda x: x.lower(), mixedWords)
    return lowerCasedList
    
def getFromUpperSnake(theWord):
    """ Return a list of lower cased words, given a SNAKE_CASED word """
    return getFromLowerSnake(theWord)
    

def startCaps(inString):
    """ Return the same word with first letter capitalized """
    if inString == '': 
        return ('')
    else:
        return (inString[0].upper() + inString[1:])
    
def makeLowerCamel(lowerCasedList):
    """ Return a lowerCamel word """
    if not lowerCasedList:
        return ""
    firstWord = lowerCasedList[0]
    newList = map(startCaps, lowerCasedList)
    newList[0] = firstWord
    finalWord = "".join(newList)
    return finalWord
    
def makeUpperCamel(lowerCasedList):
    """ Return an UpperCamel word """
    if not lowerCasedList:
        return ""
    newList = map(startCaps, lowerCasedList)
    finalWord = "".join(newList)
    return finalWord

def makeSpinal(lowerCasedList):
    """ Return a spinal-cased word """
    if not lowerCasedList:
        return ""
    finalWord = "-".join(newList)
    return finalWord

def makeTrain(lowerCasedList):
    """ Return a Train-Cased word """
    if not lowerCasedList:
        return ""
    newList = map(startCaps, lowerCasedList)
    finalWord = "-".join(newList)
    return finalWord
    
def makeLowerSnake(lowerCasedList):
    """ Return a snake_cased word """
    if not lowerCasedList:
        return ""
    finalWord = "_".join(newList)
    return finalWord
    
def makeUpperSnake(lowerCasedList):
    """ Return a SNAKE_CASED word """
    if not lowerCasedList:
        return ""
    finalWord = "_".join(newList)
    return finalWord.upper()
    
def makeAllSmalls(lowerCasedList):
    """ Return an all lower cased word, given a list of lower cased words """
    if not lowerCasedList:
        return ""
    finalWord = "".join(newList)
    return finalWord

def makeAllCaps(lowerCasedList):
    """ Return an all caps word, given a list of lower cased words """
    if not lowerCasedList:
        return ""
    finalWord = "".join(newList)
    return finalWord.upper()
    
    