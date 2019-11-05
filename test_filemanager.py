from modules.playvictory import play_victory
from modules.playbankaccount import play_bank_account
from modules.fsmanage import whereami, makedir, remove, rename, move, copy, dirlist, changedir
from main import sysinfo
import os, shutil

def test_sysinfo():
    sysinfo()

def test_whereami():
    whereami()

def test_makedir():
    try:
        makedir('test_test_test')
        assert 'test_test_test' in os.listdir()
    finally:
        os.removedirs('test_test_test')

def test_remove():
    try:
        os.mkdir('test_test_test')
        remove('test_test_test')
        assert 'test_test_test' not in os.listdir()
    except:
        os.removedirs('test_test_test')
        assert False

def test_rename():
    try:
        os.mkdir('test_test_test')
        rename('test_test_test', 'newname_test_test_test')
        assert 'newname_test_test_test' in os.listdir()
        os.removedirs('newname_test_test_test')
    except:
        os.removedirs('test_test_test')
        assert False        

def test_move():
    try:
        os.mkdir('test_test_test')
        os.mkdir('parent_test_test_test')
        move('test_test_test', 'parent_test_test_test')
        assert 'test_test_test' in os.listdir('./parent_test_test_test')
    finally:
        shutil.rmtree('parent_test_test_test')
        if 'test_test_test' in os.listdir():
            shutil.rmtree('test_test_test')

def test_copy():
    try:
        os.mkdir('test_test_test')
        copy('test_test_test', 'copy_test_test_test')
        assert 'test_test_test' in os.listdir() and 'copy_test_test_test' in os.listdir()
    finally:
        shutil.rmtree('test_test_test')
        if 'copy_test_test_test' in os.listdir():
            shutil.rmtree('copy_test_test_test')

def test_dirlist():
    dirlist()
    dirlist(dirs_only=True)
    dirlist(files_only=True)

def test_changedir():
    prev_dir = os.getcwd()
    changedir('..')
    assert os.getcwd() != prev_dir
