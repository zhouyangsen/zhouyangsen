
class Student():
    native_place='吉林'
    
    def __init__(pp,ee,ff):
        pp.ee=ee
        pp.ff=ff

    def eat(self):
        print(self.ee+'在吃饭')
    def moving(self,yundong):
        self.yundong=yundong
        print(self.ee+' '+'is'+' '+yundong+'ing')

def show(name):
        print(name+'在表演')

stu1=Student('zhangsan',20)

stu2=Student('lisi',30)

stu1.show=show
stu2.show=show

stu1.eat()
stu1.show('zhangsan')
stu2.show('lili')
stu1.moving('runn')