import re
from src.core.job.mapper import Mapper


class WordCountMapper(Mapper):
    def map(self, record, emit):
        text = str(record).lower()
        words = re.findall(r"[a-zA-Zа-яА-ЯєЄіІїЇґҐ']+", text)


        total_words = len(words)
        long_words = sum(1 for w in words if len(w) > 5)
        emit("total_words", total_words)
        emit("long_words", long_words)


        vowels_set = set("aeiouаеєиіїоуюя")


        for word in words:
            length = len(word)
            if length == 0:
                continue


            v = sum(1 for c in word if c in vowels_set)
            c = sum(1 for c in word if c.isalpha() and c not in vowels_set)
            total_letters = v + c
            if total_letters == 0:
                continue


            vowels_percent = (v / total_letters) * 100
            consonants_percent = (c / total_letters) * 100


            emit(f"{length}", (vowels_percent, consonants_percent))