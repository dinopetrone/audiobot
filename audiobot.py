from fabric.api import local
from irctk import Bot

bot = Bot()

context = 'pandora'

@bot.command('next')
@bot.command('skip')
def skip():
	local('osascript {}/skip.applescript'.format(context))
	
@bot.command('play')	
def play():
	local('osascript {}/play.applescript'.format(context))
	
@bot.command('pause')
def pause():
	local('osascript {}/pause.applescript'.format(context))
	
@bot.command('vu')
@bot.command('volume_up')
@bot.command('volumeup')
def volume_up():
	local('osascript {}/volumeUp.applescript'.format(context))
	
@bot.command('vd')
@bot.command('volume_down')
@bot.command('volumedown')
def volume_down():
	local('osascript {}/volumeDown.applescript'.format(context))

#@bot.event('PRIVMSG')
#def on_priv_mesg(context):
#	if context.line['user'].lower() == 'dave':
#		bot.reply('Shut up Dave no one cares',context.line)


def main():
	bot.config.from_pyfile('audiobot.cfg')
	bot.run()



if __name__ == '__main__':
	main()