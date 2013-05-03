Hymnal Parser
============
The code in this project is aimed at parsing hymns from [http://hymnal.net](http://hymnal.net), as part of a larger project to make an Android app that serves hymns to a client phone using my own server as a backend.

About the Website
------------
Understanding the structure of the website helps in using the parser.
There are four types of hymns: Hymns ('h'), New Songs ('ns'), Children's Songs ('c'), and Long Beach Songs ('lb). 
Each song type inherits the format http://www.hymnal.net/hymn.php/[type]/[number], and the parser uses these two parameters as input for the songs to download.

Usage
------------
- Make sure that there is a 'hymns' folder in the working directory, which should also contain the files in this project
- Edit the constants in run.py so that the correct hymn type and numbers are downloaded
- Run run.py in a terminal or console
- Wait for your files to be processed, and voila! JSON songs, all in the hymns folder
- Suggestion: after downloading hymns of one type, put them into separate folders denoting their type (e.g. 'ns'), since the parser simply names them 'hymn1.txt', etc.

Note: The website structure for which this code was originally aimed has changed, and the code no longer works, but the filters for the correct song tag data can easily be modified.
Furthermore, commercial use of the results of this script is inadvisable due to the copyrights on the hymn lyrics.
