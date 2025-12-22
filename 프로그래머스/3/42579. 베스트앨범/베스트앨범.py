from collections import defaultdict
def solution(genres, plays):
    DEBUG = True
    answer = []
    g_map = defaultdict(int)
    p_map = defaultdict(list)
    for i in range(len(genres)):
        genre = genres[i]
        g_map[genre] += plays[i]
        p_map[genre].append(i)
    
    if DEBUG:
        for g, played in g_map.items():
            print(g,played)
        print('--')
        for a in p_map.keys():
            print(a,p_map[a])
                
    while True:
        best_g = None
        max_played = 0
        for g, played in g_map.items():
            if played > max_played:
                max_played = played
                best_g = g
        if best_g == None:
            break

        for j in range(2):
            best_music = None
            max_music_played = 0
            for music_num in p_map[best_g]:
                if DEBUG:
                    print(best_g,music_num)
                if plays[music_num] > max_music_played:
                    best_music = music_num
                    max_music_played = plays[music_num]
            if best_music is None:
                break
            answer.append(best_music)
            plays[best_music] = -1
        g_map[best_g] = -1
                
            
    
    return answer