def f(a,low,high):
    i=low
    pivot=a[i]
    j=high
    while i<=j:
        if a[i]<=pivot :
            i+=1
        elif a[j]>pivot :
            j-=1
        else:
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
    a[low], a[j] = a[j], a[low]
    return j 
    
def quik(a,low,high):
    if low<high:
        part=f(a,low,high)
        quik(a,low,part-1)
        quik(a,part+1,high)
a=[1,2,3,5,4,7,8,9,6]
quik(a,0,len(a)-1)
print(a)