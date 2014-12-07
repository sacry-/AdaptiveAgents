AdaptiveAgents
==============

Lernende Agenten

- <a href="https://pub.informatik.haw-hamburg.de/home/pub/prof/neitzke_michael/PO/Lernende%20Agenten/" target="_blank">Neitzke Pub</a>
- <a href="http://digbib.ubka.uni-karlsruhe.de/eva/ira/2006/5" target="_blank">Karlsruhe Bericht</a>
- <a href="http://www.nltk.org/" target="_blank">Python NLTK</a>

### Setup ###
	
Parsing and Text Processing
```python
# Python 2.7.x used
# Python NLTK 3.0 http://www.nltk.org/install.html
# Numpy + Scipy 
pip install numpy
pip install scipy
pip install treelib
# Remove Markup from Strings
git clone https://github.com/daddyd/dewiki.git
cd dewiki/
python setup.py install
pip install beautifulsoup4
# English dictionary
brew install enchant
pip install pyenchant
# Pos Tagging Speed up
# normally: pip install -U textblob-aptagger
pip install -U git+https://github.com/sloria/textblob-aptagger.git@dev
```

Infrastructure
```python
# Install Redis
brew install redis
pip install redis-py
pip install redisdl
# Start server and then client
# redis-server
# redis-cli
```

Visualization

```python
# TODO Graph Visualization with graph-tool ~> http://graph-tool.skewed.de/ (python)
pip install pygraphviz
```

Artifacts
```python
# Install ElasticSearch
brew install elasticsearch
brew install logstash
# Download Kibana from official source and put it to your WebServer System, 
# plenty of documentation available
# ES Kopf Plugin
git clone https://github.com/lmenezes/elasticsearch-kopf.git
```

# Our plan #
<s>Phonetik und Phonologie</s><br />
1. Morphologie ist die Lehre von der Zusammensetzung und Formbildung  der Wörter.<br />
2. Syntax werden die von den Wörtern gebildeten Strukturen zusammengefasst. Hierzu zählen die Grammatiken.<br />
3. Semantik - (Lexikalisch - Bedeutung auf Wortebene) + (Kompositionell - Bedeutung von Sätzen/Abschnitten)<br />
<s>Pragmatik und Diskurs</s><br />

<a href="https://gist.github.com/sacry-/31e780c9b87d28014cb9" target="_blank">NLP Mitschrift</a>

### Usage ###
coming soon

# Notes #
coming soon
