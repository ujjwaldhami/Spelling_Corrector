from tkinter import *
from textblob import TextBlob

def check():
    b=TextBlob(text_input.get())
    corrected_text=Label(text=str(b.correct()),font=18)
    corrected_text.pack(pady=20)


root=Tk()
root.title('Spelling Corrector')
root.geometry("900x500")
root.config(bg='black')

text=Label(text='Enter your text here:',bg='black',fg='white',font=17)
text.pack(pady=(20,10))

text_input=Entry(width=70,font=14)
text_input.pack()

btn=Button(text='Click',width=10,font=20,command=check)
btn.pack(pady=15)


root.mainloop()

