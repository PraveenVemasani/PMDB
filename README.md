# ADD.ME

## Project Name
**Praveen Movie Database (PMDB)**

## Description
PMDB is a Flask-based web application that serves as a personal movie database. It utilizes The Movie Database (TMDb) API to display information about movies, TV shows, and genres. Users can browse movies by genre, search for specific titles, and view detailed information about selected movies or shows.
<img width="959" alt="PMDB" src="https://github.com/user-attachments/assets/e6502e5b-78f5-4a07-b700-4e85516d886b" />

## Project Structure

- **Static Folder**:
  - Contains images for genres.
  - Includes CSS and JavaScript files for styling and interactivity.

- **Templates Folder**:
  - `Search.html`: Displays search results for movies or genres.
  - `title.html`: Shows detailed information about a selected movie or TV show.
  - `tmdbindex.html`: The homepage displaying sections like trending movies, trending TV shows, latest releases, and genre-based movies.

- **JSON File**:
  - `genres.json`: Contains the name and ID of each genre as per the TMDb database.

- **PMDB.py**:
  - The main Python script containing the Flask application and routes for handling requests and rendering templates.

## Features
- Browse movies by genres with detailed sections for trending and latest releases.
- Search for specific movies and TV shows.
- View detailed information, including cast and related videos, for selected movies or shows.
- Displays genre-based movie lists using TMDb API.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/PraveenVemasani/pmdb.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pmdb
   ```
3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your TMDb API key to the `PMDB.py` file:
   - Locate the `Authorization` key in the `headers` dictionary and replace the existing value with your TMDb API key.

## Usage
1. Start the Flask application:
   ```bash
   python PMDB.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000/` to access the application.

3. Interact with the application:
   - Browse the homepage for trending movies and TV shows.
   - Search for movies or shows using the search bar.
   - Click on any movie or TV show for detailed information.

## API Integration
This project integrates with the following TMDb API endpoints:
- Trending Movies and TV Shows: `/trending/movie/day`, `/trending/tv/day`
- Now Playing Movies: `/movie/now_playing`
- Genre List: `/genre/movie/list`
- Search: `/search/movie`
- Movie/TV Details: `/movie/{id}`, `/tv/{id}`
- Movie/TV Credits: `/movie/{id}/credits`, `/tv/{id}/credits`



## Contact
If you have any questions or suggestions, feel free to contact me:

- Email: [praveenchowdaryvemasani@gmail.com]
- GitHub: [https://github.com/PraveenVemasani]
