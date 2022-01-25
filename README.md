### OutreachBot
Outreach is an essential part of many businesses, and often times companies have dedicated employees for this job. This bot was created in order to optimize outreach tasks, potentially saving hours of work. The bot takes a list of links to company webpages, scrapes them for their facebook page and then extracts their contact email.

### How to use
Using this tools involves three basic components: the input folder, the code (OutreachBot.py), and the output folder, which can all be found on the folder named "Bot" on the OutreachBot repository.
The first step is adding a csv file containing the links to company webpages that you want to use. This csv file should only contain a column of links and any header, note that this header is obligatory. Keep in mind that only one file should be in the Input folder, if there is more than one, the bot may take an undesired file as input.
The next step is to run the code in the OutreachBot.py file, either directly from console or using a code editor. Additionally, the repo also includes an "OutreachBot.ipynb" file, in case the user prefers using JupyterNotebook or JupyterLab.
After performing this step, a new csv file will appear on the "Output" folder. This file will now contain the original list of company webpages, as well as one new column conatining the Facebook link, if found. If no Facebook link is present in their webpage, that field will simply be empty.
![Output_image](https://user-images.githubusercontent.com/90937404/151074113-213a7e9e-eb17-43ab-9752-682236bb483f.png)
### Code Breakdown

The code for this tool leans mainly on the libraries: requests, pandas and selenium. This breakdown will mostly detail how the main functions of the code are constructed, as they are 90% of its functionality.
First, we have the "excract_fbs" function, which takes a list of urls as its only argument. This function first creates an empty list were the Facebook links will be stored. It then defines a css selector for the element that contains an "href" attribute with the desired link (facebook.com/). We can see that it excludes a link that contains the word "sharer", as many webpages contain an automatic sharer that redirects to a Facebook url that isn't of interest.
Next it cycles through the urls provided with a "for" loop, this loop contains several nested "try" and "except" blocks. In the first the requests library is used to try and retreive the desired information, however, if no links are processed, it raises an exception so it moves on to try and retreive it using the more sophisticated (and time consuming) selenium. Within these selenium blocks a new function is called which simply creates an instance of a Google Chrome window, without showing it, and it waits until the presence of an element with the css selector chosen. If after 4 seconds no element of the sort is located, it closes the driver and tries again. This was constructed as such to circumvent loading errors such as momentary connection issues. If at any point the desired element is located, is appends it to our eventual output list and continues the loop, otherwise it appens an empty string and moves on.

Next, the "get_contact_from_fb_page" function is almost exactly alike, some key differences include: no initual try with requests, as we can expect the facebook page to have to load for a bit, a different css selector, and a new argument added to the initial driver's creation. This argument points to a folder named "User_Data", which conatins the credentials for a facebook user so it is automatically signed in upon entering facebook.com. The function "OutreachBot" brings it all together and outputs a pandas dataframe conatining all relevant information. 

Finally, a bit of code containing input and output reading and creating respectively is necessary.

### Personal Note
This project was very entertaining to make, although not without its obstacles. The main one being the process needed to scrap Facebook pages, which for this specific piece of information requires being signed in to a Facebook account to carry out. Unfortunately, Facebook prohibits scraping of any kind in its Robots.txt file, so this project may very well be best shortened to just the first section which scrapes individual company webpages. It is definitely important to keep in mind what is allowed and isn't when developing a tool of this nature. 



