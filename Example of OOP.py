from random import *
class Data:
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]
 
class Teacher:
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
 
class Pupil:
    def __init__(self):
        self.knowledge = []
    def take(self, info):
        self.knowledge.append(info)
    def rem(self):
        x = randint(0,len(self.knowledge)-1)
        self.knowledge.remove(self.knowledge[x])

a = Data('1','2','3')
p = Pupil()
t = Teacher()
t.teach(a[2], p)
t.teach(a[1],p)
t.teach(a[0],p)
p.rem()
print(p.knowledge)
