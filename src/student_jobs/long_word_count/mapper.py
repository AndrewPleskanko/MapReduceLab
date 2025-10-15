import re
from src.core.job.mapper import Mapper

class LongWordMapper(Mapper):
    def map(self, record, emit):
        words = re.findall(r'\b\w+\b', str(record).lower())
        for word in words:
            if len(word) > 5:
                emit("long_words", 1)