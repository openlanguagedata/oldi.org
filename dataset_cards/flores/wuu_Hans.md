# Dataset card

## Description

FLORES+ dev set in Wu Chinese

## License

CC-BY-SA-4.0

## Attribution

```bibtex
@inproceedings{wmt24-wu,
    title="Machine Translation Evaluation Benchmark for {Wu}",
    author="Hongjian Yu and Yiming Shi and Zherui Zhou and Christopher Haberland",
    booktitle = "Proceedings of the Ninth Conference on Machine Translation",
    month = nov,
    year = "2024",
    address = "Miami, USA",
    publisher = "Association for Computational Linguistics"
}
```

## Language codes

* ISO 639-3: wuu
* ISO 15924: Hans
* Glottocode: suhu1238

## Additional language information

The target Wu variety is the Chongming dialect. The Chongming dialect (or more broadly the Shadi dialect) is a Wu dialect within the Su-Hu-Jia fraction, spoken in Chongming, Haimen and Qidong districts as well as in some areas of Zhangjiagang. Although Chongming belongs to the Manucipality of Shanghai, the dialect is distinctive from the urban variety on many aspects and is known for preserving many rare characteristics of Middle Chinese. Aside from the Shanghai dialect, the Chongming dialect is also similar to other Su-Hu-Jia dialects such as the Suzhou dialect.

A list of language reference goes here:
* 赵元任 (Yuen Ren Chao), 现代吴语的研究 (1956)
* 钱乃荣, 当代吴语研究 (1992)
* 闵家骥 et al., 简明吴方言词典 (1986)
* 钱乃荣, 上海话大词典 (2008)
* Wu Wikipedia [https://wuu.wikipedia.org/wiki/]
* Wu Chinese Forum [https://wu-chinese.com/bbs/]
* Online dictionaries for Wu Chinese [http://wu-chinese.com/minidict/index.php, https://www.wugniu.com/dict]

## Workflow

The FLORES+ Wu dataset is directly translated from English into Wu Chinese. Data were equally distributed and translated by 2 translators, both native speakers of the Chongming dialect, and have earned or are pursuing a university degree in English. Both translators grew up in Chongming; one went to Putuo, Shanghai for high school and college, and the other went to Fengxian, Shanghai for college. They mainly speak Wu at home but also to peers on occasion. They are in touch with the Shanghai urban dialect as well as other local varieties. All translated data were checked by another independent Wu speaker.

## Additional guidelines

The translators mainly used 简明吴方言词典 and then 上海话大词典 if they were unable to recall the orthogonal Hanzi that represent the utterances. Both dictionaries are based on the Shanghainese dialect. When the two dictionaries diverged in orthographies, 简明吴方言词典 was put in priority. When there was phonetic distinctions between the Chongming and Shanghai dialect and the original character was indeterminable, we made sure that the selected Hanzi has aligned pronunciation.
