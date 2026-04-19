# Dataset card

## Description  
<!-- A concise description of the data associated with this card. -->  
FLORES+ devtest set in Halh Mongolian (traditional Mongolian script).

## License  
<!-- Contributions to existing datasets must be released under the same license as the parent dataset. For completely new contributions, we encourage the use of an open license. At a minimum, data should be made available for research use. Please specify the license using an SPDX license identifier. -->  
CC-BY-SA-4.0  

## Attribution  
<!-- Who should be credited for creating this dataset? Feel free to include citation data in BibTeX format. -->  
The dataset is part of the [MiLiC-Eval benchmark](https://github.com/luciusssss/MiLiC-Eval) proposed in the following paper:
```bibtex 
@inproceedings{zhang-etal-2025-milic,
    title = "{M}i{L}i{C}-Eval: Benchmarking Multilingual {LLM}s for {C}hina{'}s Minority Languages",
    author = "Zhang, Chen  and
      Tao, Mingxu  and
      Liao, Zhiyuan  and
      Feng, Yansong",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2025",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.findings-acl.578/",
    doi = "10.18653/v1/2025.findings-acl.578",
    pages = "11086--11102",
    ISBN = "979-8-89176-256-5"
}
```  

Also thanks to the following contributors for their help in data verification and correction: Saihantaoli, Sulde, Wang Xingjun.


## Language codes  
<!-- * If this language is assigned an ISO 639-3 individual language code (not a macrolanguage code), specify it here. * Please specify the script this language is written in using an ISO 15924 code. * If this language is assigned a Glottocode, please specify it here. -->  
* ISO 639-3: khk
* ISO 15924: Mong
* Glottocode: halh1238

## Additional language information  
<!-- Any relevant additional information on the language, such as: 
  * A list of reference publications and software (dictionaries, grammars, spellcheckers). 
  * If applicable, any additional information about dialectal variation that is not captured by the Glottocode. 
  * If relevant, the orthography used in your contribution. -->   
Most existing NLP resources for Mongolian are written in the Cyrillic script, which is primarily used in Mongolia. In this contribution, we include the traditional Mongolian script, which is the official writing system in Inner Mongolia, China, and is also being actively promoted by the government of Mongolia.


## Workflow  
<!-- What workflow was followed in creating this dataset? E.g., for a translated dataset, relevant information includes: what language the content was translated from, the number of translators, aggregate translator information (how many were native speakers in the target language, how many were highly proficient in the target languages, how many had professional translation experience), was any fraction of the data checked independently by third parties, etc. -->  
We first transliterate the existing Cyrillic-script Halh Mongolian data in FLORES+ into the traditional Mongolian script using a transliteration tool developed by Inner Mongolia University (https://ai.nmgoyun.com/#/AI/transform). The transliterated outputs are then manually verified and corrected by native speakers. At present, this process has been completed for the 1,012 sentences in the devtest split.

Some of the transliterated texts may contain named entities in Latin script (e.g. "National Aeronautics and Space Administration" or "Jai Shankar Choudhary").
Occasionally, the texts in two scripts don't match exactly (e.g. in the Cyrillic version, "National Aeronautics and Space Administration" is rendered in its abbreviated form, "НАСА", but the version in Mongolian script uses the full Latin name).

## Additional guidelines  
<!-- Were any additional guidelines agreed upon? Examples might include style guidelines, the use of particular grammatical forms or sentence structures, specific spelling or punctuation rules to be followed, etc. -->