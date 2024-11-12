 # practice code: https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        # create an empty list
        result = []
        counter = 0

        # sum first number to second
        for i in range(len(nums)):
            target_number = 0  # Reset target_number for each iteration of i
            counter = i + 1    # Set counter to the next index after i

            while counter < len(nums):
                first_number = nums[i]
                second_number = nums[counter]
                target_number = first_number + second_number

                if target_number == target:
                    result.append(i)
                    result.append(counter)
                    return result  # Exit once solution is found

                counter += 1

        return result  # If no solution is found

if __name__ == '__main__':
    # Example usage
    nums = [10, 3, 4, 5]
    target = 7
    solution = Solution()
    result = solution.twoSum(nums, target)
    print(result)
