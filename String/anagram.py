# Check if two strings are anagram or not.

def anagram(strg1, strg2):
    return ''.join(sorted(strg1)) == ''.join(sorted(strg2))

if __name__ == '__main__':
    strg1 = 'stressed'
    strg2 = 'desserts'
    print (anagram(strg1, strg2))
