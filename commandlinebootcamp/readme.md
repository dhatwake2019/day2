## Command Line Bootcamp

*Original slides and activity were developed by Thomas Padilla and have been lightly altered*

@@@@change the name of the folder and the url to download

### Introduction
**Before we start, download our [sample files](@@@update zip link) and put the .zip file on the Desktop. DO NOT UNZIP THE FILE!**

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

@@check to see if cygwin needs a special first command@@@

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

Navigate to your home directory using change directory **cd**

`$ cd`

@@@@ making a diagram for this would be awesome

Move interviewfiles.zip file into the corpora folder using **mv** and a path

`$ mv Desktop/interviewfiles.zip Desktop/project/corpora`

Navigate back down to corpora using **cd** and a path

`$ cd Desktop/project/corpora`

## Manipulation
@@@replace the filenames all over - search for dmics
By this point we’ve figured out how to find our breadcrumbs if we got lost (pwd), and how to figure out what’s around us (ls), how to move up and down levels (cd / cd .. ), how to create new folders, and how to move content into different folders. Now we are going to engage in a bit of basic manipulation of content within the dmics-texts.zip file you downloaded at the beginning of the workshop, currently residing in the corpora folder that you created in the previous section.

Unzip the interviewfiles.zip file in the corpora folder using **unzip**

`$ unzip interviewfiles.zip`

`$ ls`

Result: @@@update this

```
ActoEPoems.htm
AddiRPoetr.htm
AikiLEpist.htm
BailJColle.htm
BailJFamil.htm
LadyAOrigi.htm
__MACOSX
dmics-texts.zip
iriswmagic.htm
ladyaelija.htm
ladyavarie.htm
rdme.txt
sevenagesofwoman
```

You probably don't need that zip anymore get rid of it using remove **rm**

`$ rm dmics-texts.zip` @update

@@@make sure this is still here@@ The folder `__MACOSX` is an annoying add-in you get when you zip something on Mac OS X. Let's remove that.

`$ rm -r __MACOSX`
>*the -r flag is recursive—since we're removing a folder, we want to remove the folder and everything in it*

`$ ls`

Result: @update

```
ActoEPoems.htm
AddiRPoetr.htm
AikiLEpist.htm
BailJColle.htm
BailJFamil.htm
LadyAOrigi.htm
iriswmagic.htm
ladyaelija.htm
ladyavarie.htm
rdme.txt
sevenagesofwoman
```

### Tesseract Optical Character Recognition (OCR)
#### Description
Tesseract-OCR is an open source OCR (optical character recognition) engine, originally developed by Hewlett Packard Laboratories. The standard installation of Tesseract-OCR can convert images of text in 39 different languages to plain text data.  

#### Scenario
You visit an archive and need to capture images of text based archival collections for your research - ultimately you would like to convert these images into data that you can search, visualize, text mine, etc. Using a digital camera and/or a copier you capture photos of archival collections in the .tif / .tiff format. With these files in hand you are prepared to use Tesseract-OCR to convert your images into plain text files.

*Sometimes we get page images, but what we really need is plain text. Tesseract is free OCR software available in lots of languages that can generate text from images at a large scale.*

Navigate to the folder of tiffs and list the files
`$ cd interview_0662`

`$ ls`

Convert one tiff file to one txt file using Tesseract OCR

----
**Mac Users**

`$ tesseract interview_0662-0.tiff interview_0662-0`

Using your GUI, compare the tif file to the txt file you generated

While we’re here, why don’t we just OCR all of them in one batch?

`$ for i in *.tiff ; do tesseract $i $i; done;`

----
**Windows Users**

Find tesseract.exe (it’s probably in Program Files (x86)) and drag it
in. You can also try the path below and then hunt down the file if it
doesn’t work

`$ '/c/Program Files (x86)/Tesseract-OCR/tesseract.exe' interview_0662-0.tiff interview_0662-0`

Using your GUI, compare the tif file to the txt files you generated

While we’re here, why don’t we just OCR all of them in one batch?

`$ for %i in (*.tif) do '/c/Program Files
(x86)/Tesseract-OCR/tesseract.exe' %i %i`


