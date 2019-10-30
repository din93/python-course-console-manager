import os, shutil, re

def filter_dirname(dirname):
    return re.sub(r'[./\\\$]', '', dirname)

def whereami():
    print(f'Рабочая директория:\n  {os.getcwd()}')

def makedir():
    dirname = input('Введите название создаваемой папки: ')
    dirname = filter_dirname(dirname)
    try:
        os.mkdir(os.path.join(os.getcwd(), dirname))
        print(f'Создана папка "{dirname}" в рабочей директории.')
    except FileExistsError:
        print('Папка или файл с таким названием уже существует.')
    except OSError:
        print(f'Папка "{dirname}" не может быть создана.')

def remove(exceptional_dirs=[]):
    remove_subj = input('Введите название файла/папки для удаления: ')
    remove_subj = filter_dirname(remove_subj)
    if os.path.join(os.getcwd(), remove_subj) in exceptional_dirs:
        print(f'Запрещено удаление папки/файла "{remove_subj}"/')
    elif not os.path.exists(f'./{remove_subj}'):
        print(f'Папка/файл "{remove_subj}" не существует в рабочей директории.')
    else:
        try:
            if os.path.isfile(remove_subj):
                os.remove(os.path.join(os.getcwd(), remove_subj))
                print(f'Удален файл "{remove_subj}" в рабочей директории.')
            else:
                shutil.rmtree(os.path.join(os.getcwd(), remove_subj))
                print(f'Удалена папка "{remove_subj}" в рабочей директории.')
        except OSError:
            print(f'Ошибка удаления папки/файла "{remove_subj}".')

def rename():
    source = input('Введите название файла/папки для переименования: ')
    source = filter_dirname(source)
    if not os.path.exists(source):
        print(f'Папка/файл "{source}" не существует в рабочей директории.')
        return
    destination = input('Введите новое название для файла/папки: ')
    destination = filter_dirname(destination)
    if os.path.exists(destination):
        print(f'Файл/папка с названием "{destination}" уже существует.')
        return
        
    try:
        os.rename(source, destination)
        print(f'Переименован файл/папка "{source}". Новое название: "{destination}".')
    except OSError:
        print(f'Возникла ошибка при попытке переименования файла/папки "{source}" в "{destination}".')

def move():
    source_name = input('Введите название файла/папки для перемещения: ')
    source_name = filter_dirname(source_name)
    if not os.path.exists(source_name):
        print(f'Папка/файл "{source_name}" не существует в рабочей директории.')
        return
    destination = input('Введите новую директорию для файла/папки: ')
    if os.path.isfile(destination):
        print(f'Перемещение невозможно, т.к. "{destination}" не является директорией.')
        return
        
    try:
        new_place = shutil.move(source_name, os.path.join(destination, source_name))
        print(f'Выполнено перемещение файла/папки "{source_name}". Новое расположение: "{new_place}".')
    except OSError:
        print(f'Возникла ошибка при попытке перемещения файла/папки "{source_name}" в "{destination}".')    

def copy():
    source = input('Введите название файла/папки для копирования: ')
    source = filter_dirname(source)
    if not os.path.exists(source):
        print(f'Папка/файл "{source}" не существует в рабочей директории.')
        return
    destination = input('Введите название для копии файла/папки: ')
    destination = filter_dirname(destination)
    if os.path.exists(destination):
        print(f'Файл/папка с названием "{destination}" уже существует.')
        return
    
    if os.path.isfile(source):
        try:
            shutil.copy2(source, destination)
            print(f'Создана копия файла "{source}" с названием "{destination}".')
        except OSError:
            print(f'Возникла ошибка при создании копии файла с названием "{destination}".')
    else:
        try:
            shutil.copytree(source, destination)
            print(f'Создана копия папки "{source}" с названием "{destination}".')
        except OSError:
            print(f'Возникла ошибка при создании копии папки с названием "{destination}".')
        

def dirlist(dirs_only=False, files_only=False):
    if dirs_only:
        print('Список папок в рабочей директории:')
        list_of_dirs = [f for f in os.listdir() if not os.path.isfile(f)]
        print(', '.join(list_of_dirs))
    elif files_only:
        print('Список файлов в рабочей директории:')
        list_of_files = [f for f in os.listdir() if os.path.isfile(f)]
        print(', '.join(list_of_files))
    else:
        print('Полное содержимое рабочей директории:')
        print(', '.join(os.listdir()))

def changedir():
    destination = input('Введите новую рабочую директорию: ')
    if not os.path.exists(destination):
        print(f'Не существует рабочей директории "{destination}".')
        return
    if os.path.isfile(destination):
        print(f'"{destination}" не является директорией.')
        return
    os.chdir(destination)
    print('Рабочая директория изменена.')
    whereami()