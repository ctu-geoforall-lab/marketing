#!/usr/bin/env python3

import os
import sys
import uuid

if len(sys.argv) < 2:
    sys.exit("Provide number of uuids to be generated")

for n in range(int(sys.argv[1])):
    print ('{}{}'.format(uuid.uuid4(), os.linesep))
