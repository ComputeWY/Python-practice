dx = {'N': -1, 'S': 1, 'W': 0, 'E': 0}
dy = {'N': 0, 'S': 0, 'W': -1, 'E': 1}

def solution(park, routes):
    H = len(park)
    W = len(park[0])
    x, y = -1, -1

    for i in range(H):
        for j in range(W):
            if park[i][j] == "S":
                x, y = i, j
                break
        if x != -1:
            break

    for route in routes:
        isFalse = False
        dire_, dist = route.split(" ")
        dist = int(dist)

        for i in range(1, dist + 1):
            nx, ny = x + dx[dire_] * i, y + dy[dire_] * i

            if nx >= H or ny >= W or nx < 0 or ny < 0:
                isFalse = True
                break
            if park[nx][ny] == "X":
                isFalse = True
                break

        if isFalse:
            continue

        nx, ny = x + dx[dire_] * int(dist), y + dy[dire_] * int(dist)
        x, y = nx, ny

    answer = [x, y]
    return answer
