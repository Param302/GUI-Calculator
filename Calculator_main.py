from tkinter import *
import math
import tkinter.messagebox as Msg

# Making the window
root = Tk()
# Assigning variables to colors
BG = "DarkGoldenrod2"
FG = "grey15"
ABG = "goldenrod1"
AFG = "grey15"
light_theme = True
dark_theme = False

# Setting the calculator size
root.geometry("680x460")
# Disabling the resizable option
root.resizable(0, 0)
# Setting the Title
root.title("Calculator -By Parampreet Singh")
# Setting the Icon
root.iconbitmap(bitmap="cal_icon_2.ico")
root.configure(bg="goldenrod1")
#---------------------F-U-N-C-T-I-O-N-S--F-O-R--M-E-N-U-B-A-R--------------------#

# Tools
def dark():
    global BG, FG, ABG, AFG, light_theme, dark_theme
    BG = "grey15"
    FG  = "DarkGoldenrod2"
    ABG = "grey20"
    AFG = "DarkGoldenrod2"
    light_theme = False
    dark_theme = True

    widgets = [Tools, Mode, More, B7, B8, B9, B4, B5, B6, B1, B2, B3, B0, Bd0, BDot, Bless, BAC]
    operators = [BPlus, BSub, BMul, BDiv, Equal, extra, Bfloor, Bcube, Bper, Bpow, Bpie, Bsqr, Bleft, Bright]
    for i in widgets:
        i.configure(bg=BG, fg=FG, activebackground=FG, activeforeground=BG)

    for j in operators:
        j.configure(bg=FG, fg=BG, activebackground=BG, activeforeground=FG)

    root.configure(bg=ABG)
    E.configure(bg=BG, fg=FG, selectbackground=ABG, selectforeground=AFG, insertbackground=FG, insertwidth=5)

    NF.config(bg=ABG)

    Sign.config(bg=ABG)

    Sign2.config(bg=ABG)

    root.update()

def light():

    global BG, FG, ABG, AFG, light_theme, dark_theme

    BG = "DarkGoldenrod2"
    FG = "grey15"
    ABG = "goldenrod1"
    AFG = "grey20"
    light_theme = True
    dark_theme = False

    widgets = [Tools, Mode, More, B7, B8, B9, B4, B5, B6, B1, B2, B3, B0, Bd0, BDot, Bless, BAC]
    operators = [BPlus, BSub, BMul, BDiv, Equal, extra, Bfloor, Bcube, Bper, Bpie, Bsqr, Bpow, Bleft, Bright]
    for i in widgets:
        i.configure(bg=BG, fg=FG, activebackground=AFG, activeforeground=ABG)

    for j in operators:
        j.configure(bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG)

    root.configure(bg=ABG)
    E.configure(bg=BG, fg=FG, selectbackground=ABG, selectforeground=AFG, insertbackground=FG, insertwidth=5)

    NF.config(bg=ABG)

    Sign.config(bg=ABG)

    Sign2.config(bg=ABG)

    root.update()

# More
def Help():

    h = Msg.showinfo("Calculator - Help", """This is a Calculator made by Parampreet Singh.
It has some unique features like Dark Mode, Light Mode.
Some Extra Operators: \n[ x\u00B2 ] - square\n[ x\u00B3 ] - cube\n[ ^ ] - power\n[ % ] - modulo operator\n[ // ] - floor division\n[ \u03C0 ] - pie""")

def about():

    ab = Msg.showinfo("Calculator - About", "This Calculator is Made by Parampreet Singh")

def feedback():

    fb = Msg.askyesno("Calculator - Feedback", "Do you like this Calculator?")
    if (fb):
        Msg.showinfo("Calculator - Feedback", "It's happy to see that you like this Calculator!")
    elif (fb==False):
        Msg.showinfo("Calculator - Feedback", "We are very sorry if you don't like it.\nWe will try to improve it!")



