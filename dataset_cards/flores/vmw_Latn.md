# Dataset card

## Description

FLORES+ dev and devtest set in Emakhuwa

## License

CC-BY-SA-4.0

## Attribution

```bibtex
@inproceedings{wmt24-emakhuwa,
    title="Expanding {FLORES+} Benchmark for more Low-Resource Settings: {Portuguese-Emakhuwa} Machine Translation Evaluation",
    author="Felermino Dario Mario Ali and Henrique Lopes Cardoso and Rui Sousa-Silva",
    booktitle = "Proceedings of the Ninth Conference on Machine Translation",
    month = nov,
    year = "2024",
    address = "Miami, USA",
    publisher = "Association for Computational Linguistics"
}
```

## Language codes

* ISO 639-3: vmw
* ISO 15924: Latn
* Glottocode: cent2033

## Workflow

Data was translated from Portuguese by 2 translators, all bilingual speakers of the languages. All translators were professional translators. 100% of the data was checked by three more independent translator.

The workflow is divided into three main steps:

1. **Data Preparation**: 
   - Sentences from the *devtest* and *dev* sets are compiled into segments and loaded into the Matecat CAT tool.
   - Guidelines and a glossary were prepared to standardize the translation process. The guidelines were adapted from the OLDI guidelines and written in Portuguese, focusing on the central variant of Emakhuwa. The glossary was created by digitizing existing bilingual dictionaries and a glossary from Radio of Mozambique, ensuring consistent translations and minimizing loanword use.

2. **Translation**:
   - The translation tasks were divided between two translators. They used a spell checker system to identify potential misspellings, which were then corrected based on feedback.
   
3. **Validation**:
   - This step included revision and judgments. The translated works were exchanged between translators for post-editing.
   - Direct Assessment was also used, where three raters evaluated the translation's adequacy on a scale from 0 to 100, to measure how well the translations preserved the original meaning.

## Additional guidelines

We also requested translators to mark loanwords that were adapted into Emakhuwa during the translation of each segment.
