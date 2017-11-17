# Choose your own adventure game
# Nyhilo, Nov 2017

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
            print("Game Over.")

    def choose(self, userinput):
        if len(self.choices) == 1:
            return self.choices[0][0]
        elif len(self.choices) != 0:
            return self.choices[int(userinput)-1][0]
        else:
            quit()


def loadnodes(filename):
    file = []
    with open(filename, 'r') as f:
        file = f.readlines()

    nodedict = dict()
    firstnode = file[0].split(' ', 1)[0][:-1]
    while len(file)>0:
        item = file.pop(0).split(' ', 1)
        if item != ['\n']: # Indicates newline that we can skip
            title, text = item[0][:-1], item[1]
            choicelist = []
            try:
                item = file.pop(0).split(' ', 1)
                while item != ['\n']:   # Newline that shows end of that section
                    choicelist.append([item[0][:-1], item[1]])
                    item = file.pop(0).split(' ', 1)
            except (IndexError):
                nodedict[title] = Node(text, choicelist)

            nodedict[title] = Node(text, choicelist)
    return nodedict, firstnode

def clear(error=""):
    import platform
    import os
    if platform.system() == 'Windows':
        _=os.system('cls')
    else:
        _=os.system('clear')

    if error: print(error)

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

Usage = """
        \n\tUsage: [py|python3] adven.py [FILENAME] <-d |-debug>\n
        The -debug argument will print a list of all nodes in the source file.
        """

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
                    print("{} - {}".format(choice[0], choice[1]),end="")
                print("\n")
        else:
            init(sys.argv[1])
    else:   # len(sys.argv) == 2
        init(sys.argv[1])



if __name__ == '__main__':
    main()

        