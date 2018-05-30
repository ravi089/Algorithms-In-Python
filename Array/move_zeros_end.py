#### Move all zeros to end of array ####

def moveZerosToEnd(arr):
    n = len(arr)
    arr = [x for x in arr if x != 0]
    arr.extend([0] * (n - len(arr)))
    return arr
    
if __name__ == '__main__':
    arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    print (moveZerosToEnd(arr))
