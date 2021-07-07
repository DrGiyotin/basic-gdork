import webbrowser
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import sys,os

con = sqlite3.connect("onlysearchdata.db")
cursor = con.cursor()
def closewindow():
    exityesno = messagebox.askyesno(message="Do you want to exit?",title="DetailedSearch")
    if exityesno == 1:
        window.destroy()



if __name__ == "__main__":
    window = tk.Tk()
    window.iconbitmap("LogoMakr-4dIS9Y.ico")
    window.title("DetailedSearch")
    window.geometry("600x600")
    window.resizable(False, False)
    window.config(bg="white")
    window.protocol("WM_DELETE_WINDOW", closewindow)


def Enterent(event):
    Start()
def button1(event):
    if cachevar.get() == 1:
        ent.delete(0,tk.END)
    elif authorvar.get() == 1:
        ent.delete(0, tk.END)
    elif sitevar.get() == 1:
        ent.delete(0, tk.END)
    elif mapvar.get() == 1:
        ent.delete(0, tk.END)
    elif infovar.get() == 1:
        ent.delete(0, tk.END)
    elif stocksvar.get() == 1:
        ent.delete(0, tk.END)
    elif movievar.get() == 1:
        ent.delete(0,tk.END)
    elif weathervar.get() == 1:
        ent.delete(0,tk.END)
    elif relatedvar.get() == 1:
        ent.delete(0,tk.END)
    elif bookvar.get() == 1:
        ent.delete(0,tk.END)
def leave(event):
    if  ent.get().strip() == "":
        if cachevar.get() == 1:
            ent.delete(0, "end")
            ent.insert(0, "youtube.com")
            window.focus()
        elif authorvar.get() == 1:
            ent.delete(0, "end")
            ent.insert(0, "Nazım Hikmet")
            window.focus()
        elif sitevar.get() == 1:
            ent.delete(0, "end")
            ent.insert(0, "github.com")
            window.focus()
        elif mapvar.get() == 1:
            ent.delete(0, "end")
            ent.insert(0, "Istanbul")
            window.focus()
        elif infovar.get() == 1:
            ent.delete(0, "end")
            ent.insert(0, "www.wikipedia.org")
            window.focus()
        elif stocksvar.get() == 1:
            ent.delete(0, "end")
            ent.insert(0, "Tesla")
            window.focus()
        elif movievar.get() == 1:
            ent.delete(0, "end")
            ent.insert(0, "Pulp Fiction")
            window.focus()
        elif weathervar.get() == 1:
            ent.delete(0, "end")
            ent.insert(0, "Roma")
            window.focus()
        elif relatedvar.get() == 1:
            ent.delete(0, "end")
            ent.insert(0, "stackoverflow.com")
            window.focus()
        elif bookvar.get() == 1:
            ent.delete(0, "end")
            ent.insert(0, "Crime and Punishment")
            window.focus()

def Start():
    if ent.get().strip() != "":
       cursor.execute("INSERT INTO searchdata (sdata)  VALUES(?)", (ent.get(),))
       if intçek.get() == 1:
           url = "https://www.google.com/search?q=" + saveent  + " " +  "%2B" + ent.get()
           webbrowser.open(url)
           asdasd()
       elif int2çek.get() == 1:
           url = "https://www.google.com/search?q=" + saveent + " " + "-" + ent.get()
           webbrowser.open(url)
       elif cachevar.get() == 1:
           url = "https://www.google.com/search?q=" + "cache:" + ent.get()
           webbrowser.open(url)
       elif stocksvar.get() == 1:
            url = "https://www.google.com/search?q=" + "stocks:" + ent.get()
            webbrowser.open(url)
       elif authorvar.get() == 1:
           url = "https://www.google.com/search?q=" + f'author:"{ent.get()}"'
           webbrowser.open(url)
       elif sitevar.get() == 1:
           url = "https://www.google.com/search?q=" + "site:" + ent.get()
           webbrowser.open(url)
       elif mapvar.get() == 1:
           url = "https://www.google.com/search?q=" + "maps:" + ent.get()
           webbrowser.open(url)
       elif infovar.get() == 1:
           url = "https://www.google.com/search?q=" + "info:" + ent.get()
           webbrowser.open(url)
       elif movievar.get() == 1:
           url = "https://www.google.com/search?q=" + "movie:" + ent.get()
           webbrowser.open(url)
       elif weathervar.get() == 1:
           url = "https://www.google.com/search?q=" + "weather:" + ent.get()
           webbrowser.open(url)
       elif relatedvar.get() == 1:
           url = "https://www.google.com/search?q=" + "related:" + ent.get()
           webbrowser.open(url)
       elif bookvar.get() == 1:
           url = "https://www.google.com/search?q=" + "book:" + ent.get()
           webbrowser.open(url)
       else:
           url = "https://www.google.com/search?q=" + ent.get()
           webbrowser.open(url)
    else:
        messagebox.showinfo(message="Write something for me to search")
