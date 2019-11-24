#--------------------------------------------------------------
#this part is based on youtube tutorial on tkinter by sentdex
#you can find the tutorial on his youtube
#https://www.youtube.com/user/sentdex
#--------------------------------------------------------------

import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import style

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


LARGE_FONT = ("Verdana", 12)

class SelfDevApp(tk.Tk):

	def __init__(self, *args, **kwargs):

		tk.Tk.__init__(self, *args, **kwargs)

		tk.Tk.iconbitmap(self, "penguin16.ICO")
		tk.Tk.wm_title(self, "Self-dev app client")

		container = tk.Frame(self)

		container.pack(side="top", fill="both", expand="True")

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

	
		for F in (StartPage, PageOne, PageTwo, PageThree):

			frame = F(container, self) 
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()


class StartPage(tk.Frame):


	def __init__(self, parent, controller):

		def button_func(txt, page):
			return ttk.Button(self, text=txt, 
							command=lambda: controller.show_frame(page)).pack()
		
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Start Page", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = button_func("Visit Page1", PageOne)
		button2 = button_func("Visit Page2", PageTwo)
		button3 = button_func("Graph Page", PageThree)

class PageOne(tk.Frame):
	def __init__(self, parent, controller):

		def button_func(txt, page):
			return ttk.Button(self, text=txt, 
							command=lambda: controller.show_frame(page)).pack()

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page One", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = button_func("Back to home", StartPage)
		button2 = button_func("Page Two", PageTwo)
		button3 = button_func("Graph Page",PageThree)

class PageTwo(tk.Frame):
	def __init__(self, parent, controller):

		def button_func(txt, page):
			return ttk.Button(self, text=txt, 
							command=lambda: controller.show_frame(page)).pack()

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page Two", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = button_func("Back to home", StartPage)
		button2 = button_func("Page One", PageOne)
		button3 = button_func("Graph Page", PageThree)

class PageThree(tk.Frame):
	def __init__(self, parent, controller):

		def button_func(txt, page):
			return ttk.Button(self, text=txt, 
							command=lambda: controller.show_frame(page)).pack()

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
		label.pack(pady=10, padx=10)

		button1 = button_func("Back to home", StartPage)

		f = Figure(figsize=(5,5), dpi=100)
		a = f.add_subplot(111)
		a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

		canvas = FigureCanvasTkAgg(f, self)
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		toolbar = NavigationToolbar2Tk(canvas, self)
		toolbar.update()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
		#sentdex used _tkcanvas instead of get_tk_widget(), I wonder if that changes anything

app = SelfDevApp()
app.mainloop()
