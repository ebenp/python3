# -*- coding: utf-8 -*-
'''
script to bulk upload urls to the wayback machine ('https://web.archive.org/save/[url])
from a csv file with optional header
__author__ = Eben Pendleton
__date__ = 2/5/18
History:
2/5/18 initally written
'''
import csv
import requests
import time

def readurl_from_csv_upload(csvfile,uploadUrl,header = True):
    '''
    function to bulk upload urls given a csv file with optioonal
    header
    csvfile: csv file with optional header
    uploadUrl: upload url that will be prepended
    returns: nothing
    checks status code of response
    '''
    # read in csvfile
    with open(csvfile, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        # loop through file rows
        for row in reader:
            # if file has a header row contine past the first iteration
            # update the header status
            if header == True:
                header = False
                continue
            # try the url
            r=requests.get(uploadUrl+row[0])
            # error check. If all is well the status codes should
            # all be ok
            assert r.status_code == requests.codes.ok
            # sleep 5 seconds
            time.sleep(5)

if __name__ == "__main__":
    # test case
    csvfile='urls.csv'
    uploadUrl='https://web.archive.org/save/'
    readurl_from_csv_upload(csvfile,uploadUrl)
    # print completion
    print('DONE!')
