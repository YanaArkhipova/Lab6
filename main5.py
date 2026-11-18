words=input("Enter the string: ").lower().split()
w=set()
for word in words:
    if word not in w:
        print(word, words.count(word))
        w.add(word)
