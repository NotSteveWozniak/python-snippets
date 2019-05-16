#!/usr/bin/python3.7

import zipfile
import pathlib

entries = pathlib.Path()
for entry in entries.iterdir():
    print(entry.name)

print('\n*********************\n')
    
zf = zipfile.ZipFile('test.zip', 'r')
print (zf.namelist())

zf.extractall()

