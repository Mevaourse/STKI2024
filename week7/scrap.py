import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL situs berita
url = "https://www.kompas.com/"

# Ambil konten halaman
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Perbarui sesuai struktur halaman
    articles = soup.find_all('div', class_='article__list')
    data = []
    for article in articles:
        title_tag = article.find('h3', class_='article__title')
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag.find('a')['href']
            print(f"Title: {title}, Link: {link}")  # Debug log
            data.append({"title": title, "link": link})
    
    # Simpan ke DataFrame jika ada data
    if data:
        df = pd.DataFrame(data)
        df.to_csv("news_data_scraped.csv", index=False)
        print("Data berhasil disimpan ke file news_data_scraped.csv")
    else:
        print("Tidak ada data yang ditemukan pada halaman ini.")
else:
    print(f"Failed to fetch page: {response.status_code}")
