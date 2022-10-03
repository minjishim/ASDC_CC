# (11주차 : 그래프) 13460

# 첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다. 이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다. '.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다. 'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.

# import sys -> input = sys.stdin.readline
from sys import stdin
from collections import deque

# 빠른 입출력
input = stdin.readline

# n : 세로, m : 가로
n, m = map(int, input().split())

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 2차원 리스트의 보드 정보 입력 받기
board = []
for i in range(n):
  board.append(list(input()))
  # 빨간 구슬 위치(rx, ry) 및 파란 구슬 위치(bx, by) 저장
  for j in range(m):
    if(board[i][j] == 'R'):
      rx, ry = i, j
    if(board[i][j] == 'B'):
      bx, by = i, j

# 방문 여부를 표시할 2차원 리스트
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

# -------------------------------이동 함수------------------------------------
def move(x, y, direct):
  cnt = 0
  while(board[x + dx[direct]][y + dy[direct]] != '#' and board[x][y] != 'O'):
    x += dx[direct]
    y += dy[direct]
    cnt += 1
  return x, y, cnt
  
# -------------------------------bfs 함수------------------------------------
def bfs(rx, ry, bx, by):
  queue = deque()
  queue.append((rx, ry, bx, by, 1))
  while queue:
    rx, ry, bx, by, cnt = queue.popleft()
    visited[rx][ry][bx][by] = True
    # 10회를 초과하여 시도한 경우, 실패(-1) 출력
    if(cnt > 10):
      print(-1)
      exit(0)
    # 4방향
    for i in range(4):
      nrx, nry, rcnt = move(rx, ry, i)
      nbx, nby, bcnt = move(bx, by, i)
      # 파란 구슬이 구멍에 빠지지 않았을 경우
      if(board[nbx][nby] != 'O'):
        # 빨간 구슬만 구멍에 빠졌다면 cnt 출력
        if(board[nrx][nry] == 'O'):
          print(cnt)
          exit(0)
        # 파란 구슬과 빨간 구슬이 겹쳤을 때 더 많이 이동한 구슬의 위치를 재배치
        if(nrx == nbx and nry == nby):
          if(rcnt > bcnt):
            nrx -= dx[i]
            nry -= dy[i]
          else:
            nbx -= dx[i]
            nby -= dy[i]
        # 방문한 적이 없다면 방문 처리 및 cnt+1
        if not visited[nrx][nry][nbx][nby]:
          visited[nrx][nry][nbx][nby] = True
          queue.append((nrx, nry, nbx, nby, cnt+1))
  print(-1)
  return

# ------------------------------------------------------------------------
bfs(rx, ry, bx, by)