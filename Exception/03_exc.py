import csv
import os

try:
    file = open(os.path.join('Exception','file.csv' ), 'r')
    reader = csv.reader(file)
    for row in reader:
        print(row)

except FileNotFoundError as ex:
    print(ex)
except Exception as ex:
    print(ex)
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print('File closed')
    
try:
    with open(os.path.join('Exception','file.txt' ), 'r') as file:
        lines = file.readlines()
        print(lines)
except FileNotFoundError as ex:
    print(ex)