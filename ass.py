def find_majority_element(nums):
    counts = {}
    n = len(nums)

 
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

   
    for num, count in counts.items():
        if count > n / 2:
            return num
    return -1

array = [1, 2, 2, 2, 3, 2, 4, 2, 5]
majority = find_majority_element(array)
print(majority) 
