# Maximum occurring character in a string

def max_occurring_char(strg):
    d = {}
    for ele in strg:
        d.setdefault(ele, 0)
        d[ele] += 1
    return sorted(d.items(), key=lambda x:x[1], reverse=True)[0][0]
        
    
if __name__ == '__main__':
    strg = 'sample string'
    print (max_occurring_char(strg))
