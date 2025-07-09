import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_page_html(page_num):
    base_url = (
        "https://edusanjal.com/school/district/kathmandu/grade/basic,plus-2,pre-school,secondary/"
    )
    url = f"{base_url}?page={page_num}"
    
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/98.0.4758.102 Safari/537.36"
        )
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching page {page_num}: {e}")
        return None

def extract_school_names(html):
    soup = BeautifulSoup(html, "html.parser")
    schools = []
    # Updated selector to match the <span> containing the school names
    spans = soup.select("span.flex-grow.min-w-0")
    for span in spans:
        name = span.get_text(strip=True)
        if name:
            schools.append(name)
    
    return schools


def main():
    all_schools = []
    for page_num in range(1, 63):  # 1 through 63
        print(f"Fetching page {page_num}...")
        html = fetch_page_html(page_num)
        if not html:
            print(f"Skipping page {page_num} due to fetch error.")
            continue
        
        schools_on_page = extract_school_names(html)
        print(f"Found {len(schools_on_page)} schools on page {page_num}.")
        all_schools.extend(schools_on_page)

    df = pd.DataFrame(all_schools, columns=["School Name"])
    df.to_excel("kathmandu_schools.xlsx", index=False)
    print("\nSaved all school names to 'Kathmandu_schools.xlsx'.")

if __name__ == "__main__":
    main()
