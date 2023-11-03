
FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip install pyinstaller

RUN pyinstaller --onefile web_scraper.py

ENTRYPOINT ["./dist/web_scraper"]
