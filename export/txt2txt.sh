#!/bin/bash
sourceFile=$1

if [ -z $1 ]
then
    echo "use: sh txt2txt.sh test.txt"
    exit 1
fi
 
if [ ! -f "${sourceFile}" ];then
    echo "the file of ${sourceFile} doesn't exists!"
    exit 1
fi

outputFile=`echo ${sourceFile}|awk -F'/' '{print $NF}'|awk -F'.' '{print $1}'`
echo "outputFile = $outputFile"

if [ ! -f "${outputFile}" ];then
	echo "the file of ${outputFile} doesn't exists!"
	else
	rm "$outputFile"
fi

fileDir=${sourceFile%/*}

script_path=`dirname $0`
script_path=`cd $script_path && pwd`
 
file_path=`dirname $1`
file_path=`cd $file_path && pwd`

 
python ${script_path}/txt2txt.py  ${sourceFile} ${file_path}/${outputFile}
 
