This is my funny little badly coded discord bot. You can either download the source code (EtereBot.py in the EtereBot folder) or the whole EtereBot directory, which is an almost fully functional bot.
In case you decide to download the entire directory, to set up the bot you need to
  1. add a file called ".env" in which you will write 'DISCORD_TOKEN=<token>' where you'll have to replace "<token>" with your discord bot token;
  2. head via terminal to the root directory of the bot (EtereBot) and run the following commands:
       python -m venv dc_env
       source dc_env/Scripts/activate
       pip install -r requirements.txt
     this should download a virtual environment that the bot will use to run;
  3. a couple other prerequisites are having python installed (duh); being on a windows machine (although the code needs very few changes to run in unix-like systems); and if you're planning on actually using the bot, setting it up on the discord developer portal
