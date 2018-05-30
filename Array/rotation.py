#### Array rotation #### 

def rotate(arr, d):
    return arr[d:] + arr[:d]

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7]
    print (rotate(arr, 3))
