from tkinter import *
from tkinter import filedialog as fd,END,messagebox
import tkinter.scrolledtext as st
import os
from random import *
import smtplib

mygui=Tk()
textarea=st.ScrolledText(mygui,width=100,height=80)
mygui.title("ThinkPad++")
a=StringVar()
a.set('--'*50+"\nMessage Section\n"+'--'*50)
label1=Label(mygui,textvariable=a).pack(pady=2)
##variable
find=StringVar()
replace=StringVar()
email=StringVar()
##
##functions
def newfile():
    ##if textarea has some content and you want to open new file
    if len(textarea.get('1.0',END+'-1c'))>0:
        if messagebox.askyesno("save?","Do you want to save this file?"):
            save()
            textarea.delete('1.0',END)
        else:
            textarea.delete('1.0',END)
            a.set('--'*50+"\n"+"Opened new file"+"\n"+'--'*50)
def open():
    newfile()
    ##I wrote the above thing to fix the issue of
    ##if I opened one file and trying to open another file,
    ##there data are getting appended
    file=fd.askopenfile(parent=mygui,mode='rb',title="Choose file",filetypes={("Text","*.txt")})
    name=file.name
    name=name.split("/")[-1]
    a.set('--'*50+"\nOpened file -->"+name+"\n"+'--'*50)
    if file!=None:
        data=file.read()
        textarea.insert('1.0',data)
    file.close()
def save():
    file=fd.asksaveasfile(mode="w")
    if file!=None:
        data=textarea.get('1.0',END+'-1c')
        file.write(data)
    file.close()
    a.set('--'*50+"\nfind: "+file.name+" Saved Sucessfully"+"\n"+'--'*50)
def frd(temp1,temp2,fr):
    data=textarea.get('1.0',END+'-1c')
    data=data.replace(temp1,temp2)
    textarea.delete('1.0',END)
    textarea.insert('1.0',data)
    a.set('--'*50+"\nfind: "+temp1+"-->"+"replace: "+temp2+"\n"+'--'*50)
    fr.destroy()

def findreplace():
    fr=Toplevel(mygui)
    label1=Label(fr,text="Find").pack()
    text1=Entry(fr,textvariable=find,width=25).pack()
    label2=Label(fr,text="replace").pack()
    text2=Entry(fr,textvariable=replace,width=25).pack()
    b1=Button(fr,text="find and replace",command=lambda:frd(find.get(),replace.get(),fr))
    b1.pack()
    fr.mainloop()
def exitfile():
    if messagebox.showinfo("Quit","Are you sure want to quit?"):
        mygui.destroy()
def requestotp(temp):
    mail()
def init():
##create a folder in c drive which will hold the account information
    try:
        if not os.path.exists('C:\\ThinkPad'):
            os.makedirs('C:\\ThinkPad')
    except:
        print("")
    if os.path.exists('C:\\ThinkPad\\Account'):
        myfile=open('C:\\ThinkPad\\Account',"r+")
    else:
        myfile=open('C:\\ThinkPad\\Account',"w")
    myfile.write(email+"\n"+otp)
    myfile.close()
'''def mail():
    def send_mail(recv,data):
    sender="helloabhilash2000@gmail.com"
    receiver=recv
    password=pw
    message=data
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender,password)
    server.sendmail(sender,receiver,message) 
def requestotp(temp1,temp2):
    mail
def Account():
    acc=Toplevel(mygui)
    label1=Label(acc,text="Enter Mail").pack()
    text1=Entry(acc,textvariable=email,width=30).pack()
    val=randint(1000,9999)
    with open("C:\\ThinkPad\\Account","r") as file:
        data=file.readlines()
    file.close()
    data[0]=email.get()
    data[1]=otp.get()
    with open("C:\\ThinkPad\\Account","w") as file:
        file.writelines(data)
    file.close()
    message="Thanks for choosing ThinkPad"+val
    b1=Button(acc,text="REQUEST OTP",width=30,command=lambda:requestotp(email.get())).pack()
    label2=Label(acc,text="Enter Otp").pack()
    text2=Entry(acc,textvariable=otp,width=30).pack()
    b2=Button(acc,text="VERIFY OTP",width=30).pack()
'''
##menu things dude
mymenu=Menu(mygui)
mygui.config(menu=mymenu)
file=Menu(mymenu)
edit=Menu(mymenu)
mail=Menu(mymenu)
##creating main menu
mymenu.add_cascade(label="File",menu=file)
mymenu.add_cascade(label="Edit",menu=edit)
mymenu.add_cascade(label="Mail",menu=mail)
##creating submenu inside File
file.add_command(label="New",command=newfile)
file.add_command(label="Open",command=open)
file.add_command(label="Save",command=save)
##To put line above exit
file.add_separator() 
file.add_command(label="Exit",command=exitfile)
##creating submenu of edit
edit.add_command(label="find and replace",command=findreplace)
'''
##working with mail
mail.add_command(label="Account",command=Account)
mail.add_command(label="Send mail")
'''
textarea.pack()
mygui.mainloop()
