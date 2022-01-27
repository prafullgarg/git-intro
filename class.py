#this code is just an test for understanding branching
class test:
    def __init__(self,name,age,language):
        self.__name=name
        self.__age=age
        self.__language=language
    def set_name(self,name):
        self.__name=name
    def set_age(self,age):
        self.__age=age
    def set_language(self,language):
        self.__language=language
    def __str__(self):
        return f"Author : {self.__name}\nAge : {self.__age}\nLanguage : {self.__language}"
name,age,language=map(str,input().split())
t=test(name,int(age),language)
print(t)
