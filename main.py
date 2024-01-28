import requests

# Get user input + create list + variable
first_part = input("Enter the first part of the message: ")
th = input("Enter the word to search for synonyms: ")
last_part = input("Enter the last part of the message: ")

# Get synonyms from the Merriam-Webster Thesaurus API
url = "https://www.dictionaryapi.com/api/v3/references/thesaurus/json/" + th + "key=  ENTER KEY  "
try:
 response = requests.get(url)
 response.raise_for_status()
except requests.exceptions.HTTPError as errh:
 print ("HTTP Error:",errh)
except requests.exceptions.ConnectionError as errc:
 print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
 print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
 print ("Something went wrong",err)

data = response.json()

# Access the synonyms
synonyms = data['meta'][0]['syns'][0]

# Print the synonyms
for syn in synonyms:
 print(syn)
