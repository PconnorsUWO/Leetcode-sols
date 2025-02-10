def countAndSay(n):
    # arr_of_truth = [[""] ]*n+1
    # arr_of_truth[1] = ""
    # for i in range(1,n+1):
    #     for j in range(i, n+1):
    current_string = "1"
    for _ in range(n-1):
        next_string = ""
        j = 0
        k = 0
        while j < len(current_string):
            while ( 
                k < len(current_string)
                and current_string[k] == current_string[j]
            ):
                k+=1
            next_string += str(k - j) + current_string[j]
            j = k
        current_string = next_string
    return current_string
        

# Example 1:

# Input: n = 4
case1 = 4
print(countAndSay(6))
# Output: "1211"

# Explanation:

# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"
# Example 2:

# Input: n = 1

# Output: "1"

# Explanation: