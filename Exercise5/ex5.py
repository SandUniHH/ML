#!/usr/bin/python3

# import re			# regex
import matplotlib.pyplot as plotter

def readfile():
	filename = './dataCircle.txt'
	f = open(filename, 'r')
	l = f.readlines()
	
	points = [[i for i in range(3)] for j in range(len(l))]

	for i, line in enumerate(l):
	   
	    s = line.split()
	    
	    if s:
             points[i][0] = float(s[0])        
             points[i][1] = float(s[1])
             points[i][2] = float(s[2])        
	'''
	# doesn't work for last line
	 #s = re.search('^\s+(\S+)\s+(\S+)\s+(\S+)\s+', line)        
	    if s:
		points[i][0] = float(s.group(1))
		points[i][1] = float(s.group(2))
		points[i][2] = float(s.group(3))
	'''        

	# print(points)

	return points
 
def get_point_classes(points):
    
    pos = []
    neg = []
    pos_x = []
    pos_y = []
    neg_x = []
    neg_y = []
    
    for point in points:
        if point[2] == 1.0:
            pos_x.append(point[0])
            pos_y.append(point[1])
        else:
            neg_x.append(point[0])
            neg_y.append(point[1])
            
    pos.append(pos_x)
    pos.append(pos_y)
    
    neg.append(neg_x)
    neg.append(neg_y)
            
    return pos, neg
    
 
def point_plotter(pos, neg):
            
    pos_x = pos[0]
    pos_y = pos[1]
    
    neg_x = neg[0]
    neg_y = neg[1]
            
    plotter.plot(pos_x, pos_y, 'go')
    plotter.plot(neg_x, neg_y, 'ro')
    plotter.axis([-10, 10, -10, 10])
    plotter.show()
    
########################################
    
''' 
uniformise intial distribution D1(i) = 1/len(distribution)
compute weighted errors, collect wc with min error
optimise weak classifiers, in the end 4 are enough (maybe 6)
2. set weight
'''

##### main #####

points = readfile()
pos, neg = get_point_classes(points)
point_plotter(pos, neg)