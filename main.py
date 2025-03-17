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

try:
    socials = requests.get('https://pastebin.com/raw/izgCLWZL').json()
    discord = socials['discord']
    fulldiscord = socials['fulldiscord']

    discordacc = socials['discordacc']
    fulldiscordacc = socials['fulldiscordacc']

    telegram = socials['telegram']
    fulltelegram = socials['fulltelegram']

    telegramacc = socials['telegramacc']
    fulltelegramacc = socials['fulltelegramacc']

    github = socials['github']
    fullgithub = socials['fullgithub']

    site = socials['site']
    fullsite = socials['fullsite']

    store = socials['store']
    fullstore = socials['fullstore']

except:
    discord = 'discord.gg/spamming'
    fulldiscord = 'https://discord.gg/spamming'

    discordacc = 'discordapp.com/users/1326906424873193586'
    fulldiscordacc = 'https://discordapp.com/users/1326906424873193586'

    telegram  = 't.me/limespammer'
    fulltelegram = 'https://t.me/limespammer'

    telegramacc  = 't.me/r3cik'
    fulltelegramacc = 'https://t.me/r3cik'

    github = 'github.com/recikk'
    fullgithub = 'https://github.com/recikk'

    site = 'getlime.xyz'
    fullsite = 'https://getlime.xyz'

    store = 'r3ci.sellhub.cx'
    fullstore = 'https://r3ci.sellhub.cx'

class co:
    def rgb(r, g, b):
        return f'\033[38;2;{r};{g};{b}m'   
     
    green = rgb(7, 242, 109)
    gmain1 = [132, 255, 0]
    gmain2 = [0, 255, 187]

    red = rgb(255, 0, 0)
    gred1 = [255, 0, 0]
    gred2 = [43, 2, 2]

    darkred = rgb(69, 12, 12)
    gdarkred1 = [163, 44, 44]
    gdarkred2 = [33, 3, 1]

    blue = rgb(0, 146, 250)
    gblue1 = [0, 146, 250]
    gblue2 = [26, 72, 105]

    darkblue = rgb(5, 105, 171)
    gdarkblue1 = [5, 105, 171]
    gdarkblue2 = [8, 36, 117]

    yellow = rgb(255, 232, 25)
    gyellow1 = [255, 232, 25]
    gyellow2 = [189, 158, 87]

    orange = rgb(255, 158, 3)
    gorange1 = [255, 158, 3]
    gorange2 = [110, 72, 11]

    purple = rgb(127, 0, 245)
    gpurple1 = [127, 0, 245]
    gpurple2 = [34, 1, 64]

    cyan = rgb(0, 245, 233)
    gcyan1 = [0, 245, 233]
    gcyan2 = [15, 66, 133]

    magenta = rgb(245, 0, 241)
    gmagenta1 = [245, 0, 241]
    gmagenta2 = [97, 17, 78]

    white = rgb(255, 255, 255)
    black = rgb(77, 76, 76)

class files:
    folders = [
        'data'
    ]

    files = [
        'data\\tokens.txt'
    ]
    
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
    
    for file in files:
        if not os.path.exists(file):
            open(file, 'w').close()

