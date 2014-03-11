"""__author__ = 'anyu'
Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can only move
in two directions: right and down. How many possible paths are there for the robot?
FOLLOW UP
Imagine certain squares are "off limits", such that the robot can not step on them. Design an algorithm to
get a path for the robot.
find a path is much easier, the 4th edition finds all paths, which is miserably complex

"""

def nways(x,y,x0,y0):
    """
    set upperleft location (0,0), downright coordination(M,N)
    x0,y0, can not be step on!
    assume x=M,y=N
    if multiple "off limits",just turn x0 and y0 into two array
    """
    if x is x0 and y is y0: return 0
    if x <= 0 or y <= 0: #  if x == 0 and y == 0:  this is wrong, right one exclude 3 out of 4 Quadrant(xiangxian)
                           #   x = 0 or y = 0 is also ok
        return 1
    else:
        return nways(x-1,y,x0,y0)+nways(x,y-1,x0,y0)

print nways(3,4,2,1)
print nways(3,4,10,10)



def isfree(x,y):
    if [x,y] in [[2,1],[1,2]]:return False
    else:return True

def getapath(x,y,path=[]):
    """
    only find one path, use backtracking
    """
    path+=[x,y]
    if x is 0 and y is 0: return True

    suc = False
    if x>=1 and isfree(x-1,y):
        suc = getapath(x-1,y,path)
    if suc is False and y>=1 and isfree(x,y-1):
        suc = getapath(x,y-1,path)
    if suc is False:
        path.pop()
    return suc

def getallpath(x,y,n=0,paths=[[]]): # n is index of paths, no offlimits points
    if x < 0 or y < 0: return paths
    if x is 0 and y is 0:
        paths[n]=[x,y]+paths[n]; n += 1
    return getallpath(x-1,y,n,paths)+getallpath(x,y-1,n,paths)





""" too many parameters! gotta need helper fuctions, and reduce parameters, intends to find all paths!
def nways2(x,y,x0,y0 nofpaths=0,paths=[[]]):

    if x <= 0 or y <= 0: #  if x == 0 and y == 0:  this is wrong, right one exclude 3 out of 4 Quadrant(xiangxian)
                           #   x = 0 or y = 0 is also ok
        return [nofpaths+1, paths[nofpaths].append([x,y])]

    [n1,p1] = nways2(x-1,y,nofpaths,paths)
    if isfree(x,y):
            return [nofpaths,paths[nofpaths].pop()]

    [n2,p2] = nways2(x,y-1,nofpaths,paths)
    return [n1+n2, p1+p2]

print nways2(3,4,0,[[]])
"""