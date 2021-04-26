# -*- coding: utf-8 -*-
import re
import sys
#读取文件内容，并写入另一个文件

def replace(file_path, old_str, new_str):
    f = open(file_path,'r+')
    all_lines = f.readlines()
    f.seek(0)
    f.truncate()
    for line in all_lines:
        line = line.replace(old_str, new_str)
        f.write(line)
    f.close()
def txt2txt(cfilename,newfile,oldfile):
#cfilename='lang_ru.c'
#newfile='lang_ru'
#oldfile='lang_en'

    #打开翻译好的文件，比如lang_ru
    new_file = open(newfile,'r')
    new_list = new_file.readlines()
    #打开对应的源语言文件，比如lang_en
    old_file = open(oldfile,'r')
    old_list = old_file.readlines()
    for i in range(len(old_list)):
        old_list[i] = old_list[i].strip()
        new_list[i] = new_list[i].strip()
        replace(cfilename, old_list[i],new_list[i])              
    new_file.close()
    old_file.close()
if __name__ == "__main__":
    cfilename = sys.argv[1]
    newfile  = sys.argv[2]
    oldfile  = sys.argv[3]
    txt2txt(cfilename,newfile,oldfile)
