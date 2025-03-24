# Dataset card

## Description

FLORES+ devtest set in the Valencian dialect of Catalan

## License

CC-BY-SA-4.0

## Attribution

```bibtex
@inproceedings{wmt24-spain,
    title="Expanding the FLORES+ Multilingual Benchmark with Translations for {Aragonese, Aranese, Asturian, and Valencian}",
    author="Juan Antonio Perez-Ortiz and Felipe S{\'a}nchez-Martínez and Víctor M. S{\'a}nchez-Cartagena and Miquel Esplà-Gomis and Aaron Galiano Jimenez and Antoni Oliver and Claudi Aventín-Boya and Alejandro Pardos and Cristina Valdés and Jus{\'e}p Loís Sans Socasau and Juan Pablo Martínez",
    booktitle = "Proceedings of the Ninth Conference on Machine Translation",
    month = nov,
    year = "2024",
    address = "Miami, USA",
    publisher = "Association for Computational Linguistics"
}
```

With the support of the project CENID2023/10, funded by Diputació d'Alacant; and the R+D+i project PID2021-127999NB-I00 (LiLowLa: Lightweight neural translation technologies for low-resource languages), funded by MCIN /AEI /10.13039/501100011033 / FEDER, UE.

## Language codes

* ISO 639-3: cat
* ISO 15924: Latn
* Glottocode: vale1252

## Additional language information

* [LanguageTool](https://languagetool.org/ca) grammar corrector
* [Llista diatòpica del lèxic català](https://ca.wikipedia.org/wiki/Llista_diat%C3%B2pica_del_l%C3%A8xic_catal%C3%A0): list of lexical items that change between the different dialects of the Catalan language
* [Diccionari normatiu valencià](https://www.avl.gva.es/lexicval/): dictionary of the Valencian Language Academy
* [Criteris lingüístics per als usos institucionals de les universitats valencianes](https://sl.ua.es/en/assessorament/documentos/criteris-linguistics.pdf): Linguistic criteria for the institutional use of Valencian dialect in the Valencian universities


## Workflow

The dataset was created by adapting the existing Catalan version of the FLORES+ devtest set. The work was carried out by a single native speaker of the Valencian dialect. The native speaker holds a Ph.D. and has experience in translating into Valencian and reviewing texts in Valencian. 

In order to speed up the process, LanguageTool was used to introduce an initial set of changes to the original text. Then, all these changes were manually checked, and other required changes were manually applied, taking into account the aforementioned list of lexical items that change between the different dialects of the Catalan language. In case of doubt, the dictionary of the Valencian Language Academy was checked.

## Additional guidelines

Linguistic criteria for the institutional use of the Valencian dialect in the Valencian universities were followed.

