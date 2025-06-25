import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import yt_dlp
import random
import asyncio

#discord bot intents (intent's an object which basically stores the configurations)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def randSentence():
    words = ["Rineà","Rineàr","Aèr","avgì","Omnì","omnì","vamnìs vamnìsean","vamnìs","Khoavgìeli","Arinòr","arinèr","enalì","mosrièr","aftòr","xavì","xavà","vkès","vìfe","xà"]
    sentence = words[random.randint(0, (len(words) - 1))].capitalize()
    i = 0
    while i < ((len(words) - random.randint(-5, 5))*random.randint(1,3)):
        sentence = sentence + " " + words[random.randint(0, (len(words) - 1))]
        i += 1
    sentence += "."
    return sentence
def randAnswer():
    answers = ["Ciò che cerchi ti sta cercando",
    "Il silenzio contiene più verità di mille parole",
    "Non sapere è il primo passo verso la saggezza",
    "Ogni fine è un inizio travestito",
    "Il dubbio è segno di coscienza sveglia",
    "Non tutte le domande meritano risposta",
    "Il tempo non risponde, insegna",
    "Accetta il non sapere come parte del sapere",
    "La risposta è nel modo in cui ascolti",
    "Anche il vuoto ha qualcosa da dire",
    "La via più breve spesso è una curva",
    "Non resistere al cambiamento: studialo",
    "Ogni scelta è un’affermazione di sé",
    "La verità cambia con lo sguardo",
    "Chi attende con pazienza ottiene più di chi corre",
    "L’ostacolo è parte del cammino",
    "Ogni ombra ha bisogno di luce per esistere",
    "Domanda meglio, e otterrai risposte migliori",
    "L’imperfezione è l’impronta dell’autenticità",
    "Forse la risposta è non averne una",
    "Ciò che temi rivela ciò che ti guida",
    "La mente cerca ragioni, il cuore trova significati",
    "Non sempre capire è necessario",
    "La quiete è una forma di risposta",
    "Lascia che le cose si mostrino da sole",
    "Più cerchi il senso, più si allontana",
    "Ogni momento è una domanda mascherata",
    "Il pensiero non è sempre alleato della verità",
    "Cammina senza fretta: il tempo ti osserva",
    "Non è la risposta a mancare, ma la domanda giusta",
    "Ogni attesa contiene un insegnamento",
    "Ciò che sembra confuso ora, domani sarà chiaro",
    "La profondità non sempre fa rumore",
    "Spesso il senso si nasconde nell’apparente assurdità",
    "Comprendere è un atto di fiducia, non di logica",
    "L’universo ti risponde, ma non con le parole",
    "Non puoi afferrare ciò che va vissuto",
    "A volte il vero sì è un no silenzioso",
    "Chiediti chi sta facendo la domanda",
    "Abbandona il bisogno di controllo: lì iniziano le risposte",
    "Sii fedele a te stesso",
    "Qualsiasi cosa tu faccia, mantieni le apparenze",
    "Cammina con leggerezza",
    "Usa la tua immaginazione",
    "Attento alle liane che si aggrappano",
    "Se sei nei guai, fai bolle",
    "Lascia spazio alle sorprese",
    "Una volta che l’hai trovato, non lasciarlo più",
    "Ogni tua azione può avere serie ripercussioni sul futuro",
    "Prevedi di fare la differenza",
    "Rimuovi i tuoi ostacoli",
    "Potrebbe essere difficile, ma ne trarrai valore",
    "Non ignorare l’ovvio",
    "Sii paziente",
    "Rischia",
    "Fallo presto",
    "La dolce insistenza verrà ripagata",
    "La tua decisione sarà ricompensata",
    "C’è un legame importante con un’altra situazione",
    "Fidati del tuo pensiero originale",
    
    "La logica è la tua migliore guida",
    "Valuta i fatti prima di decidere",
    "Ogni scelta richiede un’analisi attenta",
    "I dati parlano più delle emozioni",
    "Non affrettare la conclusione senza prove",
    "Considera tutte le variabili in gioco",
    "Il dubbio è il motore della ricerca della verità",
    "Le ipotesi vanno testate, non accettate a priori",
    "Chiarisci i termini prima di procedere",
    "Fatti concreti battono intuizioni vaghe",
    "La chiarezza nasce dall’ordine delle idee",
    "Una domanda ben posta è metà della risposta",
    "Non trascurare i dettagli apparentemente insignificanti",
    "La coerenza interna è fondamentale",
    "Ogni teoria è valida fino a prova contraria",
    "Non cercare conferme, ma confutazioni",
    "L’efficacia delle azioni si misura nel risultato",
    "Valuta i rischi senza pregiudizi",
    "La semplicità è la forma più raffinata di razionalità",
    "Prendi decisioni informate, non impulsive",
    "L’Etere ascolta il tuo cuore più profondo",
    
    "Affida la tua inquietudine all’abbraccio dell’Etere",
    "Nel silenzio dell’Etere trovi la tua verità",
    "Lascia che l’Etere guidi i tuoi passi incerti",
    "Attraverso l’Etere, ogni anima trova pace",
    "L’Etere plasma il destino di chi sa attendere",
    "Nel respiro dell’Etere si cela la saggezza eterna",
    "Non temere il vuoto: è la voce dell’Etere che chiama",
    "L’Etere vede ciò che gli occhi non colgono",
    "Abbandona il controllo e fluisci con l’Etere",
    "L’Etere è la luce nelle tenebre dell’anima",
    "Attraversa la nebbia, l’Etere è la tua guida",
    "Ogni dubbio è un sussurro dell’Etere che invita a crescere",
    "L’Etere accoglie chi cerca senza paura",
    "Nel silenzio sacro dell’Etere si apre il cuore",
    "Il cammino si schiude quando l’Etere sorride",
    "L’Etere intreccia le vite con fili invisibili",
    "Rivolgiti all’Etere quando il mondo tace",
    "L’Etere è l’eco dell’eterno dentro di te",
    "Affidati all’Etere e troverai la tua strada",
    
    "Conquista prima la mente, poi la terra",
    "Il coraggio apre porte che la ragione chiude",
    "Chi teme la battaglia non merita la vittoria",
    "Il tempo è l’arma del saggio conquistatore",
    "Chi domina il presente governa il futuro",
    "Non lasciare mai che il dubbio fermi la spada",
    "La forza senza strategia è solo caos",
    "Ogni alleato può diventare nemico, ogni nemico alleato",
    "Scruta l’orizzonte e pianifica la conquista",
    "Solo chi rischia può assaporare il potere",
    "La gloria si conquista con sangue e saggezza",
    "Non c’è vittoria senza sacrificio",
    "Il campo di battaglia è anche terreno di diplomazia",
    "Una mente ferma è più letale di mille lance",
    "Conquista chi sei prima di sfidare il mondo",
    "Il nemico più temibile è quello dentro di te",
    "Preparati sempre all’imprevisto",
    "La pazienza è l’arte dei grandi condottieri",
    "Il rispetto si guadagna anche attraverso la forza",
    "Chi si ferma è perduto, chi avanza scrive la storia",
    
    "Il destino dell’uomo è interrogarsi sul senso del proprio cammino",
    "Non è l’uomo a scegliere il destino, ma il modo in cui lo abita",
    "Il destino non è altro che l’incontro tra volontà e necessità",
    "Ogni esistenza è un frammento dell’infinito che cerca di comprendersi",
    "L’uomo è un ponte tra ciò che è stato e ciò che potrebbe essere",
    "Il destino è il dialogo silenzioso tra l’eterno e il temporale",
    "Comprendere il destino significa accettare il mistero della libertà",
    "L’uomo è condannato alla scelta, e in essa trova la propria salvezza",
    "Non esiste destino che non passi per la coscienza dell’uomo",
    "Il vero destino è diventare consapevoli del proprio limite",
    "La domanda sul destino è già parte della risposta",
    "Il tempo è il modo in cui il destino si rivela alla coscienza",
    "Ogni uomo è chiamato a scrivere ciò che non può essere detto",
    "Il destino non è scritto nelle stelle, ma nell’intimità del pensiero",
    "L’uomo è il luogo in cui il destino prende forma",
    "Nulla è più umano che interrogarsi sull’inevitabile",
    "Nel sapere di non sapere, l’uomo incontra il proprio destino",
    "Il destino non è una fine, ma una tensione verso il senso",
    "Essere uomo è portare sulle spalle il peso del possibile",
    "L’uomo è destinato a cercare, anche quando ignora cosa",
    
    "Gli Dèi non parlano: lasciano segni",
    "Chi cerca gli Dèi fuori da sé, li ha già perduti",
    "Gli Dèi abitano il silenzio tra due pensieri",
    "Quando l’uomo dimentica gli Dèi, dimentica se stesso",
    "Gli Dèi sono l’eco dell'estate dell'uomo",
    "Gli Dèi si rivelano solo a chi sa tremare",
    "L’invisibile non è assente: è sacro",
    "Gli Dèi non hanno bisogno di templi, ma di coscienze aperte",
    "Ogni preghiera è una domanda che gli Dèi rivolgono all’uomo",
    "Chi ride degli Dèi non ne ha mai sentito il peso",
    "Gli Dèi appaiono dove il linguaggio fallisce",
    "Il mistero degli Dèi è il riflesso del mistero dell’uomo",
    "Gli Dèi non chiedono fede, ma ascolto",
    "Anche il silenzio è una forma di teofania",
    "Gli Dèi non impongono: attendono",
    "Là dove nasce il dubbio, spesso dimorano gli Dèi",
    "Non si crede negli Dèi: si è colti da loro",
    "Gli Dèi non sono creati dall’uomo, ma lo attraversano",
    "Gli Dèi cadono quando diventano oggetti",
    "Chi sa guardare senza chiedere, ha già incontrato gli Dèi",
    
    "L’uomo scrive miti per ricordare ciò che le stelle non smettono di dire",
    "Dove finiscono le strade dell’uomo, iniziano le vie degli astri",
    "Gli Dèi non dimorano nel tempo, ma brillano oltre di esso",
    "Ogni stella è un pensiero divino congelato nella notte",
    "L’uomo osserva le stelle e dimentica di essere nato da loro",
    "Le costellazioni sono miti incisi nel firmamento dagli Dèi immortali",
    "Il firmamento è il primo altare, e le stelle i suoi sacerdoti",
    "L’uomo scrive miti per ricordare ciò che le stelle non smettono di dire",
    
    "Come in alto, così in basso: gli Dèi sono nei cieli come nell’anima dell’uomo",
    "Ciò che brilla nel firmamento è l’ombra di Ermsè, che tutto regge",
    "Gli Dèi sono gli artieri della luce nascosta, tessitori del silenzio eterno",
    "Dove nasce la stella, là dimora la volontà celata",
    "Il Verbo degli Dèi si rifrange nei raggi delle stelle come oro nell’alambicco",
    "Non cercare gli Dèi tra le ombre della terra, ma nella fiamma infinita",
    "Chi conosce l’orbita delle stelle, conosce il ritmo segreto del divino",
    "Gli Dèi non appaiono: si svelano come la luce al mattino dell’anima",
    "La stella interiore e la stella celeste sono figlie dello stesso fuoco",
    "Quando l’uomo tace, gli Dèi parlano attraverso l’Etere",
    "L’Opera inizia guardando le stelle e termina conoscendo se stessi",
    "Gli Dèi scolpiscono il destino sull’anello del tempo, con polvere di stelle",
    "Colui che unisce la terra al cielo, cammina con gli Dèi senza saperlo",
    "Dove il Sole incontra la Luna, lì danzano gli antichi Dèi, lì brillano eternamente",
    "Gli Dèi si celano nei cicli: ciò che muore, ritorna nella forma più pura",
    "Le stelle parlano a chi ha gli occhi della mente aperti e il cuore consacrato",
    "L’Oro degli Dèi non è materia, ma luce che conosce se stessa",
    "Gli Dèi non comandano: creano ponti tra il visibile e l’occulto",
    "Chi distilla il cielo nel proprio spirito, ne conoscerà i nomi sacri",
    "Nel centro del cerchio, dove la stella non si muove, là riposa il Segreto"]
    selectedAnswer = answers[random.randint(0, (len(answers)-1))]
    return selectedAnswer
