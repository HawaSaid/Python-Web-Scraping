from Scraper import Scraper

def menu():
    print("‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐")
    print("***** Web Scraping Adventure *****")
    print("1. Display Latest Deals")
    print("2. Analyze Deals by Category")
    print("3. Find Top Stores")
    print("4. Log Deal Information")
    print("5. Exit")

def menuoptions():
    myScraper=Scraper() #Creates an instance of the Scraper class
    while True:
        menu()
        choice = int(input("Enter your choice:")) #Prompts the user to enter his choice
        print("")
        if choice == 1:
            myScraper.LatestDeals() #Invokes the LastestDeals() method in Scraper class
        elif choice == 2:
           display_categories() #Invokes the display_categories() method in Scraper class
        elif choice == 3:
            myScraper.top_stores() #Invokes the display_categories() method in Scraper class
        elif choice == 4:
            myScraper.deal_info() #Invokes the display_categories() method in Scraper class
        elif choice == 5:
            print("Exiting the program. Goodbye!")
            break   #Breaks out of the loop and exits the program

def display_categories(): #Displays all the categories and their respective number of deals
    myScrap=Scraper()
    categories = myScrap.deal_by_category() #assigns categories to the dictionnary being retured in deal_by_category()
    print("Categories and Number of Deals:\n")
    for category, deal_count in categories.items(): #Prints all the categories with their corresponding deals
        print(f"{category}: {deal_count} deals")
    print("\n")

if __name__ == "__main__":
    menuoptions()
