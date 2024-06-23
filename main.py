from tkinter import *

def df2x2():
    df = Toplevel()
    df.title("2x2 Determinant")
    df.config(bg="black")

    def calculate_determinant():
        try:
            ans = str((int(e1.get()) * int(e4.get())) - (int(e2.get()) * int(e3.get())))
            result_label.config(text="Answer is \n" + ans)
        except ValueError:
            result_label.config(text="Invalid input")

    Label(df, text="2x2 Determinant", font="arial 50 underline bold", bg="black", fg="white").grid(row=0, column=0, columnspan=3)

    e1 = Entry(df, width=5, font="arial 30", bg="yellow", fg="black")
    e1.grid(row=2, column=1, padx=50,pady=10)

    e2 = Entry(df, width=5, font="arial 30", bg="yellow", fg="black")
    e2.grid(row=3, column=1, padx=50,pady=10)

    e3 = Entry(df, width=5, font="arial 30", bg="yellow", fg="black")
    e3.grid(row=2, column=2, padx=50,pady=10)

    e4 = Entry(df, width=5, font="arial 30", bg="yellow", fg="black")
    e4.grid(row=3, column=2, padx=50,pady=10)

    result_label = Label(df, text="", bg="black", fg="white", font="mono 30 bold")
    result_label.grid(row=4, column=0, columnspan=3, pady=20)

    calculate_button = Button(df, text="Calculate", command=calculate_determinant, bg="maroon", fg="white", font="arial 30")
    calculate_button.grid(row=5, column=0, columnspan=3, pady=20)

    df.mainloop()

def df3x3():
    df = Toplevel()
    df.title("3x3 Determinant")
    df.config(bg="black")

    def calculate_determinant():
        try:
            a_val = int(a.get())
            b_val = int(b.get())
            c_val = int(c.get())
            d_val = int(d.get())
            e_val = int(e.get())
            f_val = int(f.get())
            g_val = int(g.get())
            h_val = int(h.get())
            i_val = int(i.get())

            co1 = a_val * (e_val * i_val - f_val * h_val)
            co2 = b_val * (d_val * i_val - f_val * g_val)
            co3 = c_val * (d_val * h_val - e_val * g_val)
            
            ans = str(co1 - co2 + co3)
            result_label.config(text="Answer is \n" + ans)
        except ValueError:
            result_label.config(text="Invalid input")

    Label(df, text="3x3 Determinant", font="arial 50 underline bold", bg="black", fg="white").grid(row=0, column=0, columnspan=6)

    a = Entry(df, width=5, font="arial 30", bg="yellow", fg="black")
    a.grid(row=2, column=1,pady=10)

    b = Entry(df, width=5, font="arial 30", bg="yellow", fg="black")
    b.grid(row=2, column=2,pady=10)

    c = Entry(df, width=5, font="arial 30", bg="yellow", fg="black")
    c.grid(row=2, column=3,pady=10)

    d = Entry(df, width=5, font="arial 30", bg="yellow", fg="black")
    d.grid(row=3, column=1,pady=10)

    e = Entry(df, width=5, font="arial 30", bg="yellow", fg="black")
    e.grid(row=3, column=2,pady=10)

    f = Entry(df, width=5, font="arial 30", bg="yellow", fg="black")
    f.grid(row=3, column=3,pady=10)

    g = Entry(df, width=5, font="arial 30", bg="yellow", fg="black")
    g.grid(row=4, column=1,pady=10)

    h = Entry(df, width=5, font="arial 30", bg="yellow", fg="black")
    h.grid(row=4, column=2,pady=10)

    i = Entry(df, width=5, font="arial 30", bg="yellow", fg="black")
    i.grid(row=4, column=3,pady=10)

    result_label = Label(df, text="", bg="black", fg="white", font="mono 30 bold")
    result_label.grid(row=5, column=0, columnspan=6, pady=20)

    calculate_button = Button(df, text="Calculate", command=calculate_determinant, bg="maroon", fg="white", font="arial 30")
    calculate_button.grid(row=6, column=0, columnspan=6, pady=20)

    df.mainloop()

main = Tk()
main.geometry("1920x1080")
main.config(bg="black")
main.title("Determinant Founder")

Label(main, text="Determinant Founder", bg="black", fg="white", font="mono 50 bold underline").pack()
Button(main, text="2x2 Determinant", command=df2x2, bg="maroon", fg="white", font="arial 40").pack(pady=20)
Button(main, text="3x3 Determinant", command=df3x3, bg="maroon", fg="white", font="arial 40").pack(pady=20)

main.mainloop()
