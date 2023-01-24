#!/usr/bin/env python3

import os
import json

print("Content Type: aplication/json")
print()
#print(os.environ)
print(json.dumps(dict(os.environ), indent=2))
