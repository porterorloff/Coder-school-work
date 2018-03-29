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