# Remove all duplicates from the string.

def remove_duplicates(strg):
    result = []
    [result.append(x) for x in strg if x not in result]
    return ''.join(result)

if __name__ == '__main__':
    strg = 'geeksforgeeks'
    print (remove_duplicates(strg))
