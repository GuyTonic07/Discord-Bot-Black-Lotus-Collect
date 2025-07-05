
import random
import requests
from bs4 import BeautifulSoup

##################################################### WebScrapper ###############################################


def get_deck_priceArch(decklink): #Archidekt Code
    try:
        # Send a request to fetch the content of the page
        response = requests.get(decklink)
        
        if response.status_code == 200:
            # Parse the content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the price element with the specific class
            price_element = soup.find('span', class_='deckPrice_orange__dSAUq')

            if price_element:
                price_text = price_element.text.strip()
                price = float(price_text[1:])  # Convert price text to float
                if price > 0:
                    return price  # Return the price if it's greater than zero
                else:
                    return None  # Return None for non-positive prices
            else:
                return None  # Price element not found
        else:
            return None  # Failed to fetch the webpage
    except Exception as e:
        return None  # An error occurred
    
#################################################Tapped out################################################
    
def get_deck_price_tapped(decklink): # Tappedout Code
    try:
        # Send a request to fetch the content of the page
        response = requests.get(decklink)
        
        if response.status_code == 200:
            # Parse the content of the page
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all span elements with class 'pull-right'
            price_elements = soup.find_all('span', class_='pull-right')
            
            prices = []
            
            for element in price_elements:
                price_text = element.text.strip()
                
                # Split the price range if present
                price_range = price_text.split(' - ')
                
                if len(price_range) == 2:
                    min_price = price_range[0][1:]  # Remove the dollar sign
                    max_price = price_range[1][0:]  # Remove the dollar sign
                    prices.append((min_price, max_price))
                else:
                    base_price = price_range[0][1:]  # Remove the dollar sign
                    prices.append((base_price,))
            
            return prices
        else:
            return None  # Failed to fetch the webpage
    except Exception as e:
        print(f"An error occurred: {e}")
        return None  


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
        'You offer to the shrine but gain nothing\n',  # Risk of Rain 2
        'You offer to the shrine but gain nothing\n',
        'You offer to the shrine but gain nothing\n',
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
    ]

    return random.choice(quote_list)




