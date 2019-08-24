import Tkinter,sys
from Tkinter import *
import tkFileDialog
import os
from splifile import FileSplitter, FileSplitterException, mainp
from encryptdir import encrypt_file, decrypt_file, renamefiles, main



def proceed():
		n=Tkinter.Tk()
		def server():
			#global n
			pth=n.directory
			keyw=pwd.get()
			def splitter0():
				os.chdir(pth)
				n1=numc.get()
				n2=int(n1)
				a=0
				dirs=os.listdir(pth)
				for fn in dirs:
					print(fn)
					mainp(fn,n2,a)
			def encrypter0():
				a=0
				main(keyw,pth,a)
			if __name__=="__main__" :
				splitter0()
				encrypter0()
		
		def client():
			#global n
			pth=n.directory
			keyw=pwd.get()
			def splitter1():
				os.chdir(pth)
				n1=numc.get()
				n2=int(n1)
				a=1
				dirs=os.listdir(pth)
				for fn in dirs:
					print(fn)
					mainp(fn,n2,a)
			def encrypter1():
				a=1
				main(keyw,pth,a)
			if __name__=="__main__" :
				encrypter1()
				splitter1()
	
		titl=Label(n, text='			ParCrypt		').grid(row=0)
		l9=Label(n, text='').grid(row=1)
		l8=Label(n, text='Key : ').grid(row=2,column=0)
		pwd=Entry(n)
		pwd.grid(row=2, column=1)
		n.directory=tkFileDialog.askdirectory()
		b1=Button(n, text ="Encrypt", command=server)
		b1.grid(row=5,column=0)
		b2=Button(n, text ="Decrypt", command = client)
		b2.grid(row=5,column=1)
		l6=Label(n, text='Chunks : ').grid(row=3, column=0)
		numc=Entry(n)
		numc.grid(row=3,column=1)
		l7=Label(n, text='').grid(row=4)



def diffiehellman():
	global m
	p=23
	G=18
	a1=puk.get()
	b1=prk.get()
	a=int(a1)
	b=int(b1)
	A=(a**b)%p
	if(A==G):
		x=Label(m, text="Authenticated").grid(row=6)
		proceed()
	else:
		x=Label(m, text="Authentication Failed").grid(row=6)
		m.quit()

m=Tkinter.Tk()
t=Label(m, text='			ParCrypt		').grid(row=0)
l=Label(m, text='').grid(row=1)
h1=Label(m, text='Public Key : ').grid(row=2)
h2=Label(m, text='Private Key : ').grid(row=3)
puk=Entry(m)
puk.grid(row=2, column=1)
prk=Entry(m)
prk.grid(row=3, column=1)
B=Button(m, text ="Verify", command = diffiehellman)
B.grid(row=5)
m.mainloop()




	









