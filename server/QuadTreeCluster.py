import logging

logging.root.setLevel(logging.INFO)
returnedObject = []


class QuadTree:

	def __init__(self,BoundBox,lvl):
		
		self.BoundBox = BoundBox 
		self.nodes = [None]*4
		self.level = lvl
		self.maxlevel = 8
		self.objects = []
		self.maxobjects = 3 # Capacity of the taxi
		 
	def clear(self):
		
		'''Recursively clear the quadtree '''

		for node in self.nodes:
			if node:
				node.clear()
				node = None

		for data in self.objects:
			data = None

		self.nodes =[]
		self.objects = []

		for data in returnedObject:
			returnedObject.remove(data)


	def getAllobjects(self):

		if self.nodes[0]!=None:
			for nodes in self.nodes:
				nodes.getAllobjects()

		if len(self.objects)!=0:
			returnedObject.append(self.objects)
		return returnedObject

	
	def findNearbyobjects(self,obj):

		index = self.getIndex(obj)
		if (index != -1 and self.nodes[0]!=None and len(self.objects)==0):
			self.nodes[index].findNearbyobjects(obj)

		if len(self.objects)!=0:
			returnedObject = returnedObject.extend(self.objects)
		
		return returnedObject


	def getIndex(self,obj):

		index = -1
		verticalMidPoint   = self.BoundBox['x']+(self.BoundBox['width']/2)
		horizontalMidPoint = self.BoundBox['y']+(self.BoundBox['height']/2)

		left = obj['x'] < verticalMidPoint
		right = obj['x'] > verticalMidPoint

		if left:

			if obj['y']<horizontalMidPoint:
				index =  1
			
			elif obj['y']>horizontalMidPoint:
				index =  2
		else:
			if obj['y']<horizontalMidPoint:
				index = 0
			else:
				index = 3

		return index


	def split(self):

		subWidth  = self.BoundBox['width']/2 or 0
		subHeight = self.BoundBox['height']/2 or 0

		square1 = {
			'x': self.BoundBox['x'] + subWidth,
			'y': self.BoundBox['y'],
			'width': subWidth,
			'height': subHeight
		}
		
		square2 = {
			'x': self.BoundBox['x'],
			'y':	self.BoundBox['y'],
			'width': subWidth,
			'height': subHeight
		}

		square3 = {
			'x': self.BoundBox['x'],
			'y': self.BoundBox['y']+subHeight,
			'width': subWidth,
			'height': subHeight
		}

		square4 = {
			'x': self.BoundBox['x'] + subWidth,
			'y': self.BoundBox['y'] + subHeight,
			'width': subWidth,
			'height': subHeight
		}

		self.nodes[0] = QuadTree(square1,self.level+1)
		self.nodes[1] = QuadTree(square2,self.level+1)
		self.nodes[2] = QuadTree(square3,self.level+1)
		self.nodes[3] = QuadTree(square4,self.level+1)


	def insert(self,obj):

		if self.nodes[0] :
			index = self.getIndex(obj)
			if index!=-1:
				self.nodes[index].insert(obj)
				return 

		self.objects.append(obj)

		if len(self.objects)+1>self.maxobjects and self.level<self.maxlevel:
			if self.nodes[0]==None:
				self.split()

			i = 0
			while i<len(self.objects):

				index = self.getIndex(self.objects[i])
				if index!=-1:
					self.nodes[index].insert(self.objects.pop(i))
				else:
					i+=1