class ui:
    def __init__(self):
        self.size = os.get_terminal_size().columns
        self.font = 'rowancap'
    
    def gprint(self, text):
        print(ab5.vgratient(text, co.gmain1, co.gmain2))

    def ask(self, text, bool=False):
        if bool:
            text = ab5.hgratient(f'[{text}] [y/n] >', co.gmain1, co.gmain2).strip()
            if input(f'{text} {S.RESET_ALL}') in ['y', 'Y', 'yes', 'Yes', 'YES', 'Yea', 'yea', 'Yea', 'yea', 'Yea']:
                return True
            else:
                return False
        else:
            text = ab5.hgratient(f'[{text}] >', co.gmain1, co.gmain2).strip()
            return input(f'{text} {S.RESET_ALL}')

    def banner(self):
        banner = f'''
{'    dMP     dMP dMMMMMMMMb dMMMMMP '.center(self.size)}
{'   dMP     amr dMP"dMP"dMPdMP      '.center(self.size)}
{'  dMP     dMP dMP dMP dMPdMMMP     '.center(self.size)}
{' dMP     dMP dMP dMP dMPdMP        '.center(self.size)}
{'dMMMMMP dMP dMP dMP dMPdMMMMMP     '.center(self.size)}
'''
        self.gprint(banner)

    def menu(self, page=0):
        pages = {
            -1: f'''
{'dsc > Discord          how > Raiding tutorial '.center(self.size)}
{'tel > Telegram         frr > Free version gh  '.center(self.size)}
{'lim > Lime site        err > Report a error   '.center(self.size)}
{'dca > My discord acc   sug > Give a suggestion'.center(self.size)}
{'tla > My telegram acc  str > Acces the store  '.center(self.size)}
''',
            0: f'''
{'ex > Extras'.center(self.size)}
{'01 > Joiner F          06 > Message spammer F 11 > Checker F         16 > Onboarding bypass '.center(self.size)}
{'02 > Leaver F          07 > Thread spammer    12 > Avatar changer    17 > Reaction bypass   '.center(self.size)}
{'03 > Is in server F    08 > Reply spammer     13 > Bio changer F     18 > Rule bypass       '.center(self.size)}
{'04 > Anti ban          09 > Poll spammer      14 > Display changer   19 > Button bypass     '.center(self.size)}
{'05 > Nick changer      10 > Chat crasher      15 > Humanizer         20 > Restorecord bypass'.center(self.size)}
'''
        }
        self.gprint(pages[page])

    def prep(self, module, step):
        if step == 1:
            self.title(module)
            self.cls()
            self.banner()
        
        elif step == 2:
            self.cls()
            self.banner()

    def cls(self):
        os.system('cls')

    def title(self, title):
        os.system(f'title Lime FREE - {title}')

    def cleanchoice(self, chosen):
        chosen = re.sub(r'[^a-zA-Z0-9]', '', chosen)
        chosen = re.sub(r'0(?=\d)', '', chosen)
        return chosen
    
    def makemenu(self, options):
        for index, option in enumerate(options, 1):
            indx = ab5.hgratient(f'[{index:02d}]', co.gmain1, co.gmain2).strip()
            opt = ab5.hgratient(f'[{option}]', co.gmain1, co.gmain2).strip()
            print(f'{indx} > {opt}{S.RESET_ALL}')

        print('\n')

    def delayask(self):
        try:
            delay = float(self.ask('Delay (0 for no delay)'))
        except:
            delay = 0
        
        return delay
    
    class _progressbar:
        def __init__(self, prefix='Processing', suffix=''):
            self.size = os.get_terminal_size().columns
            self.width = min(self.size - 50, 40)
            self.total = 0.1
            self.iteration = 0
            self.fill_char = '█'
            self.empty_char = '░'
            self.prefix = prefix
            self.suffix = suffix
            self.start_time = time.time()
            self.last_update_time = 0
            self.delay_between_updates = 0.1
            self.print_progress()

        def update(self, n=1):
            self.iteration += n
            current_time = time.time()
            if current_time - self.last_update_time >= self.delay_between_updates:
                self.print_progress()
                self.last_update_time = current_time

        def print_progress(self):
            percent = 100 * (self.iteration / float(self.total))
            filled_length = int(self.width * self.iteration // self.total)
            empty_length = self.width - filled_length
            elapsed = max(0.001, time.time() - self.start_time)
            items_per_second = self.iteration / elapsed if elapsed > 0 else 0
            eta = (self.total - self.iteration) / items_per_second if items_per_second > 0 else 0
            eta_str = f'{eta:.0f}s'
            bar = ab5.hgratient(self.fill_char * filled_length + self.empty_char * empty_length, co.gmain1, co.gmain2).strip()
            prefixtext = ab5.hgratient(f'[{self.prefix}]', co.gmain1, co.gmain2).strip()
            backtext = ab5.hgratient(f'{percent:.1f}% [{self.iteration}/{self.total}] elapsed {elapsed:.1f}s eta {eta_str} {self.suffix}', co.gmain1, co.gmain2).strip()
            progress_text = f'{prefixtext} > {bar} {backtext}'
            sys.stdout.write(f'\r{progress_text}')
            sys.stdout.flush()

        def __iter__(self, iterable):
            self.total = len(iterable)
            self.start_time = time.time()
            self.iteration = 0
            self.print_progress()
            for item in iterable:
                yield item
                self.update()
            self.iteration = self.total
            self.print_progress()
            sys.stdout.write('\n')

    def progressbar(self, iterable=None, prefix='Processing', suffix=''):
        progress = self._progressbar(prefix=prefix, suffix=suffix)
        if iterable is not None:
            return progress.__iter__(iterable)
        return progress

    class _spinner:
        def __init__(self, prefix='Processing', onfinish='Finished', suffix=''):
            self.size = os.get_terminal_size().columns
            self.prefix = prefix
            self.onfinish = onfinish
            self.suffix = suffix
            self.spinner_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
            self.spinner_index = 0
            self.start_time = time.time()
            self.last_update = 0
            self.delay = 0.1
            self.current = 0
            self.total = None
            self.running = False
            self.spinner_thread = None
        
        def spin(self):
            self.running = True
            while self.running:
                self.print_spinner()
                self.spinner_index = (self.spinner_index + 1) % len(self.spinner_chars)
                time.sleep(self.delay)
        
        def start(self):
            self.start_time = time.time()
            self.spinner_thread = threading.Thread(target=self.spin)
            self.spinner_thread.daemon = True
            self.spinner_thread.start()
        
        def update(self, n=1):
            self.current += n
        
        def print_spinner(self, completed=False):
            elapsed = max(0.001, time.time() - self.start_time)
            
            if completed:
                spinner = '✓'
            else:
                spinner = self.spinner_chars[self.spinner_index]
            
            spinner_colored = ab5.hgratient(spinner, co.gmain1, co.gmain2).strip()
            
            if completed:
                prefix_colored = ab5.hgratient(f'[{self.onfinish}]', co.gmain1, co.gmain2).strip()
            else:
                prefix_colored = ab5.hgratient(f'[{self.prefix}]', co.gmain1, co.gmain2).strip()
            
            if self.total:
                percent = 100 * (self.current / float(self.total))
                stats_colored = ab5.hgratient(f'[{self.current}/{self.total}] {percent:.1f}% elapsed {elapsed:.1f}s {self.suffix}', co.gmain1, co.gmain2).strip()
                progress_text = f'{spinner_colored} {prefix_colored} > {stats_colored}'
            else:
                stats_colored = ab5.hgratient(f'elapsed {elapsed:.1f}s {self.suffix}', co.gmain1, co.gmain2).strip()
                progress_text = f'{spinner_colored} {prefix_colored} > {stats_colored}'
            
            sys.stdout.write('\r' + ' ' * self.size)
            sys.stdout.write(f'\r{progress_text}')
            sys.stdout.flush()
        
        def finish(self):
            self.running = False
            if self.spinner_thread and self.spinner_thread.is_alive():
                self.spinner_thread.join(1.0)
            
            elapsed = max(0.001, time.time() - self.start_time)
            spinner_colored = ab5.hgratient('✓', co.gmain1, co.gmain2).strip()
            prefix_colored = ab5.hgratient(f'[{self.onfinish}]', co.gmain1, co.gmain2).strip()
            
            if self.total:
                stats_colored = ab5.hgratient(f'completed in {elapsed:.2f}s {self.suffix}', co.gmain1, co.gmain2).strip()
            else:
                stats_colored = ab5.hgratient(f'completed in {elapsed:.2f}s {self.suffix}', co.gmain1, co.gmain2).strip()
            
            progress_text = f'{spinner_colored} {prefix_colored} > {stats_colored}'
            
            sys.stdout.write('\r' + ' ' * self.size)
            sys.stdout.write(f'\r{progress_text}\n')
            sys.stdout.flush()
        
        def __iter__(self, iterable):
            self.total = len(iterable)
            self.current = 0
            self.start()
            
            try:
                for item in iterable:
                    yield item
                    self.update()
            finally:
                self.finish()
    
    def spinner(self, iterable=None, prefix='Processing', onfinish='Finished', suffix=''):
        spinner = self._spinner(prefix=prefix, onfinish=onfinish, suffix=suffix)
        if iterable is not None:
            return spinner.__iter__(iterable)
        else:
            spinner.start()
            return spinner

class logger:
    def __init__(self, name):
        self.name = name

    def succeded(self, message, status):
        module = ab5.hgratient(f'[{self.name}]', co.gmain1, co.gmain2).strip()
        status = ab5.hgratient(f'[{status}]', co.gmain1, co.gmain2).strip()
        message = ab5.hgratient(f'[{message}]', co.gmain1, co.gmain2).strip()
        ts = f'{co.black}{dt.now().strftime("%H:%M:%S")} '

        print(f'{ts}{module} > {message} {status}{S.RESET_ALL}')

    def checkervalid(self, message, status):
        module = f'{co.green}[{self.name}]{co.white}'
        status = f'{co.green}[{status}]{co.white}'
        message = f'{co.green}[{message}]{co.white}'
        ts = f'{co.black}{dt.now().strftime("%H:%M:%S")} '

        print(f'{ts}{module} > {message} {status}{S.RESET_ALL}')

    def captcha(self, message):
        module = ab5.hgratient(f'[{self.name}]', co.gmain1, co.gmain2).strip()
        message = ab5.hgratient(f'[{message} Could have been prevented if you ware using PAID]', co.gcyan1, co.gcyan2).strip()

        ts = f'{co.black}{dt.now().strftime("%H:%M:%S")} '

        print(f'{ts}{module} > {message}{S.RESET_ALL}')

    def ratelimit(self, message):
        module = ab5.hgratient(f'[{self.name}]', co.gmain1, co.gmain2).strip()
        message = ab5.hgratient(f'[{message}]', co.gyellow1, co.gyellow2).strip()

        ts = f'{co.black}{dt.now().strftime("%H:%M:%S")} '

        print(f'{ts}{module} > {message}{S.RESET_ALL}')

    def cloudflare(self, message):
        module = ab5.hgratient(f'[{self.name}]', co.gmain1, co.gmain2).strip()
        message = ab5.hgratient(f'[{message}]', co.gyellow1, co.gyellow2).strip()

        ts = f'{co.black}{dt.now().strftime("%H:%M:%S")} '

        print(f'{ts}{module} > {message}{S.RESET_ALL}')

    def locked(self, message, ts=True):
        module = ab5.hgratient(f'[{self.name}]', co.gmain1, co.gmain2).strip()
        message = ab5.hgratient(f'[{message}]', co.gred1, co.gred2).strip()

        if not ts:
            ts = ''
        else:
            ts = f'{co.black}{dt.now().strftime("%H:%M:%S")} '

        print(f'{ts}{module} > {message}{S.RESET_ALL}')

    def info(self, message, ts=False, inp=False):
        module = ab5.hgratient(f'[{self.name}]', co.gmain1, co.gmain2).strip()
        message = ab5.hgratient(f'[{message}]', co.gmain1, co.gmain2).strip()

        if ts: ts = f'{co.black}{dt.now().strftime("%H:%M:%S")} '
        else: ts = ''

        if inp:
            input(f'{ts}{module} > {message}{S.RESET_ALL}')
        else:
            print(f'{ts}{module} > {message}{S.RESET_ALL}')

    def warn(self, message):
        module = ab5.hgratient(f'[{self.name}]', co.gmain1, co.gmain2).strip()
        message = ab5.hgratient(f'[{message}]', co.gyellow1, co.gyellow2).strip()

        ts = f'{co.black}{dt.now().strftime("%H:%M:%S")} '

        print(f'{ts}{module} > {message}{S.RESET_ALL}')

    def error(self, message, ts=True):
        module = ab5.hgratient(f'[{self.name}]', co.gmain1, co.gmain2).strip()
        message = ab5.hgratient(f'[{message}]', co.gred1, co.gred2).strip()

        if not ts:
            ts = ''
        else:
            ts = f'{co.black}{dt.now().strftime("%H:%M:%S")} '

        print(f'{ts}{module} > {message}{S.RESET_ALL}')

    def premium_only(self):
        module = ab5.hgratient(f'[Main]', co.gmain1, co.gmain2).strip()
        message = ab5.hgratient('[This is a premium only feature]', co.gmain1, co.gmain2).strip()

        print(f'{module} > {message}{S.RESET_ALL}')
    
    def errordatabase(self, text):
        # No more free db 😊😊😊
        db = {
            '401: Unauthorized': 'Invalid token/Lock invalided token',
            'captcha_key': 'Hcaptcha',
            'Unauthorized': 'Invalid token/Lock invalided token',
            'retry_after': 'Limited',
            'You need to verify': 'Locked token',
            'You are being blocked from accessing our API': 'API BAN',
            'Unknown Invite': 'Unknown Invite',
        }

        for key in db.keys():
            if key in text:
                return db[key]

        return text

log = logger('Error chandler')

def log_errors(exctype, value, tb):
    if 'auth' in str(exctype) or 'auth' in str(value) or 'auth' in str(tb):
        return
    try:
        error = ''.join(traceback.format_exception(exctype, value, tb))
        log.error(error, False)
        if 'KeyboardInterrupt' in exctype or 'KeyboardInterrupt' in value or 'KeyboardInterrupt' in tb:
            return
        
        #try:
        #    requests.get(
        #        'http://us3.bot-hosting.net:20933/error-free', 
        #        json={
        #            f'content': f'```{error}```'
        #        }
        #    )
        #except:
        #    pass
        
    except:
        print(f'{exctype} - {value} - {tb}')

sys.excepthook = log_errors

class discordhelper:
    def extract_invite(invite):
        match: re.Match = re.search(r'(?:(?:http:\/\/|https:\/\/)?discord\.gg\/|discordapp\.com\/invite\/|discord\.com\/invite\/)?([a-zA-Z0-9-]+)', invite)
        if match: 
            return match.group(1)
        
        return invite

    def delay(delay):
        if delay > 0:
            time.sleep(float(delay))
            
    def getsnowflake():
        return ((int(time.time() * 1000) - 1420070400000) << 22)

    def getemojis(length):
        emoji_ranges = [
            (0x1F600, 0x1F64F),
            (0x1F300, 0x1F5FF),
            (0x1F680, 0x1F6FF),
            (0x1F700, 0x1F77F),
            (0x1F900, 0x1F9FF),
        ]
        emojis = [chr(code) for start, end in emoji_ranges for code in range(start, end + 1)]
        return ''.join(random.choices(emojis, k=length))
    
    def getstr(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choices(characters, k=length))
    
    def getlist(length, lst):
        random.shuffle(lst)
        return lst[:min(length, len(lst))]

class thread:
    def __init__(self, func, tokens=[], args=[], delay=0):
        self.log = logger('Threads')
        self.func = func
        self.tokens = tokens
        self.args = list(args)
        self.delay = delay
        self.futures = []
        self.work()

    def execute(self, token, exe: ThreadPoolExecutor):
        current_args = [token] + self.args
        
        try:
            future = exe.submit(self.func, *current_args)
            self.futures.append(future)
        except Exception as e:
            self.log.error(e)

    def work(self):
        if not self.tokens:
            self.log.warn('Please input ur tokens into data/tokens.txt')
            return

        with ThreadPoolExecutor(max_workers=15) as exe:
            for token in self.tokens:
                self.execute(token, exe)
                discordhelper.delay(self.delay)

            for future in self.futures:
                try:
                    future.result()

                except Exception as e:
                    self.log.error(e)

__headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': f'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Priority': 'u=1, i',
    'Referer': 'https://discord.com/channels/@me',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    'X-Debug-Options': 'bugReporterEnabled',
    'X-Discord-Locale': 'en-US',
    'X-Discord-Timezone': 'Europe/Warsaw',
    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiaGFzX2NsaWVudF9tb2RzIjpmYWxzZSwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMzQuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMzQuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vZGlzY29yZC5jb20vP2Rpc2NvcmR0b2tlbj1NVE16T1RBeU9EQTROemMwT0RRek1Ua3lOdy5HVTd2QVMuTEpWdFpnU2tXb2xkSWpsbU1OMTJYUTF0b0tld191aG8xRzhKVXciLCJyZWZlcnJpbmdfZG9tYWluIjoiZGlzY29yZC5jb20iLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6Mzc3MjA3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
} 
__sess = tls_client.Session(client_identifier='chrome_120')
__cookier = __sess.get('https://discord.com', headers=__headers).cookies

