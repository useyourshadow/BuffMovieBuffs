### This is a sample Python script

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions,dollar$
'''
num= 27


firstDigit = num // 10
secondDigit = num % 10
if firstDigit== secondDigit:
    print(num)
else:
    while firstDigit != secondDigit:
        print(num, end=' ' )
        firstDigit = num // 10
        secondDigit = num % 10
        num +=1
        if num>90:
            break
base = 5
for i in range(base,-1,-1):
    print('*'*i)

def is_prime(n):
    for num in range(n):
        if num%n == 0 and n!=1 and n!= n:
            return False
        else:
            return True
print(is_prime(11))

i = 0
result= 0
choice = int(input())
while choice!= 0:
    while choice > i:
        i+=1
        sum = int(input())
        result+= sum
    print(result)
    choice= int(input())
'''
line = ["Gator", [6, 1, 9], 4, 8]
print(line[-3][0:1])
print(line[0:2][0])