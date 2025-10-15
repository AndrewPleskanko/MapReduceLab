from src.core.job.reducer import Reducer

class VowelConsonantReducer(Reducer):
    def reduce(self, key, values, emit):
        total_vowels = total_consonants = 0
        count = 0
        for v, c in values:
            total_vowels += v
            total_consonants += c
            count += 1

        if count > 0:
            vowel_ratio = (total_vowels / (total_vowels + total_consonants)) * 100
            consonant_ratio = 100 - vowel_ratio
            emit(f"{key} symbols", f"{vowel_ratio:.1f}% vowels, {consonant_ratio:.1f}% consonants")
