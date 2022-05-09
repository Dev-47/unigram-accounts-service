from .base import *

import os

# specify settings config to use
# default: `dev.py`
# options: ["DEV", "PROD"]

MODE = os.environ.get("MODE")

if MODE == "DEV":
    from .dev import *
else:
    from .prod import *
