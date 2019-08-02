# This Python script generates the TikZ script that generates Figure III:0.

from complex import *

x = Complex(1, 0)
k = 4
N = 10
x1 = -4
y1 = -2
x2 = 3
y2 = 3
step = 1
ticksize = 0.1

print("\\draw[step=%i,help lines] (%f,%f) grid (%f,%f);" % (step, x1, y1, x2, y2)) # grid
print("\\draw[->] (%f,0) -- (%f,0);" % (x1, x2)) # x-axis
print("\\draw[->] (0,%f) -- (0,%f);" % (y1, y2)) # y-axis

for i in range(x1, x2, step):
    print("\\draw (%f, %f) -- (%f,%f);" % (i, ticksize, i, -ticksize)) # x-axis ticks

for i in range(y1, y2, step):
    print("\\draw (%f, %f) -- (%f,%f);" % (ticksize, i, -ticksize, i)) # y-axis ticks

print("\\draw (1,%f) node[anchor=north,fill=white]{$1$};" % (-ticksize))
print("\\draw (%f,1) node[anchor=east,fill=white]{$i$};" % (-ticksize))

# data-points
for i in range(N+1):
    # complex multiplication to obtain next point
    a = x*(1+(k*j/N))
    
    # point label
    if x.re >= 0 and x.im >= 0:
        anchor = "south west"
    elif x.re < 0 and x.im >= 0:
        anchor = "south east"
    elif x.re < 0 and x.im < 0:
        anchor = "north east"
    elif x.re >= 0 and x.im < 0:
        anchor = "north west"
    print("\\draw (%f,%f) node[anchor=%s,fill=white]{$(1+\\frac{%.0fi}{%i})^{%i}$};" % (x.re, x.im, anchor, k, N, i))
    
    # join to next point
    print("\\filldraw (%f,%f) circle (2pt);" % (x.re, x.im))
    if i < N:
        print("\\draw (%f,%f) -- (%f,%f);" % (x.re, x.im, a.re, a.im))
        print("\\filldraw (%f,%f) circle (2pt);" % (a.re, a.im))
    
    # update the current point
    x = a
