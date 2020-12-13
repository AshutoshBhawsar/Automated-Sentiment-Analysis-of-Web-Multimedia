
from MAIN import *

media_url = get_url()

print("Fetching...")
p.download_mp3(media_url)
e.extract_sub()
