# The game Mingo involves a 100x100 board with unique positive whole numbers in the range from 1 to 1 million
# randomly distributed in the cells. Unique numbers are "called" one at a time and the goal is to have a "Mingo",
#  which is an entire row or column on cells with numbers that have been called, one might also form a diagonal
# from corner to corner with numbers that have been called. Write a function that takes as parameters a square
# array of 100x100 positive whole numbers and a list of "called" numbers. Your function will report whether a
# "Mingo" occurs, and after how many called numbers the first Mingo occurs. You may assume valid input.

# Personal Evaluation:
# I'd say this problem is comparable to a leetcode medium
# I implemeneted this as best I could but had some inefficiences that I fixed prior to uploading
# Time Complexity: O(k) Where k is the number of calls
# Space Complexity: O(1) Since the board size is constant, the bulk of the extra storage is in the hashmap I used
# which is of size 100x100, but still constant, if this question were to be generalized for variable size grid this would be different.

# This was 1/4 problems in an assessment.

def mingo(board, called):
    if not board:
        return -1
    indices = {} # To store indices of each unique value for future O(1) lookup

    for i in range(100):
        for j in range(100):
            indices[board[i][j]] = (i, j)
    
    rows = [0]*100
    cols = [0]*100
    diagonal1 = 0
    diagonal2 = 0

    call_count = 0

    for call in called:
        call_count += 1
        
        if call in indices: # if call is in board
            row, col = indices[call]
            
            rows[row] += 1
            cols[col] += 1

            if row == col:
                diagonal1 += 1
            if row+col == 99: # diagonal 2 case
                diagonal2 += 1

            if rows[row] == 100 or cols[col] == 100 or diagonal1 == 100 or diagonal2 == 100:
                return call_count
    
    return -1 # In case no mingo occured