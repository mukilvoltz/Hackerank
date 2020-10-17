def power(n,p):
    if p<=1:
        return n
    else:
        return n*power(n,p-1)
if __name__=="__main__":
    number,powe=input().split()
    number=int(number)
    powe=int(powe)
    if powe!=1:
        print(power(number,powe))
    else:
        print(number)
