# Custom_Entity_Extraction_Spacy3.5
Making a custom entity extraction model using spacy 3.5 <br />
# Setup environment
conda create -n ner_spacy35<br />
conda activate ner_spacy35<br />
conda install -c anaconda cudatoolkit<br />
conda install -c anaconda cudnn<br />
conda install -c anaconda pip<br />
pip install -U pip setuptools wheel<br />
pip install -U spacy[cuda-autodetect]<br />
conda install jupyter<br />
pip install cchardet<br />
pip install chardet