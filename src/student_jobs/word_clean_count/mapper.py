import re
from src.core.job.mapper import Mapper

class CleanWordCountMapper(Mapper):
    def map(self, record, emit):

        words = re.findall(r'\b\w+\b', str(record).lower())
        for word in words:
            emit(word, 1)