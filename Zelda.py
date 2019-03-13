import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
class helloclass:
	"""docstring for helloclass"""
	def __init__(self):
		widget = button(None, text = 'press to quit', command = self.quit)
		widget.pack()
	def quit(self):
		print ("leaving now")
		import sys; sys.exit()
helloclass()
mainloop()