# Extra Button function
def extras():
    global light_theme, dark_theme, extra, root, Sign2, FG, BG, AFG, ABG
    if (extra["text"]==">"):
        root.geometry("910x440")
        root.minsize(width=910, height=440)
        root.maxsize(width=910, height=440)
        extra.configure(text="<", bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG)
        extra.place_configure(x=860, y=86)
        Sign2.place_configure(x=630, y=80)
    
    elif (extra["text"]=="<"):
        root.geometry("680x440")
        root.minsize(width=680, height=440)
        root.maxsize(width=680, height=440)
        extra.configure(text=">", bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG)
        extra.place_configure(x=630, y=86)
        Sign2.place_configure(x=700, y=80)
    
    if (light_theme):
        light()
    elif (dark_theme):
        dark()


# Calculate class
class Calculate:
    global E, Evalue
    expression = ""
    display = ""
    inside = ""
    total = ""
    # display = inside and then display will set
    symbols = {"add" : "+", "mul" : "x", "div" : "/", "minus" : "-","floor" : "//", "per" : "%",
    "pow" : "^", "pie" : u"\u03C0", "sqr" : u"\u00B2", "cube" : u"\u00B3", "bleft" : "(", "bright" : ")"}

    symbol_use = {"add" : "+", "mul" : "*", "div" : "/", "minus" : "-","floor" : "//", "per" : "%",
    "pow" : "**", "pie" : f"*{math.pi}", "sqr" : "**2", "cube" : "**3", "bleft" : "(", "bright" : ")"}

    def Update(self, d=display):

        if (d==""):
            Evalue.set("")
        else:
            Evalue.set(Evalue.get()+d)

        E.update()
        
    # Function for number
    def number(self, n):

        self.expression+=n
        self.display+=n
        self.inside+=n
        self.Update(n)

    # Function for operators and other symbols
    def symbol(self, sname):

        self.expression+=sname
        self.display+=self.symbols[sname]
        self.inside+=self.symbol_use[sname]
        self.Update(self.symbols[sname])

    # Function for evaluating total
    def equal(self):

        if (Evalue.get()!=""):
            try:
                if (Evalue.get()==u"\u03C0"):
                    self.total = 1*math.pi
                    self.total = str(self.total)
                    self.display = self.total
                    Evalue.set(self.display)

                elif ((Evalue.get()==u"\u00B2") or (Evalue.get()==u"\u00B3")):
                    self.total = 1
                    self.total = str(self.total)
                    self.display = self.total
                    Evalue.set(self.display)

                else:
                    self.total = eval(self.inside)
                    self.total = str(self.total)
                    self.display = self.total
                    Evalue.set(self.display)

                # setting self.inside in brackets so that it calculate perfectly
                self.inside = f"({self.total})" 
            
            except SyntaxError:
                self.total = ""
                self.inside = ""
                self.expression = ""
                Evalue.set("")

        else:
            self.total = ""
            self.inside = ""
            self.expression = ""
            Evalue.set("")

        E.update()

    # Function for AC
    def all_clear(self):
        if (Evalue.get()!=""):
            self.expression = ""
            self.display = ""
            self.inside = ""
            self.total = ""
            self.Update(self.display)
        else:
            self.expression = ""
            self.display = ""
            self.inside = ""
            self.total = ""
            self.Update(d=self.display)

    # Function for lessing the entry
    def less(self):
        if (len(self.display)<=1):
            self.expression = ""
            self.display = ""
            self.inside = ""
            self.total = ""
        elif (len(self.display)>1):
            self.display = self.display[:-1]
            self.expression = self.display
            self.inside = self.display
            self.total = self.display
        Evalue.set(self.display)
        E.update()

Cal = Calculate()

