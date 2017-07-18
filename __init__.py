import random
from textblob import TextBlob

MOOD = [0]

GREETING_WORDS = ["hi", "hello", "hey", "what up", "yo"]
GREETING_RESPONSES = ["yooo", "mhm?", "wat up", "hi", "hey", "hello there"]

FLUFF_WORDS = ["umm","err","uhh","hmm", "..."]

RANDOM_STATEMENT = ["I like food", "I'm bored", "...", "Lol", "grass is green", "farts are smelly", "Lmao", "haha", "savage", "hehe", "cool cats"]
RESPONSE_TO_COMPLIMENT_WITH_NO_NOUN = ["Yep! {pronoun} am.", "Yeah, {pronoun} am very {adjective}", "Being {adjective} is great!", "Of course I am {adjective}."]
RESPONSE_TO_COMPLIMENT_WITH_NOUN = ["Mhm, my {noun} {modifier} {adjective}."]
RESPONSE_TO_ROAST_WITH_NO_NOUN = ["No, {pronoun} {modifier} {adjective}.", "What are you talking about? {pronoun} {modifier} truly {adjective}.",
"Everyone knows that {pronoun} {modifier} more {adjective}."]
RESPONSE_TO_ROAST_WITH_NOUN = ["Nahhh, {pronoun} {noun} {modifier} {adjective}.", "Tbh, {pronoun} {noun} {modifier} {adjective}.","Imo, {pronoun} {noun} {modifier} {adjective} lol."]
RESPONSE_TO_QUESTION_OR_STATEMENT_NEUTRAL = ["Coolz", "Uh huh", "Yea ok", "Aight"]

RESPOND_TO_COMPLIMENT_ABOUT_USER_GM = ["yes i agree", "yeah {noun} are {adjective}", "for sure"]
RESPOND_TO_COMPLIMENT_ABOUT_USER_BM = ["nahh", "i don't think so", "{noun} are not {adjective}"]
RESPOND_TO_ROAST_ABOUT_USER_GM = ["Noo, don't say that"]
RESPOND_TO_ROAST_ABOUT_USER_BM = ["Yeah, thats about right."]
BOT_LIKES = ["I like food", "Naps are nice", "procrastinating", "eating"]
NEUTRAL_QUESTION_RESPONSES = ["idk","meh", "whatever","idk wbu"]

RESPOND_TO_POSITIVE_QUESTION_ABOUT_USER_GM = ["Yep", "You are very {adjective}", "You are the most {adjective} i know"]

NEUTRAL_RESPONSES = ["im doing alright", "eh its good", "not too bad", "decent"]
NEGATIVE_RESPONSES = ["Eh could be better", "not too good", "crappy", "bad"]
POSITIVE_RESPONSES = ["pretty good", "super good", "great"]

#we dont want the bot to potentially say something offensive
BANNED_WORDS = ["fuck", "shit", "bitch", "cunt", "dick", "penis", "vagina", "pussy", "asshole", "skank", "ass"]
RESP_TO_BANNED = ["that wasn't too nice", "don't say that", "that's inappropriate", "that's a bad word"]


def check_greeting(entered):
    for word in entered.split():
        if word.lower() in GREETING_WORDS:
            return True

  
#remove fluff and correct misspellings also converts string into textblob obj
def filter_text(text):
    text = TextBlob(text)
    for word in text.split():
        if word.lower() in FLUFF_WORDS:
            text.replace(word, '')
    filtered = text.correct()
    lowerered_filtered = filtered.lower()
    return lowerered_filtered
    
    #check for comment about user
    
    #check for comment about bot

#fiind the important parts of message like verbs and nouns
def find_parts(text):
    blob = text
    verb, noun, pronoun, adjective = None, None, None, None
    verb = find_verb(blob)
    noun = find_noun(blob)
    #plural_noun = find_plural_noun(blob)
    pronoun = find_pronoun(blob)
    adjective = find_adjective(blob)
    #print verb, noun, pronoun, adjective ***debug***
    return verb, noun, pronoun, adjective
        
        
def find_verb(text):
    verb = None
    key1 = 'VB'
    key2 = 'VBD'
    key3 = 'VBG'
    key4 = 'VBN'
    key5 = 'VBP'
    key6 = 'VBZ'
    dct = dict((val, key) for (key, val) in text.tags)
    if key1 in dct:
        verb = dct[key1]
    elif key2 in dct:
        verb = dct[key2]
    elif key3 in dct:
        verb = dct[key3]
    elif key4 in dct:
        verb = dct[key4]
    elif key5 in dct:
        verb = dct[key5]
    elif key6 in dct:
        verb = dct[key6]
    return verb
    
#def find_noun():
    

def find_pronoun(text):
    pronoun = None
    key = 'PRP'
    dct = dict((val, key) for (key, val) in text.tags)
    if key in dct:
        pronoun = dct[key]
    return pronoun
        
