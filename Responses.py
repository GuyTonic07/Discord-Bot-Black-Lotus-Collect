
import random

###################################################### Game Changer list ###############################################
def get_gamechangerlist():
    gameChangerlist1 = '<:manaw:504110722649817099>[White](<https://scryfall.com/search?q=is%3Agamechanger+color%3DW+&unique=cards&as=grid&order=color>): Drannith Magistrate, Enlightened Tutor, Humility, Smothering Tithe, Teferi’s Protection\n<:manau:1362768231579779122>[Blue](<https://scryfall.com/search?q=is%3Agamechanger+color%3Du&unique=cards&as=grid&order=color>): Consecrated Sphinx, Cyclonic Rift, Expropriate, Fierce Guardianship, Force of Will, Gifts Ungiven, Intuition, Jin-Gitaxias Core Augur, Mystical Tutor, Narset Parter of Veils, Rhystic Study, Sways of the Stars, Thassa’s Oracle, Urza Lord High Artificer\n'
    gameChangerlist2 = '<:manab:504110722314403871>[Black](<https://scryfall.com/search?q=is%3Agamechanger+color%3Db&unique=cards&as=grid&order=color>): Bolas’s Citadel, Braids Cabal Minion, Demonic Tutor, Imperial Seal, Necropotence, Opposition Agent, Orcish Bowmasters, Tergrid God of Fright, Vampiric Tutor\n<:manar:504110722746417162>[Red](<https://scryfall.com/search?q=is%3Agamechanger+color%3Dr&unique=cards&as=grid&order=color>): Deflecting Swat, Gamble, Jeska’s Will, Underworld Breach\n<:manag:504110722343501824>[Green](<https://scryfall.com/search?q=is%3Agamechanger+color%3Dg&unique=cards&as=grid&order=color>): Natural Order, Seedborn Muse, Survival of the Fittest, Vorinclex Voice of Hunger, Worldly Tutor\n<:5c:1272218583354703982>[Multicolor](<https://scryfall.com/search?q=is%3Agamechanger+c>1&unique=cards&as=grid&order=color>): Grand Arbiter Augustin IV, Notion Thief, Yuriko the Tiger’s Shadow, Aura Shards, Winota Joiner of Forces, Kinnan Bonder of Prodigy, Coalition Victory\n<:manac:504110722331181066>[Colorless](<https://scryfall.com/search?q=is%3Agamechanger+-type%3Aland+color%3DC+&unique=cards&as=grid&order=color>): Chrome Mox, Grim Monolith, Lion’s Eye Diamond, Mana Vault, Mox Diamond, Panoptic Mirror, The One Ring\n<:manat:504110722540765204>[Land](<https://scryfall.com/search?q=is%3Agamechanger+type%3Aland+&unique=cards&as=grid&order=color>): Gaea’s Cradle, Ancient Tomb, Field of the Dead, Glacial Chasm, Mishra’s Workshop, The Tabernacle at Pendrell Vale\n'
    return (gameChangerlist1,gameChangerlist2)

