import os,subprocess

files=os.listdir()

a=''

for file in files:
    if os.path.splitext(file)[1]=='.ui':
        print(file)
        a+=str(subprocess.run('pyside2-uic %s' %(file,),stdout=subprocess.PIPE).stdout)

print(a)

with open('UI.py','w') as file:
    file.write(a)