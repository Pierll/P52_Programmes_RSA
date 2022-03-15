#definitions ici
a = [0,5,24,28,2,8]
n = 58649
c = 21138
m = 12
#ne pas toucher à partir de là
p = [] 
q = []
p0 = a[0]
q0 = 1
p.append(p0)
q.append(q0)
p1 = a[0] * a[1] + 1
q1 = a[1]
p.append(p1)
q.append(q1)
print(p)
print(q)
for i in range(2, len(a)+1):
    p.append(a[i-1]*p[i-1] + p[i-2])
    q.append(a[i-1]*q[i-1] + q[i-2])

for i in p:
    #print(i)
    print(c, "^", i, "[", n, "]", "=", m, "[", n, "]")
    if (pow(c, i) % n) == (m % n):
        print("trouve: ", i)
        break