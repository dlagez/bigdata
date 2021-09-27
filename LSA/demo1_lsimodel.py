from gensim.test.utils import common_dictionary, common_corpus
from gensim.models import LsiModel

print(common_corpus)
print(common_dictionary)

model = LsiModel(common_corpus, id2word=common_dictionary)
vectorized_corpus = model[common_corpus]

