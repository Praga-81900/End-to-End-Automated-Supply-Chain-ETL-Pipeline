#  Automated Supply Chain ETL Pipeline

###  Hey there!
Ever got tired of manually copying and pasting supplier prices and stock details into an Excel sheet every single day? Same here. Manual data entry is a bottleneck, so I decided to build a system to do the heavy lifting for me.

This is a fully automated **ETL (Extract, Transform, Load)** pipeline that I built from scratch. It goes out to the web, grabs live supplier data, cleans up all the messy text, and neatly organizes it into a relational database. 

### 🛠️ What I Used (The Tech Stack)
* **Python** - The core engine running the show.
* **BeautifulSoup 4 & Requests** - For the 'Extract' phase (Web Scraping).
* **Pandas** - For the 'Transform' phase (Data cleansing and manipulation).
* **SQLAlchemy & MySQL** - For the 'Load' phase (Database management).

### ⚙️ How It Actually Works

1. **Phase 1: Extract (`live_scraper.py`)** Instead of downloading CSVs manually, this script hits the supplier's website, scrapes live product names, pricing, and availability, and stores the raw data.
   
2. **Phase 2: Transform (`transformer.py`)**
   Raw web data is always messy. This script uses Pandas to strip out weird currency symbols (like `£` or `$`), fixes missing values, and converts text like "In Stock" into boolean/numeric values (1s and 0s) so the database won't crash.

3. **Phase 3: Load (`loader.py`)**
   Once the data is clean and "business-ready", SQLAlchemy automatically connects to my local MySQL database, creates the necessary tables if they don't exist, and loads the data perfectly.

###  Want to run this on your machine?

1. Clone this repository.
2. Install the required libraries:
   ```bash
   pip install pandas sqlalchemy mysql-connector-python beautifulsoup4 requests
   Make sure your MySQL server is running (Update your credentials in loader.py).

Run the pipeline in this exact order:
python live_scraper.py
python transformer.py
python loader.py

Check your MySQL database. Boom! The data is sitting right there. 
Note: This was built as a hands-on solution to a real-world Data Engineering problem. Feel free to explore the code, fork it, or suggest better ways to optimize the pipeline!
