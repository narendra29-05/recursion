def sort(leftarray,rightarray):
    left=0
    right=0
    nl=[]
    while left<len(leftarray) and right<len(rightarray):
        if leftarray[left]<=rightarray[right]:
            nl.append(leftarray[left])
            left+=1
        else:
            nl.append(rightarray[right])
            right+=1
    nl.extend(leftarray[left:])
    nl.extend(rightarray[right:])
    return nl
def merge(a):
    if len(a)<=1:
        return a
    m=len(a)//2
    leftarray=merge(a[:m])
    rightarray=merge(a[m:])
    return sort(leftarray,rightarray)
a=[1,5,3,7,9,0,-1,4,5,6,7,4,32,1,3,3]
print(merge(a))
