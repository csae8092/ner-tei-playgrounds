import warnings
import json
import spacy
from spacy.tokens import DocBin

DATA_SET = "RTA"
db_train = DocBin()
db_eval = DocBin()
nlp = spacy.blank('de')
fails = 0
train_sample_count = 0
eval_sample_count = 0

for x in ['eval', 'train']:
    input_file = f"{DATA_SET}__{x}.jsonl"
    with open(input_file) as f:
        for line in f:
            try:
                data = json.loads(line.strip())
            except:
                continue
            text = data['text']
            entities = data['entities']
            doc = nlp.make_doc(text)
            ents = []
            for start, end, label in entities:
                span = doc.char_span(start, end, label=label)
                if span is None:
                    # msg = f"Skipping entity [{start}, {end}, {label}] in the following text because the character span '{doc.text[start:end]}' does not align with token boundaries:\n\n{repr(text)}\n"
                    # warnings.warn(msg)
                    fails += 1
                else:
                    ents.append(span)
            try:
                doc.ents = ents
                if x == 'train':
                    db_train.add(doc)
                    train_sample_count += 1
                else:
                    db_eval.add(doc)
                    eval_sample_count += 1
            except ValueError:
                continue
        db_train.to_disk(f'train.spacy')
        db_eval.to_disk(f'dev.spacy')
print(
    f"fails: {fails}; train: {train_sample_count}; eval: {eval_sample_count}"
)