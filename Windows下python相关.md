# Windows下python相关

### 下载python

https://www.python.org/downloads/release/python-278/

> python 3.x版本需要Windows8.1以上，我们是Win7故选择python-2.7.8

### python将txt文件转为excel格式

txt2excel.sh

```shell
为了执行txt2py.sh,以及加表头在EXCEl
```

txt2excel.py

```python
作用是将导出来的字符串导入到EXCEl表中
```

##### 编译

在MinGW下执行  `sh txt2excel.sh file.txt`

### mingw安装python

##### windows环境变量

```
path
C:\MinGW\bin;
```

D:\Program Files\python27\Lib\distutils\distutils.cfg  （文件不存在就新建一个）

```
[build] 
compiler = mingw32 
```

### import xlwt #需要的模块

https://pypi.org/project/xlwt/#files

下载完成后，解压到一个目录，命令行执行

`setup.py install`

在另一台电脑按上面步骤操作了还是不行

ModuleNotFoundError: No module named 'xlwt'

原因：python的安装目录有多个

在MinGW中输入 `where python`

```
C:\msys64\mingw64\bin\python.exe
C:\msys64\usr\bin\python.exe
```

拷贝`C:\Users\Administrator.USER-20200507VX\AppData\Local\Programs\Python\Python38\Lib\site-packages\xlwt-1.3.0-py3.8.egg\`下面的xlwt目录分别到上面的

```
C:\msys64\mingw64\lib\python3.8\site-packages
C:\msys64\usr\lib\python3.8\site-packages
```

可能报错：No module named 'setuptools' 

下载 https://pypi.io/packages/source/s/setuptools/setuptools-33.1.1.zip

解压之后，在目录安装  `setup.py install`