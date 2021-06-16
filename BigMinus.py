def BigMinus(s1,s2):
    l1=len(s1)
    l2=len(s2)
    if (l1==l2):
        if s1[0]>s2[0]:
            a1=s1
            a2=s2
        else:
            a1=s2
            a2=s1
    else:
        if (l1 > l2):
            a1=s1
            a2=s2
        else:
            a1=s2
            a2=s1
 
    l1=len(a1)
    l2=len(a2)
    i1=l1-1
    i2=l2-1
    res=""
    b=0
    while(True):
        if ((i1<0) & (i2<0)):
            break
        if (i1<0):
            q2=int(a2[i2])-b
            q2=a2%10
            res=str(q2)+res
            i2-=1
            if (i2<0):
                break
        q1=int(a1[i1])
        q2=int(a2[i2])
        q=q1-b-q2
        if (q>=0):
            res=str(q)+res
            b=0
        else:
            q+=10
            b=1
            res=str(q)+res
        i1-=1
        i2-=1
        
    return res