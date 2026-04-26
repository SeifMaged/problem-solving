# Max Subarray Cost
# Given an array of integers, find the maximum cost of a subarray. The cost of a subarray is defined as the square of the sum of its elements. The subarray must contain at least one element.
# Example: 
# Input: arr = [1, -2, 3, 4]
# Output: 49
# Explanation: The subarray [3, 4] has the maximum cost of (3 + 4)^2 = 49.
# O(n) time, O(1) space, where n is the number of elements in the input array
# Kadane's Algorithm, Greedy
# We can use a modified version of Kadane's algorithm to find the maximum cost of a subarray. We will keep track of the current maximum sum and the current minimum sum at each step. The maximum cost will be the maximum of the square of the current maximum sum and the square of the current minimum sum. This is because a negative sum can also yield a large cost when squared. We will iterate through the array once, updating our current maximum and minimum sums, and calculating the maximum cost at each step.

def max_subarray_cost(arr):
    n = len(arr)
    if n == 0:
        return 0
    curr_max = max_sum = arr[0]
    curr_min = min_sum = arr[0]

    for i in range(1, n):
        num = arr[i]
        curr_max = max(num, curr_max + num)
        max_sum = max(max_sum, curr_max)

        # For minimum subarray sum
        curr_min = min(num, curr_min + num)
        min_sum = min(min_sum, curr_min)

    return max(max_sum ** 2, min_sum ** 2)
