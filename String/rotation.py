# Check if two strings are rotation of each other.

def rotation(strg1, strg2):
    return strg2 in strg1 + strg1

if __name__ == '__main__':
    strg1 = 'abcd'
    strg2 = 'cdab'
    print (rotation(strg1, strg2))
