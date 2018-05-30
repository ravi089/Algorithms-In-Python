# Count words in a given string.

def count_words(strg):
    return len(strg.split())

if __name__ == '__main__':
    strg = 'One two         three\n    four\tfive  '
    print (count_words(strg))
