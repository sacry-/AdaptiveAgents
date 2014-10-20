AdaptiveAgents
==============

Lernende Agenten

- <a href="https://pub.informatik.haw-hamburg.de/home/pub/prof/neitzke_michael/PO/Lernende%20Agenten/" target="_blank">Neitzke Pub</a>
- <a href="http://digbib.ubka.uni-karlsruhe.de/eva/ira/2006/5" target="_blank">Karlsruhe Bericht</a>
- <a href="http://www.nltk.org/" target="_blank">Python NLTK</a>


Technologies:
	- Python NLTK
	- rdflib? (for owl)

Database:
	- nosql dbs / Graph dbs

Graph Visualization:
	http://graph-tool.skewed.de/ (python)

BA Arbeit: erwin.lang@haw-hamburg.de

### Setup ###

```bash
# Python NLTK http://www.nltk.org/install.html
# Numpy + Scipy 
pip install numpy
pip install scipy
# Remove Markup from Strings
git clone https://github.com/daddyd/dewiki.git
cd dewiki/
python setup.py install
# Install ElasticSearch
brew install elasticsearch
brew install logstash
# Download Kibana from official source and put it to your WebServer System, plenty of documentation available
# ES Kopf Plugin
git clone https://github.com/lmenezes/elasticsearch-kopf.git
```

# Plan #
<s>Phonetik und Phonologie</s>
1. Morphologie ist die Lehre von der Zusammensetzung und Formbildung  der Wörter.
2. Syntax werden die von den Wörtern gebildeten Strukturen zusammengefasst. Hierzu zählen die Grammatiken.
3. Semantik - (Lexikalisch - Bedeutung auf Wortebene) + (Kompositionell - Bedeutung von Sätzen/Abschnitten)
<s>Pragmatik und Diskurs</s>

### Usage ###
coming soon

# Notes #
coming soon

# Mitschrift #

### Allgemein ###

***Morphologie***
*Morpheme* sind die kleinsten Einheiten mit Bedeutung in einer Sprache. Zwei Klassen: Stämme und Affixe.

*Stemming* - bezeichnet das Zurückführen eines Wortes auf seinen Wortstamm.
Lemmatisierung das Wort wird auf eine in der Sprache vorhandene Grundform zurückgeführt, wie z.B. in Lexika auch *Lemma*. z.B. „lachte“ -> „lachen“.

|>  Kombination aus Regeln (z.B. "ing" -> empty) und einem Lexikon.

***Syntax - Wortarten und Konstituenten***

*POS Tagging* Part-Of-Speech - Wortart eines Wortes hat erheblichen Einfluss (hilfreich beim Stemming)
Synonym: *part-of-speech, POS, word class, morphological class, lexical tag*

| Klassische  | Wortarten   |
|-------------|-------------|
| Pronomen    | Adjektiv    |
| Präposition | Adverb      |
| Nomen       | Konjunktion |
| Verb        | Artikel     |

*Tagsets* - Penn Treebank mit 45, Brown corpus mit 87, CLAWS-Tagger - C7 tagset mit 146 -> morphologische und syntaktische Eigenschaften (Mehrzahlbildung)

*Konstituent* - Gruppe von Wörter kann sich wie ein Wort verhalten. z.B. „das alte Haus“. 
*Chunking* - Erkennung wird als Chunking bezeichnet.

*Nominalphrase* - (NP, Noun Phrase) besteht aus einem Substantiv (Head) und Modifiern und Determinern (Artikel). Modifier ändern die Bedeutung des Substantivs im jeweiligen Zusammenhang oder spezifizieren sie (meist Adjektive).

*Verbalphrase* - (VP, Verb Phrase) besteht aus einem Verb, dem Head der Verbalphrase, und einer Reihe möglicher anderer Konstituenten.

*Regular Expressions* (regex) sind Ausdrücke, die Klassen von Zeichenfolgen angeben. Formal handelt es sich um eine algebraische Notation für Mengen von Zeichenfolgen.

*Parsing-Algorithmen* - Syntaktisches Parsen: top-down, bottom-up, chart-basiert

