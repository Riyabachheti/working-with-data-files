# Import necessary libraries
import pandas as pd
import requests

# Replace 'YOUR_API_KEY' with your actual TMDB API key
api_key = "8265bd1679663a7ea12ac168da84d2e8"
url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page=1"

# Make the GET request
response = requests.get(url)

# Convert the response to JSON
json_response = response.json()

# Get total number of pages from the initial response
total_pages = json_response['total_pages']

# Initialize an empty DataFrame to store all movie data
df = pd.DataFrame()

# Loop through all pages
for i in range(1, total_pages + 1):  # Loop from page 1 to total_pages
    # Construct the URL for the current page
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page={i}"

    # Make the GET request
    response = requests.get(url)

    # Convert the response to JSON
    json_response = response.json()

    # Extract the results
    results = json_response['results']

    # Create a temporary DataFrame for the current page with selected columns
    temp_df = pd.DataFrame(results)[['id', 'title', 'overview', 'release_date', 'popularity', 'vote_average', 'vote_count']]

    # Append the temporary DataFrame to the main DataFrame
    df = df.append(temp_df, ignore_index=True)

# Export the data to a CSV file
df.to_csv('movies.csv', index=False) # index=False prevents writing DataFrame index as a column

print("\nData exported to movies.csv")
