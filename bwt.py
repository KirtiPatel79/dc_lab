def bwt(text):
    n = len(text)
    rotations = [text[i:] + text[:i] for i in range(n)]
    rotations.sort()
    return ''.join(r[-1] for r in rotations)
'''
def ibwt(bwt_text):
    n = len(bwt_text)
    table = [''] * n
    for i in range(n):
        table = sorted([bwt_text[j] + table[j] for j in range(n)])
    for row in table:
        if row.endswith('$'):
            return row[:-1]
'''
text = input("Enter a string: ")
bwt_text = bwt(text)
print("Burrows-Wheeler Transform:", bwt_text)



'''
original_text = ibwt(bwt_text)
print("Original string:", original_text)

'''
