#!/usr/bin/env python

# cluster.py - given a few configurations, identify centers of clusters in a matrix and plot the results
# see: https://woteq.com/k-means-clustering-in-python-with-scikit-learn

# Eric Lease Morgan <eric_morgan@infomotions.com>
# (c) Infomotions, LLC; distributed under a GNU Public License

# March 18, 2026 - first documentation, but written a few days ago
# March 20, 2026 - started using Sci-Kit Learn
# March 31, 2026 - removed scaling, and required component input
# April  2, 2026 - reading vectors from local cache and saving plot to figures


# configure
VECTORS   = 'vectors.pkl'
LIBRARY   = 'localLibrary'
CLUSTERS2 = 'vectors-clusters-2.png'
CLUSTERS3 = 'vectors-clusters-3.png'

# require
from pathlib               import Path
from pickle                import load
from sklearn.cluster       import KMeans
from sklearn.decomposition import PCA
from sys                   import argv, exit
import matplotlib.pyplot   as plt
from rdr                   import configuration, ETC, FIGURES

# get input
if len( argv ) != 4 : exit( 'Usage: ' + argv[ 0 ] + " <carrel> <clusters> <2|3>" )
carrel     = argv[ 1 ]
clusters   = int( argv[ 2 ] )
components = int( argv[ 3 ] )

# load the previously created projections
with open( configuration( LIBRARY)/carrel/ETC/VECTORS, 'rb' ) as handle: X = load( handle )

# initialize the kmeans, fit, and cache
model = KMeans( n_clusters=clusters, init='k-means++' ).fit( X )

# get the cluster labels and centroids
labels    = model.labels_
centroids = model.cluster_centers_

# use PCA to reduce the vectors to two (or three) components (dimensions) for plotting
centroids = PCA( n_components=components ).fit_transform( centroids )
X         = PCA( n_components=components ).fit_transform( X )

# visualize
if components == 2 :

	plt.scatter( X[ :,0 ], X[ :,1 ], s=4, c=labels )
	plt.scatter( centroids[ :,0 ], centroids[ :,1 ], marker='x', s=200, linewidths=3, color='red' )
	plt.savefig( configuration( LIBRARY)/carrel/FIGURES/CLUSTERS2  )

elif components == 3 :

	figure = plt.figure()
	figure = figure.add_subplot( 111, projection='3d' )
	figure.scatter( X[ :,0 ], X[ :,1 ], X[ :,2 ], s=4, c=labels )
	figure.scatter( centroids[ :,0 ], centroids[ :,1 ], centroids[ :,2 ], marker='x', s=200, linewidths=3, color='red' )
	plt.savefig( configuration( LIBRARY)/carrel/FIGURES/CLUSTERS3  )

# done
exit()

