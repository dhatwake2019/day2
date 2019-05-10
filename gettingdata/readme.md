## Getting Data

During this session you will be introduced to a variety of methods to
get data from collections, documents, and the web.

### Tools and Platforms

-   [*Web Scraper*](https://webscraper.io/)
-   *cURL*
-   [*Postman*](https://www.getpostman.com/)
-   [*Library of Congress's Chronicling America API*](https://chroniclingamerica.loc.gov/about/api/)
-	A [Python Script for processing Chronicling America API results](https://raw.githubusercontent.com/dhatwake2019/day2/master/gettingdata/chronam.py)

### Data

-   [*Digital Public Library of America*](https://dp.la/search?q=%22wake+forest+College%22&after=1933&before=1939&type=%22image%22)
-	[Chronicling America](https://chroniclingamerica.loc.gov/)

## Scraping a Website

### Tool: [webscraper.io](http://webscraper.io)

#### Description

A freemium web scraping Chrome plugin.

#### Why you might need it

You want to scrape tabular data from the web, output to CSV format, and
don’t want to mess with BeautifulSoup.

#### Scenario

You want to capture metadata for some postcards and a map of Wake Forest College in Wake Forest, NC.

#### Activity

Use Web Scraper to extract data in CSV format from the following source or
one of your own:

-   DPLA Search Results [https://dp.la/search?q=%22wake+forest+College%22&after=1933&before=1939&type=%22image%22](https://dp.la/search?q=%22wake+forest+College%22&after=1933&before=1939&type=%22image%22)

#### Directions

1.  Navigate to [https://dp.la/search?q=%22wake+forest+College%22&after=1933&before=1939&type=%22image%22](https://dp.la/search?q=%22wake+forest+College%22&after=1933&before=1939&type=%22image%22) in a Chrome browser
2.  Open Web Scraper— either hit Cmd+Opt+I on Mac or click on the three dots in the upper right corner, then hover over ‘More Tools,’ then select ‘Developer Tools’
3.  Select the ‘Web Scraper’ tab on the window that pops up—you may need to scroll to the right to access it.
4.  Click on the ‘create new sitemap’ button and name this ‘dplawake’ Paste in the URL ([https://dp.la/search?q=%22wake+forest+College%22&after=1933&before=1939&type=%22image%22](https://dp.la/search?q=%22wake+forest+College%22&after=1933&before=1939&type=%22image%22)) under ‘Start URL’ and then click ‘Create Sitemap.’
5.  Click on the blue button near the bottom that says ‘Add New Selector.’
6.  We want to do this in steps—first we want to identify each individual item on the page. This will essentially give us a list of URLs for items that we can then go and get metadata from. 
7.  Click on ‘Select’ and then hover over the first item until there’s a green box around just the title. Click to turn the box green and then select the next title. Once you click, it should turn all of the titles red.
8.  Click on the blue ‘Done selecting!’ button. it should say `.hover-underline a`. If it doesn't, try again. Set the selectorId to 'getlinks,' set Type to 'Link,' check the ‘Multiple’ box. Confirm the Parent Selector is `_root` and then click ‘Save selector’ at the bottom.
9.  Click on one of the items to go to the item page. This should show you a table with information about the selector you just created. Double-click on that table row so that you can make child selectors. There shouldn't be any selectors listed now. Each of these will now operate on every ‘item’ selector that you created.
10. Click on ‘Add new selector,’ and name it ‘title.’ Click the ‘select’ button and click on the title of the first item—the whole box should be highlighted yellow. Once you’ve clicked the first title to highlight it red, and click ‘Done selecting!’
11. Scroll down to set the Parent Selector as 'getlinks'. Click ‘Save selector.’ [Note: We’re not selecting multiple here because this is operating on each individual item, not the whole page at once.]
11. Repeat this process for the ‘Publisher,’
12. We're going to do something similar for the URL, with a slight tweak. give it the id ‘URL’, select type 'Link,' click 'Select' and then click on it. It will very annoyingly put you into a new tab, but if you close it out and return to the WebScraper tab, it will be appropriately selected. Just scroll to the bottom, make the Parent 'getlinks,' and click save.
13. Now that you have all of the information you’d like selected, we can run a quick check to see if it’s scraping everything correctly. Scroll to the top of the Web Scraper screen and click on ‘Sitemap dplawake,’ then click ‘scrape.’ This will ask us to approve the delay and interval (to be nice to the server), and we can click ‘Start scraping.’ This will pop open and then eventually close a new window. Click ‘Refresh’ to view the data we’ve scraped.
14. There are a few columns that we don’t really need (and can easily delete later), but this should include all of the information we want.  ‘Sitemap dplawake’ and click on ‘Export data as CSV.’ 

### LC’s Chronicling America API

####Description
An API (application programming interface) is a defined set of methods for communicating with a software system. Each database has its own system, so looking at the codex and documentation for each is necessary. APIs can be public or private, though even public ones usually require a key to make sure the service isn’t being absed. Most API’s require that you get a key to access the API—this allows them to shut down abusive use. We’ll just hope that our calls won’t get our IP banned :). Library of Congress has multiple APIs—they have some documentation on the Chronicling America API and a nice tutorial on working with the API through Python in Jupyter Notebooks.

#### Why you might need it
It can be used for bulk downloading of text from Chronicling America or, with a few simple modifications, many other repositories or platforms.

#### Scenario
You want to study the newspaper coverage of North Carolina tenant farmers during the depression. 

#### Activity
Use Postman and the ChronAm API to extract OCR text from the newspapers.
*You don't have to create a Postman account—you can click the link at the bottom to skip!*

#### Directions
Make sure you’ve downloaded Postman from [https://www.getpostman.com/](https://www.getpostman.com/)

Create a folder on your Desktop called ‘ChronAm’

First, let’s check out the advanced search web interface for the newspapers. [https://chroniclingamerica.loc.gov/#tab=tab_advanced_search](https://chroniclingamerica.loc.gov/#tab=tab_advanced_search)

Let’s search for the words “labor” or “union” in the newspaper while Ford owned it:
* In ‘State’ select North Carolina
* In ‘Select Year(s)’, put in 1938-1939
* In the search, we’ll try “...with the words…” and put in “tenant farmer” and leave the number at 5
* Click Search
This should bring up 31 results that include both "tenant" and "farmer" within 5 words in the results.

Let’s take a quick look at the URL for the results page - it shows us exactly what’s going on if we know what to look for::
[https://chroniclingamerica.loc.gov/search/pages/results/?state=North+Carolina&lccn=&dateFilterType=yearRange&date1=1938&date2=1939&language=&ortext=&andtext=&phrasetext=&proxtext=tenant+farmer&proxdistance=5&rows=20&searchType=advanced](https://chroniclingamerica.loc.gov/search/pages/results/?state=North+Carolina&lccn=&dateFilterType=yearRange&date1=1938&date2=1939&language=&ortext=&andtext=&phrasetext=&proxtext=tenant+farmer&proxdistance=5&rows=20&searchType=advanced)

We’ll break this down:
**https://chroniclingamerica.loc.gov/search/pages/results/** - this is the main search results site for the project - there aren’t any fields specified, so it will bring up all 13.5 million results if we were to go to that address
**?** - this signifies that a query is coming-everything after this is the search material
**state=North+Carolina** - there are sets of keys and values; the first word tells us what field we’re searching and the second tells us what information we’re looking for. This is searching for papers in the state of North Carolina
**&** - this appends another pair of keys and values; we’ll see it used a bunch here in the URL
**dateFilterType=yearRange&date1=1938&date2=1939** - this shows that the filter is years (not month/date/year) and searches for things between 1938 (date1) & 1939 (date2)
**language=&ortext=&andtext=&phrasetext=** - for some reason, LC leaves in all the blank fields; we left language, ‘any word,’ 'all words,' and 'phrase' blank
**proxtext=tenant+farmer&proxdistance=5** - this is the proximity field that we entered - it’s looking for only papers with both words within 5 words of each other
**rows=20&searchType=advanced** - this is just showing the first 20 results, and the search was conducted via advanced search

If we’d like, we can make a cleaner URL without the blank fields. If you were to paste that into a browser, you’d see the same results.
https://chroniclingamerica.loc.gov/search/pages/results/?state=North+Carolina&dateFilterType=yearRange&date1=1938&date2=1939&proxtext=tenant+farmer&proxdistance=5

So, let’s investigate what’s here. Click on the first result.

We can see that ChronAm has things broken down into pages—not individual articles. So we may get some false positives (though, since we're using proximity text, it's extremely unlikely that the words would appear within 5 words of each other in different articles). We may also run into cases where an article continues on another page and we’re not seeing the whole thing. And if we’re analyzing the text, we’ll have some text included that’s not necessarily a part of the article we’re interested in. This is something to keep in mind as we’re looking at results.

You’ll also notice that in the top right corner of the paper viewer, there are options to view text, pdf, and jp2 (images). Click on ‘text’ and see what we get. You can see here that the OCR is...imperfect. You can also see that it has correctly followed the columns, so everything is (basically) in the correct reading order. If you were to manually collect the text you wanted, you could click on each result, click on ‘text’ on the viewer, scroll to the bottom and click on the ‘txt’ link to get a cleaner version of the text, and then save the file. That’s a lot of clicks. Thankfully, all of these text files are readily available via the API.

Ok, so why are we obsessed with the URL just a few minutes ago? Well, the API works in exactly the same way.

### Postman

Postman is a simple interface to develop and evaluate API requests, which take the form of long URLs with query information in them. Postman is not at all required for API access—you can also access data using cURL or wget on the command line, or through any web browser—it’s just a nice way to build calls and see results.

Open Postman and select ‘Requests’

It will ask you to name the request - call it ChronAm

Below, it will ask you to select a place to save things. Click ‘+ Create Collection,’ type ChronAm, then click on the checkmark on the right. Then click on ‘Save to ChronAm’ on the bottom.

This should bring you to a new screen with a space to develop a request URL and a space to see the response.

With Postman, you can enter the base URL and then add keys and values to see what kinds of responses you can get. We can just do a shortcut and paste our already-developed URL into the ‘Enter Request URL’ space: https://chroniclingamerica.loc.gov/search/pages/results/?state=North+Carolina&dateFilterType=yearRange&date1=1929&date2=1939&proxtext=tenant+farmer&proxdistance=5

Look at the ‘Query Params’ on the bottom, and you’ll see that it has broken down the request to show the sets of keys and values. **Click ‘Send’ and see what happens.**

We just got an HTML page back. All it’s doing is showing us the HTML of the page we were just looking at. We need to add a different key/value to make it more useful for us:
Key: format	value: json

Click send.

Now we have a result that is a bit intimidating but...seems to make a little more sense.

At the top, we have 
{
	"totalItems": 31,
	"endIndex": 20,
	"startIndex": 1,
	"itemsPerPage": 20,
	"items": [

This tells us that 31 pages matched our search and that it’s giving us results 1-20.

Scroll down a bit and you’ll see all kinds of metadata for the paper and the specific page that we’re looking at. Take note of the ‘ocr_eng’ field, which has all of the text for the page. (The ‘\n’ marks are new line markers—it makes it hard to read here, but we don’t really need to worry about them.)

It’s nice that we are limited to 20 responses and the results came quickly but, it would be nice to have all of the pages in a single file. Enter a new key/value:
Key: rows	Value: 31

Hit send. This may take a minute to load. (Note: I found this convention by going back to the URL and seeing the key/value ‘rows=20’. One would logically assume that the convention would be ‘itemsPerPage’ instead of ‘rows’, but it’s not.)

Once the results have come back, you should see that there are 31 results. Click on the two boxes icon on the right just above the result. This will copy the results to your clipboard. Open SublimeText and paste the results there. Click ‘save as’ and call it ‘nc-tenantfarmer.json’ and save it in the Desktop/chronam folder. [If something’s gone wrong, this file is available in our drive.](https://raw.githubusercontent.com/dhatwake2019/day2/master/gettingdata/nc-tenantfarmer.json)

So, we now have everything in one json file, but we can’t really analyze it very well. We’ll want to split it out into individual files based on each page. We can do that if we download this [fairly short Python script](https://raw.githubusercontent.com/dhatwake2019/day2/master/gettingdata/chronam.py) (right click on an empty part of the page, click save as, and put it in the Desktop/chronam folder - make sure it’s called ‘chronam.py).

On Windows: Open the chronam folder in Windows Explorer and double-click on ‘chronam.py’  @@test this on windows@@
-------
On Macs:
Open Terminal
$ cd Desktop/chronam
$ python chronam.py
------

Now, using Windows Explorer/Finder, open up the Desktop/chronam folder and see what’s there.


**Further Resources**

- Brandon Locke, [Downloading America](https://github.com/brandontlocke/downloadingamerica)
- Ian Milligan, [*Automated Downloading with
Wget*](http://programminghistorian.org/lessons/automated-downloading-with-wget)
- Free Software Foundation, [*Wget
Manual*](http://www.gnu.org/software/wget/manual/wget.html)
- Digital Public Library of America, [*API
Codex*](http://dp.la/info/developers/codex/) & [*DPLAFest 2015 Hackathon
Slides*](https://docs.google.com/presentation/d/1kVgyegobaJzDeJXKq3hn6_yW031xyCkA3xx60VqjlW4/edit#slide=id.p)
