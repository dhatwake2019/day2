## Refining Unstructured Text

### Tools
Terminal/Cygwin [Bash command line tools]
-	egrep
-	sed

### Data
Text of around 300 WPA Life Histories that take place in North Carolina, assembled by Lauren Tilton. OCR is fairly high quality, and some faux running headers were added by Brandon Locke. 

We'll be using the same data as we did for the [Command Line Bootcamp](https://github.com/dhatwake2019/day2/raw/master/commandlinebootcamp/interviewfiles.zip).

## Command Line File Editing

Open up Terminal/Gitbash and navigate to the 'Corpora' folder: `Desktop/project/corpora`

### Renaming text files based on metadata
Remember how we used OpenRefine to come up with new, descriptive filenames? Well now, using a couple of command line tools, we can rename (or, technically, *move*) files according to our spreadsheet. **Drag your exported CSV into the corpora folder (or quickly download our version by pasting `$ curl @@@where it's going to live on github@@`)** @@@ this finished version will be posted in the data viz folder and linked here@@

@@update this to have the filename that's recommended
**Mac users**: 
`$ sed -i -e '$'\n'' test.csv | cat test.csv | while IFS=, read -r orig new trash; do mv "$orig".txt "$new".txt; done`

**Windows users**: 
`$ sed -i -e '$a\' test.csv | cat test.csv | while IFS=, read -r orig new trash; do mv "$orig" "$new"; done`

This command is really long and a bit confusing, so we'll break it down. 
`sed -i -e '$'\n'' test.csv ` - @@rename This is a bit of a weird workaround. The way we'll be going through the csv will only operate on lines with a line return on the end. It wouldn't be all that strange for a csv to end without one, so we run the risk of missing the final row. `sed` ("stream editor") is a text manipulation tool, `-i` means it's edited in place (as opposed to making a backup), `$` jumps to the end of the file, `'\n'` adds the character for the line return, and `test.csv` identifies the file all of this will be performed on.

`cat test.csv |` - `cat` stands for concatenate, but it's often used to just pass some data into another tool; in this case, we're taking the file, now with a line return, and feeding it into the next command.

`while IFS=, read -r orig new trash;` - this is starting a loop that will go through every row and perform a specific task ('while' meaning 'while there are more lines'), IFS (internal file structure) & read are a way of processing structured data and assigning variables, and the `orig new trash` section is the set of variables we're creating. Since we've put out three variables, it will take the first chunk (everything until a comma) and assign it to the first variable (orig), take the next chunk (between the first and second comma) and assign it to the second variable (new), and then assign all of the rest to the third and final variable (trash). If we wanted to, we could create a variable for every one of the columns and construct a filename from each piece, but it's easier to just shove everything into a third variable (trash) and just not use it.

`do mv "$orig".txt "$new".txt; done` uses 'mv' to search for the string in our first column (with .txt added to the end), and when (or if) it's found, rename it to the string in our second column (with .txt added to the end).

----

### EGREP and Regular Expressions

#### Searching & Mining

Move back to the BWRP books

`$ cd ..`

Display the first and last ten lines of a text using **head** / **tail**

`$ head ActoEPoems.htm`

`$ tail ActoEPoems.htm`

Find out how many lines and words there are in a text of your choosing using **wc -l -w**

`$ wc -l -w bwrp_ActoEPoems.txt`

Results:

```
1607 15242 bwrp_ActoEPoems.txt
```
>1607 lines and 15,242 words

Do some very basic searching with egrep — this will print the entire line it's mentioned in

`$ egrep farm *txt`

Do some very basic counting with **egrep -c**
`$ egrep -c farm *txt`

`$ egrep -c farmer *txt`

Count only whole words using **egrep -cw**

`$ egrep -cw farm *txt`

The possibilities for regular expressions are endless (and sometimes difficult and always ugly), but you can also find matching patterns.

What 18th and 19th century years (or very similar four character numbers) are mentioned in these texts?
`$ egrep -o '\b1[8-9][0-9][0-9]\b' *txt`
> the -o flag returns just the text that matches the pattern
this looks for four numbers in a row that start with a 17 or 18—the rest can be any numbers

It's possible that some of these aren't years. They could be page numbers or amounts or anything else. Let's do a search that includes some context, but not the entire line.

`$ egrep -o '.{0,50}\b1[8-9][0-9][0-9]\b.{0,50}' *txt`

This context feature is interesting. What if we wanted to look at the words around 'farm' to see what people are saying without getting every full line?

`$ egrep -o '.{0,50}farm.{0,50}' *txt`

We could even move this into a separate corpus if we wanted by adding `> farmcontext.text` to that search.

#### Removing repeated patterns in our text
One other way that regular expressions can be really helpful is in removing a lot of repeated junk from files. If you open up the text files, you'll see some (faux) running headers that appear consistantly throughout the text. You can often see things like this pop up in digitized published works. In this case, we have lines that either say:
`NORTH CAROLINA WRITERS PROJECT      1` or 
`NORTH CAROLINA WRITERS PROJECT         2`

So we know that we're looking for a full line in the text file that starts with `NORTH CAROLINA WRITERS PROJECT`, then has some number of spaces (it varies), and then a number (in our case, we know it's one digit (and only either 1 or 2)), but lets just say that the page number is between 1 and 4 numbers.

Here's one possible regular expression to match these running headers. `NORTH CAROLINA WRITERS PROJECT\s+[0-9]+`

`NORTH CAROLINA WRITERS PROJECT` is pretty self explanatory

`\s` matches on any whitespace (spaces, line returns, tabs)

`+` means that the whitespace may repeat....in other words, it will match on a single space or 40 consecutive spaces, so long as they're consecutive

`[0-9]+` matches on any number, and the + means it can be many consecutive numbers

If we look back at our previous exercises, we could probably guess that `egrep -o 'NORTH CAROLINA WRITERS PROJECT\s+[0-9]+' *.txt` would print out every line that matches....but how to we remove that line and leave everything else behind?

`$ sed -E -i 's/NORTH CAROLINA WRITERS PROJECT[[:space:]]+[0-9]+//g' *.txt` *note that the space character changes from a `\s` to a `[[:space:]]`. The former will work for some machines, but not others*

Now let's check our work by using that egrep command again:

`$ egrep -o 'NORTH CAROLINA WRITERS PROJECT\s+[0-9]+' *.txt`


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
