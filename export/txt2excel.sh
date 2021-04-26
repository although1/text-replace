#!/bin/bash
 
sourceFile=$1
 
if [ -z $1 ]
then
    echo "use: sh txt2excel.sh test.txt"
    exit 1
fi
 
if [ ! -f "${sourceFile}" ];then
    echo "the file of ${sourceFile} doesn't exists!"
    exit 1
fi

#根据lang_en.c 生成lang_en , 目的是取出要翻译的语言
outputFile=`echo ${sourceFile}|awk -F'/' '{print $NF}'|awk -F'.' '{print $1}'`
echo "outputFile = $outputFile"
fileDir=${sourceFile%/*}

script_path=`dirname $0`
script_path=`cd $script_path && pwd`
 
file_path=`dirname $1`
file_path=`cd $file_path && pwd`


#根据lang_en 生成lang_en.xls , 目的是导出语言到Excel
#第一列增加序号
awk '{print FNR"\t"$0}' ${outputFile}  > ${outputFile}_tmp
#第一行增加标题
sed -i '1i id\tEnglish' ${outputFile}_tmp
 
python ${script_path}/txt2excel.py ${outputFile}_tmp ${file_path}/${outputFile}
 
#rm $outputFile
rm ${outputFile}_tmp