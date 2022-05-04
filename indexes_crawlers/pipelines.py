from datetime import datetime

from indexes_crawlers.exporter import export


class InfluxExportPipeline:
    def process_item(self, item, spider):
        now = datetime.utcnow()
        for key, value in item.items():
            export(spider.name, key, value, now)
        return item
