## Organizing Data

Written by Brandon T. Locke

### OpenRefine

[OpenRefine](http://openrefine.org/) (formerly known as GoogleRefine), is a very popular tool for working with unorganized, non-normalized (what some may call "messy") data. OpenRefine accepts TSV, CSV, XLS/XLSX, JSON, XML, RDF as XML, and Google Data formats, though others may be used with extensions. It works by opening into your default browser window, but all of the processing takes place on your machine and your data isn't uploaded anywhere.

**This tutorial will demonstrate some of the most popular and powerful features of OpenRefine, including geocoding using an API, algorithmic word normalization and correction, and working with multi-value cells.**

### Data
**You can [download a file of the NC life histories in this repo](@@@@).**

#### Life Histories Metadata (**nc-lh-meta.csv**)
Dataset comprising metadata records for WPA Life Histories that take place in North Carolina, assembled by Lauren Tilton and partially destroyed by Brandon Locke.

### Organizing Metadata

#### Loading the Dataset
1. Open OpenRefine. It should pop open a tab in your default web browser.
1. Click 'Open' in the top right to open a new OpenRefine tab
1. Click 'Browse' and locate the nc-lh-meta.csv on your hard drive. Then click 'Next.'
1. The Configure Parsing Options screen will ask you to confirm a few things. It has made guesses, based on the data, on the type of file, the character encoding and the character that separates columns. Take a look at the data in the top window and make sure everything looks like it's showing up correctly.
1. Name the project "nclifehist" and click 'Create Project' in the top right corner.

#### Evaluation
Take a minute to look around. Consider the structure of the data with principles of "tidy data" in mind. This will help guide what types of operations you perform on the data. Also take time to evaluate the type of information that is represented and what type of questions you might want to ask of it (e.g. Which publishers are most prominently represented in the collection?)

#### Working with Multi-Value Cells
This data has multiple people listed in the 'interviewer' and 'interviewee' columns, and in the 'gender_interviewee' and 'occupation' columns; in every case, there's a comma between values. For many purposes, this works great—it's the most compact and concise way to represent this information. But for many purposes, you may need to format this data differently. So, if you wanted to visualize your data, it wouldn't count `farmer, mechanic` as both a farmer and a mechanic, but a distinct separate entity. (Although sometimes that's what you want!) There are two ways you may want to handle this.

**Multiple Columns with One Value in Each**
1. Click on the small triangle next to 'interviewee' then click 'Edit Column' then 'Split into several columns'
2. You'll see a few options—for this you want to leave things as-is and separate on the commas. Click OK.
3. You now have 2 separate 'interviewee' columns, and each column is either empty or has one value.

We could do this for 'gender_interviewee' and 'occupation' columns, but we'll try a couple of other ways.

**Create TRUE/FALSE Columns Based on Values**
1. Select gender_interviewee > Edit column based on this column
2. In the GREL window, type `if(value.contains("female"), "true", "false")`
3. Call this column 'isFemale' and click OK.
4. Do this again for Male. gender_interviewee > Edit column based on this column. Take a look at the preview.
5. Uh-oh. It looks like using "male" would make everything true since the string 'male' also appears in 'female.' We'll need a slightly more complex regular expression to match.
6. Type `if(value.contains(/\bmale|\s+male/), "true", "false")` into the GREL window. name it 'isMale' and click OK.
> `\b` sigifies the start of a string, `|` means it will match either of the two patterns, `\s+` means there can be multiple white spaces before the string. This means it will match 'male' if it is either at the beginning of the cell, or if it comes after a space. We have to include both since there are some columns where that say "female, male".

**Dealing with categories where there are lots of different responses** 
What about Occupation? If we look at the distribution (occupation > Text > Text facet; then click 'count' to sort by count), We see that tenant farmer and farmer come up almost a quarter of the time (not including the times they come up in multiple entries), housewife and mill worker come up 8 times, and everything else is 4 or less. If we're interested in separating out some of the more popular ones, and doing further analysis, we may want to create isTenantFarmer, isFarmer, isHousewife, etc rows. We may want to split the separate occupations apart and create an occupation2 column. Or, if we're just going to refer to them occasionally to inform our reading, we can just leave them as-is. Let's do that!

> *Sometimes we may want to leave this together! In the case of interviewer, we may want to look at them as teams, rather than two different interviewers.*

#### Normalizing Controlled Vocabulary
If we scroll over to the 'race_interviewee' column, we can see that some of them are coded using full words ("black, white") while others are coded using letters ("b,w"). Let's run a quick check to see if there are more issues like this throughout the column, and correct any problems we see.
1. Click on the small triangle next to 'race_interviewee,' then click on 'Facet,' then 'Text facet.'
2. On the left, you'll see a list of all of the different values in the column, along with a count of how many times they appear. Let's change 'b' and 'w' so that they're fully written out.
3. Hover over the 'b' row—buttons should appear on the right.
4. Click 'Edit' and type out 'black.' Hit enter.
5. Note the yellow box at the top letting you know you've changed 7 rows.
6. Do the same for 'w'

#### Normalizing by Clustering
Each column has a facet function that allows you to quickly identify inconsistencies in your data by counting the number of unique occurrences for each piece of data in that column. 

Click the Interviewer column > Select Facet > Select Text Facet. Take a look at some of the inconsistencies

