#!/usr/bin/python3.7

import zipfile

zf = zipfile.ZipFile('test.zip', 'r')
print (zf.namelist())

zf.extractall()
