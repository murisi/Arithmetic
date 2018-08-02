# This script contains an implemetation of some of the functions in Complex
# Arithmetic. The definition of a complex number here is compatible with the
# one in Arithmetic, that is, a pair of rational numbers.

from fractions import Fraction

class Complex:
    def __init__(self, rp, ip):
        self.re = rp
        self.im = ip
    def __coerce(self, i):
        if isinstance(i, Complex):
            return i
        else:
            return Complex(i, 0)
            
    def __imul__(self, o):
        o = self.__coerce(o)
        rp = (self.re * o.re) - (self.im*o.im)
        ip = (self.re * o.im) + (self.im * o.re)
        self.re = rp
        self.im = ip
        return self
    def __mul__(self, o):
        o = self.__coerce(o)
        return Complex((self.re * o.re) - (self.im*o.im),
            (self.re * o.im) + (self.im * o.re))
    def __rmul__(self, o):
        o = self.__coerce(o)
        return o * self
    # Exponentiation by squaring
    def __pow__(self, o):
        if o < 0:
            return 1/(self ** -o)
        ans = Complex(1,0)
        tmp = self
        while o > 0:
            if o % 2 == 1:
                ans *= tmp
            o //= 2
            tmp *= tmp
        return ans
    def abs2(self):
        return (self.re * self.re)+(self.im * self.im)
    def conj(self):
        return Complex(self.re, -self.im)
    def __truediv__(self, o):
        o = self.__coerce(o)
        tmp1 = self * o.conj()
        tmp2 = o.abs2()
        return Complex(tmp1.re / tmp2, tmp1.im / tmp2)
    def __rtruediv__(self, o):
        o = self.__coerce(o)
        return o / self
    def __neg__(self):
        return Complex(-self.re, -self.im)
    def __pos__(self):
        return Complex(self.re, self.im)
    def __add__(self, o):
        o = self.__coerce(o)
        return Complex(self.re + o.re, self.im + o.im)
    def __radd__(self, o):
        o = self.__coerce(o)
        return o + self
    def __sub__(self, o):
        o = self.__coerce(o)
        return Complex(self.re - o.re, self.im - o.im)
    def __rsub__(self, o):
        o = self.__coerce(o)
        return o - self
    def __eq__(self, o):
        o = self.__coerce(o)
        return self.re == o.re and self.im == o.im
    def __ne__(self, o):
        o = self.__coerce(o)
        return not (self == o)
    def __str__(self):
        return str(self.re) + "+" + str(self.im) + "j"
    def __repr__(self):
        return "Complex(" + repr(self.re) + ", " + repr(self.im) + ")"
    def __complex__(self):
        return complex(self.re, self.im)

# the imaginary unit
j = Complex(Fraction(0,1),Fraction(1,1))
def exp(n, x):
    return (1 + (x/n))**n
def sin(n, x):
    return (exp(n, x*j) - exp(n, -x*j)) / (2*j)
def cos(n, x):
    return (exp(n, x*j) + exp(n, -x*j)) / (2)
def mu(a, b, n):
    l = []
    for i in range(n):
        l.append(a + i*b)
    return l
# tau is pi*2
def tau(m):
    # the following code integrates 1/x over a path from 1 to i
    path = mu(1, (j-1)/m, m+2)
    thesum = 0
    for i in range(0, m+1):
        thesum += (path[i+1] - path[i])/path[i]
    return thesum * (4/j)