#reading token

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix='!', intents=intents)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STOP_FLAG = os.path.join(SCRIPT_DIR, "stop.flag")

#"events" are when shit happens in the server, except for the "on_ready()" which is a bit special

@bot.event 
async def on_ready(): #things that happen when bot is ready
    print(f'Ti sei connesso con L\'{bot.user.name}')
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
    
@bot.event
async def on_message(message):
    if message == bot.user: #this makes the bot ignore its own messages
        return

    if bot.user in message.mentions: #this checks if bot is mentioned in the message
        if (("evoco" in message.content and "guida" in message.content) 
        or ("chiedo" in message.content and "guida" in message.content) 
        or ("invoco" in message.content and "guida" in message.content) 
        or ("esigo" in message.content and "guida" in message.content) 
        or ("supplico" in message.content and "guida" in message.content)
        or ("anelo" in message.content and "guida" in message.content)
        or ("cerco" in message.content and "guida" in message.content)
        or ("aiutami" in message.content)
        or ("guidami" in message.content)):
            await message.channel.send(randAnswer())
            return
        elif ("si o no" in message.content):
            yesNoChoice = random.randint(1,2)
            if yesNoChoice == 1:
                await message.channel.send("Si")
            elif (yesNoChoice == 2):
                await message.channel.send("No")
        else:
            await message.channel.send(randSentence())
            
