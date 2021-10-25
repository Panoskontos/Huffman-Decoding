
def decodeHuff(root, s):
    curr = root
    chars = []
    for c in s:
        if c=='0' and curr.left:
            curr = curr.left
        elif curr.right:
            curr = curr.right
            
        if curr.left is None and curr.right is None:
            # character found!          
            chars.append(curr.data)
            # back to root
            curr = root
    print(''.join(chars))
