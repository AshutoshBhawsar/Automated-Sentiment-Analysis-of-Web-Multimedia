
import threading

from MAIN import *
from tkinter import *
from get_predict import get_prediction

#---------------------------------------

def call_func():
	media_url = get_url()

	lbl3.configure(text="Fetching...")
	p.download_mp3(media_url)
	e.extract_sub()

	lbl3.configure(text="Processing...")
	q.convert()
	r.convert()

	lbl3.configure(text="Classifying...")
	t.perform_prediction()
	t.find_unique_words()
	lbl3.configure(text="Done!")

	a, b, c = get_prediction()
	lbl3.configure(text="The media contains "+a+", "+b+", "+c)

def clicked():
	res = "Got URL: " + txt.get()
	lbl2.configure(text=res)
	file = open("url.txt", "w")
	file.write(""+txt.get())
	file.close()

	t1.start()

def clicked2():
	t1._is_stopped = True
	t1._stop()
	#t1.join()
	lbl3.configure(text="Stopped!")

#---------------------------------------
t1 = threading.Thread(target=call_func, args=())

window = Tk()
window.title("Automated Sentiment Analysis of Web Multimedia!")
window.geometry('800x480')

col_count, row_count = 5, 5

for col in range(col_count):
	window.grid_columnconfigure(col, minsize=60)

for row in range(row_count):
	window.grid_rowconfigure(row, minsize=60)

lbl1 = Label(window, text="Enter your URL here: ")
lbl1.grid(column=1, row=0)

txt = Entry(window,width=60)
txt.grid(column=2, row=0)

# https://www.youtube.com/watch?v=PHxvMLoKRWg

btn = Button(window, text="Start", command=clicked)
btn.grid(column=3, row=0)
btn = Button(window, text="Stop", command=clicked2)
btn.grid(column=4, row=0)

lbl2 = Label(window, text="")
lbl2.grid(column=2, row=1)

lbl4 = Label(window, text="Progress:")
lbl4.grid(column=1, row=2)

lbl3 = Label(window, text="")
lbl3.grid(column=2, row=2)

window.mainloop()
