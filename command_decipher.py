from irc import *
from irc_commands import *

def check(ircmsg):
    if ircmsg.find("PRIVMSG") != -1:
        name = ircmsg.split('!', 1)[0][1:]
        message = ircmsg.split('PRIVMSG', 1)[1].split(':', 1)[1]

        if len(name) < 17:
            if message.find(('hi ' + botnick)) != -1:
                sendmsg(Commands.hello(name))
            elif message.find(('.vend')) != -1:
                sendmsg(Commands.vend(message))
        else:
            if ircmsg.find("PING :") != -1:
                ping()