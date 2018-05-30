# Print common characters of two string.

def common_char(strg1, strg2):
    return [x for x in strg1 if x in strg2]

if __name__ == '__main__':
    strg1 = 'geeks'
    strg2 = 'forgeeks'
    print (common_char(strg1, strg2))
    
