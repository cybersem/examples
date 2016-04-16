#!
"""
Скрипт для установки рабочей директории в качестве текущей
"""
import os

os.chdir('D:/Py')
print(os.listdir())

if __name__ == '__main__':
    print('current_dir: запущен как скрипт')
else:
    print('%s: запущен как модуль' % __name__)
        
    
