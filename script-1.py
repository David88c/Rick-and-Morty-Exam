import requests
import pprint
import csv

characters=[] # Initialize an empty list to store character information
body=requests.get("https://rickandmortyapi.com/api/character/?species=human&status=alive")# Make a GET request to the Rick and Morty API to fetch characters

for character in body.json()["results"]:
    if character["origin"]["name"].startswith("Earth"):
        characters.append({
           "name": character["name"],
           "location": character["location"]["name"],
           "image": character["image"]
        })

keys = characters[0].keys()# Get the keys from the first dictionary in the characters list

# Open a new CSV file called "characters.csv" in write mode
with open("characters.csv", "w", newline='') as f: 
    dict_writer = csv.DictWriter(f, keys)# Create a DictWriter object with the file and keys
    dict_writer.writeheader()# Write the header row to the CSV file
    dict_writer.writerows(characters)# Write the rows of character data to the CSV file