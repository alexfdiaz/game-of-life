import pygame

pygame.init()
winSize = (800, 600)
win = pygame.display.set_mode(winSize)
pygame.display.set_caption('Game of life')
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Board():
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]
		self.nextGen = [[0 for _ in range(self.width)] for _ in range(self.height)]

	def calculateNextGen(self):
		self.nextGen = self.board
		for y, row in enumerate(self.board):
			for x, cell in enumerate(row):
				liveCellCounter = 0
				if y == 0:

					if x == 0:
						for j in [-1, 0, 1]:
							for i in [-1, 0, 1]:
								if self.board[j][i] == 1 and (j != y or i != x):
									liveCellCounter += 1
						if self.board[y][x] == 0:
							if liveCellCounter == 3:
								self.nextGen[y][x] = 1
						elif self.board[y][x] == 1:
							if not (liveCellCounter == 2 or liveCellCounter == 3):
								self.nextGen[y][x] = 0

					elif x == len(row) - 1:
						for j in [-1, 0, 1]:
							for i in [-2, -1, 0]:
								if self.board[j][i] == 1 and (j != y or i != x):
									liveCellCounter += 1
						if self.board[y][x] == 0:
							if liveCellCounter == 3:
								self.nextGen[y][x] = 1
						elif self.board[y][x] == 1:
							if not (liveCellCounter == 2 or liveCellCounter == 3):
								self.nextGen[y][x] = 0

					else:
						for j in [-1, 0, 1]:
							for i in range(x-1, x+2):
								if self.board[j][i] == 1 and (j != y or i != x):
									liveCellCounter += 1
						if self.board[y][x] == 0:
							if liveCellCounter == 3:
								self.nextGen[y][x] = 1
						elif self.board[y][x] == 1:
							if not (liveCellCounter == 2 or liveCellCounter == 3):
								self.nextGen[y][x] = 0

				elif y == len(self.board) - 1:

					if x == 0:
						for j in [-2, -1, 0]:
							for i in [-1, 0, 1]:
								if self.board[j][i] == 1 and (j != y or i != x):
									liveCellCounter += 1
						if self.board[y][x] == 0:
							if liveCellCounter == 3:
								self.nextGen[y][x] = 1
						elif self.board[y][x] == 1:
							if not (liveCellCounter == 2 or liveCellCounter == 3):
								self.nextGen[y][x] = 0

					elif x == len(row) - 1:
						for j in [-2, -1, 0]:
							for i in [-2, -1, 0]:
								if self.board[j][i] == 1 and (j != y or i != x):
									liveCellCounter += 1
						if self.board[y][x] == 0:
							if liveCellCounter == 3:
								self.nextGen[y][x] = 1
						elif self.board[y][x] == 1:
							if not (liveCellCounter == 2 or liveCellCounter == 3):
								self.nextGen[y][x] = 0

					else:
						for j in [-2, -1, 0]:
							for i in range(x-1, x+2):
								if self.board[j][i] == 1 and (j != y or i != x):
									liveCellCounter += 1
						if self.board[y][x] == 0:
							if liveCellCounter == 3:
								self.nextGen[y][x] = 1
						elif self.board[y][x] == 1:
							if not (liveCellCounter == 2 or liveCellCounter == 3):
								self.nextGen[y][x] = 0
				else:

					if x == 0:
						for j in range(y-1, y+2):
							for i in [-1, 0, 1]:
								if self.board[j][i] == 1 and (j != y or i != x):
									liveCellCounter += 1
						if self.board[y][x] == 0:
							if liveCellCounter == 3:
								self.nextGen[y][x] = 1
						elif self.board[y][x] == 1:
							if not (liveCellCounter == 2 or liveCellCounter == 3):
								self.nextGen[y][x] = 0

					elif x == len(row) - 1:
						for j in range(y-1, y+2):
							for i in [-2, -1, 0]:
								if self.board[j][i] == 1 and (j != y or i != x):
									liveCellCounter += 1
						if self.board[y][x] == 0:
							if liveCellCounter == 3:
								self.nextGen[y][x] = 1
						elif self.board[y][x] == 1:
							if not (liveCellCounter == 2 or liveCellCounter == 3):
								self.nextGen[y][x] = 0

					else:
						for j in range(y-1, y+2):
							for i in range(x-1, x+2):
								if self.board[j][i] == 1 and (j != y or i != x):
									liveCellCounter += 1
									#print(f'celda ({x}, {y}), vecina viva ({i}, {j})')
						if self.board[y][x] == 0:
							if liveCellCounter == 3:
								self.nextGen[y][x] = 1
						elif self.board[y][x] == 1:
							if not (liveCellCounter == 2 or liveCellCounter == 3):
								self.nextGen[y][x] = 0

		self.board = self.nextGen

	def grid(self):
		for y, row in enumerate(self.board):
			pygame.draw.line(win, WHITE, (0, y * (winSize[1] / self.height)), (winSize[0], y * (winSize[1] / self.height)), 1)
		for x, cell in enumerate(self.board[0]):
			pygame.draw.line(win, WHITE, (x * (winSize[0] / self.width), 0), (x * (winSize[0] / self.width), winSize[1]), 1)

	def draw(self):
		for y, row in enumerate(self.board):
			for x, cell in enumerate(row):
				if self.board[y][x] == 1:
					pygame.draw.rect(win, WHITE, (x * (winSize[0] / self.width), y * (winSize[1] / self.height), winSize[0] / self.width, winSize[1] / self.height))

def drawWindow():
	win.fill(BLACK)
	board.grid()
	board.draw()

	pygame.display.update()

board = Board(40, 30)
fps = 5

board.board[8][3], board.board[8][4], board.board[8][5], board.board[7][5], board.board[6][4] = 1, 1, 1, 1, 1
print(f'holaas {board.board[6][4]}')

run = True
while run:
	clock.tick(fps)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	drawWindow()
	board.calculateNextGen()

pygame.quit()