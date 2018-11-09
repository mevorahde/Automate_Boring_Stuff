# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 17:31:04 2018

@author: David E
"""
import zipfile, os

os.chdir('C:\\Users\\David E') # move to the folder with example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
spamInfo.compress_size
'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size, 2))
exampleZip.close()


