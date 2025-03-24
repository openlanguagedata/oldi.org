# Dataset card

## Description

FLORES+ dev and devtest sets in Aragonese.

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

With the support of the R+D+i projects PID2021-127999NB-I00 (LiLowLa: Lightweight neural translation technologies for low-resource languages) and PID2021-124663OB-I00 (TAN-IBE: Neural Machine Translation for the Romance languages of the Iberian Peninsula), funded by MCIN /AEI /10.13039/501100011033 / FEDER, UE.

## Language codes

* ISO-639-3: arg
* ISO 15924: Latn
* Glottocode: arag1245

## Additional language information

* [Academia de l'Aragonés](http://www.academiadelaragones.org)
* [Orthography of Aragonese](https://academiaaragonesadelalengua.org/sites/default/files/ficheros-pdf/ortografia-de-laragones_web_an.pdf), published by EFA-ACAR (Estudio de Filología Aragonesa – Academia de l’Aragonés). 
*  [Grammar of Aragonese](http://www.academiadelaragones.org/biblio/Edacar10_GBAprovisional.pdf), published by EFA-ACAR.
* [Dictionary of Aragonese](http://www.academiadelaragones.org/biblio/Edacar13.pdf) published by EFA-ACAR. 
* Aragonese dictionary [Tresoro d'a Luenga Aragonesa](http://diccionario.sipca.es/fabla/faces/index.xhtml).
* Spanish--Aragonese and Aragonese--Spanish dictionary  [Aragonario](\url{https://aragonario.aragon.es/), developed under the project LINGUATEC and published by the Government of Aragon. 
* [Spanish-Aragonese machine translation system](https://github.com/apertium/apertium-spa-arg)

## Workflow

The data for Aragonese was initially translated from Spanish using the Spanish-Aragonese Apertium rule-based machine translation system. This translation was subsequently post-edited by specialists proficient in Aragonese. The utilization of machine translation is justified for two reasons: firstly, the two-step workflow consisting of machine translation followed by post-editing is prevalent for this language, with many existing texts being produced this way; secondly, sourcing linguists or translators for Aragonese proved challenging due to their scarcity, making it difficult to complete the task within the required timeframe.

Finally, the post-edited translation was reviewed by a member of the *Academia Aragonesa de la Lengua*. In this last step, the reviewer had also in view the English version of the FLORES+ dataset; an important number of translations were modified for better agreement with English original data.  

## Additional guidelines

The guidelines provided by the Academia de l'Aragonés were followed to ensure that the translation into Aragonese aligned with their recommendations.