class client:
    def __init__(self, token=None):
        self.headers = __headers
        if token is not None:
            self.headers['Authorization'] = token
        self.sess = tls_client.Session(client_identifier='chrome_120')
        self.sess.cookies.update(__cookier)

# Btw before flaming me this code is made to be worse bypassing than the paid for obvius reasons 
class lime:
    class joiner:
        def __init__(self):
            self.name = 'Joiner'
            self.log = logger(self.name)
            self.delay = 0
            self.invite = None

            self.succeded, self.locked, self.captcha, self.failed = 0, 0, 0, 0

        def join(self, token):
            cl = client(token)

            payload = {
                'session_id': uuid.uuid4().hex
            }

            r = cl.sess.post(
                f'https://discord.com/api/v9/invites/{self.invite}',
                headers=cl.headers,
                json=payload
            )


            if r.status_code == 200:
                self.log.succeded(f'{token[:20]}... Joined (discord.gg/{self.invite})', 200)
                self.succeded += 1
            
            elif 'retry_after' in r.text:
                limit = r.json().get('retry_after', 1.5)
                self.log.ratelimit(f'{token[:20]}... Ratelimited ({limit}s)')
                time.sleep(float(limit))
                self.join(token, cl)

            elif 'Cloudflare' in r.text:
                self.log.cloudflare(f'{token[:20]}... Cloudflare (10s)')
                time.sleep(10)
                self.join(token, cl)

            elif 'captcha_key' in r.text:
                self.log.captcha(f'{token[:20]}... Captcha')
            
            elif 'You need to verify' in r.text:
                self.log.locked(f'{token[:20]}... Locked')
                self.locked += 1

            else:
                error = self.log.errordatabase(r.text)
                self.log.error(error)
                self.failed += 1
        
        def main(self):
            ui().prep(self.name, 1)
            self.log.info('Better bypasses and more features in PAID')
            self.invite = ui().ask('Invite')
            self.delay = ui().delayask()

            ui().prep(self.name, 2)
            self.log.info('Better bypasses and more features in PAID')

            thread(
                func=self.join,
                tokens=open('data\\tokens.txt', 'r').read().splitlines(),
                args=[],
                delay=self.delay
            )
            
            self.log.info(f'Succeded > {self.succeded} Locked > {self.locked} Captcha > {self.captcha} Failed > {self.failed}')

    class leaver:
        def __init__(self):
            self.name = 'Leaver'
            self.log = logger(self.name)
            self.delay = 0
            self.serverid = None

            self.succeded, self.locked, self.failed = 0, 0, 0

        def leave(self, token):
            cl = client(token)

            payload = {
                'lurking': False
            }

            r = cl.sess.delete(
                f'https://discord.com/api/v9/users/@me/guilds/{self.serverid}',
                headers=cl.headers,
                json=payload
            )

            if r.status_code == 204:
                self.log.succeded(f'{token[:20]}... Left ({self.serverid})', 204)
                self.succeded += 1
            
            elif 'retry_after' in r.text:
                limit = r.json().get('retry_after', 1.5)
                self.log.ratelimit(f'{token[:20]}... Ratelimited ({limit}s)')
                time.sleep(float(limit))
                self.leave(token)

            elif 'Cloudflare' in r.text:
                self.log.cloudflare(f'{token[:20]}... Cloudflare (10s)')
                time.sleep(10)
                self.leave(token)
            
            elif 'You need to verify' in r.text:
                self.log.locked(f'{token[:20]}... Locked')
                self.locked += 1

            else:
                error = self.log.errordatabase(r.text)
                self.log.error(error)
                self.failed += 1
        
        def main(self):
            ui().prep(self.name, 1)
            self.serverid = ui().ask('Server ID')
            self.delay = ui().delayask()
            ui().prep(self.name, 2)

            thread(
                func=self.leave,
                tokens=open('data\\tokens.txt', 'r').read().splitlines(),
                args=[],
                delay=self.delay
            )
            
            self.log.info(f'Succeded > {self.succeded} Locked > {self.locked} Failed > {self.failed}')

    class isinserver:
        def __init__(self):
            self.name = 'Is in server'
            self.log = logger(self.name)
            self.delay = 0
            self.serverid = None

            self.succeded, self.locked, self.failed = 0, 0, 0

        def check(self, token):
            cl = client(token)

            r = cl.sess.get(
                f'https://discord.com/api/v9/guilds/{self.serverid}',
                headers=cl.headers,
            )

            if r.status_code == 200:
                self.log.succeded(f'{token[:20]}... Is in the server ({self.serverid})', 200)
                self.succeded += 1
            
            elif 'retry_after' in r.text:
                limit = r.json().get('retry_after', 1.5)
                self.log.ratelimit(f'{token[:20]}... Ratelimited ({limit}s)')
                time.sleep(float(limit))
                self.check(token)

            elif 'Cloudflare' in r.text:
                self.log.cloudflare(f'{token[:20]}... Cloudflare (10s)')
                time.sleep(10)
                self.check(token)
            
            elif 'You need to verify' in r.text:
                self.log.locked(f'{token[:20]}... Locked')
                self.locked += 1

            else:
                error = self.log.errordatabase(r.text)
                self.log.error(error)
                self.failed += 1
        
        def main(self):
            ui().prep(self.name, 1)
            self.serverid = ui().ask('Server ID')
            ui().prep(self.name, 2)

            thread(
                func=self.check,
                tokens=open('data\\tokens.txt', 'r').read().splitlines(),
                args=[],
                delay=self.delay
            )
            
            self.log.info(f'Succeded > {self.succeded} Locked > {self.locked} Failed > {self.failed}')

    class messagespammer:
        def __init__(self):
            self.name = 'Message spammer'
            self.log = logger(self.name)
            self.delay = 0
            self.basemsg = None
            self.serverid = None
            self.channelid = None
            self.nostop = False

        def replacer(self, match: re.Match):
            tag, number = match.group(1), match.group(2)
            if tag == 'emoji':
                return discordhelper.getemojis(int(number))
            elif tag == 'str':
                return discordhelper.getstr(int(number))
            return ''

        def replacetags(self, text):
            return re.sub(r'\[(ping|str|emoji)=(\d+)\]', self.replacer, text)   

        def send(self, token):
            cl = client(token)
            
            while True:
                discordhelper.delay(self.delay)
                message = self.replacetags(self.basemsg)
                if isinstance(message, list):
                    message = ' '.join(message)

                payload = {
                    'mobile_network_type': 'unknown',
                    'content': message,
                    'nonce': discordhelper.getsnowflake(),
                    'tts': False,
                    'flags': 0
                }

                r = cl.sess.post(
                    f'https://discord.com/api/v9/channels/{self.channelid}/messages',
                    headers=cl.headers,
                    json=payload
                )

                if r.status_code == 200:
                    self.log.succeded(f'{token[:20]}... Sent message ({self.channelid})', 200)
                    continue
                
                elif 'retry_after' in r.text:
                    limit = r.json().get('retry_after', 1.5)
                    self.log.ratelimit(f'{token[:20]}... Ratelimited ({limit}s)')
                    time.sleep(float(limit))
                    continue

                elif 'Cloudflare' in r.text:
                    self.log.cloudflare(f'{token[:20]}... Cloudflare (10s)')
                    time.sleep(10)
                    continue
                
                elif 'You need to verify' in r.text:
                    self.log.locked(f'{token[:20]}... Locked')
                    break

                else:
                    error = self.log.errordatabase(r.text)
                    self.log.error(error)
                    if self.nostop:
                        continue
                    else:
                        break
        
        def main(self):
            ui().prep(self.name, 1)
            self.log.info('Tags that you can use >> [ping=10] [str=10]] [emoji=10]')
            self.log.info('Example >> Spam 123 [ping=10] [str=10] [emoji=10]')
            self.log.info('Example outputted >> spam123 (pings 10 people) (sends a string with 10 in length) (sends 10 random emojis)')
            self.log.info('The number can ofc be custom does not need to be 10')
            self.basemsg = ui().ask('Message')
            self.serverid = ui().ask('Server ID')
            self.channelid = ui().ask('Channel ID')
            self.tts = ui().ask('TTS (reads the message out with a voice, normaly accounts do NOT have perms for this)', True)
            self.nostop = ui().ask('No break on error (wont stop on a unchandled error, like automod flag etc)', True)
            self.delay = ui().delayask()

            if '[ping=' in self.basemsg:
                self.log.info('Pings are paid only')

            ui().prep(self.name, 2)

            thread(
                func=self.send,
                tokens=open('data\\tokens.txt', 'r').read().splitlines(),
                args=[],
                delay=self.delay
            )

    class checker:
        def __init__(self):
            self.name = 'Checker'
            self.log = logger(self.name)
            self.delay = 0
            self.valids = []
            self.failed = []
            self.locked = []


        def check(self, token):
            cl = client(token)
            discordhelper.delay(self.delay)

            r = cl.sess.get(
                'https://discord.com/api/v9/users/@me/library',
                headers=cl.headers
            )

            if r.status_code == 200:
                self.valids.append(token)

                self.log.checkervalid(f'{token[:20]}... Valid INFO IS PAID ONLY', 200)


            elif 'retry_after' in r.text:
                limit = r.json().get('retry_after', 1.5)
                self.log.ratelimit(f'{token[:20]}... Ratelimited ({limit}s)')
                time.sleep(float(limit))
                self.check(token)

            elif 'Try again later' in r.text:
                self.log.ratelimit(f'{token[:20]}... Specific ratelimited (15s)')
                time.sleep(15)
                self.check(token)

            elif 'Cloudflare' in r.text:
                self.log.cloudflare(f'{token[:20]}... Cloudflare (10s)')
                time.sleep(10)
                self.check(token)
            
            elif 'You need to verify' in r.text:
                self.log.locked(f'{token[:20]}... Locked')
                self.locked.append(token)

            else:
                error = self.log.errordatabase(r.text)
                self.log.error(error)
                self.failed.append(token)
        
        def main(self):
            ui().prep(self.name, 1)
            self.serverid = ui().ask('Server ID')
            self.channelid = ui().ask('Channel ID')
            self.nostop = ui().ask('No break on error (wont stop on a unchandled error, like automod flag etc)', True)
            self.delay = ui().delayask()

            ui().prep(self.name, 2)

            if self.valids:
                save = ui().ask('Replace tokens.txt with only valid tokens', True)
                if save:
                    with open('data\\tokens.txt', 'w') as f:
                        f.write('\n'.join(self.valids))
            
            else:
                self.log.info('Blud has no valid tokens 😭😭😭')

            self.log.info('Token sorting is paid only')


            thread(
                func=self.check,
                tokens=open('data\\tokens.txt', 'r').read().splitlines(),
                args=[],
                delay=self.delay
            )

            self.log.info(f'EV > PAID ONLY No EV > PAID ONLY PV > PAID ONLY No PV > PAID ONLY Email > PAID ONLY No email > PAID ONLY')
            self.log.info(f'Valid > {len(self.valids)} Locked > {len(self.locked)} Nitro > PAID ONLY Nonitro > PAID ONLY Failed > {len(self.failed)}')

    class biochanger:
        def __init__(self):
            self.name = 'Bio changer'
            self.log = logger(self.name)
            self.delay = 0
            self.bio = None

            self.succeded, self.locked, self.failed = 0, 0, 0

        def change(self, token):
            cl = client(token)
            payload = {
                'bio': self.bio
            }

            r = cl.sess.patch(
                'https://discord.com/api/v9/users/@me',
                headers=cl.headers,
                json=payload
            )

            if r.status_code == 200:
                self.log.succeded(f'{token[:20]}... Changed bio', 200)
                succeded += 1

            elif 'retry_after' in r.text:
                limit = r.json().get('retry_after', 1.5)
                self.log.ratelimit(f'{token[:20]}... Ratelimited ({limit}s)')
                time.sleep(float(limit))
                self.change(token)

            elif 'Try again later' in r.text:
                self.log.ratelimit(f'{token[:20]}... Specific ratelimited (15s)')
                time.sleep(15)
                self.change(token)

            elif 'Cloudflare' in r.text:
                self.log.cloudflare(f'{token[:20]}... Cloudflare (10s)')
                time.sleep(10)
                self.change(token)
            
            elif 'You need to verify' in r.text:
                self.log.locked(f'{token[:20]}... Locked')
                locked += 1

            else:
                error = self.log.errordatabase(r.text)
                self.log.error(error)
                self.failed += 1
        
        def main(self):
            ui().prep(self.name, 1)
            self.bio = ui().ask('Bio')
            self.delay = ui().delayask()

            ui().prep(self.name, 2)

            thread(
                func=self.change,
                tokens=open('data\\tokens.txt', 'r').read().splitlines(),
                args=[],
                delay=self.delay
            )

            self.log.info(f'Succeded > {self.succeded} Locked > {self.locked} Failed > {self.failed}')

