# about

quick and dirty repo to try out
* fetching data (TEI/XML) from a github repo
* parsing data and extracting training data for NER
* running NER with spacy's CLI


## run/install

* create virtual env e.g. `virutalenv env`
* activate env, e.g. `source env/bin/activate` 
* install requirements.txt, e.g. `pip install -r requirements.txt`
* start jupyter notebook `jupyter notebook` 
* run `train_from_tei_from_github`


## package model

```shell
mkdir mkdir de_ner_mpr
python -m spacy package ./output/model-best ./de_ner_mpr/ --build wheel
cd de_ner_mpr/de_MRP_NER-0.0.0/dist/
python -m spacy huggingface-hub push de_MRP_NER-0.0.0-py3-none-any.whl
```

`pip install https://huggingface.co/csae8092/de_MRP_NER/resolve/main/de_MRP_NER-any-py3-none-any.whl`

### try out online

* Click [here](https://huggingface.co/csae8092/de_MRP_NER?text=Wie+es+aber%2C+nachdem+ungeachtet+diese+Berechnung+damals+schon+bekannt+gewesen+sei%2C+doch+nur+376.754+fr.+in+Anspruch+genommen+worden+seien%2C+noch+m%C3%B6glich+sein+sollte%2C+hinterher+noch+um+43.154+fr.+an+ordentlichem+Bedarf+mehr+durchzusetzen%2C+sei+durchaus+nicht+abzusehen%2C+und+Referent+hielt+daher+den+Antrag+der+Hofkanzlei+schon+aus+diesem+Grunde+f%C3%BCr+unausf%C3%BChrbar.) to see NER on MRP model
* Click [here](https://huggingface.co/spacy/de_core_news_md?text=Wie+es+aber%2C+nachdem+ungeachtet+diese+Berechnung+damals+schon+bekannt+gewesen+sei%2C+doch+nur+376.754+fr.+in+Anspruch+genommen+worden+seien%2C+noch+m%C3%B6glich+sein+sollte%2C+hinterher+noch+um+43.154+fr.+an+ordentlichem+Bedarf+mehr+durchzusetzen%2C+sei+durchaus+nicht+abzusehen%2C+und+Referent+hielt+daher+den+Antrag+der+Hofkanzlei+schon+aus+diesem+Grunde+f%C3%BCr+unausf%C3%BChrbar.) to see NER on same sample with default spacy model


## evaluate model

```shell
python -m spacy evaluate de_core_news_sm ./dev.spacy --output eval.json
python -m spacy evaluate ./de_ner_mpr/de_MRP_NER-0.0.0/de_MRP_NER/de_MRP_NER-0.0.0 ./dev.spacy --output eval_mrp.json
```

or run pip install https://huggingface.co/csae8092/de_MRP_NER/resolve/main/de_MRP_NER-any-py3-none-any.whl and then

`python -m spacy evaluate de_MRP_NER ./dev.spacy --output eval_mrp.json`
