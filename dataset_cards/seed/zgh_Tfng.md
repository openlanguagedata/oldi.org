# Dataset card

## Description  
Seed data in Standard Moroccan Tamazight with 2025 corrections.

## License  
CC-BY-SA-4.0  

## Attribution  
```
@inproceedings{oktem-etal-2025-correcting,
    title = "Correcting the Tamazight Portions of {FLORES}+ and {OLDI} Seed Datasets",
    author = "Oktem, Alp  and
      Farhi, Mohamed Aymane  and
      Essaidi, Brahim  and
      Jabouja, Naceur  and
      Boudichat, Farida",
    editor = "Haddow, Barry  and
      Kocmi, Tom  and
      Koehn, Philipp  and
      Monz, Christof",
    booktitle = "Proceedings of the Tenth Conference on Machine Translation",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.wmt-1.82/",
    pages = "1072--1080",
    ISBN = "979-8-89176-341-8",
    abstract = "We present the manual correction of the Tamazight portions of the FLORES+ and OLDI Seed datasets to improve the quality of open machine translation resources for the language. These widely used reference corpora contained numerous issues, including mistranslations, orthographic inconsistencies, overuse of loanwords, and non-standard transliterations. Overall, 36{\%} of FLORES+ and 40{\%} of Seed sentences were corrected by expert linguists, with average token divergence of 19{\%} and 25{\%} among changed items. Evaluation of multiple MT systems, including NLLB models and commercial LLM services, showed consistent gains in automated evaluation metrics when using the corrected data. Fine-tuning NLLB-600M on the revised Seed corpus yielded improvements of +6.05 chrF (en{\textrightarrow}zgh) and +2.32 (zgh{\textrightarrow}en), outperforming larger parameter models and LLM providers in en{\textrightarrow}zgh direction."
}
```

Awal initiative:

```
@inproceedings{oktem-boudichat-2025-awal,
  author    = {\"Oktem, Alp and Boudichat, Farida},
  title     = {Awal -- Community-Powered Language Technology for Tamazight},
  booktitle = {Proceedings of the Conf{\'e}rence Internationale sur les Technologies d'Information et de Communication pour l'Amazighe (TICAM)},
  year      = {2025},
  address   = {Rabat, Morocco},
  publisher = {Institut Royal de la Culture Amazighe (IRCAM)}
}
```

Original dataset:
```bibtex
@inproceedings{seed-23,
    title = {Small Data, Big Impact: Leveraging Minimal Data for Effective Machine Translation},
    author = {Maillard, Jean and Gao, Cynthia and Kalbassi, Elahe and Sadagopan, Kaushik Ram and Goswami, Vedanuj and Koehn, Philipp and Fan, Angela and Guzmán, Francisco},
    booktitle = {Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
    year = {2023},
    address = {Toronto, Canada},
    publisher = {Association for Computational Linguistics},
    pages = {2740--2756},
    url = {https://aclanthology.org/2023.acl-long.154},
}
```

## Language codes  
* ISO 639-3: zgh
* ISO 15924: Tfng
* Glottocode: stan1324

## Additional language information  
Standard Moroccan Tamazight as standardized by the Royal Institute of Amazigh Culture (IRCAM), using Tifinaghe-IRCAM (Neo-Tifinagh) script. Reference materials used include:

* Dictionnaire Général de la Langue Amazighe (Ameur et al., 2016)
* Arabic-Amazigh-French Landforms Dictionary (Akioud et al., 2022)  
* Arabic-Amazigh Dictionary (Chafik, 1996)
* Phonologie de l'Amazighe (Boukous, 2009)
* La Nouvelle Grammaire de l'Amazighe (Boukhris et al., 2008)
* Grammaire Générative de l'Amazighe: Morphologie et Syntaxe du Nom (El Moujahid, 2022)
* Manuel de Conjugaison de l'Amazighe (Laabdelaoui et al., 2012)

## Workflow  

The original data was released as part of the NLLB-Seed dataset, where it was incorrectly labeled `tzm_Tfng`. It was relabeled as `zgh_Tfng` after community feedback and additional quality assessment. Please refer to the paper for further information.

The 2025 update submission contains manual corrections of Standard Moroccan Tamazight (zgh) translations that addressed mistranslations, orthographic inconsistencies, overuse of loanwords, and non-standard transliterations in the original datasets. The corrected data includes 997 sentences from FLORES+ dev, 1,012 sentences from FLORES+ devtest, and 6,193 sentences from OLDI Seed, with 36% of FLORES+ and 40% of Seed sentences requiring corrections.

Corrections were performed by expert linguists taking English source sentences as reference. The FLORES+ dev and devtest sets were revised in full in two iterations by two linguists. The OLDI Seed dataset was divided into batches of 1,000 sentences and distributed among three professional Tamazight translators. Quality control was ensured through spot-checking of each linguist's work by another linguist through random sampling. All translators were professional translators and were compensated as part of this work.

## Additional guidelines  
Corrections followed IRCAM standardization guidelines, prioritizing native Tamazight terms over loanwords when available. For loanwords that were retained, proper Tamazight morphological patterns were applied (e.g., appropriate nominal prefixes). Transliterations of foreign words and names followed standardized practices, with particular attention to accurate mapping of sounds not present in Tamazight to their closest equivalents.
