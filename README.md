# Introduction

This script allows for the creation of dynamic choose-your-own-adventure style stories. It was created for my friend, who wanted to write a choose your own adventure story but didn't have a good way to do it. Usage is:
  `[py|python3] adven.py [FILENAME] <-d |-debug>`
  
# File Format

The file for the story supports an uncapped number of choices per prompts, as well as multiline prompts.
Prompts are split into blocks separated by newlines. The first line in the block is the prompt label and the prompt itself, separated by a separating character (such as a colon, semicolon, period, etc.) and a single space.
The writer has flexibility with what separating character to use, but there must be one.
If the writer wishes to have a multiline prompt, the immediately following line must be indented with a tab or with 4 spaces.
Subsequent lines are choices for the current prompt.  They consist of the label the choice points to, and the text for the choice.
When loaded, the program will automatically number the choices, unless there is only one choice in which case the program won't bother numbering it.
If there are no choices under a label, the prgram will interpret this as a dead-end and end of the story overall.
A sample file is below.

```
Intro: This is the first label. It is the label that would be shown to the reader first
        These lines are an indented continuation of the first label.
        They have 8 spaces in front of them,
        4 of which will be stripped off when displayed.
c1. This choice leads to the label 'c1' below
c2. This choice leads to the label 'c2' below

c1: This is the c1 label. Note that it has a colon after it instead of a period as above
c3. This choice leads to the label 'c3' below
Intro. This choice leads back to te first label. Looping is absolutely allowed

c2: This is the c2 label
c3. This choice leads to the label 'c3' below
end. This choice leads to the final label

c3: This is the c3 label, it only has one choice, and will only display that choice without numbers to the reader
end: Just pressing enter will bring us to the end.

end: This is the final thing the player sees before the game ends other than "Game over."

```
