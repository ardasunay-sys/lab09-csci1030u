# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    # First, go through each number in the list.
    # Next, except the number thats chosen, go through each numbers in the list again.
    # Then, check whether those two values equal to the target
    # At last, return those two selected number's indices
    for i in range(len(nums)):
        for x in range(i + 1, len(nums)):
            if nums[i] + nums[x] == target:
                return [i, x]


def max_profit(prices):
    # Outline:
    # First, go through the prices to consider possible buying days.
    # Next, for each buying day, check the prices on the following days.
    # Then, calculate the profit by subtracting buying price from the selling price.
    # Last, Compare the each profit with the largest profit found so far and after that, return max profit, or 0 if no profit is possible
    max_profit_value = 0
    for i in range(len(prices)):
        for x in range(i + 1, len(prices)):
            profit = prices[x] - prices[i]
            if profit > max_profit_value:
                max_profit_value = profit
                
            
    return max_profit_value



def max_subarray(nums):
    # Outline:
    # First, go through each number in the list as a starting point.
    # Next, go through the other numbers except the one thats chosen, but in this case, we can't skip any number since we want contiguous.
    # Then, calculate the sum as we add each number to the block.
    # After, keep track of the largest sum found so far
    # Finally, return the largest sum, even if it is negative.   
    max_sum = nums[0]

    for i in range(len(nums)):
        current_sum = 0

        for x in range(i, len(nums)):
            current_sum += nums[x]

            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
