# Dataset card

## Description

FLORES+ dev and devtest sets in Aranese.

## License

CC-BY-SA-4.0

## Attribution

```bibtex
@inproceedings{wmt24-erzya,
    title="FLORES+ translation and machine translation evaluation for the {E}rzya language",
    author="Isai Gordeev and Sergey Kuldin and David Dale",
    booktitle = "Proceedings of the Ninth Conference on Machine Translation",
    month = nov,
    year = "2024",
    address = "Miami, USA",
    publisher = "Association for Computational Linguistics"
}
```

With the support of the R+D+i projects PID2021-127999NB-I00 (LiLowLa: Lightweight neural translation technologies for low-resource languages) and PID2021-124663OB-I00 (TAN-IBE: Neural Machine Translation for the Romance languages of the Iberian Peninsula), funded by MCIN /AEI /10.13039/501100011033 / FEDER, UE.

## Language codes

* ISO-639-3: oci
* ISO 15924: Latn
* Glottocode: aran1260

## Additional language information

* [Institut d'Estudis Aranesi](https://en.wikipedia.org/wiki/Aranese_dialect)
* [Catalan-Aranese machine translation system](https://github.com/apertium/apertium-oci-cat)
* [Dictionary for Aranese](http://www.institutestudisaranesi.cat/wp-content/uploads/2021/04/DICCIONARI-DER-ARAN%C3%89S.pdf); [erratum 2021](http://www.institutestudisaranesi.cat/wp-content/uploads/2020/12/ERRATA-WEB.pdf); [extension 2021](http://www.institutestudisaranesi.cat/wp-content/uploads/2020/12/500-1-g%C3%A8r-2021-WEB.pdf); [extension 2022](http://www.institutestudisaranesi.cat/wp-content/uploads/2022/01/WEB-AMPLIACION-01-01-2022.pdf); [extension 2023](http://www.institutestudisaranesi.cat/wp-content/uploads/2023/03/Ampliacion-2023.pdf)
* [Grammar for Aranaese](http://www.institutestudisaranesi.cat/wp-content/uploads/2021/04/gramatica-aranes.pdf)
* [Orthographic vocabulary](http://www.institutestudisaranesi.cat/wp-content/uploads/2019/11/33520-vocabulari-ortografic.pdf)
* [Winter sports vocabulary](http://www.institutestudisaranesi.cat/wp-content/uploads/2019/11/33288-vocabulari-esports-iuern.pdf)
* [Computer and informatics vocabulary](http://www.institutestudisaranesi.cat/wp-content/uploads/2018/11/TECNOLOGIA.pdf)
* [Aranese verbs](http://www.institutestudisaranesi.cat/wp-content/uploads/2019/11/33287-els-ve%CC%80rbs.pdf)

## Workflow

The data was initially translated from Catalan using the Apertium rule-based machine translation system for Catalan-Aranese. The translation was then manually post-edited by native speakers of Aranese with three years of experience translating texts on diverse topics into Aranese. Finally, the post-edited translation was reviewed by different individuals, who are also native speakers, from the Institut d'Estudis Aranesi.

The data was initially obtained by translating the sentences in the Catalan FLORES+ dev and devtest datasets using the Apertium rule-based MT system for Catalan-Aranese. A revision process was then performed in two steps. Firstly, a professional reviewer with wide experience in translation and revision with proficiency in Aranese was presented with the French, Catalan and Occitan versions of the FLORES+, along with the machine translated version into Aranese. Finally, the post-edited translation was reviewed by different individuals, who are native speakers, from the Institut d'Estudis Aranesi (IEA). 

The utilization of machine translation is justified for two reasons: firstly, the two-step workflow consisting of machine translation followed by post-editing is prevalent for this language, with many existing texts being produced this way; secondly, sourcing linguists or translators for Aranese proved challenging due to their scarcity, making it difficult to complete the task within the required timeframe.

## Additional guidelines

The guidelines provided by the Institut d'Estudis Aranesi were followed to ensure that the translation into Aranese aligned with their recommendations.
