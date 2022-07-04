# Четное нечетное

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(0, n):
    s = input()
    odd = ''
    even = ''
    for j in range(len(s)):
        if j % 2 == 0:
            even += s[j]
        else:
            odd += s[j]
    print(even + ' ' + odd)

    # Метод применяемый в Python в одну строчку
    # print(s[::2], s[1::2])
