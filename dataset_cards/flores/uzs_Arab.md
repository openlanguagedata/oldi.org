# Dataset card for Southern Uzbek

## Description

FLORES+ dev set in Southern Uzbek.

## License

CC-BY-SA-4.0

## Attribution

<!-- Who should be credited for creating this dataset? Feel free to include citation data in BibTeX format. -->

```bibtex
@inproceedings{mamasaidov-etal-2025-filling,
    title = "Filling the Gap for {U}zbek: Creating Translation Resources for {S}outhern {U}zbek",
    author = "Mamasaidov, Mukhammadsaid  and
      Aral, Azizullah  and
      Shopulatov, Abror  and
      Inomjonov, Mironshoh",
    editor = "Haddow, Barry  and
      Kocmi, Tom  and
      Koehn, Philipp  and
      Monz, Christof",
    booktitle = "Proceedings of the Tenth Conference on Machine Translation",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.wmt-1.83/",
    pages = "1081--1087",
    ISBN = "979-8-89176-341-8",
    abstract = "Southern Uzbek (uzs) is a Turkic language variety spoken by around 5 million people in Afghanistan and differs significantly from Northern Uzbek (uzn) in phonology, lexicon, and orthography. Despite the large number of speakers, Southern Uzbek is underrepresented in natural language processing. We present new resources for Southern Uzbek machine translation, including a 997-sentence FLORES+ dev set, 39,994 parallel sentences from dictionary, literary, and web sources, and a fine-tuned NLLB-200 model (lutfiy). We also propose a post-processing method for restoring Arabic-script half-space characters, which improves handling of morphological boundaries. All datasets, models, and tools are released publicly to support future work on Southern Uzbek and other low-resource languages."
}
```

## Language codes

- ISO 639-3: uzs
- ISO 15924: Arab
- Glottocode: sout2699

<!-- ## Additional language information -->

<!-- Any relevant additional information on the language, such as:
  * A list of reference publications and software (dictionaries, grammars, spellcheckers).
  * If applicable, any additional information about dialectal variation that is not captured by the Glottocode.
  * If relevant, the orthography used in your contribution. -->

## Workflow

<!-- What workflow was followed in creating this dataset? E.g., for a translated dataset, relevant information includes: what language the content was translated from, the number of translators, aggregate translator information (how many were native speakers in the target language, how many were highly proficient in the target languages, how many had professional translation experience), was any fraction of the data checked independently by third parties, etc. -->

Data was translated from Northern Uzbek by one translator, a native speaker of the target language and highly proficient in Northern Uzbek and English. The translator has PhD degree in philology and the Uzbek language.
