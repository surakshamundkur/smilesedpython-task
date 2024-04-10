movies = ("Casablanca", 9.7, "The Godfather", 9.2, "The Shawshank Redemption", 9.3)

#1.	Print the average rating:
ratings = movies[1::2] #slices the tuple starting from index 1 (which is the first rating) and extracts every second element (2 as the step), resulting in a list of ratings.
average_rating = sum(ratings) / len(ratings)
print(f"Average rating: {average_rating:.1f}")

#2.	Extract the movie with the highest rating:
ratings = movies[1::2]
index_highest_rating = ratings.index(max(ratings))
highest_rated_movie = movies[index_highest_rating * 2] #Since each movie title is located at even indices (0, 2, 4, ...), we multiply the index of the highest rating by 2 to get the corresponding movie index.
print(f"Highest rated movie: {highest_rated_movie}")

#3.	Create a new tuple with only the movie titles:
movie_titles = movies[0::2] #slices the movies tuple starting from index 0 and extracts every second element (2 as the step), which corresponds to the movie titles
movie_titles_tuple = tuple(movie_titles)
print(f"Movie titles: {movie_titles_tuple}")