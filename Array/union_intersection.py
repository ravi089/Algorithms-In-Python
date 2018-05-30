# Union and intersection of two arrays.

def union(arr1, arr2):
    return list(set(arr1 + arr2))

def intersect(arr1, arr2):
    return [x for x in arr1 if x in arr2]

if __name__ == '__main__':
    arr1 = [1,2,3,4,5]
    arr2 = [4,5,6,7]
    print (union(arr1, arr2))
    print (intersect(arr1, arr2))
