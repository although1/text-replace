# -*- coding: utf-8 -*-
import re
import sys
#读取文件内容，并写入另一个文件
def txt2txt(filename,newfile):
    a_file = open(filename,"r",encoding='utf-8')
    #m = re.findall('"([^"]+)",\n', a_file.read())
    m = re.findall('"([^"]+)",', a_file.read())
    b_file = open(newfile,'w',encoding='utf-8')
    commit_text = 'txtid = %d'
    for item in m:
        if not item.isdigit():
            #.c文件中有行注释是    //printf("Get Ch text txtid = %d\n",txtId); 要排除掉
            #或者把第七行打开，第八行注释，但是要注意，后面不能有空格
            result = commit_text not in item
            if result:
                b_file.write(item+'\n')
    b_file.close()

if __name__ == "__main__":
    filename = sys.argv[1]
    newfile  = sys.argv[2]
    txt2txt(filename,newfile)
