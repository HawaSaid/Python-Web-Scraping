import os
import requests
from bs4 import BeautifulSoup

class Scraper:
    def get_store(self,listing):
        """
        Extracts the store name from the given listing.
        Parameters:
        - listing (BeautifulSoup): The BeautifulSoup object representing a deal listing.
        Returns:
        - str: The extracted store name.
        """
        #Select store elements based on their classes
        store_element_retailer = listing.select_one('.topictitle_retailer')
        store_element = listing.select_one('.topictitle')

        #Check if store element is present and then extract the store name
        if store_element_retailer:
            return store_element_retailer.text.strip()
        elif store_element:
            # Extract store from the square brackets, if available
            store_text = store_element.text.strip()
            return store_text.split(']')[0][1:].strip() if ']' in store_text else store_text
        else:
            return "N/A"
        
    def LatestDeals(self): 
        """
        Method to get the latest deals of the page.

        Returns:
        None
        """
        url = "https://forums.redflagdeals.com/" #Page to Scrape
        response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/")
        response.raise_for_status() #Exception raised if request fails
        soup = BeautifulSoup(response.content, "html.parser")
        deal_count = len(soup.find_all("li", class_="row topic")) # Get the number of deals of page

        print(f"Number of deals available: {deal_count}")
        print("")

        base_url = "https://forums.redflagdeals.com/"
        
        # Loop through each deal listing
        for listing in soup.find_all("li", class_="row topic"):
            store = self.get_store(listing)

            #Extract deal attributes
            item_element = listing.select_one('.topic_title_link')
            item = item_element.text.strip() if item_element else "N/A"

            votes_element = listing.select_one('.total_count_selector')
            votes = votes_element.text.strip() if votes_element else "N/A"

            username_element = listing.select_one('.thread_meta_author')
            username = username_element.text.strip() if username_element else "N/A"

            timestamp_element = listing.select_one('.first-post-time')
            timestamp = timestamp_element.text.strip() if timestamp_element else "N/A"

            category_element = listing.select_one('.thread_category a')
            category = category_element.text.strip() if category_element else "N/A"

            replies_element = listing.select_one('.posts')
            replies = replies_element.text.strip() if replies_element else "N/A"

            views_element = listing.select_one('.views')
            views = views_element.text.strip() if views_element else "N/A"
            
            # Extract the URL and prepend the base URL
            url_element = item_element['href'] if item_element else "N/A"
            url = base_url + url_element

            # Print the data of each deal
            print(f"Store: {store}")
            print(f"Item: {item}")
            print(f"Votes: {votes}")
            print(f"Username: {username}")
            print(f"Timestamp: {timestamp}")
            print(f"Category: {category}")
            print(f"Replies: {replies}")
            print(f"Views: {views}")
            print(f"URL: {url}")
            print("-------------------------")
            
    def deal_by_category(self):
        """
        Method to get the deals per category.

        Returns:
        dict: A dictionary containing categories as keys and their respective deal counts as values.
        """
        response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/")
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        catg = {} #Dictionary to put the category and their respective deals
        
        #Loop through each deal listing
        for listing in soup.find_all("li", class_="row topic"):
            # Get category of deal
            category_element = listing.select_one('.thread_category a')
            category = category_element.text.strip() if category_element else "N/A"
            #Count deals for each category
            if category in catg:
                catg[category] +=1
            else:
                catg[category] = 1            
        return catg

    def top_stores(self): 
        """
        Method to get all the top stores.

        Returns:
        None
        """
        response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/")
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        stores = {} #Dictionary to put the category and their respective deals
        for listing in soup.find_all("li", class_="row topic"):
            store = self.get_store(listing) #Extract the name of the store
            #Count the deals for each store
            if store in stores:
                stores[store] += 1
            else:
                stores[store] = 1
        num_top_stores = int(input("Enter the desired number of top stores to display: "))
        sorted_stores = sorted(stores.items(), key=lambda x: x[1], reverse=True)
        print("Top Stores:\n")
        #Top Stores being displayed based on the amount of deals
        for i, (store, deal_count) in enumerate(sorted_stores[:num_top_stores], 1):
            print(f"{i}. {store}: {deal_count} deals")        
    
    def deal_info(self):
        """
        Method to get information about deals by category and log their URLs to a file.

        Returns:
        None
        """
        url = "https://forums.redflagdeals.com/"
        response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/")
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")
        categories=set({})# Use a set to not have duplicate categories
        
        for listing in soup.find_all("li", class_="row topic"):
            category_element = listing.select_one('.thread_category a')
            category = category_element.text.strip() if category_element else "N/A"
            categories.add(category) # Add the categories in the set        
        num = 1
        category_dict={}
        
        for category in categories:# Store the categories from the set in a dictionary with their respective number
            print(num, category)
            category_dict[num]=category
            num += 1
        print("\n")
        input_category=int(input("Enter the number corresponding to the category:")) 
        chosen_category=category_dict.get(input_category)
        if not os.path.exists('log.txt'):
            open('log.txt', 'w').close()  # Create the log file if it doesn't exist
            #Try except block
            #close file ressources => or else intruder can intrude
        with open('log.txt', 'w') as file:
            # Write URLs of deals in the chosen category to log.txt
            for listing in soup.find_all("li", class_="row topic"):
                category_element = listing.select_one('.thread_category a')
                category = category_element.text.strip() if category_element else "N/A"
                if category == chosen_category:
                    item_element = listing.select_one('.topic_title_link')
                    if item_element:
                        deal_link = url + item_element['href']
                        file.write(deal_link + '\n')
        print("All the links have been logged successfully.")