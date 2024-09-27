Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Read the contents of the songs dataset file and return the data in a dictionary format
... import random
... def data_to_dict(filename, header):
...     # Open file to access data
...     data_file = open(filename, "r")
... 
...     # If file has a header line read it and save it
...     header_line = ""
...     if header:  
...         header_line = data_file.readline().strip() # Read the header line of the file to extract attributes
... 
...     # Initialize an empty dictionary to store the data
...     data_dict = {}
...     
...     # Iterate over each line in the data file
...     for line in data_file:
... 
...         # Remove leading and trailing whitespaces, and split the line into a list using commas
...         line = line.strip().split(",")
...         
...         # Get the artist name
...         artist = line[1]
...         # Remove the artist name from the details since it is used as the key
...         line.pop(1)
...         # If artist in dictionary add line value list
...         if artist in data_dict:
...             data_dict[artist].append(line)
...         else: # New type found
...             data_dict[artist] = [line]
...       
...      # Close the file
...     data_file.close()
... 
...     # Return the data organinzed in a dictionary
    return data_dict

########################################################
# uncomment the following line to display the data dictionary
#print(data_to_dict("SpotifySongs-Dataset.csv", True))
########################################################
# Add your solution here
########################################################
property_index = {
    "Danceability": 0,
    "Energy": 1,
    "Key": 2,
    "Loudness": 3,
    "Liveness": 4,
    "Valence": 5,
    "Tempo": 6,
    "Duration_ms": 7
}
def count_artists_and_songs(data_dict):
    num_artists = len(data_dict)
    num_songs = sum(len(songs) for songs in data_dict.values())
    return num_artists, num_songs

def select_random_song(data_dict):
    random_artist = random.choice(list(data_dict.keys()))
    random_song_index = random.randint(0, len(data_dict[random_artist]) - 1)
    random_song = data_dict[random_artist][random_song_index]
    return random_artist, random_song

