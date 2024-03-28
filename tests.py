from redfin_scraper import RedfinScraper

scraper=RedfinScraper()

scraper=RedfinScraper()
scraper.setup('./zip_code_database.csv',multiprocessing=False)

# scraper=RedfinScraper()
# scraper.setup() # From Config

# scraper.setup() # Test for no re-download

# scraper.scrape(city_states=None,zip_codes=['JUNK'])
# scraper.scrape(city_states=None,zip_codes='JUNK')
# scraper.scrape(city_states=['Omaha, NE'],zip_codes='JUNK')
# scraper.scrape(city_states=None,zip_codes=['77002','JUNK','77003'])
# scraper.scrape(city_states=['Omaha,NE'],zip_codes=None)
# scraper.scrape(city_states=[('Newark', 'NJ'),'JUNK, JUNKY'],zip_codes=None)
# scraper.scrape(city_states=['junk, junky'],zip_codes=['77002'])
# scraper.scrape() # From Config
scraper.scrape(city_states=['Omaha,NE'],zip_codes=None)

print(scraper.get_data())

for i in range(1,11):
    try:
        scraper.get_data(id=f"D00{i}")
    except:
        print("Failed")


