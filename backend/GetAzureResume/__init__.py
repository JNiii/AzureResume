import logging
import azure.functions as func
import json
import os

from azure.cosmos import CosmosClient

URL = os.environ["COSMOSDB_URI"]
KEY = os.environ["COSMOSDB_KEY"]
client = CosmosClient(URL, credential=KEY)
database = client.get_database_client("AzureResume")
container = database.get_container_client("Counter")


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    item = container.read_item(item="1", partition_key="1")
    item['count'] = item['count'] + 1
    new_item = container.replace_item(item=item, body=item)
    return func.HttpResponse(
        json.dumps(new_item),
        mimetype='application/json',
        status_code=200
        )