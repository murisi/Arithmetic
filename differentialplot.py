# This Python script generates the TikZ script that generates Figure IV:0.

from complex import *

k = Complex(Fraction(1,2), 0)
n = 15
N = 40
x1 = 0
y1 = -1
x2 = 4
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
print("\\draw (%f,1) node[anchor=east,fill=white]{$1$};" % (-ticksize))
print("\\draw (2.5,0.75) node[anchor=south west,fill=white]{$\\frac{%i}{%i}(\\frac{[0:%i]}{%i})_{%i}^{\\frac{%i}{%i}-1}$};" % (k.re.numerator,k.re.denominator,N,N/(x2-x1),n,k.re.numerator,k.re.denominator))
print("\\draw (2,0.35355339059327373) -- (2.5,0.75);")
print("\\draw (1.5,1.75) node[anchor=south east,fill=white]{$(\\frac{[0:%i]}{%i})_{%i}^{\\frac{%i}{%i}}$};" % (N,N/(x2-x1),n,k.re.numerator,k.re.denominator))
print("\\draw (2,1.4142135623730951) -- (1.5,1.75);")

# data-points
for i in range(N):
    # complex multiplication to obtain next point
    xc = Complex(1, 0)*(x1+i*(x2-x1)/N)
    xn = Complex(1, 0)*(x1+(i+1)*(x2-x1)/N)
    
    y1c = binom_series(xc, k, n)
    y1n = binom_series(xn, k, n)
    # join to next point
    print("\\filldraw (%f,%f) circle (1pt);" % (xc.re, y1c.re))
    if i < N:
        print("\\draw (%f,%f) -- (%f,%f);" % (xc.re, y1c.re, xn.re, y1n.re))
        print("\\filldraw (%f,%f) circle (1pt);" % (xn.re, y1n.re))
    
    y2c = k*binom_series(xc, k-1, n)
    y2n = k*binom_series(xn, k-1, n)
    # join to next point
    print("\\filldraw (%f,%f) circle (1pt);" % (xc.re, y2c.re))
    if i < N:
        print("\\draw (%f,%f) -- (%f,%f);" % (xc.re, y2c.re, xn.re, y2n.re))
        print("\\filldraw (%f,%f) circle (1pt);" % (xn.re, y2n.re))
    
