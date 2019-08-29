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
def binom_coeff(a, b):
    if b == 0:
      return Complex(Fraction(1,1),Fraction(0,1))
    else:
      return a*binom_coeff(a-1,b-1)/b
def binomp1_series(x, a, n):
    ans = Complex(Fraction(0,1),Fraction(0,1))
    for k in range(0, n):
      ans += binom_coeff(a, k)*(x**k)
    return ans
def lnp1_series(x, n):
    ans = Complex(Fraction(0,1),Fraction(0,1))
    for k in range(1, n):
      ans += Fraction((-1)**(k-1), k)*(x**k)
    return ans
def binom_series(x, a, n):
  return binomp1_series((x-1)/(x+1), a, n)*binomp1_series(-(x-1)/(x+1), -a, n)
def ln_series(x, n):
  return lnp1_series((x-1)/(x+1), n)-lnp1_series(-(x-1)/(x+1), n)
# tau is pi*2
def tau(m):
    return 8*lnp1_series(j,m).im

