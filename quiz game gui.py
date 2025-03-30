import tkinter as tk
from tkinter import messagebox
import random
score = 0
window = tk.Tk()
def page1():
  global window
  window.destroy()
  window = tk.Tk()
  window.title("Math quiz")
  window.geometry("300x100")
  fn = tk.Label(text="All are integer")
  fn.place(x=0,y=0)
  npage=tk.Button(text="Start",command=page2)
  npage.place(x=0,y=70)

def page2():
  global window
  global ans
  global score
  global total
  global scoresign
  global equation
  global notes
  window.destroy()
  window = tk.Tk()
  window.title("Start")
  window.geometry("300x150")
  scorestring = str(score)
  total =0
  ans =0
  sign = tk.Label(text="Score 10 points to win")
  sign.place(x=0,y=0)
  scoresign = tk.Label(text="Score:"+scorestring)
  scoresign.place(x=200,y=0)
  equation = tk.Label(text="")
  equation.place(x=0,y=25)
  notes = tk.Label(text='')
  notes.place(x=0,y=100)
  question()
  
def question():
  global ans
  global score
  global total
  global scoresign
  global equation
  global anstext
  global qbutton
  num1 = random.randint(1,50)
  num2 = random.randint(1,50)
  symbol = random.randint(1,4)
  scorestring = str(score)
  scoresign.config(text="Score:"+scorestring)
  if symbol ==1:
    equation.config(text=str(num1)+'+'+str(num2)+'=')
    total = num1 + num2
    anslabel = tk.Label(text="ans:")
    anslabel.place(x=0,y=50)
    anstext = tk.Entry()
    anstext.place(x=100,y=50)
    ans = (anstext.get())
    qbutton = tk.Button(text="Check",command=correct)
    qbutton.place(x=0,y=75)
  if symbol ==2:
    equation.config(text=str(num1)+'-'+str(num2)+'=')
    total = num1 - num2
    anslabel = tk.Label(text="ans:")
    anslabel.place(x=0,y=50)
    anstext = tk.Entry()
    anstext.place(x=100,y=50)
    ans = (anstext.get())
    qbutton = tk.Button(text="Check",command=correct)
    qbutton.place(x=0,y=75)
  if symbol ==3:
    equation.config(text=str(num1)+'X'+str(num2)+'=')
    total = num1 * num2
    anslabel = tk.Label(text="ans:")
    anslabel.place(x=0,y=50)
    anstext = tk.Entry()
    anstext.place(x=100,y=50)
    ans = anstext.get()
    qbutton = tk.Button(text="Check",command=correct)
    qbutton.place(x=0,y=75)
  if symbol ==4:
    equation.config(text=str(num1)+'/'+str(num2)+'=')
    total = num1 // num2
    anslabel = tk.Label(text="ans:")
    anslabel.place(x=0,y=50)
    anstext = tk.Entry()
    anstext.place(x=100,y=50)
    ans = (anstext.get())
    qbutton = tk.Button(text="Check",command=correct)
    qbutton.place(x=0,y=75)

def correct():
  global ans
  global score
  global total
  global notes
  global anstext
  global qbutton
  ans = anstext.get()
  qbutton = tk.Button(text="Check",command=None)
  qbutton.place(x=0,y=75)
  if ans == str(total):
    score+=1
    notes.config(text='You are correct')
  else:
    score-=1
    notes.config(text='You are incorrect and the correct answer is'+str(total))
    
  if score == 10:
    messagebox.showinfo("title","You win!")
  nbutton = tk.Button(text="Next?",command=page2)
  nbutton.place(x=100,y=75)
  


page1()
tk.mainloop()

