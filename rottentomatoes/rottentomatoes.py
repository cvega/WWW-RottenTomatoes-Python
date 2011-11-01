#!/usr/bin/env python3

import urllib.parse, urllib.request, json

class Rest(object):
    """
    RottenTomatoes API client for Python 3

    Notes: -all public methods return a json object.
           -@param not required unless otherwise specified

    @param: token (api key), required
    """

    def __init__(self, token):
        self.host   = 'http://api.rottentomatoes.com/api/public/v1.0'
        self.header = {'User-Agent':'python-WWW-RottenTomatoes/1.0'}
        self.params = '.json?apikey=' + token

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
    def box_office_movies(self, limit=None, country=None):
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
    def in_theatre_movies(self, country=None, page=None, page_limit=None):
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
    def opening_movies(self, limit=None, country=None):
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
    def up_coming_movies(self, country=None, page=None, page_limit=None):
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
    def top_rentals_dvds(self, limit=None, country=None):
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
    def current_release_dvds(self, country=None, page=None, page_limit=None):
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
    def new_release_dvds(self, country=None, page=None, page_limit=None):
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
    def up_coming_movies(self, country=None, page=None, page_limit=None):
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
    def movies_info(self, movie_id):
        url = self.host + '/movies/' + movie_id + self.params

        return self.__request__(url)

    """
    Pulls the complete movie cast for a movie

    @param: movie_id (The id number of a specific movie), required
    """
    def movies_cast(self, movie_id):
        url = self.host + '/movies/' + movie_id + '/cast' + self.params

        return self.__request__(url)

    """
    Pulls the complete movie cast for a movie

    @param: movie_id (The id number of a specific movie), required
    """
    def movies_clips(self, movie_id):
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
    def movies_reviews(self, movie_id, review_type=None, country=None, page=None, page_limit=None):
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
    def movies_similar(self, movie_id, limit=None):
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
    def movies_alias(self, movie_id, alias_type):
        
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
    def movies_search(self, query, page=None, limit=None):
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
    def lists_directory(self):
        url = self.host + '/lists' + self.params

        return self.__request__(url)

    """
    Shows the movie lists available.
    """
    def movie_lists_directory(self):
        url = self.host + '/lists/movies' + self.params

        return self.__request__(url)

    """
    Shows the DVD lists available.
    """
    def dvds_lists_directory(self):
        url = self.host + '/lists/dvds' + self.params

        return self.__request__(url)