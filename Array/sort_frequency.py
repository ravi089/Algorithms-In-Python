# Sort array elements by frequency.

def frequency_sort(arr):
    freq = {}
    for ele in arr:
        freq.setdefault(ele, 0)
        freq[ele] += 1
    sorted_t = sorted(freq.items(), key=lambda x:x[1], reverse=True)
    return [y for x in sorted_t for y in [x[0]] * x[1]]     

if __name__ == '__main__':
    arr = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
    print (frequency_sort(arr))
