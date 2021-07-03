import com_api as api
import com_cli as cli

while True:
    act1 = cli.title()
    if act1 == 1: # SFW
        api.sfwPlay(cli.sfwSelect())

    elif act1 == 2: # NSFW
        api.nsfwPlay(cli.nsfwSelect())