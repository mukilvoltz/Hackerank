if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    bigey=arr[0]
    for x in arr:
        if x>bigey:
            bigey=x
    counter=1
    while(counter):
        if bigey in arr:
            arr.pop(arr.index(bigey))
        else:
            counter=0
    secondbigey=arr[0]
    for y in arr:
        if y>secondbigey:
            secondbigey=y
    print(secondbigey)
