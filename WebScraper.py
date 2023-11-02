import requests
import time
from bs4 import BeautifulSoup

def search_amazon(product_name, quantity):
    """
    Wyszukuje produkty na Amazon i wyświetla informacje o nich.
    :param product_name: Nazwa produktu do wyszukania.
    :param quantity: Ilość produktów do wyświetlenia.
    """
    url = f'https://www.amazon.com/s?field-keywords={product_name}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('div', {'data-component-type': 's-search-result'})

        if len(items) >= quantity:
            items = items[:quantity]

            for item in items:
                title_element = item.find('span', {'class': 'a-text-normal'})
                price_element = item.find('span', {'class': 'a-offscreen'})
                link_element = item.find('a', {'class': 'a-link-normal'})

                if title_element:
                    title = title_element.text.strip()
                else:
                    title = "Brak dostępnych danych"

                if price_element:
                    price = price_element.text.strip()
                else:
                    price = "Brak dostępnych danych"

                if link_element:
                    link = 'https://www.amazon.com' + link_element.get('href')
                else:
                    link = "Brak dostępnych danych"

                print("Tytuł: " + title)
                print("Cena: " + price)
                print("Link: " + link)
                print("-" * 30)
                time.sleep(2)

        else:
            print(f"Nie znaleziono wystarczającej liczby wyników ({len(items)}), spróbuj zwiększyć ilość.")

    else:
        print("Błąd podczas pobierania strony Amazon. Kod statusu:", response.status_code)

if __name__ == "__main__":
    product_name = str(input("Wprowadź nazwę produktu na Amazon: "))
    quantity = int(input("Wprowadź ilość produktów do wyświetlenia: "))
    if quantity < 1:
        print("Nic ci nie wydzuka panie")
    search_amazon(product_name, quantity)
else:
    raise TimeoutError
