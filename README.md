

Reader Sentences
==================

**tl;dnr**  This suite of software is akin to a back-of-the-book index but on steroids.


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

Next, you will need to install these scripts:

    git pull https://github.com/ericleasemorgan/reader-sentences.git

Change directories to the just downloaded repository:

	cd reader-sentences

Now, read and cache all the sentences in a given study carrel:

	./bin/carrel2sentences.py author-homer-gutenberg

At the is stage, it is quite likely there will be missing Python modules. Do you best to install them.

The next step is to vectorize ("index") the sentences:

	./bin/vectorize.py author-homer-gutenberg
	
Again, it is quite likely you will have missing Python modules and/or you will have missing HuggingFace models. Do your best to install the modules. To resolve the issues with the HuggingFace model, create a HuggingFace account, get a HuggingFace token, and create an environment variable with the name "HF_TOKEN" with the token's value. Repeat the previous step, and please be patient; this step is computationally expensive.

Once you get this far, you can query the database of sentences. The following command queries the study carrel named "author-homer-gutenberg" for the word "hector" and returns thirty-two sentences:

	./bin/search.sh author-homer-gutenberg hector 32

The result ought be a paragraph thirty-two sentences long. Each sentece ought to allude to Hector in some way, shape, or form.

One way to make more sense of the long paragraph is to divide it into smaller paragraphs, like this:

	./bin/format.sh

Another way to make more sense of the long paragarph is to use a large-langauge model to summarize it:

	./bin/summarize.sh

The previous step requires the installation of Ollama and a large-language model called "Llama2". Alas?

Finally, you can use the following command to actually submit a question to be addressed by the system. For example:

	./bin/elaborate.sh 'who killed hector'
	
	
Usage
-----


Case study
----------


Summary
-------


---
Eric Lease Morgan &lt;eric_morgan@infomotions.com&gt;  
June 17, 2025