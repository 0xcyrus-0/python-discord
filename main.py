from discord_webhook import DiscordWebhook
import sys
import time
import random
from colorama import Fore,init
init()

# ###
# by : @números#1429 
# ###

print ("Installing Packages 🔀")
def progressBar(count_value, total, suffix=''):
    bar_length = 100
    filled_up_Length = int(round(bar_length* count_value / float(total)))
    percentage = round(100.0 * count_value/float(total),1)
    bar = '=' * filled_up_Length + '-' * (bar_length - filled_up_Length)
    sys.stdout.write('[%s] %s%s ...%s\r' %(bar, percentage, '%', suffix))
    sys.stdout.flush()
for i in range(11):
    time.sleep(random.random())
    progressBar(i,10)

webhook_id = "https://discord.com/api/webhooks/1090232729716658188/xci9_4IqN9ycbNqb-Lll6L7PRA15rZ3QYvjUReYBT_p0I26Nz1K4y1891wm3ySHQ7PpD"

webhook = DiscordWebhook(url=webhook_id,rate_limit_retry=True,content='python file has been started\nmade by : números#1429')
response = webhook.execute()
print(f"""{Fore.BLUE}                                                                                                                          
$$$$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$\ 
$$  __$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  _____|
$$ |  $$ |$$ / $$ / $$ |$$$$$$$$ |$$ |  \__|$$ /  $$ |\$$$$$$\  
$$ |  $$ |$$ | $$ | $$ |$$   ____|$$ |      $$ |  $$ | \____$$\ 
$$ |  $$ |$$ | $$ | $$ |\$$$$$$$\ $$ |      \$$$$$$  |$$$$$$$  |
\__|  \__|\__| \__| \__| \_______|\__|       \______/ \_______/                                                                                                              
""")