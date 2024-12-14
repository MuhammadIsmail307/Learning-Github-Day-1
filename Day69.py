# Creating command line utility in python


# lecture 85



# command - oder - order name


import argpasrse
import requests

def DownloadFile(url, local_filename):
    local_filename = url.split('/')[-1]
    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()
    return 

parser = argpasrse.ArgumentParser()


# add command line arguments

parser.add_argument("url1", help="Url of the file you want to download")
parser.add_argument("Output", help="By which name you want to save the file")

# parse the arguments

args = parser.parse_args()


# Use the arguments in your code

print(args.url1)
DownloadFile(args.url1, args.Output)



# TIPS  --->  Use stackoverflow for updated code 