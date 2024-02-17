# todo: food exihibit conversation bg #190

# todo: food main exhibit painting #226

image bg museum_food_top:
    "map-bgs/museum_food_top.png"
    zoom 1.15
    yalign 0.2

image badpainting:
    "items/badpainting.jpg"
    zoom 0.1
    yalign 0.5

image painting_food_floor:
    "items/Brussel_Sprouts.png"
    xalign 0.5
    yalign 1.0
    zoom 0.75

image painting_food:
    "items/Brussel_Sprouts.png"
    truecenter
    zoom 0.75

image eating:
    "items/personeatingfoodpainting.png"
    truecenter
    zoom 1.75

label museum_food:
    scene bg museum_food_top
    show posty neutral

    p "_" # todo: food exhibit imagemap #224

    menu:
        "Ripped Mitten & Unappetizing painting" if (quest.painting_food == False):
            jump .painting
        "Ripped Mitten" if quest.painting_food:
            jump .rm
        "Notepad":
            jump .notepad
        "Marble Bust":
            jump .marble
        "Corndog painting" if (food_switch == False):
            jump .corndog
        "Hidden passageway" if food_switch:
            jump janitors
        "Eating painting":
            jump .eating
        "Go back to the entrance.":
            jump museum_entrance

label .marble:
    scene bg museum_food
    show marble
    if quest.money_food:
        jump .marble3
    elif saw.marble:
        jump .marble2
    else:
        jump .marble1
    
    label .marble1:
    show posty neutral
    $ saw.marble = True
    marble "As an art critic and collector, I am severely disappointed with these so-called \"artworks\"! Everything here is so bland."
    p suspicious "..Okaay? Who are you?"
    marble "I am Marble Bust. My personal collection of fine art is one of the most respected in the art world! My name means something in this town!"
    marble "And as I said, this entire exhibit is lacking when it comes to wowing me! In fact, this entire museum has been rather upsetting. Nothing in here would fit for my collection!"
    if item.napkin:
        jump .marble_napkin
    else:
        p neutral "I don't know. I saw this one piece that-{nw}"
        marble "You clearly don't understand true art! Leave at once while I search for {b}the ultimate work of art{/b}!"
        jump museum_food

label .marble2:
    show posty neutral
    if item.napkin:
        jump .marble_napkin
    else:
        marble "Did you not hear me? Get out! I am trying to find {b}the ultimate work of art{/b}!"
    jump museum_food

label .marble_napkin: 
    marble "Hold on. What is that you're holding?"
    p "This?"
    show badpainting
    marble "Why... This is the greatest artwork I have ever seen! I simply must have it for my collection!! I will pay handsomely!"
    p suspicious "{i}Really??{/i}"
    p happy "Oh, I'm not sure! I don't want to give away this wonderful piece of art, but alright!"
    "You handed over the {b}priceless, one-of-a-kind highbrow painting{/b}!"
    $ item.napkin = False
    hide badpainting
    $ money += 2
    $ quest.money_food = True
    show cash_bundle_2 at truecenter
    $ renpy.transition(irisout, layer="master") #prevents interruption of the text window
    "{b}{color=#bdbb9a}Marble Bust{/color}{/b} gave you {b}some money{/b}!"
    hide cash_bundle_2
    call money_get
    p "Farewell!"
    jump museum_food

label .marble3:
    show posty neutral
    p "What are you going to do with your painting?"
    marble "I will hang it up proudly in my home proudly!"
    marble "The craft! The mediums! The deeper themes! You must tell me how you created this piece!"
    p "Oh, it's a complex forgotten art. You wouldn't get it. I'm sorry, but I'm busy right now."
    marble "Thank you for this masterpiece!"
    jump museum_food

label .notepad:
    scene bg museum_food
    show notepad
    if gave_chips:
        jump .notepad3
    elif saw.notepad:
        jump .notepad2
    else:
        jump .notepad1

label .notepad1:
    show posty concerned
    $ saw.notepad = True
    p "Oh my, are you alright?"
    notepad "Can't you tell?! I am at rock bottom here."
    notepad "I have turned my whole life upside down for the chance of exhibitions and now I can't even afford a bite to eat!!"
    notepad "Many times I pleaded and begged the curators to buy my life's work, many times they rejected me..."
    p sad "Man that sucks."
    notepad "Not even half of it. I reduced my prices all the way down to $2 for everything I ever made."
    notepad "You know what they said? No!"
    notepad "I am at my wits end: starving in the middle of the food exhibit."
    notepad "I should've stayed back home, then I wouldn't have ended up here."
    notepad "Time after time I put so much heart into this, only to be thrown out like a stray cup."
    notepad "I don't know why I bother."
    if item.chips:
        jump .notepad_chips
    else:
        notepad "Hey gal, you have any food?"
        p concerned "Sorry, I don't have a crumb on me."
        notepad "If you find some, please give it to me! I can hear my stomach rumbles from here!"
        p "Will do, will do."
        jump museum_food

