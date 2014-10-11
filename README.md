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

Setup
-

Plan
-
<s>Phonetik und Phonologie</s>

1. Morphologie ist die Lehre von der Zusammensetzung und Formbildung  der Wörter.
2. Syntax werden die von den Wörtern gebildeten Strukturen zusammengefasst. Hierzu zählen die Grammatiken.
3. Semantik - (Lexikalisch - Bedeutung auf Wortebene) + (Kompositionell - Bedeutung von Sätzen/Abschnitten)

<s>Pragmatik und Diskurs</s>

**Morphologie**
*Morpheme* sind die kleinsten Einheiten mit Bedeutung in einer Sprache. Zwei Klassen: Stämme und Affixe.

*Stemming* - bezeichnet das Zurückführen eines Wortes auf seinen Wortstamm.
Lemmatisierung das Wort wird auf eine in der Sprache vorhandene Grundform zurückgeführt, wie z.B. in Lexika auch *Lemma*. z.B. „lachte“ -> „lachen“.

|>  Kombination aus Regeln (z.B. "ing" -> empty) und einem Lexikon.

**Syntax - Wortarten und Konstituenten**

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

**Semantik** "Inhaltliches Verständnis"

*Semantische Analyse* -Bedeutungsrepräsentation (meaning representation) muss der linguistischen Struktur zugeordnet werden.

1. Verifizierbarkeit - Die Möglichkeit des Vergleichs einer Aussage über einen Sachverhalt mit der Modellierung dieses Sachverhalts in der Wissensbasis.
2. Eindeutigkeit - Eine Repräsentation muss eine einzige eindeutige Interpretation besitzen. (Mehrdeutigkeiten auflösen)
3. Kanonische Form - gleiche Aussagen in unterschiedlichen Repräsentationen werden in eine kanonische Form überführt z.B. „In diesem Lokal gibt es vegetarisches Essen“ und „Dieses Lokal bietet vegetarische Gerichte an“ -> Dieses Lokal + Vegetarisches Essen

*Prädikat-Argument-Strukturen* (predicate-argument structures) - legen Beziehungen zwischen den Konstituenten eines Satzes fest. Den formalen Rahmen dieser Beziehungen bildet die Grammatik.

*Linking* - Zum einen nehmen bestimmte Konstituenten an bestimmten Stellen im Satz auf der inhaltlichen Ebene bestimmte Rollen ein. Die Analyse solcher Zusammenhänge bezeichnet man als Linking. Anwendung: Informationsextraktion im Rahmen des Information Retrieval oder Text Mining, weil nach der Erkennung von semantischem Subjekt und Objekt Fragen der Art „Wer hat was mit welchem Objekt getan?“ beantwortet werden können.

**Lexikalische Semantik** - Lexem und das Lexikon

*Lexem* - bezeichnet man eine Kombination aus Form (orthographisch und phonologisch) und Bedeutung auf Wortebene, sozusagen ein „lexikalisches Morphem“. Der Bedeutungs-Teil eines Lexems heißt *Sinn* (Sense).

*Lexikon* - Liste von Lexemen (z.B. WordNet), Einträge müssen zueinander in Beziehung gesetzt werden für die Folgerung von inhaltlichem Wissen.

*Homonymie* - Wörter haben dieselbe Form, aber unterschiedliche Bedeutungen, zum Beispiel „Bank“.
*Polysemie* - Unterschiedliche, aber verwandte oder auf einen gemeinsamen Ursprung zurückzuführende Bedeutungen: „Horn“ als Berg, Instrument, Gebäck.<br />
*Synonymie* - Verschiedene Lexeme mit gleicher Bedeutung: „Streichholz“, „Zündholz“.<br />
*Antonymie* - Lexeme mit gegensätzlicher Bedeutung: „groß“, „klein“.<br />
*Hyponymie* - Klassen- und Unterklassenbildung: „Auto“ ↔ „Fahrzeug“.

**Methoden des statistischen Text Mining**

*Korpus*,*Corpus* - Referenzquelltext auf dem Methoden trainiert werden können, zusätzliche Information wie POS-Tags, Syntaxtrees etc. enthalten; Brown Corpus, Lancaster-Oslo-Bergen Corpus, Penn Treebank, Canadian Hansard

*Worttoken* - Anazhl der Wörter (in einem Satz/Paragraphen/Korpus ...)

