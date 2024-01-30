def AreawithCondition(l,w):
            if l==w:
                return "This is Square!"
            else:
                a=l*w
                return a


l=int(input("Enter Length :"))
w=int(input("Enter Width :"))
area=AreawithCondition(l,w)
print(area)