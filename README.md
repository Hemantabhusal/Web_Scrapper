# 🕸️ Web Scraping Suite for Nepal-Based Tech & School Data

A collection of Python-based web scrapers tailored to Nepal-specific websites for extracting tech company and school data. It supports both paginated and infinite scrolling (lazy loading) pages using Selenium.

---

## 🧩 Features

- 🔍 Paginated scraping for:
  - Tech companies (TechBehemoths)
  - Schools in Kathmandu (EduSanjal)
- 🔁 Infinite scroll scraping for:
  - Schools in Lalitpur (CollegeNP)
- 📄 Clean Excel output using `pandas`
- ⚙️ Modular, well-commented, and extensible codebase
- 🛡️ Error handling and browser simulation with user-agent headers

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

### 🧾 `requirements.txt`

```text
beautifulsoup4==4.13.4
certifi==2025.7.9
charset-normalizer==3.4.2
idna==3.10
numpy==2.3.1
pandas==2.3.1
python-dateutil==2.9.0.post0
pytz==2025.2
requests==2.32.4
six==1.17.0
soupsieve==2.7
typing_extensions==4.14.1
tzdata==2025.2
urllib3==2.5.0
```

> ⚠️ **If using the lazyloading scrapping script**, make sure you also install:
> 
> - `selenium`
> - ChromeDriver (installed and added to your system `PATH`)

---

## 🚀 Usage

Each script runs independently. Use the following commands:

### 🏢 TechBehemoths Company Scraper

```bash
python static_page_scraping.py
```

- **Output:** `Companies_in_nepal.xlsx`

---

### 🏫 EduSanjal School Scraper

```bash
python paginated_scrapping.py
```

- **Output:** `kathmandu_schools.xlsx`

---

### 🌀 CollegeNP Infinite Scroll Scraper

```bash
python scrapping_for_lazyloading.py
```

- **Output:** `Schools_in_lalitpur.xlsx`

---

## 📁 Project Structure

```text
.
├── static_page_scrapping.py        # Single-page scraper for company listings on TechBehemoths
├── pagianted_scrapping.py          # Scrapes paginated schools from EduSanjal
├── scrapping_for_lazyloading.py    # Scrapes lazy-loaded schools from CollegeNP using Selenium
├── requirements.txt                # All Python dependencies
└── README.md                       # This file
```

---

## 🔧 How It Works

### 🧭 Static Scrapers (TEduSanjal)

- Uses `requests` and `BeautifulSoup`
- Scrapes data from a single, non-paginated HTML page
- Parses company listings directly without pagination handling

### 🧭 Paginated Scrapers (Edusanjal)

- Uses `requests` and `BeautifulSoup`
- Detects pagination and follows "Next" links
- Parses HTML to extract structured data

### 🔄 Infinite Scroll Scraper (CollegeNP)

- Uses `Selenium` WebDriver
- Simulates browser scroll to load content
- Waits dynamically for elements to appear before extraction

---

## 📊 Output Format

Most scripts generate Excel files with:
- 📌 Name
- 📍 Address & location
- ☎️ Contact information

---

## 🛠️ Customization

You can adapt the scripts to:
- Scrape other websites
- Add or remove data fields
- Export to Excel or CSV or JSON
- Include filters (e.g., by location or type)

---

## 🙌 Acknowledgments

- [TechBehemoths](https://techbehemoths.com) – Tech directory
- [EduSanjal](https://edusanjal.com) – School listings
- [CollegeNP](https://collegenp.com) – College portal
- 🐍 `BeautifulSoup` – HTML parser
- 🤖 `Selenium` – Browser automation
- 📊 `pandas` – Data analysis and Excel export

---


## 🤝 Contributing

Contributions are welcome! Fork the repo and submit a pull request. Suggestions, bug fixes, and improvements are appreciated.
