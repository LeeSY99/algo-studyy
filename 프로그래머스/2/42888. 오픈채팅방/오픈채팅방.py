def solution(record):
    answer = []
    id_to_nick = {}
    nick_to_id = {}
    a = []
    
    for r in record:
        cmd, id, *nickname = r.split()
        if cmd == 'Enter':
            id_to_nick[id] = nickname[0]
            a.append((id, 'enter'))
        elif cmd == 'Leave':
            a.append((id, 'leave'))
        elif cmd == 'Change':
            id_to_nick[id] = nickname[0]
            
    for id, cmd in a:
        if cmd == 'enter':
            answer.append(f'{id_to_nick[id]}님이 들어왔습니다.')
        elif cmd == 'leave':
            answer.append(f'{id_to_nick[id]}님이 나갔습니다.')
    
    return answer