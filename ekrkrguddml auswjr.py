n = int(input())

x,y = [],[]

for _ in range(n):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)

x.append(x[0])
y.append(y[0])

x_result,y_result = 0,0

for i in range(n):
    x_result += x[i]*y[i+1]
    y_result += y[i]*x[i+1]

print(round(abs((x_result-y_result)/2),1))