greenent = ""
redent = ""
saveent = ""
def check1():
    global saveent,greenent,redent
    if ent["bg"] == "green":
        greenent = ent.get() + greenent
        ent.delete(0, tk.END)
    if intçek.get() == 1:
        check2.config(state=tk.DISABLED)
        if  ent.get().strip() != "":
            newslink.config(fg="red",cursor="arrow")
            mapslink.config(fg="red",cursor="arrow")
            ımageslink.config(fg="red",cursor="arrow")
            shoppinglink.config(fg="red",cursor="arrow")
            stocks.config(state=tk.DISABLED)
            info.config(state=tk.DISABLED)
            mapc.config(state=tk.DISABLED)
            site.config(state=tk.DISABLED)
            cache.config(state=tk.DISABLED)
            author.config(state=tk.DISABLED)
            saveent = saveent + ent.get()
            ent.delete(0,tk.END)
            ent.config(bg="green")
            ent.insert(0,greenent)
            greenent = ""
        elif ent.get().strip() == "":
            check2.config(state=tk.NORMAL)
            messagebox.showinfo(message="Keyword required!")
            check.deselect()

    else:
        newslink.config(fg="blue",cursor="hand2")
        mapslink.config(fg="blue",cursor="hand2")
        ımageslink.config(fg="blue",cursor="hand2")
        shoppinglink.config(fg="blue",cursor="hand2")
        stocks.config(state=tk.NORMAL)
        info.config(state=tk.NORMAL)
        mapc.config(state=tk.NORMAL)
        site.config(state=tk.NORMAL)
        cache.config(state=tk.NORMAL)
        author.config(state=tk.NORMAL)
        check2.config(state=tk.NORMAL)
        ent.insert(0,saveent)
        saveent = ""
        ent.config(bg="white")





def check2():
    global saveent, redent,greenent
    if ent["bg"] == "red":
        redent = ent.get() + redent
        ent.delete(0, tk.END)
    if int2çek.get() == 1:
        check.config(state=tk.DISABLED)
        if ent.get().strip() != "":
            newslink.config(fg="red",cursor="arrow")
            mapslink.config(fg="red",cursor="arrow")
            ımageslink.config(fg="red",cursor="arrow")
            shoppinglink.config(fg="red",cursor="arrow")
            stocks.config(state=tk.DISABLED)
            info.config(state=tk.DISABLED)
            mapc.config(state=tk.DISABLED)
            site.config(state=tk.DISABLED)
            cache.config(state=tk.DISABLED)
            author.config(state=tk.DISABLED)
            saveent = saveent + ent.get()
            ent.delete(0, tk.END)
            ent.config(bg="red")
            ent.insert(0, redent)
            redent = ""
        elif ent.get().strip() == "":
            check.config(state=tk.NORMAL)
            messagebox.showinfo(message="Keyword required!")
            check2.deselect()
    else:
        newslink.config(fg="blue",cursor="hand2")
        mapslink.config(fg="blue",cursor="hand2")
        ımageslink.config(fg="blue",cursor="hand2")
        shoppinglink.config(fg="blue",cursor="hand2")
        stocks.config(state=tk.NORMAL)
        info.config(state=tk.NORMAL)
        mapc.config(state=tk.NORMAL)
        site.config(state=tk.NORMAL)
        cache.config(state=tk.NORMAL)
        author.config(state=tk.NORMAL)
        check.config(state=tk.NORMAL)
        ent.insert(0, saveent)
        saveent = ""
        ent.config(bg="white")


