#!/usr/bin/python1
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import commands
"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  f=open(filename,'r')
  url1=[]
  urls=[]
  d=f.read()
  host=re.search(r'_(\S+)',filename)
 # host1="http://www."+ host.groups(1)[0]
  host1="https://developers.google.com/edu/python"
  url=re.findall(r'\/images\/puzzle\S+\s',d)
  for x in sorted(url):
    urls.append(host1+x.strip())
  f.close()  
  for x in urls:
    if x not in url1:
      url1.append(x)
  return url1

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  cmd='mkdir '+dest_dir
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(status)
  k=[]
  for i in range(len(img_urls)-1):
    rtr='img'
    r=re.search(r'(\w+)\.jpg',img_urls[i]).groups(0) 
    rtr=dest_dir+'/'+rtr+r[0]
    print "retrieving url....",img_urls[i]
    urllib.urlretrieve(img_urls[i],rtr)
    k.append('img'+r[0])
  str1='<html><body>'
  for x in sorted(k):
    str1=str1+'<img src="'+x+'">'
  str1=str1+'\n</body></html>'
  f= open(dest_dir+'/index.html','w')
  f.write(str1)
  f.close()
  
def main():
  args = sys.argv[:3]
  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[1] == '--todir':
    todir = args[2]
    del args[2:3]


  if todir:
    img_urls = read_urls(sys.argv[3])
    download_images(img_urls, todir)
  else:
    img_urls = read_urls(sys.argv[1])
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
