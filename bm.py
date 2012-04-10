#!/usr/bin/python env

# benchmark some urls


import requests
import datetime

def fetch (url):
    start = datetime.datetime.utcnow ()
    response = requests.get (url, allow_redirects=False)
    stop = datetime.datetime.utcnow ()
    duration = stop - start
    print "%dms\t%d\t%s" % (duration.total_seconds () * 1000.0, response.status_code, url)

    if response.headers['Location']:
        fetch (response.headers['Location'])


def total (url):
    start = datetime.datetime.utcnow ()
    fetch (url)
    stop = datetime.datetime.utcnow ()
    duration = stop - start
    print "%dms\ttotal duration" % (duration.total_seconds () * 1000.0)
    return duration.total_seconds ()


def average (url, tries):

    results = []
    for attempt in xrange(tries):
        results.append (total (url))

    print "------------------------------------"
    print "URL:     %s" % (url)
    print "Count:   %d" % (len (results))
    print "Min:     %dms" % (min (results) * 1000.0)
    print "Max:     %dms" % (max (results) * 1000.0)
    print "Average: %dms" % (sum (results) * 1000.0 / tries)

url1 = "http://archive.org/download/mbid-aff4a693-5970-4e2e-bd46-e2ee49c22de7/mbid-aff4a693-5970-4e2e-bd46-e2ee49c22de7-379410348.jpg"
url2 = "http://s3.us.archive.org/mbid-aff4a693-5970-4e2e-bd46-e2ee49c22de7/mbid-aff4a693-5970-4e2e-bd46-e2ee49c22de7-379410348.jpg"

tries = 20

average (url1, tries)
print "\n\n"
average (url2, tries)
