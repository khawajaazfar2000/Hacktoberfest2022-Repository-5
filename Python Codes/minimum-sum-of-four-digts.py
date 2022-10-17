def minimumSum(self, num: int) -> int:
    """
        You are given a positive integer num consisting of exactly four digits. 
        Split num into two new integers new1 and new2 by using the digits found in num. 
        Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.
        Return the minimum possible sum of new1 and new2.
    """
    num = sorted(str(num),reverse=True)
    return int(num[0]) + int(num[1]) + int(num[2])*10 + int(num[3])*10

num = 2932
ans = minimumSum(num)
print(ans)