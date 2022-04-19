

## Act 4 - Start

label act_four:

    scene black

    $ player_name = renpy.input("What would you like to name the MC?")
    if player_name.strip() == "":
      $ player_name = "Byron"

    menu:
        "Choose your path"

        "Octavia's Path":
            $ octavia = True

        "Dallas's Path":
            $ dallas = True

    menu:
        "Choose your path\nMonogamy: One Sexual Partner\nPolyamory: Multiple Sexual Partners"

        "Monogamy":
            $ monogamy = True
            $ polygamy = False

        "Polyamory":
            $ polygamy = True
            $ monogamy = False

    $ persistent.galleryName = "[player_name]"

    jump act_four_s

label act_four_s:

    stop music fadeout 2.0

    scene avalon with fade

    if persistent.actFour == False:
        $ renpy.notify("You've unlocked Act Four in Act Select on the Main Menu!")
        $ persistent.actFour = True

    pause

    scene avalonactfour with dissolve

    pause

    scene 1wakeup4 with fade

    ai3 "{i}Wow, he's really out.{/i}"
    ai3 "{i}I want to let him sleep but I'm too excited.{/i}"
    ai3 "{i}I want him to see the new me!{/i}"

    a3 "Uncle?"

    b "Uhnmn"

    a3 "Uncle [player_name]."
    a3 "Wake up, Sleepyhead."

    scene 3wakeup4 with dissolve

    b "Hmm?"

    scene 4wakeup4 with dissolve

    b "Did you--?"

    scene 5wakeup4 with dissolve

    b "Wah..!"
    b "Avalon."
    b "I don't want to alarm you."

    ai3 "{i}He noticed!{/i}"

    b "But something happened to your hair."

    scene 2wakeup4

    a3 "Yeah?"

    b "It looks like it turned brown overnight."

    a3 "Oh yeah?"
    ai3 "{i}Tell me what you think, dammit!{/i}"

    b "It's the color of..."
    b "Maple Syrup, actually."

    scene 6wakeup4

    b "Did it happen after you got bit by a Canadian?"
    b "The only way to tell is if after one bit you, they'd say something like..."
    b "'Sorry eh, I was just polishing my hockey stick and I must've tripped and
        accidentally bit you.'"
    b "'Let me take yoo ta a Canadian hospital, eh.'"
    b "'Where you can 'ave free medical care and virtually no risk of being shot, eh.'"

    scene 7wakeup4

    menu:
        "{b}Additional Dialogue Choice{/b}"
        "Agreed!":
            a3 "It sounds as if you're making fun of Canadians but all those seem
                        like relatively positive things."

            b "Yeah, you got me."
            b "Canada is fuckin' awesome."

        "Racist!":
            a3 "Stereotypes like these are why Canada doesn't like us."
            a3 "That, and we use the imperial system."

            b "Pfft! Canadians don't even know how to dislike!"

        "... What?":
            a3 "Are you implying that if you get bit by a Canadian, you turn into...
                syrup?"
            a3 "Like, I don't even--"
            a3 "You know what, nevermind."

    scene 2wakeup4 with dissolve

    a3 "Come on, tell me what you think!"
    a3 "Don't keep me in suspense!"

    scene 5wakeup4

    b "Mm, I don't know."
    b "You look beautiful."
    b "But you looked beautiful before too."

    scene 2wakeup4

    a3 "Okay, you can make up your mind after I finish."
    a3 "I've still got another round of dye to do."

    scene 8wakeup4 with dissolve

    b "Listen, Avalon, I wanted to talk to you about last night."
    b "I want you to know that I want to tell you everything."
    b "I really do."
    b "But I just can't yet."

    scene 9wakeup4

    a3 "We're in a relationship now, aren't we?"
    a3 "That means we're partners."
    a3 "We're in this together."

    scene 8wakeup4

    b "This isn't something I want to keep from you, Avalon."
    b "This is something dangerous that I want to keep you separate from."
    b "I don't want anything to happen to you."
    b "And this secret... it's bad."

    scene 11wakeup4

    a3 "Are you in danger??"
    a3 "Please tell me you're not!"

    scene 10wakeup4

    b "I... I don't know."
    b "Penny wasn't supposed to investigate... this."
    b "But she's sharp."
    b "I just didn't think she'd dig this deep."

    scene 9wakeup4

    a3 "Can you at least tell me what it's regarding?"
    a3 "I mean, the curiosity is really eating at me."
    a3 "And now I'm worried about you."

    scene 8wakeup4

    b "I didn't..."
    b "I didn't create a fitness app."
    b "The money I have came from my father."
    b "And he gave it to me to keep this secret."

    scene 13wakeup4

    a3 "You lied about that?"
    a3 "But it was to keep me safe, right?"
    a3 "If Penny found out, does that mean she's in danger?"

    scene 14wakeup4

    b "I don't know, Avalon."
    b "But I'm going to contact Officer Evans today."
    b "I can't tell him about what Penny found out but I can at least warn him
        that she might be in danger."
    b "It's a little risky for me but it wouldn't be right not to."

    a3 "I understand but..."

    scene 15wakeup4 with dissolve

    a3 "Please be safe, Uncle [player_name]."
    a3 "You're my everything now."
    a3 "I need you."

    b "Nothing is going to happen to us."
    b "I'll figure this out and make it right."
    b "I promise."

label galleryScene1:
    if _in_replay:
        $ player_name = renpy.input("What would you like to name the MC?")
        if player_name.strip() == "":
          $ player_name = "Byron"

    scene 16wakeup4 with fade

    b "I don't actually know his number."
    b "I can't just call 911, right?"
    b "Avalon, how... what do I do here?"

    a3 "I dunno, call information!"

    b "What is that?"
    b "How do you do that?"

    scene 17wakeup4 with dissolve

    b "Phone, call information."
    b "..."
    b "Is that not right?"
    b "Phone, respond or be destroyed."
    b "..."
    b "Damn, threats don't work either."
    b "It's really stubborn."

    scene 18wakeup4 with dissolve

    a3 "Uncle, it can't be reasoned with, it can't be bargained with."
    a3 "It doesn't feel pity or remorse or fear."
    a3 "And it absolutely will not stop--"

    b "Don't quote movie lines right now!"
    b "Help me!"

    a3 "How did I actually believe you created a phone app??"

    scene 19wakeup4 with dissolve

    a3 "Okay, dial 411."

    b "4-1-1"

    a3 "Now let's see if someone answers."

    scene 22wakeup4 with dissolve

    "Information, how can I be of assistance?"

    b "Uhh, yes, I'd like to contact a local police officer by the name of Evans."

    "Please hold while I redirect your call to your local police department."

    "*Ring* *Ring*"

    "Thank you for contacting your local police department, your call is very important to us."

    b "... Seriously?"
    b "An automated service??"

    scene 20wakeup4 with dissolve

    "If you know your party's extension, please dial now."
    "If you're looking for Detective Callahan, please press the pound sign followed
        by forty-four."
    "If you're looking for Officer Murphy, please press the pound sign followed by
        eighty-seven."
    "If you're looking for Detective Evans,"

    scene 21wakeup4 with dissolve

    a3 "That one!"

    "Please press the pound sign followed by ninety-nine."

    a3 "Press ninety-nine, press ninety-nine!"
    a3 "No no, the pound sign first!"

    b "Shit!"
    b "Don't rush me!"
    b "Uhh, number sign thingy, nine, nine."

    scene 22wakeup4 with dissolve

    "*Ring* *Ring*"

    det "Officer Ev--"
    det "I mean,"
    det "Detective Evans speaking."

    b "This is [player_name]."
    b "We spoke briefly yesterday."
    b "I was having a meeting with Penny in the Lingerie Store..."

    det "I remember."
    det "What can I do for you, Mr. [player_name]?"

    scene 23wakeup4 with dissolve

    b "Actually, I was hoping we could speak in person."

    det "Regarding Penny?"

    b "Yes, that's right."

    det "Sure thing!"
    det "Why don't you swing by my office--"

    scene 24wakeup4 with dissolve

    b "Gah!"

    det "Is... everything alright, Sir?"

    b "Y-yes, my cat is just being very affectionate all of the sudden."

    det "I understand."
    det "They can be quite needy."

    b "Right, I think she just needs some attention."

    det "Like I was saying, why don't you stop by the station?"
    det "Say, thirty minutes?"

    b "Yeah, that sounds--"

    scene 25wakeup4 with dissolve

    b "Ahh!"

    det "Quite a frisky cat you have there, by the sounds of it."

    b "Yeah, very frisky."
    b "But yes, that s-sounds great."
    b "Thirty minutes!"

    det "See you soon, Mr. [player_name]."

    b "Yep!"

    "*Click*"

    scene 26wakeup4 with dissolve

    b "You... are so freakin' dead."

    a3 "I'm just a poor witty kitty in need of attention."
    a3 "Won't you pet me, Master?"
    a3 "Pretty please?"

    scene 27wakeup4 with dissolve

    b "You've been watching those damn Japanese cartoons again, haven't you?!"
    b "I can't believe you would do that to me while I was on the phone with a police officer!"
    b "You are in so much trouble, Missy!"

    scene 28wakeup4

    a3 "I was naughty, Uncle!"
    a3 "I think I need to be punished."
    a3 "What do you want to do to me?"

    scene 29wakeup4 with dissolve

    play music "audio/cause.mp3"

    b "Oh I have a few ideas."
    b "Come here, girly!"

    a3 "This is so exciting!"

    scene 30wakeup4

    play sound "audio/bodyfallmat.mp3"

    a3 "Oof!"

    scene 31wakeup4 with dissolve

    ai3 "{i}Whoa!{/i}"
    ai3 "{i}He just pulled me over the couch!{/i}"

    b "I'm sorry!"
    b "That might have been-"

    a3 "Shut up."
    a3 "Stop talking."

    b "Huh?"

    a3 "That was really hot!"
    a3 "Keep going."

    b "Uhh, alright."
    b "Lift your leg up."

    scene 31wakeup42 with dissolve

    a3 "My... leg?"
    a3 "Like this?"

    b "Yeah, we don't need this in the way."

    scene 31wakeup43

    play sound "audio/wood_movement.mp3"

    pause

    scene 32wakeup4

    a3 "Woah."

    scene 33wakeup4 with dissolve

    b "Avalon."

    a3 "Y-yes, Uncle?"

    b "Are you going to be a good girl from now on?"

    a3 "No!"
    a3 "Uhh, nope."
    a3 "I think... I need to be taught a lesson."

    scene 34wakeup4

    b "You know what I think, Avalon?"

    a3 "W-what?"

    b "I think your hands are the problem."

    a3 "My... my hands??"

    b "Yeah."
    b "They're just free to do whatever they want."
    b "Maybe we need to pin one down."

    scene 35wakeup4 with dissolve

    a3 "What are you doing??"
    a3 "Why are you grabbing my arm??"

    scene 36wakeup4 with dissolve

    a3 "Oh my god!"
    a3 "Uncle, I'm really, really horny right now!"

    b "Oh yeah?"
    b "Is there something you want me to do to you right now, Avalon?"

    a3 "Y-yes!"
    a3 "There is!"

    b "What do you want?"

    scene 37wakeup4 with dissolve

    a3 "I want..."
    a3 "I want you to..."

    b "What?"
    b "Say it."

    a3 "I want you to play with my vagina."

    b "This isn't an anatomy class."
    b "Come on, tell me what you want."

    scene 38wakeup4 with dissolve

    a3 "I want you..."
    a3 "To play with my pussy."

    b "Well, I can't play with your pussy if your legs are in the way."

    scene 39wakeup4 with dissolve

    pause (.5)

    scene 40wakeup4 with dissolve

    a3 "Whoa!"
    a3 "Okay, this is happening."

    scene 41wakeup4 with dissolve

    pause (.5)

    scene 42wakeup4 with dissolve

    a3 "Ah!"
    a3 "Wow!"
    a3 "This is really intense!"

    scene 43wakeup4 with dissolve

    b "Is this what you want me to play with, Avalon?"

    a3 "Yes!"
    a3 "Please!"
    a3 "Please play with my pussy!"

    b "Alright, since you asked so nicely."

    scene 44wakeup4 with dissolve

    a3 "Oh!"
    a3 "Uncle, your fingers!"
    a3 "They're so big!"

    scene 45wakeup4 with dissolve

    a3 "Oooh, fuck."
    a3 "Please massage it!"
    a3 "Please please!"

    show wakeup4 with slowdissolve

    a3 "Mmmhh!"

    b "Like this?"

    a3 "Mhmm!"

    b "Your panties are soaking wet, Avalon."
    b "You don't want to ruin them, do you?"

    a3 "No."

    b "Well, we better move them aside then."

    scene 46wakeup4 with dissolve

    a3 "Wait, what?"
    a3 "What are you doing?"

    scene 47wakeup4 with dissolve

    a3 "Oh no!"
    a3 "Uncle, I'm completely exposed!"
    a3 "This is too much!"

    scene 48wakeup4 with dissolve

    stop music fadeout 2.0

    a3 "It's too intense now."
    a3 "I.."
    a3 "I want to stop."
    a3 "Please stop!"

    scene 49wakeup4

    b "Alright, I'm stopping."
    b "Did I take it too far?"
    b "I'm sorry."
    b "You just seemed--"

    a3 "No!"
    a3 "You didn't!"
    a3 "I--!"

    scene 50wakeup4 with dissolve

    a3 "Oh my god, I'm the one that should be sorry."
    a3 "You were a lot different when we were being intimate today."
    a3 "It was really sexy!"
    a3 "But it kind of scared me a little bit too..."
    a3 "I'm so embarrassed."
    a3 "I want to experience this stuff really badly but--"

    b "Avalon, you don't have to explain."
    b "I know you don't like it when I joke around while we're playing so I thought
        I'd try a different approach today."

    scene 51wakeup4 with dissolve

    b "But listen, we'll take it as slow as you want and as far as you want."
    b "We'll stop when you want."
    b "And we can try again later."
    b "If you want."
    b "And if you like something or don't like something that we do, just tell me."
    b "Communication is important."
    b "Okay?"

    a3 "Okay."
    a3 "Thank you, Uncle."
    a3 "This really was a lot of fun."

    b "I've got to go meet Detective Evans now."
    b "I'm probably already late."
    b "We'll mark this as 'To be continued!'"

    if persistent.playhard == False:
        $ renpy.notify("You've unlocked 'Play Hard' in the Scene Gallery on the Main Menu!")
        $ persistent.playhard = True

    a3 "Alright."
    a3 "I might take a nap."
    a3 "Bye, Uncle."

    b "Bye for now, my Avalon."

    $ renpy.end_replay()
    scene 1evansoffice with fade

    det "My office..."
    det "This is my office."
    det "I still can't believe it."
    det "This is definitely going to take some getting used to."

    play sound "audio/doorknock.mp3"

    scene 2evansoffice with dissolve

    det "Hmm?"
    det "Who is it?"

    b "It's [player_name]."
    b "We spoke on the phone about half an hour ago."

    det "Oh, [player_name]."
    det "Come on in."

    play sound "audio/dooropen.mp3"

    pause

    play sound "audio/doorclose.mp3"

    scene 3evansoffice

    b "I don't mean to waste your time today, Officer."

    det "Detective."

    b "Oh, right."
    b "Sorry about that."

    scene 4evansoffice

    det "Don't worry about it."
    det "I'm still getting used to it myself!"

    scene 5evansoffice with dissolve

    pause

    scene 6evansoffice with dissolve

    det "It's nice to meet you, [player_name]."

    b "Congratulations on the promotion."

    det "I've been working towards this for eight years."

    scene 7evansoffice with dissolve

    det "Please, have a seat."

    b "Alright, thanks."

    scene 8evansoffice with dissolve

    det "Now I know the office ain't much to look at right now."
    det "But it's all mine!"
    det "And after a bit of my own spice, it's going to look real groovy."

    scene 9evansoffice with dissolve

    bi "{i}Hmm?{/i}"
    bi "{i}Why is he coming back here..?{/i}"

    det "Now I know you're here to talk about Penny."
    det "And if you're wonderin', yeah."
    det "She's a big part of why I'm a detective now."

    scene 10evansoffice

    pause (.5)

    scene 11evansoffice with dissolve

    play music "audio/red_head.mp3"

    det "I've worked real hard to get here."
    det "I spend time studyin', I keep in shape."
    det "I do what it takes to be great at my job."
    det "But Penny?"
    det "Man, I can't hold a candle to that woman."

    scene 12evansoffice

    bi "{i}Why is he sitting back here instead of at his desk?{/i}"
    bi "{i}Maybe he isn't used to having an office yet?{/i}"
    bi "{i}Or..?{/i}"

    scene 16evansoffice with dissolve

    b "Detective, when I hired Penny, it was because she was remarkably convincing
        that she's exceptional at what she does."
    b "But every time I think about her now, she's just a small, young girl."
    b "I feel like I just put her in danger and I'm going to get her killed."

    scene 14evansoffice

    det "I know exactly how you feel."
    det "Sometimes I {b}still{/b} think the same thing when I look at her."
    det "I wonder how I could work with a little girl like her, ya know?"

    scene 15evansoffice with dissolve

    det "But brother, let me tell you something."
    det "I tried to sneak up on her once."
    det "I was in socks and there was music blarin' so there's no way she heard me."
    det "Before I got within four steps of her, she kicked a can behind her and hit me
        right in the thigh."
    det "I'm pretty sure she was aimin' at my thigh."
    det "She could have hit me in the testicles if she wanted to."

    scene 13evansoffice

    b "Count your blessings, Detective."
    b "At least she has the decency not to actually hit you in the crotch."
    b "So it sounds like you're telling me she's skilled at her trade."
    b "But what's with the stories? They're elaborate and ridiculous."

    scene 17evansoffice

    det "No idea why she does that!"
    det "The other day, she told me she uppercut a horse so hard, she turned it
    into a giraffe!"
    det "Then she tells me she had a sandwich for lunch."
    det "But bro, I don't know if she had a sandwich for lunch because she's got no credibility."
    det "Maybe she didn't have a sandwich, maybe she had a muffin. Who knows!?"

    scene 16evansoffice


    b "Perhaps she enjoys entertaining people?"
    b "My niece seemed awfully captivated with her performance."

    scene 14evansoffice

    det "Or maybe she just likes to keep people guessing about the real story."
    det "It might be her way of throwing people off so they can't get a read on her."
    det "I really don't know, man."
    det "But you'd be amazed the lengths she'll go to just to make someone
        believe something absolutely absurd."

    scene 18evansoffice

    b "How does your partnership with her work though?"
    b "Is it even legal for her to assist you the way she does?"
    b "Is she a vigilante or something?"

    scene 19evansoffice

    det "She unquestionably shouldn't be pokin' in police business the way she does."
    det "And my theory is that she's got someone high up givin' her special treatment."
    det "You wouldn't believe the shit that girl gets away with."
    det "But don't repeat any of that."

    scene 14evansoffice with dissolve

    det "She's helped me put away a lot of bad people though."
    det "Penny even saved my life once."
    det "As curious and frustrated as I might be when it comes to her sometimes, I tend
        to let a lot slide because of that."

    scene 18evansoffice

    b "Detective Evans, I think I may have inadvertently gotten her into something
        she might not be able to handle."
    b "I'm worried that she stumbled onto a secret that might get her into a lot of trouble."
    b "And I came here today to give you a heads up about it."

    scene 19evansoffice

    det "[player_name], if you know about a crime that's been committed, you need to report it."
    det "But if you ain't gonna, hear me out on this."
    det "Penny goes after petty criminals and pedophiles and shit to keep herself busy."
    det "But honestly, she prefers bigger fish."
    det "She might get herself killed one day, for sure."
    det "But there's no stopping her once she's set her mind to somethin'."

    scene 16evansoffice

    b "You guys are partners though?"
    b "At least, sort of?"
    b "If I can't stop her, I'd like her to have every advantage."
    b "You'll help her, right?"

    scene 14evansoffice

    stop music fadeout 2.0

    det "Don't worry, [player_name]."
    det "I'll be there for her if she lets me."
    det "Now, I've got a lot to do today."
    det "Let me walk you out."

    if octavia == True:
        jump avalon_homealone

    else:
        jump dallas_holding

