# The school children numbering NxN in total go to a cinema theatre which 
# contain NxN seats. The rows are marked 1 to N and the columns are 
# marked 1 to N, so a seat can be identified uniquely by (row, column)
# The girls and boys occupy random seats as per their preference.  
# The school guide who accompanied the children (who will not be seated) is 
# eccentric in maintaining a particular order. He says any boy cannot be 
# seated in a seat whose column index is greater than the row index.
# If such a case to occur, then two adjacent rows can be swapped completely.
# The same process is repeated until his condition is complied with.
# What is the minimum number of swaps required, given a seating arrangement?

# Example: 
# Assume the following initial order.

# Initial     Swap-1      Swap-2      Swap-3      Swap-4
# BBBG        BBBG        BBBG        BGGG        BGGG 
# BBGG        BBGG        BGGG        BBBG        BBGG
# BBGG        BGGG        BBGG        BBGG        BBBG
# BGGG        BBGG        BBGG        BBGG        BBGG 

# Swap-1: Rows 3 and 4
# Swap-2: Rows 2 and 3
# Swap-3: Rows 1 and 2
# Swap-4: Rows 2 and 3 

# Here, the minimum swap required is 4

# There may be cases where such swaps are not possible at all to arrive at 
# the guide's preset order.

def swapper(diffList, start, last):
    skipCount = 0
    while(start < last):
        if (diffList[last] + 1 == diffList[last - 1]):
            skipCount += 1
        x = diffList[last]
        diffList[last] = diffList[last - 1] - 1
        diffList[last - 1] = x + 1
        last = last - 1
        print diffList
        
    return(skipCount, diffList)
    
def superSwap(diffList):    
    retVal = -1
    if(sum(diffList) > 0):
        return(retVal)
        
    retVal = 0
    numGt0 = len(filter(lambda x: x > 0, diffList))
    while(numGt0 != 0):
        start = 0
        for i in range(len(diffList) - 1, - 1, -1):
            elem = diffList[i]
            if (elem > 0):
                startElem = elem
                start = i
                break
            
        last = len(diffList) - 1   
        mover = dict()
        minKey = 1
        for i in range(len(diffList) - 1, start - 1, -1):
            elem = diffList[i]
            mover[elem] = i
            if (elem <= -startElem):
                minKey = elem

        if(len(mover.keys()) > 0):
            print "minKey", minKey
            if minKey == 1:
                minKey = min(mover.keys())
            last = mover[minKey]
            
            while(last - start + minKey > 0):
                mover.pop(minKey)
                if(len(mover.keys()) > 0):
                    minKey = min(mover.keys())
                    last = mover[minKey]
                else:
                    retVal = -1
                    return(retVal)
                
        if(start == last):
            break
        
        print "start", start
        print "last", last 
        
        skipCount, diffList = swapper(diffList, start, last)
        print "skipCount", skipCount
        retVal = retVal + (last - start) - skipCount
        numGt0 = len(filter(lambda x: x > 0, diffList))
        print numGt0
        
    return(retVal)

rowNum = [0, 1, 2, 3]
maxC = [2, 1, 1, 0]
#maxC = [0, 1, 3, 3]
        
diffList = [x - y for x, y in zip(maxC, rowNum)]
    
diffList = [4, 0, 3, 0, 0, 0, -5, -2, -1]    
diffList = [4, 0, 3, -5, 0, 0, 0, -2, -1]    
diffList = [4, 0, 3, -5, -3, 0, 0, -2, -1]    
#diffList = [2, 1, 0, -3]    # [0, -1, 0, -1] unbound
#diffList = [2, -1, -1]     # 2
#diffList = [2, 0, -1, -3]  # 4
print superSwap(diffList)
