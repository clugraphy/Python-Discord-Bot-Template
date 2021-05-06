import environ

env = environ.Env(SECRET_KEY = str,)


# Can be multiple prefixes, like this: ("!", "?")
BOT_PREFIX = ("$htf " , "htf-")
TOKEN = env('SECRET_TOKEN')
APPLICATION_ID = "830748037290786867"
OWNERS = [104005181103964160, 437404402781782028]
BLACKLIST = []

# Bot colors
main_color = 0xD75BF4
error = 0xE02B2B
success = 0x42F56C
warning = 0xF59E42
info = 0x4299F5