import os

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

TOKEN = os.getenv("INFLUX_TOKEN")
BUCKET = os.getenv("INFLUX_BUCKET")
ORG = os.getenv("INFLUX_ORG")
URL = os.getenv("INFLUX_URL")


def export(datasource, field, value, timestamp):
    with InfluxDBClient(url=URL, token=TOKEN, org=ORG) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
        point = Point(datasource).field(field, value).time(timestamp, WritePrecision.NS)
        write_api.write(BUCKET, ORG, point)
        write_api.close()
