import requests
from bs4 import BeautifulSoup

url = "https://www.euronics.lv/audio/austinas/bezvadu-austinas?f=Cgl2aWV3c2Rlc2MwAg&p=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    product_cards = soup.select("[data-product-id]")

    print(f"Atrasti {len(product_cards)} produkti")
    for prece in product_cards:
        nosaukums = None
        for selector in [".name", ".title", "h3", ".product-title", ".product-name"]:
            name_elem = prece.select_one(selector)
            if name_elem:
                nosaukums = name_elem.get_text(strip=True)
                break

        if not nosaukums:
            for a in prece.find_all("a"):
                text = a.get_text(strip=True)
                if text:
                    nosaukums = text
                    break

        cena = None
        for selector in [".price", ".current-price", ".product-price"]:
            price_elem = prece.select_one(selector)
            if price_elem:
                cena = price_elem.get_text(strip=True)
                break

        if nosaukums:
            print("Nosaukums:", nosaukums)
        if cena:
            print(cena)
        print("---")
else:
    print("Kļūda ielādējot lapu. Statusa kods:", response.status_code)
