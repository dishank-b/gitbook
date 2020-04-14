---
description: 'This page helps with python and general programming tips you may not know:'
---

# Python

* **np.random.seed\(\)**:
  * Suppose you write a file, for say shuffling the data. Now everyone time you run the file, you want the random shuffling to be same, then you use np.random.seed\(fixed\_no\). This will allow you to have all the random function generating the same value every time you run the file.  Note:- but suppose if you use the same random function two times in the same file, then if you have use np.random.seed\(fixed\_no\) each time before calling that random function, otherwise that function will return different value in those two calls. But still if only set the seed once, then you get two different values when you run the file, but when run the file again with that seed, you will get same two number as in the previous call of the file.  For more understanding:
    *  [https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.RandomState.html\#numpy.random.RandomState](https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.random.RandomState.html#numpy.random.RandomState)
    * random numbers work by starting with a number \(the seed\), multiplying it by a large number, then taking modulo of that product. The resulting number is then used as the seed to generate the next "random" number. When you set the seed \(every time\), it does the same thing every time, giving you the same numbers.
* **Unit testing**:- The objective of Unit Testing is to isolate a section of code and verify its correctness. In procedural programming a unit may be an individual function or procedure. The purpose is to validate that each unit of the software performs as designed. A unit is the smallest testable part of any software. It usually has one or a few inputs and usually a single output. In procedural programming, a unit may be an individual program, function, procedure, etc. In object-oriented programming, the smallest unit is a method, which may belong to a base/ super class, abstract class or derived/ child class.
  * Benefits:
    * If good unit tests are written and if they are run every time any code is changed, we will be able to promptly catch any defects introduced due to the change.
    * Codes are more reusable. In order to make unit testing possible, codes need to be modular. This means that codes are easier to reuse.
    * Development is faster. How? If you do not have unit testing in place, you write your code and perform that fuzzy ‘developer test’ \(You set some breakpoints, fire up the GUI, provide a few inputs that hopefully hit your code and hope that you are all set.\) But, if you have unit testing in place, you write the test, write the code and run the test. Writing tests takes time but the time is compensated by the less amount of time it takes to run the tests.
  * Tips: 
    * Before fixing a defect, write a test that exposes the defect. Why? First, you will later be able to catch the defect if you do not fix it properly. Second, your test suite is now more comprehensive. Third, you will most probably be too lazy to write the test after you have already fixed the defect.

### **'\*'  and  '\*\*'  Operators**

The single star `*` unpacks the sequence/collection into positional arguments, so you can do this: 

```python
def sum(a, b):
    return a + b

values = (1, 2)

s = sum(*values)
```

This will unpack the tuple so that it actually executes as:

```python
s = sum(1, 2)
```

The double star `**` does the same, only using a dictionary and thus named arguments:

```python
values = { 'a': 1, 'b': 2 }
s = sum(**values)
```

You can also combine:

```python
def sum(a, b, c, d):
    return a + b + c + d

values1 = (1, 2)
values2 = { 'c': 10, 'd': 15 }
s = sum(*values1, **values2)
```

will execute as:

```python
s = sum(1, 2, c=10, d=15)
```

Additionally you can define functions to take `*x` and `**y` arguments, this allows a function to accept any number of positional and/or named arguments that aren't specifically named in the declaration.

Example:

```python
def sum(*values):
    s = 0
    for v in values:
        s = s + v
    return s

s = sum(1, 2, 3, 4, 5)
```

or with `**`:

```python
def get_a(**values):
    return values['a']

s = get_a(a=1, b=2)      # returns 1
```

this can allow you to specify a large number of optional parameters without having to declare them.

And again, you can combine:

```python
def sum(*values, **options):
    s = 0
    for i in values:
        s = s + i
    if "neg" in options:
        if options["neg"]:
            s = -s
    return s

s = sum(1, 2, 3, 4, 5)            # returns 15
s = sum(1, 2, 3, 4, 5, neg=True)  # returns -15
s = sum(1, 2, 3, 4, 5, neg=False) # returns 15
```

### @Property decorator

{% embed url="https://www.programiz.com/python-programming/property" %}

{% embed url="https://www.freecodecamp.org/news/python-property-decorator/" %}

### Yield and Generators

{% embed url="https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/" %}



