# -*- coding: utf-8 -*-
class ConstError(TypeError) : pass
class _const:
    
    def __init__(self):pass
    def __setattr__(self, key, value):
        # self.__dict__
        #print(key,self.__dict__)
        #print("\n")
        if key in self.__dict__:
            raise ConstError("{key}是不可以重新定义的变量!!!".format(key=key))
        self.__dict__[key] = value

import sys

sys.modules[__name__] = _const()