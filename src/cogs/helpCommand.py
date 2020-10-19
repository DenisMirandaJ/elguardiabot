from discord.ext import commands


class GuardiaHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        command.help = 'tupixua'
        self.command_attrs['help'] = "mipixula"
        return 'jaja'


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._original_help_command = bot.help_command
        bot.help_command = GuardiaHelp()
        bot.help_command.cog = self
        return

    def cog_unload(self):
        self.bot.help_command = self._original_help_command
        return