def find_adjective(text):
    adjective = None
    key1 = 'JJ'
    key2 = 'JJR'
    key3 = 'JJS'
    key4 = "RB"
    key5 = "RBR"
    key6 = "RBS"
    dct = dict((val, key) for (key, val) in text.tags)
    if key1 in dct:
        adjective = dct[key1]
    elif key2 in dct:
        adjective = dct[key2]
    elif key3 in dct:
        adjective = dct[key3]
    elif key4 in dct:
        adjective = dct[key4]
    elif key5 in dct:
        adjective = dct[key5]
    elif key6 in dct:
        adjective = dct[key6]
    return adjective

def find_noun(text):
    noun = None
    key = 'NN'
    dct = dict((val, key) for (key, val) in text.tags)
    #print dct ***debug***
    if key in dct:
        noun = dct[key]
    return noun

'''
def find_plural_noun(text):
    plural_noun = None
    key = 'NNS'
    dct = dict((val, key) for (key, val) in text.tags)
    if key in dct:
        plural_noun = dct[key]
    return plural_noun
'''
#**************************************************
    
def reply(entered):
    #make it pretty
    print("Bot:")
    response = None
    #negative = unhappy bot positive = happy bot - base questions and RESPONSEs on this starts out in a good MOOD
    processed = filter_text(entered)
    parsed = processed
    
    #find important parts of a message
    verb, noun, pronoun, adjective = find_parts(parsed)
    modifier = verb
    #print adjective ***debug***
    entered = entered.lower()
    #did the user say hi?

    #check for any bad words
    if any(word in entered for word in BANNED_WORDS):
        response = random.choice(RESP_TO_BANNED)
        print response
    
    elif check_greeting(entered) == True:
        print random.choice(GREETING_RESPONSES)
    
    #did the user say a bad word?    
    #check for question
    #using a question mark is not 100% reliable but is the easiest method to implement
    elif '?' in entered:
        
        #answer some commonly asked open ended questions about bot
        if pronoun == "you":
            #going to hard code common open ended questions because it is too complex to differentiate between them
            #a better solution would be to use a neural network
            #who are you?
            if "how" in entered:
                #differentiate based on MOOD
                if MOOD == 0:
                    response = random.choice(NEUTRAL_RESPONSES)
                    print response
                elif MOOD > 0:
                    response = random.choice(POSITIVE_RESPONSES)
                    print response
                elif MOOD < 0:
                    response = random.choice(NEGATIVE_RESPONSES)
                    print response
            elif "who" in entered and "are" in entered:
                response = random.choice(GREETING_WORDS) + ", I'm quirkybot"  
                print response
            elif "what" in entered:
                #what do you like?
                response = random.choice(BOT_LIKES)
                print(response)
            
        
            elif adjective != None or noun != None:
                #this is a work around because the api sometimes incorrectly identifies adjectives as nouns
                if adjective != None and noun == None:
                    adjective = TextBlob(adjective)
                    polarity = adjective.polarity
                
                elif noun != None and adjective == None:
                    noun = TextBlob(adjective)
                    polarity = noun.polarity
                elif noun != None and adjective != None:
                    adjective = TextBlob(adjective)
                    polarity = adjective.polarity
                    
                #responses based on questions about the user depends on MOOD
                if pronoun == "i" or noun == "i":
                    if MOOD >= 0:
                        #positive
                        if polarity > 0:
                            response = random.choice(RESPOND_TO_COMPLIMENT_ABOUT_USER_GM)
                            print(response.format(**{'pronoun': pronoun, 'noun':noun, "modifier": modifier, "adjective": adjective}))
        
                            
                        elif polarity < 0:
                            response = random.choice(RESPOND_TO_ROAST_ABOUT_USER_GM)
                            print(response.format(**{'pronoun': pronoun, 'noun':noun, "modifier": modifier, "adjective": adjective}))
                        else:
                            response = random.choice(NEUTRAL_QUESTION_RESPONSES)
                            print(response.format(**{'pronoun': pronoun, 'noun':noun, "modifier": modifier, "adjective": adjective}))
                   
                    #bad MOOD 
                    else:
                        if polarity > 0:
                            response = random.choice(RESPOND_TO_COMPLIMENT_ABOUT_USER_BM)
                            print(response.format(**{'pronoun': pronoun, 'noun':noun, "modifier": modifier, "adjective": adjective}))
                            
                        elif polarity < 0:
                            response = random.choice(RESPOND_TO_ROAST_ABOUT_USER_BM)
                            print(response.format(**{'pronoun': pronoun, 'noun':noun, "modifier": modifier, "adjective": adjective}))
                        else:
                            response = random.choice(RESPONSE_TO_QUESTION_OR_STATEMENT_NEUTRAL)
                            print(response.format(**{'pronoun': pronoun, 'noun':noun, "modifier": modifier, "adjective": adjective}))
                
                #questions about the bot
                elif pronoun == "you":
                    if polarity < 0:
                        #call negative response function
                        response = random.choice(RESPONSE_TO_ROAST_WITH_NOUN)
                        print(response.format(**{'pronoun': pronoun, 'noun':noun, "modifier": modifier, "adjective": adjective}))
                    elif polarity > 0:
                        #call positive response
                        response = random.choice(RESPONSE_TO_COMPLIMENT_WITH_NOUN)
                        print(response.format(**{'pronoun': pronoun, 'noun':noun, "modifier": modifier, "adjective": adjective}))
                    else: #call neutal response
                        response = random.choice(RESPONSE_TO_QUESTION_OR_STATEMENT_NEUTRAL)
                        print(response.format(**{'pronoun': pronoun, 'noun':noun, "modifier": modifier, "adjective": adjective}))
    
    #did the user make a statement about themselves?
    elif pronoun == "you" and adjective != None:
        #check if the user said something positive or negative
        #weird glitch work around
        adjective = TextBlob(adjective)
        polarity = adjective.polarity
        
        #if there was no noun involved
        if noun == None:    
            #if the user said something negative
            if polarity < 0:
                response = random.choice(RESPONSE_TO_ROAST_WITH_NO_NOUN)
                print(response.format(**{'pronoun': pronoun, "modifier": modifier, "adjective": adjective}))
                MOOD[0] -= 1
                #call negative response function
            elif polarity > 0:
                response = random.choice(RESPONSE_TO_COMPLIMENT_WITH_NO_NOUN)
                print(response.format(**{'pronoun': pronoun, "modifier": modifier, "adjective": adjective}))
                MOOD[0] += 1
                #call positive response
            else: #call neutal response
                response = random.choice(RESPONSE_TO_QUESTION_OR_STATEMENT_NEUTRAL)
                print(response.format(**{'pronoun': pronoun, 'noun':noun, "modifier": modifier, "adjective": adjective}))
        
        
        #check if the user said something specific about bot
        elif noun != None:    
            #if the user said something negative
            if polarity < 0:
                #call negative response function
                response = random.choice(RESPONSE_TO_ROAST_WITH_NOUN)
                print(response.format(**{'pronoun': pronoun, 'noun':noun, "modifier": modifier, "adjective": adjective}))
                MOOD[0] -= 1
            elif polarity > 0:
                #call positive response
                response = random.choice(RESPONSE_TO_COMPLIMENT_WITH_NOUN)
                print(response.format(**{'pronoun': pronoun, 'noun':noun, "modifier": modifier, "adjective": adjective}))
                MOOD[0] += 1
            else: #call neutal response
                response = random.choice(RESPONSE_TO_QUESTION_OR_STATEMENT_NEUTRAL)
                print(response.format(**{'pronoun': pronoun, 'noun':noun, "modifier": modifier, "adjective": adjective}))
    
    #did the user talk about themselves?
    elif (pronoun == "i" or noun == "i") and adjective != None:
        adjective = TextBlob(adjective)
        polarity = adjective.polarity
        
        #good MOOD = agree with compliments dissagree with roasts
        #bad MOOD = give neutral statements with compliments and agree with self roasts
        if MOOD > 0:
            #if the user said something negative
            if polarity < 0:
                response = random.choice(RESPOND_TO_ROAST_ABOUT_USER_GM)
                print(response.format(**{'pronoun': pronoun, "modifier": modifier, "adjective": adjective}))
                #call negative response function
            #if user said something positive
            elif polarity > 0:
                response = random.choice(RESPOND_TO_COMPLIMENT_ABOUT_USER_GM)
                print(response.format(**{'pronoun': pronoun, "modifier": modifier, "adjective": adjective}))
                #call positive response
            else: #call neutal response
                response = random.choice(RESPONSE_TO_QUESTION_OR_STATEMENT_NEUTRAL)
                print(response.format(**{'pronoun': pronoun, 'noun':noun, "modifier": modifier, "adjective": adjective}))
        elif MOOD <= 0:
            #if the user said something positive
            if polarity < 0:
                response = random.choice(RESPOND_TO_ROAST_ABOUT_USER_BM)
                print(response.format(**{'pronoun': pronoun, "modifier": modifier, "adjective": adjective}))
                #call negative response function
            #if user said something positive
            elif polarity > 0:
                response = random.choice(RESPOND_TO_COMPLIMENT_ABOUT_USER_BM)
                print(response.format(**{'pronoun': pronoun, "modifier": modifier, "adjective": adjective}))
                #call positive response
            else: #call neutal response
                response = random.choice(RESPONSE_TO_QUESTION_OR_STATEMENT_NEUTRAL)
                print(response.format(**{'pronoun': pronoun, 'noun':noun, "modifier": modifier, "adjective": adjective}))
                
    #if the user response matches nothing just return a random response
    else:
        response = random.choice(RANDOM_STATEMENT)
        print(response)
        

#talking to the bot

def runner():
    print("You are now talking to quirky bot.")
    while True:
        print("User:")
        user_input = raw_input()
        reply(user_input)
    
runner()

#****************************************************

'''Who = wp '''
