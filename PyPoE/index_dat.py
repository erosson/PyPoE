# Generate a list of all .dat file names, based on PyPoE specifications.
# Run me from the PyPoE package directory! `scripts/dist` copies me there.
from poe.file.specification.data.stable import specification
import json

print(json.dumps(list(specification.keys()), indent=4))
