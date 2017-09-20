import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
      <meta http-equiv="x-ua-compatible" content="ie=edge">
      <meta name="description" content="My favorite movies page">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Fresh Tomatoes</title>

      <!-- Bootstrap 4, jQuery, JS -->
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">

      <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
      <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>

      <!-- CSS & JS local links -->
      <link rel="stylesheet" type="text/css" href="css/theme.css">
      <script type="text/javascript" charset="utf-8" src="js/scripts.js">
      </script>

      <!-- Custom fonts from Google Fonts-->
      <link href="https://fonts.googleapis.com/css?family=Open+Sans|Cormorant+Garamond" rel="stylesheet">
</head>
"""


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24">
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <header>
      <div class="container-fluid">
        <div class="row">
          <div class="col-lg-12 mx-auto">
            <h1 class="brand-heading text-center">Fresh Tomatoes</h1>
          </div>
        </div>
      </div>
    </header>

    <main>
      <div class="container-fluid">
        <div class="row">
        {movie_tiles}
        </div>
      </div>
    </main>

  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
  <figure class="figure">
    <img src="{poster_image_url}" class="figure-img img-responsive center-block" width="220" height="342">
    <figcaption class="figure-caption">
    {movie_title}
    </figurecaption>
  </figure>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
