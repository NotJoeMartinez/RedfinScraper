from setuptools import setup, find_packages



with open('requirements.txt') as f:
    dependencies = f.read().splitlines()

with open('README.md', 'r') as f:
    long_description = f.read()


entry_points = {
    'console_scripts': [
        'redfin=redfin_cli.redfin_cli:cli',
    ],
}

setup(
    name='wieniawski', 
    description='Fork of Redfin scraper with some bugfixes. Designed for cli usage',
    long_description=long_description,
    long_description_content_type='text/markdown', 
    author='NotJoeMartinez',
    url='https://github.com/NotJoeMartinez/RedfinScraper-CLI',
    packages=find_packages(),
    install_requires=dependencies,
    entry_points=entry_points,
    python_requires='>=3.8',
)