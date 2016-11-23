################################################################################
#
#   confusingTimes.py - Finds time look-alikes in an analog clock                
# 
#   Inspired from: https://twitter.com/WWMGT/status/481044440673710080
#
################################################################################

# Assume the hour hand and minute hand on the clock looks identical
# The following code snippet finds the confusing times on the clock

for hr in range (0, 12):
    for min in range (0, 60):
        # Find the angle between the hour hand and minute hand
        angle1 = abs(30 * hr - 5.5 * min)
        
        # Find the new time, if hour hand and minute hand to be swapped
        hr2 = min // 5
        min2 = hr * 5 + min // 12.0
        angle2 = abs(30 * hr2 - 5.5 * min2)
        
        # Find the absolute difference between the two angles
        angleDiff = abs(angle1 - angle2)
        
        if angleDiff == 0 and (hr != hr2):
            print "%02d:%02d and %02d:%02d" % (hr, min, hr2, min2)

################################################################################
# Output 
#
# 00:56 and 11:04 
# 01:51 and 10:09 
# 02:47 and 09:13 
# 03:42 and 08:18 
# 04:37 and 07:23 
# 05:33 and 06:27 
# 06:28 and 05:32 
# 08:19 and 03:41 
# 09:14 and 02:46             
################################################################################