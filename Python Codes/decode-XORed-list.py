def decode(encoded: List[int], first: int) -> List[int]:
    """
        There is a hidden integer list decoded that consists of n non-negative integers.

        It was encoded into another integer list encoded of length n - 1, such that 
        encoded[i] = arr[i] XOR arr[i + 1]. For example, if arr = [1,0,2,1], then encoded = [1,2,3].

        You are given the encoded list. You are also given an integer first, that is the first element 
        of arr, i.e. arr[0].

        Return the original list decoded. It can be proved that the answer exists and is unique.
    """
    lst = [first] 
    for i in encoded:
        last.append(i ^ lst[-1])
    return lst

encoded = [1,2,3]
first = 1

decoded = decode(encoded, first)
print(decoded)