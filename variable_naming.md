Variable Naming
---------------

- use all lower case
- use underscores to break up names
```python

# do
path_to_data = os.path.join(root,'data.txt')

# don't
pathtodata = os.path.join...
pathToData = os.path.join...
PathToData = os.path.join...

```
- spell out your variable names. don't use excessive abbreviation
```python
# do
path_to_data = ...
snow_accum = ...
snow_accumulation = ...

# don't 
ptd = ...
p = ...

Sa = ...
sa = ...
s_a =...

```
- ok to use simple variables for common algebra or geometry terms
```python

x,y = 1,2
w,h = 100, 100

d = ((x-x1)**2 + (y-y2)**2)**0.5
```

- name lists/tuples using the plural form
```python
numbers = [1,2,3,4]
letters = ('A','B','C')
```

- use `i` as your iteration counter
- use `_i` or the singular form as your per iteration item
```python

for i, ni in enumerate(numbers):
    print i, ni
    

for number in numbers:
    print number
```

- avoid using buitlins as variable names
```python
id = 123
type = 'dog'
all = [1,2,3,4]
```