ent = tk.Entry(window,width=50,bd=5)
ent.focus()
ent.bind("<Return>",Enterent)
ent.bind("<Button-1>",button1)
ent.bind("<Leave>",leave)
ent.place(x=150,y=300)
button1 = tk.Button(window,text="Start",command=Start,cursor="hand2")
button1.place(x=285,y=365)
img = ImageTk.PhotoImage(Image.open("LogoMakr-4dIS9Y.png"))
imglabel = tk.Label(window, image=img,bg="white").place(x=205,y=10)
number = 0
listforurl = []
def Combine():
    def combandsea():
          listforurl.clear()
          if masterword.get().strip() != "":
              masterwordinurl = " " + masterword.get() + " "
              listforurl.append(masterwordinurl)
          if intitle.get().strip() != "":
              intitleinurl = " intitle:" + intitle.get() + " "
              listforurl.append(intitleinurl)
          if filetype.get().strip() != "":
              filetypeinurl = " filetype:" + filetype.get() + " "
              listforurl.append(filetypeinurl)
          if intext.get().strip() != "":
              intextinurl  = " intext:" + intext.get() + " "
              listforurl.append(intextinurl)
          if combinesite.get().strip() != "":
              siteinurl = " site:" + combinesite.get() + " "
              listforurl.append(siteinurl)
          if inurl.get().strip() != "":
              inurlinurl = " inurl:" + inurl.get() +  " "
              listforurl.append(inurlinurl)
          if Combinewith.get().strip() != "":
              withinurl = " %2B" + Combinewith.get() + " "
              listforurl.append(withinurl)
          if Combinewitho.get().strip() != "":
              withoutinurl = " -" + Combinewitho.get() + " "
              listforurl.append(withoutinurl)
          if listforurl == []:
              messagebox.showinfo(message="Write something for me to search")
              swindow.focus()
          elif len(listforurl) == 1 and Combinewith.get().strip() != "":
               messagebox.showinfo(message="Need to be combined")
               swindow.focus()
          elif len(listforurl) == 1 and Combinewitho.get().strip() != "":
               messagebox.showinfo(message="Need to be combined")
               swindow.focus()
          elif len(listforurl) == 2 and Combinewith.get().strip() != "":
              if Combinewitho.get().strip() != "":
                  messagebox.showinfo(message="Keyword required")
                  swindow.focus()
          elif len(listforurl) == 1 and filetype.get().strip() != "":
               messagebox.showinfo(message="Filetype cannot be used alone")
               swindow.focus()
          else:
              url = "https://www.google.com/search?q=" + "".join(listforurl)
              webbrowser.open(url)
    def swindowenter(event):
        combandsea()

    def destroy_top(*args):
        global number
        number = 0
        swindow.destroy()
    global  number
    if number == 0:
        number = 1
        global swindow
        swindow = tk.Toplevel()
        swindow.geometry("250x440+200+90")
        swindow.iconbitmap("LogoMakr-4dIS9Y.ico")
        swindow.resizable(False, False)
        swindow.bind("<Destroy>", destroy_top)
        swindow.bind("<Return>",swindowenter)
        masterword = tk.Label(swindow, text="Keyword:", font="Helvatica  10")
        masterword.place(x=10, y=10)
        intitle = tk.Label(swindow, text="Intitle:", font="Helvatica  10")
        intitle.place(x=10, y=60)
        filetype = tk.Label(swindow, text="Filetype:", font="Helvatica  10")
        filetype.place(x=10, y=110)
        intext = tk.Label(swindow, text="Intext:", font="Helvatica  10")
        intext.place(x=10, y=160)
        combinesite = tk.Label(swindow, text="Site:", font="Helvatica  10")
        combinesite.place(x=10, y=210)
        inurl = tk.Label(swindow, text="Inurl:", font="Helvatica  10")
        inurl.place(x=10, y=260)
        Combinewith = tk.Label(swindow, text="With:", font="Helvatica  10")
        Combinewith.place(x=10, y=310)
        Combinewitho = tk.Label(swindow, text="Without:", font="Helvatica  10")
        Combinewitho.place(x=10, y=360)
        masterword = tk.Entry(swindow, font="Helvatica  10")
        masterword.place(x=80, y=10)
        intitle = tk.Entry(swindow, font="Helvatica  10")
        intitle.place(x=80, y=60)
        filetype = tk.Entry(swindow, font="Helvatica  10")
        filetype.place(x=80, y=110)
        intext = tk.Entry(swindow,  font="Helvatica  10")
        intext.place(x=80, y=160)
        combinesite = tk.Entry(swindow,font="Helvatica  10")
        combinesite.place(x=80, y=210)
        inurl = tk.Entry(swindow, font="Helvatica  10")
        inurl.place(x=80, y=260)
        Combinewith = tk.Entry(swindow,font="Helvatica  10")
        Combinewith.place(x=80, y=310)
        Combinewitho = tk.Entry(swindow, font="Helvatica  10")
        Combinewitho.place(x=80, y=360)
        combineandsearch = tk.Button(swindow, command=combandsea, text="Combine and search")
        combineandsearch.place(x=10, y=410)
        masterword.focus()

