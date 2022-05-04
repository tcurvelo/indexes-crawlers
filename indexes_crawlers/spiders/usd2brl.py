import scrapy


class RemessaUSd2BRLSpider(scrapy.Spider):
    name = "usd2brl"
    start_urls = [
        "https://www.remessaonline.com.br/api/simulator?amount=1.00&inputCurrencyISOCode=USD&operationType=inbound&outputCurrencyISOCode=BRL&targetCustomerType=business"
    ]

    def parse(self, response, **kwargs):
        value = response.json().get("simulation").get("tradingQuotation")
        yield {"currency": value}
