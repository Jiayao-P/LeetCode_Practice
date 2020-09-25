def twoSum(nums: list, target: int) -> list:
    """
    QUESTION:
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
    target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    NOTES:
        1. dictionary is used to store and retrieve values, the good part of this algorithm, is that it stores the
        value instead and use it to retrieve the index, in that case, we just loop through once
        2. emumerate returns a counter and a value
        3. use d[item] = index to create new key value pair

        if we say use the value to check the index itself in the list, then it will happend that we loop over the list
        again(but we cannot in the below case)
    """
    d = {}
    for index, item in enumerate(nums):
        matched = target - nums[index]
        if matched in d:
            return [d[matched], index]
        else:
            d[item] = index


if __name__ == '__main__':
    output = twoSum(nums=[3, 2, 4], target=6)
    print(output)

    output2= twoSum(nums=[32, 3, 12, 9, 7, 8, 0, 4, 3], target=6)
    print(output2)