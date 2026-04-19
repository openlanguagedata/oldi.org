# Dataset card for Standard Moroccan Tamazight

## Description
Corrected Tamazight portions of the [FLORES+](https://huggingface.co/datasets/openlanguagedata/flores_plus) dev/devtest sets and [OLDI Seed](https://huggingface.co/datasets/openlanguagedata/oldi_seed) dataset.

## License
CC-BY-SA-4.0

## Attribution
```bibtex
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

```bibtex
@inproceedings{oktem-boudichat-2025-awal,
  author    = {\"Oktem, Alp and Boudichat, Farida},
  title     = {Awal -- Community-Powered Language Technology for Tamazight},
  booktitle = {Proceedings of the Conf{\'e}rence Internationale sur les Technologies d'Information et de Communication pour l'Amazighe (TICAM)},
  year      = {2025},
  address   = {Rabat, Morocco},
  publisher = {Institut Royal de la Culture Amazighe (IRCAM)}
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

This submission contains manual corrections of Standard Moroccan Tamazight (zgh) translations that addressed mistranslations, orthographic inconsistencies, overuse of loanwords, and non-standard transliterations in the original datasets. The corrected data includes 997 sentences from FLORES+ dev, 1,012 sentences from FLORES+ devtest, and 6,193 sentences from OLDI Seed, with 36% of FLORES+ and 40% of Seed sentences requiring corrections.

Corrections were performed by expert linguists taking English source sentences as reference. The FLORES+ dev and devtest sets were revised in full in two iterations by two linguists. The OLDI Seed dataset was divided into batches of 1,000 sentences and distributed among three professional Tamazight translators. Quality control was ensured through spot-checking of each linguist's work by another linguist through random sampling. All translators were professional translators and were compensated as part of this work.

## Additional guidelines
Corrections followed IRCAM standardization guidelines, prioritizing native Tamazight terms over loanwords when available. For loanwords that were retained, proper Tamazight morphological patterns were applied (e.g., appropriate nominal prefixes). Transliterations of foreign words and names followed standardized practices, with particular attention to accurate mapping of sounds not present in Tamazight to their closest equivalents.

## Format
Data is provided in three tab-separated values (TSV) files:

* `flores_dev_zgh_corrected.tsv` - FLORES+ dev set (997 sentences)
* `flores_devtest_zgh_corrected.tsv` - FLORES+ devtest set (1,012 sentences)
* `oldi_seed_zgh_corrected.tsv` - OLDI Seed dataset (6,193 sentences)

Each file contains the following columns:
* **ID** - Original dataset identifier (e.g., FL-dev-0, FL-dt-0, seed-0)
* **English** - English source sentence
* **Tamazight (original)** - Original Tamazight translation from the source dataset
* **Tamazight (corrected)** - Manually corrected Tamazight translation


## Changelog

This data was released as part of the FLORES-200 dataset, where it was incorrectly labeled `tzm_Tfng`. It was relabeled as `zgh_Tfng` after community feedback and additional quality assessment. Please refer to the paper for further information.

In 2025 (version 4.0 of FLORES+), the dataset underwent a deep revision described above.
