# Dataset card for Ladin (Val Badia)

## Description

FLORES+ dev and devtest sets in Ladin (Val Badia).

## License

CC-BY-SA-4.0

## Attribution

These translations were created as part of a collaboration project between the [University of Innsbruck](https://www.uibk.ac.at/en/theoretical-computer-science/research/projects/#MTladin) and the [Ladin Cultural Institute "Micurá de Rü"](https://www.micura.it/en/) led by
Samuel Frontull (samuel.frontull@uibk.ac.at).

If you use this dataset, please cite:
```bibtex
@inproceedings{frontull-etal-2025-bringing,
    title = "Bringing {L}adin to {FLORES}+",
    author = {Frontull, Samuel  and
      Str{\"o}hle, Thomas  and
      Zoli, Carlo  and
      Pescosta, Werner  and
      Frenademez, Ulrike  and
      Ruggeri, Matteo  and
      Valentin, Daria  and
      Comploj, Karin  and
      Perathoner, Gabriel  and
      Liotto, Silvia  and
      Anvidalfarei, Paolo},
    editor = "Haddow, Barry  and
      Kocmi, Tom  and
      Koehn, Philipp  and
      Monz, Christof",
    booktitle = "Proceedings of the Tenth Conference on Machine Translation",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.wmt-1.81/",
    pages = "1061--1071",
    ISBN = "979-8-89176-341-8",
    abstract = {Recent advances in neural machine translation (NMT) have opened new possibilities for developing translation systems also for smaller, so-called low-resource, languages. The rise of large language models (LLMs) has further revolutionized machine translation by enabling more flexible and context-aware generation. However, many challenges remain for low-resource languages, and the availability of high-quality, validated test data is essential to support meaningful development, evaluation, and comparison of translation systems. In this work, we present an extension of the FLORES+ dataset for two Ladin variants, Val Badia and Gherd{\"e}ina, as a submission to the Open Language Data Initiative Shared Task 2025. To complement existing resources, we additionally release two parallel datasets for Gherd{\"e}ina{--}Val Badia and Gherd{\"e}ina{--}Italian. We validate these datasets by evaluating state-of-the-art LLMs and NMT systems on this test data, both with and without leveraging the newly released parallel data for fine-tuning and prompting. The results highlight the considerable potential for improving translation quality in Ladin, while also underscoring the need for further research and resource development, for which this contribution provides a basis.}
}
```

## Language codes

* ISO-639-3: lld
* ISO 15924: Latn
* Glottocode: ladi1250

## Additional language information

* IETF BCP 47: lld_valbadia
* The translations in this dataset follow the "Val Badia" standard of the Ladin language.
* [Institute for Ladin Culture (Micurá de Rü)](https://www.micura.it/en/)
* [Ladin (Val Badia) Spellchecker - Web](https://itavalbadia.ladinternet.it/), developed by [smallcodes](https://smallcodes.com/index.php/en/portfolio-items/spellcheckers/).
* [Ladin (Val Badia) Spellchecker - LibreOffice Extension](https://extensions.libreoffice.org/en/extensions/show/41981)
* [Ladin Dictionaries](https://www.micura.it/en/dictionaries)
* [Machine translation system for Ladin](https://tradutur-informatik.uibk.ac.at/)

## Workflow

Professional translators, all affiliated with the [Ladin Cultural Institute "Micurá de Rü"](https://www.micura.it), were involved in making the FLORES dataset available in Ladin (Val Badia).
The Ladin translation dataset was created by translating the existing FLORES+ dev and devtest sets from English into Ladin.
The texts from the FLORES+ dataset were divided into kits of 25 sentences, which were imported into a dedicated tool accessible to each translator. This tool featured basic spell-checking functions to minimise typos and enhance the accuracy of the translations. On average, each translator worked on two kits per week. The translation process took 10 weeks to complete.
Following the translation phase, each text underwent a review by a native speaker who suggested revisions. These revisions were then applied by the professional translators.


## Additional guidelines

All translators have been provided with the guidelines from [OLDI](https://oldi.org/guidelines#translation-guidelines) and have agreed to use the English texts as reference translations.
