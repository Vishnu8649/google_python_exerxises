#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
def reg(filename):
  match=re.search(r'__[\w]+__',filename)
  d=0
  if match!=None:
    d=1
  else:
    d=0
  return d
def specialfile(dir1):
  d=[]
  filenames=os.listdir(dir1)
  for filename in filenames:
    if reg(filename)==1:
      path=os.path.join(dir1,filename)
      d=d+[os.path.abspath(path)]
  return d
def copyfile1(src,dest):
  if os.path.exists(dest)==True:
    for x in specialfile(src):
      shutil.copy(x,dest)
  else:
    os.mkdir(dest)
    for x in specialfile(src):
      shutil.copy(x,dest)
  return
def zipfile(fname, dir):
  cmd='zip -j '+fname
  dir1= specialfile(dir)
  for x in dir1:
    cmd=cmd+" "+x
  (status,output)=commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)
  
# Write functions and modify main() to call them



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if sys.argv[1] == '--todir':
    todir = sys.argv[2]
    del args[0:3]

  tozip = ''
  if sys.argv[1] == '--tozip':
    tozip = sys.argv[2]
    del args[0:3]

  if len(sys.argv) == 1:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
 
  dirs=sys.argv
  if dirs[1]=='--todir':
    copyfile1(dirs[3],todir)  
  elif dirs[1]=='--tozip':
    zipfile(tozip,dirs[3])
  else:
    for x in  specialfile(dirs[1]):
      print x
  # Call your functions
  
if __name__ == "__main__":
  main()
