import os
import sys
import codecs
import argparse
import urllib.request

parse = argparse.ArgumentParser(description='Download from ImageNet')
parse.add_argument('--file','-f', default='', required=True,
                    help='URL Files')
parse.add_argument('--loop','-l', type=int, default=100,
                    help='No. of Imgs')
parse.add_argument('--name','-n', default='', required=True,
                    help='Name of Diretory')
args = parse.parse_args()

n = 0
f = codecs.open(args.file, 'r', 'utf8', 'ignore')
os.makedirs(args.name, exist_ok=True)


for line in f.readlines():
    n += 1
    try:
        img = urllib.request.urlopen(line[0:-2])
        path = os.path.join(args.name, os.path.basename(line[0:-2]))
        localfile = open(path, 'wb')
        localfile.write(img.read())
        img.close()
        localfile.close()
        print('{}: {}'.format(n, path))
    except Exception as e:
        print(e)

    if n==args.loop:
        sys.exit()
