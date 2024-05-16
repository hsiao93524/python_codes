# Reference: 
# https://medium.com/ai反斗城/類別-class-物件-object-和實體-instance的差別-轉錄-5f359c9787fd
# https://totoroliu.medium.com/物件導向-object-oriented-programming-概念-5f205d437fd6
# https://en.wikipedia.org/wiki/Object-oriented_programming#Inheritance_and_behavioral_subtyping

"""
Three principles of OOP
Encapsulation: Binding together the data and functions 
    that manipulate the data, and that keeps both 
    safe from outside interference and misuse.
Inheritance: Allowing classes to be arranged in a 
    hierarchy that represents "is-a-type-of" relationships.
Polymorphism: The same operation name among objects
    in an inheritance hierarchy may behave differently.
"""

# Class, 類別
class ClassName(object):

    arg_names = ["arg1", "arg2", "arg3"]

    # Constructor function, 建構式, コンストラクタ 【構築子】
    def __init__(self, *args, **kwargs):
        super(ClassName, self).__init__()
        if "arg" in kwargs:
            self.arg = kwargs["arg"]

        # === rapid method ===
        """
        for arg_name in arg_names:
            val = getattr(kwargs, arg_name, None)
            setattr(self, arg_name, val)
        """

        # Encapsulation, 封裝
        self.encapsulation_method()

    # Method, 方法
    def method_A(self):
        # do something
        pass

    # [Polymorphism, 多型] Overloading, 多載
    def method_B(self, arg_a, arg_b=None):
        if arg_b is not None:
            # do something
        else:
            # do something
        pass

    # [Encapsulation, 封裝]
    def encapsulation_method(self):
        # public
        self.arg_a = "arg_a"
        # protect
        self._arg_b = "arg_b"
        # private
        self.__arg_c = "arg_c"

    # [Encapsulation, 封裝] getter
    @property
    def __arg_c(self):
        print('get __arg_c')
        return self.__arg_c

    # [Encapsulation, 封裝] setter
    @__arg_c.setter
    def __arg_c(self, new_val):
        print('set __arg_c')
        self.__arg_c = new_val

# Inheritance, 繼承
class Child(ClassName):
    def __init__(self, *args, **kwargs):
        super(Child, self).__init__(*args, **kwargs)

    # [Polymorphism, 多型] Overriding, 複寫
    def method_B(self):
        # do something different with parent
        pass

# Instance, 實例, 個人喜歡稱「實體」
# Instance: An instanceis an object created from a class
class_obj = ClassName()