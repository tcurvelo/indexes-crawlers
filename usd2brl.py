#!/usr/bin/env python
from datetime import datetime

import requests
from exporter import export


def main():
    response = requests.get(
        "https://www.remessaonline.com.br/api/simulator?amount=1.00&inputCurrencyISOCode=USD&operationType=inbound&outputCurrencyISOCode=BRL&targetCustomerType=business"
    )
    if response.status_code == 200:
        value = response.json().get("simulation").get("tradingQuotation")
        now = datetime.utcnow()
        print(f"Currency at {now} is {value}")
        export("usd2brl", "currency", value, now)
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    main()
