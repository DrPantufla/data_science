import requests
import json

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=LLljvESaXs7nIlbBRmfAuKp7y9ZgidjPYdeGxa74"

payload = json.dumps({})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

#1

datos =json.loads(response.text)["photos"][:25]

#2

url_img = [diccionario["img_src"] for diccionario in datos]

#3

def build_web_page(lista):
    html = "<html>\n<head>\n</head>\n<body>\n<ul></ul>\n</body>\n</html>"
    img_html=""
    for imagen in lista:
        img_html += "<li><img src=\"{}\"></li>\n".format(imagen) 
    
    html = "<html>\n<head>\n</head>\n<body>\n<ul>{}</ul>\n</body>\n</html>".format(img_html)
    with open("imagenes_nasa.html", "w") as f:
        f.write(html)
    
build_web_page(url_img)