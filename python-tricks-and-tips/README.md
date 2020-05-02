---
description: 'This page helps with python and general programming tips you may not know:'
---

# Python

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



