import pymongo

url = 'mongodb+srv://Harsh:Harsh1998#@atlaschat.nh2jjcm.mongodb.net/'

client = pymongo.MongoClient(url)
db = client['Atlaschat']
