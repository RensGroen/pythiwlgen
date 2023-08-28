### USAGE: python3 obfuscatechars.py input= output=
### python3 obfuscatechars.py input=~/some/input_file.txt output=~/some/result.txt

from bin import sysArgumentsReader

ioFiles = sysArgumentsReader.SysArgumentsReader()

fixedDict = {
    'a' : ['a', '@', '4'],
    'A' : ['A', '@', '4'],
    'e' : ['e', '3'],
    'E' : ['e', '3'],
    'i' : ['i', '1', '!'],
    'I' : ['I', '1', '!'],
    'o' : ['o', '0'],
    'O' : ['O', '0'],    
}

currentWordIteration = ''
currentIterationOutcome = []

def charIteration(charPos, twoPossibleCharsToPlace, nextFIteration='empty'):
    for char in twoPossibleCharsToPlace:
        global currentWordIteration
        chars = list(currentWordIteration)
        chars[charPos] = char
        currentWordIteration = "".join(chars)
        if nextFIteration != 'empty':
            nextFIteration()
        else:
            currentIterationOutcome.append(currentWordIteration + '\n')

def addFIterationToList(charIterations, charPos, twoPossibleCharsToPlace):  
    charIterations.append(lambda : charIteration(charPos, twoPossibleCharsToPlace))

def addFIterationToList2(charIterations, charPos, twoPossibleCharsToPlace):
    cIt = charIterations[len(charIterations) -1]
    charIterations.append(lambda : charIteration(charPos, twoPossibleCharsToPlace, cIt))

lines = ioFiles.input.readlines()
for line in lines:
    currentWordIteration = str(line)

    chars = list(line.strip())
    charIterations = []
    for index, char in enumerate(chars):
        if char in fixedDict:             
            if len(charIterations) == 0:
                addFIterationToList(charIterations, index, fixedDict.get(char))
            else:
                addFIterationToList2(charIterations, index, fixedDict.get(char))

    if len(charIterations) > 0:
        #execute the lambda char iteration
        charIterations[len(charIterations) -1]()    
        ioFiles.output.writelines(currentIterationOutcome)
        currentIterationOutcome.clear()


ioFiles.output.close()