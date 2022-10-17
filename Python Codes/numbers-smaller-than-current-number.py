def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    """
        Given the list nums, for each nums[i] find out how many numbers in the list are smaller than it. 
        That is, for each nums[i] you have to count the number of valid j's such that j != i and 
        nums[j] < nums[i].

        Return the answer in a list.
    """
	temp = sorted(nums)
	mapping = {}
	result = []
	for i in range(len(temp)):
		if temp[i] not in mapping:
			mapping[temp[i]] = i
	for i in range(len(nums)):
		result.append(mapping[nums[i]])
	return result

nums = [8,1,2,2,3]
ans = smallerNumbersThanCurrent(nums)
print(ans)