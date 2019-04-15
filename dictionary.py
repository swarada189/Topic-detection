# Generate a dictionary / vocabulary from a text dataset.

import gensim
import nltk



dataset = 'output-Wales.txt' #Input dataset filename
outfile = 'vocab-Wales.txt' #Output filename. (default='vocab.txt')
threshold = 20 #Word count threshold; excludes words below threshold. (default=20)


def generate(f, outfile, t):
	

	dataset = []

	with open(f,'r',encoding='utf-8') as file:
		dataset = file.readlines()

	toks = []

	for doc in dataset:
		
		toks.append(nltk.word_tokenize(doc))

	
	
	# print "Generating word counts."
	dictionary = gensim.corpora.dictionary.Dictionary(toks)
	bag_of_words = dictionary.doc2bow([i for row in toks for i in row])
	
	# print "Filtering words with less than {0} occurrences.".format(t)
	good_ids = map(lambda y: y[0], filter(lambda x: x[1] > t, bag_of_words))
	dictionary.filter_tokens(bad_ids=None, good_ids=good_ids)
	
	# print "Writing output to {0}.".format(outfile)
	with open(outfile, 'w',encoding='utf-8') as of:
		for word in dictionary.values():
			#word = unicode(word.lower(), "utf-8")
			of.write("%s\n" % word.lower())
	
	# print "Done."

generate(dataset, outfile, threshold)