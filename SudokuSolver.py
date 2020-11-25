#OOGA BOOGA CODERS
import math
import tkinter as tk

MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

'''
=============================================
				GUI stuff below
=============================================
'''

class Application(tk.Frame):

	puzzle = [[0, 0, 0,  0, 0, 0,  0, 0, 0],
		  [0, 0, 0,  0, 0, 0,  0, 0, 0],
          [0, 0, 0,  0, 0, 0,  0, 0, 0],

		  [0, 0, 0,  0, 0, 0,  0, 0, 0],
          [0, 0, 0,  0, 0, 0,  0, 0, 0],
		  [0, 0, 0,  0, 0, 0,  0, 0, 0],
		  
          [0, 0, 0,  0, 0, 0,  0, 0, 0],
		  [0, 0, 0,  0, 0, 0,  0, 0, 0],
          [0, 0, 0,  0, 0, 0,  0, 0, 0]]
		
	original = [[0, 0, 0,  0, 0, 0,  0, 0, 0],
		  [0, 0, 0,  0, 0, 0,  0, 0, 0],
          [0, 0, 0,  0, 0, 0,  0, 0, 0],

		  [0, 0, 0,  0, 0, 0,  0, 0, 0],
          [0, 0, 0,  0, 0, 0,  0, 0, 0],
		  [0, 0, 0,  0, 0, 0,  0, 0, 0],
		  
          [0, 0, 0,  0, 0, 0,  0, 0, 0],
		  [0, 0, 0,  0, 0, 0,  0, 0, 0],
          [0, 0, 0,  0, 0, 0,  0, 0, 0]]

	def __init__(self, master):
		super().__init__(master)
		self.master = master
		self.pack()

		self.row, self.col = -1, -1

		self.board = tk.Canvas(self,
        	width=WIDTH,
            height=HEIGHT,
			bg = "#0d0d0d",
			bd = 0)
		self.board.pack(fill="both", expand=True, side="top")

		self.create_widgets()
		self.draw_grid()
		self.draw_puzzle()

		self.board.bind("<Button-1>", self.cell_clicked)
		self.board.bind("<Key>", self.key_pressed) 

	def draw_grid(self):
		for num in range (0,10):
			if (num % 3 == 0):
				color = "#a90016"#"#ffd0d6"
				lineWidth = 4
			else: 
				color = "#ffffff"
				lineWidth = 2
				
			x0 = MARGIN + num * SIDE 
			y0 = MARGIN

			x1 = MARGIN + num * SIDE
			y1 = HEIGHT - MARGIN
			self.board.create_line(x0,y0,x1,y1, fill=color, width=lineWidth)

			x0 = MARGIN
			y0 = MARGIN + num * SIDE

			x1 = WIDTH - MARGIN
			y1 = MARGIN + num * SIDE
			self.board.create_line(x0,y0,x1,y1, fill=color, width=lineWidth)
			
	def create_widgets(self):
		self.quit = tk.Button(
			self, text="QUIT",
			bg="#0d0d0d",
			bd=1,
			fg="red",
			activebackground="#1a1a1a",
			activeforeground="red",
			command=self.master.destroy)
		self.quit.pack(fill="both",side="bottom")

		self.positionSolve = tk.Button(
			self, text="Solve Selected Square",
			bg="#0d0d0d",
			bd=1,
			fg="white",
			activebackground="#1a1a1a",
			activeforeground="white",
			command=self.positionSolve)
		self.positionSolve.pack(fill="both",side="bottom")

		self.fullSolve = tk.Button(
			self, text="Solve Entire Board",
			bg="#0d0d0d",
			bd=1,
			fg="white",
			activebackground="#1a1a1a",
			activeforeground="white",
			command=self.fullSolve)
		self.fullSolve.pack(fill="both",side="bottom")

		self.clear = tk.Button(
			self, text="Clear Board",
			bg="#0d0d0d",
			bd=1,
			fg="white",
			activebackground="#1a1a1a",
			activeforeground="white",
			command=self.clear)
		self.clear.pack(fill="both",side="bottom")

	def cell_clicked(self, event):
		self.board.delete("error")
		x, y = event.x, event.y
		if (MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
			self.board.focus_set()
			row, col = (y - MARGIN) / SIDE, (x - MARGIN) / SIDE
			self.row, self.col = row, col
		self.draw_cursor()

	def draw_cursor(self):
		self.board.delete("cursor")
		if int(self.row) >= 0 and int(self.col) >= 0:
			x0 = MARGIN + int(self.col) * SIDE + 1
			y0 = MARGIN + int(self.row) * SIDE + 1
			x1 = MARGIN + (int(self.col) + 1) * SIDE - 1
			y1 = MARGIN + (int(self.row) + 1) * SIDE - 1
			self.board.create_rectangle(
				x0, y0, x1, y1,
				outline="#ff3b00", tags="cursor", width=4
			)

	def key_pressed(self, event):
		if int(self.row) >= 0 and int(self.col) >= 0 and event.char in "1234567890":
			self.puzzle[int(self.row)][int(self.col)] = int(float(event.char))
			self.col, self.row = -1, -1
			self.draw_puzzle()
			self.draw_cursor()

	def draw_puzzle(self):
		self.board.delete("numbers")
		for i in range(0,9):
			for j in range(0,9):
				if self.puzzle[i][j] != 0:
					x = MARGIN + j * SIDE + SIDE / 2
					y = MARGIN + i * SIDE + SIDE / 2
					color = "white"
					self.board.create_text(
						x, y, text=self.puzzle[i][j], tags="numbers", fill=color, font="Consalos"
					)

	def draw_error(self):
		x0 = y0 = MARGIN + SIDE * 2
		x1 = y1 = MARGIN + SIDE * 7
		self.board.create_oval(
            x0, y0, x1, y1,
            tags="error", fill="dark red", outline="red"
        )
		
		x = y = MARGIN + 4 * SIDE + SIDE / 2
		self.board.create_text(
            x, y,
            text="You need at least\n   20 numbers!", tags="error",
            fill="white", font=("Arial", 10)
        )

	'''
	==============================================
		BOARD SOLVING STUFF THINGY OOGA BOOGA
	==============================================
	'''

	# returns a copy of board
	def deepCopy(self, board):
	    temp = [[0 for i in range(9)] for j in range(9)]
	    for i in range(len(board)):
	        for j in range(len(board[0])):
	            temp[i][j] = board[i][j]
	    return temp

	#find Next Empty slot/number
	def findNextEmpty(self, board):
	    for i in range(len(board)):
	        for j in range(len(board[0])):
	            if (board[i][j] == 0):
	                return (i, j)  # return location (row,col) AUTO GIVES NONE

		# Find the quadrant at position
	def quadrant(self, board, position):
	    x = position[0]
	    y = position[1]
	    if (x == 0 or x == 3 or x == 6):
	        x = x + 1
	    if (y == 0 or y == 3 or y == 6):
	        y = y + 1
	    tempTuple = (math.ceil(x / 3), math.ceil(y / 3))
	    return tempTuple
	
	# verify if column doesn't have specific number
	def validColumn(self, board, position, value):
	    x = position[0]
	    y = position[1]
	    for i in range(len(board)):
	        if (board[i][y] == value and i != x):
	            return False
	    return True

	#verify if row doesn't have specific number
	def validRow(self, board, position, value):
	    x = position[0]
	    y = position[1]
	    for j in range(len(board[0])):
	        if (board[x][j] == value and j != y):
	            return False
	    return True

	#verify if quadrant doesn't have specific value
	def validBox(self, board, position, value):
	    boxInfo = self.quadrant(board, position)
	    x = int((boxInfo[0] - 1) * 3)
	    y = int((boxInfo[1] - 1) * 3)
	    for i in range(x, x + 3):
	        for j in range(y, y + 3):
	            if ((board[i][j] == value) and (i != x and j != y)):
	                return False
	    return True

	#returns if there is no duplicate number in row, column or quadrant
	def valid_Move(self, board, position, value):
		return (self.validRow(board, position, value)
				and self.validColumn(board, position, value)
				and self.validBox(board, position, value))

	#solves board
	def solveBoard(self, board):
	    find = self.findNextEmpty(board)

	    if not find:
	        return True
	    else:
	        x, y = find

	    for i in range(1, 10):
	        if (self.valid_Move(board, find, i)):
	            board[x][y] = i
	            if self.solveBoard(board):
	                return True
	            board[x][y] = 0

	    return False

	def enoughValues(self, board):
		x = 0
		for i in range(len(board)):
			for j in range(len(board[0])):
				if (board[i][j] > 0):
					x += 1

		return (True if x >= 20 else False)

	def clear(self):
		self.puzzle = self.deepCopy(self.original)
		self.draw_puzzle()
		
	def fullSolve(self):
		if (not self.enoughValues(self.puzzle)):
			self.draw_error()
			return

		self.solveBoard(self.puzzle)
		self.draw_puzzle()

	def positionSolve(self):
		if (not self.enoughValues(self.puzzle)):
			self.draw_error()
			return

		x = int(self.row)
		y = int(self.col)
		board = self.deepCopy(self.puzzle)
		self.solveBoard(board)
		self.puzzle[x][y] = board[x][y]
		self.draw_puzzle()

root = tk.Tk()
root.title("Sudoku Solver")
app = Application(master=root)
app.mainloop()
