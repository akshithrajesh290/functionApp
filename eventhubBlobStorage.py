import azure.functions as func
import logging
from azure.storage.blob import BlobClient
import os
import uuid

app = func.FunctionApp()

@app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="myeventhub",
                               connection="nmspeventhubdevv01_RootManageSharedAccessKey_EVENTHUB") 
def eventhub_triggernew(azeventhub: func.EventHubEvent):
    logging.info('Python EventHub trigger processed an event updated code updated: %s',
                azeventhub.get_body().decode('utf-8'))
    conn_string = ""
    blob_client = BlobClient.from_connection_string(
        conn_string,
        container_name="functionapp",
        blob_name=f"sample-blob-{str(uuid.uuid4())[0:5]}.txt",
    )
    blob_client.upload_blob(azeventhub.get_body().decode('utf-8'))
    logging.info('completed saving the file')