number2 = 0
def History():
    global number3
    global con
    global cursor
    global historylist
    global  historywindow
    def historylistleftdoubleclick(event):
        ent.delete(0,tk.END)
        ent.insert(0,historylist.get(tk.ACTIVE))
    def historylistdoubleclick(event):
        elementdata = "".join(historylist.get(tk.ACTIVE))
        historylist.delete(tk.ANCHOR)
        cursor.execute("DELETE FROM searchdata WHERE sdata = ?",(elementdata,))
    def destroy_top(*args):
        global number2
        number2 = 0
        historywindow.destroy()
    global number2
    if number2 == 0:
        number2 = 1
        global historywindow
        historywindow = tk.Toplevel()
        historywindow.geometry("250x440+635+90")
        historywindow.iconbitmap("LogoMakr-4dIS9Y.ico")
        historywindow.resizable(True,False)
        historywindow.bind("<Destroy>", destroy_top)
        scroll = tk.Scrollbar(historywindow)
        scroll.pack(side = tk.RIGHT, fill = tk.BOTH)
        historylist = tk.Listbox(historywindow, width=250, height=440,font="Helvatica 12")
        historylist.bind("<Button-2>",historylistdoubleclick)
        historylist.bind("<Double-1>", historylistleftdoubleclick)
        historylist.focus()
        historylist.select_set(tk.END)
        historylist.config(yscrollcommand=scroll.set)
        scroll.config(command=historylist.yview)
        historylist.pack(side = tk.LEFT, fill = tk.BOTH)
        sqllitedb()

def sqllitedb():
    global  historywindow
    global historylist
    cursor.execute("CREATE TABLE IF NOT EXISTS searchdata(id INTEGER PRIMARY KEY AUTOINCREMENT,sdata TEXT)")
    con.commit()
    cursor.execute("SELECT *  FROM searchdata ORDER BY sdata DESC LIMIT 20")
    for datas in cursor.fetchall()[::-1]:
        historylist.insert(0, datas[1])
        con.commit()

button2 = tk.Button(window, text="COMBINE", command=Combine,fg="dark goldenrod",
bg="white",
font="Helvatica 12",
relief="flat",
activebackground="white",compound=tk.CENTER,bd=0,cursor="hand2")
button2.place(x=485, y=550)
button3 = tk.Button(window, text="HISTORY", command=History,fg="dark goldenrod",
bg="white",
font="Helvatica 12",
relief="flat",
activebackground="white",compound=tk.CENTER,bd=0,cursor="hand2")
button3.place(x=20, y=550)


intçek = tk.IntVar()
int2çek = tk.IntVar()
check = tk.Checkbutton(window,command=check1 ,onvalue = 1, offvalue = 0 ,variable = intçek,text="With",fg="green")
check.place(x=200,y=365)

check2 = tk.Checkbutton(window,command=check2 ,onvalue = 1, offvalue = 0 ,variable = int2çek,text="Without",fg="red")
check2.place(x=350,y=365)
def bookcheck():
    if bookvar.get() == 1:
        window.focus()
        ent["bg"] = "#943126"
        ent.delete(0, tk.END)
        newslink.config(fg="red", cursor="arrow")
        mapslink.config(fg="red", cursor="arrow")
        ımageslink.config(fg="red", cursor="arrow")
        shoppinglink.config(fg="red", cursor="arrow")
        stocks["state"] = tk.DISABLED
        movie["state"] = tk.DISABLED
        related["state"] = tk.DISABLED
        weather["state"] = tk.DISABLED
        cache["state"] = tk.DISABLED
        info["state"] = tk.DISABLED
        mapc["state"] = tk.DISABLED
        site["state"] = tk.DISABLED
        author["state"] = tk.DISABLED
        check["state"] = tk.DISABLED
        check2["state"] = tk.DISABLED
        ent.insert(0, "Crime and Punishment")

    else:
        ent.focus()
        ent["bg"] = "white"
        newslink.config(fg="blue", cursor="hand2")
        mapslink.config(fg="blue", cursor="hand2")
        ımageslink.config(fg="blue", cursor="hand2")
        shoppinglink.config(fg="blue", cursor="hand2")
        stocks["state"] = tk.NORMAL
        movie["state"] = tk.NORMAL
        weather["state"] = tk.NORMAL
        related["state"] = tk.NORMAL
        cache["state"] = tk.NORMAL
        info["state"] = tk.NORMAL
        mapc["state"] = tk.NORMAL
        site["state"] = tk.NORMAL
        check["state"] = tk.NORMAL
        check2["state"] = tk.NORMAL
        author["state"] = tk.NORMAL
        ent.delete(0, tk.END)
