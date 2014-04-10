import os
import sqlite3
import urllib2
import random
from rottentomatoes import RT
import json
from StringIO import StringIO

#####
##### SETTINGS
#####

rt_api_key = "your-key-here"

#####
##### UPC TO ID MAPPING
#####


response = urllib2.urlopen('http://i.rottentomatoes.com/syndication/links/movies_upc.txt')
id_url_map = response.read().split("\n")
response.close()

movie_url_dict = {'UPC':'ID'}

for row in id_url_map:
    movie_line = row.split("\t")
    if len(movie_line) == 2:
        movie_url_dict[movie_line[1]] = movie_line[0] # 1 = UPC, 0 = RT ID
    else:
        pass

#####
##### FIND THE MOVIE
#####

def get_upc(default):
    upc = raw_input("Enter UPC: ")
    if upc == "":
        upc = default
        
    if upc in movie_url_dict:
        return movie_url_dict[upc]
    else:
        print "UPC not found. Try again."
        return get_upc(default)

print "Rotten Tomatoes UPC to IDs loaded"

known_id = random.choice(movie_url_dict.keys())
movie_id = get_upc(known_id)

#####
##### ACCESS & READ THE MOVIE DATA
#####

movie_data_core = RT(rt_api_key).info(movie_id)
movie_data_cast = RT(rt_api_key).info(movie_id, 'cast')
movie_data_reviews = RT(rt_api_key).info(movie_id, 'reviews')


print "\n\n\n ================================= \n"
print "          CORE"
print "\n ================================= \n"

print json.dumps(movie_data_core, sort_keys=True, indent=10)

print "\n\n\n ================================= \n"
print "          CAST"
print "\n ================================= \n"

print json.dumps(movie_data_cast, sort_keys=True, indent=10)

print "\n\n\n ================================= \n"
print "          REVIEWS"
print "\n ================================= \n"

print json.dumps(movie_data_reviews, sort_keys=True, indent=10)










