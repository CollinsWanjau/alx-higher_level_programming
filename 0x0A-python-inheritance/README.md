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
