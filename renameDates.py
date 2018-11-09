#! python3
# -*- coding: utf-8 -*-
"""
renameDate.py - Renames filesnames with American MM-DD-YYYY date format to European DD-MM-YYYY.
Created on Thu Nov  8 17:45:17 2018

@author: David E
"""
import shutil, os, re

# Create a regex that matches files with the American date format.
datePattern = re.compile( r""" ^(.*?)(( 0 | 1)?\ d)-(( 0 | 1 | 2 | 3)?\ d)-(( 19 | 20)\ d\ d)(.*?) $ """, re.VERBOSE)
# Format for datePattern: 
# - text before the date
# - one or two digits for the month
# - one or two digits for the day
# - four digits for the year
# - all text after the date
                        
# Loop ovr the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    
    # Skip files without a date.
    if mo == None:
        continue
    
    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    
    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename) # uncomment after testing

    

                        

                        
Q