import asyncio
import re
import os
import pdfkit
import markdown
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler

# Initial links list
initial_links = [
    "https://www.uiu.ac.bd/",
    ]


HTML_STYLE = """
<style>
    body { font-family: 'Segoe UI', sans-serif; padding: 30px; color: #333; background: #fdfdfd; }
    h1, h2, h3 { color: #004080; border-bottom: 2px solid #ddd; padding-bottom: 5px; }
    table { width: 100%; border-collapse: collapse; margin: 20px 0; }
    th, td { border: 1px solid #ccc; padding: 8px 12px; text-align: center; }
    th { background-color: #f2f2f2; }
    a { pointer-events: none; color: #000; text-decoration: none; }
    img { display: none; }
    code, pre { background-color: #f4f4f4; padding: 6px; display: block; overflow-x: auto; }
</style>
"""

# 📁 Ensure PDF output directory exists
OUTPUT_DIR = "dataPacks"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def sanitize_filename(url: str) -> str:
    """Sanitize URL into a filename-safe format."""
    return re.sub(r'[^\w\-]', '_', url.strip())[:80]

def extract_links_from_html(html: str) -> list:
    """Extract all unique HTTP(s) links from HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    return list({a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('http')})

async def scrape_and_save(link, crawler, visited, to_visit):
    """Scrape a single link, convert to PDF, and queue new links."""
    if link in visited:
        return

    clean_url = link.strip()
    print(f"[⇓] Scraping: {clean_url}")
    visited.add(link)

    try:
        result = await crawler.arun(url=clean_url)
        md_content = result.markdown

        # Convert Markdown to HTML
        html_body = markdown.markdown(md_content, extensions=["tables"])
        full_html = f"<html><head>{HTML_STYLE}</head><body><h1>{clean_url}</h1>{html_body}</body></html>"

        # Save PDF
        safe_name = sanitize_filename(clean_url)
        pdf_file = os.path.join(OUTPUT_DIR, f"{safe_name}.pdf")
        pdfkit.from_string(full_html, pdf_file)
        print(f"[✔] Saved PDF: {pdf_file}")

        # Extract links for further scraping
        found_links = extract_links_from_html(full_html)
        for new_link in found_links:
              if ( new_link not in visited and "uiu.ac.bd" in new_link  # only allow UIU domain
                  ):
                    to_visit.add(new_link)

    except Exception as e:
        print(f"[✘] Failed: {clean_url}\nReason: {e}")

async def main():
    visited_links = set()
    to_visit_links = set(initial_links)

    async with AsyncWebCrawler() as crawler:
        while to_visit_links:
            current_batch = list(to_visit_links)
            to_visit_links.clear()

            for link in current_batch:
                await scrape_and_save(link, crawler, visited_links, to_visit_links)

        print("\n[✅] Scraping complete.")
        print(f"Total pages saved: {len(visited_links)}")
        print("All visited links:")
        for v in sorted(visited_links):
            print(" -", v)

if __name__ == "__main__":
    asyncio.run(main())
