# bookstorewebscrape-and-analysis

This project demonstrates how to collect, clean, analyze, and visualize data scraped from an online bookstore. The dataset was gathered using Python web scraping techniques and analyzed with tools like Pandas, Seaborn, and Plotly. The result: a set of interactive insights into book pricing, availability, ratings, and more.

---

# Project Overview

## What this project covers:
- *Web Scraping* book data (title, price, rating, availability, etc.)
- *Data Cleaning & Transformation* using Pandas
- *Exploratory Data Analysis (EDA)* with Seaborn & Matplotlib
- *Interactive Visualizations* with Plotly
- *SQL queries* on cleaned dataset

---

#  Project Structure

bookstore-web-scraping-eda/
│
├── cleaned_books_data.csv # Final cleaned dataset
├── scraper.py # Web scraper script (optional to include)
├── DA.ipynb # Jupyter Notebook with EDA and visualizations
├── app.py # Optional Streamlit app for dashboard
├── requirements.txt # Python libraries used


---

# Tools & Technologies Used

- `requests`, `BeautifulSoup` – for web scraping
- `pandas` – data manipulation
- `seaborn`, `matplotlib` – static visualizations
- `plotly.express` – interactive charts
- `streamlit` – interactive dashboard (optional)
- `sqlite3` or `sqlalchemy` – SQL querying (optional)

---

#  Key Visualizations

- 📌 Top 10 Most Expensive Books
- 📈 Average Price by Rating
- 🟩 Book Availability Distribution (Pie & Donut Charts)
- 📉 Rating vs Price (Scatter Plot)
- 📚 Top Authors by Book Count
- 📦 Histogram of Book Prices
- 🧠 Correlation Heatmap

---

# Key Insights

- A large majority of books are **in stock**, though some are consistently out of stock.
- **Price doesn’t always correlate with rating** — some of the cheapest books have top ratings.
- A few authors publish **many titles**, indicating popularity or series.
- There is a **wide variance in pricing**, even among similarly rated books.

---

# Install Reqiurement 

Install requirements
│
├── pip install requests #Download HTML content from website Final cleaned dataset
├── pip install beautifulsoup4 # Parse and extract data from html
├── pip install pandas # Data Cleaning and manipulation
├── pip install seaborn # Static visualisation
├── pip install plotly # Interactive chart and dashboard
├── pip install matplotlib # Static visualisation
├── pip install plotly # Interactive chart and dashboard
├── pip install sqlite # You c an also use built-in sqlite3

# How to Run
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/bookstore-web-scraping-eda.git
cd bookstore-web-scraping-eda
