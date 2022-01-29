from asyncio import subprocess
from importlib.abc import Traversable
import uuid
import random
import subprocess

subprocess.call("color a", shell=True)

while True:
    id = str(uuid.uuid4())
    trimmed = id[:random.randint(0, len(id)-1)]
    spaces = " " * random.randint(0,15)
    print(f"{spaces}{trimmed}")