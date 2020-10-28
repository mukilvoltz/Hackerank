def MinDiscount():
    items=[]
    for i in range(int(input())):
        name,cost,discount=input().split(",")
        cost=int(cost)
        discount=int(discount)
        disamt=int(cost*(discount/100))
        items.append(name)
        items.append(cost)
        items.append(discount)
        items.append(disamt)
    mini=items[3]
    for j in range(0,len(items),4):
        if items[j+3]<mini:
            mini=items[j+3]
    for k in range(0,len(items),4):
        if items[k+3]==mini:
            print(items[k])
if __name__=='__main__':
    MinDiscount()
