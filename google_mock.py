def slowestKey(releaseTimes, keysPressed):
    N = len(releaseTimes)
    
    for i in range(1,N):
        releaseTimes[i] -= releaseTimes[i-1]
        
    max_duration = releaseTimes[0]
    max_key = keysPressed[0]

    for i in range(1,N):
        if releaseTimes[i] > max_duration:
            max_duration = releaseTimes[i]
            max_key = keysPressed[i]
        elif releaseTimes[i] == max_duration:
            max_key = max(max_key,keysPressed[i])

    if releaseTimes[-1] > max_duration:
        return keysPressed[-1]
    elif releaseTimes[-1] == max_duration:
        return max(max_key,keysPressed[-1])
    return max_key

# Input: releaseTimes = [9,29,49,50], keysPressed = "cbcd"
# Output: "c"
# Explanation: The keypresses were as follows:
# Keypress for 'c' had a duration of 9 (pressed at time 0 and released at time 9).
# Keypress for 'b' had a duration of 29 - 9 = 20 (pressed at time 9 right after the release of the previous character and released at time 29).
# Keypress for 'c' had a duration of 49 - 29 = 20 (pressed at time 29 right after the release of the previous character and released at time 49).
# Keypress for 'd' had a duration of 50 - 49 = 1 (pressed at time 49 right after the release of the previous character and released at time 50).
# The longest of these was the keypress for 'b' and the second keypress for 'c', both with duration 20.
# 'c' is lexicographically larger than 'b', so the answer is 'c'.
case1 = [9,29,49,50]
case2 = "cbcd"
print(slowestKey(case1,case2))