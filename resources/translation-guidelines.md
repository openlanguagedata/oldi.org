# Translation guidelines

These translation guidelines must be acknlowedged by all translators who will be contributing data.

> ![NOTE]
> The latest version of these guidelines is available at <a href="https://oldi.org/translation-guidelines.pdf">https://oldi.org/translation-guidelines.pdf</a>.

## Important note

Your translations will be used to help train or evaluate machine translation engines. For this reason, this project requires **human translation**.

* If you are translating data to be used for evaluation purposes, such as for FLORES+, using or even referencing machine translation output is not allowed (this includes post-editing).
* If you are translating data to be used for training purposes, such as Seed, the use of post-edited machine translated content is allowed, provided all data is manually verified and edited where necessary.

> ![CAUTION]
> Some commercial machine translation or LLM services – including DeepL, Google Translate, ChatGPT, Claude and Gemini – prohibit the use of their output for training other translation or AI models. Their use is not permitted.

## General guidelines

1. You will be translating sentences coming from different sources. Please refer to the source document if available.
2. Do not convert any units of measurement. Translate them exactly as noted in the source content.
3. When translating, please maintain the same tone used in the source document. For example, encyclopedic content coming from sources like Wikipedia should be translated using a formal tone.
4. Provide fluent translations without deviating too much from the source structure. Only allow necessary changes.
5. Do not expand or replace information compared to what is present in the source documents. Do not add any explanatory or parenthetical information, definitions, etc.
6. Do not ignore any meaningful text that was present in the source.
7. In case of multiple possible translations, please pick the one that makes the most sense (e.g., for gender concordance, cultural fit in the target language, level of formality, etc.).
8. Translations must be faithful to the source in terms of pragmatics such as (if applicable) level of hedging/modality, sentiment and its intensity, negation, speech effects (disfluencies), etc.
9. For proper nouns and common abbreviations, please see the guidelines on Named Entities below.
10. Idiomatic expressions should not be translated word for word. Use an equivalent idiom, if one exists. If no equivalent idiom exists, use an idiom of similar meaning. If no similar expressions exist in the target language, paraphrase the idiom such that the meaning is retained in the target language.
11. When a pronoun to be translated is ambiguous (for instance, when it could be interpreted as either _him/her_ or _he/she_), opt for gender neutral pronouns (such as _them/they_) if those exist in the target language. However, when a pronoun to be translated is clearly marked for gender, you should follow the source material and continue to mark for gender.
12. Foreign words and phrases used in the text should be kept in their original language when this is necessary to preserve the meaning of the sentence (e.g. if given as an example of a foreign word).

## Named entities

Named entities are people, places, organisations, etc., that are commonly referred to using a proper noun. This section provides guidance on how to handle named entities. Please review the following guidelines carefully:

1. If there is a commonly used term in the target language for the Named Entity:
   1. If the most commonly used term is the same as in the source language, then keep it as it is.
   2. If the most commonly used term is a translation or a transliteration, then use that.
2. If there is no commonly used term:
   1. If possible, a transliteration of the original term should be used.
   2. If a transliteration would not be commonly understood in the context, and the source term would be more acceptable, you may retain the original term.
