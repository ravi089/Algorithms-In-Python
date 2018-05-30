# Print all items of list containing all characters of string.

def print_all_items(strg, arr):
    return list(filter(lambda x: all(z in x for z in strg), arr))


if __name__ == '__main__':
    strg = 'sun'
    arr = ['geeksforgeeks', 'unsorted', 'sunday', 'just', 'sss']
    print (print_all_items(strg, arr))