#-----------------M-E-N-U--B-A-R----------------#
MainMenu = Menu(root)
#-----T-O-O-L-S-----#
Tools = Menu(MainMenu, tearoff=0, bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG)
Tools.add_command(label="Clear", command=lambda : Cal.all_clear())
Tools.add_separator()
# Mode
Mode = Menu(Tools, tearoff=0, relief="sunken", bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG)
Mode.add_radiobutton(label="Light Mode", command=light)
Mode.add_radiobutton(label="Dark Mode", command=dark)
Tools.add_cascade(label="Mode", menu=Mode)
Tools.add_separator()
Tools.add_command(label="Close", command=quit)
MainMenu.add_cascade(label="Tools", menu=Tools)

#-----M-O-R-E-----#
More = Menu(MainMenu, tearoff=0, bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG)
More.add_command(label="Help", command=Help)

More.add_command(label="About", command=about)
More.add_separator()
More.add_command(label="Feedback", command=feedback)
MainMenu.add_cascade(label="More", menu=More)
root.config(menu=MainMenu)

#-------------------E-N-T-R-Y---W-I-D-G-E-T-------------------#
Evalue = StringVar()
Evalue.set("")
E = Entry(root, text=Evalue, font=("consolas", 30, "bold"), bg=BG, fg=FG, selectbackground=ABG, selectforeground=AFG, justify="right", insertbackground=FG, insertwidth=5)
E.pack(padx=10, pady=10, ipadx=20, ipady=5, fill=X)
E.bind("<<enter>>", Cal.equal())

#-------------------F-R-A-M-E---&---B-U-T-T-O-N-S-------------------#
# Frame for buttons
NF = Frame(root, bg="goldenrod1")
# Button 7
B7 = Button(NF, text="7", font=("Arial", 30), bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.number("7"))
B7.grid(row=0, column=0, ipadx=30, padx=5, pady=5)

# Button 8
B8 = Button(NF, text="8", font=("Arial", 30), bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.number("8"))
B8.grid(row=0, column=1, ipadx=30, padx=5, pady=5)

# Button 9
B9 = Button(NF, text="9", font=("Arial", 30), bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.number("9"))
B9.grid(row=0, column=2, ipadx=30, padx=5, pady=5)

# Button 4
B4 = Button(NF, text="4", font=("Arial", 30), bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.number("4"))
B4.grid(row=1, column=0, ipadx=30, padx=5, pady=5)

# Button 5
B5 = Button(NF, text="5", font=("Arial", 30), bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.number("5"))
B5.grid(row=1, column=1, ipadx=30, padx=5, pady=5)

# Button 6
B6 = Button(NF, text="6", font=("Arial", 30), bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.number("6"))
B6.grid(row=1, column=2, ipadx=30, padx=5, pady=5)

# Button 1
B1 = Button(NF, text="1", font=("Arial", 30), bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.number("1"))
B1.grid(row=2, column=0, ipadx=30, padx=5, pady=5)

# Button 2
B2 = Button(NF, text="2", font=("Arial", 30), bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.number("2"))
B2.grid(row=2, column=1, ipadx=30, padx=5, pady=5)

# Button 3
B3 = Button(NF, text="3", font=("Arial", 30), bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.number("3"))
B3.grid(row=2, column=2, ipadx=30, padx=5, pady=5)

# Button 0
B0 = Button(NF, text="0", font=("Arial", 30), bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.number("0"))
B0.grid(row=3, column=0, ipadx=30, padx=5, pady=5)

# Button 00
Bd0 = Button(NF, text="00", font=("Arial", 30), bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.number("00"))
Bd0.grid(row=3, column=1, ipadx=20, padx=5, pady=5)

# Button .
BDot = Button(NF, text=".", font=("Arial", 30), bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.number("."))
BDot.grid(row=3, column=2, ipadx=34, padx=5, pady=5)

NF.pack(side="left", anchor="n", padx=5)

#---------------------O-P-E-R-A-T-I-O-N-S---------------------#
Sign = Frame(root, bg="goldenrod1")
# Button CE
Bless = Button(Sign, text="<-", font=("consolas", 28), bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.less())
Bless.grid(row=0, column=0, ipadx=15, padx=10, pady=5, ipady=2)

