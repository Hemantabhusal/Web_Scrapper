import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_page_html(page_number):
    if page_number == 1:
        url = "https://techbehemoths.com/companies/nepal"
    else:
        url = f"https://techbehemoths.com/companies/nepal?page={page_number}"
        
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
        print(f"Error fetching page {page_number}: {e}")
        return None

def extract_companies(html):
    soup = BeautifulSoup(html, "html.parser")
    # Each company's info is in a div with class "co-box__primary"
    primary_boxes = soup.select("div.co-box__primary")
    companies = []
    
    for box in primary_boxes:
        # Get all text within the div, with newlines between sub-elements.
        box_text = box.get_text(separator="\n", strip=True)
        lines = box_text.split("\n")

        # Remove any unwanted entries like "Verified Company"
        cleaned_lines = [line for line in lines if line and line != "Verified Company"]
        if not cleaned_lines:
            continue
        
        name = cleaned_lines[0]
        address_parts = cleaned_lines[1:]
        address = " ".join(address_parts).replace(" ,", ",").strip()
        
        companies.append((name, address))
    
    return companies

def main():
    all_companies = []
    page_number = 1

    while True:
        print(f"Fetching page {page_number}...")
        html = fetch_page_html(page_number)
        if not html:
            break

        companies = extract_companies(html)
        # If no companies are found, we've reached the last page.
        if not companies:
            print(f"No companies found on page {page_number}. Ending pagination.")
            break

        print(f"Found {len(companies)} companies on page {page_number}.")
        all_companies.extend(companies)
        page_number += 1

    df = pd.DataFrame(all_companies, columns=["Name", "Address"])
    excel_file = "Companies_in_nepal.xlsx"
    df.to_excel(excel_file, index=False)
    print(f"\nResults have been saved to '{excel_file}'.")

if __name__ == "__main__":
    main()
