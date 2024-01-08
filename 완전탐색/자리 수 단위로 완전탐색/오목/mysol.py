arr=[list(map(int,input().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        five=False
        if arr[i][j]!=0:
            if j<=15:        
                if arr[i][j]==arr[i][j+1]==arr[i][j+2]==arr[i][j+3]==arr[i][j+4]:
                    print(arr[i][j])
                    print(i+1,j+3)
                    five=True
                    break
            if i<=15:
                if arr[i][j]==arr[i+1][j]==arr[i+2][j]==arr[i+3][j]==arr[i+4][j]:
                    print(arr[i][j])
                    print(i+3,j+1)
                    five=True
                    break
            if i<=15 and j<=15:
                if arr[i][j]==arr[i+1][j+1]==arr[i+2][j+2]==arr[i+3][j+3]==arr[i+4][j+4]:
                    print(arr[i][j])
                    print(i+3,j+3)
                    five=True
                    break
            if (j>=4) and i<=14:
                if arr[i][j]==arr[i+1][j-1]==arr[i+2][j-2]==arr[i+3][j-3]==arr[i+4][j-4]:
                    print(arr[i][j])
                    print(i+3,j-1)
                    five=True
                    break
    if five:
        quit()

print(0)