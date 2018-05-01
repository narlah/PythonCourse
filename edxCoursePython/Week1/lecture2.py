result = ""
num = .1
p = 0
while num*(2**p)%1!=0:
    p+=1
print (p)

num = int(num*(2**p))
print(num)

while num >= 1:
    result = str(num % 2) + result
    num /= 2
print(result)

result = "."+(p-len(result))*"0" + result
print("final :" + result)
