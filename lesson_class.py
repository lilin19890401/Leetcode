# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        if ( (gender != 'male') and (gender != 'female')):
            raise ValueError('bad value!')
        else:
            self.__gender = gender

            
#test
bart = Student('Bart','male')
if bart.get_gender() != 'male':
    print('you failed~')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('you failed~')
    else:
        print('YOU SUCCESS~')
