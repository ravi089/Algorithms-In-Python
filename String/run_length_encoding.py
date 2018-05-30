# Run length encoding of a string.

def run_length_encoding(strg):
    d = {}
    for ele in strg:
        d.setdefault(ele, 0)
        d[ele] += 1
    res = ''
    for ele in strg:
        if ele in d:
            res += (ele + str(d[ele]))
            del d[ele]
    return res

if __name__ == '__main__':
    strg = 'wwwwaaadexxxxxx'
    print (run_length_encoding(strg))