label .notepad2:
    show posty neutral
    notepad "Oh hey, it's you again! Do you have any food on you now?"
    if item.chips:
        jump .notepad_chips
    else:
        p "Sorry, I still got nothing."
        notepad "Oh well. Let me know if you find any. I would appreciate it!"
        jump museum_food

label .notepad_chips:
        p "It isn't much, but I got a bunch of chips if you wan-"
        notepad "OOOHH PLEASE GIVE IT TO ME THANK YOU SO MUCH!!!"
        p "You need it more than I do."
        show generichips at truecenter
        "You handed over the {b}Generi-Chips{/b}!"
        $ item.chips = False
        $ gave_chips = True
        hide generichips
        notepad "This tastes soooo amazing!"
        notepad "First meal in a week, you are my shining saviour!"
        p happy "Glad to be of help!"
        notepad "For assisting me in my direst hour, you shall have my greatest work."
        notepad "It distills my essence into a small package you can carry around as a reminder."
        p astonished "Aw shucks, that is too much!"
        show badpainting
        "You got the {b}napkin \"painting\"{/b}! If this was in the eye of the beholder, then they would go blind."
        $ item.napkin = True
        hide badpainting
        p confused "Oohhheheh it looks... avant garde."
        notepad "This is for feeding me, only the best!"
        p happy "Hehe no biggie!"
        p suspicious quiet "(Did they pick up some trash to fool me? Why would anyone even consider this?)"
        p neutral quiet "(Eh whatever, it's free.)"
        p concerned "Ahahaha ohh I am soo sorry, I have a meeting in 30 minutes!"
        p concerned "I can't hang around any longer sadly..."
        notepad "It is a shame I can't see your enjoyment for any longer."
        p happy "See you around I guess!"
        jump museum_food
label .notepad3: #247
    show posty neutral
    notepad "_" # revisiting notepad
    jump museum_food

label .painting:
    scene bg museum_food
    show painting_food_floor
    show posty neutral
    show rm
    p "Um hi there!"
    rm "Oh hello! I'm currently looking at..."
    extend " whatever this is."
    rm "This {i}thing{/i} feels so out of place here... Honestly, they could've used a better painting."
    p happy "I'm sure someone would want it!"
    rm "Doubt it."
    hide rm with moveoutright
    show posty astonished
    "The odd painting suddenly and inexplicably calls out to you. You are filled with {color=#ffff00}{i}inspiration{/i}{/color}."
    p astonished quiet "{i}...I need it.{/i}"
    p happy quiet "{i}It's not like it'll be missed anyway!{/i}"
    hide painting_food_floor
    show painting_food
    "You got an {b}art piece{/b}! A strange painting depicting... brussel sprouts?"
    $ item.painting_food = True
    $ quest.painting_food = True
    $ paintings += 1
    hide painting_food
    if paintings == 1:
        p happy "Hehheheehehe! Oh I want to find more!"
    else:
        p happy "That was easy! I'm not complaining though!"
    jump museum_food

label .rm:
    scene bg museum_food
    show posty neutral
    show rm
    rm "Oh hey, what's up?"
    p "Nothing much, how about you?"
    rm "Eh, it could be better. I wanted to get a picture in front of a painting, but I think something's wrong with my camera."
    rm "All my photos are just a black screen! I'm not sure what to do."
    p concerned "Aw man!"
    p suspicious "You sure you don't have your lens cap on the lens?"
    rm "I hope not! Ha! That would be too easy to fix! I'm sure I'll figure it out eventually though."
    jump museum_food

label .corndog:
    scene bg museum_food
    show corndog
    show posty happy
    p "Ooooh corndog!"
    p suspicious "I don't see why it has to take up this much space. Guess it seems tasty?"
    p "It doesn't even look like it's held up on the wall... Weird."
    p "Oh well, time to look elsewhere."
    jump museum_food

label .eating: #233
    scene bg museum_food
    show eating
    show posty neutral
    if food_switch == False:
        p suspicious "Huh what is that doing there? Among all the food based pieces, it doesn't look that appetizing to look at someone eating."
        "The title of the painting is \"{i}Crisis of the Poplar Trees{/i}\". The rest of the text is too small to read at this distance." 
        p "The only thing true about the title is that guy is clearly having a crisis about something!"
        p "If I didn't know any better, I would've thought he was having some pizza psychosis..."
        label .eating_decide:
        menu:
            "Read more of the placard?"

            "Yes.":
                "You try to read more of the placard, but bonk your face on it by mistake!"
                #389 play a sound here! like a click!!!
                # and then a scene of the corndog painting disappearing, revealing the secret passageway.
                $ food_switch = True
                p confused "Well, that was weird. Wonder what that sound was!"
                jump museum_food
            "No.":
                p "_" # posty decides she is uninterested in reading more of the placard. she starts to walk away, but returns to the placard, still curious.
                jump .eating_decide
    else:
        p "_" # posty returns to actually read the placard this time.
        "The placard reads: \"{i}(something){/i}\". Weird!" # placard full text.
        p "_" # some kind of remark
        jump museum_food

