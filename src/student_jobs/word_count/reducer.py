from src.core.job.reducer import Reducer


class WordCountReducer(Reducer):
    def reduce(self, key, values, emit):
        if key in ("total_words", "long_words"):
            emit(key, sum(values))
        else:


            total_v = sum(v for v, c in values)
            total_c = sum(c for v, c in values)
            count = len(values)
            avg_v = round(total_v / count, 2) if count else 0
            avg_c = round(total_c / count, 2) if count else 0


            emit(key, f"vowels: {avg_v}%    consonants: {avg_c}%")
