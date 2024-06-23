from tkinter import *

def Matrix_2x2():
    df = Canvas(main, bg="black", highlightthickness=0)
    df.grid(row=1, column=0, pady=20, sticky="nsew")
    main.grid_rowconfigure(1, weight=1)

    canvas_frame = Frame(df, bg="black")
    canvas_frame.pack(fill="both", expand=True)

    df.create_window((0, 0), window=canvas_frame, anchor="nw")

    df_scrollbar = Scrollbar(main, orient="vertical", command=df.yview)
    df_scrollbar.grid(row=1, column=1, sticky='ns')

    df.configure(yscrollcommand=df_scrollbar.set)

    def calculate_inverse():
        try:
            ans = int((int(a.get()) * int(d.get())) - (int(b.get()) * int(c.get())))
            if ans != 0:
                if ans < 0:
                    ans = -ans
                    Label(result_frame, text=str(-int(d.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=0, column=0, padx=10)
                    Label(result_frame, text=str(int(b.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=0, column=1, padx=10)
                    Label(result_frame, text=str(int(c.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=1, column=0, padx=10)
                    Label(result_frame, text=str(-int(a.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=1, column=1, padx=10)
                else:
                    Label(result_frame, text=str(int(d.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=0, column=0, padx=10)
                    Label(result_frame, text=str(-int(b.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=0, column=1, padx=10)
                    Label(result_frame, text=str(-int(c.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=1, column=0, padx=10)
                    Label(result_frame, text=str(int(a.get())) + "/" + str(ans), width=7, font="arial 40", bg="yellow", fg="black").grid(row=1, column=1, padx=10)
        except:
            pass

    def calculate_determinant():
        try:
            ans = str((int(a.get()) * int(d.get())) - (int(b.get()) * int(c.get())))
            result_label.config(text="Determinant is " + ans)
        except ValueError:
            result_label.config(text="Invalid input")

    Label(canvas_frame, text="2x2 Matrix", font="arial 50 underline bold", bg="black", fg="white").grid(row=0, column=0, columnspan=2, pady=20)

    a = Entry(canvas_frame, width=7, font="arial 30", bg="yellow", fg="black")
    a.grid(row=2, column=0, padx=10, pady=10)

    b = Entry(canvas_frame, width=7, font="arial 30", bg="yellow", fg="black")
    b.grid(row=2, column=1, padx=10, pady=10)

    c = Entry(canvas_frame, width=7, font="arial 30", bg="yellow", fg="black")
    c.grid(row=3, column=0, padx=10, pady=10)

    d = Entry(canvas_frame, width=7, font="arial 30", bg="yellow", fg="black")
    d.grid(row=3, column=1, padx=10, pady=10)

    result_frame = Frame(canvas_frame, bg="black")
    result_frame.grid(row=6, column=0, columnspan=2, pady=20)
    result_label = Label(result_frame, text="", bg="black", fg="white", font="mono 30 bold")
    result_label.grid(row=4, column=0, columnspan=2, pady=20)

    Button(canvas_frame, text="Determinant", command=calculate_determinant, bg="maroon", fg="white", font="arial 30").grid(row=8, column=0, columnspan=2, pady=20)
    Button(canvas_frame, text="Inverse", command=calculate_inverse, bg="maroon", fg="white", font="arial 30").grid(row=9, column=0, columnspan=2, pady=20)

def Matrix_3x3():
    df = Canvas(main, bg="black", highlightthickness=0)
    df.grid(row=2, column=0, pady=20, sticky="nsew")
    main.grid_rowconfigure(2, weight=1)

    canvas_frame = Frame(df, bg="black")
    canvas_frame.pack(fill="both", expand=True)

    df.create_window((0, 0), window=canvas_frame, anchor="nw")

    df_scrollbar = Scrollbar(main, orient="vertical", command=df.yview)
    df_scrollbar.grid(row=2, column=1, sticky='ns')

    df.configure(yscrollcommand=df_scrollbar.set)

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
                    Label(result_frame, text=str(-(int(A))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=0, column=0, padx=10)
                    Label(result_frame, text=str(-(int(D))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=0, column=1, padx=10)
                    Label(result_frame, text=str(-(int(G))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=0, column=2, padx=10)
                    Label(result_frame, text=str(-(int(B))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=1, column=0, padx=10)
                    Label(result_frame, text=str(-(int(E))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=1, column=1, padx=10)
                    Label(result_frame, text=str(-(int(H))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=1, column=2, padx=10)
                    Label(result_frame, text=str(-(int(C))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=2, column=0, padx=10)
                    Label(result_frame, text=str(-(int(F))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=2, column=1, padx=10)
                    Label(result_frame, text=str(-(int(I))) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=2, column=2, padx=10)
                else:
                    Label(result_frame, text=str(int(A)) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=0, column=0, padx=10)
                    Label(result_frame, text=str(int(D)) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=0, column=1, padx=10)
                    Label(result_frame, text=str(int(G)) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=0, column=2, padx=10)
                    Label(result_frame, text=str(int(B)) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=1, column=0, padx=10)
                    Label(result_frame, text=str(int(E)) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=1, column=1, padx=10)
                    Label(result_frame, text=str(int(H)) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=1, column=2, padx=10)
                    Label(result_frame, text=str(int(C)) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=2, column=0, padx=10)
                    Label(result_frame, text=str(int(F)) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=2, column=1, padx=10)
                    Label(result_frame, text=str(int(I)) + "/" + str(ans), width=7, font="arial 30", bg="yellow", fg="black").grid(row=2, column=2, padx=10)
        except:
            pass

    def calculate_determinant():
        try:
            A = (int(e.get()) * int(i.get())) - (int(f.get()) * int(h.get()))
            B = (int(d.get()) * int(i.get())) - (int(f.get()) * int(g.get()))
            C = (int(d.get()) * int(h.get())) - (int(e.get()) * int(g.get()))
            ans = (int(a.get()) * A) - (int(b.get()) * B) + (int(c.get()) * C)
            result_label.config(text="Determinant is " + str(ans))
        except ValueError:
            result_label.config(text="Invalid input")

    Label(canvas_frame, text="3x3 Matrix", font="arial 50 underline bold", bg="black", fg="white").grid(row=0, column=0, columnspan=3, pady=20)

    a = Entry(canvas_frame, width=7, font="arial 30", bg="yellow", fg="black")
    a.grid(row=2, column=0, padx=10, pady=10)

    b = Entry(canvas_frame, width=7, font="arial 30", bg="yellow", fg="black")
    b.grid(row=2, column=1, padx=10, pady=10)

    c = Entry(canvas_frame, width=7, font="arial 30", bg="yellow", fg="black")
    c.grid(row=2, column=2, padx=10, pady=10)

    d = Entry(canvas_frame, width=7, font="arial 30", bg="yellow", fg="black")
    d.grid(row=3, column=0, padx=10, pady=10)

    e = Entry(canvas_frame, width=7, font="arial 30", bg="yellow", fg="black")
    e.grid(row=3, column=1, padx=10, pady=10)

    f = Entry(canvas_frame, width=7, font="arial 30", bg="yellow", fg="black")
    f.grid(row=3, column=2, padx=10, pady=10)

    g = Entry(canvas_frame, width=7, font="arial 30", bg="yellow", fg="black")
    g.grid(row=4, column=0, padx=10, pady=10)

    h = Entry(canvas_frame, width=7, font="arial 30", bg="yellow", fg="black")
    h.grid(row=4, column=1, padx=10, pady=10)

    i = Entry(canvas_frame, width=7, font="arial 30", bg="yellow", fg="black")
    i.grid(row=4, column=2, padx=10, pady=10)

    result_frame = Frame(canvas_frame, bg="black")
    result_frame.grid(row=6, column=0, columnspan=3, pady=20)
    result_label = Label(result_frame, text="", bg="black", fg="white", font="mono 30 bold")
    result_label.grid(row=4, column=0, columnspan=3, pady=20)

    Button(canvas_frame, text="Determinant", command=calculate_determinant, bg="maroon", fg="white", font="arial 30").grid(row=8, column=0, columnspan=3, pady=20)
    Button(canvas_frame, text="Inverse", command=calculate_inverse, bg="maroon", fg="white", font="arial 30").grid(row=9, column=0, columnspan=3, pady=20)

main = Tk()
main.attributes('-fullscreen', True)
main.config(bg="black")
main.title("Matrix Calculator")
main.grid_columnconfigure(0, weight=1)

Label(main, text="Matrix Calculator", bg="black", fg="white", font="mono 50 bold underline").grid(row=0, column=0, pady=20)
Button(main, text="2x2 Matrix", command=Matrix_2x2, bg="maroon", fg="white", font="arial 40").grid(row=1, column=0, pady=20)
Button(main, text="3x3 Matrix", command=Matrix_3x3, bg="maroon", fg="white", font="arial 40").grid(row=2, column=0, pady=20)

main.mainloop()
