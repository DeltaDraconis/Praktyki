# Użyj obrazu bazowego Pythona
FROM python:3.9

# Ustaw katalog roboczy na /app
WORKDIR /app

# Skopiuj plik wymagań (requirements.txt) do obrazu
COPY requirements.txt .

# Zainstaluj zależności za pomocą pip
RUN pip install -r requirements.txt

# Skopiuj resztę plików projektu do obrazu
COPY . .

# Zainstaluj pyinstaller
RUN pip install pyinstaller


# Kompiluj skrypt Pythona do pliku wykonywalnego .exe
RUN pyinstaller --onefile web_scraper.py

# Określ plik wykonywalny jako ENTRYPOINT
ENTRYPOINT ["./dist/web_scraper"]
