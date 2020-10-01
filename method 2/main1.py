from all_filter import all_filter
import tkinter
from tkinter import *
import cv2

class App:

	def __init__(self, window, window_title, video_source=0):
		self.window = window
		self.window.title(window_title)
		self.video_source = video_source
		# window.geometry("1920x1080+0+0")
		window.geometry("240x700+0+0")

		# open video source (by default this will try to open the computer webcam)
		# self.vid = MyVideoCapture(self.video_source)
		self.a = self.gui(self.window)


	def gui(self, window):

		self.a = DoubleVar()
		self.b = DoubleVar()
		self.c = DoubleVar()
		self.d = DoubleVar()
		self.e = DoubleVar()
		self.f = DoubleVar()
		self.g = DoubleVar()
		self.h = DoubleVar()

		self.btn_start = tkinter.Button(window, text="start", bg="light green", font=("", 10), command=self.openCam)
		self.btn_start.place(x=10, y=20, width=200, height=40)

		self.w1 = tkinter.Scale(self.window, from_=20, to=100, orient='horizontal',label="threshold",variable = self.a)
		self.w1.place(x=10, y=140, width=200, height=60)

		self.w2 = tkinter.Scale(self.window, from_=0, to=2, orient='horizontal',label="sobel_filterX",variable = self.b)
		self.w2.place(x=10, y=200, width=200, height=60)

		self.w3 = tkinter.Scale(self.window, from_=1, to=255, orient='horizontal',label="asd",variable = self.c)
		self.w3.place(x=10, y=260, width=200, height=60)

		self.w4 = tkinter.Scale(self.window, from_=1, to=100, orient='horizontal',label="asd",variable = self.d)
		self.w4.place(x=10, y=320, width=200, height=60)

		self.w5 = tkinter.Scale(self.window, from_=1, to=100, orient='horizontal',label="asd",variable = self.e)
		self.w5.place(x=10, y=380, width=200, height=60)

		self.w6 = tkinter.Scale(self.window, from_=1, to=200, orient='horizontal',label="asd",variable = self.f)
		self.w6.place(x=10, y=440, width=200, height=60)

		self.w6 = tkinter.Scale(self.window, from_=1, to=255, orient='horizontal',label="asd",variable = self.g)
		self.w6.place(x=10, y=500, width=200, height=60)

		self.w6 = tkinter.Scale(self.window, from_=0, to=255, orient='horizontal',label="asd",variable = self.h)
		self.w6.place(x=10, y=560, width=200, height=60)

		# After it is called once, the update method will be automatically called every delay milliseconds
		self.delay = 15

		self.window.mainloop()

	def openCam(self, video_source=0):

		self.delay = 15
		self.update()

	def update(self):
		a = int(self.a.get())
		b = int(self.b.get())
		c = int(self.c.get())
		d = int(self.d.get())
		e = int(self.e.get())
		f = int(self.f.get())
		g = int(self.g.get())
		h = int(self.h.get())
		ret, frame = cap.read()
		# frame1, thresh1, frame3, a, b, c = all_filter(frame,scale_percent = 20,
		# 												frame_val=2,
		# 												thresh1_val =170,
		# 												gaussian1_val= 40,
		# 												sobel_val1 = 13,
		# 												sobel_val2 = 30,
		# 												thresh_val =70)
		frame1, thresh1, frame3, pix_a, pix_b, pix_c = all_filter(frame,scale_percent = a,
																		frame_val=      b,
																		thresh1_val =   c,
																		gaussian1_val=  d,
																		sobel_val1 =    e,
																		sobel_val2 =    f,
																		thresh_val =    g)
		
		c = (pix_b-pix_a)/pix_b*100
		if c >= 80:
			print (f'bottle has more than {int(c)}')

		cv2.imshow('frame1',frame1)
		cv2.imshow('thresh1',thresh1)
		cv2.imshow('frame3',frame3)
		cv2.imshow('frame',frame)
		# cv2.waitKey(0)

		self.window.after(self.delay, self.update)


path = 'F:/sliit/Y 4/Y4 sem 2 2020/image processing/assigninet/PICS/vid2.MP4'
path = 'F:/sliit/Y 4/Y4 sem 2 2020/image processing/assigninet/PICS/5.JPG'
cap = cv2.VideoCapture(0)
App(tkinter.Tk(), "Tkinter and OpenCV",video_source=cap)	