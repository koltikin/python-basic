class student:

    def __init__(self,frist,last,pay):
        self.frist = frist
        self.last = last
        self.py = pay
        self.email = frist + '.' + last + '@gmail.com'
    
    def full_name(self,age):
        # return f"{self.frist} {self.last}"
        return "{} {} {} years old".format(self.frist, self.last,age)


student1 = student("ziya","huseyin","4500")
student2 = student("abdullah","ali","6500")

# student1.frist_name = 'ziya'
# student1.last_name = "huseyin"

print(student1.full_name(32))

print(student.full_name(student1,32))
