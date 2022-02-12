# Project Milestone One
This is a simple website that uses API calls to dynamically fetch and display movie information

# Libraries Used
1. **flask**, to run the web server
2. **requests**, to interact with APIs
3. **dotenv**, to interact with a .env file containing api keys

# APIs used
1. **TMDB**, to fetch movie title, tagline, genres, and poster image
2. **MediaWiki**, to fetch the movie's wikipedia link

# Technical Issues
1. The MediaWiki API is pretty difficult to use, it took a while to find out how to search directly for pages, google helped me out a lot
2. Subscripting the MediaWiki response was also a pain, as one key held a list with one element containing a bunch of other keys, I copied the response into an IDE to analyze it and finally figured it out
