from tkinter import *

def Matrix_2x2():
    df = Toplevel()
    df.title("2x2 Matrix")
    df.config(bg="black")
    df.attributes('-fullscreen', True)  # Set the window to full screen

    canvas = Canvas(df, bg="black")
    canvas.pack(side=TOP, fill=BOTH, expand=True)

    # Add a frame inside canvas for placing widgets
    frame = Frame(canvas, bg="black")
    canvas.create_window((0, 0), window=frame, anchor='nw')

    xscrollbar = Scrollbar(df, orient=HORIZONTAL, command=canvas.xview)
    xscrollbar.pack(side=BOTTOM, fill=X)
    canvas.configure(xscrollcommand=xscrollbar.set)

    yscrollbar = Scrollbar(df, orient=VERTICAL, command=canvas.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=yscrollbar.set)

    # Function to adjust scroll region when resizing
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    frame.bind('<Configure>', on_configure)

    def calculate_inverse():
        try:
            ans = int((int(a.get()) * int(d.get())) - (int(b.get()) * int(c.get())))
            if ans != 0:
                if ans < 0:
                    ans = -ans
                    Label(frame, text=str(-int(d.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=0, column=0, padx=10)
                    Label(frame, text=str(int(b.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=0, column=1, padx=10)
                    Label(frame, text=str(int(c.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=1, column=0, padx=10)
                    Label(frame, text=str(-int(a.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=1, column=1, padx=10)
                else:
                    Label(frame, text=str(int(d.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=0, column=0, padx=10)
                    Label(frame, text=str(-int(b.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=0, column=1, padx=10)
                    Label(frame, text=str(-int(c.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=1, column=0, padx=10)
                    Label(frame, text=str(int(a.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=1, column=1, padx=10)
        except Exception as e:
            print(e)

    def calculate_determinant():
        try:
            ans = str((int(a.get()) * int(d.get())) - (int(b.get()) * int(c.get())))
            result_label.config(text="Determinant is " + ans)
        except ValueError:
            result_label.config(text="Invalid input")

    Label(frame, text="2x2 Matrix", font="arial 50 underline bold", bg="black", fg="white").grid(row=0, column=0, columnspan=2, pady=20)

    a = Entry(frame, width=7, font="arial 30", bg="yellow", fg="black")
    a.grid(row=2, column=0, padx=10, pady=10)

    b = Entry(frame, width=7, font="arial 30", bg="yellow", fg="black")
    b.grid(row=2, column=1, padx=10, pady=10)

    c = Entry(frame, width=7, font="arial 30", bg="yellow", fg="black")
    c.grid(row=3, column=0, padx=10, pady=10)

    d = Entry(frame, width=7, font="arial 30", bg="yellow", fg="black")
    d.grid(row=3, column=1, padx=10, pady=10)

    result_label = Label(frame, text="", bg="black", fg="white", font="mono 30 bold")
    result_label.grid(row=4, column=0, columnspan=2, pady=20)

    Button(frame, text="Determinant", command=calculate_determinant, bg="maroon", fg="white", font="arial 30").grid(row=5, column=0, columnspan=2, pady=20)
    Button(frame, text="Inverse", command=calculate_inverse, bg="maroon", fg="white", font="arial 30").grid(row=6, column=0, columnspan=2, pady=20)

    df.mainloop()

def Matrix_3x3():
    df = Toplevel()
    df.title("3x3 Matrix")
    df.config(bg="black")
    df.attributes('-fullscreen', True)  # Set the window to full screen

    canvas = Canvas(df, bg="black")
    canvas.pack(side=TOP, fill=BOTH, expand=True)

    # Add a frame inside canvas for placing widgets
    frame = Frame(canvas, bg="black")
    canvas.create_window((0, 0), window=frame, anchor='nw')

    xscrollbar = Scrollbar(df, orient=HORIZONTAL, command=canvas.xview)
    xscrollbar.pack(side=BOTTOM, fill=X)
    canvas.configure(xscrollcommand=xscrollbar.set)

    yscrollbar = Scrollbar(df, orient=VERTICAL, command=canvas.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=yscrollbar.set)

    # Function to adjust scroll region when resizing
    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    frame.bind('<Configure>', on_configure)

    def calculate_inverse():
        try:
            co1 = (int(e.get()) * int(i.get())) - (int(f.get()) * int(h.get()))
            co3 = (int(d.get()) * int(h.get())) - (int(e.get()) * int(g.get()))
            co2 = (int(d.get()) * int(i.get())) - (int(f.get()) * int(g.get()))
            ans = int(int(a.get()) * co1 - int(b.get()) * co2 + int(c.get()) * co3)
            if ans != 0:
                A = (((int(e.get()) * int(i.get())) - (int(f.get()) * int(h.get()))))
                B = (((int(d.get()) * int(i.get())) - (int(f.get()) * int(g.get()))) * -1)
                C = (((int(d.get()) * int(h.get())) - (int(e.get()) * int(g.get()))))
                D = (((int(b.get()) * int(i.get())) - (int(h.get()) * int(c.get()))) * -1)
                E = (((int(a.get()) * int(i.get())) - (int(c.get()) * int(g.get()))))
                F = (((int(a.get()) * int(h.get())) - (int(b.get()) * int(g.get()))) * -1)
                G = (((int(b.get()) * int(f.get())) - (int(e.get()) * int(c.get()))))
                H = (((int(a.get()) * int(f.get())) - (int(d.get()) * int(c.get()))) * -1)
                I = (((int(a.get()) * int(e.get())) - (int(d.get()) * int(b.get()))))

                if ans < 0:
                    ans = -ans
                    Label(frame, text=str(-(int(A))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=0, column=0, padx=10)
                    Label(frame, text=str(-(int(D))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=0, column=1, padx=10)
                    Label(frame, text=str(-(int(G))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=0, column=2, padx=10)
                    Label(frame, text=str(-(int(B))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=1, column=0, padx=10)
                    Label(frame, text=str(-(int(E))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=1, column=1, padx=10)
                    Label(frame, text=str(-(int(H))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=1, column=2, padx=10)
                    Label(frame, text=str(-(int(C))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=2, column=0, padx=10)
                    Label(frame, text=str(-(int(F))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=2, column=1, padx=10)
                    Label(frame, text=str(-(int(I))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=2, column=2, padx=10)
                else:
                    Label(frame, text=str((int(A))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=0, column=0, padx=10)
                    Label(frame, text=str(-(int(D))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=0, column=1, padx=10)
                    Label(frame, text=str(-(int(G))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=0, column=2, padx=10)
                    Label(frame, text=str(-(int(B))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=1, column=0, padx=10)
                    Label(frame, text=str(-(int(E))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=1, column=1, padx=10)
                    Label(frame, text=str((int(H))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=1, column=2, padx=10)
                    Label(frame, text=str(-(int(C))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=2, column=0, padx=10)
                    Label(frame, text=str(-(int(F))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=2, column=1, padx=10)
                    Label(frame, text=str((int(I))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=2, column=2, padx=10)
        except Exception as e:
            print(e)

    def calculate_determinant():
        try:
            ans = str((int(a.get()) * (int(e.get()) * int(i.get()) - int(f.get()) * int(h.get()))) - (int(b.get()) * (int(d.get()) * int(i.get()) - int(f.get()) * int(g.get()))) + (int(c.get()) * (int(d.get()) * int(h.get()) - int(e.get()) * int(g.get()))))
            result_label.config(text="Determinant is " + ans)
        except ValueError:
            result_label.config(text="Invalid input")

    Label(frame, text="3x3 Matrix", font="arial 50 underline bold", bg="black", fg="white").grid(row=0, column=0, columnspan=7, pady=20)

    a = Entry(frame, width=7, font="arial 30", bg="yellow", fg="black")
    a.grid(row=2, column=1, padx=10, pady=10)

    b = Entry(frame, width=7, font="arial 30", bg="yellow", fg="black")
    b.grid(row=2, column=2, padx=10, pady=10)

    c = Entry(frame, width=7, font="arial 30", bg="yellow", fg="black")
    c.grid(row=2, column=3, padx=10, pady=10)

    d = Entry(frame, width=7, font="arial 30", bg="yellow", fg="black")
    d.grid(row=3, column=1, padx=10, pady=10)

    e = Entry(frame, width=7, font="arial 30", bg="yellow", fg="black")
    e.grid(row=3, column=2, padx=10, pady=10)

    f = Entry(frame, width=7, font="arial 30", bg="yellow", fg="black")
    f.grid(row=3, column=3, padx=10, pady=10)

    g = Entry(frame, width=7, font="arial 30", bg="yellow", fg="black")
    g.grid(row=4, column=1, padx=10, pady=10)

    h = Entry(frame, width=7, font="arial 30", bg="yellow", fg="black")
    h.grid(row=4, column=2, padx=10, pady=10)

    i = Entry(frame, width=7, font="arial 30", bg="yellow", fg="black")
    i.grid(row=4, column=3, padx=10, pady=10)

    result_label = Label(frame, text="", bg="black", fg="white", font="mono 30 bold")
    result_label.grid(row=5, column=1, columnspan=3, pady=20)

    Button(frame, text="Determinant", command=calculate_determinant, bg="maroon", fg="white", font="arial 30").grid(row=6, column=1, columnspan=3, pady=20)
    Button(frame, text="Inverse", command=calculate_inverse, bg="maroon", fg="white", font="arial 30").grid(row=7, column=1, columnspan=3, pady=20)

    df.mainloop()

# Main window
root = Tk()
root.title("Matrix")

# Buttons for 2x2 and 3x3 matrices
Button(root, text="2x2 Matrix", command=Matrix_2x2, font="arial 30", bg="yellow", fg="black").pack(pady=20)
Button(root, text="3x3 Matrix", command=Matrix_3x3, font="arial 30", bg="yellow", fg="black").pack(pady=20)

root.mainloop()
