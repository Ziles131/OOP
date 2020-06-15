#Example number one
class Snow:
    def __init__(self, x, m):
        self.m = m
        self.x = float(x)
    def __call__(self, xrw):
        self.x = xrw
    def __add__(self, n):
        self.x += n
        return self.x
    def __sub__(self, n):
        self.x -= n
        return self.x
    def __mul__(self, n):
        self.x *= n
        return self.x 
    def __truediv__(self, n):
        self.x /= n
        dround = '{:.1f}'.format(int(self.x))
        return dround
    def __str__(self):
        a = float(self.x) + self.m
        return str(a)
    def makeSnow(self, m):
        self.m = m
        ix = int(self.x )
        return ('\n'+'{:*<'+str(self.m)+'}').format("")*(-ix)


a = Snow(-35, 100)
a(12)
print("1) "+ str(a+85))

print("2) "+ str(a-85))

print("3) "+ str(a*(-5)))

print("4) "+ str(a/15))

print("5) "+ str(a))

print(a.makeSnow(3))

'''class Snow:   #Example number two
    def __init__(self, x, m):
        self.m = m
        self.x = float(x)
    def __call__(self, xrw):
        self.x = xrw
    def __add__(self, n):
        self.n = n
        return self.x+self.n
    def __sub__(self, n):
        self.n = n
        return self.x - self.n
    def __mul__(self, n):
        self.n = n
        return self.x * self.n
    def __truediv__(self, n):
        self.n = n
        dround = '{:.1f}'.format(int(self.x / self.n))
        return dround
    def __str__(self):
        a = float(self.x) + self.m
        return str(a)
    def makeSnow(self, m):
        self.m = m
        return ('\n'+'{:*<'+str(self.m)+'}').format("")*self.x


a = Snow(-35, 100)
a(12)
print("1) "+ str(a+85))

print("2) "+ str(a-85))

print("3) "+ str(a*(-5)))

print("4) "+ str(a/15))

print("5) "+ str(a))

print(a.makeSnow(3))'''



