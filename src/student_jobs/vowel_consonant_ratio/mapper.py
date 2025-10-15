import re
from src.core.job.mapper import Mapper

class VowelConsonantMapper(Mapper):
    vowels = set("aeiouаеєиіїоуюя")

    def map(self, record, emit):
        words = re.findall(r'\b\w+\b', str(record).lower())
        for word in words:
            vowels = sum(1 for c in word if c in self.vowels)
            consonants = sum(1 for c in word if c.isalpha() and c not in self.vowels)
            emit(len(word), (vowels, consonants))
