# 🕸️ Web Scraping Suite for Nepal-Based Tech & School Data

A collection of Python-based web scrapers tailored to Nepal-specific websites for extracting tech company and school data. It supports both paginated and infinite scrolling (lazy loading) pages using Selenium.

---

## 🧩 Features

- 🔍 Static scraping for:
  - Tech companies (TechBehemoths)
- 🔍 Paginated scraping for:
  - Schools in Kathmandu (EduSanjal)
- 🔁 Infitine/Lazy-Loading scraping for:
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

## 🔧 How It Works

### 🧭 Static Scrapers (TEduSanjal)

- Uses `requests` and `BeautifulSoup`
- Scrapes data from a single, non-paginated HTML page
- Parses company listings directly without pagination handling

### 🧭 Paginated Scrapers (Edusanjal)

- Uses `requests` and `BeautifulSoup`
- Detects pagination and follows "Next" links
- Parses HTML to extract structured data

### 🔄 Infinite/Lazy-Loading Scroll Scraper (CollegeNP)

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
