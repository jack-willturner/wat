def get_moves(state):
    t1,t2,t3 = state[0], state[1], state[2] 
    moves = []

    if t1: 
        n1 = t1.pop(-1)
        if not t2 or n1 < t2[-1]: 
            moves.append([t1,t2+[n1],t3])
     
        if not t3 or n1 < t3[-1]: 
            moves.append([t1,t2,t3+[n1]])
        
        t1.append(n1) # this appends n1 to both t1s above
    if t2: 
        n2 = t2.pop(-1) 
        if not t1 or n2 < t1[-1]: 
            moves.append([t1+[n2],t2,t3])
        if not t3 or n2 < t3[-1]:
            moves.append([t1,t2,t3+[n2]])
        t2.append(n2)


    if t3:
        n3 = t3.pop(-1)
        if not t1 or n3 < t1[-1]: 
            moves.append([t1+[n3],t2,t3])
        if not t2 or n3 < t2[-1]:
            moves.append([t1,t2+[n3],t3])
        t3.append(n3)
        
        
    #print(moves)
    return moves


def hanoi(n): 
    final_state = [i for i in range(n)] 
    t1, t2, t3 = [i for i in range(n)], [], []
    queue = [[(t1,t2,t3)]]
    
    visited = []
    while(queue):
        p = queue.pop(0) # [(t1,t2,t3)]
        state = p[-1]    # (t1,t2,t3)  
        
        if state[2] == final_state: # 
            return p
        else:
            succs = get_moves(state) # t1,t2,t3
            for s in succs:
                if s not in visited:
                    queue.append(p+[s])
                visited.append(s) 
                
                
hanoi(3)
