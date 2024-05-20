from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__, template_folder='templates')

def scrape_player_info(player_name):
    # Split the player name into first and last names
    parts = player_name.split()
    
    # Check if the player name has at least two parts
    if len(parts) < 2:
        return ['607', '6.6', '5.5', '0.9', '49.2', '11.1', '57.0', '49.2', 'Kwame Brown', 'https://www.basketball-reference.com/req/202106291/images/headshots/brownkw01.jpg', True]
    else:
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
        media_item = soup.find(class_="media-item")
        
        if not media_item:
            return ['607', '6.6', '5.5', '0.9', '49.2', '11.1', '57.0', '49.2', 'Kwame Brown', 'https://www.basketball-reference.com/req/202106291/images/headshots/brownkw01.jpg', True]

        face = media_item.find('img')['src']
        print(face)
        stats_section = soup.find_all(class_="stats_pullout")

        if not stats_section:
            return ['607', '6.6', '5.5', '0.9', '49.2', '11.1', '57.0', '49.2', 'Kwame Brown', 'https://www.basketball-reference.com/req/202106291/images/headshots/brownkw01.jpg', True]
        
        for stats in stats_section:
            stats = stats.text.strip().replace(' ', '').split('\n')
        
        career_stats = [0, 0, 0, 0, 0, 0, 0, 0, player_name, face, False]
        
        for i in range(8):
            if i < 4:
                career_stats[i] = stats[(i*3)+7]
            else:
                career_stats[i] = stats[(i*3)+8]
        
        print(career_stats)
    else:
        return ['607', '6.6', '5.5', '0.9', '49.2', '11.1', '57.0', '49.2', 'Kwame Brown', 'https://www.basketball-reference.com/req/202106291/images/headshots/brownkw01.jpg', True]

    return career_stats

@app.route('/', methods=['GET', 'POST'])
def index():
    player_info = None
    if request.method == 'POST':
        player_name = request.form['player_name'].strip()
        player_info = scrape_player_info(player_name)
    
    return render_template('index.html', player_info=player_info)

if __name__ == '__main__':
    app.run(debug=True)
