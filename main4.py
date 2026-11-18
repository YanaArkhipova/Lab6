numbers=input("Enter the string: ").split()
n=set()
for num in numbers:
    if num in n:
        print("YES")
    else:
        print("NO")
    n.add(num)
