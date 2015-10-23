numberLines = int(input())

while 0 < numberLines:
    number = int(input())
    sum = 0
    for i in range(number):
        if i%3 == 0 or i%5 == 0:
            sum = sum + i
    print(sum)
    
    numberLines = numberLines - 1