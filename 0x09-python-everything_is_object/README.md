# 0x09. Python - Everything is object

## Learning Objectives

* Why Python programming is awesome
* What is an object
* What is the difference between a class and an object or instance
* What is the difference between immutable object and mutable object
* What is a reference
* What is an assignment
* What is an alias
* How to know if two variables are identical
* How to know if two variables are linked to the same object
* How to display the variable identifier (which is the memory address in the CPython implementation)
* What is mutable and immutable
* What are the built-in mutable types
* What are the built-in immutable types
* How does Python pass variables to functions


## Data Model

### Objects, values and types

* Objects are Python's abstraction for data.

* All data in a Python program is represented by objects or by relations between objects.

* Every object has an identity, a type and a value.

* An object's identity never changes once it has been created; i.e an object's address in memory.The `is` operator compares the identity of two objects; the `id()` function returns an integer representing representing it's identity.

* An object's type determines the operations that the object supports (e.g., "does it have a length?") and also defines the possible values for objects of that type..

* Like identity, an object's type is also unchangeable.

* Objects are never explicitly destroyed by the programmer.Instead, the Python interpreter has a garbage collector that automatically reclaims memory occupied by the objects that are no longer reachable or referenced.

* When an object becomes unreachable, meaning there are no references to it from any part of the program, it becomes a candidate for garbage collection.The garbage collector periodically scans the heap, identifies and collects these unreachable objects, and frees up the memory they were occupying

* Some objects contain references to other objects; these are called `containers`.Examples of containers are tuples, lists and dictionaries

* The refs are part of a container's value. In most cases, when we talk about the value of a container, we imply thwe values, not the identities of the contained objects.;however, when  we talk about the mutability of a container, only the identities of the immediately contained objects are implied.So, if an immutable container (like a tuple) contains a ref to a mutable object, its value changes if that mutable objest is changed.
