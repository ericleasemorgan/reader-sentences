

Reader Sentences
==================

**tl;dnr**  This suite of software is akin to a back-of-the-book index but on steroids. It is a tool for reading.


Introduction
------------

This directory contains a suite of software used to index and then search databases of sentences, and its purpose is to faciliate a question/answer interface to Distant Reader study carrels. For example, you could ask the system "Who killed Hector?" and get back an answer something like this:

> In the context of the story, it is clear that Hector was killed by
Achilles. The passage mentions several instances where Hector is injured
or threatened by Achilles, including when Achilles "struck him with a
spear and gave him a wound in the groin" (lines 170-171) and when he
"dragged him away to cut off his head and take the body to fling before
the dogs of Troy" (line 234). Additionally, the passage states that
Hector was killed by Achilles, with the fatal blow delivered under the
Trojan wall (line 258).

Alternatively, you could ask the system "What is knowledge?", and get back something like this:

> In this context, knowledge is seen as an existing entity that cannot be
created or formed, but rather derived from experience. The mind interacts
with its environment to gain knowledge, and all knowledge is based on
personal experience. Knowledge is not just theoretical or contemplative,
but also practical and applicable in the world. However, it is recognized
that knowledge itself depends on a level of "strategic ignorance" to reach
manageable conclusions. While information can be a tool for generating
knowledge, knowledge belongs only to an individual person. The concept
of knowledge is closely tied to the idea of self-knowledge, which can
only be realized through face-to-face encounters with others.

**Very important!** This system is not intended nor expected to return <em>the</em> answers to given questions. Instead it is intended to return <em>plausible</em> answers, and you are expected to use the results as discussion points or to use traditional reading techniques for the purpose of verification.

Think of this system as a tool to suppliment your reading. Create a collection of texts, index (model) the collection, search the index, interact with the model, and in the end, garner a better understanding of the collection. Think of the whole process as a sort of interactive discussion with a book. As such, this system implemements a form of reading. 


(Not So) Quick Start
--------------------

First, you will need to install the Distant Reader Toolbox:

    pip install reader-toolbox

Then you will need to create and/or download at least one Distant Reader study carrel. For example, download the Iliad and the Odyssey by Homer:

	rdr download author-homer-gutenberg

Next, you will need to install Reader Sentences scripts:

    git pull https://github.com/ericleasemorgan/reader-sentences.git

Change directories to the just downloaded repository:

	cd reader-sentences

Now, read and cache all the sentences in a given study carrel:

	./bin/carrel2sentences.py author-homer-gutenberg

At this stage, it is quite likely there will be missing Python modules. Do you best to install them.

The next step is to vectorize ("index") the sentences:

	./bin/vectorize.py author-homer-gutenberg
	
Again, it is quite likely you will have missing Python modules and/or you will have missing HuggingFace models. Do your best to install the modules. To resolve the issues with the HuggingFace models, create a HuggingFace account, get a HuggingFace token, and create an environment variable with the name "HF_TOKEN" with the token's value. Repeat the previous step, and please be patient; this step is computationally expensive.

Once you get this far, you can query the database of vectorized sentences. The following command queries the study carrel named "author-homer-gutenberg" for the word "hector" and returns thirty-two sentences:

	./bin/search.sh author-homer-gutenberg hector 32

The result ought be a long paragraph thirty-two sentences in length. Each sentece ought to allude to Hector in some way, shape, or form.

One way to make more sense of the long paragraph is to divide it into smaller paragraphs, like this:

	./bin/format.sh

Another way to make more sense of the long paragarph is to use a large-langauge model to summarize it:

	./bin/summarize.sh

The previous step requires the installation of Ollama and a large-language model called "Llama2". Alas?

Finally, you can use the following command to actually submit a question to be addressed by the system. For example:

	./bin/elaborate.sh 'who killed hector'
	

	
Usage
-----

This suite of software is made up many little Python scripts and Bash front-ends. This first list of scripts are the most used:

* `./bin/carrel2sentences.py` - given the name of study carrel, extract and cache each of the sentences in each of the carrel's items

* `./bin/vectorize.py` - given the name of a study carrel, vectorize ("index") the cached sentences

* `./bin/search.py` - given a study carrel, a query, and an integer (N), search the carrel's database and return N sentences while simultaneously caching the results in the ./etc directory

* `./bin/search.sh` - a front-end to `./bin/search.py`; simply reformats the results into a single paragraph

* `./bin/format.py` - takes the cached result of `./bin/search.py`, compares each sentence to it's subsequent sentence, and (usually) outputs many smaller paragraphs instead of just one

