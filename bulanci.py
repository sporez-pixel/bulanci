from tkinter import *
from random import randint

class hra:
	def __init__(self):
		self.okno = Tk()
		self.platno = Canvas(self.okno, width=600, height=600)
		self.platno.pack()
		self.vytvorbludiste()
		self.klavesy=[]
		self.okno.bind("<KeyPress>",self.stisk)
		self.okno.bind("<KeyRelease>",self.pustit)
		self.s1=strelec(self,"pistolnik1.png",1,1,["Right","Left","Up",
		"Down","Return"],[1,0],15,15)
		self.s2=strelec(self,"pistolnik3.png",18,18,["d","a","w","s",
		"f"],[-1,0],585,585)
	def stisk(self,event):
		klavesa=event.keysym
		self.klavesy.append(klavesa)
	def pustit(self,event):
		klavesa=event.keysym
		while (klavesa in self.klavesy):
			self.klavesy.remove(klavesa)
		
	
	def vytvorbludiste(self):
		self.labyrint = []
		self.labyrint.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
		self.labyrint.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
		self.labyrint.append([1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
		self.labyrint.append([1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1])
		self.labyrint.append([1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1])
		self.labyrint.append([1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1])
		self.labyrint.append([1,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1])
		self.labyrint.append([1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1])
		self.labyrint.append([1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,1,1,1])
		self.labyrint.append([1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1])
		self.labyrint.append([1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1])
		self.labyrint.append([1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1])
		self.labyrint.append([1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1])
		self.labyrint.append([1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1])
		self.labyrint.append([1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1])
		self.labyrint.append([1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1])
		self.labyrint.append([1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1])
		self.labyrint.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
		self.labyrint.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
		self.labyrint.append([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
		for i in range(20):
			for j in range(20):
				if (self.labyrint[i][j]==1):
					self.platno.create_rectangle(j*30,i*30,j*30+30,
					i*30+30,fill="black")
				else:
					self.platno.create_rectangle(j*30,i*30,j*30+30,
					i*30+30,fill="white")
	
class strelec:
	def __init__(self,h,obrazek,x,y,ovladani,orientace,x1,y1):
		self.h=h
		self.zivoty = 3
		self.soubor = PhotoImage(file=obrazek)
		self.orientace = orientace
		self.nabito = 0
		self.x = x
		self.y = y
		self.x1 = x1
		self.y1 = y1
		self.ovladani = ovladani
		self.obrazek = self.h.platno.create_image(self.x*30+15,
		self.y*30+15,image=self.soubor)
		self.zivotyNapis = self.h.platno.create_text(x1,y1,
		text=self.zivoty,font=["Arial",15],fill="white")
		self.pozor()
	def pozor(self):
		if (self.ovladani[0] in self.h.klavesy):
			self.pohyb([1,0])
		if (self.ovladani[1] in self.h.klavesy):
			self.pohyb([-1,0])
		if (self.ovladani[2] in self.h.klavesy):
			self.pohyb([0,-1])
		if (self.ovladani[3] in self.h.klavesy):
			self.pohyb([0,1])
		if (self.ovladani[4] in self.h.klavesy):
			self.vystrel()
		self.nabito+=1
		self.h.okno.after(50,self.pozor)
	def pohyb(self,smer):
		if (smer!=self.orientace):
			self.orientace=smer
		else:
			self.x+=smer[0]
			self.y+=smer[1]
			if(self.jeTamZed()):
				self.x-=smer[0]
				self.y-=smer[1]
				smer=[0,0]
			self.h.platno.move(self.obrazek,smer[0]*30,smer[1]*30)
	def jeTamZed(self):
		if(self.h.labyrint[self.y][self.x]==1):
			return True
		return False
	def vystrel(self):
		if (self.nabito>40):
			self.nabito = 0
			s = strela(self.h,self.x,self.y,self.orientace)
	def zasah(self):
		self.zivoty -= 1
		if (self.zivoty == 0):
			self.h.platno.create_text(300,300,text="GAME OVER",font=
			["Arial",50],fill="black")
			self.h.okno.after(2000,self.h.okno.quit)
		self.h.platno.delete(self.zivotyNapis)
		self.zivotyNapis = self.h.platno.create_text(self.x1,self.y1,
		text=self.zivoty,font=["Arial",15],fill="white")
		
class strela:
	def __init__(self,h,x,y,orientace):
		self.h = h
		self.x = x
		self.y = y
		self.orientace = orientace
		self.obrazek = self.h.platno.create_oval(self.x*30+12,self.y*30+
		12,self.x*30+18,self.y*30+18,fill="red")
		self.pohyb()
	def pohyb(self):
		self.x+=self.orientace[0]
		self.y+=self.orientace[1]
		if (self.x==self.h.s1.x) and (self.y==self.h.s1.y):
			self.h.s1.zasah()
		if (self.x==self.h.s2.x) and (self.y==self.h.s2.y):
			self.h.s2.zasah() 
		if (self.h.labyrint[self.y][self.x]==1):
			self.h.platno.delete(self.obrazek)
		else:
			self.h.platno.move(self.obrazek,self.orientace[0]*30,
			self.orientace[1]*30)
			self.h.platno.after(20,self.pohyb)
										
		
h = hra()
mainloop() 