## Dallas being held at police station. ##

    label dallas_holding:

    scene 14evansoffice

    play sound "audio/dooropen.mp3"

    pause

    scene 22evansoffice with dissolve

    play sound "audio/doorclose.mp3"

    det "Hey, haven't you heard of knocking??"

    scene 21evansoffice with dissolve

    k "Flores just arrested the two guys he was looking into that own the cafe
        down off 11th."
    k "We've got them in holding right now."

    det "About time, he's been at that for months."
    det "What do you need from me?"

    scene 20evansoffice with dissolve

    k "They pulled in a girl that was getting ready for work."
    k "We're holding her for questioning but everyone else is preoccupied."
    k "Would you mind lending a hand on this one?"

    scene 23evansoffice with fade

    det "Yeah, I can help out."
    det "What did you say her name is?"

    k "She said her name is Dallas."

    scene 24evansoffice with dissolve

    b "Dallas?!"
    b "Dirty blonde, green eyes, freckles??"

    k "Yeah, that's her."

    scene 15evansoffice

    det "You know her?"

    b "Yes, she's a very good friend of my niece and I."
    b "I'd like to see her."

    det "Well, doesn't sound like she's being held for a crime."
    det "I can take you to her."

    scene 1dholding with fade

    pause

    play sound "audio/dooropen.mp3"

    pause

    scene 2dholding with dissolve

    d "Ugh!"
    d "Finally!"
    d "You just stuff people in here and leave 'em fo--"

    play sound "audio/doorclose.mp3"

    scene 3dholding

    d "[player_name]?!"
    d "Wow, I didn't expect to see you."
    d "What are you doing here?"

    b "I had a meeting here."
    b "I heard they were holding you."

    scene 4dholding

    d "Yeah, they threw me in here and left."
    d "I've been in here for almost half an hour."
    d "They could have given me a magazine or something, you know?"
    d "Jeez."

    scene 5dholding

    b "I'm glad you're alright."
    b "They didn't hurt you did they?"

    scene 6dholding

    d "No, I'm fine."
    d "They didn't hurt me."

    scene 7dholding with dissolve

    d "[player_name], what are you doing?"
    d "Don't get weird on me, alright?"
    d "Everything is fine."

    scene 8dholding with dissolve

    d "No no, come on!"
    d "Really, I'm fine!"
    d "You don't have to--"

    scene 9dholding with dissolve

    d "Aw, Christ."
    d "You don't have to go all drama queen on me, ya big lug."
    d "You're so emotional, are you sure you're not the girl here?"
    d "Although, if I'm being honest, it is nice you're here."

    scene 10dholding with dissolve

    d "This whole ordeal was pretty crazy."
    d "I mean, they were screaming at me so loudly."
    d "I didn't even do anything."
    d "But they just kept yelling at me."

    scene 11dholding with dissolve

    d "Then they started groping me."
    d "They said they were checking for weapons but I was practically naked already."
    d "Then they forced me into a police car..."
    d "They wouldn't even tell me what was going on."
    d "I was... I was really scared."

    scene 12dholding with dissolve

    d "Can you just hold me a little longer, [player_name]?"
    d "Please?"
    d "Please don't let go."

    b "I've got you, Dallas."
    b "Everything is going to be alright."
    b "I'm not going to let anything happen to you."

    bi "{i}I could feel her tears soaking through my shirt.{/i}"
    bi "{i}When I heard her muffled cries, I held her tighter.{/i}"
    bi "{i}Dallas was a tough girl and I deeply admired her for that.{/i}"
    bi "{i}But even the strongest branches snap if you apply enough pressure.{/i}"

    scene 13dholding with fade

    play music "audio/disturbed_mind.mp3"

    d "So I'm in the woman's restroom and I'm changing clothes for work, right?"
    d "All of a sudden, three police bust through the door with guns drawn and start yelling."
    d "'Freeze! Don't move!'"
    d "There I am, hands in the air, pants at my ankles, and I'm flashing my panties at all three of them."

    scene 23dholding

    b "God damn, Dallas!"
    b "That is just some bad luck with timing!"

    scene 16dholding

    d "I know, right?"
    d "They wouldn't let me pull my pants up, either."
    d "Bunch of pervs."

    scene 20dholding

    b "So what happened, Dallas?"
    b "Why were they after the owners of that cafe you work at?"

    scene 14dholding

    d "I don't know."
    d "To be honest, I noticed some shady things once in a while."
    d "But they paid well and they let me work the front however I wanted."
    d "It was the best job I ever had so I just didn't ask questions."

    scene 20dholding

    b "I understand."
    b "It doesn't look like you're going to have that job anymore though."
    b "Do you have some money in savings?"
    b "Are you going to be alright?"

    scene 42dholding

    d "I haven't thought ahead a whole lot yet."
    d "I have a little money saved up but not much."

    b "I hear being a stripper pays pretty well."

    scene 16dholding with dissolve

    d "Oh yeah?"
    d "Would you come put dollar bills in my panties?"

    scene 19dholding

    b "I'd put dollar bills in your mouth to keep those gums from flapping so much."

    scene 20dholding with dissolve

    b "On a serious note though, let's not worry about money until we get you out of here."
    b "Avalon and I can help you out if you need."

    scene 14dholding

    d "No, I'm not taking money from you."
    d "I don't need handouts."
    d "I can take care of myself."

    scene 20dholding

    b "It's not up for debate, Dallas."
    b "You're not going to live on the street."
    b "You're too important to Avalon and I for us to let that happen."
    b "It's not all about you, it's about us too."

    scene 16dholding

    d "You just like having me around because of my melons."
    d "Go ahead, you can touch them if you want."
    d "I don't mind."

    scene 19dholding

    b "Let's be honest, melons is a bit generous."
    b "I think a more comparable fruit would be oranges."

    scene 20dholding with dissolve

    b "Dallas, you can't keep tempting me like this."
    b "It would crush Avalon if you made a move on me."

    scene 15dholding

    d "I'm sorry, I just..."
    d "I guess I'm jealous."

    scene 16dholding with dissolve

    d "Remember when we were talking on the phone before we went out for burgers?"
    d "We were, you know, flirting and stuff."
    d "I was kind of excited to see where it was going to lead."

    scene 42dholding with dissolve

    d "The very next day, you were with Avalon."
    d "I really felt like we had something and now we don't get to explore that."
    d "It really sucks, man."

    scene 20dholding

    b "We don't get to explore every path presented to us in life, Dallas."
    b "Each choice we don't make is a choice lost forever."
    b "I desperately wish I could try both paths, one with you and one with her."
    b "But it just doesn't work like that."

    scene 42dholding

    d "Do you think you could have loved me as much as you love her?"
    d "If, you know, you made a different choice."

    scene 21dholding

    b "You're a very different person, Dallas."
    b "I love you differently than I love her."
    b "She is a very gentle and sweet person."
    b "You're more outgoing and aggressively playful."
    b "Both of you are wonderful in your own ways."

    scene 16dholding

    d "Wait, you just said you love me."
    d "You totally want to make out with me right now, don't you?"

    scene 19dholding

    b "No way."
    b "I don't make out with criminals."
    b "It was part of my new years resolution back in two thousand sixteen."

    scene 20dholding with dissolve

    b "But yeah, of course I love you."
    b "Just because we don't bump uglies doesn't mean I can't care about you."
    b "Our relationship is platonic but I still want you to be a big part of my life."

    scene 13dholding

    d "Yeah, I want that too."
    d "If you really think about it though, you're kind of old."
    d "And you come bail me out of jail, comfort me when I'm sad and give me little
        life lessons once in a while."

    scene 16dholding with dissolve

    d "Without the sex, I mean, it's kind of like you're my dad."
    d "Should I start calling you 'Daddy'?"

    stop music fadeout 2.0

    b "Is it weird that I'm actually turned on by that?"

    play sound "audio/dooropen.mp3"

    pause

    scene 24dholding with dissolve

    d "Ngh..!"

    b "Dallas, look at me."

    play sound "audio/doorclose.mp3"

    scene 25dholding with dissolve

    b "Don't worry, everything is going to be fine."
    b "I'm not going to let anything happen."

    scene 26dholding

    pause

    scene 28dholding with dissolve

    b "I promise."
    b "I'm right here with you."

    scene 27dholding

    pause

    scene 29dholding with dissolve

    d "Thanks, [player_name]."
    d "It really means a lot to me that you're here."

    scene 30dholding

    det "Dallas, right?"
    det "I'm Detective Evans, it's nice to meet you."

    scene 32dholding with dissolve

    det "Listen, I'm going to keep this as informal as possible."
    det "You can even stay seated on the desk if you prefer."
    det "We don't suspect you were involved with any of the illegal operations
        going on at that cafe."
    det "But if you know anything, it might be helpful when we bring a case against
        the owners of that establishment."

    scene 31dholding

    d "I really don't know anything."
    d "They kept me out of that side of it."
    d "I just worked the front."

    scene 32dholding

    det "Are you sure you never saw anything?"
    det "Anything at all could be helpful."

    scene 33dholding

    d "I opened a box of coffee once and they yelled at me."
    d "I thought I saw something under the coffee but I can't really be sure."

    scene 34dholding

    det "Can you describe what it was?"
    det "Was it square-shaped, wrapped in anything?"
    det "Can you tell me what color it was?"
    det "Anything at all?"

    scene 31dholding

    d "I really don't remember, it was months ago."
    d "I just saw a shimmer, like a fleck of light reflecting off it."
    d "Am I... am I in trouble?"

    scene 32dholding

    det "No, you're not in any trouble."
    det "That's not really enough to go on but it shouldn't matter."
    det "We've got plenty on these guys."
    det "Sorry to have put you through this, Miss Dallas."

    scene 35dholding

    b "Detective Evans here also has a friend that likes to torment him sometimes."
    b "She's about the size of a garden gnome and still gets one up on him."

    d "Really?"

    scene 36dholding

    det "I ain't proud to say it but, it's true."
    det "The first time I walked into my new office, I fell right to the floor."
    det "Turns out she thinks I should be on my game all the time now since I made Detective,"
    det "so she put a tripwire in front of the door."
    det "As training, you see."

    scene 37dholding

    d "Couple years ago, I put cayenne pepper in [player_name]'s face wash."
    d "He couldn't see for nearly half an hour."

    scene 40dholding

    det "Bro, we gotta get better friends."

    b "You're telling me."
    b "She laughed at me for the entire half-hour that I was blind."

    scene 32dholding with dissolve

    det "Miss Dallas, you're free to go."
    det "I'm going to give you my number though."
    det "If you think of anything, please call me."

    scene 39dholding

    b "Detective, I really appreciate you treating us right."
    b "Can I buy you a beer sometime as a thank you?"

    scene 40dholding

    det "I've been meaning to celebrate my promotion anyway."
    det "A beer sounds great."
    det "You've got my number."
    det "Let me walk you folks out."

    jump avalon_homealone

