# Dataset card for Norwegian Bokmål (radical variety)

## Description
<!-- A concise description of the data associated with this card. -->
FLORES+ dev and devtest set in Norwegian Bokmål -- radical variety.

## License
<!-- Contributions to existing datasets must be released under the same license as the parent dataset. For completely new contributions, we encourage the use of an open license. At a minimum, data should be made available for research use. Please specify the license using an SPDX license identifier. -->
CC-BY-SA-4.0

## Attribution
<!-- Who should be credited for creating this dataset? Feel free to include citation data in BibTeX format. -->
```bibtex
@inproceedings{maehlum-etal-2025-improved,
    title = "Improved {N}orwegian {B}okm{\r{a}}l Translations for {FLORES}",
    author = "M{\ae}hlum, Petter  and
      N{\ae}ss Evensen, Anders  and
      Scherrer, Yves",
    editor = "Haddow, Barry  and
      Kocmi, Tom  and
      Koehn, Philipp  and
      Monz, Christof",
    booktitle = "Proceedings of the Tenth Conference on Machine Translation",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.wmt-1.86/",
    pages = "1124--1132",
    ISBN = "979-8-89176-341-8",
    abstract = "FLORES+ is a collection of parallel datasets obtained by translation from originally English source texts. FLORES+ contains Norwegian translations for the two official written variants of Norwegian: Norwegian Bokm{\r{a}}l and Norwegian Nynorsk. However, the earliest Bokm{\r{a}}l version contained non-native-like mistakes, and even after a later revision, the dataset contained grammatical and lexical errors. This paper aims at correcting unambiguous mistakes, and thus creating a new version of the Bokm{\r{a}}l dataset. At the same time, we provide a translation into Radical Bokm{\r{a}}l, a sub-variety of Norwegian which is closer to Nynorsk in some aspects, while still being within the official norms for Bokm{\r{a}}l. We discuss existing errors and differences in the various translations and the corrections that we provide."
}
```

## Language codes
<!-- * If this language is assigned an ISO 639-3 individual language code (not a macrolanguage code), specify it here. * Please specify the script this language is written in using an ISO 15924 code. * If this language is assigned a Glottocode, please specify it here. -->
* ISO 639-3: nob
* ISO 15924: Latn
* Glottocode: norw1259
* `variant` tag: `radical` (we had to introduce this field to disambiguate between the two Bokmål standards that share the same ISO codes and Glottocode).

## Additional language information
<!-- Any relevant additional information on the language, such as:
  * A list of reference publications and software (dictionaries, grammars, spellcheckers).
  * If applicable, any additional information about dialectal variation that is not captured by the Glottocode.
  * If relevant, the orthography used in your contribution. -->
The radical version is based on the official Bokmål dictionary: https://ordbokene.no/nob/
And guided by the Association of Radical Bokmål:  https://bokmal.no/

## Workflow
<!-- What workflow was followed in creating this dataset? E.g., for a translated dataset, relevant information includes: what language the content was translated from, the number of translators, aggregate translator information (how many were native speakers in the target language, how many were highly proficient in the target languages, how many had professional translation experience), was any fraction of the data checked independently by third parties, etc. -->
The data was corrected based on the most recent FLORES+ Bokmål translations. The corrections were done by two native Norwegian Bokmål writers with high proficiency in English, and with earlier experience in translation.

## Additional guidelines
<!-- Were any additional guidelines agreed upon? Examples might include style guidelines, the use of particular grammatical forms or sentence structures, specific spelling or punctuation rules to be followed, etc. -->
