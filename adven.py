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

    def text(self):
        print(self.script, end="\n\n")
        if len(self.choices)>0:
            for i in range(len(self.choices)):
                print("{}. {}".format(i+1,self.choices[i][1]), end="\n")
        else:
            print("Game Over.\n")

    def choose(self, userinput):
        if self.choices != []:
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
            item = file.pop(0).split(' ', 1)
            while item != ['\n'] and item != ['eof']:   # Newline that shows end of that section
                choicelist.append([item[0][:-1], item[1]])
                item = file.pop(0).split(' ', 1)
            nodedict[title] = Node(text, choicelist)
    return nodedict, firstnode

def clear():
    import platform
    import os
    if platform.system() == 'Windows':
        _=os.system('cls')
    else:
        _=os.system('clear')

def init(filename):
    nodedict, firstnode = loadnodes(filename)
    currentnode = nodedict[firstnode]



    while 1<2:
        clear()
        currentnode.text()
        try:
            currentnode = nodedict[currentnode.choose(input())]
        except Exception as e:
            print("-----\nTry again.")
        print("-----")



def main():
    import sys
    if len(sys.argv) == 1:
        print("Please provide a filename.")
    elif len(sys.argv) > 2:
        if sys.argv[2] == "-d" or sys.argv[2] == "-debug":
            nodedict, firstnode = loadnodes("adven.txt")
            for key, node in nodedict:
                print("Node Name: {}\nText: {}".format(key, node.script))
                for choice in node.choices:
                    print("{} - {}".format(choice[0], choice[1]))
        else:
            init(sys.argv[1])
    else:   # len(sys.argv) == 2
        init(sys.argv[1])



if __name__ == '__main__':
    main()

        