# This pyton file has functions to change the names of variables in source file

###############################################################################
# SUPPORTED MODES
# camelCase
# CamelCase
# spinal-case or lisp-case or kebab-case
# Train-Case
# snake_case
# SNAKE_CASE
# ALLCAPS
# allsmalls
###############################################################################

###############################################################################
# Idea of using replacement function with extra argument taken from the link
# below in Stack Overflow
# http://goo.gl/uvYUXl
#
# Todo:
# 1. From the same link above, need to try "partial" from "functools"
###############################################################################
    
###############################################################################
# This short snippet for function composition is taken from 
# https://mathieularose.com/function-composition-in-python/#solution

import functools

def compose(*functions):
    # Specific to a 2-function composition
    def compose2(f, g):
        return lambda x: f(g(x))
    # Generalizing the function composition for more than 2 functions    
    return functools.reduce(compose2, functions)
###############################################################################

import re
import os.path
import sys

def getNewDict(keyList, valueList):
    """ Return a dictionary, initialized using two lists """
    newDict = dict()
    newDict.fromkeys(keyList)
    assert(len(keyList) == len(valueList))
    for i in range(len(keyList)):
        newDict[keyList[i]] = valueList[i]
        
    return newDict
    
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
    finalWord = "-".join(lowerCasedList)
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
    finalWord = "_".join(lowerCasedList)
    return finalWord
    
def makeUpperSnake(lowerCasedList):
    """ Return a SNAKE_CASED word """
    if not lowerCasedList:
        return ""
    finalWord = "_".join(lowerCasedList)
    return finalWord.upper()
    
def makeAllCaps(lowerCasedList):
    """ Return an all caps word, given a list of lower cased words """
    if not lowerCasedList:
        return ""
    finalWord = "".join(lowerCasedList)
    return finalWord.upper()

def makeAllSmalls(lowerCasedList):
    """ Return an all lower cased word, given a list of lower cased words """
    if not lowerCasedList:
        return ""
    finalWord = "".join(lowerCasedList)
    return finalWord

###############################################################################
# CONSTANTS

fromKeysList = ["camelCase", "CamelCase", "spinal-case", 
                "Train-Case", "snake_case", "SNAKE_CASE"]
fromValuesList = [getFromLowerCamel, getFromUpperCamel, getFromSpinal,
                  getFromTrain, getFromLowerSnake, getFromUpperSnake]
# patternList will use fromKeysList to form a dictionary                         
patternList = [ r"(?<=\W)[a-z][a-z0-9]*([A-Z][a-z0-9]+)*",
                r"(?<=\W)([A-Z][a-z0-9]*)+",    
                r"(?<=\W)([a-z][a-z0-9]*-)+[a-z0-9]+",    
                r"(?<=\W)([A-z][a-z0-9]*-)+[A-Z][a-z0-9]+",    
                r"(?<=\W)([a-z][a-z0-9]*_)+[a-z0-9]+",    
                r"(?<=\W)([A-Z][A-Z0-9]*_)+[A-Z0-9]+"]
             
toKeysList = ["camelCase", "CamelCase", "spinal-case", 
              "Train-Case", "snake_case", "SNAKE_CASE", 
              "ALLCAPS", "allsmalls"]
toValuesList = [makeLowerCamel, makeUpperCamel, makeSpinal,
                makeTrain, makeLowerSnake, makeUpperSnake,
                makeAllCaps, makeAllSmalls]

fromFuncDict = getNewDict(fromKeysList, fromValuesList)
toFuncDict = getNewDict(toKeysList, toValuesList)                
###############################################################################
    
def convertorFunction(fromConvention, toConvention):
    """ Return a composed function object """
    convertor = compose(toFuncDict[toConvention], fromFuncDict[fromConvention]) 
    return convertor
    
def getReplacement(theConvertor):
        
    def replFunction(matchObj):
        theWord = matchObj.group(0)
        return theConvertor(theWord)
    
    return replFunction    
    
def lineParser(lineRange):
    lineNums = re.split(r',', lineRange)
    newList = list()
    for x in lineNums:
        if re.match(r'^\d+$', x):
            newList.append(int(x))
        if re.search(r':', x):
            minMax = re.split(r':', x)
            if len(minMax) != 2:
                continue
            if not re.match(r'^\d+$', minMax[0]):
                continue
            if not re.match(r'^\d+$', minMax[1]):
                continue
            lo = int(minMax[0])
            hi = int(minMax[1]) + 1
            for i in range(lo, hi):
                newList.append(i)
    return newList    
    
def processFile(fileName, fromConvention, toConvention, ls = ""):

    if fromConvention not in fromKeysList:
        return "UnrecognizedConvention"

    if toConvention not in toKeysList:
        return "UnrecognizedConvention"
                        
    if not os.path.isfile(fileName):
        return fileName + ": " + "File does not exist!"
    
    theConvertor = convertorFunction(fromConvention, toConvention)
    
    # Copy the original contents to a back-up file 
    bakFile = fileName + ".bak"
    fwBK = open(bakFile, "w")
    fr = open(fileName, 'r')
    originalLines = fr.readlines()
    fwBK.writelines([l for l in originalLines])
    fr.close()
    fwBK.close()

    if ls != "":
        selectLines = lineParser(ls)
    else:
        selectLines = range(1, sum (1 for i in originalLines) + 1)
        
    patternDict = getNewDict(fromKeysList, patternList)
        
    fw = open(fileName, "w")
    lineNum = 1
    for l in originalLines:
        if lineNum in selectLines:
            fw.write(re.sub(patternDict[fromConvention], 
                getReplacement(theConvertor), l))
        else:
            fw.write(l)
        lineNum += 1
    fw.close()
    
    return "Success: File Processed"
    

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--help":
            print "Usage:"
            print "changeNames.py file fromMode toMode <lineNumbers>"
            print "\nAvailable fromModes:"
            print fromKeysList
            print "\nAvailable toModes:"
            print toKeysList
            print "\n<lineNumbers> is optional; Default: Process all lines"
            print "Input format Supports ',' and ':'"
            print "Example: 1:4,6,7,9:10,14 process lines 1,2,3,4,6,7,9,10,14"
    elif len(sys.argv) != 4 and len(sys.argv) != 5:
        print "Usage: changeNames.py file fromMode toMode <lineNumbers>"
        print "       changeNames.py --help for detailed info"
    else:    
        status = processFile(*sys.argv[1:])
        print status
    