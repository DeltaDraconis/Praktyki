# Wybierz obraz bazowy Python 3.9
FROM python:3.9

# Przejdź do katalogu /app wewnątrz kontenera
WORKDIR /app

# Skopiuj całą zawartość Twojego projektu do katalogu /app w kontenerze
COPY . /app

# Instaluj potrzebne narzędzia i biblioteki
RUN apt-get update && apt-get install -y python3-pip
RUN pip install requests beautifulsoup4 python-dotenv

# Instalacja pyinstaller
RUN pip install pyinstaller

# Komenda do konwersji kodu na plik EXE za pomocą PyInstaller
CMD ["pyinstaller", "--onefile", "WebScraper.py"]
