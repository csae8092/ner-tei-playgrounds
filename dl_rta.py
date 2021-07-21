import os
from nerdpool_client import NerdPoolClient

DATA_SET = "RTA"

url = f"https://nerdpool-api.acdh-dev.oeaw.ac.at/api/ner-sample/?format=json&ner_ent_type__contains=&ner_source__title={DATA_SET}"
client = NerdPoolClient()
client.dump_to_train_eval(url, file_name_prefix=f"{DATA_SET}__", split=10)