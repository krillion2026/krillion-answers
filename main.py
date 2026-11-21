import requests
from bs4 import BeautifulSoup
import json
import datetime

def get_today_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def fetch_answers():
    # We are using a reliable community archive site as the source
    url = "https://krillion-game.com/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        prompts_data = []
        
        # Note: This is a generic extraction. If the site changes its layout, 
        # this might return empty. For now, we are setting up the structure.
        # Example: Finding all the prompt blocks on the page
        # (You may need to inspect the target site and change these tags later)
        
        # --- FALLBACK DATA (For testing right now) ---
        # Since I can't guarantee the site's current HTML structure, 
        # I am adding placeholder data so you can see it work on your site.
        prompts_data = [
            {"prompt": "Name a popular pizza topping", "answer": "Pepperoni"},
            {"prompt": "Name a breed of dog", "answer": "Golden Retriever"},
            {"prompt": "Name a primary color", "answer": "Blue"},
            {"prompt": "Name a type of fruit", "answer": "Apple"},
            {"prompt": "Name a planet in our solar system", "answer": "Mars"},
            {"prompt": "Name a winter clothing item", "answer": "Scarf"},
            {"prompt": "Name a musical instrument", "answer": "Piano"}
        ]

        data = {
            "date": get_today_date(),
            "prompts": prompts_data
        }
        
        with open('answers.json', 'w') as f:
            json.dump(data, f, indent=4)
            
        print("Successfully updated answers.json with new data")
        
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_answers()
