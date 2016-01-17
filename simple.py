try:
  import Tkinter              # Python 2
  import ttk
except ImportError:
  import tkinter as Tkinter   # Python 3
  import tkinter.ttk as ttk

root =Tk()
root.overrideredirect(1)
root.geometry("500x500")
welcome=Label(root,text="Generator" , bg="red",fg="white")
welcome.pack(fill=X)
topFrame=Frame(root)
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)
topFrame.pack()
button1=Button(topFrame, text="search",fg="gray")
button1.pack(side=LEFT)
button2=Button(bottomFrame, text="Exit",fg="gray")
button2.pack()
fb = ttk.Frame()

fb.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)

  pb_hd = ttk.Progressbar(ft, orient='horizontal', mode='determinate')


  pb_hd.start(10)
root.mainloop()
