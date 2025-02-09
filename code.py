from tkinter import *
from tkinter.messagebox import *

root=Tk()
root.title('Calculator')
root.geometry('350x600')
root.configure(background='black')
root.grid_rowconfigure(0,weight=2)
root.grid_rowconfigure(1,weight=2)
root.grid_rowconfigure(2,weight=6)
root.grid_columnconfigure(0,weight=1)
# root.resizable(False, False) 
prob_display=Frame(root, bg="black")
prob_display.grid(row=0,column = 0, sticky = "nesw")
ans_display=Frame(root, bg="black")
ans_display.grid(row=1,column = 0, sticky = "nesw")
calci=Frame(root, bg="black")
calci.grid(row=2,column = 0, sticky = "nesw")
for i in range (4): calci.grid_columnconfigure(i,weight=1)
for i in range (6): calci.grid_rowconfigure(i,weight=1)
myfont={'font' :('helvica', 20),'fg' : 'white','bg':'gray25'}

string=''
oper=['/','*','+','-']
l=['/','*','+','-','(',')']
nums=['1','2','3','4','5','6','7','8','9','0','.']
num_string = StringVar()
history_ans=[]
history_prob=[]
answer= DoubleVar()

def num(key):
    global string, answer,num_string,check_string
    if key == '': 
        string=string[1:1] 
        answer.set('')
    if key == " ": 
        string=string[:-1]
        key=''
        answer.set('')
    if key in oper:
        if len(string)==0:showerror("Error", "Invalid format used.")
        try: 
            if string[-1] in oper : string=string[:-1]
        except IndexError: key=''
    if   key=='.' and  string=='' : key='0.'
    else:
        try :
            if key=='.' and (string[-1] in oper or string=='') : key='0.'
        except IndexError: pass
    string=string+key
    check_string=string
    for i in l: check_string=check_string.replace(i, ",")
    check_string=check_string.split(',')
    check_string[:] = (value for value in check_string if value != '') 
    for i in range (len(check_string)):
        try:aaa=len(check_string[i].split('.')[1]) 
        except IndexError: aaa=0
        if len(check_string[i].split('.')[0])+aaa <=15 :pass
        else: string=string[:-1]; showerror("Error", "Can't enter more than 15 digits.")
        if aaa<=10: pass
        else: string=string[:-1];showerror("Error", "Can't enter more than 10 digits after decimal point.")
    num_string.set(string)
    a=prob_label.cget('text')
    try: 
        if len(check_string)==1:answer.set('')
        else:
            answer.set(eval(num_string.get()))
            ans_label.config(textvariable=answer)
    except SyntaxError: answer.set('')

def ans():
    global string,check_string
    if len(check_string)==1: answer.set('')
    else:
        try: 
            if str(answer.get()).split('.')[1]=='0': string=str(answer.get()).split('.')[0]
            else: string=str(answer.get())
            history_prob.append(num_string.get())
            history_ans.append('='+string)
            num_string.set(string)
            answer.set('')
        except TclError: showerror("Error", "Invalid format used.")
      
def ops():
    global memory_frame,button2
    memory_frame = Frame(calci, bg="gray8")
    memory_frame.grid(row=1,column = 0, rowspan=5,columnspan=3,sticky = "nesw")
    button2 = Button(calci, text = 'Back',cnf=myfont,font =('helvica', 15),bd=0,bg='black',command=destroyy)
    button2.grid(column=0,row=0,sticky = "nesw")
    clearhistory_button=Button(memory_frame, text = 'Clear History',cnf=myfont,font =('helvica', 15),command=ops2)
    clearhistory_button.pack(side='bottom',anchor="s",fill='x')
    for i in range (len(history_ans)):
        Label(memory_frame,text=history_prob[len(history_ans)-i-1],cnf=myfont,font =('helvica', 14),fg = 'grey',bg='gray8').pack(anchor='e')
        Label(memory_frame,text=history_ans[len(history_ans)-i-1],cnf=myfont,font =('helvica', 14),bg='gray8').pack(anchor='e')
def destroyy():
    memory_frame.destroy()
    button2.destroy()
def ops2():
    history_prob.clear()
    history_ans.clear()
    destroyy()
prob_label=Label(prob_display,text='problem',textvariable=num_string,font =('helvica', 23),fg = 'white',bg='black')
prob_label.pack(side="right",anchor="e")
ans_label=Label(ans_display,text='',font =('helvica', 15),fg = 'grey',bg='black')
ans_label.pack(side="right",anchor="e")

button = Button(calci, text = 'M',font =('helvica', 15),fg = 'white',bd=0,bg='black',command=ops).grid(column=0,row=0,sticky = "nesw")
button = Button(calci, text = '⌫',font =('helvica', 15),fg = 'white',bd=0,bg='black',command=lambda: num(" ")).grid(column=3,row=0,sticky = "nesw")

# operational buttons
button = Button(calci, text = '÷',cnf=myfont,bg='orange',command=lambda: num("/")).grid(column=3,row=1,sticky = "nesw")
button = Button(calci, text = 'x',cnf=myfont,bg='orange',command=lambda: num("*")).grid(column=3,row=2,sticky = "nesw")
button = Button(calci, text = '-',cnf=myfont,bg='orange',command=lambda: num("-")).grid(column=3,row=3,sticky = "nesw")
button = Button(calci, text = '+',cnf=myfont,bg='orange',command=lambda: num("+")).grid(column=3,row=4,sticky = "nesw")

# functional buttons
button = Button(calci, text = 'AC',font =('helvica',15),fg = 'black',bg='gray50',command=lambda: num('')).grid(column=0,row=1 ,sticky = "nesw")
button = Button(calci, text = '=',cnf=myfont,bg='orange',command=ans).grid(column=3,row=5,sticky = "nesw")
button = Button(calci, text = '(',cnf=myfont,fg = 'black',bg='gray50',command=lambda: num("(")).grid(column=1,row=1,sticky = "nesw")
button = Button(calci, text = ')',cnf=myfont,fg = 'black',bg='gray50',command=lambda: num(")")).grid(column=2,row=1,sticky = "nesw")

# num buttons
button = Button(calci, text = 7,cnf=myfont,command=lambda: num("7")).grid(column=0,row=2,sticky = "nesw")
button = Button(calci, text = 8,cnf=myfont,command=lambda: num("8")).grid(column=1,row=2,sticky = "nesw")
button = Button(calci, text = 9,cnf=myfont,command=lambda: num("9")).grid(column=2,row=2,sticky = "nesw")
button = Button(calci, text = 4,cnf=myfont,command=lambda: num("4")).grid(column=0,row=3,sticky = "nesw")
button = Button(calci, text = 5,cnf=myfont,command=lambda: num("5")).grid(column=1,row=3,sticky = "nesw")
button = Button(calci, text = 6,cnf=myfont,command=lambda: num("6")).grid(column=2,row=3,sticky = "nesw")
button = Button(calci, text = 1,cnf=myfont,command=lambda: num("1")).grid(column=0,row=4,sticky = "nesw")
button = Button(calci, text = 2,cnf=myfont,command=lambda: num("2")).grid(column=1,row=4,sticky = "nesw")
button = Button(calci, text = 3,cnf=myfont,command=lambda: num("3")).grid(column=2,row=4,sticky = "nesw")
button = Button(calci, text = 0,cnf=myfont,command=lambda: num("0")).grid(column=0,row=5,columnspan=2,sticky = "nesw")
button = Button(calci, text = '.',cnf=myfont,command=lambda: num(".")).grid(column=2,row=5,sticky = "nesw")

root.mainloop()