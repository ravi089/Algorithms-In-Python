# Print array such that there are no duplicates.

def print_unique(arr):
    res = []
    [res.append(x) for x in arr if x not in res]
    return res

if __name__ == '__main__':
    arr = [12, 10, 9, 45, 2, 10, 10, 45]
    print (print_unique(arr))
