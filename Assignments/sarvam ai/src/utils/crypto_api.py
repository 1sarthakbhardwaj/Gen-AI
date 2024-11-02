import requests
from cachetools import TTLCache, cached

# Set up a cache with a 5-minute TTL (Time-to-Live)
cache = TTLCache(maxsize=100, ttl=300)

@cached(cache)
def fetch_crypto_price(crypto_id="bitcoin", currency="usd"):
    """
    Fetches the current price of a cryptocurrency with caching.

    :param crypto_id: The ID of the cryptocurrency (e.g., "bitcoin", "ethereum").
    :param currency: The target currency for the price (e.g., "usd", "eur").
    :return: The current price if successful, None otherwise.
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data[crypto_id][currency]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price: {e}")
        return None
