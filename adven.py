# Choose your own adventure game
# Nyhilo, Nov 2017

###########
# Classes #
###########
class Node(object):
    def __init__(self, script, choices):
        """
        script is a string
        choices is an array of arrays of the format [[key, text], [key, text]]
        """
        self.script = script
        self.choices = choices

    def print_choices(self):
        print(self.script, end="\n")

        if len(self.choices) > 1:
            for i in range(len(self.choices)):
                print("{}. {}".format(i+1,self.choices[i][1]), end="\n")
        elif len(self.choices) == 1:
            print(self.choices[0][1], end="\n")
        else:
            print("\nGame Over.")
        print("> ", end='')

    def choose(self, userinput):
        if len(self.choices) == 1:
            return self.choices[0][0]
        elif len(self.choices) != 0:
            return self.choices[int(userinput)-1][0]
        else:
            quit()


#############
# Functions #
#############

def loadnodes(filename):
    file = []
    with open(filename, 'r') as f:
        file = f.readlines()

    nodedict = dict()
    firstnode = file[0].lstrip().split(' ', 1)[0][:-1]   # Marks the label of the first node

    linecount = 0

    # Load each block as a node
    while len(file) > 0:
        # Pops the first line of a block, this is the Node's label and text
        line = file.pop(0)
        linecount += 1

        #Looks to see if the next line is indented, if there is a next line
        indent = True
        while(indent):
            if len(file) > 0:
                if file[0][:1] == "\t":
                    line = line + file.pop(0)[1:]
                    linecount += 1
                elif file[0][:4] == "    ":
                    line = line + file.pop(0)[4:]
                    linecount += 1
                else: indent = False
            else: indent = False

        # Cleans up the leading whitespace leftover then splits the line into an array of the format [label, text]
        line = line.lstrip().split(' ', 1)

        # Looks to see if the popped line has text in it, if not we can skip to the next line
        if line != ['\n']:
            # Strips the last character from the label
            label, text = line[0][:-1], line[1]

            if label in nodedict:
                print("Duplicate Label detected on line {}. Overwriting previous...".format(linecount))

            # Empty choice list to be populated
            choicelist = []

            try:
                # List all subsequent lines as choices until we find a newline
                line = file.pop(0).lstrip().split(' ', 1)
                linecount += 1

                while line != ['']:   # Newline that shows end of that block
                    choicelist.append([line[0][:-1], line[1]])
                    if len(file) > 0:   # Tells us if we are at the end of the file
                        line = file.pop(0).lstrip().split(' ', 1)
                        linecount += 1
            except IndexError:
                    print("IndexError at {}".format(line))
            finally:
                nodedict[label] = Node(text, choicelist)

            nodedict[label] = Node(text, choicelist)
    return nodedict, firstnode


def clear(error=""):
    import platform
    import os
    if platform.system() == 'Windows':
        _=os.system('cls')
    else:
        _=os.system('clear')

    if error: print(error)

###########
# Globals #
###########

Usage = """
        \n\tUsage: [py|python3] adven.py [FILENAME] <-d |-debug>\n
        The -debug argument will print a list of all nodes in the source file.
        """

########
# Main #
########

def init(filename):
    nodedict, firstnode = loadnodes(filename)
    currentnode = nodedict[firstnode]
    clear("Welcome to the game. Type a number of your choice and press 'Enter' to continue. Press Ctrl+C at any time to quit.\n-----\n")

    while 1<2:
        currentnode.print_choices()
        try:
            currentnode = nodedict[currentnode.choose(input())]
            clear()
        except Exception as e:
            clear(error="-----\nIncorrect entry, try again...")
        print("-----")


def main():
    import sys
    if len(sys.argv) == 1:
        print(Usage)

    elif len(sys.argv) > 2:
        if sys.argv[2] == "-d" or sys.argv[2] == "-debug":
            nodedict, firstnode = loadnodes(sys.argv[1])
            for key, node in nodedict.items():
                print("Node Name: {}\nText: {}Choices:".format(key, node.script))
                for choice in node.choices:
                    print("{} - {}".format(choice[0], choice[1]),end='')
                print("\n")
        else:
            init(sys.argv[1])
    else:   # len(sys.argv) == 2
        init(sys.argv[1])



if __name__ == '__main__':
    main()

        