We could go through each of these and edit them, as we did for the race column, but that could take a long time. In OpenRefine, it's also possible to cluster and normalize variation across the dataset algorithmically. Clustering will look for patterns of variation without the need for you to (1) sleuth your way through the dataset looking for small variations (2) using facets or filters to eliminate them one at a time. Begin with the default method of 'key collision' using the 'fingerprint' function. Clustering reveals patterns of irregularity throughout the selected column of data. It is then possible to review clustering results and merge the data into the desired form. For more information on all of the available clustering methods and functions consult [OpenRefine documentation on Github](https://github.com/OpenRefine/OpenRefine/wiki/Clustering-In-Depth).

1. Click on the 'Cluster' button that's on the left side of the screen, just above the list of terms.
2. Review the proposed merges. Do they make sense?
3. Select a few suggestions that seem right and click 'Merge & Re-Cluster' to edit several of values at once.
4. There are several different algorithms here that can be used. On the left, you'll see a dropdown that says 'key collision.' Click on that, and select nearest neighbor.
5. Select the merges that make sense, and hit 'Merge Selected & Re-Cluster.'
6. Let's change the radius here to 8 and see if a wider lense would help.
7. Are all of these correct?

#### Working with dates
This dataset has the date information split out into three separate columns—year, month, and day. This is good for some purposes, but oftentimes, it's helpful to have all info in one column—either to sort things or because a tool you're using wants [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601). Let's combine those columns together to make a single YYYY-MM-DD column.

1. year_interview > Edit column > Add column based on this column...
2. In the GREL box, type `cells["year_interview"].value + "-" + cells["month_interview"].value + "-" + cells["day_interview"].value`. You may notice that this doesn't add leading zeroes (e.g. it should say '1939-**03**-29' instead of '1939-**3**-29'), but we'll take care of that in a moment.
3. Call the column 'fullDate' and click ok.
4. Click 'date_new' > Edit cells > Common transforms > To date

#### Creating a new filename
In a later session, we'll rename these text files so that we can use them a little more easily. Right now, the only information that's in the name is the interview number, which we can use to connect with all of this other metadata. But it would be easier for us to search, select, or sort the files if we had this information right there in the filename. 

For our purposes, lets name the file according to the following convention: *date_interviewer_interviewnumber.txt*

While we don't absolutely have to create a filename in OpenRefine (we could just rename files according to the metadata fields we want), we're doing it here for two reasons.
1) When we rename the files, it'll be good to have that updated name in the spreadsheet!
2) It's easier this way.

Also, be sure that the first column is the old filename and the second column is the new filename. This will help us later on when we rename them!

So let's get started on combining these metadata fields.
1. file_name > Edit column > Add column based on this column...
2. In the GREL window, paste `substring(cells["fullDate"].value,0,10).replace("-","") + "_" + replaceChars(cells["interviewer"].value,'., ',"") + "_" + value.replace("interview_","")` this takes the date column, pulls just the first 10 characters (yyy-mm-dd), and replaces the `-` with nothing
* `replaceChars(cells["interviewer"].value,'., ',"")` this takes the information from the interviewer column and replaces all periods, commas, and spaces with nothing
* `value.replace("interview_","")` this takes the filename column and replaces 'interview_' with nothing so that only the number remains
5. Name this column new_filename and hit ok

#### Geocoding
*[Geocod.io](https://geocod.io/) may also be a good option*

*If you're doing this for your own project, you'll need to get a MapQuest API Key from the [MapQuest Developer Site](https://developer.mapquest.com/) - click the 'Get your Free API Key' button on the front page and fill out the information. For this workshop, I'm making a key available, and will cancel the key after our session*

*We'll also just do a few rows, since this can take awhile*
@@@@find/create a key for this@@
- Let's limit our work to just geocoding cities in Sampson County. Click County > Filter, and then type in Sampson. This should just show the 6 rows from Sampson County.
- Then click **City** > Edit Column > Add Column by Fetching URLs... and enter this expression: `'http://open.mapquestapi.com/nominatim/v1/search.php?' + 'key=YOURKEY&' + 'format=json&' + 'q=' + escape(value, 'url') + '+north+carolina'` **Note: Be sure to add your own API key in the above expression where it says `key=`**
- Name the column 'geocodingResponse' and click OK. This will take quite some time to finish.
- The new 'geocodingResponse' column won't be very clear or useful - it will be the full JSON response with all of the information Google has about that location.
- Click geocodingResponse > Edit Column > Add Column based on this column
- Enter `value.parseJson()[0].lat + ', ' + value.parseJson()[0].lon` and call the new column 'latlng.' Hit OK. This will parse the JSON and correctly format the latitute and longitude in the new column.
- You should see that the resulting column has the latitude and longitude for the city name.
- You can delete the 'geocodingResponse' column (Edit Column > Remove This Column) after you have already extracted the lat/lng coordinates.
- Some software (including the software we'll be using) will want latitude and longitude separately. Click latlng Column > Split into several columns... and then split by the substring ",". Rename accordingly.

#### Saving and Exporting
In the top right corner, you can click on 'Export' and save the data in a number of different formats, including csv and HTML tables. Let's export this as `nc_lifehist_metadata.csv`.

You may also want to export the entire project. This is useful if you want to share the project with others, or if you want to continue working on a different machine. It's also useful for transparency and documentation, as every change you've made is documented (and reversible).

## Additional OpenRefine Resources
- [OpenRefine Wiki](https://github.com/OpenRefine/OpenRefine/wiki)
- [OpenRefine Recipes](https://github.com/OpenRefine/OpenRefine/wiki/Recipes)
- [Cleaning Data with OpenRefine](https://libjohn.github.io/openrefine/)
- [Fetching and Parsing Data from the Web with OpenRefine](https://programminghistorian.org/lessons/fetch-and-parse-data-with-openrefine)
