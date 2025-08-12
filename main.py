"""
Yahoo Finance News Scraper
--------------------------
This script scrapes news headlines from Yahoo Finance's homepage
and stores them in a PostgreSQL database.
"""

import requests
from bs4 import BeautifulSoup
import psycopg2
from datetime import datetime

# =========================
# Database Configuration
# =========================
DB_CONFIG = {
    'host': 'localhost',
    'port': '5432',
    'dbname': 'scraper',
    'user': 'postgres',
    'password': 'ygautam96'  # ⚠️ Consider using environment variables for security
}


# =========================
# Database Connection
# =========================
def connect_db():
    """
    Establish a connection to the PostgreSQL database.

    Returns:
        psycopg2.connection or None: Database connection object if successful, None if failed.
    """
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        print("❌ Database connection error:", e)
        return None


# =========================
# Insert Data into Database
# =========================
def insert_news(headline, url):
    """
    Insert a news headline and URL into the database.

    Args:
        headline (str): The news headline text.
        url (str): The URL of the news article.
    """
    conn = connect_db()
    if conn is None:
        return  # Skip if database connection failed

    try:
        cur = conn.cursor()
        query = """
            INSERT INTO bbc_news (headline, url, scraped_at)
            VALUES (%s, %s, %s)
            ON CONFLICT DO NOTHING
        """
        cur.execute(query, (headline, url, datetime.now()))
        conn.commit()
        cur.close()
        print(f"✅ Saved: {headline}")
    except psycopg2.Error as e:
        print("❌ Failed to insert data:", e)
    finally:
        conn.close()


# =========================
# Scrape Yahoo Finance News
# =========================
def scrape_yahoo_news():
    """
    Scrape news headlines from Yahoo Finance's homepage and store them in the database.
    """
    url = "https://finance.yahoo.com/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    base_url = "https://finance.yahoo.com/"

    # Fetch the webpage
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print("❌ Failed to load Yahoo Finance:", e)
        return

    # Parse HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    seen = set()  # Track already processed headlines

    # Extract news links and text
    for a_tag in soup.find_all("a", href=True):
        text = a_tag.get_text(strip=True)
        href = a_tag["href"]

        # Filter relevant news links
        if text and "/news/" in href and len(text) > 25:
            full_url = href if href.startswith("http") else base_url + href
            if text not in seen:
                insert_news(text, full_url)
                seen.add(text)


# =========================
# Script Entry Point
# =========================
if __name__ == "__main__":
    scrape_yahoo_news()
