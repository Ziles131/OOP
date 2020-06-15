class Person:
    def __init__(self, n, s, sp = 1):
        self.name = n
        self.surname = s
        self.specialization = sp
    def ret(self):
        return "Cотрудник: "+str(self.name)+" "+str(self.surname)+" "+str(self.specialization)
    def __del__(self):
        a1 = self.name
        a2 = self.surname
        a = str(a1) + " " + str(a2)
        print("До свидания, мистер " + a)
        del a1
        del a2

obj1 = Person("Nick", "Tompson", 2)
obj2 = Person("Tom", "Perry", 5)
obj3 = Person("Luis", "Jackson")

print(obj1.ret() +'\n'+ obj2.ret() +'\n'+ obj3.ret())
els = {
"Nick Tompson": obj1,        
"Tom Perry": obj2,
"Luis Jackson": obj3
}
x = els[input()]
eval('x'+'.__del__()')
input()
