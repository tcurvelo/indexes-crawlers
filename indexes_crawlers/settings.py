BOT_NAME = "indexes_crawlers"

SPIDER_MODULES = ["indexes_crawlers.spiders"]
NEWSPIDER_MODULE = "indexes_crawlers.spiders"

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    "indexes_crawlers.pipelines.InfluxExportPipeline": 300,
}
