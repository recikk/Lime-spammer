# Copyright (C) 2025 recikk
#
# This file is licensed under the GNU General Public License v3.0 (GPL-3.0).
# You are free to use, modify, and distribute this code under the terms of the GPL-3.0 license.
#
# If you modify and/or redistribute this code, you must include the above copyright notice and the license.
#
# WARNING: If you "steal" or "skid" this code (i.e., use it without proper attribution), I can take legal action.
# If you use this code in any way, you assume all responsibility for your actions and any consequences.
# I, recikk, am not responsible for any issues, damages, or problems caused by the use of this code.
# Use it at your own risk.
#
#
# SITE https://getlime.xyz
# SITE https://getlime.xyz
# SITE https://getlime.xyz
# SITE https://getlime.xyz
# SITE https://getlime.xyz
# SITE https://getlime.xyz

version = '1.0'

import os
try:
    import requests
    import tls_client
    import webbrowser
    import ab5
    from colorama import Style as S
    import time
    import re
    import sys
    import random
    import string
    from datetime import datetime as dt
    import threading
    import uuid
    from concurrent.futures import ThreadPoolExecutor
    import traceback

except ModuleNotFoundError as e:
    for lib in [
        'requests',
        'tls_client',
        'webbrowser',
        'ab5',
        'colorama',
        'tls-client',
        'typing-extensions',
        'datetime',
        'uuid'
    ]:
        os.system(f'pip install {lib}')

    import requests
    import tls_client
    import webbrowser
    import ab5
    from colorama import Style as S
    import time
    import re
    import sys
    import random
    import string
    from datetime import datetime as dt
    import threading
    import uuid
    from concurrent.futures import ThreadPoolExecutor
    import traceback

webbrowser.open('https://getlime.xyz')