## Avalon at home alone. ##

    label avalon_homealone:

    play music "audio/one_step_closer.mp3"

    scene 1ahomealone with fade

    ai3 "{i}I've applied the second coat of dye and now it's time to see how it looks.{/i}"
    ai3 "{i}Please don't look stupid, please don't look stupid...{/i}"

    scene 2ahomealone with dissolve

    ai3 "{i}Hmm.{/i}"
    ai3 "{i}It's... sort of red a little bit.{/i}"
    ai3 "{i}But it looks nice!{/i}"
    ai3 "{i}It almost matches Uncle [player_name]'s hair.{/i}"

    scene 3ahomealone with dissolve

    a3 "Who's that bodacious babe in the mirror??"
    a3 "Oh, it's just me and my sexy new hairdo."
    a3 "If I was a dude, I'd totally hit on this hotness!"
    a3 "I'd be like,"
    a3 "'Hey girl, you know what has two thumbs and totally wants to, you know, make out with you right now??'"

    scene 4ahomealone with dissolve

    a3 "'This guy!'"
    a3 "'Cause of the thumbs and the wantin' to make out and stuff.'"
    a3 "'Yeah, girl.'"

    scene 5ahomealone with dissolve

    ai3 "{i}Ugh!{/i}"
    ai3 "{i}I'd make a terrible guy.{/i}"
    ai3 "{i}I'm pretty sure I just sexually harrassed myself.{/i}"

    scene 6ahomealone with dissolve

    ai3 "{i}But that's alright!{/i}"
    ai3 "{i}Who needs charisma when you've got sweater stretchers to do the talking for you??{/i}"
    ai3 "{i}Go forth, my twins!{/i}"
    ai3 "{i}Work your magic!{/i}"

    scene 7ahomealone with dissolve

    ai3 "{i}Yes!{/i}"
    ai3 "{i}A little bit of skin goes a long way.{/i}"
    ai3 "{i}Not too much though.{/i}"
    ai3 "{i}These puppies are off the market now!{/i}"

    scene 8ahomealone with dissolve

    ai3 "{i}Eat your heart out, Uncle.{/i}"
    ai3 "{i}I'm back to my old self and ready to start a new life.{/i}"
    ai3 "{i}The world is my oyster.{/i}"

    "*Ring* *Ring*"

    scene 9ahomealone with dissolve

    ai3 "{i}Hm?{/i}"
    ai3 "{i}Is that my phone?{/i}"

    scene 10ahomealone with fade

    ai3 "{i}Oh, I must have left my phone in here on accident.{/i}"
    ai3 "{i}Let's see who it is.{/i}"

    if octavia == True:
        jump avalon_homealone_octavia

    else:
        jump avalon_homealone_dallas

    label avalon_homealone_octavia:

    scene 11ahomealone

    ai3 "{i}Oh, it's Octavia!{/i}"
    ai3 "{i}I wonder how she's doing today?{/i}"

    scene 13ahomealone

    a3 "Hey, Octavia!"
    a3 "How are you today?"

    o "Good morning, Avalon."
    o "I'm doing very well."
    o "How are you?"

    a3 "I'm great!"
    a3 "I feel like I could take on the world today!"

    o "Wow, that's so fantastic!"
    o "I'm really happy to hear that!"
    o "Is [player_name] there?"
    o "I wanted to invite you both over to meet my cat."

    scene 14ahomealone with dissolve

    a3 "Your... cat?"
    a3 "I didn't know you had a cat."

    o "I do!"
    o "She's been rather lonely lately."
    o "So I thought I'd introduce her to some new people!"

    scene 15ahomealone with dissolve

    a3 "[player_name] had a meeting this morning."
    a3 "He texted me that he's going to the gym afterward for a little while."
    a3 "But I'd love to meet your cat!"

    o "Great!"
    o "I'll come pick you up."

    scene 16ahomealone with dissolve

    a3 "Okay!"
    a3 "I'll see you soon!"

    o "Bye for now!"

    scene 17ahomealone with dissolve

    stop music fadeout 2.0

    ai3 "{i}Guess I'll finish this movie while I wait.{/i}"
    ai3 "{i}It's a classic!{/i}"
    ai3 "{i}I've always wondered though...{/i}"
    ai3 "{i}I mean, gloves with knives on them seem pretty cool.{/i}"
    ai3 "{i}But what if you forget to take them off before using the bathroom?{/i}"
    ai3 "{i}He might accidentally turn himself into a girl!{/i}"
    ai3 "{i}Yep, cutting off your penis with knife-hands would be the real nightmare.{/i}"

    play sound "audio/doorbell.mp3"

    scene 18ahomealone with dissolve

    ai3 "{i}That must be her!{/i}"
    ai3 "{i}I'm actually really curious to see what her home looks like.{/i}"

    scene 19ahomealone

    a3 "Uhh... Octavia?"

    o "It's me!"

    a3 "Okay, just making sure!"

    scene 20ahomealone with dissolve

    a3 "Hey, Octavia!"
    a3 "Wow, you look so pretty today!"

    o "You too!"
    o "Did you do something with your hair?"

    a3 "I changed it closer to my original color."

    scene 21ahomealone with dissolve

    o "It looks lovely."
    o "Are you ready to go?"

    a3 "Yep!"

    ## Octavia House with Maize ##

    scene 2ohouse_mb with fade

    play music "audio/tomorrows_rain.mp3"

    o "Welcome to where I rest my head!"
    o "It's not very big but it's all I've come to need."
    o "Come on in!"

    scene 1ohouse_mb

    a3 "Thank you."
    a3 "I can't believe the security downstairs."
    a3 "I guess you don't have much risk of getting robbed."

    scene 3ohouse_mb with dissolve

    a3 "Wow!"
    a3 "That view is awe-inspiring, Octavia!"
    a3 "How can you afford to be right on the water like this??"

    scene 4ohouse_mb

    o "Oh, it's not too expensive."
    o "I find the water calming so I always try to live as close to a river or
        lake as possible."
    o "Sometimes I look at the buildings across the street and it reminds me
        of what we can do when we all work together, you know?"
    o "All the lights, the structures, the boats."
    o "They wouldn't be possible if we didn't come together as a collective and
        help each other."

    scene 3ohouse_mb

    a3 "I... guess I don't really think about it that much."
    a3 "I like the way you look at the world though."
    a3 "I try to be positive too but it's hard sometimes."

    o "I didn't mean to get too deep on you there."
    o "Let me show you the kitchen!"

    scene 5ohouse_mb

    o "It's simple but that's actually what I like about it!"

    a3 "There's... no refrigerator?"

    o "Nope!"
    o "I have my food prepared and brought to me."
    o "I seldom cook my own meals."
    o "But I keep fruit around for snacks."

    a3 "Octavia, you're... weird."

    o "Yep!"

    scene 6ohouse_mb with dissolve

    o "And if you thought the kitchen was weird, this is my bedroom."

    a3 "It's just a bed and glass walls?"

    o "Mhmm!"
    o "It comforts me knowing I can see my entire home while I'm in bed."

    a3 "What about upstairs?"

    o "Oh, remember my cat that I mentioned?"
    o "That's her area."
    o "She keeps an eye on things up there."
    o "She's probably just waking up."

    scene 7ohouse_mb with dissolve

    o "What do you think of the bedroom?"
    o "Do you like it?"

    a3 "W-what's that?"
    a3 "It looks like..."

    scene 9ohouse_mb

    a3 "Is that a gun?"

    o "Oh, yes."
    o "I always keep a firearm close when I sleep."

    a3 "Why..?"

    scene 8ohouse_mb

    o "Habit, I suppose."
    o "I went into the military at a young age."
    o "So I learned to operate a firearm early on."
    o "If it bothers you, I can put it away?"

    a3 "N-no, it's fine."

    scene 10ohouse_mb with dissolve

    a3 "Honestly, I haven't been around guns much at all."

    o "I'd be happy to teach you if you'd like?"
    o "Having it close is peace of mind."

    a3 "You know, yeah, maybe that would be a good idea."

    scene 11ohouse_mb with dissolve

    a3 "I could certainly do with--"

    scene 12ohouse_mb with dissolve

    pause (.3)

    scene 13ohouse_mb with dissolve

    pause (.3)

    scene 14ohouse_mb with dissolve

    a3 "Ahh!"
    a3 "Octavia, help!"
    a3 "It wants to eat me!"

    scene 15ohouse_mb

    o "Maize!"
    o "I brought her over to visit you."
    o "She's not going to want to be your friend if you scare her!"

    scene 16ohouse_mb with dissolve

    o "Why are you hiding behind me?"
    o "Are you using me as a human shield?"

    a3 "You brought me here!"
    a3 "It's only right she eats you first!"

    o "Oh she won't eat us."

    scene 17ohouse_mb with dissolve

    o "Hi, Maize!"
    o "Did you miss me?"
    o "I bet you didn't even notice I was gone, lazy girl."

    scene 18ohouse_mb with dissolve

    o "This is Avalon."
    o "She's a friend of mine."
    o "Go ahead, Avalon."
    o "Say 'Hello'."

    scene 19ohouse_mb with dissolve

    a3 "Uhm..."
    a3 "Hello, Maize."

    o "She loves being pet on the head."

    a3 "Aren't panthers feral?"
    a3 "How is she so docile?"

    scene 20ohouse_mb with dissolve

    o "Maize is a special feline."
    o "She was found by a farmer and his wife several years ago in their cornfield."

    a3 "Oh, that must be where her name comes from?"

    o "That's right!"
    o "Her mother abandoned her probably due to a shortage of food."

    scene 21ohouse_mb with dissolve

    a3 "... Wow!"
    a3 "She's... she's so soft."

    o "Yeah, I have several professionals look after her."
    o "They come over during the day to feed her, give her baths, take her out to
        run and play."

    a3 "But how is she like this?"
    a3 "She's domesticated."

    o "Well, that's a bit of a story."
    o "Join me on the couch?"

    a3 "Okay."

    scene 22ohouse_mb with dissolve

    a3 "Wow, she's so big."

    o "About one hundred and sixty pounds, actually."

    a3 "Amazing..."

    scene 23ohouse_mb with dissolve

    pause (.3)

    scene 24ohouse_mb with dissolve

    a3 "Woah!"
    a3 "You let her on the couch??"

    o "Oh yes, that's why I have such a large couch."
    o "It's more for her than it is for me."

    scene 25ohouse_mb with dissolve

    o "I've let her lounge about for too long."
    o "She's really just a fat and lazy house cat now."

    a3 "She really just comes and hangs out, huh?"
    a3 "That's so neat!"

    scene 26ohouse_mb

    o "Avalon, may I ask..?"
    o "Did [player_name] hire Penny to investigate the man that hurt you?"
    o "I believe she's got a silly catchphrase that she uses as a name for her business?"
    o "'Penny for Your Thoughts'?"

    scene 27ohouse_mb with dissolve

    a3 "Oh, uhh, yeah."
    a3 "I actually met her last night."
    a3 "She's a bit of a wild card."
    a3 "Do you know her?"

    scene 30ohouse_mb

    o "I used to."
    o "We had a bit of a falling out some time ago."
    o "She simply wanted a lifestyle I wasn't interested in."
    o "Is she doing well?"

    scene 31ohouse_mb

    a3 "As far as I could tell, yes."
    a3 "But I only spent a few minutes with her."

    scene 29ohouse_mb with dissolve

    a3 "She told a rather exciting story."
    a3 "And she insisted it was all true but I could tell she was exaggerating."
    a3 "Has she always been a bit of a bard?"

    scene 34ohouse_mb

    o "Yes."
    o "She likes to see how gullible people are."
    o "I must admit, it may be a bit of my own fault she's like that."

    scene 28ohouse_mb with dissolve

    o "I used to regale her with stories of my own life."
    o "She was often absolutely captivated with them."
    o "I think she wanted her life to be just as exciting."

    scene 35ohouse_mb

    a3 "Oooh, the mysterious Octavia shows her hand a little."
    a3 "So you {b}are{/b} a super spy!"

    scene 34ohouse_mb

    o "Nothing like that, I'm afraid."
    o "Silly goose."

    scene 28ohouse_mb with dissolve

    o "But when I was in the Air Force, I did have some interesting experiences."
    o "I really wanted to settle down though and try a simpler life."
    o "That's why I moved out here!"

    scene 29ohouse_mb

    a3 "Well, I'll try not to pry too much but you've got to tell me more about Maize."
    a3 "I'm dying of curiosity!"
    a3 "What happened after the farmer found her?"
    a3 "How did she end up here, with you?"

    scene 28ohouse_mb

    o "Well, the farmer actually turned her over to a small research company."
    o "I wasn't privileged with much detail but I think they ran experiments on her."
    o "Their operations weren't legal, however, so they were shut down."
    o "When they couldn't find a zoo willing to take her, she was going to be euthanized."
    o "When a friend asked me to see what I could do to keep her from being destroyed,
        I went and visited Maize."
    o "And then, well, it's hard to explain but Maize and I just had a connection."
    o "So I pulled some strings and had her come live with me."

    scene 29ohouse_mb

    a3 "I don't know what kind of 'strings' you have to pull to legally own a panther but
        I'm sure glad you made it happen."
    a3 "She seems like a very sweet and friendly companion."

    scene 31ohouse_mb with dissolve

    a3 "Octavia, I hate to switch subjects so quickly but can I ask you a question?"

    o "Of course."

    a3 "Do you..?"
    a3 "Do you like sex?"

    scene 28ohouse_mb

    o "It's perhaps my favorite past time!"
    o "Although, admittedly, I've had more experience with those of my own gender."
    o "It's not that I'm opposed to male partners."
    o "I simply haven't met many I'd be willing to go to bed with, I suppose."

    scene 33ohouse_mb

    a3 "I-I didn't expect you--"
    a3 "I mean, not to say I thought you were... prudish."
    a3 "But all that was--"

    scene 28ohouse_mb

    o "Surprising?"
    o "I try to be more conservative in conversation when it comes to sex."
    o "Why do you ask though?"
    o "Is it about [player_name]?"

    scene 31ohouse_mb

    a3 "Yeah, well, it's kind of hard to explain."
    a3 "I want to have fun, you know, in that way..."
    a3 "But when we reach a certain point while we're fooling around, I just get freaked out and scared."
    a3 "And then I feel so stupid for feeling that way."

    scene 30ohouse_mb

    o "Avalon, have you had sex before that man hurt you?"

    a3 "I used to fool around a little with my girlfriend but never with a boy."

    o "When you got into a relationship with [player_name], I noticed you appeared to recover very quickly
        from your ordeal."
    o "But I suspected there was probably still some residual damage lingering beneath the surface."
    o "You might be subconsciously linking your experiences with [player_name] to that terrible event."

    scene 31ohouse_mb

    a3 "I don't want to live my life like that."
    a3 "Dreaming about it, having it haunt my subconscious, always bringing me down..."
    a3 "I've tried to push past it and leave it behind but--"

    scene 30ohouse_mb

    o "It takes time."
    o "And I'll help you, Avalon."
    o "I promise."
    o "We'll get there."

    scene 29ohouse_mb

    a3 "Thank you, Octavia."
    a3 "You're pretty great, you know that?"

    if monogamy == True:
        jump octavia_deny

    else:
        jump octavia_request

    ## Octavia Request if one Polygamy Path ##

    label octavia_request:

    scene 30ohouse_mb

    o "Avalon, I want to ask you something."
    o "And this is partially selfish on my part."
    o "So I want you to take that into consideration when you answer."
    o "[player_name] said he doesn't mind if you have sexual relations with women."
    o "Would you be willing to entertain that idea with me?"

    scene 33ohouse_mb

    a3 "That was... forward!"
    a3 "Uhm, wow, I..."
    a3 "I am more comfortable with the idea of a woman..."
    a3 "At least right now."

    scene 29ohouse_mb with dissolve

    a3 "I mean, yeah, I think that would be interesting."
    a3 "I've got butterflies in my stomach."
    a3 "That really surprised me!"

    scene 28ohouse_mb

    o "I don't mean to make you uncomfortable but I am attracted to you."
    o "So I felt like it couldn't hurt to ask."
    o "And I think I could better aid in helping you form more positive feelings
        towards sex if I showed you how fun it can be."
    o "But we'll take it slow, of course!"

    scene 31ohouse_mb

    a3 "Should I tell [player_name] about this?"
    a3 "I don't want to keep anything from him."

    scene 30ohouse_mb

    o "Avalon, it's imperative that you tell [player_name]."
    o "Your relationship will collapse under the weight of lies and deception."
    o "So keep everything out in the open."
    o "If he doesn't like the idea of us having a fling, then we won't."
    o "And I hold firm on that."

    scene 34ohouse_mb with dissolve

    o "But I'm sure he'll be fine with it."
    o "He keeps it buried beneath the surface pretty well but underneath,"
    o "he's a big ol' perv."

    scene 35ohouse_mb

    a3 "Trust me, I know."
    a3 "He compared his penis to a giant shark last night."
    a3 "After ogling my boobs but just before grabbing a handful of them."

    scene 28ohouse_mb

    o "Well it does sound like you two are having fun!"
    o "Just remember to pace yourself, don't go beyond the point you're comfortable."
    o "Actually, [player_name] might be home soon."
    o "Would you like to head back?"

    scene 36ohouse_mb

    a3 "Yeah, that sounds good."
    a3 "I'm going to miss you, Maize!"
    a3 "But I'll be back to visit."
    a3 "Promise!"

    stop music fadeout 2.0

    jump penny_vs_faith

    ## Octavia denied due to Monogamy path ##

    label octavia_deny:

    scene 30ohouse_mb

    o "Avalon, would you tell me about the last time you were being intimate and
        became uncomfortable?"
    o "Perhaps I can give you some advice?"

    scene 31ohouse_mb

    a3 "It was this morning."
    a3 "I was actually trying to get him worked up."
    a3 "You know, because... I wanted to play."

    scene 35ohouse_mb with dissolve

    a3 "I was doing the old 'Oh, I've been so naughty, punish me' routine."
    a3 "I saw it in a dirty video one time and it really excited me."

    scene 31ohouse_mb with dissolve

    a3 "But he was kind of assertive and a little aggressive."
    a3 "It's weird because I thought it was really sexy,"
    a3 "but then I just got really uncomfortable all of the sudden."

    scene 28ohouse_mb

    o "Take breaks!"
    o "The next time you begin to become uncomfortable, tell [player_name] to step away for
        a moment."
    o "And then, after you take a few breaths and compose yourself, see how you feel."
    o "Ask him to continue if you'd like or tell him that's enough for today."

    scene 31ohouse_mb

    a3 "But..."
    a3 "What if he doesn't stop?"
    a3 "What if he keeps going even if I tell him not to?"

    scene 30ohouse_mb

    o "Did you ask him to stop today?"

    a3 "Yes."

    o "And did he?"

    a3 "Well, yeah..."

    o "Avalon, [player_name] cares about you very much."
    o "He's not going to do anything you don't want him to do."
    o "Trust me, I've seen--"
    o "I mean, I just know."

    scene 29ohouse_mb

    a3 "Yeah, I know he loves me."
    a3 "And I know you're right."
    a3 "Maybe I just needed to hear it out loud."

    scene 28ohouse_mb

    o "You know, he might be home by now?"
    o "Would you like to head back?"

    scene 36ohouse_mb

    a3 "Yeah, that sounds good."
    a3 "It was nice to meet you, Maize!"
    a3 "I'll miss you!"

    stop music fadeout 2.0

    jump penny_vs_faith

    ## Avalon Home Alone, Dallas Path ##

    label avalon_homealone_dallas:

    scene 12ahomealone

    ai3 "{i}Oh, it's Dallas!{/i}"
    ai3 "{i}That's weird.{/i}"
    ai3 "{i}I thought she worked today.{/i}"

    scene 13ahomealone

    a3 "Hey, Dallas!"
    a3 "Are you playing hooky today?"

    d "Nah, girl, I went to work today."
    d "But then I got pinched."

    scene 14ahomealone with dissolve

    a3 "Pinched?"
    a3 "Like, by a crab?"
    a3 "That must have been painful."
    a3 "Wait, where did you find a crab??"

    d "No, dummy, I mean I got arrested."

    scene 15ahomealone with dissolve

    a3 "Well, flashing your tatas at people in public places is illegal."
    a3 "I always knew you'd get caught eventually."
    a3 "I guess your exhibitionist days are through, huh?"
    a3 "How long did they give you?"
    a3 "Ten to twenty?"

    d "I didn't get thrown in the pen for flashing my tits!"

    scene 14ahomealone with dissolve

    a3 "Wait, are you being serious right now?"
    a3 "Did you really get arrested?"
    a3 "Dallas, are you alright?"

    d "Yeah, I'm fine."
    d "[player_name] was there to rescue me."
    d "Can you believe it?"

    scene 15ahomealone with dissolve

    a3 "Oh right, Uncle [player_name] was having a meeting at the station."
    a3 "Wow, that's a lucky coincidence."

    d "Isn't it?"
    d "We're going to come pick you up and head to my place."

    scene 16ahomealone with dissolve

    a3 "Alright."
    a3 "See you soon then!"

    scene 17ahomealone with fade

    stop music fadeout 2.0

    ai3 "{i}I guess I'll finish this movie while I wait.{/i}"
    ai3 "{i}You know, it must be pretty cool to be a teleporting, immortal, machete-wielding
        zombie.{/i}"
    ai3 "{i}But is it worth it if you have to have a messed up mug like that?{/i}"
    ai3 "{i}I mean, that is a face for radio!{/i}"
    ai3 "{i}At least he can cover it up with that hockey mask, I guess.{/i}"

    play sound "audio/doorbell.mp3"

    scene 18ahomealone with dissolve

    ai3 "{i}That must be Dallas and Uncle [player_name]!{/i}"
    ai3 "{i}The more I think about it...{/i}"
    ai3 "{i}Getting arrested must have been pretty intense.{/i}"
    ai3 "{i}I hope she's okay.{/i}"

    scene 19ahomealone with fadefast

    a3 "Umm... who's there?"

    d "It's me, girl!"
    d "Open up."

    a3 "Oh, alright. I was just making sure."

    scene 20ahomealone with dissolve

    a3 "Hey, Dallas!"

    d "Ooh, going for a new look huh?"
    d "I can dig it."
    d "Come on, [player_name] is in the car."

    a3 "Thanks, Dallas!"

    scene 21ahomealone with dissolve

    a3 "That shirt is a little tight, isn't it?"

    d "That's not the only thing tight on this bod, girl!"

    a3 "Ugh."

    ## Dallas' House! ##

    scene 1dallashouse with fade

    d "This cost me a small fortune."
    d "I got it a few months ago for a steal!"
    d "It's three times the size of my last home."
    d "Can you believe it??"

    b "Well let's see it, Dallas."
    b "Don't hold us in suspense here."

    scene 2dallashouse with dissolve

    d "Tada!"
    d "It's got {b}two{/b} bedrooms and a spacious living area."
    d "This kitchen can seat four people, [player_name]."
    d "{b}Four{/b}."

    b "Damn, Dallas."
    b "This is top shelf."

    scene 3dallashouse with dissolve

    b "Do you have a roommate?"

    d "Nope!"
    d "It's just me."

    b "Not many people your age own their own home, Dallas."
    b "This is very impressive."
    b "I'm so proud of you."

    scene 4dallashouse with dissolve

    d "I--"
    d "What?"

    b "I mean, you worked hard for this."
    b "You're making it."
    b "A lot of people don't."
    b "So, I'm really proud of you."

    d "T-thank you."
    d "Uhh, [player_name]?"

    scene 5dallashouse with dissolve

    b "Yeah?"

    d "I think you should go."

    b "What?"
    b "Did I say something wrong?"

    d "No."
    d "I just... want to be with Avalon alone right now."

    scene 6dallashouse with dissolve

    a3 "Out, Uncle!"
    a3 "Out, out!"
    a3 "We need girl time!"

    b "What the hell??"
    b "Stop pushing me."

    a3 "Go to the gym."

    scene 7dallashouse with dissolve

    b "Okay, Okay."
    b "Call me when you're ready to go, alright?"
    b "And... tell Dallas I'm sor--"

    scene 8dallashouse

    play sound "audio/doorclose.mp3"

    b "Bye, Beautiful!"

    a3 "Bye, Uncle."

    d "Sorry, Avalon."
    d "I'm just having a weird day, you know?"
    d "I lost my job."
    d "I got arrested."
    d "And [player_name]..."

    scene 9dallashouse with dissolve

    a3 "Come on."
    a3 "Let's go talk it out."

    d "Thanks, Avalon."
    d "I'm bein' kind of a pain in the ass today, huh?"

    a3 "We all have bad days, Dallas."
    a3 "Even you."

    scene 10dallashouse with fadefast

    b "I must have said something to upset her."
    b "I'm sure she'll be fine but I hate not being able to help."
    b "Avalon's right though."
    b "They need some time with each other."
    b "I wonder why she stopped me from apologizing..?"

    scene 13dallashouse with fadefast

    play music "audio/disturbed_mind.mp3"

    d "And then they stuck me in a freezing cold interrogation room for half an hour."
    d "I was fine, too!"
    d "I was ready to handle whatever police bullshit that I had comin'."
    d "But then, [player_name] came in and..."
    d "I dunno, he just completely disarmed me."
    d "All the fear and anxiety I was pushing down rose right to the surface."
    d "I couldn't keep it together after that."
    d "Does that... does that make sense?"

    scene 12dallashouse

    a3 "Yeah, I know what you mean."
    a3 "Those times when you have to put on a brave face."
    a3 "And when you don't have to wear that mask anymore, you kind of break down."
    a3 "I've been there."

    scene 13dallashouse

    d "But I'm out of work now."
    d "And I don't think I'm going to find something that pays well enough for me
        to keep this place..."

    a3 "I have some money..."

    d "I'm not taking handouts."

    scene 16dallashouse

    a3 "I'm not offering a handout!"
    a3 "Maybe I'm looking to invest."

    scene 12dallashouse with dissolve

    a3 "Seriously."
    a3 "What if we started something of our own?"

    scene 11dallashouse

    d "Is that... something we could do?"
    d "Are you sure you'd want to?"

    a3 "Uhh, yeah!"

    scene 17dallashouse with dissolve

    d "Hey, maybe we could buy the cafe!"
    d "Those dipshits I worked for had it seized."
    d "The government has to sell it now or something, right?"

    scene 16dallashouse

    a3 "I have no idea how all that works."
    a3 "But hell yeah!"
    a3 "If you find out what it's going for, let me know!"

    scene 12dallashouse with dissolve

    a3 "Even if we don't get that though, we can still start something else."
    a3 "It would be pretty cool to own our own business, I think."
    a3 "It's worth a shot!"

    scene 15dallashouse

    d "Thanks, Avalon."
    d "You're good people."
    d "I'm feeling a bit better now."
    d "How are things going with you and [player_name]?"

    if monogamy == True:
        jump dallashouse_mono
    else:
        jump dallashouse_poly

    ## Dallas House, Monogamy Path ##

    label dallashouse_mono:

    scene 12dallashouse

    a3 "Actually, I wanted to talk to you about that."
    a3 "Maybe you've got some advice."
    a3 "Remember that porno we watched together?"
    a3 "The girl was telling that guy how naughty she'd been and that she needed to be punished."

    scene 17dallashouse

    d "Oh yeah!"
    d "I remember that!"
    d "Your mom was so pissed when she found that videotape under your bed."
    d "I thought she was gonna kill you."

    scene 16dallashouse

    a3 "Which was dumb!"
    a3 "I got it from her room!"

    scene 12dallashouse with dissolve

    a3 "Anyway, I started kind of reenacting that."
    a3 "With [player_name]..."

    scene 17dallashouse

    d "Oh shit!"
    d "Tell me everything!"
    d "Wait, let me take my pants off first."

    scene 16dallashouse

    a3 "Stop!"
    a3 "I'm being serious!"
    a3 "I got... kind of scared."
    a3 "In the middle of us fooling around, I just started feeling really uncomfortable."

    scene 13dallashouse

    d "Babe, I know you're eager to experience everything with him."
    d "You've got that new relationship high right now and it has your trauma
        repressed."
    d "But that shit isn't gone."

    scene 18dallashouse

    a3 "I-"
    a3 "I know."
    a3 "But..."
    a3 "Dallas, I don't want to be like this anymore."
    a3 "I want to move on and enjoy my life."
    a3 "I don't want one stupid event to ruin everything..."

    scene 15dallashouse

    d "I know, Avalon."
    d "It'll get better with time."
    d "But for now, try to take breaks when you're with [player_name]."
    d "If you start feeling uncomfortable, tell him to fuck off for a minute."
    d "Take a breath and compose yourself."
    d "Then you can keep going or stop for the day."

    scene 12dallashouse

    a3 "I guess I can try that."
    a3 "It sounds like you know what you're talking about."
    a3 "How do you know this stuff?"

    scene 15dallashouse

    d "I'm just regurgitating what a counselor told me."
    d "You know, I'm actually kind of jealous of your relationship..."
    d "You wouldn't happen to be willing to share him sometime, would you?"

    scene 14dallashouse

    a3 "Nope."

    scene 12dallashouse with dissolve

    a3 "I know you kind of have a thing for him."
    a3 "I'm sorry that I stole him away."
    a3 "But you're going to find someone, I promise!"
    a3 "Please don't hate me."

    scene 15dallashouse

    d "You know I don't."
    d "You guys are perfect together."
    d "And you're right, I'll be fine."
    d "No harm in asking though, right?"

    scene 12dallashouse

    stop music fadeout 2.0

    a3 "Actually, we should probably talk to him."
    a3 "I feel bad for kicking him out."
    a3 "Let's give him a call and we'll head back to his place."

    jump penny_vs_faith

    ## Dallas House, Polygamy Path ##

