import os, sys
import modules.fsmanage as fsmanage
from modules.playvictory import play_victory
from modules.playbankaccount import play_bank_account

current_transactions = []
exceptional_dirs = [os.path.join(os.getcwd(), f) for f in ['modules', 'main.py', '.git']]

def print_help():
    print('Список команд:')
    print('  help => вывести список доступных команд')
    print('  whereami => просмотр рабочей директории')
    print('  makedir => создать папку')
    print('  remove => удалить (файл/папку)')
    print('  rename => переименовать (файл/папку)')
    print('  move => переместить (файл/папку)')
    print('  copy => копировать (файл/папку)')
    print('  dirlist => просмотр содержимого рабочей директории')
    print('  dirlist-d => посмотреть только папки')
    print('  dirlist-f => посмотреть только файлы')
    print('  changedir => смена рабочей директории')
    print('  sysinfo => просмотр информации об операционной системе')
    print('  playvictory => играть в викторину')
    print('  playbankaccount => мой банковский счет')
    print('  author => создатель программы')
    print('  exit => выход')

def sysinfo():
    print('Операционная система:', os.environ['OS'])
    print('Имя пользователя:', os.environ['USERNAME'])
    print('Программная платформа:', sys.platform)

print('\nSimple Commands Manager v0.1')
fsmanage.whereami()
print('Используйте команду "help" для получения информации о доступных командах')
print('Вводите команду после @>:')
while True:
    command = input('@> ').lower().strip()
    if command == 'help':
        print_help()
    elif command == 'whereami':
        fsmanage.whereami()
    elif command == 'makedir':
        fsmanage.makedir()
    elif command == 'remove':
        fsmanage.remove(exceptional_dirs=exceptional_dirs)
    elif command == 'rename':
        fsmanage.rename()
    elif command == 'move':
        fsmanage.move()
    elif command == 'copy':
        fsmanage.copy()
    elif command == 'dirlist':
        fsmanage.dirlist()
    elif command == 'dirlist-d':
        fsmanage.dirlist(dirs_only=True)
    elif command == 'dirlist-f':
        fsmanage.dirlist(files_only=True)
    elif command == 'changedir':
        fsmanage.changedir()
    elif command == 'sysinfo':
        sysinfo()
    elif command == 'playvictory':
        play_victory()
    elif command == 'playbankaccount':
        current_transactions = play_bank_account(current_transactions)
    elif command == 'author':
        print('Автор программы: Динов Радик Камилевич')
        print('vk.com/din_93')
        print('t.me/din_93')
    elif command == 'exit':
        print('Завершение Simple File Manager...')
        break
    else:
        print('Не распознана введенная команда')
