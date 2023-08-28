import sys

class SysArgumentsReader:
    systemArgsDict = {}
    def __init__(self, customSysArgs={}):
        for i in range(1, len(sys.argv)):
            if sys.argv[i].startswith('input='):
                self.input = open(sys.argv[i].split('=')[1], 'r')
                continue
                
            if sys.argv[i].startswith('output='):
                self.output = open(sys.argv[i].split('=')[1], 'w')
                continue

            for sysArg in customSysArgs:
                if sys.argv[i].startswith(sysArg):            
                    self.systemArgsDict[sysArg] = sys.argv[i].split('=')[1]

    def getSysArgValue(self, key):
        return self.systemArgsDict[key]                    