# Find maximum depth of nested parenthesis in a string.

def max_depth_parenthesis(strg):
    dep = 0
    res = 0
    for ele in strg:
        if ele == '(':
            dep += 1
        elif ele == ')':
            dep -= 1
        if res < dep:
            res = dep
        if dep < 0:
            return -1
    return (res if dep == 0 else -1)

if __name__ == '__main__':
    strg = '(b) ((c) ()'
    print (max_depth_parenthesis(strg))