# Button AC
BAC = Button(Sign, text="AC", font=("consolas", 28), bg=BG, fg=FG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.all_clear())
BAC.grid(row=0, column=1, ipadx=15, pady=5, ipady=2)

# Button Plus +
BPlus = Button(Sign, text="+", font=("Times New Roman", 28, "bold"), bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.symbol("add"))
BPlus.grid(row=1, column=0, ipadx=25, padx=5, pady=5)

# Button Multiply
BMul = Button(Sign, text="x", font=("consolas", 28), bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.symbol("mul"))
BMul.grid(row=1, column=1, ipadx=26, pady=5)

# Button Subtract -
BSub = Button(Sign, text="-", font=("Times New Roman", 26, "bold"), bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.symbol("minus"))
BSub.grid(row=2, column=0, ipadx=30, padx=5, ipady=4, pady=5)

# Button Divide
BDiv = Button(Sign, text="/", font=("Times New Roman", 26, "bold"), bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.symbol("div"))
BDiv.grid(row=2, column=1, ipadx=30, padx=10, ipady=4, pady=5)

Sign.place(x=390, y=80)

#---------------------E-Q-U-A-L---S-I-G-N---------------------#
# Equal sign
Equal = Button(root, text="=", font=("Times New Roman", 30, "bold"), bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG, width=8, padx=10, cursor="hand2", command=Cal.equal)
Equal.place(x=398, y=351, border="outside")
Equal.bind("<<Enter>>", Cal.equal())

#----------------M-O-R-E---O-P-E-R-A-T-I-O-N-S----------------#
# Extra button
extra = Button(root, text=">", font=("Times New Roman", 20, "bold"), bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG, height=10, pady=6, command=extras)
extra.place(x=630, y=86)

# Frame for extra buttons
Sign2 = Frame(root, bg="goldenrod1")
# Button power
Bfloor = Button(Sign2, text="//", font=("Arial", 24), bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.symbol("floor"))
Bfloor.grid(row=0, column=0, ipadx=30, ipady=8, padx=5, pady=5)

# Button percentage
Bper = Button(Sign2, text="%", font=("Arial", 24), bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.symbol("per"))
Bper.grid(row=0, column=1, ipadx=22, ipady=7, padx=5, pady=5)

# Button power
Bpow = Button(Sign2, text="^", font=("Arial", 24), bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.symbol("pow"))
Bpow.grid(row=1, column=0, ipadx=28, ipady=5, padx=5, pady=5)

# Button pie
Bpie = Button(Sign2, text=u"\u03C0", font=("Arial", 24), bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.symbol("pie"))
Bpie.grid(row=1, column=1, ipadx=28, ipady=5, padx=5, pady=5)

# Button square
Bsqr = Button(Sign2, text=u"x\u00B2", font=("consolas", 24), bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.symbol("sqr"))
Bsqr.grid(row=2, column=0, ipadx=20, ipady=5,  padx=5, pady=5)

# Button cube
Bcube = Button(Sign2, text=u"x\u00B3", font=("consolas", 24), bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.symbol("cube"))
Bcube.grid(row=2, column=1, ipadx=20, ipady=5,  padx=5, pady=5)

# Button left bracket
Bleft = Button(Sign2, text="(", font=("Arial", 26), bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.symbol("bleft"))
Bleft.grid(row=3, column=0, ipadx=28, ipady=4, padx=5, pady=10)

# Button right bracket
Bright = Button(Sign2, text=")", font=("Arial", 26), bg=FG, fg=BG, activebackground=ABG, activeforeground=AFG, cursor="hand2", command=lambda : Cal.symbol("bright"))
Bright.grid(row=3, column=1, ipadx=28, ipady=4, padx=5, pady=10)

Sign2.place(x=700, y=90)

root.mainloop()
#---------------------P-A-R-A-M-P-R-E-E-T---S-I-N-G-H---------------------#
