#!/usr/bin/env python

# elbow.py - given a 2D matrix, plot KMeans inertia

# Eric Lease Morgan <eric_morgan@infomotions.com>
# (c) Infomotions, LLC; distributed under a GNU Public License

# March 18, 2026 - first documentation, but written a few days ago


# configure
CACHE      = 'etc'
VECTORS    = 'vectors.pkl'
RANGE      = 16
COMPONENTS = 2

from matplotlib.pyplot     import plot, grid, show, savefig 
from pathlib               import Path
from pickle                import load
from sklearn.cluster       import KMeans
from sklearn.decomposition import PCA

# load the previously cached set of vectors
with open( Path( CACHE )/VECTORS, 'rb' ) as handle: X = load( handle )

# initialize PCA and fit the vectors all in one go
X = PCA( n_components=COMPONENTS ).fit_transform( X )

# calculate a list of inertias
inertia = []
for k in range( 1, RANGE ) :

	# fit and update
    kmeans = KMeans( n_clusters=k ).fit( X )
    inertia.append( kmeans.inertia_ )

# plot
plot( range( 1, RANGE ), inertia, marker='o' )
grid( True )

# output and done
savefig( '/home/emorgan/pracrice.png' )
exit()
