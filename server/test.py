from QuadTreeCluster import *
cluster = QuadTree({'x':0,'y':0,'width':800,'height':800},0)
data = {'x':350,'y':345,'width':800,'height':800}
cluster.insert(data)
data = {'x':800,'y':145,'width':800,'height':800}
cluster.insert(data)

data = {'x':250,'y':345,'width':800,'height':800}

cluster.insert(data)
data = {'x':150,'y':455,'width':800,'height':800}
cluster.insert(data)
data = {'x':350,'y':515,'width':800,'height':800}
cluster.insert(data)
data = {'x':750,'y':145,'width':800,'height':800}
cluster.insert(data)


cluster.getAllobjects()

for i in returnedObject:
	print i
