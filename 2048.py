import random
grid=[[""]*4,[""]*4,[""]*4,[""]*4]


def insertnumber(grid):

	emptyspace=[]

	for x in range (4):
		for y in range (4):

			if grid[x][y]=="":
				emptyspace.append((x,y))
	spot=random.choice(emptyspace)
	grid[spot[0]][spot[1]]=random.choice([2,2,2,2,2,2,2,4,4,4])

def is_win(grid):
	for x in range (4):
		for y in range (4):
			if grid [x][y]==2048:
				return True

	return False

def valid_move(grid,move):
	copy=[row.copy() for row in grid]
	move(copy)
	if copy == grid:
		return False
	return True

def is_lose(grid):


def left(grid):
	for y in range(4):
		combined =[False]*4
		for x in range(4):
			if grid [y][x]=="":
				continue
			pickedup =grid [y][x]
			grid [y][x]=""
			for spot in range(x,-2,-1):
				if spot==-1:
					grid [y][0]=pickedup
					break
				if grid [y][spot]=="":
					continue 
				if pickedup==grid [y][spot]and not combined[spot]:
					grid[y][spot] *=2
					combined [spot]=True
					break
				else:
					grid [y][spot+1]=pickedup
					break

def right(grid):
	for y in range(4):
		combined =[False]*4
		for x in range(3,-1,-1):
			if grid[y][x]=="":
				continue
			pickedup =grid [y][x]
			grid [y][x]=""
			for spot in range(x,5,1):
				if spot==4:
					grid [y][3]=pickedup
					break
				if grid [y][spot]=="":
					continue 
				if pickedup==grid [y][spot] and not combined[spot]:
					grid[y][spot] *=2
					combined [spot]=True
					break
				else:
					grid [y][spot-1]=pickedup
					break


def up(grid):
	for x in range(4):
		combined =[False]*4
		for y in range(4):
			if grid [y][x]=="":
				continue
			pickedup =grid [y][x]
			grid [y][x]=""
			for spot in range(y,-2,-1):
				if spot==-1:
					grid [0][x]=pickedup
					break
				if grid [spot][x]=="":
					continue 
				if pickedup==grid [spot][x] and not combined[spot]:
					grid[spot][x] *=2
					combined [spot]=True
					break
				else:
					grid [spot+1][x]=pickedup
					break


def down(grid):
	for x in range(4):
		combined =[False]*4
		for y in range(3,-1,-1):
			if grid [y][x]=="":
				continue
			pickedup =grid [y][x]
			grid [y][x]=""
			for spot in range(y,5,1):
				if spot==4:
					grid [3][x]=pickedup
					break
				if grid [spot][x]=="":
					continue 
				if pickedup==grid [spot][x] and not combined[spot]:
					grid[spot][x] *=2
					combined [spot]=True
					break
				else:
					grid [spot-1][x]=pickedup
					break
