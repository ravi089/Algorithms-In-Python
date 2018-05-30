# Count vowels in a string.

def count_vowels(strg):
    return len(list(filter(lambda x: x in strg and x in 'aeiou', strg)))

if __name__ == '__main__':
    strg = 'geeksforgeeks portal'
    print (count_vowels(strg))
