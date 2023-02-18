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
python -m spacy download en_core_web_trf<br />
conda install jupyter<br />
pip install cchardet<br />
pip install chardet<br />
conda install pytorch torchvision torchaudio pytorch-cuda=11.6 -c pytorch -c nvidia
# Dataset link
https://www.kaggle.com/datasets/abhinavwalia95/entity-annotated-corpus