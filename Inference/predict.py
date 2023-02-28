import spacy
import pandas as pd

nlp = spacy.load(r"E:\Work\Data_Science\Projects\Custom_NER_Spacy3.5\models\model_2\model-best")

text = str(input())

doc = nlp(text)

print(doc.to_json())

for ele in doc.to_json()['ents']:
    label = ele['label']
    start = ele['start']
    end = ele['end']
    print({'label':label, 'value':text[start:end]})
           
           