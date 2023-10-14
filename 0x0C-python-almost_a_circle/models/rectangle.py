#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
	def __init__(self,height,width,x=0,y=0,id = None)
	self.width= width
	self.height = height
	self.x = x
	self.y = y
	super().__init__(id)
@proprety
def width(self):
	return self.width
@width.setter
	def width(self,value):
		if type(value) != int:
			raise("")
		elif value <= 0:
			raise("")
		else:
			self.__width = value 