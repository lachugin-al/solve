# Enter your code here. Read input from STDIN. Print output to STDOUT
# Словари

n = int(input())
d = {}

for i in range(n):
    s = input().split()
    d[s[0]] = s[1]

while True:
    try:
        el = input()
        if el in d.keys(): # el - key, d[el] - value
            print(f'{el}={d[el]}')
        else:
            print('Not found')
    except:
        break
