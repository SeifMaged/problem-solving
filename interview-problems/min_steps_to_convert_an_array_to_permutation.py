# Minimum steps to convert an Array into permutation of numbers from 1 to N
# Given an array arr of length N, the 
# task is to count the minimum number 
# of operations to convert given sequence 
# into a permutation of first N natural 
# numbers (1, 2, ...., N). In each operation,
# increment or decrement an element by one.
# Example:

# Input: arr[] = {4, 1, 3, 6, 5} 
# Output: 4 
# Apply decrement operation four times on 6
# Input : arr[] = {0, 2, 3, 4, 1, 6, 8, 9} 
# Output : 7 

# O(n log n) time, O(1) space, where n is the number of elements in the input array
# Sorting, Greedy
# We can sort the array and then calculate the number of steps required to convert 
# each element to its corresponding position in the sorted array. The number of steps
# for each element will be the absolute difference between the element's value and its
# index (1-based) in the sorted array. We will sum up these differences to get the total
# number of steps required to make the array consecutive.

def min_steps(arr):
    n = len(arr)
    
    arr = sorted(arr) # n log n
    steps = 0

    for i in range(n):
        steps += abs(arr[i]- (i+1))
    
    return steps