def relatedcheck():
    if relatedvar.get() == 1:
        window.focus()
        ent["bg"] = "#784212"
        ent.delete(0, tk.END)
        newslink.config(fg="red", cursor="arrow")
        mapslink.config(fg="red", cursor="arrow")
        ımageslink.config(fg="red", cursor="arrow")
        shoppinglink.config(fg="red", cursor="arrow")
        stocks["state"] = tk.DISABLED
        movie["state"] = tk.DISABLED
        weather["state"] = tk.DISABLED
        book["state"] = tk.DISABLED
        cache["state"] = tk.DISABLED
        info["state"] = tk.DISABLED
        mapc["state"] = tk.DISABLED
        site["state"] = tk.DISABLED
        author["state"] = tk.DISABLED
        check["state"] = tk.DISABLED
        check2["state"] = tk.DISABLED
        ent.insert(0, "stackoverflow.com")

    else:
        ent.focus()
        ent["bg"] = "white"
        newslink.config(fg="blue", cursor="hand2")
        mapslink.config(fg="blue", cursor="hand2")
        ımageslink.config(fg="blue", cursor="hand2")
        shoppinglink.config(fg="blue", cursor="hand2")
        stocks["state"] = tk.NORMAL
        movie["state"] = tk.NORMAL
        weather["state"] = tk.NORMAL
        book["state"] = tk.NORMAL
        cache["state"] = tk.NORMAL
        info["state"] = tk.NORMAL
        mapc["state"] = tk.NORMAL
        site["state"] = tk.NORMAL
        check["state"] = tk.NORMAL
        check2["state"] = tk.NORMAL
        author["state"] = tk.NORMAL
        ent.delete(0, tk.END)
def weathercheck():
    if weathervar.get() == 1:
        window.focus()
        ent["bg"] = "#DC7633"
        ent.delete(0, tk.END)
        newslink.config(fg="red", cursor="arrow")
        mapslink.config(fg="red", cursor="arrow")
        ımageslink.config(fg="red", cursor="arrow")
        shoppinglink.config(fg="red", cursor="arrow")
        stocks["state"] = tk.DISABLED
        movie["state"] = tk.DISABLED
        related["state"] = tk.DISABLED
        book["state"] = tk.DISABLED
        cache["state"] = tk.DISABLED
        info["state"] = tk.DISABLED
        mapc["state"] = tk.DISABLED
        site["state"] = tk.DISABLED
        author["state"] = tk.DISABLED
        check["state"] = tk.DISABLED
        check2["state"] = tk.DISABLED
        ent.insert(0, "Roma")

    else:
        ent.focus()
        ent["bg"] = "white"
        newslink.config(fg="blue", cursor="hand2")
        mapslink.config(fg="blue", cursor="hand2")
        ımageslink.config(fg="blue", cursor="hand2")
        shoppinglink.config(fg="blue", cursor="hand2")
        stocks["state"] = tk.NORMAL
        movie["state"] = tk.NORMAL
        related["state"] = tk.NORMAL
        book["state"] = tk.NORMAL
        cache["state"] = tk.NORMAL
        info["state"] = tk.NORMAL
        mapc["state"] = tk.NORMAL
        site["state"] = tk.NORMAL
        check["state"] = tk.NORMAL
        check2["state"] = tk.NORMAL
        author["state"] = tk.NORMAL
        ent.delete(0, tk.END)
def moviecheck():
    if movievar.get() == 1:
        ent.focus()
        ent["bg"] = "#F1948A"
        ent.delete(0, tk.END)
        newslink.config(fg="red", cursor="arrow")
        mapslink.config(fg="red", cursor="arrow")
        ımageslink.config(fg="red", cursor="arrow")
        shoppinglink.config(fg="red", cursor="arrow")
        stocks["state"]  = tk.DISABLED
        weather["state"]  = tk.DISABLED
        related["state"] = tk.DISABLED
        book["state"]   = tk.DISABLED
        cache["state"] = tk.DISABLED
        info["state"] = tk.DISABLED
        mapc["state"] = tk.DISABLED
        site["state"] = tk.DISABLED
        author["state"] = tk.DISABLED
        check["state"] = tk.DISABLED
        check2["state"] = tk.DISABLED
        ent.insert(0, "Pulp Fiction")

    else:
        ent.focus()
        ent["bg"] = "white"
        newslink.config(fg="blue", cursor="hand2")
        mapslink.config(fg="blue", cursor="hand2")
        ımageslink.config(fg="blue", cursor="hand2")
        shoppinglink.config(fg="blue", cursor="hand2")
        stocks["state"] = tk.NORMAL
        weather["state"] = tk.NORMAL
        related["state"] = tk.NORMAL
        book["state"] = tk.NORMAL
        cache["state"] = tk.NORMAL
        info["state"] = tk.NORMAL
        mapc["state"] = tk.NORMAL
        site["state"] = tk.NORMAL
        check["state"] = tk.NORMAL
        check2["state"] = tk.NORMAL
        author["state"] = tk.NORMAL
        ent.delete(0, tk.END)
