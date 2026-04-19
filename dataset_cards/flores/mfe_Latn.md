# Dataset card for Mauritian Creole

## Description  
<!-- A concise description of the data associated with this card. -->  
FLORES-200 dev and devtest set in Mauritian Creole.

## License  
<!-- Contributions to existing datasets must be released under the same license as the parent dataset. For completely new contributions, we encourage the use of an open license. At a minimum, data should be made available for research use. Please specify the license using an SPDX license identifier. -->  
CC-BY-SA-4.0  

## Attribution  
<!-- Who should be credited for creating this dataset? Feel free to include citation data in BibTeX format. -->  
```bibtex 
@inproceedings{rajcoomar-2025-kozkreolmru,
    title = "{K}oz{K}reol{MRU} {WMT} 2025 {C}reole{MT} System Description: Koz Kreol: Multi-Stage Training for {E}nglish{--}Mauritian Creole {MT}",
    author = "Rajcoomar, Yush",
    editor = "Haddow, Barry  and
      Kocmi, Tom  and
      Koehn, Philipp  and
      Monz, Christof",
    booktitle = "Proceedings of the Tenth Conference on Machine Translation",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.wmt-1.92/",
    doi = "10.18653/v1/2025.wmt-1.92",
    pages = "1183--1190",
    ISBN = "979-8-89176-341-8",
    abstract = "Mauritian Creole (Kreol Morisyen), spoken by approximately 1.5 million people worldwide, faces significant challenges in digital language technology due to limited computational resources. This paper presents ``Koz Kreol'', a comprehensive approach to English{--}Mauritian Creole machine translation using a three-stage training methodology: monolingual pretraining, parallel data training, and LoRA fine-tuning. We achieve state-of-the-art results with a 28.82 BLEU score for EN{\textrightarrow}MFE translation, representing a 74{\%} improvement over ChatGPT-4o. Our work addresses critical data scarcity through the use of existing datasets, synthetic data generation, and community-sourced translations. The methodology provides a replicable framework for other low-resource Creole languages while supporting digital inclusion and cultural preservation for the Mauritian community. This paper consists of both a systems and data subtask submission as part of a Creole MT Shared Task."
}
```  

## Language codes  
<!-- * If this language is assigned an ISO 639-3 individual language code (not a macrolanguage code), specify it here. * Please specify the script this language is written in using an ISO 15924 code. * If this language is assigned a Glottocode, please specify it here. -->  
* ISO 639-3: mfe
* ISO 15924: Latn
* Glottocode: mori1278

## Additional language information  
<!-- Any relevant additional information on the language, such as: 
  * A list of reference publications and software (dictionaries, grammars, spellcheckers). 
  * If applicable, any additional information about dialectal variation that is not captured by the Glottocode. 
  * If relevant, the orthography used in your contribution. -->   
  
## Workflow  
<!-- What workflow was followed in creating this dataset? E.g., for a translated dataset, relevant information includes: what language the content was translated from, the number of translators, aggregate translator information (how many were native speakers in the target language, how many were highly proficient in the target languages, how many had professional translation experience), was any fraction of the data checked independently by third parties, etc. -->  
Data was translated from English by 2 translators, all native speakers of the target language and highly proficient in English (at C2 level of the European Language Framework). 100% of the target translations were reviewed by a native speaker.

## Additional guidelines  
<!-- Were any additional guidelines agreed upon? Examples might include style guidelines, the use of particular grammatical forms or sentence structures, specific spelling or punctuation rules to be followed, etc. -->