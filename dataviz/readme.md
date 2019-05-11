## Data Visualization with Flourish

**Please be sure to have a free account on [Flourish](http://flourish.studio) and either have the exported data from the OpenRefine tutorial, or use [this fully geocoded dataset](https://raw.githubusercontent.com/dhatwake2019/day2/master/dataviz/nc-lifehist-metadata.csv).**

### Introduction
Flourish is a new, freemium, web-based data visualization platform. It's fairly similar to Tableau, if you've heard of that, but it doesn't require downloading any software, and it's a bit easier to figure out (in my opinion, anyway). Because we're using the free version, all data and visualizations will be publicly available, but *most* of the valuable parts of the service will still be available.

Go to [Flourish.studio](http://flourish.studio) and log in.

#### Hierarchy (Tree Map) Chart
Let's say we're interested in the demographic breakdown of the people interviewed by:

1. Click 'New' under Visualizations
2. Scroll down and click on 'Hierarchy'
3. Click on the Data tab at the top and then 'Import your data' (or drag your file in)
4. On the right, it will ask what columns you want to visualize. Let's try Interviewer, Race_interviewee, Gender_interviewee and remove the letter in 'Size by'. Now click on 'Preview' in the top.
5. Take a moment to see what's being visualized here. Try selecting different Layouts—in addition to Treemap, there's also Circles, Sunburst, and Bar.
6. Notice that gender isn't shown—try playing with the 'Visible levels' and seeing if that helps.
7. Take a moment to look through the different features in the pop-out menu to style your visualization.
7. Give it a name on the top left—maybe 'NC-interviewerdemos'
8. When you're happy with it, click on 'Export & Publish' in the top right—you can publish this and embed or link to it, or download it as a PNG, JPG, or SVG in your preferred size.

#### Alluvial Chart
Let's say we want to see if the interviewers had a particular territory, or if multiple interviewers went in and out of the same cities:

1. Click 'New' under Visualizations
2. Scroll down and click on the 'Sankey Diagram - Default' options
3. Click on the Data tab at the top and then 'Import your data' (or drag your file in)
4. On the right, it will ask what columns you want to visualize. Let's try Interviewer in 'Source' and City in 'Target.' Be sure to delete the next input, since we don't have an integer we want to measure.
5. It looks like there are very few times where a city had more than one interviwer. Let's try County to see if that holds up.
6. Give this one a name—maybe 'Sankey-location' and click on the back arrow to return to the homepage.

#### Map
What if we wanted to create a map of the interview locations and see how they're distributed over the state?

1. Click 'New' under Visualizations
2. Scroll down and click on the 'Projection Maps > US (States)' option.
4. On the right, it will ask what columns you want to visualize. You may notice that this map is colored by states, and it also has points plotted on it. This data is in two separate sheets—Regions and Points. We don't want to color in the states, we just want the lines there to help us make sense of the map. On the right, make the 'Value' field empty.
5. Click on the 'Points' tab, and then 'Import your data' (or drag your file in)
6. Scroll Down to the Points portion. For Name, put in the City column, put in the lat and lon columns, and then click Preview.
7. Name this 'map-allinterviews'

#### Create a Story
Stories are a way to contextualize and share multiple interactive visualizations. [It is essentially a web-hosted slideshow that can include the visualizations you've created.]

1. Click 'New' under stories
2. Follow the instructions to add one of the vizualiations you've created.
3. Add a few more, including a basic slide or two.
4. When you're done, click 'Export & Publish' in the top right, just like the other visualizations.
