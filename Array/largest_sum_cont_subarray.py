# Largest sum coninous subarray.

def largest_sum_cont_array(arr):
    max_sum_so_far = 0
    max_all = float('-inf')
    for ele in arr:
        max_sum_so_far += ele
        if max_sum_so_far < 0:
            max_sum_so_far = 0
        if max_all < max_sum_so_far:
            max_all = max_sum_so_far
    return max_all
        
if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print (largest_sum_cont_array(arr))
