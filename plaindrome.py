def plaindrome(ch):
    n=len(ch)
    for i in range (0,n):
        if ch[i]==ch[n-i-1] :
            return True
        else :
            return False

print(plaindrome('tot'))
