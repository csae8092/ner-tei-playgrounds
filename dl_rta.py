import os
from nerdpool_client import NerdPoolClient

DATA_SET = "MONNER1"

url = f"http://127.0.0.1:8000/api/ner-sample/?ner_source__title={DATA_SET}"
client = NerdPoolClient()
client.dump_to_train_eval(url, file_name_prefix=f"{DATA_SET}__", split=10)