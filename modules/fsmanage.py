import os, shutil, re

def filter_dirname(dirname):
    return re.sub(r'[./\\\$]', '', dirname)

def whereami():
    print(f'Рабочая директория:\n  {os.getcwd()}')

def makedir(dirname=None):
    dirname = input('Введите название создаваемой папки: ') if dirname is None else dirname
    dirname = filter_dirname(dirname)
    try:
        os.mkdir(os.path.join(os.getcwd(), dirname))
        print(f'Создана папка "{dirname}" в рабочей директории.')
    except FileExistsError:
        print('Папка или файл с таким названием уже существует.')
    except OSError:
        print(f'Папка "{dirname}" не может быть создана.')

def remove(remove_subj=None, exceptional_dirs=[]):
    remove_subj = input('Введите название файла/папки для удаления: ') if remove_subj is None else remove_subj
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

def rename(oldname=None, newname=None):
    oldname = input('Введите название файла/папки для переименования: ') if oldname is None else oldname
    oldname = filter_dirname(oldname)
    if not os.path.exists(oldname):
        print(f'Папка/файл "{oldname}" не существует в рабочей директории.')
        return
    newname = input('Введите новое название для файла/папки: ') if newname is None else newname
    newname = filter_dirname(newname)
    if os.path.exists(newname):
        print(f'Файл/папка с названием "{newname}" уже существует.')
        return
    try:
        os.rename(oldname, newname)
        print(f'Переименован файл/папка "{oldname}". Новое название: "{newname}".')
    except OSError:
        print(f'Возникла ошибка при попытке переименования файла/папки "{oldname}" в "{newname}".')

def move(filename=None, destination=None):
    filename = input('Введите название файла/папки для перемещения: ') if filename is None else filename
    filename = filter_dirname(filename)
    if not os.path.exists(filename):
        print(f'Папка/файл "{filename}" не существует в рабочей директории.')
        return
    destination = input('Введите новую директорию для файла/папки: ') if destination is None else destination
    if os.path.isfile(destination):
        print(f'Перемещение невозможно, т.к. "{destination}" не является директорией.')
        return
    try:
        new_place = shutil.move(filename, os.path.join(destination, filename))
        print(f'Выполнено перемещение файла/папки "{filename}". Новое расположение: "{new_place}".')
    except OSError:
        print(f'Возникла ошибка при попытке перемещения файла/папки "{filename}" в "{destination}".')    

def copy(filename=None, copyname=None):
    filename = input('Введите название файла/папки для копирования: ') if filename is None else filename
    filename = filter_dirname(filename)
    if not os.path.exists(filename):
        print(f'Папка/файл "{filename}" не существует в рабочей директории.')
        return
    copyname = input('Введите название для копии файла/папки: ') if copyname is None else copyname
    copyname = filter_dirname(copyname)
    if os.path.exists(copyname):
        print(f'Файл/папка с названием "{copyname}" уже существует.')
        return
    if os.path.isfile(filename):
        try:
            shutil.copy2(filename, copyname)
            print(f'Создана копия файла "{filename}" с названием "{copyname}".')
        except OSError:
            print(f'Возникла ошибка при создании копии файла с названием "{copyname}".')
    else:
        try:
            shutil.copytree(filename, copyname)
            print(f'Создана копия папки "{filename}" с названием "{copyname}".')
        except OSError:
            print(f'Возникла ошибка при создании копии папки с названием "{copyname}".')
        

def dirlist(dirs_only=False, files_only=False, dump_file=False):
    list_of_files = [path for path in os.listdir() if os.path.isfile(path)]
    list_of_dirs = [path for path in os.listdir() if not os.path.isfile(path)]
    if dirs_only:
        print('Список папок в рабочей директории:')
        print(', '.join(list_of_dirs))
    elif files_only:
        print('Список файлов в рабочей директории:')
        print(', '.join(list_of_files))
    elif dump_file:
        filename = 'dirlist.txt'
        with open(filename, 'w') as dfile:
            dfile.writelines([
                f'files: {", ".join(list_of_files)}\n',
                f'dirs: {", ".join(list_of_dirs)}\n'
            ])
        print(f'Полное содержимое рабочей директории сохранено в файл {filename}.')
    else:
        print('Полное содержимое рабочей директории:')
        print(f'Файлы: {", ".join(list_of_files)}')
        print(f'Папки: {", ".join(list_of_dirs)}')

def changedir(destination=None):
    destination = input('Введите новую рабочую директорию: ') if destination is None else destination
    if not os.path.exists(destination):
        print(f'Не существует рабочей директории "{destination}".')
        return
    if os.path.isfile(destination):
        print(f'"{destination}" не является директорией.')
        return
    os.chdir(destination)
    print('Рабочая директория изменена.')
    whereami()