__log = logger('Main')
options = {
    'dsc': lambda: os.system(f'start {fulldiscord}'),
    'tel': lambda: os.system(f'start {fulltelegram}'),
    'lim': lambda: os.system(f'start {fullsite}'),
    'dca': lambda: os.system(f'start {fulldiscordacc}'),
    'tla': lambda: os.system(f'start {fulltelegramacc}'),
    'how': lambda: print('DISCORD.GG/SPAMMING\nGETLIME.XYZ\n\n1. Automod\nTo check if a server has auto mod use server info\nIf has be careful as it will flag after 6 accounts join from the same ip\n2. Proxy\nGet good proxies as bad ones will either not work will flag or will just have bad performance\nGet RESIDENTIAL ONLY\n\n3. Captchas\nDepend on many things like\n- If automod flagged\n- If you have proxies\n- If you have a lot of tokens\n- Token overusage\n- Usage of bad outdated flagged tools\n- And more more more\n\n4. Solving\nMost solvers require proxies\nWARNING NOT ALL PROXIES WORK FOR FOR SOLVERS AS THEY MIGHT BE FLAGGED ON HCAPTCHA\n\n5. Joining\nPlease use a delay even a small one \nPLEASE READ THE AUTOMOD (nr 1)\n\nGETLIME.XYZ\nDISCORD.GG/SPAMMING'),
    'frr': lambda: os.system(f'start {fullgithub}'), 
    #'err': lambda: os.system(f'start {fullgithub}'), #
    #'sug': lambda: os.system(f'start {fullgithub}'), #
    'str': lambda: os.system(f'start {fullstore}'),

    '1': lime.joiner().main,
    '2': lime.leaver().main,
    '3': lime.isinserver().main,
    '4': __log.premium_only,
    '5': __log.premium_only,
    '6': lime.messagespammer().main,
    '7': __log.premium_only,
    '8': __log.premium_only,
    '9': __log.premium_only,
    '10': __log.premium_only,
    '11': lime.checker().main,
    '12': __log.premium_only,
    '13': lime.biochanger().main,
    '14': __log.premium_only,
    '15': __log.premium_only,
    '16': __log.premium_only,
    '17': __log.premium_only,
    '18': __log.premium_only,
    '19': __log.premium_only,
    '20': __log.premium_only,
}

while True:
    ui().cls()
    ui().title(f'{discord} - {site}')
    ui().banner()
    ui().menu(0)
    print('\n')

    chosen = ui().ask('Choice')
    chosen = ui().cleanchoice(chosen)

    while chosen == 'ex':
        ui().cls()
        ui().title(f'{discord} - {site}')
        ui().banner()
        ui().menu(-1)
        chosen = ui().ask('Choice')
        chosen = ui().cleanchoice(chosen)

    if chosen in options:
        options[chosen]()
        if chosen not in ['>', '<']:
            __log.info('Finished! Enter to continue', False, True)
        
    else:
        __log.info('That option does not exist yet', False, True)
