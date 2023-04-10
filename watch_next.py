# NOTE TO REVIEWER: There is a bit of confusion in the instructions between
# 'Your task is to create a function to return which movies' (multiple proposal)
# and 'The function should take in the description as a parameter and return
# the title of the most similar movies' (single proposal). We proposed two alternatives;
# one that will return a single title with the highest matching and a second one that
# could return either a single title or three top picks. I have a preference for Option 2 for
# flexibility.

import spacy

# Import medium model for higher accuracy
nlp = spacy.load('en_core_web_md')

# Initialize what the user has just watched
last_movie_name = 'Planet Hulk'
last_movie_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# OPTION 1: function that return a single title
def next_movie_proposal (last_movie_description: str)->str:

    # Read the file and store the description of possible movies
    with open('movies.txt', 'r') as file:
        options = file.readlines()

    description = nlp(last_movie_description)

    # Iterate through the list and keep track of the highest similarity and its corresponding index
    highest_index = 0
    highest_similarity = 0
    for count, option in enumerate(options):
        similarity = nlp(option).similarity(description)
        if similarity > highest_similarity:
            highest_similarity = similarity
            highest_index = count

    # Return the first 7 characters so that it returns the movie name only
    return f'After watching {last_movie_name}, we think you may like watching {options[highest_index][:7]}.'

print(next_movie_proposal(last_movie_description))

# OPTION 2: function that return a single or multiple title (with minimal changes)
def next_movies_proposal (last_movie_description: str)->str:

    # Read the file and store the description of possible movies
    with open('movies.txt', 'r') as file:
        options = file.readlines()

    description = nlp(last_movie_description)

    # Initialize nested list where we will store: count, option, similarity
    list_proposals = []
    for count, option in enumerate(options):
        similarity = nlp(option).similarity(description)
        list_proposals.append([count, option, similarity])

    # Sort list by similarity in increasing order
    new_l = sorted(list_proposals, key=lambda item:item[2], reverse=True)

    # Return the first 7 characters so that it returns the movie name only
    return f'After watching {last_movie_name}, we think you may like watching {new_l[0][1][:7]}.'
    # If multiple titles: return f'After watching {last_movie_name}, we think you may like watching {new_l[0][1][:7]}, {new_l[1][1][:7]}, or {new_l[2][1][:7]}.'

print(next_movies_proposal(last_movie_description))

