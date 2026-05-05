# A company is choosing phone numbers for its employees. 
# In order to avoid confusion, the company has decided that
# no phone number will contain the same digit more than once
# in a row (so 0232 is allowed, but not 0223 or 0222). 
# Additionally, any phone number that contains a 4 must begin with 4. 
# The company has also decided to exclude up to three additional digits
# from the number, but it hasn't decided which ones yet. Write a function
# that takes the length of the phone number and the additional digits to be
# disallowed in the number as parameters and prints all possible valid phone
# numbers. You may assume valid input.

# Personal Evaluation:
# I'd say this problem is comparable to a leetcode medium
# I recognized that this problem needs a backtracking solution
# I implemeneted this as best I could but had some inefficiences
# and a bug that I fixed prior to uploading
# Time Complexity: O(k^n) Where k is the number of valid digits: (7-10), and n is the length of the number
# Space Complexity: O(n^2) Recursion stack with up to size n strings leading to approximately O(n^2)
# Possible improvements: Use a mutable structure such as a list to reduce space complexity to O(n) and just add/pop to it

# Was 1/4 problems of an assessment

def all_valid_numbers(length, excluded):
    
    allowed_digits = [i for i in range(10) if i not in excluded]

    def dfs(number, prev_digit, current_len):
        if current_len == length:
            print(number)
            return

        for digit in allowed_digits:
            if digit == 4 and number and number[0] != 4:
                continue
            if digit != prev_digit:
                dfs(number+str(digit), digit, current_len +1)
    
    dfs("", None, 0)