* `./bin/format.sh` - a front-end to `./bin/search.py`; simply reformats the results to include a few blank lines for readability

* `./bin/summarize.py` - takes the cached result of `./bin/search.py`, and uses a large-language model to summarize the cache

* `./bin/elaborate.py` - given a query in the form of a question, uses the cached result of `./bin/search.py` to address the given question; as such, this script is a simple implemenation of a retrieval-augmented generation (RAG) application

* `./bin/elaborate.sh` - a front-end to `./bin/elaborate.py`; simply adds a few blank lines to the output for readability purposes


Queries can be of just about any length and require zero syntax. That said, it is oft-times difficult to articulate useful, meaningful, or comprehensive queries. The scripts below use extracted features from the given study carrel to create queries for you:

* `./bin/search-with-unigrams.sh` - given the name of a study carrel, an integer (N), and another integer (D), identifies the N-most frequent unigrams in the given carrel, uses them as the query for `./bin/search.py`, and returns D sentences

* `./bin/search-with-nouns.sh` - just like `./bin/search-with-unigrams.sh` but identifies the given carrel's N-most frequent nouns instead of unigrams

* `./bin/search-with-keywords.sh` - just like `./bin/search-with-unigrams.sh` but identifies the given carrel's N-most frequent keywords instead of unigrams

* `./bin/search-with-entities.sh` - given the name of a carrel, the value "PERSON" or "ORG", an integer (N), and another integer (D), identify the given carrel's N-most frequent persons or organizations, uses them as the query for `./bin/search.py`, and returns D sentences

* `./bin/search-with-semantics.sh` - given a carrel, a word, an integer (I), and other integer (D), identify the N-most semantically related words to the given word, uses the given word and the related words as the query to `./bin/search.py`, and output D sentences


In natural langaue processing, a set of stop words is a list of words with no or little importance. Examples usually include the words "the", "a", "an", "of", etc. Conversely, one might articulate a list of very useful words -- word of great significance. Such a set of words is sometimes called a "lexicon". If you create a file named ./etc/lexicon within your study carrel(s), then the following scripts will use the file as a part of their input:

* `./bin/search-with-lexicon.sh` - given a study carrel and an integer (D), use the carrel's lexicon as the query for `./bin/search.py` and outputs D sentences

* `./bin/search-with-modals.sh` -  given a study carrel, reads the carrel's lexicon and outputs all sentences where the lexicon words are the subject of the sentence, and the verb of the sentence is a modal verb; good for identifying very assertive sentences

* `./bin/search-with-verb.py` - given a carrel and a lematize verb, find all sentences whose subject is a lexicon word and whose verb is a form of the verb

* `./bin/search-with-verb.sh` - a front-end to `./bin/search-with-verb.py`, and merely adds some formatting to the output


The following two scripts help you to define words. They do not output <em>the</em> defintion of words but rather <em>plausible</em> definitions:

* `./bin/define.py` - given a carrel and a words, finds all sentences containing the given word, uses the Lesk Algorithm to predict the word's defintion, and output possible defintions of the word and their frequencies

* `./bin/concordance.sh` - given the name of a study carrel and a word/phrase, output a list of sentence-like thing containin the word/phrase

The following is a miscelleneous script:

* `./bin/pose-a-question.py` - given the name of a carrel, randomly select a question from it's database of sentences


The following scripts are just for fun. They employ a Markov modeling technique to pseudo-randomly generate sentences. Use these scripts to become familiar with the common bigrams (two-word phrases) in the given carrel.

* `./bin/markov2sentences.py` - given the name of a carrel, a two-word phrase, and an integer, parse the text of the given carrel, and output the given phrase and common two-word phrases that <em>may</em> follow it; the integer denotes how many times the process should be repeated.

* `./bin/tell-a-story.py` - given the name of a carrel, randomly select an item from it, model the text, and output two paragraphs of pseudo-sentences

* `./bin/tell-a-story.sh` - a front-end to `./bin/tell-a-story.py`, and merely adds some formatting to the output


Case study
----------


Summary
-------

This suite of software is as tool for reading. Create and/or download Distant Reader study carrels ("data sets"). Extract and cache all of the sentences in all of the items in the carrel. Vectorize (index/model) them. Use the scripts in this distribution to query the sentences and thus become familar with the carrel's content. Compare and contrast the results with other study carrel of similar content. Use the results as points of dicussion with other people.

---
Eric Lease Morgan &lt;eric_morgan@infomotions.com&gt;  
June 18, 2025