# -Automated-Financial-News-Scraper
# 📈 Yahoo Finance News Scraper

A Python script that scrapes the latest news headlines from **Yahoo Finance** and stores them in a **PostgreSQL** database.

## 🚀 Features
- Scrapes headlines and URLs from Yahoo Finance homepage
- Stores data in a PostgreSQL database with timestamps
- Skips duplicate entries automatically (`ON CONFLICT DO NOTHING`)
- Simple, clean, and extendable code structure

## 📂 Project Structure

## 🛠 Requirements
- Python 3.8+
- PostgreSQL database
- Required Python packages:
  - `requests`
  - `beautifulsoup4`
  - `psycopg2`

## 📦 Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/yahoo-finance-scraper.git
   cd yahoo-finance-scraper
2.Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3.Insatall dependencies
pip install -r requirements.txt


*Requirements.txt
requests>=2.31.0
beautifulsoup4>=4.12.2
psycopg2-binary>=2.9.9