##################################################### Quotes ###############################################
def get_response():
    quote_list = [
        'YOU ARE A TOY',  # Toy Story
        'I think a lot about meteors... the purity of them. BOOM! The end. Start again. The world made clean for the new man to rebuild. I was meant to be new. I was meant to be beautiful. The world would have looked to the sky and seen hope... seen mercy. Instead, they will look up in horror because of you.',  # Age of Ultron
        'There is a difference between you and me. We both looked into the abyss. But when it looked back at us… you blinked.',  # Justice League: Crisis on Two Earths
        'And the universe said I love you',  # Minecraft ending poem
        'You look like a calm and reasonable person',  # God of War: Ragnarok
        'Incredibilis',  # For Honor
        'Do you know what type of animal waits for its own slaughter? Sheep.',  # For Honor
        "I want to buy you something, but I don't have any money",  # The Drums - Money
        '4 pixels',  # SCP-096
        'One second of eternity has passed',  # Doctor Who
        'Do not be sorry, be better',  # God of War
        "What counts is not necessarily the size of the dog in the fight — it's the size of the fight in the dog",  # WW2 quote
        'You offer to the shrine but gain nothing\n  
         You offer to the shrine but gain nothing\n
         You offer to the shrine but gain nothing\n', # Risk of Rain 2
        'Dude, sucking is the first step to being sorta good at something',  # Adventure Time
        'WHY AREN’T YOU LAUGHING?',  # The Killing Joke
        'Breathe it in — that’s your own mortality',  # Batman v Superman
        'I love you 3000',  # Avengers: Endgame
        'Not even a Blood Moon can stop capitalism',  # Merchant - Terraria
        'Life... uh... finds a way',  # Jurassic Park
        "Nature doesn't give, it doesn't take. It merely says: it's in my nature",  # Dan Bull - Jurassic Park song
        'A man chooses, a slave obeys',  # BioShock
        'I fear no man. But that thing... it scares me.',  # Team Fortress 2 - Heavy
        "I’m not locked in here with you. You’re locked in here with me.",  # Watchmen
        'The game was rigged from the start',  # Fallout: New Vegas
        'Reality is often disappointing',  # Thanos
        'You either die a hero, or live long enough to see yourself become the villain',  # The Dark Knight
        'The universe is under no obligation to make sense to you',  # Neil deGrasse Tyson
        'You look lonely',  # Cyberpunk: Edgerunners
        "The world is not in your books and maps. It's out there",  # The Hobbit
        'Even the smallest person can change the course of the future',  # Lord of the Rings
        'War is a universal language',  # Captain Marvel
        'The world only makes sense if you force it to',  # Batman v Superman
        'A thousand times I’ve imagined this moment. Never like this.',  # Star Wars
        'Power comes in response to a need, not a desire. You have to create that need.',  # Dragon Ball Z
        'I finally know what it means... to fight for someone other than myself',  # Dragon Ball Super
        "There’s nothing wrong with being afraid. It’s the courage to face it that counts. And when you do, you’ll find it’s not as bad as you think. In fact, you might even start to laugh.",  # Star Fox / general
        "You'll laugh at your fears when you find out who you are",  # Piccolo (Dragon Ball Z: The History of Trunks)
        'Bow before me, or be broken',  # Mortal Kombat / general villain quote
        'I have no enemies',  # Thors - Vinland Saga
        'Sometimes, the world isn’t a nice place. But you gotta keep your soul clean',  # BoJack Horseman
        'Whatever happens, happens',  # Cowboy Bebop
        'Without something to believe in, people are just floating around',  # The Legend of Korra
        'If you find yourself dying, it’s probably because you’re doing something stupid',  # Deadpool / humor-based
        'Trust your instincts. The Darkness knows no honor',  # Star Fox Adventures
        "Introduce a little anarchy. Upset the established order, and everything becomes chaos",  # The Dark Knight
        'Why so serious?',  # The Dark Knight
        'The hardest part about this job isn’t running fast — it’s knowing when to slow down',  # The Flash
        'With great power comes great responsibility.',  # Spider-Man
        'The hardest choices require the strongest wills',  # Thanos
        'Peace through tyranny',  # Transformers / Megatron
        "You're gonna carry that weight",  # Cowboy Bebop
        'YOU SHALL NOT PASS!',  # Lord of the Rings
        'Humans don’t need gods. We need each other',  # God of War / general
        'There’s nothing more terrifying than the unknown. And I am the unknown',  # General villain quote
        'I am the rock against which the surf crashes. Nothing can move me. Nothing can break me.',  # God of War
        "Do you think God lives in Heaven because He, too, lives in fear of what He's created here on Earth?",  # Spy Kids 2
        'Then I shall face God and walk backwards into Hell',  # Meme / Tumblr
        "It's showtime.",  # Beetlejuice
        'IT WAS ME, BARRY!',  # Reverse Flash
        "This is the best I can do. This is exactly what I wanted. All of you, against all of me.",  # God of War
        'We have such sights to show you.',  # Hellraiser
        "I see now that the circumstances of one's birth are irrelevant. It is what you do with the gift of life that determines who you are",  # Mewtwo
        "Do you know what happens when a toad is hit by lightning?",  # Storm - X-Men (2000)
        "“your blood will water the foundation of my new universe”", # Wizard 101
        "if this relationship is gonna work out, I need to feel free to party with a bunch of strangers whenever I feel like it", # The lego movie
        "People already hate on you, don't do their job it makes it true" # jurrasic world rebirth 
    ]
    return random.choice(quote_list)
##################################################### Quotes ###############################################













