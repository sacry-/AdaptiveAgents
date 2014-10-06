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
1. Morphologie ist die Lehre von der Zusammensetzung und Formbildung der Wörter.
2. Syntax werden die von den Wörtern gebildeten Strukturen zusammengefasst. Hierzu zählen die Grammatiken.
3.1 Lexikalische Semantik - Bedeutung auf Wortebene
3.2 Kompositionelle Semantik - Bedeutung von Sätzen oder längeren Abschnitten.
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

*Prädikat-Argument-Strukturen* (predicate-argument structures) - legen Beziehungen zwischen den Konstituenten eines Satzes fest. Den formalen Rahmen dieser Beziehungen bildet die Grammatik.

*Linking* - Zum einen nehmen bestimmte Konstituenten an bestimmten Stellen im Satz auf der inhaltlichen Ebene bestimmte Rollen ein. Die Analyse solcher Zusammenhänge bezeichnet man als Linking. Anwendung: Informationsextraktion im Rahmen des Information Retrieval oder Text Mining, weil nach der Erkennung von semantischem Subjekt und Objekt Fragen der Art „Wer hat was mit welchem Objekt getan?“ beantwortet werden können.

**Lexikalische Semantik** - Lexem und das Lexikon

*Lexem* - bezeichnet man eine Kombination aus Form (orthographisch und phonologisch) und Bedeutung auf Wortebene, sozusagen ein „lexikalisches Morphem“. Der Bedeutungs-Teil eines Lexems heißt *Sinn* (Sense).

*Lexikon* - Liste von Lexemen (z.B. WordNet), Einträge müssen zueinander in Beziehung gesetzt werden für die Folgerung von inhaltlichem Wissen.

*Homonymie* - Wörter haben dieselbe Form, aber unterschiedliche Bedeutungen, zum Beispiel „Bank“.
*Polysemie* - Unterschiedliche, aber verwandte oder auf einen gemeinsamen Ursprung zurückzuführende Bedeutungen: „Horn“ als Berg, Instrument, Gebäck
*Synonymie* - Verschiedene Lexeme mit gleicher Bedeutung: „Streichholz“, „Zündholz“
*Antonymie* - Lexeme mit gegensätzlicher Bedeutung: „groß“, „klein“
*Hyponymie* - Klassen- und Unterklassenbildung: „Auto“ ↔ „Fahrzeug“

Usage
-

Notes
-


