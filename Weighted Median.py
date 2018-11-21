n = int(input())

upper = 0

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
for i in range(n):
    upper += lst1[i] * lst2[i]

print(upper/sum(lst2))