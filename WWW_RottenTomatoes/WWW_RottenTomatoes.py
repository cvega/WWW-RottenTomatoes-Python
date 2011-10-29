#!/usr/bin/env python

import urllib.parse, urllib.request, json

class WWW_RottenTomatoes(object):
    """
    RottenTomatoes API client for Python 3

    Notes: -all public methods return a json object.
           -@param not required unless otherwise specified

    @param: token (api key), required
    @param: debug (formats json for debugging aka pretty printing)
    
    """
    def __init__(self, token, debug=None):
        self.host = 'http://api.rottentomatoes.com/api/public/v1.0'
        self.header = {'User-Agent':'python-WWW-RottenTomatoes/1.0'}

        self.params = '.json?apikey=' + token
        if debug is not None:
            self.params += '&_prettyprint=true'

    """
    Make HTTP request to api and return data via a JSON object

    @params: url (the constructed url passed from a public method), required
    """
    def __request__(self, url):
        req = urllib.request.Request(url=url, headers=self.header)
        response = urllib.request.urlopen(req).read()

        return json.loads(bytes.decode(response))

    """
    Displays Top Box Office Earning Movies, Sorted by Most Recent Weekend Gross
    Ticket Sales

    @param: limit (Limits the number of results returned), default 10
    @param: country (localized country data (ISO 3166-1 alpha-2)), default US
    """
    def BoxOfficeMovies(self, limit=None, country=None):
        if limit is not None:
            self.params += '&limit=' + limit
        if country is not None:
            self.params += '&county=' + country 
   
        url = self.host + '/lists/movies/box_office' + self.params
        
        return self.__request__(url)

    """
    Retrieves movies currently in theaters

    @param: country (localized country data (ISO 3166-1 alpha-2)), default US
    @param: page (The selected page of upcoming movies), default 1
    @param: page_limit (Opcoming movies to show per page), default 16 
    """
    def InTheaterMovies(self, country=None, page=None, page_limit=None):
        if country is not None:
            self.params += '&county=' + country
        if page is not None:
            self.params += '&page=' + page
        if page_limit is not None:
            self.params += '&page_limit=' + page_limit

        url = self.host + '/lists/movies/in_theaters' + self.params

        return self.__request__(url)

    """
    Retrieves current opening movies

    @param: limit (Limits the number of results returned), default 16
    @param: country (localized country data (ISO 3166-1 alpha-2)), default US
    """
    def OpeningMovies(self, limit=None, country=None):
        if limit is not None:
            self.params += '&limit=' + limit
        if country is not None:
            self.params += '&county=' + country

        url = self.host + '/lists/movies/opening' + self.params

        return self.__request__(url)

    """
    Retrieves upcoming movies. Results are paginated if they go past the
    specified page limit.

    @param: country (localized country data (ISO 3166-1 alpha-2)), default US
    @param: page (The selected page of upcoming movies), default 1
    @param: page_limit (Opcoming movies to show per page), default 16
    """
    def UpComingMovies(self, country=None, page=None, page_limit=None):
        if country is not None:
            self.params += '&county=' + country
        if page is not None:
            self.params += '&page=' + page
        if page_limit is not None:
            self.params += '&page_limit=' + page_limit

        url = self.host + '/lists/movies/upcoming' + self.params

        return self.__request__(url)

    """
    Retrieves the current top dvd rentals
    
    @param: limit (Limits the number of results returned), default 16
    @param: country (localized country data (ISO 3166-1 alpha-2)), default US    
    """
    def TopRentalsDvds(self, limit=None, country=None):
        if limit is not None:
            self.params += '&limit=' + limit
        if country is not None:
            self.params += '&county=' + country

        url = self.host + '/lists/dvds/top_rentals' + self.params

        return self.__request__(url)

    """
    Retrieves current release dvds. Results are paginated if they go past the
    specified page limit
    
    @param: country (localized country data (ISO 3166-1 alpha-2)), default US
    @param: page (The selected page of upcoming movies), default 1
    @param: page_limit (Opcoming movies to show per page), default 16
    """
    def CurrentReleaseDvds(self, country=None, page=None, page_limit=None):
        if country is not None:
            self.params += '&county=' + country
        if page is not None:
            self.params += '&page=' + page
        if page_limit is not None:
            self.params += '&page_limit=' + page_limit

        url = self.host + '/lists/dvds/current_releases' + self.params

        return self.__request__(url)

    """
    Retrieves new release dvds. Results are paginated if they go past the
    specified page limit.

    @param: country (localized country data (ISO 3166-1 alpha-2)), default US
    @param: page (The selected page of upcoming movies), default 1
    @param: page_limit (Opcoming movies to show per page), default 16
    """
    def NewReleaseDvds(self, country=None, page=None, page_limit=None):
        if country is not None:
            self.params += '&county=' + country
        if page is not None:
            self.params += '&page=' + page
        if page_limit is not None:
            self.params += '&page_limit=' + page_limit

        url = self.host + '/lists/dvds/new_releases' + self.params

        return self.__request__(url)

    """
    Retrieves upcoming dvds. Results are paginated if they go past the specified
    page limit

    @param: country (localized country data (ISO 3166-1 alpha-2)), default US
    @param: page (The selected page of upcoming movies), default 1
    @param: page_limit (Opcoming movies to show per page), default 16
    """
    def UpcomingDvds(self, country=None, page=None, page_limit=None):
        if country is not None:
            self.params += '&county=' + country
        if page is not None:
            self.params += '&page=' + page
        if page_limit is not None:
            self.params += '&page_limit=' + page_limit

        url = self.host + '/lists/dvds/upcoming' + self.params

        return self.__request__(url)

    """
    Detailed information on a specific movie specified by Id. You can use the
    movies search endpoint or peruse the lists of movies/dvds to get the urls
    to movies.

    @param: movie_id (The id number of a specific movie), required
    """
    def MoviesInfo(self, movie_id):
        url = self.host + '/movies/' + movie_id + self.params

        return self.__request__(url)

    """
    Pulls the complete movie cast for a movie

    @param: movie_id (The id number of a specific movie), required
    """
    def MoviesCast(self, movie_id):
        url = self.host + '/movies/' + movie_id + '/cast' + self.params

        return self.__request__(url)

    """
    Pulls the complete movie cast for a movie

    @param: movie_id (The id number of a specific movie), required
    """
    def MoviesClips(self, movie_id):
        url = self.host + '/movies/' + movie_id + '/clips' + self.params

        return self.__request__(url)

    """
    Retrieves the reviews for a movie. Results are paginated if they go past the
    specified page limit

    @param: country (localized country data (ISO 3166-1 alpha-2)), default US
    @param: page (The selected page of upcoming movies), default 1
    @param: page_limit (Opcoming movies to show per page), default 16
    @param: review_type (3 review types are possible:

                        "all", "top_critic" and "dvd". Default "top_critic"

                        "top_critic" shows all the designated top critics.
                        "dvd" pulls the reviews given on the DVD of the movie.
                        "all" as the name implies retrieves all reviews.)
    """
    def MoviesReviews(self, movie_id, review_type=None, country=None, page=None, page_limit=None):
        if review_type is not None:
            self.params += '&review_type=' + review_type
        if country is not None:
            self.params += '&county=' + country
        if page is not None:
            self.params += '&page=' + page
        if page_limit is not None:
            self.params += '&page_limit=' + page_limit

        url = self.host + '/movies/' + movie_id + '/reviews' + self.params

        return self.__request__(url)

    """
    Shows similar movies for a movie

    @param: movie_id (The id number of a specific movie), required
    @param: limit (Limits the number of results returned), default 16
    """
    def MoviesSimilar(self, movie_id, limit=None):
        if limit is not None:
            self.params += '&limit=' + limit

        url = self.host + '/movies/' + movie_id + '/similar' + self.params

        return self.__request__(url)

    """
    Provides a movie lookup by an id from a different vendor. Only supports imdb
    lookup at this time

    @param: movie_id (The id number of a specific movie), required
    @param: type (alias type to look up - only imdb is supported at this time)
    """
    def MoviesAlias(self, movie_id, alias_type):
        
        self.params += '&type=' + alias_type
        self.params += '&id' + movie_id
        
        url = self.host + '/movie_alias/' + self.params

        return self.__request__(url)

    """
    The movies search endpoint for plain text queries.

    @param: query (plain text), required
    @param: page  (selected page of movie results), default 1
    @param: limit (results per page), default 30
    """
    def MoviesSearch(self, query, page=None, limit=None):
        self.params += '&q=' + urllib.parse.quote_plus(query)

        if page is not None:
            self.params += '&page=' + page
        if limit is not None:
            self.params += '&limit=' + limit

        url = self.host + '/movies' + self.params

        return self.__request__(url)
    
    """
    Displays the top level (movie and dvd) lists available in the API.
    """
    def ListsDirectory(self):
        url = self.host + '/lists' + self.params

        return self.__request__(url)

    """
    Shows the movie lists available.
    """
    def MovieListsDirectory(self):
        url = self.host + '/lists/movies' + self.params

        return self.__request__(url)

    """
    Shows the DVD lists available.
    """
    def DvdsListsDirectory(self):
        url = self.host + '/lists/dvds' + self.params

        return self.__request__(url)
