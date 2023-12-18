j = 0
List = []
while j < 5:
    i = input('enter something:')
    try:
        n = int(i)
    except Exception as e:
        #print(e)
        List.append(i)
    List.append(n)
    j += 1
print(List)