*Earley Algorithmus* - Laufzeit O(n) für LR(k)-Grammatiken, O(n^2) für nicht mehrdeutige nicht-LR(k)-Grammatiken und O(n^3) sonst.

***Semantik*** "Inhaltliches Verständnis"

*Semantische Analyse* -Bedeutungsrepräsentation (meaning representation) muss der linguistischen Struktur zugeordnet werden.

1. Verifizierbarkeit - Die Möglichkeit des Vergleichs einer Aussage über einen Sachverhalt mit der Modellierung dieses Sachverhalts in der Wissensbasis.
2. Eindeutigkeit - Eine Repräsentation muss eine einzige eindeutige Interpretation besitzen. (Mehrdeutigkeiten auflösen)
3. Kanonische Form - gleiche Aussagen in unterschiedlichen Repräsentationen werden in eine kanonische Form überführt z.B. „In diesem Lokal gibt es vegetarisches Essen“ und „Dieses Lokal bietet vegetarische Gerichte an“ -> Dieses Lokal + Vegetarisches Essen

*Prädikat-Argument-Strukturen* (predicate-argument structures) - legen Beziehungen zwischen den Konstituenten eines Satzes fest. Den formalen Rahmen dieser Beziehungen bildet die Grammatik.

*Linking* - Zum einen nehmen bestimmte Konstituenten an bestimmten Stellen im Satz auf der inhaltlichen Ebene bestimmte Rollen ein. Die Analyse solcher Zusammenhänge bezeichnet man als Linking. Anwendung: Informationsextraktion im Rahmen des Information Retrieval oder Text Mining, weil nach der Erkennung von semantischem Subjekt und Objekt Fragen der Art „Wer hat was mit welchem Objekt getan?“ beantwortet werden können.

***Lexikalische Semantik*** - Lexem und das Lexikon

*Lexem* - bezeichnet man eine Kombination aus Form (orthographisch und phonologisch) und Bedeutung auf Wortebene, sozusagen ein „lexikalisches Morphem“. Der Bedeutungs-Teil eines Lexems heißt *Sinn* (Sense).

*Lexikon* - Liste von Lexemen (z.B. WordNet), Einträge müssen zueinander in Beziehung gesetzt werden für die Folgerung von inhaltlichem Wissen.

*Homonymie* - Wörter haben dieselbe Form, aber unterschiedliche Bedeutungen, zum Beispiel „Bank“.
*Polysemie* - Unterschiedliche, aber verwandte oder auf einen gemeinsamen Ursprung zurückzuführende Bedeutungen: „Horn“ als Berg, Instrument, Gebäck.<br />
*Synonymie* - Verschiedene Lexeme mit gleicher Bedeutung: „Streichholz“, „Zündholz“.<br />
*Antonymie* - Lexeme mit gegensätzlicher Bedeutung: „groß“, „klein“.<br />
*Hyponymie* - Klassen- und Unterklassenbildung: „Auto“ ↔ „Fahrzeug“.

### Methoden des statistischen Text Mining ###

*Korpus*,*Corpus* - Referenzquelltext auf dem Methoden trainiert werden können, zusätzliche Information wie POS-Tags, Syntaxtrees etc. enthalten; Brown Corpus, Lancaster-Oslo-Bergen Corpus, Penn Treebank, Canadian Hansard

*Worttoken* - Anazhl der Wörter (in einem Satz/Paragraphen/Korpus ...)

*Worttypen* - Anazhl der voneinander verschiedener Wörter (in einem Satz/Paragraphen/Korpus ...)

