import os
import shutil
path1 = 'F:/Madhavi Folder/mark'
path2 = 'F:/Madhavi Folder/mark1'

content = os.listdir(path1)
print(content)

for i in content:
    name,extension = os.path.splitext(i)
    print(name,extension)
    if extension == '':
        continue
    if extension in ['.jpeg','.png']:
        text = path1+'/'+i
        text1 = path2+'/'+'Images Files'
        text2 = path2+'/'+'Image Files'+i
        print(text)
        print(text1)
        if os.path.exists(text1):
            print('Moving '+i+'.....')
            shutil.move(text,text2)
        else:
            os.makedirs(text1)
            print('Moving '+i+'...')
            shutil.move(text,text2)
               