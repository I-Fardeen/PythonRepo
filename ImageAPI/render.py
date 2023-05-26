from PIL import ImageTk, Image
import requests,io
response = requests.get('https://source.unsplash.com/random/600x600?cats')
con = response.content
raw_img = Image.open(io.BytesIO(con))

