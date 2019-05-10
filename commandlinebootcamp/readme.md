## Command Line Bootcamp

*Original slides and activity were developed by Thomas Padilla and have been lightly altered*

### Introduction
**Before we start, download [interviewfiles.zip](https://github.com/dhatwake2019/day2/raw/master/commandlinebootcamp/interviewfiles.zip), which has some texts and page images for us to work with, and put the .zip file on the Desktop. DO NOT UNZIP THE FILE!**

[Slides here](https://docs.google.com/presentation/d/1ikyXzrrbHEa9JUi14quuGZFMnEkye8tNtKaCVYJawAw/edit?usp=sharing)

During this session you will be introduced to the command line. The
command line is a text based method for interacting with your computer.
There are a great deal of things you can do from the command line, but
for our purposes we’ll just be covering:

-   **Navigation** - moving in and out of directories, figuring out
    where you are, etc.
-   **Creation** - creating folders, moving content around
-   **Manipulation** - reading files, renaming files, and more

In what follows I’ll signal commands you should enter with a '$'
symbol. Only enter the text that comes after the ‘$’. Note that capitalization matters!

For OS X users open the **Terminal** program.

For Windows users, open a program called **[Cygwin](https://www.cygwin.com/).**

### Protips

-   You can drag files into the Terminal rather than type out their filepath (think of this like an address to your file)

-   Pressing the up and down arrow will let you recall commands you enter in the Terminal. Think of this like a command history that you can reuse so you don't need to keep retyping that same command.

-   CTRL A - move cursor to the start of the line

-   CTRL D - move cursor to the end of the line

### Navigation & Creation

Generally speaking most of the stuff you interact with on your computer
is organized according to a hierarchical folder structure that is partially obscured through the GUI. When you first start your command line interpreter, you’ll want to find where you are located in that structure.

**Windows/Cygwin users: when you first open Cygwin, type `$ cd c:/Users/YOURUSERNAME`. If you're not sure of your username, you can type `$ cd:/Users` and then type `$ ls` to see the options. - this will get you to your 'home' directory**

Find your location in the filesystem using print working directory
**pwd**

`$ pwd`

List the folders and files at your location using list directory **ls**

`$ ls`

Navigate to your Desktop using change directory **cd**

`$ cd Desktop`

List the folders and files on your Desktop **ls**

`$ ls`

Create a project and corpora folder on your Desktop using make
directory **mkdir**

`$ mkdir project`

`$ mkdir corpora`

Move the corpora folder into the project folder using move **mv**

`$ mv corpora project`

Navigate to your corpora folder from your desktop using change
directory **cd**

`$ cd project/corpora`

Navigate up one directory **cd ..**

`$ cd ..`

Again

`$ cd ..`

You should now be in the Desktop directory. Move interviewfiles.zip file into the corpora folder using **mv** and a path

`$ mv interviewfiles.zip project/corpora`

Navigate back down to corpora using **cd** and a path

`$ cd project/corpora`

## Manipulation
By this point we’ve figured out how to find our breadcrumbs if we got lost (pwd), and how to figure out what’s around us (ls), how to move up and down levels (cd / cd .. ), how to create new folders, and how to move content into different folders. Now we are going to engage in a bit of basic manipulation of content within the dmics-texts.zip file you downloaded at the beginning of the workshop, currently residing in the corpora folder that you created in the previous section.

**Windows/Cygwin**: there is a package for unzipping, but it's not installed by default. It's easiest to just navigate to the folder in the GUI and unzip it ('Extract here').

**Mac** Unzip the interviewfiles.zip file in the corpora folder using **unzip**

`$ unzip interviewfiles.zip`

`$ ls`

```
__MACOSX
interviewfiles.zip
interview_0368
texts-header
```

You probably don't need that zip anymore get rid of it using remove **rm**

`$ rm interviewfiles.zip`

The folder \_\_MACOSX is an annoying add-in you get when you zip something on Mac OS X. Let's remove that.

`$ rm -r __MACOSX`      (that's two underscores)
>*the -r flag is recursive—since we're removing a folder, we want to remove the folder and everything in it*

`$ ls`

Result:

```
interview_0368
texts-header
```

### Tesseract Optical Character Recognition (OCR)
#### Description
Tesseract-OCR is an open source OCR (optical character recognition) engine, originally developed by Hewlett Packard Laboratories. The standard installation of Tesseract-OCR can convert images of text in 39 different languages to plain text data.  

#### Scenario
You visit an archive and need to capture images of text based archival collections for your research - ultimately you would like to convert these images into data that you can search, visualize, text mine, etc. Using a digital camera and/or a copier you capture photos of archival collections in the .tif / .tiff format. With these files in hand you are prepared to use Tesseract-OCR to convert your images into plain text files.

*Sometimes we get page images, but what we really need is plain text. Tesseract is free OCR software available in lots of languages that can generate text from images at a large scale.*

Navigate to the folder of tiffs and list the files
`$ cd interview_0368`

`$ ls`

Convert one tif file to one txt file using Tesseract OCR

----
**Mac Users**

`$ tesseract interview_0368-1.tif interview_0368-1`

(there may be an error here, but let's check out the text file to see what happened)

Using your GUI, compare the tif file to the txt file you generated

While we’re here, why don’t we just OCR all of them in one batch?

`$ for i in *.tif ; do tesseract $i $i; done`

If we want to put these all into a single file, we can do that

`$ cat *.txt > interview_0368.txt`

----
**Windows Users**

Find tesseract.exe (it’s probably in Program Files (x86)) and drag it
in. You can also try the path below and then hunt down the file if it
doesn’t work

`$ '/cygdrive/c/Users/YOURUSERNAME/AppData/Local/Tesseract-OCR/tesseract.exe' interview_0368-1.tiff interview_0368-1` [**be sure to add your username in the appropriate space**]

Using your GUI, compare the tif file to the txt files you generated

While we’re here, why don’t we just OCR all of them in one batch?

`$ for i in *.tif; do '/cygdrive/c/Users/YOURUSERNAME/AppData/Local/Tesseract-OCR/tesseract.exe' $i $i; done` [**be sure to add your username in the appropriate space**]

If we want to put these all into a single file, we can do that

`$ cat *.txt > interview_0368.txt`

## Further Resources

[*Sourcecaster*](https://datapraxis.github.io/sourcecaster/)

Library Carpentry. [Shell Lessons for Librarians](https://librarycarpentry.github.io/lc-shell/)

Idan Kamara, [*Explain Shell*](http://explainshell.com/)

Learn Code The Hard Way, [*Linux Bash Shell Cheat
Sheet*](http://cli.learncodethehardway.org/bash_cheat_sheet.pdf)

Learn Code the Hard Way, [*The
Setup*](http://cli.learncodethehardway.org/book/ex1.html)

Ian Milligan and James Baker, [*Introduction to the Bash Command
Line*](http://programminghistorian.org/lessons/intro-to-bash)
