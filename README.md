# Basketball Web Scraper

This project is a web application built with Flask that allows users to search for basketball players and retrieve their career statistics. It scrapes data from the website [Basketball Reference](https://www.basketball-reference.com/). This project is a work in progress as I wanted to learn about web scraping.

## Features

- Users can enter a basketball player's name in the search bar.
- The application retrieves the player's career statistics including games played, points per game, rebounds per game, assists per game, field goal percentage, 3-point field goal percentage, free throw percentage, and effective field goal percentage.

## Technologies Used

- Python
- Flask
- BeautifulSoup
- HTML
- TailwindCSS

## Usage (Windows)

1. Clone the repository.
2. Create a virtual environment (`python3 -m venv .venv` and `.venv\Scripts\activate`)
3. Install the required dependencies (`flask`, `bs4`, `requests`, `re`).
4. Run the Flask application (`flask run`).
5. Open your web browser and navigate to `http://localhost:5000`.
6. Enter the name of the basketball player you want to search for and click on the "Search" button.
7. View the player's career statistics displayed on the page.
