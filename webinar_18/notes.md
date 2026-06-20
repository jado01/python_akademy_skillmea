# Webinar 18 – Object-Oriented Programming (OOP)

## What is OOP?

* OOP (Object-Oriented Programming) is a programming paradigm.
* It defines how we structure and organize code.
* Until now we mostly used procedural programming:

  * functions
  * inputs and outputs
  * operations on data

---

## Important Concepts

### Class

A class is a blueprint or template for creating objects.

Example:

```python
class Person:
    pass
```

Naming convention:

* Use CamelCase for class names.
* Examples:

  * `Person`
  * `Car`
  * `EmployeeManager`

---

### Object (Instance)

An object is an instance of a class.

```python
p1 = Person()
p2 = Person()
```

* `p1` and `p2` are objects of class `Person`.
* We can create many objects from one class.

Analogy:

* Class = house blueprint
* Object = real house built from that blueprint

---

## Constructor - `__init__`

The constructor initializes object data.

```python
class Person:
    def __init__(self):
        pass
```

Rules:

* Constructor name is always `__init__`.
* First parameter must be `self`.
* `self` represents the current object.
* Constructor can accept any number of parameters.

---

## Attributes

Attributes store object data.

```python
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
```

Creating objects:

```python
p1 = Person("Janko", "Hrasko")
p2 = Person("Michal", "Hrasko")
```

Accessing attributes:

```python
print(p1.name)
print(p2.name)
```

---

## Default Parameters

Constructor parameters can have default values.

```python
class Person:
    def __init__(self, name, surname, is_student=False):
        self.name = name
        self.surname = surname
        self.is_student = is_student
```

Example:

```python
s1 = Person(
    name="Ferko",
    surname="Mrkvicka",
    is_student=True
)
```

---

## Methods (Behavior)

Methods define object behavior.

```python
class Person:
    def introduce_yourself(self):
        print(
            f"Hi my name is {self.name} "
            f"and my surname is {self.surname}"
        )
```

Calling a method:

```python
p1.introduce_yourself()
```

Important:

* Methods must have `self`.
* Through `self` we access object attributes.
* Python automatically passes `self`.

---

## Methods Can Contain Logic

Methods can use:

* conditions
* loops
* variables
* function parameters

Example:

```python
def introduce_yourself(self):
    if self.is_student:
        print("I am a student")
```

---

## Method Parameters

Methods can receive additional parameters.

```python
def introduce_yourself(self, repeat=1):
```

Example:

```python
p1.introduce_yourself(2)
```

---

## Calling Methods from Other Methods

Methods can call other methods.

```python
self.introduce_yourself()
```

Methods can be called from:

* constructor
* another method

---

## Designing a Class

When creating a class, ask:

1. What data should objects store?
2. What behavior should objects have?

Example:

```python
class Person:
```

Data:

* name
* surname
* car
* student status

Behavior:

* introduce yourself

---

## Objects Inside Objects

Objects can contain other objects.

```python
class Car:
```

```python
class Person:
```

Example:

```python
car = Car("Volkswagen", "AA12345")

person = Person(
    "Janko",
    "Hrasko",
    car,
    is_student=True
)
```

Usage:

```python
person.car.get_info()
```

---

## Mutable vs Immutable

Be careful with mutable objects.

Example:

```python
class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = list(members)
```

Why?

Without copying:

```python
self.members = members
```

changes to the original list would affect the object.

Safe version:

```python
self.members = list(members)
```

This creates a copy of the list.

---

## Key Takeaways

* Everything in Python is an object.
* Class = blueprint.
* Object = instance of a class.
* Constructor = `__init__`.
* `self` refers to the current object.
* Attributes store data.
* Methods define behavior.
* Objects can contain other objects.
* Be careful with mutable types.
