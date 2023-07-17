# 0x0A. Python - Inheritance

# Inheritance

* The syntax for a derived class definition looks like this:

```
class DerivedClassName(BaseClassName):
	<statement-1>
	.
	.
	.
	<statement-2>
```

```
class DerivedClassName(modname.BaseClassName):
```

* Execution of a derived class definition proceeds the same as for a base class.
When the class object is constructed, the base class is remembered.

* This is used to resolve attribute refs: if a requested attribute is not found in the class, the search proceeds to look in the base class.This rule is applied recursively if the base class itself is derived from some other class.

* ```DerivedClassName()``` creates a new instance of the class.Method references a resolved as follws: the corresponding class attr is searched, descending down the chain of base classes if necessary and the method ref is valid if this yields a 
 function object.

* An overriding method in a derived class may in fact want to extend rather than simply replace the base class method of the same name.

* There's a simple way to call the base class method directly: just call `BaseClassName(self, args)`.

# Multiple Inheritance

```
class DerivedClassName(Base1, Base2, Base3):
	<statement-1>
	.
	.
	.
	<statement-2>
```

* For most purposes, in the simplest cases, you can think of the search for attrs
 inherited from a parent class as depth-first, left-to-right, not searching twice in the same class where there is an overlap in the hierachy.

* Thus, if an attr is not found in `DerivedClassName`, it is searched for in Base1, then (-r) in the base classes of Base1, if not there, it was searched for in Base2, and so on.

* Dynamic ordering is necessary because all cases of multiple inheritance exhibit one or more diamond relationships.

* To keep the base classes from being accessed more than once, the dynamic algorithm linearizes the search order in a way that preserves the left-to-right ordering specified in each class, that calls each parent only once, and that is monotonic (meaning that a class can be subclassed without affecting the precedence order of ot parents).

## Tasks

### 0. Lookup

Write a function that returns the list of available attributes and methods of an object:

Prototype: def lookup(obj):
Returns a list object
You are not allowed to import any module

```
guillaume@ubuntu:~/0x0A$ cat 0-main.py
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

guillaume@ubuntu:~/0x0A$ ./0-main.py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
guillaume@ubuntu:~/0x0A$
```
