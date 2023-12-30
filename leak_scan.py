import requests
import json
import itertools
import os

class PostmanCollection:

   def __init__(self, data):
       self.uid = data["uid"]
       self.name = data["name"]
       self.item = data["item"]

def get_postman_collections(query):
   """Busca coleções Postman usando a API."""
   api_key = os.environ.get("POSTMAN_API_KEY")
   headers = {"X-Api-Key": api_key}
   url = f"https://api.getpostman.com/collections?q={query}"
   response = requests.get(url, headers=headers)
   response.raise_for_status()  # Levanta exceção em caso de erro HTTP
   data = json.loads(response.text)
   return [PostmanCollection(collection) for collection in data["results"]]

def search_for_leaks(collection):
   """Busca por vazamentos de informações confidenciais em uma coleção."""
   for item in collection.item:
       try:
           request = item["request"]
           url = request["url"]
           headers = request.get("header", [])
           body = request.get("body")
           for pattern in confidential_patterns:
               if pattern in url or pattern in headers or pattern in body:
                   print(f"Potential leak in {'URL' if pattern in url else 'headers' if pattern in headers else 'body'}: {url}")
       except KeyError:
           pass  # Trata casos de dados ausentes

def banner():
   print("""
    (__)
   (oo)
  /------\/
* / |    ||
   ~~   ~~

**P0STM4N Detect Leaks**

 **Por 0x5FE**

Uma ferramenta que ajuda a detectar
vazamentos de informações confidenciais
em coleções Postman.
""")


if __name__ == "__main__":
   # Define confidential patterns to search for
   confidential_patterns = [
       "password",
       "api_key",
       "access_token",
       "secret",
   ]

   banner()

   # Busca por coleções matching the query
   collections = get_postman_collections("company_name")

   for collection in collections:
       search_for_leaks(collection)
