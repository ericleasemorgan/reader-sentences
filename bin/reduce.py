#!/usr/bin/env python

# reduce.py - use PCA to reduce a large matrix to only two or three dimensions
# see: https://github.com/AccelAI/AI-Tutorials/blob/main/PCA_Tutorial/PCA_Tutorial.ipynb

# Eric Lease Morgan <eric_morgan@infomotions.com>
# (c) Infomotions, LLC; distributed under a GNU Public License

# March 18, 2026 - first documentation, but written a few days ago
# March 20, 2026 - added command-line input
# March 31, 2026 - removed scaling as well as caching


# configure
CACHE   = 'etc'
VECTORS = 'vectors.pkl'

# require
from matplotlib.pyplot     import scatter, show, figure, savefig
from pathlib               import Path
from pickle                import load
from sys                   import stderr, argv, exit
from sklearn.decomposition import PCA

# get input
if len( argv ) != 2 : exit( 'Usage: ' + argv[ 0 ] + " <2|3>" )
components = int( argv[ 1 ] )

# initialize
cache = Path( CACHE )

# load the vectors
with open( cache/VECTORS, 'rb' ) as handle: X = load( handle )

# initialize PCA, fit the vectors, and cache; do the work
pca         = PCA( n_components=components )
projections = pca.fit_transform( X )

# branch accordingly; visualize
if components == 2 :

	# create a 2d scatter plot
	scatter( projections[ :,0 ], projections[ :,1 ], s=2 )
	
elif components == 3 :
	
	# create a 3d scatter plot; kewl
	figure = figure()
	figure = figure.add_subplot( 111, projection='3d' )
	figure.scatter( projections[ :,0 ], projections[ :,1 ], projections[ :,2 ], s=2 )

else : exit( 'Invalid value for components (%s). Call Eric.' % str( components ) )

# output and done
savefig( '/home/emorgan/practice.png' )
exit()



