import pprint
pp = pprint.PrettyPrinter(indent=0)
import language_filter
from first_line import word_generator as first_line
from second_line import word_generator as second_line

first_line_words = first_line.find_words()
filtered_first_line_words = language_filter.filter_words(first_line_words)
with open("./first_line/corpus.py", "a+") as first_line_corpus:
    first_line_corpus.write("beluga_sevruga={}".format(filtered_first_line_words))

second_line_words = second_line.summon_seas()
filtered_second_line_words = language_filter.filter_words(second_line_words)
with open("./second_line/corpus.py", "w") as second_line_corpus:
    second_line_corpus.write("caspian_sea=")
    second_line_corpus.write(pp.pformat(filtered_second_line_words))
