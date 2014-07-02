from QuadTreeCluster import *
from pygeocoder import Geocoder

addresses = [
	"koramangla,Banglore","Powai,Mumbai","Ghatkoper,Mumbai","Salt Lake,Kolkata",
	"Forum Mall,koramangla,Banglore","ITPL road,Banglore","Marathalli,Banglore"
	]
cluster = QuadTree({'x':0,'y':0,'width':18,'height':24},0)

data = {}

for addr in addresses:
	coord = Geocoder.geocode(addr)
	data = {'x':coord.coordinates[0],'y':coord.coordinates[1],'address':addr}
	cluster.insert(data)



print 'Fuck yeah {0}'.format(cluster.getAllobjects())


addr = "Samsung Banglore"
coord = Geocoder.geocode(addr)
data = {'x':coord.coordinates[0],'y':coord.coordinates[1],'address':addr}

cluster.clear()

cluster.insert(data)
print 'Mofo the ans {0}'.format(cluster.getAllobjects())
#print 'Nearest Place to {0} is {1}'.format(addr,cluster.findNearbyobjects(data))
