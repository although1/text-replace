#!/bin/bash
sourceFile=$1
newFile=$2

if [ -z $1 ]
then
    echo "use: sh txt2c.sh test.txt"
    exit 1
fi
 
if [ ! -f "${sourceFile}" ];then
    echo "the file of ${sourceFile} doesn't exists!"
    exit 1
fi

if [ -z $2 ]
then
    echo "use: sh txt2c.sh test.txt"
    exit 1
fi
 
if [ ! -f "${newFile}" ];then
    echo "the file of ${newFile} doesn't exists!"
    exit 1
fi

outputFile=`echo ${sourceFile}|awk -F'/' '{print $NF}'|awk -F'.' '{print $1}'`
echo "outputFile = $outputFile"

fileDir=${sourceFile%/*}

script_path=`dirname $0`
script_path=`cd $script_path && pwd`
 
file_path=`dirname $1`
file_path=`cd $file_path && pwd`

 
python ${script_path}/txt2c.py  ${sourceFile} ${file_path}/${outputFile} ${newFile}
 
