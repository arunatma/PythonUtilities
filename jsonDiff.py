from sets import Set
dictBef = dict()
dictAft = dict()

dictBef["R1"] = "V1"
dictBef["R2"] = "CV1CV2CV3CV4"
dictBef["R3"] = "V3"

# K1 unmodified
# K2 updated
# K3 deleted
# K4 added
# K5 added
dictAft["R1"] = "V1"
dictAft["R2"] = "CV1XX2CV3CV4"
dictAft["R4"] = "V4"
dictAft["R5"] = "V5"

def findDiff(dictBef, dictAft):
    """
    Return the difference between the two dictionaries
    """
    dictAgg = dict()
    keysBef = dictBef.keys()
    keysAft = dictAft.keys()
    keySet = Set(keysBef + keysAft)
    for k in keySet:
        existsBef = k in dictBef
        existsAft = k in dictAft
        updated = existsBef and existsAft
        added = not existsBef and existsAft
        deleted = existsBef and not existsAft
        if updated:
            v1 = dictBef[k]
            v2 = dictAft[k]
            if v1 == v2:
                status = "same"
            else:
                status = "updated"
            aggVal = (v1, v2, status)
        elif added:
            v2 = dictAft[k]
            aggVal = ("-", v2, "added")
        elif deleted:
            v1 = dictBef[k]
            aggVal = (v1, "-", "deleted")
        dictAgg[k] = aggVal
    return dictAgg
    