'''
定义一个学生类，用来描述学生
'''
#定义一个空的类，pass代表直接跳过
class Student():
    pass

#定义一个对象
pingping = Student()

#再定义一个类
class PythonStudent():
    #用none给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 需要注意
    # 1. def DoHomework的缩进层级
    # 2. 系统默认由一个self参数
    def doHomework(self):
        print("我干着呢")

        # 推荐在函数末尾使用return
        return  None

#实例化一个叫pingping的学生，是一个具体的人
pingping = PythonStudent()
print(pingping.name)
print(pingping.age)
#注意成员函数的调用没有传入参数
pingping.doHomework()

