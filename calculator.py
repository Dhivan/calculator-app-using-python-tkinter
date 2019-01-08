from tkinter import *

root=Tk()
frame = Frame(root, width=500,height=500, bg= 'blue')
equal=""
equation = StringVar()
calculator = Label(root,textvariable=equation)
equation.set('Enter the variable')
calculator.grid(columnspan=4)

def press(num):
    global equal
    equal= equal+ str(num)
    equation.set(equal)

def equalpress():
    try:
        global equal
        total=str(eval(equal))
        equation.set(total)
    except:
        equation.set('Zero')
        equal=''

def clearpress():
    global equal
    equal=''
    equation.set('')


button0= Button(root,text='0', command= lambda:press(0))
button0.grid(row=4, column=1)
button1= Button(root,text='1', command= lambda:press(1))
button1.grid(row=1, column=0)
button2= Button(root,text='2', command= lambda:press(2))
button2.grid(row=1, column=1)
button3= Button(root,text='3', command= lambda:press(3))
button3.grid(row=1, column=2)
button4= Button(root,text='4', command= lambda:press(4))
button4.grid(row=2, column=0)
button5= Button(root,text='5', command= lambda:press(5))
button5.grid(row=2, column=1)
button6= Button(root,text='6', command= lambda:press(6))
button6.grid(row=2, column=2)
button7= Button(root,text='7', command= lambda:press(7))
button7.grid(row=3, column=0)
button8= Button(root,text='8', command= lambda:press(8))
button8.grid(row=3, column=1)
button9= Button(root,text='9', command= lambda:press(9))
button9.grid(row=3, column=2)
equal1= Button(root,text='=', command= equalpress)
equal1.grid(row=4, column=2)
clear= Button(root,text='C', command=clearpress)
clear.grid(row=4, column=0)
add= Button(root,text='+', command= lambda:press('+'))
add.grid(row=1, column=3)
sub= Button(root,text='-', command= lambda:press('-'))
sub.grid(row=2, column=3)
div= Button(root,text='%', command= lambda:press('%'))
div.grid(row=3, column=3)
mul= Button(root,text='*', command= lambda:press('*'))
mul.grid(row=4, column=3)


root.mainloop()
