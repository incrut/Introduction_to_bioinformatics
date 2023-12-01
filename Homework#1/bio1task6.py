def LongestCommonSubstr (s1, s2):

    l1 = len(s1)
    l2 = len(s2)

    lon_com_sbst=""

    for i in range (l1):
        for j in range (l1):
            if s1[i:i+j] in s2 and len(s1[i:i+j]) > len(lon_com_sbst):
                lon_com_sbst = s1[i:i+j]
                ind1 = i
                ind2 = s2.index(lon_com_sbst)

    new_s1 = ""
    if ind1 > ind2:
        long = ind1
        short = ind2
        longs = s1
        shorts =s2
    else:
        long = ind2
        short = ind1
        longs = s2
        shorts = s1
    for i in range(short-len(lon_com_sbst)):
        new_s1 += 'x'
    new_s1 += shorts
    new_s2 = longs
    for i in range (len(new_s1)-len(longs)):
        new_s2 += 'x'
    return lon_com_sbst, new_s1, new_s2


print (LongestCommonSubstr("CAAGATCCCGTCGACGGACACAGGTAGTCGAAGTGGAGAATTCAGACTCAACCACCAAGTGTCATAGGCCCTGGATTGGTCATTTAACAGA",
                           "GCTCCACATATCTTACCGCTGATTCGTCAGGATCAGGTAGAGAGTCATGCGGGCCAGGTCATCCGAACGAGCTCGGCGGATAACGA"))
