# tabScraper
Program to input old apple music scrobbles into lastFM 

NOTE: As of 4/5/22, this is still under development.

NOTE 2: As of now, this is still a SCRIPT, not a proper application. As such, downloading and running it is a little messy and requires about 10 minutes. I hope the instructions below make sense, but if they don't, please reach out to me at virginkargarv@gmail.com

Dependencies : (will make more in depth later) 

- Chrome >=v97 
- Chrome Webdriver
- Python > 3.9
- pip3
- Selenium (pip3 install selenium)

Installation/Running Instructions: (I'm hoping to make this WAY shorter soon)
1. Download the project using git clone.
2. Move your Apple Music json file into the project folder.
3. Download the chromedriver if you have not already. You can download it from https://chromedriver.chromium.org/downloads. You'll probably be using chrome version 97. Also download chrome if you don't have it.
4. Download python if you don't have it. You can download it from https://www.python.org/downloads/.
5. ONLY IF YOU GET A PIP-RELATED ERROR: Download pip from https://pip.pypa.io/en/stable/installation/
6. Install selenium. To do this, open a terminal and run "pip3 install selenium".
7. Enter the chromedriver path into the program. To do this, open scrobbler.py with any text editor. Inside the quotes on line 13, paste the path to your chromedriver. You can do this by right clicking on your chrome driver file and hitting either "get location" or "get address as text".
8. Enter your lastFM login info on lines 71 and 74 inside the quotes. Enter these exactly as they are on your lastFM account.
9. Run the program. To do this, navigate to the project folder and run the python file. You can do this from terminal by navigating to the python file, right clicking, and hitting open/run in terminal/command prompt.
10. To close the program, hit ctrl+c or command+c. Wait for the program to fully close so it can properly resume again. This should take < 20 seconds.

Just download the dependencies and run the script. You're going to need the .json file
called Apple Music Library Tracks.json (you can get it from https://privacy.apple.com/). 
Detailed instructions can be found here : https://smartphones.gadgethacks.com/how-to/download-your-2018-apple-music-listening-history-just-like-spotify-0191681/. 

The script can cleanly stop and resume halfway through. For now, just do a keyboard 
interrupt when running it from the terminal (ctrl/command c) and wait for the program 
to close (it takes a second). 
