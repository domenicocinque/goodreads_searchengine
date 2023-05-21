from pathlib import Path
import logging

class Config:
    ROOT_DIR = Path(__file__).resolve().parent

    # Path to the data directory
    DATA_DIR = ROOT_DIR / "data"

    # Number of pages to scrape from the website
    MAX_NUM_PAGES = 5

    # Path to the index directory
    INDEX_DIR = DATA_DIR / "index"

    # Name of the data files
    RAW_HTML_DIR = DATA_DIR / "raw_html"
    BOOK_LIST_FILENAME = "data_list.csv"
    BOOK_DATA_FILENAME = "books.csv"

    # Logging level
    LOGGING_LEVEL = "DEBUG"

    logging.basicConfig(
        level=LOGGING_LEVEL,
        format="%(name)s | %(levelname)-8s | %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
    )



# The only config is a debug config for now
# TODO: Add a production config
config = Config()