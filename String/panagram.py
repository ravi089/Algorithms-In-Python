# Check if the given string is panagram or not.

def panagram(strg):
    test = 'abcdefghijklmnopqrstuvwxyz'
    return len([x for x in test if x not in strg]) == 0

if __name__ == '__main__':
    strg = 'the quick brown fox jumps over the lazy dog'
    print (panagram(strg))
