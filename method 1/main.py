from all_filters import all_filters
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
		self.i = DoubleVar()

		self.btn_start = tkinter.Button(window, text="start", bg="light green", font=("", 10), command=self.openCam)
		self.btn_start.place(x=10, y=20, width=200, height=40)

		self.w1 = tkinter.Scale(self.window, from_=20, to=100, orient='horizontal',label="threshold",variable = self.a)
		self.w1.place(x=10, y=140, width=200, height=60)

		self.w2 = tkinter.Scale(self.window, from_=1, to=255, orient='horizontal',label="sobel_filterX",variable = self.b)
		self.w2.place(x=10, y=200, width=200, height=60)

		self.w3 = tkinter.Scale(self.window, from_=1, to=255, orient='horizontal',label="asd",variable = self.c)
		self.w3.place(x=10, y=260, width=200, height=60)

		self.w4 = tkinter.Scale(self.window, from_=1, to=255, orient='horizontal',label="asd",variable = self.d)
		self.w4.place(x=10, y=320, width=200, height=60)

		self.w5 = tkinter.Scale(self.window, from_=1, to=255, orient='horizontal',label="asd",variable = self.e)
		self.w5.place(x=10, y=380, width=200, height=60)

		self.w6 = tkinter.Scale(self.window, from_=1, to=255, orient='horizontal',label="asd",variable = self.f)
		self.w6.place(x=10, y=440, width=200, height=60)

		self.w6 = tkinter.Scale(self.window, from_=1, to=255, orient='horizontal',label="asd",variable = self.g)
		self.w6.place(x=10, y=500, width=200, height=60)	

		self.w6 = tkinter.Scale(self.window, from_=0, to=20, orient='horizontal',label="asd",variable = self.h,resolution = 2)
		self.w6.place(x=10, y=560, width=200, height=60)

		self.w6 = tkinter.Scale(self.window, from_=0, to=300, orient='horizontal',label="asd",variable = self.i,resolution = 1)
		self.w6.place(x=10, y=620, width=200, height=60)

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
		h = (int(self.h.get())+1)
		i = int(self.i.get())
		ret, frame = cap.read()

														# all_filters(scale_percent = 20,
														# 			threshVal1 = 120,
														# 			threshVal2 = 255,
														# 			thresholdVal1_inv = 70,
														# 			thresholdVal2_inv = 255,
														# 			thresholdthresholdVal3 = 0,
														# 			thresholdVal4 = 100,
														# 			median_filter_size = 5)


		frame2, frame3, frame4, a,b,  ratio_full = all_filters(frame,scale_percent     = a,
																	threshVal1         = b,
																	threshVal2         = c,
																	thresholdVal1_inv  = d,
																	thresholdVal2_inv  = e,
																	thresholdVal3      = f,
																	thresholdVal4      = g,
																	median_filter_size = h,
																	blackign           = i)
		
		if ratio_full>= 80:
			print('ratio_full is more than 80% and to be exact ',ratio_full,'%')
			drawer(frame4)
		
		# print (frame2)
		# c = (pix_b-pix_a)/pix_b*100
		# if c >= 80:
		# 	print (f'bottle has more than {int(c)}')

		cv2.imshow('frame1',frame2)
		cv2.imshow('thresh1',frame3)
		cv2.imshow('frame3',frame4)
		# cv2.imshow('frame',frame)
		# cv2.waitKey(0)

		self.window.after(self.delay, self.update)





path = 'PICS/26.JPG'
cap = cv2.VideoCapture(0)
App(tkinter.Tk(), "Tkinter and OpenCV",video_source=cap)	