import feedparser
import pandas as pd

# URL RSS feed
rss_urls = [
    "https://rss.tempo.co/nasional",
    "https://rss.tempo.co/bisnis",
    "https://rss.tempo.co/olahraga"
]

# Ambil data dari RSS feed
data = []
for url in rss_urls:
    feed = feedparser.parse(url)
    for entry in feed.entries:
        data.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "summary": entry.summary
        })

# Simpan ke DataFrame
df = pd.DataFrame(data)
df.to_csv("news_data_rss.csv", index=False)
print("Data berhasil disimpan ke file news_data_rss.csv")
