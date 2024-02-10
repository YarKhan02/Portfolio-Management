import requests

from fastapi import HTTPException, status



def calculate_buy(current, new_entry):
    get_token(new_entry)

    total_coins = (new_entry.amount / new_entry.price) + current.coins

    average_price = (current.price + new_entry.price) / 2

    total_amount = current.amount + new_entry.amount

    new_entry.id = current.id
    new_entry.price = average_price
    new_entry.amount = total_amount
    new_entry.coins = total_coins
    new_entry.created_at = current.created_at



def calculate_sell(current, rm):
    get_token(rm)

    coins_to_sell = (rm.amount / rm.price)

    if coins_to_sell > current.coins:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = 'invalid amount')

    total_coins = current.coins - coins_to_sell

    average_price = (current.price + rm.price) / 2

    percent_of_coins_to_sell = coins_to_sell / current.coins

    total_amount = current.amount - (current.amount * percent_of_coins_to_sell)

    rm.id = current.id
    rm.price = average_price
    rm.amount = total_amount
    rm.coins = total_coins
    rm.created_at = current.created_at



def get_token(cypto):
    api_url = f"https://api.coingecko.com/api/v3/simple/price?ids={cypto.name}&vs_currencies=usd"

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Check for errors

        data = response.json()

    except requests.exceptions.RequestException as e:
        raise e

    cypto.price = data[next(iter(data))]['usd']