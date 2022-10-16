Arr = [8,7,4,6,3,5,9]
def running_sum(array):
    for i in range(1, len(array)):
        array[i] += array[i - 1]
    return array

ans = running_sum(Arr)
print(ans)