class Solution:
    def findDiagonalOrder(self, nums):
        rows = len(nums)
        max_diagonal_sum, total_elements, result_index = 0, 0, 0
        element_map = [[] for _ in range(100001)]
        
        for row_index in range(rows):
            total_elements += len(nums[row_index])
            for col_index in range(len(nums[row_index])):
                current_diagonal_sum = row_index + col_index
                element_map[current_diagonal_sum].append(nums[row_index][col_index])
                max_diagonal_sum = max(max_diagonal_sum, current_diagonal_sum)
        
        result = [0] * total_elements
        for i in range(max_diagonal_sum + 1):
            current_diagonal_elements = element_map[i]
            for j in range(len(current_diagonal_elements) - 1, -1, -1):
                result[result_index] = current_diagonal_elements[j]
                result_index += 1
        
        return result
