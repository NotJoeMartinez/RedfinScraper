import click
from .redfin_scraper import RedfinScraper

REDFIN_VERSION = '0.1.0'

@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(REDFIN_VERSION, message='redfin cli version: %(version)s')
def cli():
    pass



@cli.command()
@click.option("--zip-code", "-z", required=True, help="Get houses by zip code")
@click.option("--data-path", "-d", required=True, help="Path to zip code database")
def zip(zip_code, data_path):
    scraper = RedfinScraper()
    scraper.setup(data_path,multiprocessing=False)
    scraper.scrape(city_states=None,zip_codes=[zip_code])

    data = scraper.get_data()
    data.to_csv("data.csv", index=False)
