def min_players_shot(N,He, KKK):
    H=[]
    for i in He:
        H.append(int(i))
    # Sort the players by height
    H.sort()
    # Check if Ali is already visible
    if  H[-1]< KKK:
        return 0
    # Find the first player who blocks Ali's line of sight
    max_height_seen = 0
    num_players_shot = 0
    for i in range(N):
        if int(H[i])> max_height_seen:
            num_players_shot += 1
            max_height_seen = int(H[i])
            # Check if Ali is now visible
            if max_height_seen >= KKK:
                break
    return num_players_shot

T=int(input())
for i in range(T):
 N,K= input().split(" ")
 H = input().split(" ")
 result = min_players_shot(int(N),H,int(K))
 print(result)