def stockscheck():
    if stocksvar.get() == 1:
        window.focus()
        ent["bg"] = "#F0B27A"
        ent.delete(0,tk.END)
        newslink.config(fg="red",cursor="arrow")
        mapslink.config(fg="red",cursor="arrow")
        ımageslink.config(fg="red",cursor="arrow")
        shoppinglink.config(fg="red",cursor="arrow")
        related["state"] = tk.DISABLED
        movie["state"] = tk.DISABLED
        weather["state"] = tk.DISABLED
        book["state"] = tk.DISABLED
        cache["state"] = tk.DISABLED
        info["state"] = tk.DISABLED
        mapc["state"] = tk.DISABLED
        site["state"] = tk.DISABLED
        author["state"] = tk.DISABLED
        check["state"] = tk.DISABLED
        check2["state"] = tk.DISABLED
        ent.insert(0,"Tesla")

    else:
        ent.focus()
        ent["bg"]  = "white"
        newslink.config(fg="blue",cursor="hand2")
        mapslink.config(fg="blue",cursor="hand2")
        ımageslink.config(fg="blue",cursor="hand2")
        shoppinglink.config(fg="blue",cursor="hand2")
        related["state"] = tk.NORMAL
        movie["state"] = tk.NORMAL
        weather["state"] = tk.NORMAL
        book["state"] = tk.NORMAL
        cache["state"] = tk.NORMAL
        info["state"] = tk.NORMAL
        mapc["state"] = tk.NORMAL
        site["state"] = tk.NORMAL
        check["state"] = tk.NORMAL
        check2["state"] = tk.NORMAL
        author["state"] = tk.NORMAL
        ent.delete(0,tk.END)

def cachecheck():
    if cachevar.get() == 1:
        window.focus()
        ent["bg"] = "#26A68D"
        ent.delete(0,tk.END)
        newslink.config(fg="red",cursor="arrow")
        mapslink.config(fg="red",cursor="arrow")
        ımageslink.config(fg="red",cursor="arrow")
        shoppinglink.config(fg="red",cursor="arrow")
        related["state"] = tk.DISABLED
        movie["state"] = tk.DISABLED
        weather["state"] = tk.DISABLED
        book["state"] = tk.DISABLED
        stocks["state"] = tk.DISABLED
        info["state"] = tk.DISABLED
        mapc["state"] = tk.DISABLED
        site["state"] = tk.DISABLED
        author["state"] = tk.DISABLED
        check["state"] = tk.DISABLED
        check2["state"] = tk.DISABLED
        ent.insert(0,"youtube.com")

    else:
        ent.focus()
        ent["bg"]  = "white"
        newslink.config(fg="blue",cursor="hand2")
        mapslink.config(fg="blue",cursor="hand2")
        ımageslink.config(fg="blue",cursor="hand2")
        shoppinglink.config(fg="blue",cursor="hand2")
        related["state"] = tk.NORMAL
        movie["state"] = tk.NORMAL
        weather["state"] = tk.NORMAL
        book["state"] = tk.NORMAL
        stocks["state"] = tk.NORMAL
        info["state"] = tk.NORMAL
        mapc["state"] = tk.NORMAL
        site["state"] = tk.NORMAL
        check["state"] = tk.NORMAL
        check2["state"] = tk.NORMAL
        author["state"] = tk.NORMAL
        ent.delete(0,tk.END)
def authorcheck():
    if authorvar.get() == 1:
        window.focus()
        ent["bg"] = "#DC8428"
        ent.delete(0, tk.END)
        newslink.config(fg="red",cursor="arrow")
        mapslink.config(fg="red",cursor="arrow")
        ımageslink.config(fg="red",cursor="arrow")
        shoppinglink.config(fg="red",cursor="arrow")
        related["state"] = tk.DISABLED
        movie["state"] = tk.DISABLED
        weather["state"] = tk.DISABLED
        book["state"] = tk.DISABLED
        stocks["state"] = tk.DISABLED
        info["state"] = tk.DISABLED
        mapc["state"] = tk.DISABLED
        site["state"] = tk.DISABLED
        check["state"] = tk.DISABLED
        check2["state"] = tk.DISABLED
        cache["state"]  = tk.DISABLED
        ent.insert(0, "Nazım Hikmet")
    else:
        ent.focus()
        ent["bg"]  = "white"
        newslink.config(fg="blue",cursor="hand2")
        mapslink.config(fg="blue",cursor="hand2")
        ımageslink.config(fg="blue",cursor="hand2")
        shoppinglink.config(fg="blue",cursor="hand2")
        related["state"] = tk.NORMAL
        movie["state"] = tk.NORMAL
        weather["state"] = tk.NORMAL
        book["state"] = tk.NORMAL
        stocks["state"] = tk.NORMAL
        info["state"] = tk.NORMAL
        mapc["state"] = tk.NORMAL
        site["state"] = tk.NORMAL
        check["state"] = tk.NORMAL
        check2["state"] = tk.NORMAL
        cache["state"] = tk.NORMAL
        ent.delete(0,tk.END)
