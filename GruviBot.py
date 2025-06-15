import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import yt_dlp
from collections import deque
import asyncio

#reading token

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

SONG_QUEUES = {}

#wizard shit which i do not understand and which i obviously copied

async def search_ytdlp_async(query, ydl_options):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, lambda: _extract(query, ydl_options))

def _extract(query, ydl_options):
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        return ydl.extract_info(query, download=False)
    
#discord bot intents (intent's an object which basically stores the configurations)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STOP_FLAG = os.path.join(SCRIPT_DIR, "stop.flag")

#"events" are when shit happens in the server, except for the "on_ready()" which is a bit special

@bot.event 
async def on_ready(): #things that happen when bot is ready
    print(f'{bot.user.name}\'s ready')
    try:
        synced = await bot.tree.sync()
    except Exception as e:
        print(f"Slash command sync failed: {e}")
    bot.loop.create_task(check_for_stop_flag())

async def check_for_stop_flag():
    while True:
        if os.path.exists(STOP_FLAG):
            print("Stop flag detected. Shutting down...")
            os.system('del stop.flag')
            await bot.close()
            break
        await asyncio.sleep(5)
    
@bot.tree.command(name="play", description="makes the bot join your channel and play smth")
async def play(interaction: discord.Interaction, song_query: str):
    await interaction.response.defer()

    if interaction.user.voice is None or interaction.user.voice.channel is None:
        await interaction.followup.send("You're not in a voice channel", ephemeral=True)
        return

    voice_channel = interaction.user.voice.channel
    voice_client = interaction.guild.voice_client

    if voice_client is None:
        voice_client = await voice_channel.connect()
    elif voice_client.channel != voice_channel:
        await voice_client.move_to(voice_channel)

    ydl_options = {
        "format": "bestaudio[abr<=96]/bestaudio",
        "noplaylist": True,
        "quiet": True,
        "youtube_include_dash_manifest": False,
        "youtube_include_hls_manifest": False,
    }

    ffmpeg_options = {
        "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
        "options": "-vn",
        "executable": "bin\\ffmpeg\\ffmpeg.exe",  # Make sure this path is correct
    }

    def get_info(query: str):
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            return ydl.extract_info(query, download=False)

    # Determine if it's a YouTube link or search query
    if any(song_query.startswith(prefix) for prefix in [
        "https://www.youtube.com/watch?v=",
        "youtube.com/watch?v=",
        "https://youtu.be/",
        "youtu.be/"
    ]):
        info = get_info(song_query)
    else:
        info = get_info(f"ytsearch1:{song_query}")
        info = info["entries"][0] if "entries" in info else info

    title = info.get("title", "Untitled")
    stream_url = info["url"]  # This is the direct audio stream for FFmpeg

    # Play the audio
    source = discord.FFmpegOpusAudio(stream_url, **ffmpeg_options)

    guild_id = str(interaction.guild_id)
    if SONG_QUEUES.get(guild_id) is None:
        SONG_QUEUES[guild_id] = deque()

    SONG_QUEUES[guild_id].append((stream_url, title))

    if voice_client.is_playing():
        await interaction.followup.send(f"Added to queue: **{title}**")
    else:
        await interaction.followup.send(f"Now playing: **{title}**")
        voice_client.play(source, after=lambda e: bot.loop.create_task(play_next_song(voice_client, guild_id, interaction.channel)))

@bot.tree.command(name="stop", description="Stops the music and makes the bot leave")
async def stop(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client

    # check if bot in voice channel
    if not voice_client or not voice_client.is_connected():
        return await interaction.response.send_message("Bot's not in any voice channel", ephemeral = True)
        
    # Clear the guild's queue
    guild_id_str = str(interaction.guild_id)
    if guild_id_str in SONG_QUEUES:
        SONG_QUEUES[guild_id_str].clear()

    # If something is playing or paused, stop it
    if voice_client.is_playing() or voice_client.is_paused():
        voice_client.stop()
        
    await voice_client.disconnect()

    await interaction.response.send_message("Bot successfully left", ephemeral = True)
    
@bot.tree.command(name="skip", description="Skips the current playing song")
async def skip(interaction: discord.Interaction):
    if interaction.guild.voice_client and (interaction.guild.voice_client.is_playing() or interaction.guild.voice_client.is_paused()):
        interaction.guild.voice_client.stop()
        await interaction.response.send_message("Skipped current song")
    else:
        await interaction.response.send_message("Not playing anything to skip", ephemeral = True)

async def play_next_song(voice_client, guild_id, channel):
    if SONG_QUEUES[guild_id]:
        audio_url, title = SONG_QUEUES[guild_id].popleft()

        ffmpeg_options = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn -c:a libopus -b:a 96k",
            "executable": "bin\\ffmpeg\\ffmpeg.exe"
        }

        source = discord.FFmpegOpusAudio(audio_url, **ffmpeg_options)

        def after_play(error):
            if error:
                print(f"Error playing {title}: {error}")
            asyncio.run_coroutine_threadsafe(play_next_song(voice_client, guild_id, channel), bot.loop)

        voice_client.play(source, after=after_play)
    else:
        await voice_client.disconnect()
        SONG_QUEUES[guild_id] = deque()
        
bot.run(TOKEN)