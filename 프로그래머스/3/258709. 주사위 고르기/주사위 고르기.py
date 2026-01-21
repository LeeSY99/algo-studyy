def solution(dice):
    answer = []
    n = len(dice)
    a_dice = []
    max_win = 0
    
    def choice_dice(get, idx):
        if get == n//2:
            b_dice = []
            for i in range(n):
                if i not in a_dice:
                    b_dice.append(i)
            calc(a_dice, b_dice)
            return
        
        if idx == n:
            return
        a_dice.append(idx)
        choice_dice(get+1, idx+1)
        a_dice.pop()
        choice_dice(get, idx+1)
    
    def calc(a,b):
        nonlocal max_win, answer
        A = {}
        B = {}
        a_sum = 0
        b_sum = 0
        
        def roll_dice(idx,a_sum,b_sum):
            if idx == n//2:
                if a_sum not in A:
                    A[a_sum] = 1
                else:
                    A[a_sum] += 1
                
                if b_sum not in B:
                    B[b_sum] = 1
                else:
                    B[b_sum] += 1
                return
            
            a_dice = dice[a[idx]]
            b_dice = dice[b[idx]]
            for i in range(6):
                a_sum += a_dice[i]
                b_sum += b_dice[i]
                roll_dice(idx + 1, a_sum, b_sum)
                a_sum -= a_dice[i]
                b_sum -= b_dice[i]
                
        roll_dice(0, a_sum, b_sum)
        
        win = 0
        lose = 0
        draw = 0
        for num_a, count_a in A.items():
            for num_b, count_b in B.items():
                if num_a > num_b:
                    win += count_a * count_b
                elif num_a < num_b:
                    lose += count_a * count_b
                else:
                    draw += count_a * count_b
        # print(win)
        if win > max_win:
            max_win = win
            # print(max_win, a)
            answer = []
            for i in a:
                answer.append(i+1)

        
    choice_dice(0,0)
    print(max_win)
    return answer