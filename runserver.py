#!/usr/local/bin/python
from website import app
from utils import clear, load, load_images
import sys


if __name__ == '__main__':
    if len(sys.argv) == 1:
        app.debug = True
        app.run(host='0.0.0.0', port=5000)
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'clear':
            clear()
        elif sys.argv[1] == 'load':
            load()
        elif sys.argv[1] == 'load_images':
            load_images()
        else:
            print "error starting server: could not interpret argument"
    else:
        print "error starting server: too many arguments"
