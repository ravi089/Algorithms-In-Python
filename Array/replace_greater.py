# Replace every element with greatest element on right side.

def replace_greatest_right(arr):
    max_ele = float('-inf')
    for (idx, ele) in reversed(list(enumerate(arr))):
        arr[idx] = max_ele if max_ele != float('-inf') else -1
        if max_ele < ele:
            max_ele = ele
    return arr

if __name__ == '__main__':
    arr = [16, 17, 4, 3, 5, 2]
    print (replace_greatest_right(arr))