def sitecheck():
    if sitevar.get() == 1:
        window.focus()
        ent["bg"] = "#BE3FBA"
        ent.delete(0, tk.END)
        newslink.config(fg="red",cursor="arrow")
        mapslink.config(fg="red",cursor="arrow")
        ımageslink.config(fg="red",cursor="arrow")
        shoppinglink.config(fg="red",cursor="arrow")
        related["state"] = tk.DISABLED
        movie["state"] = tk.DISABLED
        weather["state"] = tk.DISABLED
        book["state"] = tk.DISABLED
        stocks["state"] = tk.DISABLED
        info["state"] = tk.DISABLED
        mapc["state"] = tk.DISABLED
        author["state"] = tk.DISABLED
        check["state"] = tk.DISABLED
        check2["state"] = tk.DISABLED
        cache["state"] = tk.DISABLED
        ent.insert(0, "github.com")
    else:
        ent.focus()
        ent["bg"] = "white"
        newslink.config(fg="blue",cursor="hand2")
        mapslink.config(fg="blue",cursor="hand2")
        ımageslink.config(fg="blue",cursor="hand2")
        shoppinglink.config(fg="blue",cursor="hand2")
        related["state"] = tk.NORMAL
        movie["state"] = tk.NORMAL
        weather["state"] = tk.NORMAL
        book["state"] = tk.NORMAL
        stocks["state"] = tk.NORMAL
        info["state"] = tk.NORMAL
        mapc["state"] = tk.NORMAL
        author["state"] = tk.NORMAL
        check["state"] = tk.NORMAL
        check2["state"] = tk.NORMAL
        cache["state"] = tk.NORMAL
        ent.delete(0, tk.END)

def mapcheck():
    if mapvar.get() == 1:
        window.focus()
        ent["bg"] = "#D5CF25"
        ent.delete(0, tk.END)
        newslink.config(fg="red",cursor="arrow")
        mapslink.config(fg="red",cursor="arrow")
        ımageslink.config(fg="red",cursor="arrow")
        shoppinglink.config(fg="red",cursor="arrow")
        related["state"] = tk.DISABLED
        movie["state"] = tk.DISABLED
        weather["state"] = tk.DISABLED
        book["state"] = tk.DISABLED
        stocks["state"] = tk.DISABLED
        info["state"] = tk.DISABLED
        site["state"] = tk.DISABLED
        author["state"] = tk.DISABLED
        check["state"] = tk.DISABLED
        check2["state"] = tk.DISABLED
        cache["state"] = tk.DISABLED
        ent.insert(0, "Istanbul")
    else:
        ent.focus()
        ent["bg"] = "white"
        newslink.config(fg="blue",cursor="hand2")
        mapslink.config(fg="blue",cursor="hand2")
        ımageslink.config(fg="blue",cursor="hand2")
        shoppinglink.config(fg="blue",cursor="hand2")
        related["state"] = tk.NORMAL
        movie["state"] = tk.NORMAL
        weather["state"] = tk.NORMAL
        book["state"] = tk.NORMAL
        stocks["state"] = tk.NORMAL
        info["state"] = tk.NORMAL
        site["state"] = tk.NORMAL
        author["state"] = tk.NORMAL
        check["state"] = tk.NORMAL
        check2["state"] = tk.NORMAL
        cache["state"] = tk.NORMAL
        ent.delete(0, tk.END)
def infocheck():
    if infovar.get() == 1:
        window.focus()
        ent["bg"] = "#1A9CBA"
        ent.delete(0, tk.END)
        newslink.config(fg="red",cursor="arrow")
        mapslink.config(fg="red",cursor="arrow")
        ımageslink.config(fg="red",cursor="arrow")
        shoppinglink.config(fg="red",cursor="arrow")
        related["state"] = tk.DISABLED
        movie["state"] = tk.DISABLED
        weather["state"] = tk.DISABLED
        book["state"] = tk.DISABLED
        stocks["state"] = tk.DISABLED
        mapc["state"] = tk.DISABLED
        site["state"] = tk.DISABLED
        author["state"] = tk.DISABLED
        check["state"] = tk.DISABLED
        check2["state"] = tk.DISABLED
        cache["state"] = tk.DISABLED
        ent.insert(0, "www.wikipedia.org")
    else:
        ent.focus()
        ent["bg"] = "white"
        newslink.config(fg="blue",cursor="hand2")
        mapslink.config(fg="blue",cursor="hand2")
        ımageslink.config(fg="blue",cursor="hand2")
        shoppinglink.config(fg="blue",cursor="hand2")
        related["state"] = tk.NORMAL
        movie["state"] = tk.NORMAL
        weather["state"] = tk.NORMAL
        book["state"] = tk.NORMAL
        stocks["state"] = tk.NORMAL
        mapc["state"] = tk.NORMAL
        site["state"] = tk.NORMAL
        author["state"] = tk.NORMAL
        check["state"] = tk.NORMAL
        check2["state"] = tk.NORMAL
        cache["state"] = tk.NORMAL
        ent.delete(0, tk.END)

