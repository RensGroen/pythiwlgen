### USAGE: python3 obfuscatechars.py input= output=
### python3 addExclamationMark.py input=~/some/input_file.txt output=~/some/result.txt

from bin import sysArgumentsReader

ioFiles = sysArgumentsReader.SysArgumentsReader()

lines = ioFiles.input.readlines()
for line in lines:
    ioFiles.output.writelines([line.strip() + '!\n'])    

ioFiles.output.close()