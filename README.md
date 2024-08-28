# Project Overview

This project involves processing articles from given URLs to perform content cleaning and analysis. The solution is implemented using Python and consists of four main components, each handled by a separate Python script.

## How I Approached the Solution

1. Extract Articles from Given URLs
   - File: `extract_articles.py`
   - Description: Scrapes the content from URLs listed in `Input.xlsx` using the BeautifulSoup library.
   - Output: Content is saved in the `URL_Content` folder.

2. Remove Stopwords from Extracted Articles
   - File: `remove_stopwords.py`
   - Description: Removes stopwords provided in the `StopWords` folder from the extracted content.
   - Output: Cleaned content is saved in the `Cleaned_URL_Content` folder.

3. Create Dictionary
   - File: `create_dictionary.py`
   - Description: Creates a dictionary of positive and negative words from the `MasterDictionary` folder.
   - Output: Dictionary is saved as `Dictionary.json`.

4. Analyze Variables
   - File: `analyze_variables.py`
   - Description: Analyzes variables based on the `Output Data Structure.xlsx` file.
   - Output: Analyzed variables are updated in the `Output Data Structure.xlsx` file itself.

## How to Run the Scripts

To execute the Python scripts and generate the output, follow these steps:

1. Create Environment:
   conda create -p "{path to the current directory}\venv"

2. Activate Environment:
   conda activate "{path to the current directory}\venv"

3. Install Dependencies:
   pip install -r requirements.txt

4. Run Main Script:
   python main.py

## Dependencies

All necessary packages are listed in `requirements.txt`.

## Notes

- In the `Output Data Structure.xlsx` file, rows where articles are removed or not found at the URL have been blanked out.