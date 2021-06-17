def BigMinus(s1,s2):
    l1=len(s1)
    l2=len(s2)
    if (l1==l2):
        if s1[0]>s2[0]:
            a1=s1
            a2=s2
            res = ""
        else:
            a1=s2
            a2=s1
            res = ""
    else:
        if (l1 > l2):
            a1=s1[l1-l2-1:l1]
            a2=s2
            res = s1[:l1-l2-1]
        else:
            a1=s2[l2-l1-1:l2]
            a2=s1
            res = s2[:l2-l1-1]
 
    l1=len(a1)
    l2=len(a2)
    i1=l1-1
    i2=l2-1
    subres=""
    b=0
    while(True):
        if ((i1<0) & (i2<0)):
            break
        if (i2<0):
            q1=int(a1[i1])-b
            subres=str(q1)+subres
            i1-=1
            if (i1<0):
                break
        q1=int(a1[i1])
        q2=int(a2[i2])
        q=q1-b-q2
        if (q>=0):
            subres=str(q)+subres
            b=0
        else:
            q+=10
            b=1
            subres=str(q)+subres
        i1-=1
        i2-=1
    
    res += subres
        
    return res
