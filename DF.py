from tkinter import *
main=Tk()
main.geometry("1920x1080")
main.config(bg="black")
main.title("Determinant Founder")
#2x2 DF
def df2x2():
    df=Tk()
    df.geometry("1920x1080")
    df.title("2x2 Determinant")
    df.config(bg="black")
    def dfp():
        try:
            ans=str((int(e1.get())*int(e4.get()))-(int(e2.get())*int(e3.get())))
            ans1=Label(df,text="Answer is \n"+ans,bg="black",fg="white",font="mono 50 bold").place(x=800,y=600)
        except :
            pass
            
    a1=Label(df,text="2x2 Determinant",font="arial 50 underline bold",bg="black",fg="white").pack()
    c1=Canvas(df,width=9,height=320,bg="white").place(x=1200,y=100)
    c2=Canvas(df,width=9,height=320,bg="white").place(x=750,y=100)
    e1=Entry(df,width=5,font="arial 40",bg="yellow",fg="black")
    e1.place(x=800,y=150)
    e2=Entry(df,width=5,font="arial 40",bg="yellow",fg="black")
    e2.place(x=1000,y=150)
    e3=Entry(df,width=5,font="arial 40",bg="yellow",fg="black")
    e3.place(x=800,y=300)
    e4=Entry(df,width=5,font="arial 40",bg="yellow",fg="black")
    e4.place(x=1000,y=300)
    b1=Button(df,text="Answer",command=dfp,bg="maroon",fg="white",font="arial 40").place(x=880,y=500)
    df.mainloop()

def df3x3():
    df=Tk()
    df.geometry("1920x1080")
    df.title("3x3 Determinant")
    df.config(bg="black")
    def dfp():
        try:
            co1=(int(e.get())*int(i.get()))-(int(f.get())*int(h.get()))
            
            co3=(int(d.get())*int(h.get()))-(int(e.get())*int(g.get()))
            
            co2=(int(d.get())*int(i.get()))-(int(f.get())*int(g.get()))
            
            ans=str(int(a.get())*co1-int(b.get())*co2+int(c.get())*co3)
            ans1=Label(df,text="Answer is \n"+ans,bg="black",fg="white",font="mono 50 bold").place(x=800,y=750)
        except:
            pass
    a1=Label(df,text="3x3 Determinant",font="arial 50 underline bold",bg="black",fg="white").pack()
    c1=Canvas(df,width=10,height=480,bg="white").place(x=1300,y=100)
    c2=Canvas(df,width=10,height=480,bg="white").place(x=650,y=100)
    a=Entry(df,width=5,font="arial 40",bg="yellow",fg="black")
    a.place(x=700,y=150)
    b=Entry(df,width=5,font="arial 40",bg="yellow",fg="black")
    b.place(x=900,y=150)
    c=Entry(df,width=5,font="arial 40",bg="yellow",fg="black")
    c.place(x=1100,y=150)
    d=Entry(df,width=5,font="arial 40",bg="yellow",fg="black")
    d.place(x=700,y=300)
    e=Entry(df,width=5,font="arial 40",bg="yellow",fg="black")
    e.place(x=900,y=300)
    f=Entry(df,width=5,font="arial 40",bg="yellow",fg="black")
    f.place(x=1100,y=300)
    g=Entry(df,width=5,font="arial 40",bg="yellow",fg="black")
    g.place(x=700,y=450)
    h=Entry(df,width=5,font="arial 40",bg="yellow",fg="black")
    h.place(x=900,y=450)
    i=Entry(df,width=5,font="arial 40",bg="yellow",fg="black")
    i.place(x=1100,y=450)
    
    b1=Button(df,text="Answer",command=dfp,bg="maroon",fg="white",font="arial 40").place(x=880,y=650)
    df.mainloop()
Label(main,text="Determinant Founder\n\n",bg="black",fg="white",font="mono 50 bold underline").pack()
Button(main,text="2x2 Determinant",command=df2x2,bg="maroon",fg="white",font="arial 40").pack()
Label(main,text="\n",bg="black").pack()
Button(main,text="3x3 Determinant",command=df3x3,bg="maroon",fg="white",font="arial 40").pack()
main.mainloop()
