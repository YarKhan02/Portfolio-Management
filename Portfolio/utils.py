import requests



def calculate(current, new_entry):
    total_coins = (new_entry['amount'] / new_entry['price']) + current.coins

    average_price = (current.price + new_entry['price']) / 2

    total_amount = current.amount + new_entry['amount']

    current.price = average_price
    current.amount = total_amount
    current.coins = total_coins



def get_token(add):
    api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={add.name}&vs_currencies=usd"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for errors

        data = response.json()

    except requests.exceptions.RequestException as e:
        raise e

    result_dict = {'name': next(iter(data)), 'price': data[next(iter(data))]['usd'], 'amount': add.amount}

    return result_dict
