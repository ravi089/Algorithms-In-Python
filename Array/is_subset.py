# Find whether an array is subset of another array or not.

def is_subset(arr1, arr2):
    return len(list(filter(lambda x: x in arr1, arr2))) == len(arr2)

if __name__ == '__main__':
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]
    print (is_subset(arr1, arr2))
