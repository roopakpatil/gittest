def reverse(text):
    print "reverse"
    reverse={}
    rev=''
    for i in text:
        reverse=i
    print reverse
    for i in range(len(reverse),1):
        rev.append(reverse[i])
    print "rev:" +rev
    return rev 

reverse("abcd")