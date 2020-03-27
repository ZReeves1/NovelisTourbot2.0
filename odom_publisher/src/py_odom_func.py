import time
import math


class d2_odom():
  def __init__(self,vr,vl,t):
    self.vr = vr
    self.vl = vl
    self.t = t
  def printodom(self):
    tab = {'vr':self.vr, 'vl':self.vl,'t':self.t}
    print('vr is {vr:f} and vl is {vl:f} and time is {t:f}'.format(**tab))

def integrate(yt,yi,t,ti):
  dt = t-ti    
  return yi+yt*dt

class robot_loc():
  def __init__(self,x,y,thet):
    self.x = x
    self.y = y
    self.thet = thet 

  def print_location(self):  
    tab = {'x':self.x, 'y':self.y}
    print('robot is at [{x:f},{y:f}]'.format(**tab))

def main():
  i =0
  d1 = d2_odom(0,0,0)
  location = robot_loc(0,0,0)
  l =1
  ts = time.time()
  to = 0
  while i < 10:
    ti = time.time()-ts
    print(ti)
    print(to)
    li = location 
    d1= d2_odom(2,2,i)
    theta = integrate(1/l *(d1.vr-d1.vl),li.thet,ti,to)
    location.x = integrate(.5*(d1.vr+d1.vl),li.x,ti,to)*math.cos(theta)
    location.y = integrate(.5*(d1.vr+d1.vl),li.x,ti,to)*math.sin(theta)
    i=i+1
    location.print_location()
    d1.printodom()
    to=ti
    time.sleep(1)

if __name__ =='__main__':
  Main()
