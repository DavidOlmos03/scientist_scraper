import json
from scraper import search_scientist
from nlp import process_text
from database import save_to_db

def main():
    with open("data/scientists.json", "r", encoding="utf-8") as file:
        scientists = json.load(file)
    
    for scientist in scientists:
        data = search_scientist(scientist["name"])
        data["bio_tokens"] = process_text(data["bio"])
        save_to_db(data)
        print(f"Guardado en MongoDB: {data}")

if __name__ == "__main__":
    main()