def calculate_average_properties(data_dict):
    avg_properties = {}
    for artist, songs in data_dict.items():
        properties_sum = [0] * (len(songs[0]) - 1)
        for song in songs:
            for i in range(len(properties_sum)):
                properties_sum[i] += float(song[i + 1])
        avg_properties[artist] = []
        for sum_val in properties_sum:
            avg_properties[artist].append(sum_val // len(songs))
    return avg_properties

def song_with_highest_popularity(data_dict):
    max_popularity = -1
    max_popularity_song = None
    for artist, songs in data_dict.items():
        for song in songs:
            popularity = float(song[1])
            if popularity > max_popularity:
                max_popularity = popularity
                max_popularity_song = (artist, song)
    return max_popularity_song

def song_with_shortest_duration(data_dict):
    min_duration = float('inf')
    min_duration_song = None
    for artist, songs in data_dict.items():
        for song in songs:
            duration = int(song[-1])
            if duration < min_duration:
                min_duration = duration
                min_duration_song = (artist, song)
    return min_duration_song

def song_with_longest_duration(data_dict):
    max_duration = -1
    max_duration_song = None
    for artist, songs in data_dict.items():
        for song in songs:
            duration = int(song[-1])
            if duration > max_duration:
                max_duration = duration
                max_duration_song = (artist, song)
    return max_duration_song

def most_common_key(data_dict):
    key_counts = {}

    # Count occurrences of each key
    for songs in data_dict.values():
        for song in songs:
            key = song[4]  # Extract the key
            if key.isdigit() or key == "-1":  # Check if the value is a valid integer or equals -1
                key = int(key)
                if key != -1:  # If a valid key is detected
                    key_counts[key] = key_counts.get(key, 0) + 1

    if not key_counts:  # If no valid keys found
        return None, 0 

    # Find the most common key
    most_common_key = max(key_counts, key=key_counts.get)
    count = key_counts[most_common_key]

    return most_common_key, count

def find_artist_by_property(data_dict, property_name, highest=True):
    property_index = {"Danceability": 1, "Energy": 2, "Key": 3, "Loudness": 4, "Liveness": 5, "Valence": 6, "Tempo": 7, "Duration_ms": 8}
    artists_avg_properties = calculate_average_properties(data_dict)
    best_artist = None
    best_value = float('-inf') if highest else float('inf')
    
    for artist_name, properties in artists_avg_properties.items():
        value = properties[property_index.get(property_name, -1) - 1]
        if highest:
            if value > best_value:
                best_value = value
                best_artist = artist_name
        else:
            if value < best_value:
                best_value = value
                best_artist = artist_name
                
    return best_artist

def find_artists_by_properties(data_dict, properties):
    property_index = {"Danceability": 1, "Energy": 2, "Key": 3, "Loudness": 4, "Liveness": 5, "Valence": 6, "Tempo": 7, "Duration_ms": 8}
    artists_avg_properties = calculate_average_properties(data_dict)
    
    results = {}
    
    for property_name in properties:
        highest_artist = find_artist_by_property(data_dict, property_name, highest=True)
        lowest_artist = find_artist_by_property(data_dict, property_name, highest=False)
        
        results[property_name] = {"highest": highest_artist, "lowest": lowest_artist}
    
    return results

# Main function
def main():
   filename = "SpotifySongs-Dataset.csv"
   data_dict = data_to_dict(filename, True)




   # Task 1 and 2: Counting artists and songs
   num_artists, num_songs = count_artists_and_songs(data_dict)
   print("Number of artists:", num_artists)
   print("Number of songs:", num_songs)




   # Task 3: Selecting a random song and displaying its information
   random_artist, random_song = select_random_song(data_dict)
   print("\nRandom Song:")
   print("Artist:", random_artist)
   print("Song:", random_song[0])
   print("Popularity:", random_song[1])
   print("Danceability:", random_song[2])
   print("Energy:", random_song[3])
   print("Key:", random_song[4])
   print("Loudness:", random_song[5])
   print("Liveness:", random_song[6])
   print("Valence:", random_song[7])
   print("Tempo:", random_song[8])
   if len(random_song) >= 10:
       print("Duration:", random_song[9])
   else:
       print("Duration: Not Available")




   # Task 4: Calculating average properties per artist
   avg_properties = calculate_average_properties(data_dict)
   print("\nAverage Properties per Artist:")
   for artist, properties in avg_properties.items():
       print(artist + ":", end=" ")
       for property_name, value in zip(property_index.keys(), properties):
           print(property_name + ":", value, end=" ")
       print()  # Move to the next line for the next artist




   # Task 5: Song with highest popularity
   max_popularity_song = song_with_highest_popularity(data_dict)
   print("\nSong with Highest Popularity:")
   print("Artist:", max_popularity_song[0])
   print("Song:", max_popularity_song[1][0])
   print("Popularity:", max_popularity_song[1][2])




   # Task 6: Song with shortest duration
   shortest_duration_song = song_with_shortest_duration(data_dict)
   print("\nSong with Shortest Duration:")
   if shortest_duration_song is not None:
       print("Artist:", shortest_duration_song[0])
       print("Song:", shortest_duration_song[1][0])
       if len(shortest_duration_song[1]) >= 10:
           print("Duration:", shortest_duration_song[1][9])
       else:
           print("Duration: Not Available")
   else:
       print("No song found")




   # Task 7: Song with longest duration
   longest_duration_song = song_with_longest_duration(data_dict)
   print("\nSong with Longest Duration:")
   if longest_duration_song is not None:
       print("Artist:", longest_duration_song[0])
       print("Song:", longest_duration_song[1][0])
       if len(longest_duration_song[1]) >= 10:
           print("Duration:", longest_duration_song[1][9])
       else:
           print("Duration: Not Available")
   else:
       print("No song found")
   # Task 8: Most common key used in songs
   most_common_key_value = most_common_key(data_dict)
   print("\nMost Common Key Used in Songs:", most_common_key_value)

   # Task 9: Finding artist by property
   properties_to_analyze = ["Popularity", "Danceability", "Energy", "Key", "Loudness", "Liveness", "Valence", "Tempo", "Duration_ms"]
   # Find artists with highest and lowest average values for each property
   artists_by_properties = find_artists_by_properties(data_dict, properties_to_analyze)
   # Print the results
   for property_name, artists in artists_by_properties.items():
       print(f"Artist with highest {property_name} average: {artists['highest']}")
       print(f"Artist with lowest {property_name} average: {artists['lowest']}")
       print()

main()

