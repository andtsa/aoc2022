if __name__ == "__main__":
    pass

f1 = open("day6.txt")
f2 = open("day6test.txt")
file = f1.read()
testf = f2.read()

def hasDuplicates(x):
    k = 0
    for l in range(len(x)-1):
        k=l+1
        for l in range(k):
            if x[l]==x[k]:
                return True
    return False

x = 0
y = []

for char in file:
    x+=1
    y.append(char)
    if len(y)>14:
        y.pop(0)
    if len(y)==14:
        if not hasDuplicates(y):
            print(x, end=", ")
