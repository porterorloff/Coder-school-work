import random
import turtle as t 
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
	pass

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

def square(size,position,color1,color2):
	t.penup()
	t.goto(position)
	t.pendown()
	t.color(color1,color2)
	t.begin_fill()
	for i in range(4):
		t.forward(size)
		t.right(90)
	t.end_fill()

backgroundcolor="#4d8076"
gridcolor="#2eb8b8"
tilecolors={	2:"#47d1d1",
				4:"#67e4e4",
				"default":"#a3f5f5"
			}
def background():
	square(600,(-300,300), backgroundcolor,backgroundcolor)
	for i in range (4):
		for j in range(4):
			square(100,(-300+40+140*i,300-40-140*j),gridcolor,gridcolor)

def tile(position,number):
	if number in tilecolors:
		square(100,position,tilecolors[number],tilecolors[number])
	else:
		square(100,position,tilecolors["default"],tilecolors["default"])
	t.write(number)

def drawgrid(grid):
	for x in range(4):
		for y in range (4):
			if grid [y][x] != "":
				tile((-300+40+140*x,300-40-140*y),grid[y][x])

t.tracer(0,0)
t.hideturtle()
background()
grid=[[2]*4,[4]*4,[8]*4,[16]*4]
drawgrid(grid)
t.update()
t.done()
