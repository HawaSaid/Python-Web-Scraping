# Web Scraping
The notion of web Scraping was introduced in this assignment. Two python libraries were used to do that: BeautifulSoup and requests.
The request library is used for sending HTTP requests and retrieving HTML content from websites. The Beautiful is used
to facilitate parsing and extraction of relevant information from HTML, simplifying web scraping tasks.

## Implementation
<u>A main menu is displayed when the program is first being executed.
5 options will appear:</u>
1. Display Latest Deals
2. Analyze Deals by Category
3. Find Top Stores
4. Log Deal Information
5. Exit

### Option 1
This option presents the most recent deals scraped from the designated website. 
Essential details such as store name, item description, voting counts, username, timestamp, category, replies, views, and URL link for each deal are displayed.

### Option 2
This option offers a detailed list of every category that is accessible, along with the amount of deals that fall into each area. 
### Option 3
Users are invited to enter the number of top stores they would want to see when they select this option. 
Based on the quantity of deals linked to each store, the top stores are being determined and displayed.
### Option 4
This option prompts the user to enter the number that corresponds to the category they have selected after displaying all of the available categories. 
The application then finds and logs every deal link in the chosen category to the file called "log.txt." 
