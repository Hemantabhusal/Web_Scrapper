import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_schools_infinite_scroll():
    # 1. Launch Chrome (point to your chromedriver.exe if needed)
    driver = webdriver.Chrome()  # or webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
    driver.get("https:/collegenp.com/schools-in-lalitpur")
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
        new_height = driver.execute_script("return document.body.scrollHeight")
        # If height hasn’t changed, we likely reached the end
        if new_height == last_height:
            break
        last_height = new_height

    html = driver.page_source
    driver.quit()
    
    return html

def extract_school_names(html):
    soup = BeautifulSoup(html, "html.parser")
    schools = []
    # For example, if each school name is in <h3 class="college-name"><a>School Name</a></h3>
    # Adjust your selectors to match the actual HTML structure
    h3_tags = soup.find_all("h3", class_="college-name")
    for h3 in h3_tags:
        a_tag = h3.find("a")
        if a_tag:
            name = a_tag.get_text(strip=True)
            if name:
                schools.append(name)
    return schools

def main():
    html = scrape_schools_infinite_scroll()
    school_names = extract_school_names(html)
    print("School Names:")
    for name in school_names:
        print(name)

    # Save to Excel
    df = pd.DataFrame(school_names, columns=["School Name"])
    df.to_excel("Schools_in_lalitpur.xlsx", index=False)
    print("\nSaved all school names to 'Schools_in_lalitpur.xlsx'.")

if __name__ == "__main__":
    main()
