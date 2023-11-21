from pyamaze import maze, agent, textLabel, COLOR
from collections import deque

rowsAmount = 10 # จำนวน rows [แถวแนวนอน] เปลี้ยนค่าได้ตรงนี้เลย
colsAmount = 10 # จำนวน columns [แถวแนวตั้ง] เปลี้ยนค่าได้ตรงนี้เลย

def BFS(m, start=None):
    if start is None:
        start = (m.rows,m.cols)
    frontier = deque()
    frontier.append(start)
    bfsPath = {}
    explored = [start]
    bSearch = []

    while len(frontier) > 0:
        currCell = frontier.popleft()
        if currCell == m._goal:
            # print(currCell)
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell=(currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell=(currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell=(currCell[0]+1, currCell[1])
                elif d == 'N':
                    childCell=(currCell[0]-1, currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
                bSearch.append(childCell)
                # print(bSearch[-1])
    fwdPath = {}
    cell = m._goal
    while cell != (m.rows,m.cols):
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]
        # print(cell)
    return bSearch, bfsPath, fwdPath

if __name__=='__main__':
    m = maze(rowsAmount, colsAmount)
    m.CreateMaze(loopPercent=10, theme='light')
    bSearch,bfsPath,fwdPath=BFS(m)
    a=agent(m,footprints=True, color=COLOR.blue, shape='square',filled=True)
    b=agent(m,footprints=True, color=COLOR.red, shape='square',filled=False)
    c=agent(m,1,1,footprints=True, color=COLOR.cyan, shape='square', filled=True, goal=(m.rows,m.cols))
    m.tracePath({a:bSearch}, delay=100)
    m.tracePath({c:bfsPath}, delay=100)
    m.tracePath({b:fwdPath}, delay=100)
    # print(b.position)

    l=textLabel(m,'Length of Shortest Path',len(bfsPath)+1)

    m.run()