*Worttypen* - Anazhl der voneinander verschiedener Wörter (in einem Satz/Paragraphen/Korpus ...)

*Durchchnittliche Häufigkeit eines Wortes* - ![#Token/#Typen](http://latex.codecogs.com/svg.latex?%5Cinline%20%5Cfrac%20%7BAnazahl%5C%2C%20von%5C%2C%20Worttoken%7D%20%7BAnzahl%5C%2C%20von%5C%2C%20Worttypen%7D), ein Indikator für die Wortreichheit des Textes, Vergleiche Tom Sawyer mit einem wissenschaftlichen Text

*Zipf's Gesetz* - Zipf's Gesetz ist eine mathematische Approximation der Beobachtung, dass einige weniger Worte viel öfter in einem Text erscheinen als alle restlichen Wörter. Sei *f(w)* die Frequenz und *r(w)* der Häufigkeitsrang des Wortes, dann besagt Zipf's Gesetz, dass das Produkt beider konstant ist, ![Zipf's Gesetz](http://latex.codecogs.com/svg.latex?%5Cinline%20f%28w%29%20r%28w%29%20=%20const.). In anderen Worten heißt das, dass das zehnthäufigste Wort fünfmal häufiger vorkommtals das 50st-häufigste Wort. Mandelbrot entwickelte in den 1950er eine bessere Approximation des Zipf's Gesetzes.

*Kollokationen* - Ausdrücke mit zwei oder mehr Wörtern die gemeinsam einen gesonderten Sinn ergeben, bsp. *Schwarzes Brett* 

*Erkennung von Kollokationen durch Häufigkeit* - Kollokationen werden anhand wiederkehrenden Wortgruppen erkannt. Dabei bieten sich Wortklassensequenzen zur Erkennung an. Zum Beispiel wird "New York City" durch die POS-Tags ![New York City Pos-Tag](http://latex.codecogs.com/svg.latex?%5Cinline%20%5BN%5C!N,%20N%5C!N,%20N%5C!N%5D) erkannt. Diese Methode erkennt jedoch auch Phrasen wie *letzten Abend* als Kollokation. Daher bietet sich diese Methode für feste Phrasen wie *Bundeskanzler Schröder* an.

*Erkennung von Kollokationen durch Mittelwert und Streuung* - Sollen zwei Wörter (z.B. *nahm* und *Abschied*) als Kollokation erkannt werden, bietet es sich an die mittleren Abstände zwischen den Worten und die Streuung dieser Abstande zu betrachten.
Durchschnitt der Abstände: ![enter image description here](http://latex.codecogs.com/svg.latex?%5Cmu%20%3D%20%5Cfrac%20%7B%5Csum_%7Bi%3D1%7D%5E%7BN%7D%20d_i%7D%20%7BN%7D)
Streuung: ![enter image description here](http://latex.codecogs.com/svg.latex?%5Csigma%20=%20%5Csqrt%7B%5Cfrac%20%7B%5Csum_%7Bi=1%7D%5E%7BN%7D%20%28d_i%20-%20%5Cmu%29%5E%7B2%7D%7D%20%7BN%20-1%7D%7D)
Paare mit geriger Standardabweichung und einem Mittelwert > 1 werden als Kollokationen erkannt. Trotzdem werden dennoch einige Wortpaare aufgrund ihrer schieren Käufigkeit als Kollokation erkannt. Durch einen Signifikanztest (T-Test/Chi-Quadrat-Test) können solche Fälle eliminiert werden.

*Theorem von Bayes* - Oft ist die Wahrscheinlichkeit ![enter image description here](http://latex.codecogs.com/gif.latex?%5Cinline%20P%28Ereignis%7CUrsache%29) bekannt, während die
Wahrscheinlichkeit ![enter image description here](http://latex.codecogs.com/gif.latex?%5Cinline%20P%28Ursache%7CEreignis%29) gesucht ist. Das Theorem von Bayes ermöglicht die Berechnung, ob die Ursache gegeben dem vorliegenden Ergebnis zutrifft oder nicht.
![enter image description here](http://latex.codecogs.com/gif.latex?%5Cinline%20P%28U%7CE%29%20=%20%5Cfrac%20%7BP%28E%7CU%29P%28U%29%7D%20%7BP%28E%29%7D)
Das Theorem von Bayes ist zum Beispiel zur Spamfilterung von Emails sehr nützlich.



Usage
-

Notes
-



