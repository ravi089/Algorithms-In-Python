#### Rearrange array to separate negative and positive numbers ####

def rearrange(arr):
    return [x for x in arr if x < 0] + [x for x in arr if x >= 0]

if __name__ == '__main__':
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    print (rearrange(arr))
