# /bin/bash

echo "download data"
python dl_rta.py

echo "convert data"
python jsonl_to_spacydoc.py

echo "train"
python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./dev.spacy

echo "eval against default german model"
python -m spacy evaluate de_core_news_sm ./dev.spacy --output eval_WRDIARIUM_DE.json

echo "eval current model"
python -m spacy evaluate ./output/model-best ./dev.spacy --output eval_WRDIARIUM.json