mapvar = tk.IntVar()
sitevar = tk.IntVar()
cachevar = tk.IntVar()
authorvar = tk.IntVar()
infovar = tk.IntVar()
stocksvar = tk.IntVar()
movievar = tk.IntVar()
weathervar = tk.IntVar()
relatedvar = tk.IntVar()
bookvar = tk.IntVar()
stocks = tk.Checkbutton(window,command=stockscheck ,onvalue = 1, offvalue = 0 ,variable = stocksvar,text="Stocks",fg="#F0B27A")
stocks.place(x=20,y=265)
movie = tk.Checkbutton(window,command=moviecheck ,onvalue = 1, offvalue = 0 ,variable = movievar,text="Movie",fg="#F1948A")
movie.place(x=20,y=300)
weather = tk.Checkbutton(window,command=weathercheck ,onvalue = 1, offvalue = 0 ,variable = weathervar,text="Weather",fg="#DC7633")
weather.place(x=20,y=335)
related = tk.Checkbutton(window,command=relatedcheck ,onvalue = 1, offvalue = 0 ,variable = relatedvar,text="Related",fg="#784212")
related.place(x=20,y=370)
book = tk.Checkbutton(window,command=bookcheck ,onvalue = 1, offvalue = 0 ,variable = bookvar,text="Book",fg="#943126")
book.place(x=20,y=405)
info = tk.Checkbutton(window,command=infocheck ,onvalue = 1, offvalue = 0 ,variable = infovar,text="Info",fg="#1A9CBA")
info.place(x=530,y=265)
cache = tk.Checkbutton(window,command=cachecheck ,onvalue = 1, offvalue = 0 ,variable = cachevar,text="Cache",fg="#26A68D")
cache.place(x=530,y=300)
author = tk.Checkbutton(window,command=authorcheck,onvalue = 1, offvalue = 0 ,variable = authorvar,text="Author",fg="#DC8428")
author.place(x=530,y=335)
site = tk.Checkbutton(window,command=sitecheck,onvalue = 1, offvalue = 0 ,variable = sitevar,text="Site",fg="#BE3FBA")
site.place(x=530,y=370)
mapc = tk.Checkbutton(window,command=mapcheck,onvalue = 1, offvalue = 0 ,variable = mapvar,text="Map",fg="#D5CF25")
mapc.place(x=530,y=405)

def newsbind(event):
    if ent.get().strip() != "" and newslink["fg"] == "blue":
        url = f"https://www.google.com/search?q={ent.get()}&tbm=nws"
        webbrowser.open(url)
def mapsbind(event):
    if ent.get().strip() != "" and mapslink["fg"] == "blue":
        url = f"https://www.google.com/maps/place/{ent.get()}/"
        webbrowser.open(url)
def ımagesbind(event):
    if ent.get().strip() != "" and ımageslink["fg"] == "blue":
        url = f"https://www.google.com/search?q={ent.get()}&tbm=isch"
        webbrowser.open(url)
def shoppingbind(event):
    if ent.get().strip() != "" and shoppinglink["fg"] == "blue":
        url = f"https://www.google.com/search?q={ent.get()}&tbm=shop"
        webbrowser.open(url)

newslink = tk.Label(window,text="News",bg="white",fg="blue",cursor="hand2")
newslink.place(x=190,y=270)
mapslink = tk.Label(window,text="Maps",bg="white",fg="blue",cursor="hand2")
mapslink.place(x=250,y=270)
ımageslink = tk.Label(window,text="Images",bg="white",fg="blue",cursor="hand2")
ımageslink.place(x=310,y=270)
shoppinglink = tk.Label(window,text="Shopping",bg="white",fg="blue",cursor="hand2")
shoppinglink.place(x=370,y=270)
newslink.bind("<Button-1>",newsbind)
mapslink.bind("<Button-1>",mapsbind)
ımageslink.bind("<Button-1>",ımagesbind)
shoppinglink.bind("<Button-1>",shoppingbind)


window.mainloop()