*Durchchnittliche Häufigkeit eines Wortes* - ![#Token/#Typen](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Cfrac%20%7BAnazahl%5C%2C%20von%5C%2C%20Worttoken%7D%20%7BAnzahl%5C%2C%20von%5C%2C%20Worttypen%7D), ein Indikator für die Wortreichheit des Textes, Vergleiche Tom Sawyer mit einem wissenschaftlichen Text

*Zipf's Gesetz* - Zipf's Gesetz ist eine mathematische Approximation der Beobachtung, dass einige weniger Worte viel öfter in einem Text erscheinen als alle restlichen Wörter. Sei *f(w)* die Frequenz und *r(w)* der Häufigkeitsrang des Wortes, dann besagt Zipf's Gesetz, dass das Produkt beider konstant ist, ![Zipf's Gesetz](http://latex.codecogs.com/svg.latex?%5Cinline%20f%28w%29%20r%28w%29%20=%20const.). In anderen Worten heißt das, dass das zehnthäufigste Wort fünfmal häufiger vorkommtals das 50st-häufigste Wort. Mandelbrot entwickelte in den 1950er eine bessere Approximation des Zipf's Gesetzes.

*Kollokationen* - Ausdrücke mit zwei oder mehr Wörtern die gemeinsam einen gesonderten Sinn ergeben, bsp. *Schwarzes Brett* 

*Erkennung von Kollokationen durch Häufigkeit* - Kollokationen werden anhand wiederkehrenden Wortgruppen erkannt. Dabei bieten sich Wortklassensequenzen zur Erkennung an. Zum Beispiel wird "New York City" durch die POS-Tags ![New York City Pos-Tag](http://latex.codecogs.com/svg.latex?%5Cinline%20%5BN%5C!N,%20N%5C!N,%20N%5C!N%5D) erkannt. Diese Methode erkennt jedoch auch Phrasen wie *letzten Abend* als Kollokation. Daher bietet sich diese Methode für feste Phrasen wie *Bundeskanzler Schröder* an.

**Erkennung von Kollokationen durch Mittelwert und Streuung** - Sollen zwei Wörter (z.B. *nahm* und *Abschied*) als Kollokation erkannt werden, bietet es sich an die mittleren Abstände zwischen den Worten und die Streuung dieser Abstande zu betrachten. Paare mit geriger Standardabweichung und einem Mittelwert > 1 werden als Kollokationen erkannt. Trotzdem werden dennoch einige Wortpaare aufgrund ihrer schieren Käufigkeit als Kollokation erkannt. Durch einen Signifikanztest (T-Test/Chi-Quadrat-Test) können solche Fälle eliminiert werden.

Durchschnitt der Abstände: ![enter image description here](http://latex.codecogs.com/svg.latex?%5Cmu%20%3D%20%5Cfrac%20%7B%5Csum_%7Bi%3D1%7D%5E%7BN%7D%20d_i%7D%20%7BN%7D)

Streuung: ![enter image description here](http://latex.codecogs.com/svg.latex?%5Csigma%20=%20%5Csqrt%7B%5Cfrac%20%7B%5Csum_%7Bi=1%7D%5E%7BN%7D%20%28d_i%20-%20%5Cmu%29%5E%7B2%7D%7D%20%7BN%20-1%7D%7D)

*Theorem von Bayes* - Oft ist die Wahrscheinlichkeit ![enter image description here](http://latex.codecogs.com/gif.latex?%5Cinline%20P%28Ereignis%7CUrsache%29) bekannt, während die
Wahrscheinlichkeit ![enter image description here](http://latex.codecogs.com/gif.latex?%5Cinline%20P%28Ursache%7CEreignis%29) gesucht ist. Das Theorem von Bayes ermöglicht die Berechnung, ob die Ursache gegeben dem vorliegenden Ergebnis zutrifft oder nicht.
![enter image description here](http://latex.codecogs.com/gif.latex?%5Cinline%20P%28U%7CE%29%20=%20%5Cfrac%20%7BP%28E%7CU%29P%28U%29%7D%20%7BP%28E%29%7D)
Das Theorem von Bayes ist zum Beispiel zur Spamfilterung von Emails sehr nützlich.


**n-Gramm Modelle** - Dient bei Sprachverarbeitung dazu die Wahrscheinlichkeit des n-ten Wortes aus den n-1 vorherigen Worten zu berechnen. Speziell: 2:Bigramm, 3:Trigramm, 4: Tetragramm. Ein Bigramm eines Textes ordnet jedem Wort zu wie oft ein anderes Wort als dessen Nachfolger auftaucht. Z.B. gilt ![enter image description here](http://latex.codecogs.com/svg.latex?%5Cinline%20P%28%22Film%22%7C%22Ich%22%29%20%3C%20P%28%22gehe%22%7C%22Ich%22%29).

![enter image description here](http://latex.codecogs.com/svg.latex?%5Cinline%20P%28w_i%7Cw_%7Bi-1%7D,w_%7Bi-2%7D,...w_%7Bi-N%7D%29) - Die Wahscheinlichkeit, dass ![enter image description here](http://latex.codecogs.com/svg.latex?%5Cinline%20w_i) nach den n-Worten davor vorkommt.

Die Maximum-Likelihood-Methode bestimmt aus deer Anzahl der Vorkommen der n-Gramme ihre Wahrscheinlichkeiten. Da aber oft 0 als Ergebnis vorkommt und dadurch Produkte zu 0 zusammenfallen, wird noch Smoothing eingesetzt, was das Sinken der Wahscheinlichkeit begrenzt. Daneben gibt es noch das Witten-Bell Discounting und das Good-Turing Discounting als Smoothing-Verfahren.

**Hidden-Markov-Modelle** - Hidden-Markov-Modelle sind Automaten mit probabilistischen Zustandsübergängen. Dies folgt aus den Beiden folgenden Annahmen:

*begrenztes Horizont*: ![enter image description here](http://latex.codecogs.com/svg.latex?%5Cinline%20P%28X_%7Bt&plus;1%7D%20=%20s_k%7CX_1,%20.%20.%20.%20,X_t%29%20=%20P%28X_%7Bt&plus;1%7D%20=%20s_k%7CX_t%29) - Die Wahscheinlichkeit des Folgezustandes ist nur vom letzten Zustand abhängig.

*Der Zeitinvarianz*: ![enter image description here](http://latex.codecogs.com/svg.latex?%5Cinline%20P%28X_%7Bt&plus;1%7D%20=%20s_k%7CX_1,%20.%20.%20.%20,X_t%29%20=%20P%28X_1%20=%20s_k%7CX_1%29) - Die Übergangswahscheinlichkeiten änderen sich nicht.
Das Hidden Markov Modell eignet sich gut in der Spracherkennung.


**Probabalistisches Parsen** - Eine Parsing Methode, bei der die Regeln mit Wahscheinlichkeiten versehen sind. alle Regeln mit gleichem Kopf addieren sich zu 1 zusammen. Probabalistisches Parsen geht mit den Mehrdeutigkeiten, die beim Erzeugen eines Syntaxbaums eines natürlichsprachlichen Satzes entsehen, um. Es wird einfach der Syntaxbaum mit der insgesamt höchsten Wahrscheinlichkeit genommen. Die Wahscheinlichkeiten einer Regeln kann z.B. an einem Korpus mit Syntaxtrees (Penn Treebank) trainiert werden.
Probabalistisches Parsen hat zwei große Probleme:
1. Das Modell geht davon aus, dass die einzellnen Sätze voneinander uabhängig sind.  Dies ist aber nicht der Fall.
2. Die semantischen Abhängigkeiten zwischen Worten eines Satzes lassen sich hierdurch nicht modellieren oder sinnvoll verabreiten.

**Statistische Zuordnung** - Maschinelle Übersetzung eines Quelltextes in eine Zielsprache. Dabie gibt es vier Methoden:

1. Wort-für-Wort. Einfach, aber Unzureichend

2.  Syntaktische Überführung. Ein Syntaxbaum des Quelltextes wird erzeugt, uberstetzt und in der Zielsprache ausformuliert. Löst einige Probleme von (1). Aber semantische Fehler können auftreten: "Ich esse gerne" wird zu "I eat willingly" übersetzt, obwohl es "I like to eat" sein sollte.

3.  Semantische Überführung. Die Semantik jedes Satzes wird übersetzt und anschließsend ausformuliert. Löst Probleme von (1) und (2). Aufwändiger. Kann jedoch unnatürliche Übersetztungen erzeugen.

4. Interlingua. Der Quelltext wird zunächst in eine (universelle) intermediäre Sprache (Interlingua) übersetzt und anschließend in die Zielsprache ausformuliert. Die Interlingua dient rein zur Wissensrespräsensation und ist unabhängig von der Art und Weise wie verschiedene Sprache den Sinngehalt ausdrücken. Es ist außerdem einfacher für viele Übersetzungen zwischen verschied. Sprachen eine gemeinsame Interlingua zu haben, anstatt Übersetztungen zwischen je zwei Sprachen bauen zu müssen.


### Text Mining ###


*Information Overload* - seit der Verbreitung Internets ist jemend Menschen immer mehr Information in immer weniger Zeit zugreifbar. Dadurch wachsen aber auch die Anforderungen an Mensch und Maschine mit der Informationsflut umzugehen. Obwohl die größten Unternhemen und Forschungseinheiten mit riesigen Mengen strukturierter Daten umgehen, gibt es jedoch einen größeren und relevanteren Anteil and unstrukturierten Informationen. Diese sind meist in natürlicher Sprache geschrieben und umfassten im Jahre 2000 geschätzt 1000 Petabyte an Daten in allen Unternehmen und Instituten auf der gesamten Welt. Eine (automatische) Verarbeitung/Aufbereitung durch den Computer ist daher sehr hilfreich.


*Text Mining* - Wissensextraction und -verarbeitung basierend auf Texten (in diesem Sinne Data Mining auf Texten statt Daten).

Eine Definition von Marti Hearst: [Text Mining ist die Menge von Techniken zum Entdecken und automatischen Extrahieren von neuen, zuvor unbekannten
Informationen aus Texten.]


*Möglichkeiten des Text Mining* - Text Mining stellt die automatisierte Verarbeitung und Auswertung riesiger natürlichsprachlicher Textdatenbanken (Internet, interne Kommunikation, externe Archive, ...) zur Verfügung und ermöglicht es damit Aktionen auf einer höheren semantischen Ebene. Kundenmeinungen großer Anzahl von Kunden automatisch zu klassifizieren um sich ein Bild der Kunden zu machen, Beschwerdenmails automatisch den richigen Ansprechpartner zuordnnen und weiterleiten oder Hinweise für Korrelationen & Kausalitäten aus Publikationen in der Medizin erkennen und melden und vieles mehr.


*Vier Schritte des Text Mining* - Dan Sullivan erkennt vier Schritte im Prozess des Text Mining:

1. Suche (Welche Texte sind relevant?)

2. Vorberarbeitung (Wie kann ich die Texte machinenlesbar machen?)

3. Bewertung & Selektion (Wie hängen die Texte miteinander zusammen?)

4. Extrahierung & Mustererkennung (Welche konkreten Informationen will der Nutzer?)


**Suche & Information Retrieval**

Ziel dieses Schrittes ist es zu einer gegebenen Anfrage auf eine Textdatenbank die Menge an relevanten Texten ausfindig zu machen. Die Menge soll aber nicht soweit reduziert werden, dass der Nutzer diese durchgehen kann - vielmehr ist dieser Schritt ein erster Filter der für die folgenden Schritte die Textmenge und damit die Arbeit verringert. Es werden hier zwei Verfahren vorgestellt, die diesen Schritt durchführen.


*Vektorraummodell* - Das Vektorraummodell ist ein einfaches Modell zum Vergleich arbiträrer Texte und Anfragen verwendet werden kann - jedoch mit unzureichenden Ergebnissen. In diesem Verfahren wird jedem Wort eine Dimension zugeordnet - ein Text der ein bestimmtes Wort enthält, wird der bei der Dimension des Wortes der Zahl 1 zugeordnet - sonst bekommt der Text die Zahl 0. Dies kann man auch für Anfragen wiederholen. Dadurch kann man jeder/m Anfrage/Text einen Punkt im n-dimentionalen Vektorraum zuordnen. Die Ähnlichkeit zweier Objekte in diesem Raum lässt sich damit ziemlich einfach als geometischer Abstand oder als die Winkelabweichung ihrer Vektoren implementieren. Die Suche gibt nun die Dokumente zurück, die ein gewisses Grad an Ähnlichkeit mit der Anfrage haben.

Dieses Verfahren hat jedoch zwei Nachteile. Erstens werden Wörte mit gleicher Bedeutung (Synonyme) auf unterschiedliche Dimensionen zugeordnet. Dies führt zu spärlichem Auftauchen der Objekte im Raum.

Die Spärlichkeit und das Clustering der Objekte an bestimmten Worten ist der zweite Nachteil dieses Verfahrens. Bei manchen Anfragen stehen einfahc nicht genügend Texte mit ähnlichen Ort im Raum zur Verfügung, sodass die Suche sehr wenige Ergebnisse liefert.


*Latent Semantic Indexing* - Beim Latent Semantic Indexing wird nicht die inhaltliche Bedeutung eines Wortes oder eines Konzeptes berücksichtigt, sondern es werden Verfahren der Statistik und der linearen Algebra eingesetzt, um Termcluster zu finden, die bestimmte Konzepte beschreiben. Die Cluster werden nicht vorgegeben sondern werden anhand der Wahrscheinlichkeit für das Auftreten eines Terms gegeben eines anderen Terms geschätzt. Dadurch können Konzepte approximiert werden, die regelmäßig gemeinsam auftretende Terme beschreiben. Während in einem einfachen Vektorraummodell alle Begriffe verschiedene Dimensionen benötigen, wird genau durch das Zusammenführen von Dimensionen zu einem gemeinsamen Konzept so viel Genauigkeit verloren, dass nun auch Dokumente, die nur einen Teil der Begriffe beinhalten eine Suchanfrage erfüllen.


**Vorverarbeitung**

Bei der Vorverarbeitung werden die relevanten Dokumente auf linguistischer Ebene analysiert und für die nächsten Schritte aufbereitet. Dabei kommen die, bereits in der Einführung genannten, Schritte der Computerliguistik zum tragen. Diese sind Morphologie, Tokenisierung, POS-Tagging, Chunk-Parser sowie Syntaxanalyse und semantische Analyse. Ergebnisse all dieser Zwischenschritte sind zum darauffolgenden Clustering hilfreich. Hinzu kommen statistische Methoden die zwar teils weniger genau sind, aber dafür ohne großen Menschenfleiß durchgeführt werden können. (Was das Ziel von Text Mining in erster Linie ist.)

Neben semantischen Netzten, die die Bedeutung von Texten festhalten, sind auch die Verwerndung der Makrostrukturen eine nützlich um die Bedeutung eines Dokumentes festzuhalten. Makrostrukturen verweist hierbei auf nicht-linguistische kontextuelle Informationen - z.B. Weblinks oder Hierarchische Gliederungen des Textes. Weblinks werden z.B. in dem von Google vorgestlelten Pagerank Algorithmus verwendet um Hubs (Dokumente mit vielen ausgehenden Links) und Authorities (Dokumente mit vielen eingehenden Links) zu erknenen.


**Bewertung & Selektion**

Nach der Aufbereitung für den Computer können die Dokumente nun Themen zugeordnet werden(Klassifizierung) oder zu Gemeinsamkeiten geruppiert werden(Clustering). 


*Klassifikation durch Labeling* - Durch einfache statistische Verfahren wie Wortfrequenzstatistiken über den standardisierten Morphemen des vorherigen Schrittes lassen sich nun durch die Inverse Dokumentenfrequenz die Relevanz einzellner Morpheme zur Klassifikation dr Dokumente verwenden. Taucht ein Morphen nur in weniger ausgewählten Dokumenten auf, dann kann dieses Morphem als Klasse verwendet werden. Diese relativ einfache Methode hat jedoch den Nachteil, dass es nicht generalisieren kann. Dokumente mit Bus, Bahn und Auto gelabelt werden, werden damit nicht automatisch auch dem Begriff Bodentransportmittel zugeordnet.


*Klassifkation durch Multidimensionale Taxonomien* - Gegeben einer Taxonomie (einer Menge von "Is-A" Beziehungen zwischen Klassen, z.B *Mensch is-a Lebewesen*) kann dieses Verfahren eine Reihe konkreter Instanzen solcher Klassen erkennen und zuordnen - und  nach und nach die allgemeineren Klassifizierungen ergänzen.

*Clustering* - Clustering versucht anhand der Texte (und ggf. ihrer Makrostrukturen) zusammengehörige Dokuemente ausfindig zu machen. Im Gegensatz zur Klassifizierung sind keine Themen/Texonomien vordefiniert. Es gibt im wesentlichen zwei Clustering Arten - binäre und hierarchische Verfahren.

Binäres Clustering versucht Dokumente in ineinander ähnliche aber voneinander möglichst verschiedene Cluster zusammenzuordnen. Dabei gehört ein Dokument genau einem Cluster. Ergebnisse aus der Aufbereitung können verwendet werden um das Thema eines Clusters zu bestimmen.

Hierarchisches Clustering ordnet die Cluster stattdessen in einem Baum - wobei die Cluster und die Dokumente nach oben hin allgemeineren Themen zugeordnet werden. Dieses Verfahren fängt zunäcsht mit allen Dokumenten in ihrem eigenen Cluster an und fasst nach und nach je zwei Cluster mit dem geringsten Abstand zueinander zusammen - bis nur noch ein Cluster übrig bleibt oder die Cluster einen Schwellwert an Ähnlichkeit unterschreiten und der Algorithmus abgebrochen wird. Hierarchisches Clustering ist ausserdem aufgrund der Navigierbarkeit sehr vorteilhaft. Ein Beispiel sei hierbei [Carrot² Search](http://search.carrotsearch.com/carrot2-webapp/search?source=web&view=foamtree&skin=fancy-compact&query=Ebola&results=100&algorithm=lingo3g&EToolsDocumentSource.country=ALL&EToolsDocumentSource.language=ALL&EToolsDocumentSource.customerId=&EToolsDocumentSource.safeSearch=false). (Man bemerke, wie man hierbei auch in die einzelnen Themen navigieren kann.) 


**Mustererkennung & Information Extraction**

Nun sind die Ergebnisse dem Nutzer visualiziert und zugeordnet und es geht darum konkret die relevanten Informationen aus den Texten zu extrahieren und dem Nutzer zu präsentieren. Dabei werden hier nun 'komplexere' Methoden als nur einfache reguläre Ausdrücke verwendet um die Informationen ausfindig zu machen. Vorgestellt werden hierbei Wort/Term Matchings und Relevancy Signatures.


*Wort/Term Matchings* - Die Ergebnisse der vorherigen Schritte können verwendet werden um Korrelationen zwischen bestimmten Wörtern zu finden und zu bewerten (z.B. Diebstahl und Kreditkartenmissbrauch). Dabei setzt man einen Schwellwert für eine Korreleation fest und eliminiert Stopp-wörter oder Wörte ohne relevante Semantik (wie Präpositionen oder Konjunktionen im Gegensatz zu Substantiven). Ist bereits vorher bekannt nach was für einer Art von Zusammenhängen gesucht wird (z.B. im Rahmen eines monatlichen Geschäftsberichtes), so bietet sich auch der Einsatz von Templates an. Anhand von Matchings versucht man dann die korrekten Wörter/Ergebnisse Felder einzufüllen.


*Relevancy Signatures* - Ein Relevance Signature ist ein Paar der Form (Wort, Konzept) wobei das Wort eine starker Indikator für das Konzept/den Kontext ist. Durch Fund eines Wortes oder bei der suche eines Konzeptes/in einem Kontext ist der Fund des Wortes ein Indikator für die Relevanz dieses Satzes/Absatzes/Dokuments. Relevancy Signatures beschreiben einen heuristischen Ansatz um Informationen aus einem Text zu extrahieren.