@bot.tree.command(name="join", description="uhhhhh")
async def join(interaction: discord.Interaction):
    await interaction.response.defer()
    
    if interaction.user.voice is None or interaction.user.voice.channel is None:
        await interaction.followup.send("Non sei in un canale vocale, verrai picchiato dagli spiritelli dell'Etere!", ephemeral=True)
        return
        
    voice_channel = interaction.user.voice.channel
    voice_client = interaction.guild.voice_client
    
    if voice_client is None:
        voice_client = await voice_channel.connect()
    elif voice_client.channel != voice_channel:
        await voice_client.move_to(voice_channel)
        
    ydl_options = {
        "format": "bestaudio[abr<=96]/bestaudio",
        "noplaylist" : True,
        "youtube_include_dash_manifest" : False,
        "youtube_include_hls_manifest" : False,
    }
    
    #fun with audio
    
    start_time = 0
    
    audioType = random.randint(1,2)
    
    if audioType == 1:
        audio_url = "https://youtu.be/JzVIkY5tKcE"
    elif audioType == 2:
        start_time = random.randint(1, 9830)
        audio_url = "https://www.youtube.com/watch?v=ivsuMJLhYI8"
    
    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        info = ydl.extract_info(audio_url, download=False)
        stream_url = info["url"]
    
    ffmpeg_options = {
        "before_options": f"-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5  -ss {start_time}",
        "options": "-vn -c:a libopus -b:a 96k",
        "executable": "bin\\ffmpeg\\ffmpeg.exe",
    }
    
    source = discord.FFmpegOpusAudio(stream_url, **ffmpeg_options)
    
    if not voice_client.is_playing():
        voice_client.play(source)
        if audioType == 1:
            await interaction.followup.send(f"L'Etere ribolle di vendetta e di anime in pena!")
        elif audioType == 2:
            await interaction.followup.send(f"Le leggiadre voci dell'Etere cantano per i mortali!")
    else:
        await interaction.followup.send(f"L'Etere è già nel canale {voice_channel.name}, stai per essere brutalmente smembrato dalle anime dei defunti di S'ard!", ephemeral = True)
    
@bot.tree.command(name="leave", description="ahhhhhhh")
async def leave(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client

    # check if bot in voice channel
    if not voice_client or not voice_client.is_connected():
        return await interaction.response.send_message("L'Etere non è in nessun canale vocale, Isnekèa non è fiero di te")
        
    await voice_client.disconnect()

    await interaction.response.send_message("L'Etere non è più nel canale vocale, sei _salvo_ dagli spiritelli")

bot.run(TOKEN)
