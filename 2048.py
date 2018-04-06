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

def left(grid):
	for y in range(4):
		for x in range(4):
			if grid [y][x]=="":
				continue
			pickedup =grid [y][x]
			grid [y][x]=""
			for spot in range(x,-2,-1):
				if grid [y][spot]=="":
					continue 
				if spot==-1:
					grid [y][0]=pickedup
				if pickedup==grid [y][spot]:
					grid[y][spot] *=2
				else:
					grid [y][spot+1]=pickedup	




































































































































