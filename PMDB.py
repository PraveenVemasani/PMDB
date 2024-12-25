from flask import Flask, redirect, request, jsonify, url_for, render_template
import requests
import json
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmZTM5MDdmZjY3Njk5ZGRmMjYyODQzOGNmNzk0Njg1NSIsInN1YiI6IjY0YmRmMWQzYjg2NWViMDBlMjA3MWY0OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.MgX6__rDRqspnY8aJQ2Ls9SXwIkAWtJPfhdL5wIlivI"
}


app = Flask(__name__, static_url_path='/static')


# Route to the selected Genre Type in the tmdbindex page
@app.route('/genre/<string:genre_id>/', methods=['GET'])
def get_genre(genre_id):
    url = "https://api.themoviedb.org/3/discover/movie?with_genres="+genre_id
    response = requests.get(url, headers=headers)
    result = response.json()

    if result.get('Response') == 'False':
        # Return an error message if the movie with the given name is not found in the movie data source
        return render_template('Search.html', name={'error': 'Movie not found'})
    else:
        movies=result["results"]
        genre_name=""
        genre_id = int(genre_id)
        with open('genres.json', 'r') as f:
            genres_data = json.load(f)
            for genre in genres_data["genres"]:
                if genre["id"] == genre_id:
                    genre_name=genre["name"]
                    break
        return render_template("Search.html", name=movies, pages=result['total_pages'], total=result['total_results'],
                               search=genre_name, page=result['page'])


@app.route('/<string:title_id>/<string:type>/', methods=['GET'])
def get_title(title_id, type):
    url = "https://api.themoviedb.org/3/"+type+"/"+title_id
    response = requests.get(url, headers=headers)
    result = response.json()

    # Cast Details
    url = "https://api.themoviedb.org/3/"+type+"/"+title_id+"/credits"
    response=requests.get(url,headers=headers)
    cast=response.json()

    # Videos
    url = "https://api.themoviedb.org/3/"+type+"/"+title_id+"/videos?language=en-US"
    response=requests.get(url,headers=headers)
    videos=response.json()

    if result.get('Response') == 'False':
        # Return an error message if the movie with the given name is not found in the movie data source
        return render_template('Search.html', name={'error': 'Movie not found'})
    else:
        return render_template("title.html", data=result,cast=cast["cast"])
        # return cast
        # return result
        # return videos


# Route to find Movies
@app.route('/movie/',methods=['Get'])
def get_movie():
    movie=request.args.get('Movie')
    return redirect(url_for('get_movie_details',movie_name=movie))
@app.route('/<string:movie_name>/', methods=['GET'])
def get_movie_details(movie_name):
    page = request.args.get('page', 1, type=int)  # Get the page number from the form (default to 1)
    url = "https://api.themoviedb.org/3/search/movie?query="+movie_name+"&page="+str(page)
    response = requests.get(url, headers=headers)

    data = response.json()
    # return jsonify(data)
    if data.get('Response') == 'False':
        # Return an error message if the movie with the given name is not found in the movie data source
        return render_template('Search.html', name={'error': 'Movie not found'})
    else:
        total_results = int(data['total_results'])
        pages = data["total_pages"]
        movies=data["results"]
        return render_template("Search.html", name=movies, pages=pages, total=data['total_results'],
                               search=movie_name, page=page)
    

# Route to tmdbindex
@app.route('/', methods=['GET'])
def get_movies():
    url_trending_movies = "https://api.themoviedb.org/3/trending/movie/day"
    response_trending_movies = requests.get(
        url_trending_movies, headers=headers)
    url_trending_tv = "https://api.themoviedb.org/3/trending/tv/day"
    response_trending_tv = requests.get(url_trending_tv, headers=headers)
    url_now_playing_movies = "https://api.themoviedb.org/3/movie/now_playing?query=region=IN"
    response_now_playing_movies = requests.get(
        url_now_playing_movies, headers=headers)
    url_now_playing_Telugu_movies = "https://api.themoviedb.org/3/discover/movie?with_genres=10749"
    response_now_playing_Telugu_movies = requests.get(
        url_now_playing_Telugu_movies, headers=headers)
    url_categories="https://api.themoviedb.org/3/genre/movie/list"
    response_categories= requests.get(url_categories, headers=headers)
    if response_trending_movies.status_code == 200 and response_trending_tv.status_code == 200 and response_now_playing_movies.status_code == 200:
        data = response_trending_movies.json()
        trending_movies = data['results']
        data = response_trending_tv.json()
        trending_tv = data['results']
        data = response_now_playing_movies.json()
        now_playing_movies = data['results']
        data = response_now_playing_Telugu_movies.json()
        now_playing_Telugu_movies = data['results']
        data = response_categories.json()
        categories = data['genres']
        return render_template("tmdbindex.html", name_dis_movies=trending_movies, name_dis_tv=trending_tv, now_playing_movies=now_playing_movies,name_playing_telugu=now_playing_Telugu_movies,categories=categories)
    else:
        return jsonify({"error": "Failed to retrieve movies"}), response_trending_movies.status_code


if __name__ == '__main__':
    app.run(debug=True)
