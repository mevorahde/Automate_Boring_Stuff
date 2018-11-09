import os
for folderName, subFolders, fileNames in os.walk('C:\\Users\\David E\\delicious'):
    print(' The current folder is ' + folderName)

    for subFolder in subFolders:
        print(' SUBFOLDER OF ' + folderName + ': ' + subFolder)

    for filename in fileNames:
        print(' FILE INSIDE ' + folderName + ': ' + filename)
    print('\n')
print('')


