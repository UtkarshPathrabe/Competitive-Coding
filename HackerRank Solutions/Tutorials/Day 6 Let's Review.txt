for x in range(int(raw_input())):
    S = raw_input()
    R = S[::-1]
    funny_flag = True
    for i in range(1, len(S)):
        if abs(ord(S[i]) - ord(S[i-1])) != abs(ord(R[i]) - ord(R[i-1])):
            funny_flag = False
            break
    if funny_flag:
        print 'Funny'
    else:
        print 'Not Funny'