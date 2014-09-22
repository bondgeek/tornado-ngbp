import sys
import inspect
import os

BASE_PATH = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
sys.path.insert(0, BASE_PATH)

import server.app

if __name__=="__main__":
    if len(sys.argv) == 2:
        port = sys.argv[1]
    else:
        port = 8888

    server.app.run(port=port)