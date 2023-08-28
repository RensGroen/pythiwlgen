### USAGE: python3 obfuscatechars.py input= output= fromYear=
### python3 addYears.py fromYear=1950 input=~/some/input_file.txt output=~/some/result.txt

import datetime
from datetime import datetime

from bin import sysArgumentsReader

sysArgValues = sysArgumentsReader.SysArgumentsReader(['fromYear'])

lines = sysArgValues.input.readlines()
tillYear = datetime.now().year + 1
yearsPerLine = [] 
for line in lines:
    for year in range(int(sysArgValues.getSysArgValue('fromYear')), int(tillYear)):
        yearsPerLine.append(line.strip() + str(year) + '\n')

    sysArgValues.output.writelines(yearsPerLine)
    yearsPerLine.clear()

sysArgValues.output.close()
