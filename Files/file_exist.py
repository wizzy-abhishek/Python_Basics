import os
dir = 'Files'
path = 'freq.py'

if os.path.exists(os.path.join(dir, path)):
    print(f'The file {path} exists')
else:
    print("Does not exists")