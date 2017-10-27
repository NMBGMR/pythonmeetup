9/6

Current status
------------------------
- Slack signup
- Github signup

- learnpython.org
- try.git


New Github repo
----------------------
- make repo
- use default rename, .gitignore, license

Using pycharm
----------------------
- clone project
- setup interpreter / create conda env


Using conda
------------------------
- installed?
- conda create -nmyenv pip
- source activate myenv

- note path for `setup interpreter`
- make two different envs and switch between them


Common Do's/Don'ts
- string assembly
  ```python
  # do
  new_str = 'this is a {} formatted string => {}'.format(desc, myvar)
  
  # dont
  new_str = 'this is a'+' poorly '+ 'formatted string => '+'some text'
  ```
- path assembly
  ```python
  # do
  new_path = os.path.join(a,b,c)
  
  # dont
  new_path = '/Users/ross/Documents/data/foo/bar'
  
  # easy way to get "home" folder
  home = os.path.expandusr('~')
  ```
- opening a file
  ```python
  # do
  with open(path_to_file, 'r') as rfile:
    for line in rfile:
      print line.strip()
      
  # dont
  rfile = open(path_to_file,'r')
  
  DIGRESSION: remember files are iterable. Sooo
  
  # do
  for line in rfile:
    ...
    
  # dont
  lines = rfile.readlines()
  for line in lines:
    ...
  ```
- iteration
  ```python
  # Use xrange instead of range
  # Don't
  for i in range(10):
  	print i
  	
  # Do
  for i in xrange(10):
  	print i
  	
  # Use enumerate instead of manual counter
  # Don't
  cnt = 0
  for line in xrange(10,20):
  	print cnt, line
  	cnt+=1
  	
  # Do
  for cnt, line in enumerate(xrange(10,20)):
  	print cnt, line
  ```

TODOs
-------------------
- open a file and write its contents to another file
- open a csv file and write its contents slightly modified to another file. e.g swap column order, format number (0.000), add a column, etc. See [csvdata.csv](https://github.com/NMTHydro/SWACodingMeeting/blob/master/csvdata.csv) for an example file