label dallashouse_poly:
    if _in_replay:
        $ player_name = renpy.input("What would you like to name the MC?")
        if player_name.strip() == "":
          $ player_name = "Byron"

    scene 14dallashouse

    a3 "You're crushing on him, aren't you?"
    a3 "I saw you trying to force him to grope you yesterday."
    a3 "'Oh [player_name], feel my chest, my heart is beating so fast.'"

    scene 11dallashouse

    d "Shit."
    d "I shouldn't have done that."
    d "Seeing you two together..."
    d "I'm jealous, you know?"

    scene 12dallashouse

    a3 "Yeah, I know you've always had a thing for him."
    a3 "I was thinking about that earlier."
    a3 "I got a little scared while [player_name] and I were fooling around."
    a3 "And I started thinking about you."

    scene 15dallashouse

    d "You were with [player_name] but you were thinking about me?"
    d "Damn, girl, sounds like we're both doin' wrong."
    d "It's getting my juices flowing a little bit thinking about it."

    scene 16dallashouse

    a3 "No, you slut, just listen."

    scene 12dallashouse with dissolve

    a3 "When we were being intimate, I wished you were there to point me in the right direction."
    a3 "And to help me calm down."
    a3 "But it's also more than that..."

    scene 20dallashouse with dissolve

    a3 "When you were flirting with [player_name], I didn't really mind."
    a3 "You're my best friend and I want you to have everything you want."
    a3 "And I want you to be a part of my life."
    a3 "I want you to be a part of... our life."
    a3 "I love you, Dallas."

    stop music fadeout 2.0

    d "R-really?"
    d "I mean, I love you too."
    d "But I--"

    scene 21dallashouse with dissolve

    play music "audio/cause.mp3"

    d "Mm!"

    ai3 "{i}Her lips are tender and warm.{/i}"
    ai3 "{i}I could feel the tension in them.{/i}"
    ai3 "{i}I really surprised her with this kiss.{/i}"

    scene 22dallashouse with dissolve

    ai3 "{i}Her breasts are firm and soft at the same time.{/i}"
    ai3 "{i}And her whole body was that way.{/i}"
    ai3 "{i}She always worked out twice as hard as the other girls in gym.{/i}"
    ai3 "{i}Her body was like a machine in that way.{/i}"
    ai3 "{i}But despite her toned body, her skin is always so smooth.{/i}"

    scene 23dallashouse with dissolve

    ai3 "{i}She wouldn't mind if I went further, would she?{/i}"
    ai3 "{i}Dallas loves showing off her breasts.{/i}"
    ai3 "{i}She certainly wouldn't mind showing them to me.{/i}"
    ai3 "{i}Right?{/i}"

    scene 24dallashouse with dissolve

    d "Mmfh!"

    scene 25dallashouse with dissolve

    ai3 "{i}It's so squishy.{/i}"
    ai3 "{i}And her nipple is getting hard.{/i}"

    scene 26dallashouse with dissolve

    d "God damn, Avalon."
    d "What has gotten into you??"
    d "Not that I'm complaining!"

    scene 27dallashouse

    a3 "I don't know."
    a3 "When we were fooling around yesterday, it reminded me how fun it is."
    a3 "And I want that again."

    scene 30dallashouse

    d "Yeah, that was great."
    d "Until you passed out!"
    d "What the hell was that, by the way?"

    scene 29dallashouse

    a3 "I fall asleep sometimes after I orgasm."
    a3 "Especially if they're really intense."

    d "That's fuckin' weird, Avalon."

    a3 "Dallas."
    a3 "Do you... maybe want to go further?"

    d "Hell yeah."

    scene 27dallashouse with dissolve

    a3 "Well, you're going to have to take your pants off then."

    scene black with dissolve

    play sound "audio/zipper.mp3"

    pause (1)

    scene 31dallashouse with dissolve

    a3 "I've never seen someone disrobe so quickly before in my life."

    d "What can I say?"
    d "I might be a tad bit eager."

    a3 "You know, this is about as far as [player_name] and I got."

    d "About?"

    a3 "Well, he started doing this..."

    show dallas_rubbing with dissolve

    d "Ah!"
    d "He really went for it!"

    a3 "Actually, he kind of made me ask for it."

    d "Holy fuck, that's awesome!"

    a3 "It freaked me out actually."
    a3 "He really wanted me to say 'Pussy'."

    d "I'll say 'Pussy'!"
    d "I'll say anything you want if it takes this further!"

    a3 "Okay, see, I didn't really have that mindset."
    a3 "That's why I need you around."
    a3 "To help, you know, guide me in the right direction."

    d "Avalon, I'd like to help but I'm really distracted right now."

    scene 34dallashouse with dissolve

    a3 "How distracted would you be if we, say..."
    a3 "Remove these?"

    d "Fuck."
    d "Yes."

    scene 35dallashouse with dissolve

    a3 "Don't you feel, you know, exposed right now."

    d "Uhh, yeah, that's why I'm dripping wet, Doofus."

    a3 "But don't you feel like..."
    a3 "I don't know."
    a3 "Someone can take advantage of you?"

    d "I'm really hoping someone very specific {b}does{/b} take advantage of me right now!"

    a3 "Ugh, you're no help."

    scene 36dallashouse with dissolve

    d "Oh!"

    a3 "Is this what you want?"

    d "Yes!"
    d "Okay, I know this is the point at which some girls will say something like 'Be gentle,
        it's my first time.'"
    d "You know it's not my first time."
    d "And I want you to finger me like you're trying to kill me."

    a3 "Jesus, Dallas!"
    a3 "You are warped in the head!"
    a3 "But..."
    a3 "I'll do my best?"

    show dallas_fingering with dissolve

    d "Mmh!"

    ai3 "{i}I couldn't believe how easily my fingers slid right inside of Dallas.{/i}"
    ai3 "{i}It felt as if my fingers were being sucked into her.{/i}"
    ai3 "{i}And it was so tight, I could barely even fit two fingers.{/i}"
    ai3 "{i}Everytime I was as deep as I could go, she pressed her lips hard against mine.{/i}"
    ai3 "{i}And I was enjoying it.{/i}"
    ai3 "{i}Not the act, not the sex.{/i}"
    ai3 "{i}But giving her what she wanted.{/i}"
    ai3 "{i}It felt so wonderful giving Dallas this pleasure.{/i}"

    scene 38dallashouse

    d "Oh fuck, stop stop!"
    d "Fuck!"
    d "I'm cumming!"
    d "Oooh!"

    scene 39dallashouse

    d "Uhn..."

    a3 "Dallas, I think your vagina just exploded."
    a3 "These sheets are soaking wet now."
    a3 "My god."

    stop music fadeout 2.0

    scene 40dallashouse with dissolve

    a3 "Are you alright, Dallas."

    d "I just..."
    d "Need a minute..."
    d "To catch my breath."

    scene 27dallashouse

    a3 "Alright."
    a3 "Did you... like it?"

    scene 30dallashouse

    d "Fuck yes."
    d "For all the shit I had to deal with today, this was a nice surprise."
    d "Thank you, Avalon."

    scene 29dallashouse

    a3 "We should talk to [player_name] about, you know, bringing you into our relationship."
    a3 "Do you think he'll be okay with it?"

    scene 30dallashouse

    d "There's only one way to find out."
    d "But if he's not, I want you to know it's okay."
    d "I don't want to come between you and him."

    scene 27dallashouse

    if persistent.lovefordallas == False:
        $ renpy.notify("You've unlocked 'Love for Dallas' in the Scene Gallery on the Main Menu!")
        $ persistent.lovefordallas = True

    a3 "Thank you, Dallas."
    a3 "Let me give him a call."
    a3 "We'll talk to him about it later tonight."
    a3 "Get dressed when you can move again."

    $ renpy.end_replay()
    jump penny_vs_faith

    ## Penny at the Dentist's Office with Faith and Tyler ##

    label penny_vs_faith:

    scene 1pennyvsfaith with fade

    f "Ugh."
    f "Finally time to clock out and go home."
    f "Another day, another dollar..."

    scene 2pennyvsfaith with dissolve

    f "Dad??"

    t "Yes, Faith?"

    f "Are you ready to go?"

    t "I'll be right there, Honeybee."

    scene 3pennyvsfaith with dissolve

    f "Ack."
    f "I hate that stupid nickname."
    f "Why couldn't I have a normal father..?"

    scene 4pennyvsfaith with dissolve

    pause (.5)

    scene 5pennyvsfaith with dissolve

    f "Hm?"

    scene 6pennyvsfaith with dissolve

    f "That's strange."
    f "I thought I heard something..."
    f "Must have been nothin'"

    scene 7pennyvsfaith with fadefast

    f "Dad."

    t "Yes, Daughter?"

    f "We're having pork for dinner."

    t "Is that so?"
    t "Well, alright then."

    scene 8pennyvsfaith with dissolve

    pause (1)

    scene 9pennyvsfaith with dissolve

    pause

    scene 10pennyvsfaith with dissolve

    pause

    scene 11pennyvsfaith with dissolve

    pause

    scene 12pennyvsfaith with dissolve

    pause

    scene 13pennyvsfaith with dissolve

    ps2 "Oh!"
    ps2 "The... lights?"

    scene 14pennyvsfaith with dissolve

    play music "audio/black_mermaid.mp3"

    f "Move and I'll paint the wall with your brains!"

    ps2 "Shit."

    f "Yeah, shit is right."
    f "You messed up today."
    f "But don't worry, it'll be the last time you ever mess up."

    scene 15pennyvsfaith with dissolve

    ps2 "L-look, I don't want any trouble."
    ps2 "I'm just doing what I was hired to do!"
    ps2 "D-don't shoot me!"

    f "See that chair in front of you?"
    f "Go sit down."
    f "Now!"

    scene 16pennyvsfaith with dissolve

    ps2 "Okay, Okay!"
    ps2 "J-just take it easy, alright?"

    f "You're not the one giving orders here."
    f "Dad!"
    f "Come on in."

    scene 17pennyvsfaith with dissolve

    ps2 "If you let me go, I won't tell anyone anything!"
    ps2 "Promise!"

    f "Shut up."
    f "And sit down."

    t "Good work, Daughter."

    scene 18pennyvsfaith with dissolve

    ps2 "How'd you know I was here?"

    f "You practically announced yourself when you hit the ground."
    f "How did you get in?"
    f "Did you weasel your way through the vents?"

    ps2 "B-being small has advantages..."

    f "Cuff her."
    f "I want to find out what she knows."

    scene 19pennyvsfaith with dissolve

    t "Probably not much."
    t "We certainly caught her easy enough."
    t "She can't be too good at her job."

    f "Let me do the thinking, Dad!"

    t "Yes, ma'am."

    f "Just put the damn cuffs on her."

    scene 20pennyvsfaith with dissolve

    play sound "audio/handcuffs.mp3"

    f "What's your name?"

    ps2 "P-penny."

    f "Well, Penny, who hired you?"

    ps2 "An old man named Copper."
    ps2 "He said your d-dad hurt his daughter."
    ps2 "Asked if I'd investigate and see if I could find something on him."

    scene 21pennyvsfaith with dissolve

    t "You know, you're kind of cute, little Penny."

    f "No!"

    scene 22pennyvsfaith with dissolve

    f "I can explain that I shot an intruder."
    f "I can't explain why she was raped!"
    f "Idiot!"
    f "Just... go home, Dad!"
    f "I'll handle this."

    scene 23pennyvsfaith with dissolve

    t "Tsk."
    t "Fine."

    f "Just home."
    f "No stops, no nothin'."
    f "Is that clear?"

    t "Crystal."

    scene 24pennyvsfaith with dissolve

    f "You see what I have to deal with, Penny?"
    f "All my fucking life he's been like this."
    f "Insatiable."
    f "I tried, Penny."
    f "I tried to control him, keep him out of trouble."
    f "But he can't help himself."

    show talk_talk with dissolve

    f "He's a monster."
    f "So I let him out of his cage once a month."
    f "Let him find someone to sleep with, or to hurt..."
    f "Whatever he needs to do to get it out of his system."
    f "But he goes too far!"
    f "Every time!"
    f "And then I gotta clean up the mess."

    scene 27pennyvsfaith with dissolve

    f "Just like I have to clean up this one!"

    ps2 "I'll tell Copper I didn't find anything!"
    ps2 "I swear, no one will ever know about your dad!"

    f "Sorry."
    f "Can't risk it."

    scene 28pennyvsfaith

    stop music fadeout 2.0

    ps2 "Please, God!"
    ps2 "Don't let her shoot me!"
    ps2 "I don't want to die!"
    ps2 "I'll do anything!"
    ps2 "I'll--"

    play sound "audio/revolver.mp3"

    scene 29pennyvsfaith with vpunch

    "*BANG*"

    scene 30pennyvsfaith with dissolve

    play music "audio/sneaking_up_on_you.mp3"

    ps2 "Damn."
    ps2 "I wasn't sure you were actually going to pull the trigger."
    ps2 "Color me impressed."

    scene 35pennyvsfaith

    f "T-that's impossible!"
    f "Nobody can catch a bullet."
    f "I--"
    f "I must have missed!"

    scene 31pennyvsfaith

    ps2 "Yeah, maybe."
    ps2 "I mean, there's only one way to find out, right?"
    ps2 "Go ahead."
    ps2 "Take another shot."

    play sound "audio/revolver.mp3"

    scene 32pennyvsfaith with vpunch

    "*BANG*"

    play sound "audio/revolver.mp3"

    scene 33pennyvsfaith with vpunch

    "*BANG*"

    scene 34pennyvsfaith

    f "No..."
    f "No!"
    f "It's just not possible."
    f "Y-you're..."
    f "You're a superhero??"

    scene 36pennyvsfaith with dissolve

    f "I surrender!"
    f "Just don't hurt me!"

    scene 37pennyvsfaith

    ps2 "Faith, do you know what a bullet looks like after you catch it?"
    ps2 "It's fascinating, actually."
    ps2 "Here, let me show you."

    scene 38pennyvsfaith with dissolve

    pause (.5)

    scene 39pennyvsfaith with dissolve

    pause

    scene 40pennyvsfaith with dissolve

    ps2 "Ahaha!"

    scene 41pennyvsfaith with dissolve

    ps2 "You should see your face right now."
    ps2 "You're terrified!"

    scene 40pennyvsfaith with dissolve

    ps2 "Ahaha!"

    scene 41pennyvsfaith with dissolve

    ps2 "I can't believe you thought I could actually catch bullets."
    ps2 "Oh man, that was great!"
    ps2 "I thought you might pee yourself for a minute!"

    scene 40pennyvsfaith with dissolve

    ps2 "Ahaha!"

    scene 42pennyvsfaith with dissolve

    f "It... was a trick?"
    f "How??"
    f "... Why!?"

    scene 41pennyvsfaith with dissolve

    ps2 "I did some research and found you purchased a revolver some years back."
    ps2 "So I bought blanks for it."
    ps2 "I replaced your bullets when I snuck in last night."
    ps2 "Oh man, it was work."
    ps2 "But so worth it!"

    scene 42pennyvsfaith with dissolve

    f "You're a fucking lunatic."
    f "You know what?"
    f "I might not be able to shoot you."
    f "But this gun {b}is{/b} made of metal."

    scene 43pennyvsfaith with dissolve

    f "I'll just beat you to death with it!"

    scene 44pennyvsfaith

    f "Yaaah!"

    scene 45pennyvsfaith with dissolve

    pause (.3)

    scene 46pennyvsfaith with dissolve

    pause (.3)

    scene 47pennyvsfaith with dissolve

    f "Eyaah!"

    scene 48pennyvsfaith with dissolve

    pause (.3)

    scene 49pennyvsfaith with dissolve

    pause (.3)

    play sound "audio/body_punch.mp3"

    scene 50pennyvsfaith with vpunch

    f "Huugh!"

    scene 51pennyvsfaith with dissolve

    f "Hahk"
    f "Haaaahk"

    scene 52pennyvsfaith with dissolve

    ps2 "Having some trouble breathing?"
    ps2 "There's a soft spot just below the sternum."
    ps2 "It doesn't take but a light tap in that spot to paralyze the diaphragm."
    ps2 "The diaphragm, of course, being the muscle that draws air into the lungs."

    scene 53pennyvsfaith

    ps2 "You'll be alright in a minute."
    ps2 "And don't misunderstand, I know you were just trying to protect your dad."
    ps2 "But he's causing unjust pain to others."
    ps2 "He needs to be removed from society, Faith."
    ps2 "I hope you come to understand the necessity of this one day."

    scene 54pennyvsfaith with dissolve

    pause (.5)

    scene 55pennyvsfaith with dissolve

    ps2 "I'm actually tracking his phone."
    ps2 "Looks like he's heading home."
    ps2 "Just like you told him."

    scene 56pennyvsfaith

    ps2 "Let's see if Detective Evans is up for sending a message."

    stop music fadeout 1.0

    if octavia == True:
        jump octavia_sharol_call
    else:
        jump foot_massage_with_dallas


    ## Back at Byron's house with Dallas and Avalon, Byron giving Avalon a foot
    ## massage

    label foot_massage_with_dallas:

    scene 1dsharolcall with fade

    bi "{i}When I picked up the girls, they both seemed ecstatic.{/i}"
    bi "{i}I guess Dallas really did just need some girl time.{/i}"
    bi "{i}I thought Avalon really needed Dallas for support,{/i}"
    bi "{i}but it seems they actually both need each other.{/i}"

    d "Yeah, I guess he was kind of cute."
    d "He seems like a pushover though."
    d "I'm not really into that."

    a3 "He's a police officer turned detective!"
    a3 "He can't be that much of a pushover."

    b "I think he was just trying to be nice."

    scene 3dsharolcall with dissolve

    b "Dallas, I've been wondering."
    b "And I don't mean to be intrusive."
    b "But..."
    b "Where are your parents?"
    b "You don't live with them?"

    scene 4dsharolcall with dissolve

    d "I have no idea."
    d "When I was fifteen, they said they wanted to hit the road and travel the world."
    d "I refused to go and so they left without me."
    d "That's when I started working at the cafe."
    d "I got that job, paid the bills under my parent's name and lived on my own."
    d "They write once in a while but for the most part, I don't hear much from them."

    scene 5dsharolcall with dissolve

    a3 "You kept it a secret long enough!"
    a3 "I didn't find out until weeks later when I came over and your parent's stuff
        was gone."

    d "I guess I just didn't think it was that big of a deal."

    a3 "You're crazy!"
    a3 "Your parents abandoning you is a huge deal!"

    d "I didn't really see it that way."
    d "They were just doing what they loved."
    d "I could have gone with them but I wanted to finish school and I didn't
        want to leave my friends behind."

    scene 3dsharolcall with dissolve

    b "I wish you two would have told me."
    b "I could have helped you, Dallas."

    scene 4dsharolcall with dissolve

    d "[player_name], I didn't need help."
    d "I'm not helpless, I can take care of myself."
    d "I actually enjoyed the freedom of being on my own."
    d "And the challenge of making it on my own was kind of fun."

    "*Ding!*"

    scene 6dsharolcall with dissolve

    pause

    b "It's Sharol."
    b "Shit."

    scene 7dsharolcall with dissolve

    b "I gotta go for a bit."
    b "But I'll be back soon."
    b "Do you want to go see your mom, Avalon?"

    a3 "Not yet..."

    scene 8dsharolcall with dissolve

    b "Alright, I'll see you an hour or so."

    a3 "Okay."
    a3 "I've got to use the restroom, Dallas."
    a3 "I'll be right back."

    d "I'll be here."

    scene 9dsharolcall with dissolve

    a3 "Hey."
    a3 "You should call that Detective while I'm gone."

    scene 10dsharolcall with dissolve

    d "Hmm."
    d "That's not a bad idea."
    d "Suzi."

    suzi "Yes, Dallas?"

    d "Call Detective Evans."

    suzi "Calling Detective Evans."

    "*Ring* *Ring*"

    det "Detective Evans speaking."

    d "Uh, hey, it's... Dallas."

    det "Miss Dallas, it's nice to hear from you."
    det "Did you remember something you would like to report?"

    scene 11dsharolcall with dissolve

    d "No, sorry."
    d "That's not why I'm calling."
    d "I actually had some questions about the cafe I was working at."

    det "I'll do my best to answer them, Miss Dallas."
    det "But I'm actually on my way to conduct some business at the moment."

    scene 12dsharolcall with dissolve

    d "Oh?"
    d "Did someone knock over a traffic cone and you have to go stand it back up?"

    det "Miss Dallas, I'll have you know my duties go beyond just erecting tipped traffic cones."
    det "I also deliver messages."
    det "In fact, I'm on my way to deliver one right now."

    d "I wasn't aware they were combining the police force with the postal service."

    det "It's all about efficiency when it comes to your tax dollars, Miss Dallas."
    det "After I'm finished, I'd be happy to discuss your questions in person."
    det "If... you'd like?"

    scene 13dsharolcall with dissolve

    d "O-oh, uhh, sure."
    d "I'm actually at [player_name]'s house, with his niece."

    det "I'll stop by after I'm finished with this business."

    scene 12dsharolcall with dissolve

    d "Alright."
    d "I'll see you soon then."

    "*Click*"

    scene 14dsharolcall with dissolve

    d "Ha."
    d "I think he's a little into me."

    scene 15dsharolcall with dissolve

    a3 "I heard you talking."
    a3 "How did it go?"

    scene 16dsharolcall with dissolve

    d "It went well."
    d "He's going to stop by so we can discuss the cafe."

    a3 "Wow, really?"

    d "Yeah."
    d "He said he has to deliver a message first."
    d "Whatever that means."

    a3 "Hmm."
    a3 "A message..?"

    jump evans_message

    label evans_message:

    scene 1tylershelter with fade

    pause

    scene 2tylershelter with dissolve

    pause

    play sound "audio/doorclose.mp3"

    scene 3tylershelter with dissolve

    pause

    scene 4tylershelter with dissolve



    det "Nice place you have here, Mr. Tyler."

    play music "audio/red_head.mp3"

    det "Not very easy on the eyes but sensible, I suppose."

    t "Hm?"

    scene 5tylershelter with dissolve

    t "You broke into the wrong place today, kid."
    t "And I'm already in a bad mood."

    scene 6tylershelter with dissolve

    pause (.2)

    scene 7tylershelter

    play sound "audio/unholster.mp3"

    pause (.2)

    scene 8tylershelter

    det "We don't have to shake hands today, Mr. Tyler."
    det "You can stay right where you are."

    scene 9tylershelter with dissolve

    det "I'm just here to deliver a message."
    det "Your daughter, Faith, is in custody."

    scene 10tylershelter

    t "What are you talking about??"
    t "That's impossible."
    t "She had everything under con--"
    t "I mean, she didn't do anything wrong."

    scene 9tylershelter

    det "Mr. Tyler, your daughter is looking at a long prison sentence."
    det "I'm here to offer you a deal."
    det "If you provide a written confession of all your wrongdoings over the last five years,"
    det "we will drop all charges against her."

    scene 11tylershelter

    t "If you're not going to arrest me or shoot me, I'll have to ask you to get
        the fuck out of my room."

    scene 12tylershelter with dissolve

    det "You have until noon tomorrow to decide."
    det "If you're not at the police station by that time, I'll be comin' back."
    det "You have yourself a wonderful night, Mr. Tyler."

    stop music fadeout 2.0

    scene 13tylershelter with dissolve

    play sound "audio/doorclose.mp3"

    t "... Shit."

    if octavia == True:
        jump octavia_new_hair
    else:
        jump dallas_evans_kitchen

    label dallas_evans_kitchen:

    scene 1kitchenwevans with fade

    det "Miss Dallas, it's nice to see you again."

    scene 3kitchenwevans with dissolve

    det "And you must be Avalon."
    det "It's a pleasure to meet you."

    a3 "Likewise."

    scene 1kitchenwevans with dissolve

    det "I don't mean to intrude, Miss Dallas, but I wanted to apologize in person for this morning."
    det "I heard through the grapevine how aggressive my associates were when they
        raided the cafe."
    det "Must have been awfully frightening for you."

    scene 2kitchenwevans

    d "I was just surprised."
    d "I don't remember seeing you there though."
    d "Did they have you on meter maid duty?"

    a3 "Oh, that's parking tickets and stuff, right?"

    scene 1kitchenwevans

    det "I believe I was asleep at the time, actually."
    det "Someone spiked my morning coffee with a sleep aid."
    det "Apparently I'm not supposed to lose sight of a drink that I am enjoying."
    det "Not even for a second."

    scene 2kitchenwevans

    a3 "Sounds like you're no stranger to pranks."
    a3 "That sounds extreme though..."

    d "Sounds like we'll get along just fine."

    a3 "Would you like to join us in the kitchen?"

    det "Sure."

    scene 5kitchenwevans with fade

    d "We were just curious what's going to happen to the cafe now?"
    d "I worked there for several years."
    d "In fact, I pretty much ran the entire establishment."
    d "Is it possible that I could keep running it?"

    scene 4kitchenwevans

    det "The property will be seized under Civil Forfeiture if the owners of the
        establishment are found guilty of any criminal activity operating out of the cafe."
    det "After reviewing the case, I can tell you it's extremely likely this will be the case."
    det "So the property will be auctioned off and the profits will go to the government."

    scene 5kitchenwevans

    d "And assuming this all goes the way you've laid it out, when will the cafe be
        up for purchase?"
    d "Avalon and I were interested in taking it over."
    d "If that's a possibility."

    scene 4kitchenwevans

    det "Well, the trials will likely take several months."
    det "There's a lot going on with this case."
    det "So, even if it does actually go up for auction, it could be a year."
    det "Or more."

    scene 12kitchenwevans

    d "Shit."
    d "I really don't have that kind of time."
    d "I didn't know it would take so long..."

    scene 8kitchenwevans

    det "Listen, I don't know how set on that specific location you are,"
    det "but I do know of a salon that's recently been approved for auction."
    det "I'm not much good with this kind of thing but I know someone who can
        pull a string or two when she wants."
    det "Apparently, she's rather fond of Avalon so I'd be willing to
        bet she might just be down with helping you two out."
    det "That somethin' you might be interested in?"

    scene 11kitchenwevans

    a3 "You mean Penny?"
    a3 "She could actually do that?"

    d "That would be amazing!"
    d "Avalon and I have some experience with hairstyling."

    scene 10kitchenwevans

    det "Now there's a lot more to business than that."
    det "I don't want you to get into something you can't--"

    scene 9kitchenwevans

    d "Detective, I didn't mean to undersell my part at the cafe."
    d "I was in charge of virtually every aspect of it."
    d "The books, the inventory, hiring, scheduling."
    d "I did it all."
    d "I can handle it."

    scene 8kitchenwevans

    det "Alright then."
    det "You strike me as a very capable young woman, Miss Dallas."
    det "I'll make the call."

    scene 7kitchenwevans

    a3 "Detective, how is Penny by the way?"
    a3 "[player_name] and I were nervous we may have gotten her into something that
        might place her in danger."
    a3 "She seems like a really good person and we don't want her to get hurt."

    scene 6kitchenwevans

    det "[player_name] and I spoke this morning about that."
    det "Let me put it this way, Miss Avalon."
    det "The guy you hired her to pursue?"
    det "Well, she had her fun and now she's wrapping up the case."
    det "It's done."

    scene 11kitchenwevans

    a3 "W-what?"
    a3 "She's gotten him already??"

    d "The guy that assaulted Avalon?"
    d "She seriously got him already?"

    a3 "Wow."
    a3 "I guess she really was worth every--"

    det "Don't say it."

    a3 "... Penny."

    scene 10kitchenwevans

    det "I really hate that catchphrase."
    det "She based her whole damn agency around it."
    det "I said it was stupid to her face once."
    det "I woke up the next morning to 'No, you're stupid!' spelled out in pennies
        on my bedroom floor."
    det "I'm a light sleeper."
    det "How the hell did she do that without waking me up?"
    det "You know what the worst part was?"
    det "I was havin' trouble hearing that whole day."
    det "Turns out she also put a penny in my ear."

    scene 11kitchenwevans

    a3 "Wow, she's pretty sneaky, huh?"

    d "I would very much like to meet her!"
    d "It sounds like I could learn a lot from this chick."

    scene 6kitchenwevans

    det "I don't want you to worry about Penny, Miss Avalon."
    det "Believe me, I've been concerned about her too."
    det "I assure you, she's a very competent woman and this is what she loves doing."
    det "I hope she doesn't get herself in over her head, but you can't stop that
        gal from doin' what she's gonna do."
    det "Trust me."
    det "I believe she's caught wind of a major crime lord or something, actually."
    det "She didn't come out and say it but I believe she's visiting her ex tonight
        to get some additional details."
    det "She always takes extra time on her hair when she plans to visit her ex."

    scene 8kitchenwevans with dissolve

    det "Listen, I hate to dash so soon but I've got to be well-rested tomorrow."
    det "I'm expecting a meeting that I need to be at my best for."

    scene 5kitchenwevans

    d "I should actually go too."
    d "Would you mind if I catch a ride with you, Evans?"

    scene 4kitchenwevans

    det "It would be my pleasure."

    scene 6kitchenwevans with dissolve

    det "Miss Avalon, it was nice to finally meet you."
    det "I hope Penny's resolution of this case gives you some peace of mind."
    det "I'm sure she'll want to speak to you about it soon."

    scene 7kitchenwevans

    a3 "I'm eager to thank her."
    a3 "And I'd like to thank you for meeting with us today."
    a3 "I'll walk you out."

    jump sharol_date

    ## Back at Byron's with Octavia and Avalon leading to Octavia's new haircut ##

    label octavia_sharol_call:

    scene 1osharolcall with fade

    bi "{i}I hope I didn't take things too far this morning with Avalon.{/i}"
    bi "{i}Sometimes she acts like she's completely fine and has moved on.{/i}"
    bi "{i}And then other times, there are screaming reminders that she's still
        affected by what happened.{/i}"
    bi "{i}I just keep getting mixed signals from her...{/i}"

    play sound "audio/dooropen.mp3"
    pause (1)

    scene 2osharolcall with dissolve

    pause

    play sound "audio/doorclose.mp3"

    scene 8osharolcall

    o "Hello, [player_name]."
    o "It's nice to see you again."

    a3 "Hey, Uncle."
    a3 "What are you doing?"

    scene 3osharolcall

    b "Hey, girls!"
    b "I was just... thinking."

    a3 "Careful not to hurt yourself, Uncle."

    o "Did you have a nice workout, [player_name]?"

    b "I've had better."
    b "I was admittedly a bit distracted today."

    scene 4osharolcall with dissolve

    a3 "Do you know Octavia has a panther??"
    a3 "It's huge!"

    b "A... panther??"
    b "Seriously?"

    scene 5osharolcall with dissolve

    a3 "Yeah!"
    a3 "You'll have to come see her sometime!"

    b "Uhh."
    b "Alright, I'll come see Octavia's... panther."
    b "We are talking about a feline animal, right?"

    o "Yes, her name is Maize."
    o "She's a rescue."

    scene 6osharolcall

    b "Okay, you've really got to tell me everything."
    b "How does someone come to own a panther??"

    a3 "It's a really interesting story!"
    a3 "She--"

    "*Ding*"

    scene 7osharolcall with dissolve

    b "Damn."
    b "It's your mom."
    b "I forgot to drop something off to her."
    b "Do you want to go see her?"

    a3 "Not yet..."

    scene 6osharolcall with dissolve

    b "Alright, I'm sorry to cut this short."
    b "But I'll be back shortly."

    a3 "Okay, bye for now I guess..."

    scene 9osharolcall

    b "I really am sorry, Avalon."
    b "I made a promise, I have to keep it."

    a3 "It's fine, Uncle."
    a3 "Just hurry back."

    scene 10osharolcall with dissolve

    a3 "Octavia."

    o "Yes?"

    play sound "audio/dooropen.mp3"

    a3 "I noticed you always have your hair up."

    play sound "audio/doorclose.mp3"

    scene 11osharolcall

    o "Oh, yes, I keep it up in a bun so it's not in the way."
    o "I should go to a salon and have it trimmed."
    o "Why do you ask?"

    scene 10osharolcall

    a3 "I think it's time for a makeover, Octavia."
    a3 "It'll be fun, I promise!"

    scene 12osharolcall

    o "That sounds like a great idea!"
    o "Oh, but I wouldn't want to get my dress dirty."
    o "Do you have something I can wear?"

    a3 "I sure do!"

    jump evans_message

    ## Byron visits his sister, Sharol

    label sharol_date:

    scene 1sharoldate with fade

    bi "{i}Ugh.{/i}"
    bi "{i}This is going to be miserable.{/i}"

    "*Knock* *Knock*"

    play sound "audio/doorknock.mp3"

    scene 2sharoldate with dissolve

    play sound "audio/dooropen.mp3"

    pause (.2)

    play music "audio/evil_aliens.mp3"

    sg1 "Well, look who it is."
    sg1 "The man of the fuckin' hour."

    b "Yeah, when I got money for you, I sure am."

    sg1 "Come on in, Shit Licker."
    sg1 "We're headin' to the kitchen."

    scene 3sharoldate with fadefast

    b "What the hell are you wearing, anyway?"

    sg1 "Oh this?"
    sg1 "I had to dig this outta my closet."
    sg1 "It's been buried in there so long, I'm lucky the moths didn't get at it."

    b "Alright but why are you wearing it?"
    b "Who are you trying to impress?"

    scene 4sharoldate with dissolve

    sg1 "Maybe I just wanted to look nice today."
    sg1 "Why don't you mind your own fuckin' business, you little prick."

    b "Fine!"
    b "I don't actually care anyway."
    b "Do you always have to be such a pain in the ass?"

    scene 5sharoldate with dissolve

    sg1 "Why don't you just sit down and stop being a whiny bitch?"
    sg1 "That somethin' you're even capable of?"
    sg1 "It's like talking to a crying toddler with you."
    sg1 "For fuck sake."

    scene 6sharoldate

    pause (1)

    scene 7sharoldate with dissolve

    b "I brought you the money I promised."
    b "Maybe hire a maid, ya ol' crone."

    scene 8sharoldate with dissolve

    sg1 "What the fuck would I need a maid for?"
    sg1 "I cleaned today."
    sg1 "And thanks for the money you {b}owed{/b} me."

    b "The only time I hear 'thank you' from you is when you're gettin' paid."

    scene 9sharoldate with dissolve

    sg1 "You're a real cocksucker, [player_name]."
    sg1 "Dick."

    stop music fadeout 2.0

    b "What can I say?"
    b "You bring out the worst in me."

    scene 11sharoldate

    sg1 "So."
    sg1 "How is my daughter doing?"
    sg1 "Does she talk about me at all?"

    play music "audio/a_way_out.mp3"

    scene 10sharoldate

    b "She's doing well."
    b "She's still bitter towards you for kicking her out."

    scene 12sharoldate with dissolve

    b "I don't understand why you're so eager to shove her out of your life."
    b "Shit, it's not like you have a whole lot of people lining up to be your best friend."

    sg1 "I didn't sign up for this, [player_name]."
    sg1 "Raising a child is impossible like this."
    sg1 "I was supposed to have help with this shit."
    sg1 "She's better off with you anyway."

    b "I tried to help you, Sharol."

    scene 14sharoldate with dissolve

    sg1 "You didn't try shit."
    sg1 "You come into all that money and all I ask for is enough to get by."
    sg1 "And you won't even tell me where you fuckin' got it!"
    sg1 "For all I know, you robbed a god damn bank or somethin'."

    scene 13sharoldate

    b "I offered you a lot of this money, Sharol!"
    b "A lot!"
    b "All I asked--"

    scene 15sharoldate with dissolve

    sg1 "Yeah, I remember."
    sg1 "Typical fuckin' [player_name]."
    sg1 "Trying to save the world by tellin' people how to live in it."
    sg1 "As if you know best."

    b "All I asked was that you quit drinking."
    b "For Avalon's sake."
    b "Hell, for your own fuckin' sake!"

    sg1 "It ain't help if there are strings attached, Fuckface!"

    scene 19sharoldate with dissolve

    b "Look where it led, Sharol!"
    b "Bringing shady guys over for you to fuck and forget."
    b "Then one of them rapes your daughter and you ignore it!?"
    b "You're a fucking monster!"

    scene 20sharoldate

    sg1 "Don't talk about my life like you know it!"
    sg1 "You disappeared for three years!"
    sg1 "You don't get a say in how the fuck I live my life if you ain't even in it!"
    sg1 "I wasn't supposed to have to do this shit alone!"
    sg1 "I didn't know how the fuck to raise a kid!"

    scene 21sharoldate

    sg1 "And don't talk to me like you ain't played your part, Cumstain!"
    sg1 "I ain't stupid!"
    sg1 "You just had to know about your daddy, didn't you?"
    sg1 "You even made Johnny look into him for you."
    sg1 "And he found him, didn't he?"
    sg1 "The next thing I know, my husband has overdosed on somethin' he ain't touched for five years."
    sg1 "That a coincidence, [player_name]?!"

    b "We're done."

    scene 22sharoldate with dissolve

    sg1 "Fuck."
    sg1 "I'm sorry, alright?"
    sg1 "I don't fuckin' know what happened."

    scene 23sharoldate with dissolve

    b "I don't know either."
    b "But I moved on."
    b "You should have too."

    sg1 "Well, I'm tryin' to now."
    sg1 "Randall is comin' over later."
    sg1 "Gonna take me out on a date."
    sg1 "Sometimes, the way he acts, it..."
    sg1 "It reminds me of Johnny."

    scene 24sharoldate with dissolve

    stop music fadeout 2.0

    b "That's... great."
    b "I met him briefly."
    b "He seemed like a nice guy."

    sg1 "Yeah, poor as dirt though."
    sg1 "He wanted to take me out someplace nice but didn't have the means."

    scene 25sharoldate with dissolve

    b "So that's why you needed the money."
    b "Well, I hope you have a good time."
    b "On my dime..."
    b "Listen, I'll try to bring Avalon over tomorrow."
    b "If she's up for it."

    sg1 "It'd be nice to see her."
    sg1 "Thank you."

    scene 26sharoldate with dissolve

    b "Bye, ya fuckin' harpy."

    sg1 "Bye, Shitdick."

    jump night_four


    ## This is the scene with Octavia and Avalon, where Octavia gets a new
    ## haircut and then proceeds to finger Avalon

    label octavia_new_hair:

    play music "audio/tomorrows_rain.mp3"

    scene 1onewhair with fade

    a3 "You have very fair skin, Octavia."
    a3 "I don't think I've seen anyone as light-skinned as you."

    scene 2onewhair with dissolve

    a3 "Weren't you in the military?"
    a3 "I'm surprised you aren't more tan."

    scene 4onewhair with dissolve

    o "O-oh, well, I actually wasn't outdoors much even while serving."
    o "I don't think it would have mattered if I was though."

    scene 3onewhair with dissolve

    o "I don't tan and I burn very easily."
    o "I'm actually very self-conscious about my skin tone."
    o "Is it unappealing?"

    scene 1onewhair with dissolve

    a3 "I like it, actually."
    a3 "I might even go as far as to say I'm jealous."
    a3 "You look almost as if you're glowing!"

    scene 5onewhair with dissolve

    o "Thank y-- oh?"

    a3 "I didn't mean to startle you."

    scene 6onewhair with dissolve

    a3 "We have to take these off though so I can see what I'm working with!"

    o "Alright."
    o "Please be careful with them."

    scene 8onewhair with dissolve

    a3 "These seem very sturdy."
    a3 "They're kind of heavy."

    o "Do you like them?"

    scene 7onewhair with dissolve

    a3 "I dunno!"
    a3 "I've never had glasses before."
    a3 "Hmm."
    a3 "What does the world look like through the eyes of Octavia?"

    o "N-no, don't put them--"

    scene 9onewhair with dissolve

    a3 "Hey, look at that!"
    a3 "I think my intelligence just increased!"
    a3 "Wait, why isn't it blurry?"
    a3 "These... aren't prescription glasses?"

    o "Avalon, p-please take those off."

    scene 10onewhair with dissolve

    a3 "So, you don't actually need these?"
    a3 "They're just for show?"

    o "Well, I just..."
    o "I prefer for people to think of me as just a regular person."

    scene 13onewhair with dissolve

    a3 "What?"
    a3 "What does that even mean?"

    scene 11onewhair with dissolve

    o "Well, to tell you the truth, I don't have very many flaws."
    o "I have perfect vision, I've never had a cavity."
    o "I can't recall the last time I got sick."
    o "I don't even have dry skin!"

    scene 12onewhair with dissolve

    o "But I don't want anyone to be envious of me because I'm unblemished."
    o "I don't want people to think I'm special."
    o "I want to stand shoulder to shoulder with everyone else."
    o "I just want to be a normal person."

    scene 13onewhair with dissolve

    a3 "That's probably the craziest thing I've ever heard."
    a3 "What are you implying?"
    a3 "That you're perfect?"
    a3 "Are you a robot, Octavia?"

    o "I'm not a robot!"

    scene 7onewhair with dissolve

    a3 "I was pretty in high school."
    a3 "Not as pretty as my friend Dallas, but pretty enough."
    a3 "I remember some people resented me for it."

    scene 8onewhair with dissolve

    a3 "I guess I sort of understand what you mean."
    a3 "But you can be yourself around me!"

    scene 16onewhair with dissolve

    a3 "I'm not envious or jealous of you."
    a3 "I admire you!"
    a3 "So I'm going to help you bring out more of your best."

    scene 15onewhair with dissolve

    a3 "Now, I have to let your hair down to see what I'm working with."
    a3 "So we're going to undo this bun and see what we've got going on!"

    scene 17onewhair with dissolve

    a3 "Ehhh..."

    o "Hmm?"

    a3 "Well, see the big poofy bulge on the top of your head?"
    a3 "It sort of makes you look like..."
    a3 "A cone head."

    scene 18onewhair with dissolve

    a3 "And your face isn't really shaped right for all this hair."
    a3 "It kind of eats your whole head."

    scene 19onewhair with dissolve

    o "What do you suggest?"

    a3 "We need to frame your face!"
    a3 "Because you're really pretty!"
    a3 "So, just like a beautiful Rembrandt, that's what we'll do."
    a3 "We'll make a frame for your head."

    scene 20onewhair with dissolve

    o "Do you know much about hair styling?"

    a3 "Well, my best friend Dallas and I grew up without much money."
    a3 "So if we wanted to treat ourselves to a nice pedicure, manicure or hair styling,
        we had to do it for each other!"
    a3 "We actually got pretty good at all of it."

    a3 "So you'll have to trust me on this next part."

    o "Next part?"

    scene 21onewhair with dissolve

    a3 "The trimming!"

    o "W-wait, I can just schedule a professional to do it!"

    a3 "Nah, I can do it."

    o "But why do you have that crazy look in your eyes?"

    a3 "I'm just very passionate about my work."
    a3 "Hold still, Octavia."

    o "What have I gotten myself into today..?"

    scene black with dissolve

    play sound "audio/haircutone.mp3"

    "*Snip* *Snip*"

    play sound "audio/haircuttwo.mp3"

    "*Snip*"

    scene 23onewhair with dissolve

    a3 "Tada!"
    a3 "You're like, a whole yeti worth of fur lighter!"
    a3 "And see how it goes around your face sort of like a frame?"

    o2 "Magnificent, Avalon!"

    scene 24onewhair with dissolve

    stop music fadeout 2.0

    a3 "You like it?"

    o2 "Very much!"
    o2 "I've never worn my hair quite like this before."
    o2 "It's lovely!"

    scene 25onewhair with dissolve

    a3 "Would you mind turning towards me?"
    a3 "I'd like to make sure the sides are even."

    scene 26onewhair with dissolve

    a3 "I hate to toot my own horn but I've outdone myself."
    a3 "This might be some of my best work."

    if monogamy == True:
        jump octavia_mono_hair
    else:
        jump octavia_poly_hair

    label octavia_mono_hair:

    scene 55onewhair

    o2 "I'm meeting an old friend tonight."
    o2 "This was perfect timing for a new hair cut, Avalon."

    scene 54onewhair

    a3 "Oh?"
    a3 "Who are you meeting?"
    a3 "Is it a date?"

    scene 55onewhair

    o2 "We used to date!"
    o2 "But we had a falling out."
    o2 "It will be nice to reconnect, though."

    scene 56onewhair

    a3 "They will surely regret they ever let you go after seeing you now."
    a3 "When are you supposed to meet?"

    o2 "In half an hour, actually."

    a3 "Oh!"
    a3 "We need to get you on your way then."
    a3 "I'll walk you out."

    jump sharol_date

