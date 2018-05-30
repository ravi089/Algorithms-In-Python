# Remove all spaces in a string

def remove_spaces(strg):
    return ''.join(strg.split())

if __name__ == '__main__':
    strg = 'g  eeks   for ge  eeks  '
    print (remove_spaces(strg))
