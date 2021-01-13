# -*- coding: utf-8 -*-
import pygame
import random
import time

class Cubo:
	def __init__(self):
		self.__Front = [[Utility.Color(0)]*3,[Utility.Color(0)]*3,[Utility.Color(0)]*3]
		self.__Back = [[Utility.Color(1)]*3,[Utility.Color(1)]*3,[Utility.Color(1)]*3]
		self.__Left = [[Utility.Color(2)]*3,[Utility.Color(2)]*3,[Utility.Color(2)]*3]
		self.__Right = [[Utility.Color(3)]*3,[Utility.Color(3)]*3,[Utility.Color(3)]*3]
		self.__Top = [[Utility.Color(4)]*3,[Utility.Color(4)]*3,[Utility.Color(4)]*3]
		self.__Down = [[Utility.Color(5)]*3,[Utility.Color(5)]*3,[Utility.Color(5)]*3]
		self.__Moves = []
		self.__count = 0
		self.isSolved = False
		self.draw()

	def move(self,b):
		if b == "FR":#Front to right

				temp = self.__Front[0][0]
				self.__Front[0][0] = self.__Front[2][0]
				self.__Front[2][0] = self.__Front[2][2]
				self.__Front[2][2] = self.__Front[0][2]
				self.__Front[0][2] = temp
				
				temp = self.__Front[0][1]
				self.__Front[0][1] = self.__Front[1][0]
				self.__Front[1][0] = self.__Front[2][1]
				self.__Front[2][1] = self.__Front[1][2]
				self.__Front[1][2] = temp
	
				temp = self.__Top[2][0]
				temp1 = self.__Top[2][1]
				temp2 = self.__Top[2][2]
				self.__Top[2][0] = self.__Left[2][2]
				self.__Top[2][1] = self.__Left[1][2]
				self.__Top[2][2] = self.__Left[0][2]
				self.__Left[0][2] = self.__Down[2][0]
				self.__Left[1][2] = self.__Down[2][1]
				self.__Left[2][2] = self.__Down[2][2]
				self.__Down[2][0] = self.__Right[2][0]
				self.__Down[2][1] = self.__Right[1][0]
				self.__Down[2][2] = self.__Right[0][0]
				self.__Right[0][0] = temp
				self.__Right[1][0] = temp1
				self.__Right[2][0] = temp2

				self.__Moves.append("FR")

				if self.__count < 10:
					self.__count += 1

		if b == "FL":#Front to left

			temp = self.__Front[0][0]
			self.__Front[0][0] = self.__Front[0][2]
			self.__Front[0][2] = self.__Front[2][2]
			self.__Front[2][2] = self.__Front[2][0]
			self.__Front[2][0] = temp
			temp = self.__Front[0][1]
			self.__Front[0][1] = self.__Front[1][2]
			self.__Front[1][2] = self.__Front[2][1]
			self.__Front[2][1] = self.__Front[1][0]
			self.__Front[1][0] = temp
			
			Fake = [[None]*3]*3
			
			Fake[2][0] = self.__Top[2][0]
			Fake[2][1] = self.__Top[2][1]
			Fake[2][2] = self.__Top[2][2]
			self.__Top[2][0] = self.__Right[0][0]
			self.__Top[2][1] = self.__Right[1][0]
			self.__Top[2][2] = self.__Right[2][0]
			self.__Right[0][0] = self.__Down[2][2]
			self.__Right[1][0] = self.__Down[2][1]
			self.__Right[2][0] = self.__Down[2][0]
			self.__Down[2][0] = self.__Left[0][2]
			self.__Down[2][1] = self.__Left[1][2]
			self.__Down[2][2] = self.__Left[2][2]
			self.__Left[0][2] = Fake[2][2]
			self.__Left[1][2] = Fake[2][1]
			self.__Left[2][2] = Fake[2][0]

			self.__Moves.append("FL") 

			if self.__count < 10:
				self.__count += 1

		if b == "TL":#Top to left
			temp = self.__Top[0][0]
			self.__Top[0][0] = self.__Top[2][0]
			self.__Top[2][0] = self.__Top[2][2]
			self.__Top[2][2] = self.__Top[0][2]
			self.__Top[0][2] = temp
			temp = self.__Top[0][1]
			self.__Top[0][1] = self.__Top[1][0]
			self.__Top[1][0] = self.__Top[2][1]
			self.__Top[2][1] = self.__Top[1][2]
			self.__Top[1][2] = temp

			temp = self.__Front[0]
			self.__Front[0] = self.__Right[0]
			self.__Right[0] = self.__Back[0]
			self.__Back[0] = self.__Left[0]
			self.__Left[0] = temp

			self.__Moves.append("TL")

			if self.__count < 10:
				self.__count += 1

		if b == "TR":#Top to right
			temp = self.__Top[0][0]
			self.__Top[0][0] = self.__Top[0][2]
			self.__Top[0][2] = self.__Top[2][2]
			self.__Top[2][2] = self.__Top[2][0]
			self.__Top[2][0] = temp
			temp = self.__Top[0][1]
			self.__Top[0][1] = self.__Top[1][2]
			self.__Top[1][2] = self.__Top[2][1]
			self.__Top[2][1] = self.__Top[1][0]
			self.__Top[1][0] = temp

			temp = self.__Front[0]
			self.__Front[0] = self.__Left[0]
			self.__Left[0] = self.__Back[0]
			self.__Back[0] = self.__Right[0]
			self.__Right[0] = temp

			self.__Moves.append("TR")

			if self.__count < 10:
				self.__count += 1

		if b == "DL":#Down to left
			temp = self.__Down[0][0]
			self.__Down[0][0] = self.__Down[2][0]
			self.__Down[2][0] = self.__Down[2][2]
			self.__Down[2][2] = self.__Down[0][2]
			self.__Down[0][2] = temp
			temp = self.__Down[0][1]
			self.__Down[0][1] = self.__Down[1][0]
			self.__Down[1][0] = self.__Down[2][1]
			self.__Down[2][1] = self.__Down[1][2]
			self.__Down[1][2] = temp

			temp = self.__Front[2]
			self.__Front[2] = self.__Right[2]
			self.__Right[2] = self.__Back[2]
			self.__Back[2] = self.__Left[2]
			self.__Left[2] = temp

			self.__Moves.append("DL")

			if self.__count < 10:
				self.__count += 1
			
		if b == "DR":#Down to right

			temp = self.__Down[0][0]
			self.__Down[0][0] = self.__Down[0][2]
			self.__Down[0][2] = self.__Down[2][2]
			self.__Down[2][2] = self.__Down[2][0]
			self.__Down[2][0] = temp
			temp = self.__Down[0][1]
			self.__Down[0][1] = self.__Down[1][2]
			self.__Down[1][2] = self.__Down[2][1]
			self.__Down[2][1] = self.__Down[1][0]
			self.__Down[1][0] = temp

			temp = self.__Front[2]
			self.__Front[2] = self.__Left[2]
			self.__Left[2] = self.__Back[2]
			self.__Back[2] = self.__Right[2]
			self.__Right[2] = temp

			self.__Moves.append("DR")

			if self.__count < 10:
				self.__count += 1

		if b == "RR":#Right to right
			temp = self.__Right[0][0]
			self.__Right[0][0] = self.__Right[2][0]
			self.__Right[2][0] = self.__Right[2][2]
			self.__Right[2][2] = self.__Right[0][2]
			self.__Right[0][2] = temp

			temp = self.__Right[0][1]
			self.__Right[0][1] = self.__Right[1][0]
			self.__Right[1][0] = self.__Right[2][1]
			self.__Right[2][1] = self.__Right[1][2]
			self.__Right[1][2] = temp
			
			temp = self.__Top[0][2]
			temp1 = self.__Top[1][2]
			temp2 = self.__Top[2][2]
			self.__Top[0][2] = self.__Front[0][2]
			self.__Top[1][2] = self.__Front[1][2]
			self.__Top[2][2] = self.__Front[2][2]
			self.__Front[0][2] = self.__Down[2][2]
			self.__Front[1][2] = self.__Down[1][2]
			self.__Front[2][2] = self.__Down[0][2]
			self.__Down[0][2] = self.__Back[0][0]
			self.__Down[1][2] = self.__Back[1][0]
			self.__Down[2][2] = self.__Back[2][0]
			self.__Back[0][0] = temp
			self.__Back[1][0] = temp1
			self.__Back[2][0] = temp2

			self.__Moves.append("RR")

			if self.__count < 10:
				self.__count += 1
				
		if b == "RL":#Right to left
			
			temp = self.__Right[0][0]
			self.__Right[0][0] = self.__Right[0][2]
			self.__Right[0][2] = self.__Right[2][2]
			self.__Right[2][2] = self.__Right[2][0]
			self.__Right[2][0] = temp

			temp = self.__Right[0][1]
			self.__Right[0][1] = self.__Right[1][2]
			self.__Right[1][2] = self.__Right[2][1]
			self.__Right[2][1] = self.__Right[1][0]
			self.__Right[1][0] = temp
			
			temp = self.__Top[0][2]
			temp1 = self.__Top[1][2]
			temp2 = self.__Top[2][2]
			self.__Top[0][2] = self.__Back[2][0]
			self.__Top[1][2] = self.__Back[1][0]
			self.__Top[2][2] = self.__Back[0][0]
			self.__Back[0][0] = self.__Down[0][2]
			self.__Back[1][0] = self.__Down[1][2]
			self.__Back[2][0] = self.__Down[2][2]
			self.__Down[0][2] = self.__Front[2][2]
			self.__Down[1][2] = self.__Front[1][2]
			self.__Down[2][2] = self.__Front[0][2]
			self.__Front[0][2] = temp
			self.__Front[1][2] = temp1
			self.__Front[2][2] = temp2

			self.__Moves.append("RL")

			if self.__count < 10:
				self.__count += 1
				
		if b == "LL":#Left to left
			temp = self.__Left[0][0]
			self.__Left[0][0] = self.__Left[0][2]
			self.__Left[0][2] = self.__Left[2][2]
			self.__Left[2][2] = self.__Left[2][0]
			self.__Left[2][0] = temp

			temp = self.__Left[0][1]
			self.__Left[0][1] = self.__Left[1][2]
			self.__Left[1][2] = self.__Left[2][1]
			self.__Left[2][1] = self.__Left[1][0]
			self.__Left[1][0] = temp

			temp = self.__Front[0][0]
			temp1 = self.__Front[1][0]
			temp2 = self.__Front[2][0]
			self.__Front[0][0] = self.__Down[0][0]
			self.__Front[1][0] = self.__Down[1][0]
			self.__Front[2][0] = self.__Down[2][0]
			self.__Down[0][0] = self.__Back[0][2]
			self.__Down[1][0] = self.__Back[1][2]
			self.__Down[2][0] = self.__Back[2][2]
			self.__Back[0][2] = self.__Top[0][0]
			self.__Back[1][2] = self.__Top[1][0]
			self.__Back[2][2] = self.__Top[2][0]
			self.__Top[0][0] = temp
			self.__Top[1][0] = temp1
			self.__Top[2][0] = temp2

			self.__Moves.append("LL")

			if self.__count < 10:
				self.__count += 1

		if b == "LR":#Left to Right
			Fake = self.__Left

			temp = self.__Left[0][0]
			self.__Left[0][0] = self.__Left[2][0]
			self.__Left[2][0] = self.__Left[2][2]
			self.__Left[2][2] = self.__Left[0][2]
			self.__Left[0][2] = temp

			temp = self.__Left[0][1]
			self.__Left[0][1] = self.__Left[1][0]
			self.__Left[1][0] = self.__Left[2][1]
			self.__Left[2][1] = self.__Left[1][2]
			self.__Left[1][2] = temp

			temp = self.__Front[0][0]
			temp1 = self.__Front[1][0]
			temp2 = self.__Front[2][0]
			self.__Front[0][0] = self.__Top[0][0]
			self.__Front[1][0] = self.__Top[1][0]
			self.__Front[2][0] = self.__Top[2][0]
			self.__Top[0][0] = self.__Back[0][2]
			self.__Top[1][0] = self.__Back[1][2]
			self.__Top[2][0] = self.__Back[2][2]
			self.__Back[0][2] = self.__Down[0][0]
			self.__Back[1][2] = self.__Down[1][0]
			self.__Back[2][2] = self.__Down[2][0]
			self.__Down[0][0] = temp
			self.__Down[1][0] = temp1
			self.__Down[2][0] = temp2

			self.__Moves.append("LR")

			if self.__count < 10:
				self.__count += 1
			
		if b == "ADR":#All diagonal to right
			sp = self.__Front[0][0]
			self.__Front[0][0] = self.__Front[2][0]
			self.__Front[2][0] = self.__Front[2][2]
			self.__Front[2][2] = self.__Front[0][2]
			self.__Front[0][2] = sp

			sp = self.__Front[0][1]
			self.__Front[0][1] = self.__Front[1][0]
			self.__Front[1][0] = self.__Front[2][1]
			self.__Front[2][1] = self.__Front[1][2]
			self.__Front[1][2] = sp

			sp = self.__Back[0][0]
			self.__Back[0][0] = self.__Back[0][2]
			self.__Back[0][2] = self.__Back[2][2]
			self.__Back[2][2] = self.__Back[2][0]
			self.__Back[2][0] = sp

			sp = self.__Back[0][1]
			self.__Back[0][1] = self.__Back[1][2]
			self.__Back[1][2] = self.__Back[2][1]
			self.__Back[2][1] = self.__Back[1][0]
			self.__Back[1][0] = sp



			s1 = self.__Top[0][0]
			s2 = self.__Top[0][1]
			s3 = self.__Top[0][2]
			s4 = self.__Top[1][0]
			s5 = self.__Top[1][1]
			s6 = self.__Top[1][2]
			s7 = self.__Top[2][0]
			s8 = self.__Top[2][1]
			s9 = self.__Top[2][2]

			self.__Top[0][0] = self.__Left[2][0]
			self.__Top[0][1] = self.__Left[1][0]
			self.__Top[0][2] = self.__Left[0][0]
			self.__Top[1][0] = self.__Left[2][1]
			self.__Top[1][1] = self.__Left[1][1]
			self.__Top[1][2] = self.__Left[0][1]
			self.__Top[2][0] = self.__Left[2][2]
			self.__Top[2][1] = self.__Left[1][2]
			self.__Top[2][2] = self.__Left[0][2]

			self.__Left[0][0] = self.__Down[0][0]
			self.__Left[0][1] = self.__Down[1][0]
			self.__Left[0][2] = self.__Down[2][0]
			self.__Left[1][0] = self.__Down[0][1]
			self.__Left[1][1] = self.__Down[1][1]
			self.__Left[1][2] = self.__Down[2][1]
			self.__Left[2][0] = self.__Down[0][2]
			self.__Left[2][1] = self.__Down[1][2]
			self.__Left[2][2] = self.__Down[2][2]

			self.__Down[0][0] = self.__Right[2][2]
			self.__Down[0][1] = self.__Right[1][2]
			self.__Down[0][2] = self.__Right[0][2]
			self.__Down[1][0] = self.__Right[2][1]
			self.__Down[1][1] = self.__Right[1][1]
			self.__Down[1][2] = self.__Right[0][1]
			self.__Down[2][0] = self.__Right[2][0]
			self.__Down[2][1] = self.__Right[1][0]
			self.__Down[2][2] = self.__Right[0][0]

			self.__Right[0][0] = s7
			self.__Right[0][1] = s4
			self.__Right[0][2] = s1
			self.__Right[1][0] = s8
			self.__Right[1][1] = s5
			self.__Right[1][2] = s2
			self.__Right[2][0] = s9
			self.__Right[2][1] = s6
			self.__Right[2][2] = s3

			self.__Moves.append("ADR")

			if self.__count < 10:
				self.__count += 1

		if b == "ADL":#All Diagonal to left
			sp = self.__Back[0][0]
			self.__Back[0][0] = self.__Back[2][0]
			self.__Back[2][0] = self.__Back[2][2]
			self.__Back[2][2] = self.__Back[0][2]
			self.__Back[0][2] = sp

			sp = self.__Back[0][1]
			self.__Back[0][1] = self.__Back[1][0]
			self.__Back[1][0] = self.__Back[2][1]
			self.__Back[2][1] = self.__Back[1][2]
			self.__Back[1][2] = sp

			sp = self.__Front[0][0]
			self.__Front[0][0] = self.__Front[0][2]
			self.__Front[0][2] = self.__Front[2][2]
			self.__Front[2][2] = self.__Front[2][0]
			self.__Front[2][0] = sp

			sp = self.__Front[0][1]
			self.__Front[0][1] = self.__Front[1][2]
			self.__Front[1][2] = self.__Front[2][1]
			self.__Front[2][1] = self.__Front[1][0]
			self.__Front[1][0] = sp		


			s1 = self.__Top[0][0]
			s2 = self.__Top[0][1]
			s3 = self.__Top[0][2]
			s4 = self.__Top[1][0]
			s5 = self.__Top[1][1]
			s6 = self.__Top[1][2]
			s7 = self.__Top[2][0]
			s8 = self.__Top[2][1]
			s9 = self.__Top[2][2]

			self.__Top[0][0] = self.__Right[0][2]
			self.__Top[0][1] = self.__Right[1][2]
			self.__Top[0][2] = self.__Right[2][2]
			self.__Top[1][0] = self.__Right[0][1]
			self.__Top[1][1] = self.__Right[1][1]
			self.__Top[1][2] = self.__Right[2][1]
			self.__Top[2][0] = self.__Right[0][0]
			self.__Top[2][1] = self.__Right[1][0]
			self.__Top[2][2] = self.__Right[2][0]

			self.__Right[0][0] = self.__Down[2][2]
			self.__Right[0][1] = self.__Down[1][2]
			self.__Right[0][2] = self.__Down[0][2]
			self.__Right[1][0] = self.__Down[2][1]
			self.__Right[1][1] = self.__Down[1][1]
			self.__Right[1][2] = self.__Down[0][1]
			self.__Right[2][0] = self.__Down[2][0]
			self.__Right[2][1] = self.__Down[1][0]
			self.__Right[2][2] = self.__Down[0][0]

			self.__Down[0][0] = self.__Left[0][0]
			self.__Down[0][1] = self.__Left[1][0]
			self.__Down[0][2] = self.__Left[2][0]
			self.__Down[1][0] = self.__Left[0][1]
			self.__Down[1][1] = self.__Left[1][1]
			self.__Down[1][2] = self.__Left[2][1]
			self.__Down[2][0] = self.__Left[0][2]
			self.__Down[2][1] = self.__Left[1][2]
			self.__Down[2][2] = self.__Left[2][2]

			self.__Left[0][0] = s3
			self.__Left[0][1] = s6
			self.__Left[0][2] = s9
			self.__Left[1][0] = s2
			self.__Left[1][1] = s5
			self.__Left[1][2] = s8
			self.__Left[2][0] = s1
			self.__Left[2][1] = s4
			self.__Left[2][2] = s7

			self.__Moves.append("ADL")

			if self.__count < 10:
				self.__count += 1

		if b == "AL":##All to right
			temp = self.__Down[0][0]
			self.__Down[0][0] = self.__Down[0][2]
			self.__Down[0][2] = self.__Down[2][2]
			self.__Down[2][2] = self.__Down[2][0]
			self.__Down[2][0] = temp

			temp = self.__Down[0][1]
			self.__Down[0][1] = self.__Down[1][2]
			self.__Down[1][2] = self.__Down[2][1]
			self.__Down[2][1] = self.__Down[1][0]
			self.__Down[1][0] = temp

			temp = self.__Top[0][0]
			self.__Top[0][0] = self.__Top[0][2]
			self.__Top[0][2] = self.__Top[2][2]
			self.__Top[2][2] = self.__Top[2][0]
			self.__Top[2][0] = temp

			temp = self.__Top[0][1]
			self.__Top[0][1] = self.__Top[1][2]
			self.__Top[1][2] = self.__Top[2][1]
			self.__Top[2][1] = self.__Top[1][0]
			self.__Top[1][0] = temp
			
			Fake1 = [[None]*3]*3

			Fake1[0] = self.__Front[0]
			self.__Front[0] = self.__Left[0]
			self.__Left[0] = self.__Back[0]
			self.__Back[0] = self.__Right[0]
			self.__Right[0] = Fake1[0]
			
			Fake1 = [[None]*3]*3

			Fake1[2] = self.__Front[2]
			self.__Front[2] = self.__Left[2]
			self.__Left[2] = self.__Back[2]
			self.__Back[2] = self.__Right[2]
			self.__Right[2] = Fake1[2]
			
			Fake1 = [[None]*3]*3
			
			Fake1[1] = self.__Front[1]
			self.__Front[1] = self.__Left[1]
			self.__Left[1] = self.__Back[1]
			self.__Back[1] = self.__Right[1]
			self.__Right[1] = Fake1[1]

			self.__Moves.append("AL")

			if self.__count < 10:
				self.__count += 1
			
		if b == "AR":#All to left
			temp = self.__Down[0][0]
			self.__Down[0][0] = self.__Down[2][0]
			self.__Down[2][0] = self.__Down[2][2]
			self.__Down[2][2] = self.__Down[0][2]
			self.__Down[0][2] = temp
			temp = self.__Down[0][1]
			self.__Down[0][1] = self.__Down[1][0]
			self.__Down[1][0] = self.__Down[2][1]
			self.__Down[2][1] = self.__Down[1][2]
			self.__Down[1][2] = temp

			Fake1 = [[None]*3]*3

			Fake1[2] = self.__Front[2]
			self.__Front[2] = self.__Right[2]
			self.__Right[2] = self.__Back[2]
			self.__Back[2] = self.__Left[2]
			self.__Left[2] = Fake1[2]
			
			temp = self.__Top[0][0]
			self.__Top[0][0] = self.__Top[2][0]
			self.__Top[2][0] = self.__Top[2][2]
			self.__Top[2][2] = self.__Top[0][2]
			self.__Top[0][2] = temp

			temp = self.__Top[0][1]
			self.__Top[0][1] = self.__Top[1][0]
			self.__Top[1][0] = self.__Top[2][1]
			self.__Top[2][1] = self.__Top[1][2]
			self.__Top[1][2] = temp

			Fake1 = [[None]*3]*3

			Fake1[0] = self.__Front[0]
			self.__Front[0] = self.__Right[0]
			self.__Right[0] = self.__Back[0]
			self.__Back[0] = self.__Left[0]
			self.__Left[0] = Fake1[0]

			Fake1 = [[None]*3]*3
			
			Fake1[1] = self.__Front[1]
			self.__Front[1] = self.__Right[1]
			self.__Right[1] = self.__Back[1]
			self.__Back[1] = self.__Left[1]
			self.__Left[1] = Fake1[1]

			self.__Moves.append("AR")

			if self.__count < 10:
				self.__count += 1

		if b == "BL":#Back to left
			temp = self.__Back[0][2]
			self.__Back[0][2] = self.__Back[2][2]
			self.__Back[2][2] = self.__Back[2][0]
			self.__Back[2][0] = self.__Back[0][0]
			self.__Back[0][0] = temp

			temp = self.__Back[0][1]
			self.__Back[0][1] = self.__Back[1][2]
			self.__Back[1][2] = self.__Back[2][1]
			self.__Back[2][1] = self.__Back[1][0]
			self.__Back[1][0] = temp
			
			Fake = [[None]*3]*3

			Fake[0][0] = self.__Top[0][0]
			Fake[0][1] = self.__Top[0][1]
			Fake[0][2] = self.__Top[0][2]
			self.__Top[0][0] = self.__Left[2][0]
			self.__Top[0][1] = self.__Left[1][0]
			self.__Top[0][2] = self.__Left[0][0]
			self.__Left[2][0] = self.__Down[0][2]
			self.__Left[1][0] = self.__Down[0][1]
			self.__Left[0][0] = self.__Down[0][0]
			self.__Down[0][2] = self.__Right[0][2]
			self.__Down[0][1] = self.__Right[1][2]
			self.__Down[0][0] = self.__Right[2][2]
			self.__Right[0][2] = Fake[0][0]
			self.__Right[1][2] = Fake[0][1]
			self.__Right[2][2] = Fake[0][2]

			self.__Moves.append("BL")

			if self.__count < 10:
				self.__count += 1

		if b == "BR":#Back to right
			temp = self.__Back[0][2]
			self.__Back[0][2] = self.__Back[0][0]
			self.__Back[0][0] = self.__Back[2][0]
			self.__Back[2][0] = self.__Back[2][2]
			self.__Back[2][2] = temp

			temp = self.__Back[0][1]
			self.__Back[0][1] = self.__Back[1][0]
			self.__Back[1][0] = self.__Back[2][1]
			self.__Back[2][1] = self.__Back[1][2]
			self.__Back[1][2] = temp
			
			Fake = [[None]*3]*3

			Fake[0][0] = self.__Top[0][0]
			Fake[0][1] = self.__Top[0][1]
			Fake[0][2] = self.__Top[0][2]
			self.__Top[0][0] = self.__Right[0][2]
			self.__Top[0][1] = self.__Right[1][2]
			self.__Top[0][2] = self.__Right[2][2]
			self.__Right[0][2] = self.__Down[0][2]
			self.__Right[1][2] = self.__Down[0][1]
			self.__Right[2][2] = self.__Down[0][0]
			self.__Down[0][2] = self.__Left[2][0]
			self.__Down[0][1] = self.__Left[1][0]
			self.__Down[0][0] = self.__Left[0][0]
			self.__Left[2][0] = Fake[0][0]
			self.__Left[1][0] = Fake[0][1]
			self.__Left[0][0] = Fake[0][2]

			self.__Moves.append("BR")

			if self.__count < 10:
				self.__count += 1
				
		if b == "AU":#All to up
			temp = self.__Left[0][0]
			self.__Left[0][0] = self.__Left[0][2]
			self.__Left[0][2] = self.__Left[2][2]
			self.__Left[2][2] = self.__Left[2][0]
			self.__Left[2][0] = temp

			temp = self.__Left[0][1]
			self.__Left[0][1] = self.__Left[1][2]
			self.__Left[1][2] = self.__Left[2][1]
			self.__Left[2][1] = self.__Left[1][0]
			self.__Left[1][0] = temp

			temp = self.__Right[0][2]
			self.__Right[0][2] = self.__Right[0][0]
			self.__Right[0][0] = self.__Right[2][0]
			self.__Right[2][0] = self.__Right[2][2]
			self.__Right[2][2] = temp

			temp = self.__Right[0][1]
			self.__Right[0][1] = self.__Right[1][0]
			self.__Right[1][0] = self.__Right[2][1]
			self.__Right[2][1] = self.__Right[1][2]
			self.__Right[1][2] = temp
			
			Fake = [[None]*3]*3

			Fake[0] = self.__Front[0]
			Fake[1] = self.__Front[1]
			Fake[2] = self.__Front[2]
			self.__Front[0] = self.__Down[2]
			self.__Front[1] = self.__Down[1]
			self.__Front[2] = self.__Down[0]
			self.__Down[0] = self.__Back[0][::-1]
			self.__Down[1] = self.__Back[1][::-1]
			self.__Down[2] = self.__Back[2][::-1]
			self.__Back[0] = self.__Top[2][::-1]
			self.__Back[1] = self.__Top[1][::-1]
			self.__Back[2] = self.__Top[0][::-1]
			self.__Top[0] = Fake[0]
			self.__Top[1] = Fake[1]
			self.__Top[2] = Fake[2]

			self.__Moves.append("AU")

			if self.__count < 10:
				self.__count += 1

		if b == "AD":#All to down
			temp = self.__Left[0][0]
			self.__Left[0][0] = self.__Left[2][0]
			self.__Left[2][0] = self.__Left[2][2]
			self.__Left[2][2] = self.__Left[0][2]
			self.__Left[0][2] = temp

			temp = self.__Left[0][1]
			self.__Left[0][1] = self.__Left[1][0]
			self.__Left[1][0] = self.__Left[2][1]
			self.__Left[2][1] = self.__Left[1][2]
			self.__Left[1][2] = temp

			temp = self.__Right[0][2]
			self.__Right[0][2] = self.__Right[2][2]
			self.__Right[2][2] = self.__Right[2][0]
			self.__Right[2][0] = self.__Right[0][0]
			self.__Right[0][0] = temp

			temp = self.__Right[0][1]
			self.__Right[0][1] = self.__Right[1][2]
			self.__Right[1][2] = self.__Right[2][1]
			self.__Right[2][1] = self.__Right[1][0]
			self.__Right[1][0] = temp

			Fake = [[None]*3]*3

			Fake[0] = self.__Top[0]
			Fake[1] = self.__Top[1]
			Fake[2] = self.__Top[2]
			self.__Top[0] = self.__Back[2][::-1]
			self.__Top[1] = self.__Back[1][::-1]
			self.__Top[2] = self.__Back[0][::-1]
			self.__Back[0] = self.__Down[0][::-1]
			self.__Back[1] = self.__Down[1][::-1]
			self.__Back[2] = self.__Down[2][::-1]
			self.__Down[0] = self.__Front[2]
			self.__Down[1] = self.__Front[1]
			self.__Down[2] = self.__Front[0]
			self.__Front[0] = Fake[0]
			self.__Front[1] = Fake[1]
			self.__Front[2] = Fake[2]

			self.__Moves.append("AD")

			if self.__count < 10:
				self.__count += 1

		self.checkSolvedCube()
		self.draw()

	def __randomMove(self):
		rnd = random.randint(0,5)
		if rnd == 0:
			return "TL"
		elif rnd == 1:
			return "DL"
		elif rnd == 2:
			return "FL"
		elif rnd == 3:
			return "BR"
		elif rnd == 4:
			return "RL"
		else:
			return "LR"

	def shuffleCube(self):
		self.isSolved = False
		for i in range(50):
			self.move(self.__randomMove())
			self.draw()
			pygame.display.flip()
		self.__count = 0

	def Undo(self):
		if self.__count > 0:
			self.__count -= 1
			self.move(self.__Moves[len(self.__Moves)-1])
			self.__count -= 1
			self.move(self.__Moves[len(self.__Moves)-1])
			self.__count -= 1
			self.move(self.__Moves[len(self.__Moves)-1])
			self.__count -= 1
			del(self.__Moves[len(self.__Moves)-1])
			del(self.__Moves[len(self.__Moves)-1])
			del(self.__Moves[len(self.__Moves)-1])
			del(self.__Moves[len(self.__Moves)-1])

	def SolveCube(self):
		if self.__Moves is None:
			pass
		else:
			for i in range(len(self.__Moves)):
				self.move(self.__Moves[len(self.__Moves)-1])
				self.move(self.__Moves[len(self.__Moves)-1])
				self.move(self.__Moves[len(self.__Moves)-1])
				del(self.__Moves[len(self.__Moves)-1])
				del(self.__Moves[len(self.__Moves)-1])
				del(self.__Moves[len(self.__Moves)-1])
				del(self.__Moves[len(self.__Moves)-1])
				self.draw()
				pygame.time.delay(200)
				pygame.display.flip()
		self.__count = 0

	def checkSolvedCube(self):
		if not self.__checkSolvedFace(self.__Front):
			self.isSolved = False
			return
		elif not self.__checkSolvedFace(self.__Back):
			self.isSolved = False
			return
		elif not self.__checkSolvedFace(self.__Left):
			self.isSolved = False
			return
		elif not self.__checkSolvedFace(self.__Right):
			self.isSolved = False
			return
		elif not self.__checkSolvedFace(self.__Top):
			self.isSolved = False
			return
		self.isSolved = True

	def __checkSolvedFace(self,face):
		checker = face[0][0]
		for i in range(3):
			for j in range(3):
				if face[i][j] != checker:
					return False
		return True

	def draw(self):
		for i in range(3):
			for j in range(3):
				Utility.drawLosangF(gameDisplay,self.__Front[i][j],[5+j,3+i+j/3],width,length)
				Utility.drawLosangR(gameDisplay,self.__Right[i][j],[8+j,4+i-j/3],width,length)
				Utility.drawLosangT(gameDisplay,self.__Top[i][j],[7-i+j,2+1/3+j/3+i/3],width,length)

