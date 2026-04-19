# Dataset card

## Description

French partition of the OLDI Seed Corpus, consisting of segments sourced from Wikipedia articles.

## License

CC BY-SA 4.0

## Attribution

```bibtex
@inproceedings{marmonier-etal-2025-french,
    title = "A {F}rench Version of the {OLDI} Seed Corpus",
    author = "Marmonier, Malik  and
      Sagot, Beno{\^i}t  and
      Bawden, Rachel",
    editor = "Haddow, Barry  and
      Kocmi, Tom  and
      Koehn, Philipp  and
      Monz, Christof",
    booktitle = "Proceedings of the Tenth Conference on Machine Translation",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.wmt-1.80/",
    pages = "1048--1060",
    ISBN = "979-8-89176-341-8",
    abstract = "We present the first French partition of the OLDI Seed Corpus, our submission to the WMT 2025 Open Language Data Initiative (OLDI) shared task. We detail its creation process, which involved using multiple machine translation systems and a custom-built interface for post-editing by qualified native speakers. We also highlight the unique translation challenges presented by the source data, which combines highly technical, encyclopedic terminology with the stylistic irregularities characteristic of user-generated content taken from Wikipedia. This French corpus is not an end in itself, but is intended as a crucial pivot resource to facilitate the collection of parallel corpora for the under-resourced regional languages of France."
}
```
See the paper "A French Version of the OLDI Seed Corpus" at https://aclanthology.org/2025.wmt-1.80. 

## Language codes

* ISO 639-3: fra
* ISO 15924: Latn
* Glottocode: stan1290

## Additional language information

The data follows the grammatical and lexical norms of standard French, as spoken and written in France. However, for consistency and to align with common practices in related datasets, it adopts a few specific typographical conventions:
* Dactylographic apostrophes (') are used systematically instead of typographic apostrophes (’).
* The use of French _guillemets_ (« ») with non-breaking spaces is not strictly enforced, a convention also followed in the French partitions of the FLORES dataset.

For authoritative guidance on the French language, the following resources are recommended. For grammar and usage, the primary reference is M. Grevisse and A. Goosse, _Le Bon Usage_ (16th ed., De Boeck Supérieur, 2016). For a comprehensive reference in English, see H. N. Labeau & P. Larrivée, _The Cambridge Grammar of French_ (Cambridge University Press, 2022). For lexicographical aspects, the main monolingual references are _Le Grand Robert de la langue française_ and A. Rey (ed.), _Dictionnaire historique de la langue française_. A standard bilingual reference is the _Collins-Robert French Dictionary_. A recent and comprehensive reference work in English covering the French language in all its facets is W. Ayres-Bennett & M. McLaughlin (eds.), _The Oxford Handbook of the French Language_ (Oxford University Press, 2024). A high-quality open-source spell and grammar checker for French is available via [Grammalecte](https://grammalecte.net/).

## Workflow

This dataset was created using a machine translation post-editing (MTPE) approach. Starting from the original English partition of the OLDI Seed Corpus, we generated nine translation hypotheses per segment using a mix of systems: four "traditional" sequence-to-sequence Transformer MT models (OPUS-MT, NLLB-3.3B, NLLB-600M, MADLAD-400-3B) and five hypotheses from large language models (four from Llama 4 Scout using varied prompting strategies, and one from DeepSeek-R1).

This diverse set of nine translation candidates for each segment was then presented to post-editors in a custom-built interface. The interface allowed post-editors to select any of the candidate translations, which would then populate a text area for further refinement. This refinement process focused on two key aspects of the target text: improving the fluency of the translations, a non-trivial task due to the many stylistic irregularities and errors found in the user-generated source segments originating from Wikipedia; and meticulously verifying and correcting, through extensive external research, the translation of technical terminology across the wide range of specialized, encyclopedic domains represented in the corpus.

As a final step, all post-edited segments underwent a validation pass using the Grammalecte grammar checker interface.

This post-editing and validation work was performed by two native French speakers with a C2 level in English. A native British English speaker with a C2 level in French was also consulted to clarify specific aspects of the source segments. Domain experts were occasionally consulted to solve terminological difficulties in highly technical domains.