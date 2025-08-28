n, k = map(int, input().split())

switch = []
for _ in range(k):
    a,b = map(int, input().split())
    switch.append((a,b))

seat_set = [set([i]) for i in range(n+1)]
seat = list(range(n+1))

for i in range(3 * k):
    i = i % k
    a,b = switch[i]

    seat[a],seat[b] = seat[b], seat[a]
    seat_set[seat[a]].add(a)
    seat_set[seat[b]].add(b)
    # print(seat)

for i in range(1,n+1):
    # print(seat_set[i])
    print(len(seat_set[i]))

