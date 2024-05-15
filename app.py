from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
import re

app = Flask(__name__, template_folder='templates')

def scrape_player_info(player_name):
    # Split the player name into first and last names
    parts = player_name.split()
    first_name = parts[0].lower()
    last_name = parts[1].lower()
    
    print(first_name, last_name)
    # Construct the player's URL
    player_url = f'https://www.basketball-reference.com/players/{last_name[0]}/{last_name[:5]}{first_name[:min(2, len(first_name))]}01.html'
    print("Player URL:", player_url)

    # Send a request to the player's URL
    response = requests.get(player_url)
    print("Response Status Code:", response.status_code)

    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        face = soup.find(class_="media-item").find('img')['src']
        stats = soup.find_all(class_="stats_pullout")
        
        for i in stats:
            stats=i.text.strip().replace(' ', '').split('\n')

        career_stats = [0, 0, 0, 0, 0, 0, 0, 0, player_name, face]
        
        for i in range(8):
            if i < 4:
                career_stats[i] = stats[(i*3)+7]
            else:
                career_stats[i] = stats[(i*3)+8]
        
        print(career_stats)

    return career_stats
    

@app.route('/', methods=['GET', 'POST'])
def index():
    player_info = None
    if request.method == 'POST':
        player_name = request.form['player_name']
        
        player_info = scrape_player_info(player_name)
    
    return render_template('index.html', player_info=player_info)

if __name__ == '__main__':
    app.run(debug=True)