label octavia_poly_hair:

    play music "audio/cause.mp3"

    scene 27onewhair with dissolve

    a3 "Hm?"

    scene 28onewhair with dissolve

    a3 "Mm."

    scene 29onewhair with dissolve

    a3 "W-what was that for?"

    o2 "I wanted to thank you for the great haircut."

    a3 "Oh."
    a3 "You can... thank me more."
    a3 "If you want."

    o2 "That could be fun."
    o2 "We'll have to stand up for that though."

    scene 30onewhair with dissolve

    a3 "Oof."
    a3 "What are you doing?"

    o2 "Thanking you, of course."
    o2 "There is something irresistible about you, Avalon."

    a3 "There... is?"

    o2 "Oh yes."
    o2 "I've been quite enamored with you ever since I first touched you."

    scene 31onewhair with dissolve

    o2 "You're an incredibly optimistic person."
    o2 "When I touch you, when I feel you, I can feel that optimism."
    o2 "It brightens my whole world, Avalon."

    a3 "R-really?"

    o2 "Yes."

    scene 32onewhair with dissolve

    o2 "But I can feel your pain, too."
    o2 "And I want to take that pain away from you."
    o2 "I want to help you heal."

    a3 "You can do that?"

    scene 33onewhair with dissolve

    o2 "Sex is a powerful thing, Avalon."
    o2 "It can distract from, or even heal, pain."
    o2 "It's like a euphoric dance between two people."
    o2 "And the pleasure can be..."

    scene 36onewhair with dissolve

    a3 "Mm!"

    scene 34onewhair with dissolve

    o2 "Immense."
    o2 "May I have this dance, Avalon?"

    a3 "Y-yes."

    o2 "Close your eyes."

    a3 "Okay..."

    scene 35onewhair with dissolve

    o2 "Can you feel my breath on your lips?"

    a3 "I can."

    o2 "How does being this close to me make you feel?"

    a3 "I'm... having urges."

    o2 "Will you tell me about them?"

    a3 "I want to kiss you again."

    o2 "Okay."

    scene 36onewhair with dissolve

    a3 "Mmha."

    scene 37onewhair with dissolve

    o2 "Keep your eyes closed."

    a3 "Oh, sorry."

    scene 38onewhair with dissolve

    o2 "What else do you want?"

    a3 "I..."
    a3 "I want you to touch me."

    scene 40onewhair with dissolve

    o2 "Here?"

    a3 "No..."
    a3 "Somewhere more... private."

    scene 38onewhair with dissolve

    o2 "I think I understand."

    play sound "audio/zipper.mp3"

    scene 39onewhair with dissolve

    a3 "Oh!"
    a3 "My shorts..?"

    o2 "We'll have to remove them so I can touch you."
    o2 "Won't we?"

    a3 "Y-yes."

    scene 40onewhair

    pause

    scene 41onewhair with dissolve

    pause (.5)

    scene 42onewhair with dissolve

    pause (.5)

    scene 43onewhair with dissolve

    o2 "Avalon?"

    a3 "Yes?"

    o2 "Are you not wearing underwear?"

    scene 44onewhair with dissolve

    a3 "I keep getting my underwear wet."
    a3 "They're... all dirty now."

    o2 "You're frequently aroused?"

    a3 "Yeah..."

    o2 "We'll have to talk more about that later."
    o2 "But for now, let's see if we can sate your desires."
    o2 "At least for the moment."
    o2 "Would you like that?"

    a3 "Yes, very much."

    o2 "Lift your leg up."

    a3 "W-what?"
    a3 "How do you mean?"

    o2 "Let me help you."

    scene 45onewhair

    a3 "Oh!"
    a3 "I feel very exposed right now!"
    a3 "I don't know about this..."

    scene 39onewhair

    o2 "It's okay, Avalon."
    o2 "It's just me."
    o2 "I won't do anything you don't want to do."
    o2 "Would you like to stop?"

    a3 "I..."
    a3 "I trust you."
    a3 "I want to keep going..."

    scene 36onewhair with dissolve

    pause

    scene 38onewhair with dissolve

    o2 "Can you lift your leg a little bit more?"

    a3 "I think so."

    scene 45onewhair

    pause

    scene 46onewhair with dissolve

    a3 "Oh wow!"
    a3 "I'm really exposed now!"

    o2 "It's just me here with you, Avalon."
    o2 "Just breathe."

    scene 47onewhair

    a3 "I don't know why, but I get really anxious when I'm exposed like this."

    o2 "I can see that."
    o2 "But I would never do anything to hurt you."

    a3 "I know."

    scene 36onewhair with dissolve

    pause

    scene 47onewhair with dissolve

    o2 "Do you still want me to touch you, Avalon?"

    a3 "Yeah."
    a3 "I still want that."
    a3 "P-please."

    o2 "Alright."
    o2 "Take a deep breath."

    scene 48onewhair with dissolve

    a3 "Oh!"
    a3 "Yes, right there..!"

    o2 "You weren't lying, Avalon."
    o2 "You're really wet right now."
    o2 "I'm going to insert two fingers inside you."
    o2 "Just a little at first."
    o2 "Alright?"

    a3 "Wow!"
    a3 "Uhm..!"
    a3 "A-alright..."

    scene 1octaviaplay with dissolve

    a3 "Ooh god!"
    a3 "You're inside me!"

    o2 "Are you ready, Avalon."

    a3 "I..."
    a3 "I think so..."

    show octavia_playa

    a3 "Mmmhaa.."
    a3 "This is so crazy."
    a3 "I can't believe this is happening..."

    o2 "Are you enjoying it?"

    scene 49onewhair

    a3 "Mhmm!"

    o2 "Do you want me to go a little deeper?"

    a3 "Mmm..."

    scene 1octaviaplay

    a3 "Okay..."

    o2 "If it gets uncomfortable, just say so."
    o2 "Here we go."

    show octavia_playb

    a3 "Woah woah!"
    a3 "Aaah!"
    a3 "You're going so deep!"
    a3 "Oh Jesus!"

    o2 "You're soaking wet, Avalon."
    o2 "Even so, you're almost too tight."
    o2 "I can barely fit."

    a3 "I..!"
    a3 "I'm going to..!"

    scene 50onewhair

    a3 "Ughn!"
    a3 "Stop stop!"
    a3 "I'm cumming!"
    a3 "Oh shit!"
    a3 "It's so intense!"

    scene 51onewhair with dissolve

    a3 "Ooh..."
    a3 "Oh my god."
    a3 "That was incredible."
    a3 "My legs are shaking, I can barely stay standing."

    o2 "Did you enjoy it?"

    a3 "That is an understatement."

    stop music fadeout 2.0

    scene 52onewhair with dissolve

    o2 "I'm glad."
    o2 "I hope I didn't scare you at all."

    a3 "I don't know why I get so freaked out."
    a3 "I feel so silly for it now."
    a3 "That was amazing!"

    scene 53onewhair with dissolve

    if persistent.closeyoureyes == False:
        $ renpy.notify("You've unlocked 'Close Your Eyes' in the Scene Gallery on the Main Menu!")
        $ persistent.closeyoureyes = True

    o2 "We'll have to do it again sometime!"

    a3 "Mhmm."

    o2 "But for now, I'm a little late for an appointment."
    o2 "I hate to cut this short but I must leave."

    a3 "Okay."

    o2 "Let me just put my dress back on."
    o2 "And then, would you see me out?"

    a3 "Alright."


    $ renpy.end_replay()
    jump sharol_date


    ## Night Four with Avalon and Byron

    label night_four:

    scene 1nightfour with fade

    a3 "Hey, Uncle [player_name]!"
    a3 "You've been gone so long I almost gave up hope you were coming home tonight."

    b "I'm sorry, Avalon."
    b "I didn't mean to be gone so long."

    scene 2nightfour with dissolve

    a3 "Did something happen?"
    a3 "You look a touch melancholy."
    a3 "Is mom alright?"

    scene 3nightfour with dissolve

    pause

    scene 4nightfour with dissolve

    play music "audio/a_quiet_thought.mp3"

    b "Remember Randall?"
    b "We met him when we went to collect your things?"

    a3 "Mhmm."

    b "Apparently, he and your mom are dating."
    b "So I think she's doing rather well."

    scene 8nightfour with dissolve

    a3 "That's great!"
    a3 "I hope she finally found someone that isn't a complete jackweed."
    a3 "Why did you need to go see her though?"

    scene 7nightfour

    b "I promised her some money and I forgot to deliver."
    b "She wanted a romantic evening with Randall but didn't have the funds."
    b "So I just went over to give her the cash I promised."
    b "She misses you."
    b "Do you think you might be up for visiting her tomorrow?"

    scene 12nightfour

    a3 "I'm still pretty angry with her."
    a3 "She's been really mean lately, and very hurtful."
    a3 "I don't know if it has something to do with her drinking more recently or what."
    a3 "But I don't want to be around her when she's like that."
    a3 "If you think she's getting better though, I'll visit her."
    a3 "As long as you go with me."

    scene 11nightfour

    b "She can be a bitter old hag but she's still your mom."
    b "And I do think this relationship she's in is doing her some good."
    b "We'll try to make time to see her tomorrow."

    scene 7nightfour with dissolve

    b "I haven't really had a chance to tell you what I think of your hair."
    b "I was worried when you were all gothed out."
    b "It's not that I disliked the style but I was concerned it wasn't really you."
    b "This feels more like you again."

    scene 8nightfour

    a3 "I was in a dark place for a while."
    a3 "I suppose I just wanted my inner feelings to be reflected in my appearance."
    a3 "A cry for help, maybe?"
    a3 "But being here with you makes me feel happy again."

    scene 11nightfour

    b "I'm glad to hear that but I'm..."
    b "I'm sorry about this morning."
    b "I don't know what got into me, I should have known better."

    scene 6nightfour

    a3 "That was actually a lot of fun."
    a3 "And don't even think about threatening to slow down on the sexy stuff!"

    scene 12nightfour with dissolve

    a3 "I just got caught up in the romance and the new relationship high."
    a3 "There's still damage below the surface and we both need to remember that."

    scene 8nightfour with dissolve

    a3 "I'm going to be better at communicating!"
    a3 "And if I get overwhelmed, we'll just take a break."
    a3 "Okay?"

    scene 9nightfour

    b "It sounds like you've thought a lot about this."

    scene 7nightfour with dissolve

    b "Alright, yeah, communication is key."
    b "Perhaps we need a safe word?"
    b "Like, 'Banana Hammock!' or 'The Queen's Coinslot!'."

    scene 6nightfour

    menu:
        "{b}Additional Dialogue Choice{/b}"
        "Banana Hammock?":
            a3 "Isn't that just lady undergarments that men wear?"

            b "It's not for ladies!"
            b "It's like tucking your best friend in at night with silk sheets!"

            a3 "Gay!"

            b "Nuh uhh!"

        "The Queen's Coinslot?":
            a3 "Careful, Uncle!"
            a3 "If you offend the great country of England, they might come after you!"

            b "The police don't even carry guns there!"
            b "What are they going to send after me?"
            b "Pikemen!?"

        "Or...":
            a3 "Or I could just say 'Stop'."

            b "Simple yet effective."
            b "I wonder why everyone doesn't just use that word?"

            a3 "Another question even science can't answer, I'm afraid."

    scene 7nightfour

    b "I wanted to show you something, Avalon."
    b "Would you accompany me to the attic?"

    scene 10nightfour

    a3 "Uhh, sure."
    a3 "I forgot you even had an attic."
    a3 "What's up there?"

    b "Come on, I'll show you."

    scene 13nightfour with dissolve

    b "Why are there cupcakes on your pajamas?"

    a3 "Because I'm so sweet!"
    a3 "Duh!"

    stop music fadeout 2.0

    scene 14nightfour with fadefast

    b "I haven't been up here in years."
    b "In fact, I think that last time I was up here was with Frank."
    b "We were trying to find one of Sharol's old trinkets that she'd lost."

    a3 "Did you find it?"

    scene 15nightfour with dissolve

    b "Here, take my hand."

    a3 "Oh, thank you!"

    b "No, we never found it."
    b "Watch your head."

    scene 16nightfour with dissolve

    a3 "There's so much stuff up here!"

    b "It's all junk."

    a3 "Then why keep it all..?"

    b "Because it's {b}my{/b} junk!"

    a3 "Packrat!"

    scene 17nightfour with dissolve

    b "This is what I was looking for."

    a3 "An old chest?"
    a3 "What's inside?"

    b "Some of Johnny's old stuff."
    b "This used to be his house, if you remember."

    a3 "Yeah, I remember."
    a3 "He left it to mom but she didn't want it."
    a3 "Too many painful memories, she said."

    scene 18nightfour with dissolve

    b "Yeah, well, there's a lot of good memories here too."
    b "The room you're staying in was actually always your room."
    b "I remember when I helped Johnny put your crib together in there."
    b "I must have been ten years old at the time."

    scene 19nightfour with dissolve

    b "Aha!"
    b "Here it is!"

    a3 "You're keeping me in suspense, Uncle."
    a3 "What is it?"

    scene 20nightfour with dissolve

    b "It's a memory, Avalon."
    b "I want to share it with you."

    a3 "A... memory?"
    a3 "What do you mean?"

    scene 21nightfour with dissolve

    b "Come sit with me."
    b "I have a story to tell you about your dad."

    a3 "Okay."

    scene 22nightfour with dissolve

    play music "audio/touching_moment.mp3"

    b "I'm sure your mother told you but your dad had a guitar."

    a3 "Oh yeah, she did mention that."

    b "It wasn't anything terribly fancy but he loved it all the same."
    b "Sharol used to look fondly at him while he'd strum out some old rock song."

    scene 23nightfour with dissolve

    b "Now, Johnny wasn't exactly the greatest guitarist or singer."
    b "In fact, I'm pretty sure the man was tone-deaf."
    b "But he was so passionate when he'd play that you almost didn't even notice the music."
    b "You would just be entranced by his eagerness and his jubilance."

    scene 28nightfour

    a3 "Where is the guitar now?"
    a3 "I've never seen it before."

    scene 30nightfour with dissolve

    a3 "Don't tell me mom pawned it!"
    a3 "Did she!?"

    scene 26nightfour

    b "No."
    b "I'm getting to that."
    b "Just listen."

    a3 "Okay, okay!"

    scene 23nightfour with dissolve

    b "Johnny had a few friends he liked to jam out with once in a while."
    b "He invited me along with him one day."
    b "Well, his friends lived on the third floor of an apartment complex."
    b "As we were walking up, a gust of wind picked up and tore that guitar right
        out of Johnny's hands."

    scene 30nightfour

    a3 "Oh no!"
    a3 "That's terrible!"
    a3 "What floor were you on?"
    a3 "Was the guitar--"

    scene 26nightfour

    b "Shhh!"
    b "Stop interrupting."

    a3 "Ugh, alright!"
    a3 "Keep going."

    scene 23nightfour with dissolve

    b "The guitar fell all three stories and shattered on the ground."
    b "We were fortunate nobody was standing under it because they'd surely have been
        killed."
    b "We rushed back down the stairs to find his guitar in pieces."
    b "Johnny was devastated!"

    scene 32nightfour

    a3 "Aww!"
    a3 "That's awful."
    a3 "Did he get a new one?"

    b "Well, no..."

    scene 31nightfour

    b "He... never had a chance."
    b "But I managed to fish out a few pieces of the guitar from the dumpster
        he'd thrown it away in."

    scene 23nightfour with dissolve

    b "I found a blacksmith and requested that he fashion something from the metal
        pieces of what remains I had of the guitar."
    b "It was expensive but fortunately, I had some extra cash at the time."

    scene 33nightfour

    b "He made this for me."
    b "I was going to give it to Johnny as a gift."
    b "I... never got the chance."
    b "I came over to give it to him the next day and I found him on the couch."
    b "He wasn't moving, his skin was pale and his body was just... limp."
    b "And I remember his eyes were still open but there was nobody in them."
    b "He was gone."

    scene 30nightfour

    a3 "Y-you're the one that found him?"
    a3 "I didn't know that."
    a3 "That must have been horrifying..."

    scene 32nightfour with dissolve

    a3 "I'm so sorry, Uncle."

    scene 31nightfour with dissolve

    b "That was the worst day of my life."
    b "I still see him like that when I close my eyes sometimes."

    scene 33nightfour

    b "But this isn't supposed to represent that tragedy."
    b "It's a piece of something he loved."

    scene 34nightfour with dissolve

    b "It's a piece of... him."
    b "And I want you to have it so you can always carry a part of him with you."

    scene 35nightfour with dissolve

    b "I know it's too large for your fingers."
    b "But we could make a necklace out of it."
    b "Or, you know, you don't have to wear it."
    b "You can just--"

    scene 36nightfour

    a3 "Try my thumb?"

    b "Your thumb?"
    b "That might work."

    scene 37nightfour with dissolve

    b "Hey, would you look at that?"
    b "It fits!"

    a3 "Yeah!"
    a3 "It slid right on."
    a3 "And it's nice and snug."

    scene 38nightfour with dissolve

    a3 "That's pretty lucky, huh?"

    b "Yeah, it really is."

    scene 39nightfour with dissolve

    a3 "This is..."
    a3 "This is really nice, Uncle."
    a3 "Thank you for this."
    a3 "I'll never take it off."

    scene 40nightfour with dissolve

    b "You're welcome."
    b "I know you didn't know your father very well."
    b "But he loved you so much."
    b "And... so do I."

    scene 41nightfour with dissolve

    a3 "You do?"

    b "I've always loved you, Avalon."
    b "And I always will."

    a3 "Aww, Uncle..."

    scene 42nightfour with dissolve

    a3 "I love you, too."

    scene 43nightfour with dissolve

    pause

    scene 42nightfour with dissolve

    a3 "Maybe we should..."
    a3 "Take this to the bedroom?"
    a3 "So I can thank you more appropriately."

    b "If you want."
    b "Sure."
