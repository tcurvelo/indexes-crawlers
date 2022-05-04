import scrapy


class NumbeoSpider(scrapy.Spider):
    name = "numbeo"
    start_urls = [
        "https://www.numbeo.com/cost-of-living/compare_cities.jsp"
        "?country1=United+States&country2=Brazil&city1=New+York%2C+NY&city2=Brasilia"
    ]
    indexes = {
        "Consumer Prices": "cost_of_living_index",
        "Rent Prices": "rent_index",
        "Groceries Prices": "groceries_index",
        "Restaurant Prices": "restaurant_index",
        "Local Purchasing Power": "local_purchasing_index",
    }

    def parse(self, response, **kwargs):
        raw_indexes = (
            response.css(".table_indices_diff td")
            .xpath("normalize-space()")
            .re(
                r"((?:Consumer|Rent|Restaurant|Groceries) Prices|Local Purchasing Power) "
                r"in (.*) (?:are|is) ([\d.%]+) (lower|higher) than in ([^(]+)"
            )
        )
        for index in range(0, len(raw_indexes), 5):
            value = float(raw_indexes[index + 2].rstrip("%")) / 100
            if raw_indexes[index + 3] == "lower":
                value = 1 - value

            yield {self.indexes[raw_indexes[index]]: value}
