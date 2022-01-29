# tabScraper
Program to input old apple music scrobbles into lastFM 

Dependencies : (will make more in depth later) 

- Chrome >=v97 
- Chrome Webdriver
- Python > 3.9
- pip3
- Selenium (pip3 install selenium)

Just download the dependencies and run the script. You're going to need the .json file
called Apple Music Library Tracks.json (you can get it from https://privacy.apple.com/). 
Detailed instructions can be found here : https://smartphones.gadgethacks.com/how-to/download-your-2018-apple-music-listening-history-just-like-spotify-0191681/. 

The script can cleanly stop and resume halfway through. For now, just do a keyboard 
interrupt when running it from the terminal (ctrl/command c) and wait for the program 
to close (it takes a second). 
