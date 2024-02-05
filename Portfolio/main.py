import requests

def get_token_price(token_symbol):
    api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={token_symbol}&vs_currencies=usd"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for errors

        data = response.json()
        # Parse and use the 'data' dictionary as needed
        print("API Response:", data)

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data: {e}")

if __name__ == "__main__":
    token_symbol = "ethereum"  # Replace with the token symbol you are interested in
    get_token_price(token_symbol)