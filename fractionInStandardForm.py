def factor(number):
    a = number
    i = a
    fac = [1]
    def loop(a):
        for x in range(2,i+1):
            if a % x == 0:
                fac.append(x)
                a = a/x
                if a != 1:
                    loop(a)
                break
            else:
                pass
    loop(a)
    return fac



num = int(input("Numerator : "))
den = int(input("Denominator : "))


list_num = factor(num)
list_den = factor(den)
# print()
# print('old', list_num)
# print('old', list_den)
# print()

x = list_num.copy()
y = list_den.copy()

new_num = 1
new_den = 1

for i in x:
    for j in list_den:
        if j == i:
            list_num.remove(i)
            list_den.remove(j)
            break
        else:
            pass

# print(list_num)
# print(list_den)

for i in list_num:
    new_num = new_num*i

for j in list_den:
    new_den = new_den*j

print()
print()
print(new_num)
print("-")
print(new_den)