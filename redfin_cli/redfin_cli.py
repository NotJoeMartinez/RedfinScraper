import click
import datetime
from .redfin_scraper import RedfinScraper

REDFIN_VERSION = '0.1.0'

@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(REDFIN_VERSION, message='redfin cli version: %(version)s')
def cli():
    pass



@cli.command()
@click.option("--zip-code", "-z", required=False, help="Get houses by zip code")
@click.option("--city-state", "-c", required=False, help="Get houses by city and state")
@click.option("--data-path", "-d", required=True, help="Path to zip code database")
@click.option("--sold-by", "-s", required=False, help="1mo','3mo','6mo','1yr','2yr','3yr','5yr' ")
def export(zip_code, data_path, city_state, sold_by):

    if zip_code is None and city_state is None:
        print("Please provide either a zip code or a city-state")
        return
    


    scraper = RedfinScraper()
    scraper.setup(data_path,multiprocessing=False)

    if city_state is None:
        arg_city_state = None
    else:
        arg_city_state = [city_state]
    

    if sold_by is None:
        print("Scraping for active listings")
        scraper.scrape(zip_codes=[zip_code], city_states=arg_city_state)
    else:
        scraper.scrape(zip_codes=[zip_code], 
                       city_states=arg_city_state, 
                       sold=True,
                       sale_period=sold_by)

    data = scraper.get_data()
    # remove SALE TYPE = In accordance with local MLS rules, some MLS listings are not included in the download

    clean_data = data[data['SALE TYPE'] != 'In accordance with local MLS rules, some MLS listings are not included in the download']

    date_str = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    out_csv = f"{date_str}_data.csv"
    print(f"Exporting data to {out_csv}")
    clean_data.to_csv(out_csv, index=False)
