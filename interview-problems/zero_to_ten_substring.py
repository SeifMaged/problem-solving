''' 
Problem: Zero To Ten Substring

Given a String s containing digits from 0 to 9, determine the count of occurences of the shortest substring that encompasses
all numbers from 0 to 10


Example:
Input: "0123456789100"
Output: 2
Explanation: The shortest substring that contains all numbers from 0 to 10 is of length 12.
There are two such substrings: "012345678910" and "123456789100".
'''

def zeroToTenSubstring(s):
 
    hexa = ""

    i = 0
    n = len(s)

    # Replace all occurences of '10' with A for simplicity
    while i < n:
        if s[i] != '1':
            hexa += s[i]
        else:
            if i < n-1 and s[i+1] == '0':
                hexa += 'A'
                i += 1
            else:
                hexa += '1'
        
        i += 1
    
    shortest = float('inf')

    left = 0

    n = len(hexa)
    count = {}
    
    occurences = -1

    for right in range(n):
        count[hexa[right]] = 1 + count.get(hexa[right], 0)

        while len(count) == 11:
            
            current = right - left + 1 + count['A'] # Each 'A' represents '10' (2 characters), so we add count['A'] to get the true window length in the original string

            if current < shortest:
                shortest = current
                occurences = 1
            elif current == shortest:
                occurences += 1

            if count[hexa[left]] == 1:
                del count[hexa[left]]
            else:
                count[hexa[left]] -= 1
            left += 1
    
    return occurences

print(zeroToTenSubstring("0123456789100"))
