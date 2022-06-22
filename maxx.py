def max(L):
    if L==[]:
        return False
    else:
        max=L[0]
        for i in range(len(L)):
            if L[i]>=max:
                return max==L[i]
            elif L[i]==max:
                return max
            else:
                return max
    return max

print(max([11,11,1,66,999]))
