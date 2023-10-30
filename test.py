A= open("text.txt","rt")
new= 0
arr= []
for line in A:
    line = line.strip()
    try:
        value = int(line)
        new +=value
    except ValueError:
        arr.append(line)


print(new)


