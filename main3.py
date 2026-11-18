a=input("Enter the first dictionary: ").split()
b=input("Enter the second dictionary: ").split()

a=dict(zip(a[::2], a[1::2]))
b=dict(zip(b[::2], b[1::2]))

A=set(a.keys())
B=set(b.keys())
print(*(A&B))
