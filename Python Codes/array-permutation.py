arr = = [0,2,1,5,3,4]

def buildArray(nums: List[int]) -> List[int]:
  q = len(nums)
  for i,c in enumerate(nums):
    nums[i] += q * (nums[c] % q)
  for i,_ in enumerate(nums):
    nums[i] //= q
  return nums

ans = buildArray(arr)
print(ans)