class Utility:
	def drawLosangR(surface, color, point,screenWidth,screenLength):
		dy = screenWidth/9
		dx = screenLength/16
		x0 = point[0]*dx
		y0 = point[1]*dy
		pygame.draw.polygon(surface, color,[(x0,y0),(x0,y0+dy),(x0+dx,y0+dy-dy/3),(x0+dx,y0-dy/3)],0)
		pygame.draw.polygon(surface, (0,0,0),[(x0,y0),(x0,y0+dy),(x0+dx,y0+dy-dy/3),(x0+dx,y0-dy/3)],3)

	def drawLosangF(surface, color, point,screenWidth,screenLength):
		dy = screenWidth/9
		dx = screenLength/16
		x0 = point[0]*dx
		y0 = point[1]*dy
		pygame.draw.polygon(surface, color,[(x0,y0),(x0,y0+dy),(x0+dx,y0+dy+dy/3),(x0+dx,y0+dy/3)],0)
		pygame.draw.polygon(surface, (0,0,0),[(x0,y0),(x0,y0+dy),(x0+dx,y0+dy+dy/3),(x0+dx,y0+dy/3)],3)

	def drawLosangT(surface, color, point,screenWidth,screenLength):
		dy = screenWidth/9
		dx = screenLength/16
		x0 = point[0]*dx
		y0 = point[1]*dy
		pygame.draw.polygon(surface, color,[(x0,y0),(x0+dx,y0+dy/3),(x0+2*dx,y0),(x0+dx,y0-dy/3)],0)
		pygame.draw.polygon(surface, (0,0,0),[(x0,y0),(x0+dx,y0+dy/3),(x0+2*dx,y0),(x0+dx,y0-dy/3)],3)

	def drawButtonRect(surface, point,screenWidth,screenLength):
		dy = screenWidth/9
		dx = screenLength/16
		x0 = int(point[0]*dx)
		y0 = int(point[1]*dy)
		pygame.draw.rect(surface,(105,105,105),(x0,y0,2*dx,dy),0)
		pygame.draw.rect(surface,(0,0,0),(x0,y0,2*dx,dy),3)

	def drawButtonCirc(surface, point,rad,screenWidth,screenLength):
		dy = screenWidth/9
		dx = screenLength/16
		x0 = int(point[0]*dx)
		y0 = int(point[1]*dy)
		pygame.draw.circle(surface,(105,105,105),(x0,y0),int(rad*dx),0)
		pygame.draw.circle(surface,(0,0,0),(x0,y0),int(rad*dx),3)

	def Color(tag):
		if type(tag) == type('a'):
			c = {'white':(255,255,255),'red':(255,0,0),'green':(0,128,0),'blue':(0,0,255),'orange':(255,165,0),'yellow':(255,255,0)}
		else:
			c = [(255,255,255),(255,255,0),(0,128,0),(0,0,255),(255,165,0),(255,0,0)]
		return c[tag]

	def MainFont():
		return pygame.font.SysFont('Arial',	width//10-15)

	def print(text,display,color,posX,posY,screenLength):
		dx = screenLength/16
		text_print = Utility.MainFont().render(text, False, color)
		display.blit(text_print,(posX*dx,posY*dx))

	def insideSqr(pos,point,screenLength):
		dx = screenLength/16
		x = pos[0]
		y = pos[1]
		Lx = point[0]*dx
		Ly = point[1]*dx
		if y >= Ly and y <= Ly+dx:
			if x >= Lx and x <= Lx+dx:
				return True
		else:
			return False
	
pygame.init()
pygame.display.init()
pygame.font.init()
pygame.display.set_caption("Cubo Mágico")

width = 768
length = 1366
gameDisplay = pygame.display.set_mode((length,width))
pygame.draw.rect(gameDisplay, (185,185,185),(0,0,length,width), 0)

Utility.drawButtonRect(gameDisplay,[1,1],width,length)
Utility.print("Shuffle",gameDisplay,(0,0,0),1,1,length)
Utility.drawButtonRect(gameDisplay,[13,1],width,length)
Utility.print("Undo",gameDisplay,(0,0,0),13,1,length)
Utility.drawButtonRect(gameDisplay,[1,7],width,length)
Utility.print("Solve",gameDisplay,(0,0,0),1,7,length)

for i in range(3):
	for j in range(2):
		Utility.drawButtonCirc(gameDisplay,[4.5+7*j,3.5+i],0.15+(i%2)/16,width,length)
		Utility.drawButtonCirc(gameDisplay,[5.5+i+3*j,2.5-i/3+4.7*j],0.15+(i%2)/16,width,length)
		Utility.drawButtonCirc(gameDisplay,[5.5+i+3*j,6.5+i/3-4.7*j],0.15+(i%2)/16,width,length)


play = True
main = Cubo()
ini = time.time()
clock = pygame.time.Clock()

while play:
	for event in pygame.event.get():
		m = pygame.mouse.get_pos()

		if event.type == pygame.QUIT:
			play = False
		if (event.type == pygame.KEYDOWN and event.key == pygame.K_s) or (event.type == pygame.MOUSEBUTTONDOWN and (Utility.insideSqr(m,[1,1],length) or Utility.insideSqr(m,[2,1],length))):
			main.shuffleCube()
			ini = time.time()
		if (event.type == pygame.KEYDOWN and event.key == pygame.K_r):
			main = Cubo()
		if event.type == pygame.KEYDOWN and event.key == pygame.K_v or (event.type == pygame.MOUSEBUTTONDOWN and (Utility.insideSqr(m,[1,7],length) or Utility.insideSqr(m,[2,7],length))):
			main.SolveCube()
		if event.type == pygame.KEYDOWN and event.key == pygame.K_u or (event.type == pygame.MOUSEBUTTONDOWN and (Utility.insideSqr(m,[13,1],length) or Utility.insideSqr(m,[14,1],length))):
			main.Undo()

		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[5,2],length):
			main.move('FL')
		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[6,2-1/3],length):
			main.move('ADL')
		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[7,2-2/3],length):
			main.move('BR')

		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[4,3],length):
			main.move('TL')
		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[4,4],length):
			main.move('AR')
		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[4,5],length):
			main.move('DL')

		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[5,6],length):
			main.move('LR')
		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[6,6+1/3],length):
			main.move('AD')
		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[7,6+2/3],length):
			main.move('RL')

		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[8,2-2/3],length):
			main.move('LL')
		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[9,2-1/3],length):
			main.move('AU')
		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[10,2],length):
			main.move('RR')

		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[11,3],length):
			main.move('TR')
		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[11,4],length):
			main.move('AL')
		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[11,5],length):
			main.move('DR')

		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[8,7],length):
			main.move('FR')
		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[9,7-1/3],length):
			main.move('ADR')
		if event.type == pygame.MOUSEBUTTONDOWN and Utility.insideSqr(m,[10,7-2/3],length):
			main.move('BL')

	if main.isSolved:
		Utility.print("Cube",gameDisplay,(0,0,0),13,6,length)
		Utility.print("Solved!",gameDisplay,(0,0,0),13,7,length)
		ini = time.time()
	else:
		pygame.draw.rect(gameDisplay, (185,185,185),(3*length/4,2*width/3,length,width), 0)
		Utility.drawButtonRect(gameDisplay,[1,4],width,length)
		Utility.print("%.2f" % (time.time()-ini),gameDisplay,(0,0,0),1,4,length)

	pygame.display.flip()
	clock.tick(60)
pygame.quit()
quit()
