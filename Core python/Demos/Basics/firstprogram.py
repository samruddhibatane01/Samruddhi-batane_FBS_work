#1.str
var = 'First"bit" Solutions'
print(type(var))

var = "Firstbit's solutions"
print(type(var))

var = '''This is first line.
This is second line.'''
print(type(var))

var = """This is first line.
This is second line."""
print(type(var))

####Sequential
#1. list
var = [10,20,30,40]
print(type(var))

#2.tuple
var = (10,20,30,40)
print(type(var))

var = 10,20,30,40
print(type(var))

#3.range
var = range(1,10000000)
print(type(var))

####Set type
#1. set
var = {10,20,30,40}
print(type(var))

#2. frozenset
var = frozenset({10,20,30,40})
print(type(var))

####Mapping
#1. dict
var = {'id':10, 'name':'Samruddhi', 'sal':30000}
print(type(var))

####other
#1. bool
var = True
print(type(var))

#2. Nonetype
var = None
print(type(var))


