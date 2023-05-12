###########################################################################################################################################
                                                    #CODE CLAUSE INTERNSHIP 
                                            #CALCULATOR IN PYTHON BY VATALA PHALGUN

###########################################################################################################################################
                                            #IMPORTING TKINTER MODULE AND SETTING ROOT 
from tkinter import *

root = Tk()
root.geometry("300x400")
root.title("CALCULATOR")

bar = Entry(root,width=22,font=("Ubuntu",18,"normal"),fg="black",bg="white")
bar.place(x=5,y=3)

X = 75
Y = 75 

root.minsize((X*5)-75,(5*Y)+20)
root.maxsize((X*5)-75,(5*Y)+20)

#########################################################################################################################################
                                                          #INSERT FUNCTION TO INSERT A NUMBER OR OPERATOR 
def insert(num):
    bar['fg']="black"
    text = bar.get()
    if (text.split() == []) and (num=="/" or num=="*" or num==")"):
        num = ''
    elif (text.endswith('*')) and (num=="+" or num=="-" or num=="/" or num=="*"):
        Back()
    elif (text.endswith('/')) and (num=="+" or num=="-" or num=="/" or num=="*"):
        Back()
    elif (text.endswith('+')) and (num=="+" or num=="-" or num=="/" or num=="*"):
        Back()
    elif (text.endswith('-')) and (num=="+" or num=="-" or num=="/" or num=="*"):
        Back()
    elif (text.endswith('.')) and (num=="." or num=="+" or num=="-" or num=="/" or num=="*"):
        num = ''
    bar.insert(END,num)
                                                         #BACK FUNCTION TO DELETE THE LAST CHARACTER ON DISPLAY

def Back():
    bar['fg']="blue"
    try:
        text = bar.get()
        l = list(text)
        l.pop()
        Text = ""
        for i in range(len(l)):
            Text += l[i]
        bar.delete(0,END)
        bar.insert(0,Text)
    except:
        None 
                                                         #DELETE FUNCTION TO CLEAR THE DISPLAY
        
def Delete():
    bar['fg']="blue"
    bar.delete(0,END)
                                                         #BRACKET CHECKER 

def BracketCheck():
    text = str(bar.get())
    Text = list(text)
    a=0
    for i in range(len(Text)):
        if Text[i] == "(":
            a+=1
    b=0
    for i in range(len(Text)):
        if Text[i] == ")":
            b+=1
    Add = a-b
    return Add
                                                         #ANSWER FUNCTION TO EVALUATE THE ANSWER 

def Answer():
    text = str(bar.get())

    Add = BracketCheck()
    if Add>0:
        bar.insert(END,Add*")")
    else:
        try:
            answer = eval(text) #eval function is responsible for evaluating the arithmetic operation and stores result in answer 
            Delete()
            bar.insert(0,answer)
            bar['fg'] = "forestgreen"
        except:
            bar['fg'] = "red"

#####################################################################################################################################
                                                   #BUTTONS FOR NUMBERS

n1 = Button(root,text="1",font=("Comic Sans",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("1"))
n1.place(x=0,y=Y+20)

n2 = Button(root,text="2",font=("Comic Sans",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("2"))
n2.place(x=X,y=Y+20)

n3 = Button(root,text="3",font=("Comic Sans",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("3"))
n3.place(x=2*X,y=Y+20)

n4 = Button(root,text="4",font=("Comic Sans",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("4"))
n4.place(x=0,y=(2*Y)+20)

n5 = Button(root,text="5",font=("Comic Sans",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("5"))
n5.place(x=X,y=(2*Y)+20)

n6 = Button(root,text="6",font=("Comic Sans",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("6"))
n6.place(x=2*X,y=(2*Y)+20)

n7 = Button(root,text="7",font=("Comic Sans",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("7"))
n7.place(x=0,y=(3*Y)+20)

n8 = Button(root,text="8",font=("Comic Sans",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("8"))
n8.place(x=X,y=(3*Y)+20)

n9 = Button(root,text="9",font=("Comic Sans",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("9"))
n9.place(x=2*X,y=(3*Y)+20)

n0 = Button(root,text="0",font=("Comic Sans",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("0"))
n0.place(x=X,y=(4*Y)+20)

dot = Button(root,text=".",font=("Comic Sans",16,"bold"),padx = 23,pady = 16,bd = 4,bg="gray",command=lambda:insert("."))
dot.place(x=0,y=(4*Y)+20)

equal = Button(root,text="=",font=("Comic Sans",16,"bold"),padx = 20,pady = 16,bd = 4,bg="forestgreen",command=Answer)
equal.place(x=2*X,y=(4*Y)+20)

###################################################################################################################################
                                                   #BUTTONS FOR OPERATIONS

mul = Button(root,text="*",font=("Comic Sans",16,"bold"),padx = 23,pady = 16,bd = 4,bg="orange",command=lambda:insert("*"))
mul.place(x=3*X,y=Y+20)

div = Button(root,text="/",font=("Comic Sans",16,"bold"),padx = 23,pady = 16,bd = 4,bg="orange",command=lambda:insert("/"))
div.place(x=3*X,y=(2*Y)+20)

plus = Button(root,text="+",font=("Comic Sans",16,"bold"),padx = 20,pady = 16,bd = 4,bg="orange",command=lambda:insert("+"))
plus.place(x=3*X,y=(3*Y)+20)

minus = Button(root,text="-",font=("Comic Sans",16,"bold"),padx = 23,pady = 16,bd = 4,bg="orange",command=lambda:insert("-"))
minus.place(x=3*X,y=(4*Y)+20)

###################################################################################################################################
                                                  #UPPER BUTTONS 

AC = Button(root,text="AC",font=("Comic Sans",16,"bold"),padx = 14,pady = 6,bd = 4,bg="light yellow",command=Delete)
AC.place(x=0,y=Y-35)

back = Button(root,text=u"\u2190",font=("Comic Sans",16,"bold"),padx = 20,pady = 6,bd = 4,bg="light yellow",command=Back)
back.place(x=X,y=Y-35)

Open = Button(root,text="(",font=("Comic Sans",16,"bold"),padx = 23,pady = 6,bd = 4,bg="light yellow",command=lambda:insert("("))
Open.place(x=2*X,y=Y-35)

Close = Button(root,text=")",font=("Comic Sans",16,"bold"),padx = 23,pady = 6,bd = 4,bg="light yellow",command=lambda:insert(")"))
Close.place(x=3*X,y=Y-35)

root.mainloop()
                                                #END OF THE CODE 

###################################################################################################################################
                                                  