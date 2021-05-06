# -*- coding: utf-8 -*-
import re
import sys
#读取文件内容，并写入另一个文件

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
    #打开C文件
    f = open(cfilename,'r+')
    all_lines = f.readlines()
    f.seek(0)
    f.truncate()
    index = 0
    for line in all_lines:   
        matchObj = re.search('"([^"]+)",', line, re.M|re.I)
        commit_text = 'txtid = %d'
        result = commit_text not in line
        if matchObj and result:           
            old_list[index] = old_list[index].strip()
            new_list[index] = new_list[index].strip()
            line = line.replace(old_list[index], new_list[index])
            index = index + 1
        f.write(line)
    f.close()               
    new_file.close()
    old_file.close()
if __name__ == "__main__":
    cfilename = sys.argv[1]
    newfile  = sys.argv[2]
    oldfile  = sys.argv[3]
    txt2txt(cfilename,newfile,oldfile)
