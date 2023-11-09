######################################
#                                    #
#             VIRALFORTH             #
#           Dawson Richards          #
#                                    #
######################################


#initialize a python dictionary (.pydef file)
def importdictionary(filename):

    imported_dict = {}
    pydict = open(filename)
    readDef = False

    for line in pydict.readlines():

        # Execute statements that start with `$:` directly
        # Useful for import statements for the module
        if line.startswith('$:'):
            exec(line.lstrip("$: "))
        
        #if a line starts with a colon, it's considered the definition name.
        #No python code starts a line with a colon
        if line.startswith(':'):
            #remove nasty whitespace
            defname = line.strip(":\t\n ")
            readDef = True
            deflines = []
            continue
        
        #The $ symbol is not used in python syntax
        #$$$ indicates the end of a definition
        if line == '$$$\n':    
            readDef = False
            definition = "\n".join(deflines)
            imported_dict[defname] = definition
            continue

        if readDef and not line.startswith('#') and not line.isspace():
            deflines.append(line)
            continue

    pydict.close()
    return imported_dict


pythondict = importdictionary('core.pydef') | importdictionary('circuit.pydef')
forthdict = {}
##################################################

#initialize lists
inputs = []
stack = []

#create easier stack functions
def push(number):
    stack.append(number)

def pop():
    if stack:
        popped_value = stack.pop(len(stack)-1)
        return popped_value
    else:
        print("Stack underflow, chucklenuts. Get it together.")
        return 0

def compiledef(line):
    name = line[1]
    definition = ' '.join(line[2:])
    forthdict[name] = definition
        
    
def interpret(inputted_line):

    #parse inputted words into a list, split along spaces
    inputs = inputted_line.split()

    #check if it's a number or a word in the dictionary
    for word in inputs:

        #if it's a comment, discard the rest of the input
        if word == "#" :
            break

        #if it's a colon, start the colon definition
        if word == ':' :
            compiledef(inputs)
            break
            
        #if it's a number, push it to stack
        elif word.isnumeric() :
            push(int(word))
            
        #if it's in the dictionary, execute it!
        elif word in forthdict :
            interpret(forthdict[word])
        
        elif word in pythondict :
            exec(pythondict[word])

        #otherwise, stop the loop and return an error
        else :
            print(word,"is not a word!!")

def interpretfile(filename):
    file = open(filename)
    for line in file:
        interpret(line)

#run the boot file
interpretfile('boot.vf')

#interpreter loop
while True:
    interpret(input(''))
    print("ok")
