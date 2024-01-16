def binarySearch(val, low, high, num):
    mid = (high + low) // 2
    if low <= high:
        if val[mid] == num:
            return f"number {num} is present in {mid}"
        elif num > val[mid]:
            return binarySearch(val, mid+1, high, num)
        else:
            return binarySearch(val, low, mid-1, num)
    else:
        return 'not found'


values = [1, 2, 3, 4, 5]
print(binarySearch([1, 2, 3, 4, 5], 0, len(values), 2))