label galleryScene2:
    if _in_replay:
        $ player_name = renpy.input("What would you like to name the MC?")
        if player_name.strip() == "":
          $ player_name = "Byron"

    scene 44nightfour with fade

    a3 "Uncle."
    a3 "You did such a good job of taking care of me this morning."
    a3 "Maybe tonight it's time I took care of you?"

    scene 46nightfour

    b "Take care of me?"
    b "Is that girl talk for braiding my hair or something?"
    b "Because I would be down for that just so you know."

    scene 45nightfour

    a3 "No, I'm not going to braid your hair tonight."
    a3 "You don't even have enough--"
    a3 "You know what I mean, Uncle!"

    scene 44nightfour with dissolve

    a3 "It's sexy time!"

    scene 46nightfour

    b "Ooh!"
    b "Why didn't you just say so?"
    b "Everything has to be encoded with you girls."
    b "Sheesh."

    scene 47nightfour

    a3 "I think we should pick up where we left off last night."
    a3 "You were grabbing my breast."
    a3 "And I said I'd take my top off for you."
    a3 "Do you remember?"

    b "Hard to forget!"

    a3 "Close your eyes, Uncle."

    scene black with dissolve

    b "Alright, they're closed."
    b "This isn't one of those weird fetishes where I close my eyes and you
        pee on me, is it?"
    b "To each his own but I'm really not into that."

    a3 "I'm not going to pee on you, Uncle!"
    a3 "Shut up."
    a3 "And, umm..."
    a3 "You can open them now."

    scene 48nightfour with dissolve

    a3 "I'm a little more nervous than I thought I'd be."
    a3 "Do you..."
    a3 "Do you like them?"

    scene 50nightfour

    b "Well, I can only see the one."
    b "But it's a nice one!"

    scene 49nightfour

    a3 "I didn't want to overwhelm you with both at the same time!"
    a3 "If there's two, how would you know which one to look at?"
    a3 "And I like this one more so I thought I'd show it off first."

    scene 50nightfour

    b "Are they nocturnal boobs?"
    b "Or will they come out in the day sometimes too?"

    a3 "No more jokes!"

    scene 51nightfour with dissolve

    a3 "Come here."
    a3 "I want to put my arms around you."

    b "Hm?"
    b "Alright."

    scene 53nightfour with dissolve

    ai3 "{i}Looking up at him, I saw the man I love towering over me.{/i}"
    ai3 "{i}I could hide away from the world in his shadow.{/i}"
    ai3 "{i}Nothing could get to me, nothing could hurt me.{/i}"
    ai3 "{i}I'm safe here with him.{/i}"

    scene 52nightfour

    bi "{i}So much tragedy has happened in my life.{/i}"
    bi "{i}I worked so hard to guard myself against the world and block out the pain.{/i}"
    bi "{i}But looking down at her, I felt like I didn't need my armor anymore.{/i}"
    bi "{i}I can be vulnerable with her.{/i}"
    bi "{i}I can let her in.{/i}"

    scene 54nightfour with dissolve

    pause

    scene 55nightfour with dissolve

    a3 "Uncle."

    b "Yeah?"

    a3 "Lay down."

    b "Alright."

    scene 57nightfour with dissolve

    a3 "I'm... still a little nervous."
    a3 "I mean, I want you to see me."
    a3 "I guess I'm just worried you won't like every part of me..."
    a3 "Is that weird?"

    scene 60nightfour

    b "Of course it's weird!"
    b "You're a nut!"
    b "There isn't a hair on your head I don't adore."
    b "There isn't any part of you that I'm not head over heels in love with."

    scene 59nightfour with dissolve

    b "You could be completely naked or you could wear eight layers of clothing."
    b "As long as I can see your eyes, I'm putty in your hands."

    a3 "That was a heck of a gear switch, Uncle!"
    a3 "From silly jokes to genuine compliments."
    a3 "What happened?"

    b "I'm just trying to convince you to lower your arm."
    b "I figured flattery might work."

    scene 58nightfour

    a3 "Ass."
    a3 "You meant it all though, didn't you?"

    b "Every word."

    a3 "You can't hide behind your humor with me, Uncle."

    scene 59nightfour with dissolve

    a3 "I can see right through you."
    a3 "You're completely transparent."

    b "What can I say?"
    b "You've got me under your spell."
    b "I can't--"

    scene 62nightfour with dissolve

    b "Gah!"

    a3 "Is this what you wanted, Uncle?"
    a3 "My chest bare for you to see?"
    a3 "Why do you look so flabbergasted?"
    a3 "They're just boobs..."

    scene 63nightfour with dissolve

    b "They're not just boobs!"
    b "Avalon, I have to tell you something."
    b "I don't want you to get upset."

    a3 "Ugh, here it comes."

    b "You have..."

    scene 61nightfour

    b "Medusa Boobs!"

    a3 "W-what?"
    a3 "What are Medusa Boobs?"

    b "They're the kind of boobs that can petrify a man."
    b "If you stare directly at them, you turn to stone!"
    b "Yep, I am rock hard right now!"

    scene 64nightfour with dissolve

    a3 "If you don't behave, I'll take these away from you!"
    a3 "Don't test me."

    scene 66nightfour

    b "What?!"
    b "Okay okay!"
    b "I'll behave."
    b "Don't put them away."
    b "Ever."

    scene 67nightfour

    a3 "I think it's time for the main course, Uncle."
    a3 "I said I was going to take care of you tonight, didn't I?"

    b "You did. You did say that."

    scene 68nightfour with dissolve

    a3 "Let's see what we're working with here..."

    b "Be gentle."
    b "I mean, with the jeans."
    b "They're pretty cheap, the zipper is on its last leg."

    scene 69nightfour with dissolve

    b "The last time this monster was released, they had to call in Jason Statham
        to take it down."
    b "I know that sounds gay but he said 'No homo' first so it was okay."
    b "..."
    b "Alright, I know you want to take your time."

    scene 71nightfour with dissolve

    b "But eventually you've got to just--"

    scene 72nightfour with dissolve

    b "Avalon?"
    b "What's wrong?"

    scene 70nightfour

    a3 "I... I don't know."
    a3 "My heart just started racing all of the sudden."
    a3 "My chest feels tight."

    scene 73nightfour with dissolve

    a3 "My hands..."
    a3 "My hands won't stop shaking."
    a3 "What's wrong with me?"
    a3 "Why is this happening to me!?"

    scene 74nightfour with dissolve

    b "It's alright, you're going to be alright."
    b "Come here."
    b "Just sit with me."

    scene 75nightfour with dissolve

    if persistent.medusaboobs == False:
        $ renpy.notify("You've unlocked 'Medusa Boobs' in the Scene Gallery on the Main Menu!")
        $ persistent.medusaboobs = True

    a3 "I don't know what happened."
    a3 "I was fine one moment and then..."

    b "It's okay, I've got you."
    b "We're done for tonight."
    b "And we'll figure this out."
    b "I promise..."

    $ renpy.end_replay()
    stop music fadeout 1.0

    ## Penny and Octavia if on the Octavia Path

    if octavia == True:
        jump pennyohouse
    else:
        jump myrabelle_four

    label pennyohouse:

    scene 1pennyohouse with fade

    pause

    scene 2pennyohouse with dissolve

    pause

    scene 3pennyohouse with dissolve

    pause

    scene 4pennyohouse with dissolve

    pause

    scene 5pennyohouse with dissolve

    ps2 "Hm?"
    ps2 "Well, isn't that strange."

    scene 6pennyohouse

    ps2 "I figured she would be in bed."
    ps2 "Too bad."
    ps2 "I was hoping to surprise her."

    scene 7pennyohouse

    play music "audio/tomorrows_rain.mp3"

    ps2 "It's certainly not like her to stay up late."

    scene 8pennyohouse with dissolve

    ps2 "Oh ho ho!"
    ps2 "Someone is trying to be sneaky tonight!"

    scene 9pennyohouse with dissolve

    ps2 "You certainly got the jump on me."
    ps2 "I confess, I may have let my guard down."
    ps2 "What's your next move?"
    ps2 "Are you going to frisk me?"
    ps2 "Pat me down to make sure I'm not carrying anything dangerous?"

    scene 10pennyohouse

    ps2 "I'm not, just so you know."
    ps2 "What use are weapons in the presence of such disarming beauty, anyway?"
    ps2 "Though one can never be too careful."
    ps2 "I could have something up my sleeve!"
    ps2 "Shall I disrobe to put your mind at ease?"

    scene 11pennyohouse

    o2 "You're so long-winded tonight, Penny."
    o2 "I haven't even been able to get in a simple 'Hello'."
    o2 "And please don't try to seduce me right now."
    o2 "I thought you came here to talk?"
    o2 "Lights on."

    scene 12pennyohouse with dissolve

    ps2 "You changed your hair?"

    scene 12pennyohouse2 with dissolve

    ps2 "Wow!"
    ps2 "I've got to admit, I don't think I've ever seen you quite so alluring."
    ps2 "You've asked me to remain maidenly but I don't know if that's possible with
        you looking so enticing."
    ps2 "You must introduce me to your stylist!"

    scene 14pennyohouse

    o2 "I believe you already know her."
    o2 "The young Miss Avalon?"

    scene 13pennyohouse

    ps2 "Our mutual acquaintance, it would seem."
    ps2 "It's quite the coincidence, isn't it?"
    ps2 "Both of our fates intertwining with the same person, in the same week?"
    ps2 "The stars align, Octavia."
    ps2 "Perhaps we're destined to be together after all?"

    scene 16pennyohouse

    o2 "Or perhaps someone is artificially weaving the strings."
    o2 "It is quite the coincidence, isn't it?"
    o2 "It wouldn't happen to be one of your ploys, would it?"

    scene 23pennyohouse

    ps2 "You think I'm capable of such an elaborate scheme?"
    ps2 "You flatter me!"
    ps2 "But I assure you, this is not one of my stratagems."

    scene 19pennyohouse with dissolve

    ps2 "I know it seems like something I might do but I am not trying
        to force myself back into your life."
    ps2 "Despite how much I might want to be a part of it."
    ps2 "I'm trying to give you space, Octavia."
    ps2 "Sincerely."

    scene 24pennyohouse

    o2 "I miss you, Penny."
    o2 "I do."
    o2 "But I stand resolute, I don't want the lifestyle you've chosen."
    o2 "I've had enough adventure for multiple lifetimes."
    o2 "I don't need anymore."

    scene 25pennyohouse

    ps2 "I'm not asking you to be a part of my work, Octavia."
    ps2 "I never did."

    scene 20pennyohouse

    o2 "The time I spend with Avalon and [player_name] is cordial."
    o2 "I feel tranquil around them."
    o2 "And I have Maize who will lounge around and relax on the couch with me."
    o2 "I want that, Penny."
    o2 "I want a quiet, uncomplicated life."
    o2 "Your trade invites chaos and it always bleeds into our personal lives."

    scene 21pennyohouse

    ps2 "Fine, whatever, I didn't come here to persuade you to take me back anyway."

    o2 "Why did you come?"

    ps2 "I forget."

    o2 "Thank you."

    scene 25pennyohouse with dissolve

    ps2 "Wh--"
    ps2 "For what?"

    scene 18pennyohouse

    o2 "For helping [player_name] find that man that assaulted Avalon."
    o2 "I'm sure Avalon would like to thank you in person once you catch him."
    o2 "Do you have plans to see her?"

    scene 17pennyohouse

    ps2 "The first time I met her, she left an impression."
    ps2 "That girl is clever, kind and beautiful."
    ps2 "She sort of reminds me of someone else I know, if you catch my drift."
    ps2 "Yes, I have plans to see her again."

    scene 19pennyohouse with dissolve

    ps2 "I'd like to be a part of your life again, Octavia."
    ps2 "I hope you'll reconsider our relationship."
    ps2 "I'd even settle for being just friends."
    ps2 "Can you at least call once in a while?"

    scene 18pennyohouse

    o2 "I'll consider it."
    o2 "Perhaps the next time you stop by, you can come during the day."
    o2 "I know Maize misses you."
    o2 "Would you like me to see you out?"

    scene 15pennyohouse

    ps2 "There was one more thing."
    ps2 "It's about [player_name]."
    ps2 "I was hoping you could get me some information about--"

    o2 "His father."

    scene 17pennyohouse with dissolve

    ps2 "Ahh."
    ps2 "You already knew I was going to ask, didn't you?"

    scene 24pennyohouse

    o2 "I had a feeling it was the reason you were coming over."
    o2 "And here you said you wouldn't involve me in your work."

    scene 21pennyohouse

    ps2 "Well, we're not dating so the terms of that deal don't apply."
    ps2 "And besides, do you really want [player_name] to have to live in fear for
        the rest of his life?"
    ps2 "You should want me to handle this, Octavia."

    scene 22pennyohouse

    o2 "And what if you get hurt?"
    o2 "Or worse?"
    o2 "It's not worth it, Penny!"

    scene 21pennyohouse

    ps2 "I can handle it."
    ps2 "Are you going to help me or not?"

    scene 24pennyohouse

    o2 "I already got all the information I could."
    o2 "I'll send it to you."

    scene 19pennyohouse

    ps2 "Thank you."
    ps2 "I'll see myself out."
    ps2 "You know, when it comes to matters of the heart,"
    ps2 "you really give no quarter."
    ps2 "Goodbye, Octavia."

    stop music fadeout 1.0



    ## Myrabelle, Act Four

    label myrabelle_four:

    jump act_five_s

    scene 1mfour with fade

    play music "audio/cheer_up.mp3"

    m "Hey there!"
    m "I'm Myrabelle, Lockheart's trusted representative."
    m "And you know what this means."
    m "That's right, you've reached the end of the current content."
    m "Bummer!"

    scene 10mfour with dissolve

    m "But it's not all bad!"
    m "We have some news for you."
    m "But first, I bet you're curious as to whose room I'm in."
    m "I have a personal guard who has been annoying the shit out of me lately."
    m "He's supposed to be protecting me at all times but I gave him the slip a few hours ago."

    scene 3mfour with dissolve

    m "This is his room, and this is his bed where he lays his empty noggin."
    m "It's a bed that is too good for a slimy little dickweasel like him."
    m "He's overpaid."

    scene 11mfour with dissolve

    m "If you're wondering about the candle behind me, so am I!"
    m "What kind of dipshit leaves a candle burning while he's not at home?"
    m "Especially on top of a wooden desk!"
    m "This is what I'm talking about."
    m "He's a moron."

    scene 4mfour with dissolve

    play sound "audio/magic_summons.mp3"

    m "We're going to leave him a surprise today."
    m "Don't feel bad for him."
    m "Trust me, he deserves this."

    scene 5mfour with dissolve

    pause

    scene 6mfour with dissolve

    m "I have a task for you, Serpent."
    m "When my Swordsman lays down tonight, I want you to bite him."
    m "Hard!"
    m "Is that understood?"

    play sound "audio/snake_hiss.mp3"

    "*Hhsss*"

    m "Good."
    m "Now uncoil and flatten out so I can hide you."

    scene 7mfour with dissolve

    pause

    scene 8mfour with dissolve

    m "Perfect."

    scene 9mfour

    m "It's not venomous but the bite is still going to hurt like hell."
    m "Anyway, we've been working really hard lately!"
    m "As our skills have grown, we've gone back through and polished up Avalon
        a bit."
    m "If you played earlier versions, you may have noticed some extra choices this
        time around!"
    m "Let us know what you thought about them."

    scene 13mfour with dissolve

    m "I know a lot of you have been interested in donating."
    m "We are absolutely flattered that so many people want to support us."
    m "So we're starting a Patreon, as requested!"
    m "But we're going to put together some perks before we open it up to the public."

    scene 12mfour with dissolve

    m "One perk of being a supporter is going to be mini-episodes featuring yours truly."
    m "That's right!"
    m "I'm going to have my own episodic visual novel available to patrons!"

    scene 10mfour with dissolve

    m "And we'll have some other special rewards too!"
    m "The scheduled release for our Patreon account will be April 2nd."

    scene 13mfour with dissolve

    m "Thank you so much for taking the time to enjoy our novel."
    m "Please let us know what you thought!"
    m "We're aiming to release Act Five in Mid-May."
    m "We hope you'll be back for more Avalon."
    m "Bye for now!"

    stop music fadeout 1.0

    return
