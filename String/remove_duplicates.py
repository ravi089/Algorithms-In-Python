# Remove all duplicates from the string.

def remove_duplicates(strg):
    return "".join(set(strg))
    
if __name__ == '__main__':
    strg = 'geeksforgeeks'
    print (remove_duplicates(strg))
