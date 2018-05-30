#### Shuffling the array (Even elements at even index and odd elements at
#### odd index)####

def shuffling(arr):
    for i in range(len(arr)):
        if arr[i]%2 == 0:
            if i%2 == 0:
                continue
            

if __name__ == '__main__':
    arr = [10, 9, 7, 18, 13, 19, 4, 20, 21, 14]
    shuffling(arr)
