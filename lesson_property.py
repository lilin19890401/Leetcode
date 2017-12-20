# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,value):
        self.__width = value
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,value):
        self.__height = value
    @property
    def resolution(self):
        return self.__width*self.__height

#test
s = screen()
s.width = 1024
s.height = 768
print('resolution = ' ,s.resolution)
if s.resolution == 786432:
    print('YOU SUCCESS~')
else:
    print('you failed~')