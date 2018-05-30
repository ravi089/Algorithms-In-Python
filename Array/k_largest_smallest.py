# k-largest/k-smallest element in an array.

def k_largest_smallest(arr,k,large):
    return sorted(arr, reverse=large)[:k]

if __name__ == '__main__':
    arr = [1, 23, 12, 9, 30, 2, 50]
    print (k_largest_smallest(arr, 2, False))
