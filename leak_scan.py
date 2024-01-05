import requests
import json
import os
from typing import List, Dict
import argparse


class PostmanCollection:
    def __init__(self, data: Dict) -> None:
        self.uid = data["uid"]
        self.name = data["name"]
        self.item = data["item"]

    def __str__(self) -> str:
        return f"PostmanCollection(uid={self.uid}, name={self.name})"


def fetch_collections(query: str) -> List[PostmanCollection]:
    """Busca coleções Postman usando a API."""
    api_key = os.environ.get("POSTMAN_API_KEY")
    headers = {"X-Api-Key": api_key}
    url = f"https://api.getpostman.com/collections?q={query}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = json.loads(response.text)
    return [PostmanCollection(collection) for collection in data["results"]]


def search_for_leaks(collection: PostmanCollection) -> None:
    """Busca por vazamentos de informações confidenciais em uma coleção."""
    logger = logging.getLogger(__name__)
    for item in collection.item:
        try:
            request = item["request"]
            url = request["url"]
            headers = request.get("header", [])
            body = request.get("body")

            for pattern in confidential_patterns:
                if pattern in url or pattern in headers or pattern in body:
                    logger.warning(
                        f"Potential leak in {_find_leak_location(pattern, url, headers, body)}: {url}"
                    )
        except KeyError as e:
            logger.error(f"Erro ao acessar dados da requisição: {e}")

def banner():
   print("""
    (__)
   (oo)
  /------\/
* / |    ||
   ~~   ~~

**P0STM4N Detect Leaks**

 **Por 0x5FE**
 
""")


def _find_leak_location(pattern: str, url: str, headers: List[str], body: str) -> str:
    if pattern in url:
        return "URL"
    elif pattern in headers:
        return "headers"
    elif pattern in body:
        return "body"
    else:
        return "unknown"


def main():
    parser = argparse.ArgumentParser(description="Detecta vazamentos de informações confidenciais em coleções Postman.")
    parser.add_argument("--query", type=str, help="Palavra-chave para pesquisar coleções.")
    parser.add_argument(
        "--confidential-patterns",
        type=str,
        help="Lista de padrões de informações confidenciais a serem pesquisados.",
    )
    args = parser.parse_args()

    # Define confidential patterns
    confidential_patterns = set(args.confidential_patterns.split(","))

    # Busca por coleções matching the query
    collections = fetch_collections(args.query)

    # Procura por vazamentos em cada coleção
    for collection in collections:
        search_for_leaks(collection)

if __name__ == "__main__":
    main()
