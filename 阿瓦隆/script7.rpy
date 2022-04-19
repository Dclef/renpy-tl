

label act_seven:

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

    jump act_seven_s

label act_seven_s:

    scene avalon with fade

    if persistent.actSeven == False:
        $ renpy.notify("You've unlocked Act Seven in Act Select on the Main Menu!")
        $ persistent.actSeven = True

    stop music fadeout 2.0

    pause

    scene avalonactseven with dissolve

    pause

    scene 1returnofleah with fade

    b "It... it can't be. After all this time..?"

    scene 2returnofleah with dissolve

    play music "audio/soft_reminder.mp3"

    l "It's me, [player_name]! It's really me!"

    scene 3returnofleah with dissolve

    l "Oh, [player_name]. I'm so glad to see you!"

    b "But you disappeared. You were just gone. And then you just--?"

    l "I'm sorry! I'm so sorry! I can explain, [player_name]. I can explain everything!
        I promise!"

    scene 4returnofleah with dissolve

    l "Please don't tell me you hate me for leaving. I couldn't bear it."
    l "I shouldn't have left, I know. I should have left a note or... or something!"
    l "I dreamt of this day for six months. I thought it would never come!"

    b "Why didn't you just come back then? Why didn't you call or--"

    scene 5returnofleah

    a3 "Uncle, what's going on? I heard someone in distress. Is everything alright?"

    b "Er, no. I mean, yes, everything is... everything is..."

    scene 6returnofleah with dissolve

    l "I didn't realize [player_name] had someone over. I didn't mean to disturb you."

    a3 "Who are you? Why are you here so late?"

    scene 7returnofleah with dissolve

    l "I guess I don't have a great excuse. This probably could have waited
        until the morning. I was just too excited to see [player_name]."
    l "I'm his [persistent.leah_rel], Leah. You must be his niece, Avalon. He's told me so much
        about you!"

    scene 8returnofleah

    a3 "You're Leah!? We were just talking about you! We thought you were dead.
        Where have you been?"
    a3 "Did Penny find you? Wow, she's exceptional. That was fast!"

    scene 7returnofleah

    l "Penny? I'm sorry, I don't know who that is. I wasn't 'found', I was--"
    l "Well, it's a bit of a story actually."

    scene 8returnofleah

    a3 "I'm sure we would love to hear it."

    scene 9returnofleah with dissolve

    a3 "Isn't that right, Uncle? You must be thrilled."

    scene 10returnofleah with dissolve

    a3 "[player_name]? What's wrong? Are you alright?"

    scene 11returnofleah

    b "You were just... gone. I looked for you, Leah. I called the police."
    b "How could you just leave like that? And then you just show up at my
        doorstep six months later?"
    b "I was crushed, Leah. I thought I'd never see you again..."

    scene 12returnofleah

    l "I was upset and angry and I made a mistake. I'm sorry, I'm really sorry!"
    l "Please give me a chance to explain. And if you're still mad at me, I'll leave."
    l "And you can hate me and never see me again. I would deserve that..."

    scene 13returnofleah with dissolve

    a3 "I think we should hear her out, Uncle. I bet she has a good reason."
    a3 "We all deserve a chance, don't we? And she seems genuinely apologetic!"

    b "Of course. I'm just trying to collect myself. I'm sorry."

    a3 "It's alright! Let's go talk in the kitchen."

    scene 14returnofleah with fadefast

    a3 "I'm eager to hear where you've been, but first I just want to say that
        you are really pretty."
    a3 "I didn't expect that since [player_name] is so-- Er, I mean..."

    scene 21returnofleah

    b "Go on, Avalon. Finish that statement."

    a3 "No, I don't want to! You can't make me!"

    scene 24returnofleah

    l "Thank you, Avalon. You're really pretty, too. I knew you would be though."
    l "[player_name] used to talk about you like you were the brightest star in his
        sky."
    l "I'm starting to see why. You're a bundle of positivity. That's quite inspiring."

    scene 15returnofleah with dissolve

    l "I know you're eager to hear where I've been so I'll try to be blunt."
    l "A few days before we went to the pool, my company made me an offer. I
        turned it down flat right away!"
    l "But after what happened, I was desperate to leave. I just... wanted to get
        away from you. So I changed my mind and accepted the offer."

    scene 17returnofleah

    b "I should have handled that situation differently, Leah. I shouldn't have left."
    b "I panicked! I just didn't know how to react so I ran. Like a coward."

    scene 28returnofleah

    a3 "You accepted the offer? What does that mean? You were transfered to another city?"
    a3 "You should have called though. Or written an e-mail or something..."

    l "I couldn't!"

    scene 15returnofleah

    l "The offer was a research and development project. They set aside tens of
        millions for a year long project to make a breakthrough in artificial organics."
    l "Specifically, they wanted to engineer a bio-mechanical heart."

    scene 30returnofleah

    a3 "An artificial heart? You got to be a part of a project like that?"
    a3 "You must be like, super smart and educated. Why did you turn it down at first?"
    a3 "A project like that must be huge! I mean, you'd have your name on it, right?"
    a3 "How could you say 'No' to that?"

    scene 26returnofleah

    l "Erm. I hadn't thought about it like that. I was more interested in
        the lives it would save rather than having recognition."

    a3 "I didn't mean to imply--"

    scene 24returnofleah with dissolve

    l "I know you didn't mean it that way. I didn't mean to say you did."
    l "But it was much more complicated than that. Our prototype is only a step
        forward, not a leap. The battery for the device--"

    scene 20returnofleah

    b "This is fascinating, I'm sure. But could you please skip to the part where
        you couldn't let me know you were alive??"

    scene 15returnofleah

    l "We weren't allowed to, [player_name]. That's why I turned it down at first."
    l "They were paranoid about a leak. We weren't allowed to contact anyone until we were finished
    a year later."
    l "It was part of the contract and that's why I turned it down at first. You and I were
        becoming so close, I didn't want to leave you."
    l "When you rejected me, I told them I wanted in on the project. They approved,
        and the next day I was locked in to a contract."

    scene 28returnofleah

    a3 "You made a brash decision and were stuck with the consequences."
    a3 "I can understand that, Leah. I'm sure we all can. But didn't you say
        it was a year long project?"
    a3 "You're back and it's only been six months."

    scene 25returnofleah

    l "I worked my team so hard that we finished in half the time we expected
        it to take."
    l "And I did it so I could get back to [player_name]. But this isn't going
        at all like I expected..."

    scene 19returnofleah

    b "I didn't mean to make this reunion so grim, Leah."

    scene 18returnofleah with dissolve

    b "I'm glad you're back. I'm just stunned right now. I'm in disbelief."

    scene 17returnofleah with dissolve

    b "B-but I... I met someone, Leah. I'm in a--"

    scene 27returnofleah

    menu:

        "{b}Additional Dialogue Choice{/b}"

        "Shrink!":
            a3 "A therapist! He met with a therapist. They're working through
                some things."
            a3 "The results are in! It turns out [player_name] is utterly bananas."

            l "R-really?"

            a3 "Yeah, anyway..."

        "Detective!":
            a3 "Penny! He met with Penny who is a detective and she's searching for
                you as we speak."
            a3 "Uhm. We should probably let her know we found you. Suzi, tell Penny to
                call off the dogs!"
            a3 "... {w} I forgot that I left my phone in the other room. Anyway!"

        "Jesus!":
            a3 "He found Jesus! Uh, yeah. He's in a relationship with God. It's long
                distance but they both seem happy."

            l "He found Jesus but he's in a relationship with God?"

            a3 "They're the same person. Or something. Religion is confusing, I
                just go with it."
            a3 "But anyway..!"

    a3 "Tell me more about your project. You said you finished? Was there a prototype or..?"

    bi "{i}She's trying to keep our relationship a secret from Leah? Why would
        she do that..?{/i}"

    scene 24returnofleah with dissolve

    l "We finished our work and we have a prototype. That's right!"
    l "I don't want to geek out on you but it's quite an impressive device. It
        doesn't beat like a heart, it pumps consistently."

    a3 "So you wouldn't have a heartbeat!?"

    l "Freaky, right? But don't get too excited, there were many flaws in the design."
    l "For example, there's no battery we could comfortably use to power the device long term."
    l "We'd like to use the body's own power supply but we're some time away from
        that technology."

    a3 "Fascinating!"

    scene 21returnofleah

    b "Don't act like you know what she's talking about. She's a Gyro-Medical Engineer."

    l "Bio-Mechanical Engineer."

    b "That's what I said."
    b "You have no idea what she's talking about right now, Avalon."

    a3 "I do too!"

    scene 29returnofleah

    a3 "But I don't understand something. If it was so secretive that they cut you off
        from the rest of the world, how are you telling us all this now?"
    a3 "Wouldn't this be a breach of your contract?"

    scene 24returnofleah

    l "Nope! We weren't allowed to leave until the patent went through. The
        design is solidified under the ownership of the company now."
    l "So we can talk about it!"
    l "Once modern technology moves a little further along, we'll make some minor
        adjustments to the design."
    l "Hopefully we will be able to eliminate the need for live organ transplants
    within the next decade or so!"

    scene 22returnofleah

    b "Leah is a little ahead of us in terms of personal achievements."
    b "I guess we have some catching up to do!"

    a3 "I've got time!"

    scene 27returnofleah

    a3 "I'm eager to hear more about you, Leah. But I imagine you're pretty exhausted.
        I know I am!"
    a3 "Do you want to stay the night? You can have my bed!"

    scene 25returnofleah

    l "Actually, I might have to take you up on that offer. I signed over my house
        to the company and they sold it for me."
    l "I don't have a place to live right now. But I don't want to intrude. I can
        get a hotel ro--"

    a3 "I insist! Please stay!"

    scene 26returnofleah

    l "O-okay. Sure. Thank you, Avalon."

    scene 18returnofleah

    b "I'm glad you're back, Leah. Sincerely, you have no idea what this means
        to me."
    b "I hope I didn't disappoint you too much when you arrived. I'm just... taking
        it in, you know?"

    scene 16returnofleah

    l "I understand. I may have built unrealistic expectations of our reunion up
        in my head."
    l "I'm glad it went this way though."

    scene 24returnofleah

    l "I didn't expect you to be here, Avalon. But I'm sure glad you were."
    l "You actually made this a lot easier. I-- Umm, thank you."

    scene 27returnofleah

    a3 "You're welcome. I like meeting new people!"
    a3 "Come on, I'll show you to my room and we can talk more tomorrow."

    stop music fadeout 1.0

    jump sharolfinds

    label sharolfinds:

        scene 1sharolfinds with fade

        sg2 "Ugh! My head. What the hell poison did we drink last night? Gasoline!?"
        sg2 "Fuck!"

        scene 2sharolfinds

        play music "audio/natural.mp3"

        r "Hey, lady. Oh, damn. You're feelin' a bit hungover, huh?"
        r "You were hittin' the sauce pretty hard last night. You gonna be alright?"

        scene 3sharolfinds with dissolve

        sg2 "I feel like there's a twelve car pile-up inside my brain. I don't
            usually drink the hard stuff these days."

        r "Well, you just go on an' rest today, Gorgeous. I got an errand ta run."

        scene 4sharolfinds

        sg2 "An errand? Oh shit, you gotta take that ol' tractor in for repairs.
            I forgot."
        sg2 "Let me put on some--"

        scene 3sharolfinds with dissolve

        sg2 "Shit! My head is killing me!"

        r "How about you hang out here until I get back and ward off them nasty
            devil's shakin' about in yer brain?"

        scene 5sharolfinds with dissolve

        sg2 "Are you sure? You said it was a long drive there and back. I
            don't want you to have to go alone."

        r "It's no problem at all! I'm used ta it. And I'll have a recouped woman
            to look forward to coming back to."

        r "Maybe you can call your daughter today and see if she has time to visit?"

        scene 4sharolfinds

        sg1 "Ugh. That sick fuck [player_name] is taking advantage of my little girl and
            turning her into an incestuous freak!"

        scene 3sharolfinds with dissolve

        sg2 "Ow ow. I think my head is about to pop."

        r "She's an adult now, Sharol. We talked about this. You gotta let her
            make her own decisions and her own mistakes."

        sg2 "He's probably manipulating her or... something."

        scene 5sharolfinds with dissolve

        r "How about you just focus on gettin' better and we'll worry about
            all other stuff later. Okay?"
        r "We got all the time in the world."

        scene 6sharolfinds with dissolve

        r "I gotta run, Lady. I don't want to be late! Bye for now."

        sg2 "Hurry back!"

        stop music fadeout 2.0

        scene 7sharolfinds

        sg2 "Uhn, fuck. Gotta take something for this... headache..."

        scene 8sharolfinds with dissolve

        pause

        scene 9sharolfinds

        play music "audio/evil_aliens.mp3"

        sg2 "Hmm."

        scene 10sharolfinds

        sg2 "What's in here?"

        scene 11sharolfinds

        pause

        scene 12sharolfinds

        sg2 "Not helpful."

        scene 13sharolfinds

        pause

        scene 14sharolfinds with dissolve

        sg2 "Aha! Jackpot!"

        scene 16sharolfinds with dissolve

        sg2 "Thought you could hide from me, didn't you?"
        sg2 "But I found you!"

        scene 15sharolfinds with dissolve

        sg2 "Nothin' heals a hangover better than a little hair of the dog."

        stop music fadeout 2.0

        ## Avalon invites Leah out for a fun day date.

        scene 1morningseven with fade

        ai3 "{i}[player_name] has his therapy session this morning so I'll have some time
            to get to know Leah.{/i}"
        ai3 "{i}I spent an hour planning out an event for us earlier. I hope
            she's up for it.{/i}"
        ai3 "{i}And afterwords, I can tell her about [player_name] and I. I have to make
            her like me before that though!{/i}"
        ai3 "{i}She's so important to [player_name]. She just can't hate me, I can't let
            that happen!{/i}"

        scene 2morningseven with dissolve

        ai3 "{i}Okay, here goes nothing. Be super sweet, Avalon! You can do this!{/i}"

        play sound "audio/doorknock.mp3"

        "*Knock* *Knock*"

        a3 "Uhm, Leah? It's me, Avalon. Are you awake?"

        scene 3morningseven

        play music "audio/soft_reminder.mp3"

        l "Avalon? Yeah, I'm awake. You can come in."

        play sound "audio/dooropen.mp3"

        scene 4morningseven

        a3 "Good morning! I didn't wake you, did I? You must be exhausted from
            your work."

        l "I've been awake for a while. I'm used to getting up early. No rest for
            the weary!"

        scene 5morningseven with dissolve

        a3 "Whoa! Is that a tattoo? Are you in a knife gang or something?"

        l "No, silly!"

        scene 6morningseven

        l "Tattoos aren't just for ruffians and thugs."

        scene 7morningseven with dissolve

        l "Here, take a look."

        scene 8morningseven with dissolve

        a3 "It's a heart with squigglies. Like from a heart monitor, right?"

        l "Exactly! When I was growing up, I had a heart condition. The beeping
            from the heart monitor let me know that I was still alive."
        l "It was reassuring, in a way. So I wanted to carry it around with me
            forever."

        scene 9morningseven

        a3 "So that must be what made you get into your profession. Bio-Mechanical
            Engineering, right?"

        l "Yep! My inspiration was my own failing heart."

        a3 "But you're okay now?"

        scene 10morningseven

        l "For now I am. It's unlikely that my heart will carry me into old age though."

        scene 8morningseven with dissolve

        l "But by then, we should have an artificial alternative. I'm staying positive!"

        scene 11morningseven with dissolve

        l "In the morning, when I look into the mirror and I see this tattoo,
            I hear the beeping all over again and I'm happy to be alive."

        scene 7morningseven with dissolve

        l "It's cheesy, I know."

        l "But it works for me."

        scene 12morningseven

        a3 "I guess it is cheesy but I liked it. You have a physical representation of
            your positivity. I found out how important that is recently."
        a3 "When I feel sad or scared or anxious, I have this ring that Uncle [player_name]
            gave me. It reminds me that people love and support me."
        a3 "I um, I have a confession, Leah. I kind of thought about you a lot last night."

        l "O-oh?"

        a3 "Well, I mean, you're this educated and accomplished woman. You designed
            an artificial organ! I just... hope I'm that cool one day."

        scene 13morningseven

        l "No no, it's nothing terribly impressive. It doesn't even technically work.
            And I had a whole team to help me."

        a3 "So humble, too."

        scene 14morningseven with dissolve

        l "Sometimes I think I dedicated too much to this career. Now I have it but
            I don't have many friends."
        l "It's hard to enjoy your accomplishment when you don't have someone to share--"

        scene 15morningseven with dissolve

        a3 "Holy guacamole! Is that a braid?! I didn't notice that yesterday.
            How did I not notice that yesterday?"
        a3 "Can I touch it?"

        l "Er, I mean, sur--"

        scene 16morningseven with dissolve

        a3 "It's so soft, Leah! You have the most unique and awesome hair I've
            ever seen."

        l "You think so? A lot of people think it's pretty lame."

        a3 "I think they're pretty lame! You look like one of those Irish bar maids
            that guys fawn over. Like a sexy beer maiden."

        l "Thanks... I think?"

        a3 "Yeah, it was definitely a compliment."

        scene 17morningseven with dissolve

        l "Well, I like your braid too. You look like a fairytale princess with those
            big innocent eyes and soft features."

        a3 "You think so?"

        l "Yeah, I do."

        scene 18morningseven with vpunch

        l "Oof!"

        a3 "Thank you, Leah! You're so nice. I knew you would be!"

        l "Oh, you're welcome. You're quite affectionate, aren't you?"

        scene 19morningseven with dissolve

        a3 "Sorry! I know we just met so that was awkward. I was so nervous that this wasn't going
            to go well. I'm just happy that it is."

        a3 "Uncle [player_name] has an appointment this morning. I thought
            it would be the perfect time for us to get to know each other."
        a3 "I set up a special event for us if you're interested?"

        scene 20morningseven

        l "That sounds intriguing and mysterious. Okay, yeah, sure. I know
            [player_name] needs some time to process everything anyway."
        l "I'm actually glad you were around. The thought of making it
            back to [player_name] kept me going but I..."
        l "I guess I didn't consider the possibility that he might be pretty upset
            with me."

        scene 19morningseven

        a3 "He's happy you're back, Leah. He'll forgive you, you'll see!"
        a3 "Let me go tell him that we're going to hang out today."
        a3 "When you're all dressed and ready to go, come meet us in the living room."

        l "Okay, I shouldn't be long."

        stop music fadeout 2.0

        scene 21morningseven with fadefast

        a3 "Hey, Uncle! I hope sleeping on the couch wasn't too uncomfortable."
        a3 "I wanted to let you know that--"

        b "Shh! Come here and watch this."

        scene 22morningseven with dissolve

        stop music fadeout 2.0

        a3 "What is it, Uncle?"

        b "I'm not exactly sure yet but the picture I saw was nuts."

        a3 "Is everything okay?"

        b "Yeah, for us! But not for the guy on the news, apparently."

        scene 1morningnews with fadefast

        pat "Welcome to the morning news brought to you by Hound News."
        pat "We have a very unusual story for you this morning. I'm Trish with the dish
            and here's the scoop!"

        scene 2morningnews with dissolve

        pat "Several police departments around the city erupted with incoming calls
            from concerned citizens describing a man floating in the sky."
        pat "Our helicopter was able to make it out to the scene before
            the police and captured several images."

        scene 3morningnews with dissolve

        transform news_pos:
            pos (6,64)
            alpha 0.0
            ease 1.5 alpha 1.0

        image 1balloon = im.Scale("images/actseven/morningnews/1balloon_degenerate.webp", 960, 540)
        image 2balloon = im.Scale("images/actseven/morningnews/2balloon_degenerate.webp", 960, 540)

        show 1balloon at news_pos with dissolve

        pat "It appears a hot air balloon was repurposed and filled with helium.
            It was then latched to this man before being released."
        pat "It would seem this poor fellow was on the receiving end of a nasty prank."
        pat "The man flailed wildly and cried out desperately for help as our helicopter
            flew along beside him to capture these images."
        pat "We here at Hound News would never interfere with an ongoing criminal
            action due to legal remifications so we did not intervene."

        scene 2morningnews with dissolve

        show 2balloon at news_pos with dissolve

        pat "We were able to get quite close, however, and managed to witness the man
            black out several times from fear only to awaken still dangling in the sky."
        pat "Luckily authorities were able to rescue the man without incident."
        pat "Our sources tell us the man was in possession of a note and an old
            coin known as a {color=#b87333}Sixpence{/color}."

        scene 4morningnews with dissolve

        show 1balloon at news_pos with dissolve

        pat "We were not allowed to view the contents of the note but a trusted
            anonymous source sent us an alleged copy."
        pat "It reads; 'Dear Degenerate, you shouldn't have let slip your fear of heights.
            Keep your hands clean or next time I'll tie you to a rocket.'"
        pat "This man was recently charged with possession with intent to sell.
            An error in the case led to a dismissal of all charges."

        scene 5morningnews with dissolve

        show 2balloon at news_pos with dissolve

        pat "But it would seem someone wasn't ready to let it go that easily."
        pat "Will we be seeing more of this vigilante's unique brand of chastising?"
        pat "We'll keep you in the know. I'm Trish with Hound News, thanks for joining us."

        hide 2balloon

        scene 23morningseven with fadefast

        play music "audio/a_quiet_thought.mp3"

        a3 "That was wild! It sounds like the worst rollercoaster ride ever."
        a3 "Somebody must have been pretty upset with him to stage such an elaborate
            prank."
        a3 "Why'd you want to show this to me?"

        scene 25morningseven

        b "A sixpence is also known as a sixpenny."
        b "I was thinking... maybe..?"

        scene 24morningseven

        a3 "Come on, Uncle. Penny's a detective! She doesn't, you know, get her hands
            dirty like that."
        a3 "I'm sure she leaves the dangerous stuff to the police, right?"

        scene 25morningseven

        b "You don't know her like I know her. I've seen her do things, Avalon."
        b "First time I met her, she tased a man who looked similar to the guy we just saw on
            the news."
        b "And Evans just told her she can't assist the police anymore. But she's
            not one to listen to authority!"

        scene 26morningseven

        a3 "You're crazy, Uncle. Penny is too nice to strap someone to a rocket."
        a3 "But anyway! You have an appointment with Dr. Yu this morning so..."
        a3 "I thought I'd spend the day with Leah!"

        scene 30morningseven

        b "Oh. Is that what you were doing this morning on the computer? Looking for
            something for you two to do today?"

        a3 "Yeah!"

        b "Why didn't you let me tell her about us, yesterday?"

        scene 27morningseven

        a3 "I'm afraid when she finds out, she's going to hate me. I didn't want
            the first thing we spring on her to be something heartbreaking."
        a3 "I'll tell her, I promise! But I want to have a little time to get to
            know her first and let her get to know me."

        scene 32morningseven

        b "I was so awkward around her last night. I didn't know how to feel or
            what to say. I was in shock, I didn't think I'd ever see her again."
        b "She must have been so disappointed with me..."

        scene 28morningseven

        a3 "No she's not! I talked to her this morning, she's just waiting for
            you to stop being such a butt."
        a3 "After your appointment, there will be plenty of time for us all to
            talk and figure everything out."

        scene 31morningseven

        b "Ever the optimist. That might be my favorite thing about you, Avalon."
        b "Thank you for helping me through this."

        a3 "Of course! We're partners!"

        b "Yeah but I don't always feel like I'm pulling my weight. I sure disappointed
            you yesterday and--"

        scene 26morningseven

        a3 "Stop. Come on. I don't want to dwell on that. We talked about it and
            now we can move on."

        scene 29morningseven with dissolve

        a3 "Besides, I had so much fun last night. I can't stop thinking about it!"
        a3 "If only my stupid anxiety didn't kick in all the time!"

        scene 33morningseven

        b "You sure have an unusual fascination with sex, especially everything
            considered."
        b "But I had a lot of fun too. As long as you're comfortable and you're ready,
            maybe tonight we can--"

        scene 34morningseven

        l "Um, good morning. Sorry to interrupt. I'm all ready when you are."
        l "Hey, [player_name]."

        scene 35morningseven

        a3 "Hey, Leah! I didn't notice how toned your abs were yesterday."
        a3 "You must workou--"

        scene 36morningseven with dissolve

        a3 "Oh? [player_name]?"

        b "I'm sorry about last night, Leah. I am so glad you're back, I am!"

        scene 37morningseven with dissolve

        b "I'm not mad at you. And I hope you're not mad at me."
        b "I'm going through a lot right now and I don't always know how to handle
            things."
        b "I want you to be apart of our life, Leah. Of course I do! You're my [persistent.leah_rel]."
        b "Can you forgive me?"

        scene 38morningseven

        l "You... you look so different. And you act a little different than I remember
            too."
        l "I guess a lot happened while I was gone, huh?"

        scene 40morningseven with dissolve

        l "And you grew this funny beard. You look like a woodsman or a lumberjack."
        l "You kind of look like an old man with it, too. It adds 10 years at least!"

        b "No! You're just saying that to hurt me!"

        l "I like it. It fits you. You're a big hairy bear, you should look like one."

        scene 39morningseven

        b "Careful, Leah. Bears are prone to mauling pretty little redheads. Rawr!"

        l "You're more like a teddy bear."

        b "Yeah but like a monster teddy bear. Like a teddisaurus!"

        l "Maybe a cute and cuddly teddisaurus."

        b "Goodbye, masculinity!"

        scene 41morningseven

        a3 "Don't feed him affection, Leah. He feeds off it. He's a big ol' attention
            hog!"

        scene 42morningseven

        a3 "It goes straight to his head!"

        scene 43morningseven with dissolve

        a3 "Isn't that right, Uncle?"
        a3 "Oink oink!"

        scene 44morningseven

        l "Erm, sorry, I didn't mean to--"

        scene 45morningseven with dissolve

        l "We, um... we should go."

        a3 "Okay. We'll see you this afternoon, Uncle [player_name]."

        scene 37morningseven

        b "I'll, um... see you later then. Right?"

        scene 38morningseven

        stop music fadeout 2.0

        l "Yeah. See you later,"
        l "[player_name]."

        scene 1delivered with fade

        pause

        play sound "audio/doorknock.mp3"

        "*Knock* *Knock*"

        scene 2delivered with dissolve

        ben "Hm? Come in."

        play sound "audio/dooropen.mp3"

        ben "Oh, Penny. I've been expecting you for an hour, I'd almost given up
            hope you would arrive at all."
        ben "Were you delayed?"

        scene 3delivered

        play music "audio/sneaking_up_on_you.mp3"

        p "Good morning, Doctor. Yes, I was held up by a previous... entanglement."
        p "I apologize for keeping you waiting."

        scene 4delivered

        ben "Quite alright, quite alright. Please, Penny, I'd prefer not to delay."
        ben "Did you bring it? Do you have the artifact with you?"
        ben "You're not carrying anything. Were you unable to retrieve it?"

        scene 5delivered

        p "There was a complication with the item I promised you. But I won't disappoint
            you a second time, Doctor!"
        p "It just so happens that I was able to procure the item after all."
        p "And it's right..."

        scene 6delivered with dissolve

        p "Here!"
        p "Pretty groovy, right? To sneak it out, I had to--"

        scene 7delivered

        ben "Penny, what are you doing!? You put that in your pocket??"
        ben "That object is two thousand years old! And you've got your hands all
            over it!"
        ben "It's a ancient piece of history and you're waving it around like a toddler
            with a rattle!"

        scene 8delivered

        p "I gather it's supposed to be in a container of some sort?"
        p "I apologize! I didn't know! It's, you know, metal!"
        p "I figured it was durable. Like a steel rod or--"

        scene 7delivered

        ben "Maybe a few millenia ago it was durable! Please put it down on
            the table, Penny. Quickly!"
        ben "For the sake of my old heart, please set it down!"

        scene 9delivered

        p "Alright, alright! I just set it down right here? On this desk?"

        ben "Yes, quickly! Before you do any more damage to it?"

        scene 10delivered with dissolve

        ben "No, don't drop it! Set it do--"

        scene 11delivered with dissolve

        ben "I can't. I can't watch. Somebody pinch me, I must be dreaming.
            There is no way this is happening."

        p "I'm sorry! I don't know any better! You said to drop it so I dropped it.
            It's just a hunk of junk to me."
        p "Look, it's fine. Well, except for all the tarnish and the missing wooden
            handle shaft..."

        scene 12delivered

        ben "You would be the worst treasure hunter in the entire world, Penny!"

        p "Hey, I got the item so I can't be the worst!"

        ben "If there is a God, he is surely shaking his head at this clumsy attempt
            to preserve his holy artifacts."

        p "You'd think he would despise this thing if it was used to kill his son."

        scene 13delivered with dissolve

        ben "It most assuredly was not. There were tens of thousands of these
            created around the same time period."
        ben "There would simply be no way to definitively prove it's the geniune article
            even if by some miracle it were."

        p "So why are you getting so frazzled over it then?"

        scene 16delivered with dissolve

        ben "It's incredibly rare, Penny! And a significant historical find."

        scene 17delivered with dissolve

        p "It's just an old, rusted piece of garbage. You couldn't even smelt it down
            to make something better from it."
        p "Now you're going to place it on display with other junk and guard it
            with thousands of dollars worth of security."
        p "I'm sorry, Doctor, but I will never understand this practice."

        scene 16delivered

        ben "You don't have to understand it, Penny. But you must respect the fact
            that others do."
        ben "Now please, before we continue, tell me how you came into possession of this."
        ben "Was it obtained illegally? I know you like to bend the rules, Penny, but
            I don't want to be apart of anything illegal!"

        scene 14delivered

        p "The man that was in possession of it before is... {w} he's dead."
        p "I hadn't noticed before but, in hindsight, I believe he may have been
            depressed."
        p "The prank we played... I think it put him over the edge. He hanged himself
        yesterday."

        scene 15delivered

        ben "I see. I assume he did not register the finding of this item then."
        ben "I don't relish the idea that I was, in part, the cause of his demise
            but I did meet the man."
        ben "There is no question the world is a better place without him."

        scene 16delivered with dissolve

        ben "I appreciate you bringing this to me, all the same. It's easily worth
            ten times as much as the most valuable object we have here."

        scene 18delivered

        p "A check will be fine. You can make it out to {p}'{color=#b87333}Penny for Your Thoughts{/color}'."
        p "I'm also not opposed to an oversized sack of cash that I can carry around like a raccoon bandit
            from one of those old-timey cartoons."

        scene 19delivered

        ben "I don't have that kind of money, Penny! This is a museum, we take donations."
        ben "I assumed this was a donation."

        scene 20delivered

        p "Relax, Doctor Benson! Of course it's a donation. I can't imagine taking money
            for that old thing anyway."
        p "Maybe you can clean it up, smelt it down and make a toaster out of it or something."

        ben "A toaster?! You would destroy a piece of history to make a toaster!?"

        p "It would be more useful!"

        ben "I won't hear anymore of this, Penny. You're just being silly at this point."

        scene 21delivered with dissolve

        p "But this! I could understand keeping this around. Such a magnificent creature."
        p "Even death hasn't tarnished its beauty. Its bones alone can inspire an
            image of sheer power and dominance."

        scene 22delivered

        p "The earth shook under his mighty steps and when he would roar, creatures fled."
        p "This is surely the most fearsome creature to have ever walked the earth."

        scene 23delivered with dissolve

        ben "One could argue that people are more fearsome, Penny."

        p "One would be wrong! Our strength comes from our unity, our numbers. But the
            Tyrannosaurus rex is a singular destructive titan."
        p "Had twists of fate not intervened, this creature would never have allowed
            us to become what we are today."
        p "It took the universe itself to stop them!"

        ben "That is a fascinating way of looking at it, Penny. And I must admit,
            I'm rather fond of your vision of them."
        ben "I bet you're full of unique insights."

        scene 25delivered with dissolve

        ben "Here, this is for you. It's not much but it's everything I was able
            to save over the last year."

        p "I told you, Doctor, you don't owe me anything."

        scene 24delivered with dissolve

        ben "You saved my life a year ago and, more than that, you saved my family
            from having to go on without me."
        ben "Besides, this isn't for you. It's for the people you help."
        ben "I want you to use this towards that end."

        scene 26delivered with dissolve

        p "Alright, if you insist. I'll be sure it does not go to waste. Thank you,
            Doctor Benson."

        ben "No, thank you, Penny. For everything."

        stop music fadeout 2.0

        ben "Now I must attend to this new piece you've delivered."

        scene 27delivered with dissolve

        ben "Let me escort you out."

        if octavia == True:

            scene 1bcall with fade

            bi "{i}I can't explain it but I'm dreading this meeting with Dr. Yu
            this morning.{/i}"
            bi "{i}I feel like I'm showing all the sides of myself that I try so
            desperately to hide.{/i}"
            bi "{i}There's only a handful of people I feel comfortable enough
                showing those sides to.{/i}"
            bi "{i}Maybe one of those people can join me today..?{/i}"

            "*Ring*"

            bi "{i}I hope she's not busy today.{/i}"

            "*Ring*"

            play music "audio/tomorrows_rain.mp3"

            o2 "Good morning, [player_name]. How are you today?"

            scene 2bcall with dissolve

            b "Oh, hey. Good morning. I'm... well, something interesting happened last
                night."

            scene 4bcall with dissolve

            b "My [persistent.leah_rel] showed up in the middle of the night. I haven't seen her
                in six months."

            scene 5bcall with dissolve

            b "I actually thought she was dead..."

            o2 "That's wonderful, [player_name]! You must be so excited to see her
                after so long!"
            o2 "I don't believe you've mentioned her before."

            b "I'm sorry, I just... I didn't want to talk about it before."
            b "Now that she's back, there are some complications."

            o2 "Oh?"

            scene 4bcall with dissolve

            b "I could use your support today. If you have time, would you be
                willing to meet me at my therapist's office?"

            o2 "Last time Avalon and I waited for you, [player_name], you left
            us after your session."

            scene 3bcall with dissolve

            b "Yeah, that was kind of a dick move. Sorry about that!"
            b "But this time I'd like it if you went into the session with me."

            scene 5bcall with dissolve

            b "I'm feeling a bit uncomfortable with the whole... therapy thing."

            o2 "I'd love to join you, [player_name]. Of course I'll join."

            scene 6bcall with dissolve

            stop music fadeout 2.0

            b "Okay, great. Thank you, Octavia."
            b "Can you be there in half an hour?"

            o2 "Sure! I'll see you soon!"

            jump karts

        else:

            scene 1bcall with fade

            bi "{i}I can't explain it but I'm dreading this meeting with Dr. Yu
            this morning.{/i}"
            bi "{i}I feel like I'm showing all the sides of myself that I try so
            desperately to hide.{/i}"
            bi "{i}There's only a handful of people I would be comfortable
                showing those sides to.{/i}"
            bi "{i}Maybe one of those people can join me today..?{/i}"

            "*Ring*"

            bi "{i}She's not working right now so she shouldn't be busy today.{/i}"

            "*Ring*"

            play music "audio/disturbed_mind.mp3"

            d "Hey, [player_name]! What's the haps, man?"

            scene 2bcall

            b "Hey, Dallas. Took you long enough to answer the phone."
            b "You're not getting all fat and lazy now that you're out of a job,
                are you?"

            scene 6bcall with dissolve

            d "Dude, I am seriously going crazy with nothing to do. I'm antsy as hell!"
            d "I'm just gettin' my tan on right now, trying to relax and enjoy the vay-kay."
            d "But I'm not going to lie, it's the worst. I need purpose, [player_name]! I need--"

            scene 7bcall with dissolve

            b "Getting a free salon must be very difficult for you, Dallas."
            b "Let me just play the world's tiniest violin for you."

            d "Says the pot!"

            scene 3bcall with dissolve

            b "Listen, if you want something to do today, I wouldn't mind a little
                company during this therapy session I have today."

            scene 5bcall with dissolve

            b "I, uhh... had a surprise visitor last night and it's bringing a lot
                of feelings back to the surface."
            b "These sessions make me uneasy though."

            d "I'd love to help you out, [player_name]!"

            scene 4bcall with dissolve

            b "Really? You're not too busy drying your nails or waxing your butt hairs?"

            scene 6bcall with dissolve

            d "I don't have any butt hairs! What kind of women have you been with
                that have butt hairs?!"
            d "Where do you pick up girls, [player_name]? The circus?"

            stop music fadeout 2.0

            b "Can you meet me at the therapist's office in half an hour?"

            d "You got it, buddy!"

            jump karts

    label karts:

        scene 1karts with dissolve

        play music "audio/soft_reminder.mp3"

        a3 "Here we are!"

        l "Oh! This looks incredible, Avalon! What a great idea."

        a3 "I didn't expect it to be so big. The pictures online
            made it look a lot smaller!"

        scene 2karts

        l "How is it empty though?"

        a3 "Well, I rented it out for just the two of us so that we can have it
            all to ourselves."

        l "That must have been expensive."

        a3 "Nope! It's a weekday so most people are at work. We got it for a steal!"

        scene 3karts

        sid "Hey there! I'm Sidney, you two must be--"

        scene 4karts

        a3 "Witchcraft! Where the crap did you come from?!"

        l "Seriously, I didn't even hear footsteps. Did you hover over here
            like a phantom??"

        a3 "Don't do that! I think I peed a little..."

        scene 6karts

        sid "I apologize, ladies. I didn't mean to startle you."
        sid "You'll have the tracks all to yourselves today but I'm here to show you
            the ropes and make sure you stay safe."
        sid "Have you girls been here before?"

        scene 5karts

        a3 "Nope! First time for me."

        l "I've done bumper cars before but nothing like this."
        l "Is it different?"

        scene 6karts

        sid "These go a bit faster than bumper cars and it's imperative that
            you try not to run into each other on the tracks."

        scene 7karts with dissolve

        sid "Are you girls ready to have some fun?"

        scene 8karts

        l "Heck yes! I'm fired up!"

        a3 "This is gonna be epic."

        stop music fadeout 1.0

        scene 9karts with fadefast

        sid "There's a few things I want to go over with you before we begin."

        scene 10karts with dissolve

        sid "Go Karts typically can reach speeds of forty-five miles per hour or faster."
        sid "We throttle our Karts down to thirty miles per hour for saftey reasons.
            We generally cater to a younger demographic."

        scene 11karts

        a3 "Okay, thirty miles per hour still seems pretty fast. I sure can't run
            that fast!"

        l "Yeah, I'm fine with that speed."

        scene 10karts with dissolve

        sid "So let's get you guys into a Kart and I'll explain how everything
            works inside your vehicles."

        a3 "Roger that!"

        scene 12karts

        a3 "Hmm. Let's see here. I just... climb in--"

        play music "audio/bored_to_death.mp3"

        scene 13karts with dissolve

        l "Oh, Avalon. Before we start, I just wanted to say that..."

        scene 14karts with dissolve

        l "You're gonna be eatin' my exhaust today, girlfriend."
        l "You're going down!"

        ai3 "She's competitive!? I love it."

        scene 15karts

        a3 "Oh, Leah, can you hang on for just a moment?"
        a3 "I'd like to practice my victory dance for when I inevitably cross
            the finish line before you."

        show kart_dancing

        a3 "Don't worry if you miss some of these moves, Leah."
        a3 "You'll be seeing this dance again real soon."

        l "Damn, Avalon, you got the smack talk down! I might have to take notes."

        sid "You girls are quite a pair."

        scene 17karts

        sid "Go ahead and get situated inside your vehicles. Don't worry if you press
            on the pedals, the karts are not powered on yet."

        l "Let's see if I can squeeze in here..."

        a3 "It looks like it's the perfect size for me."

        scene 18karts with dissolve

        l "Ugn. This must be made for kids. I can barely fit in it."

        a3 "Really? I'm quite comfortable."

        l "Maybe I'm just a fat cow."

        a3 "Sexiest fat cow I've ever seen..."

        scene 48karts with dissolve

        l "W-what? What'd you say?"

        menu:
            "{b}Additional Dialogue Choice{/b}"

            "Truth":
                a3 "Er, well, you have weight in all the right places. It actually
                    makes you sexy."
                a3 "I'm pretty jealous. I hope that doesn't weird you out?"

                l "Oh, no. That's alright. I think... you're pretty sexy too."

            "Lie":
                a3 "I said 'For the Motherland!'. I'm part Russian, we say that
                    sometimes."

                l "Really?!"

                a3 "No, not really. I just didn't want you to know what I said."

                l "Oh, alright. Keep your secrets then."

        scene 20karts with dissolve

        sid "The pedal on your right is the 'Go' pedal and the one on the left
            is the 'Stop' pedal."
        sid "To go in reverse, slide your foot under right pedal and pull it up."

        scene 21karts with dissolve

        sid "You got it?"

        a3 "Yeah! It seems simple enough. Thanks, Sidney!"

        sid "You're welcome. Let me help out Leah and we'll get you two started."

        a3 "Okay!"

        scene 22karts

        sid "Use the right pedal to accelerate and the left pedal to brake."
        sid "Slide your foot under the right pedal and pull up to go in reverse."

        scene 23karts with dissolve

        sid "Any questions before we start?"

        l "Nope! Seems simple enough. Thanks, Sidney!"

        sid "Excellent. Let's get this race started."

        scene 24karts with dissolve

        sid "Alright, girls. Remember to try not to bump into each other."
        sid "On your mark, get set..."

        scene 25karts with dissolve

        sid "Go!"

        a3 "Woohoo!"

        l "It's on, Avalon!"

        scene 26karts

        a3 "What the..? Is your kart faster than mine!? How'd you do that?"

        l "All skill, girlfriend! All skill!"

        scene 27karts

        a3 "I guess your kart isn't as fast as I thought, Leah!"
        a3 "Eat my dust!"

        l "Don't count your chickens before they hatch!"

        scene 28karts

        l "Did that wall slow you down, Avalon?"

        a3 "It came out of nowhere!"

        scene 31karts

        sid "And the winner is..."

        scene 32karts with dissolve

        sid "Avalon by a nose!"

        l "What!? No way!"

        a3 "Toot toot! Victory train coming through, Leah!"

        scene 27karts

        stop music fadeout 2.0

        ai3 "{i}Leah and I raced a few more rounds. In the end, we ended up
            tied for wins.{/i}"
        ai3 "{i}I ended up seeing what Uncle saw in her. And I understood why
        he was so upset when she was gone.{/i}"

        stop music fadeout 2.0

        ai3 "{i}He doesn't bond with many people so when he does,
            they must be really special.{/i}"

        scene 33karts with fadefast

        l "Avalon, this has been so much fun. Thank you for bringing me here."
        l "I needed something like this. Work was rough, seeing [player_name] was
            stressful. This was the perfect remedy."

        play music "audio/soft_reminder.mp3"

        a3 "You're welcome!"

        l "I didn't expect you to be so competitive though! You seem so sweet
            and innocent."

        scene 34karts with dissolve

        a3 "I was a cheerleader! We had lots of cheer competitions. It was more
            competitive than you might think."

        l "That makes sense. You seem like you would make a great cheerleader."
        l "Rah rah, shish kebab!"

        a3 "Our cheers were a little different than that..."

        scene 35karts with dissolve

        l "Can you tell me about the last few months that I've missed? How is [player_name]?
            When did you and him reignite your relationship?"

        scene 41karts

        a3 "We only just reunited about a week ago. We had been apart for
            years before that."
        a3 "I thought maybe he'd have changed but he's the same ol' Uncle
            [player_name]!"

        scene 36karts

        l "Yeah? I guess he's always been a bit of a goofball, huh?"
        l "Him and I only got to know each other a little over a few months.
            I like his silly humor but he's also very sweet."

        a3 "He totally is."

        l "So, what drew you guys back together?"

        scene 44karts

        a3 "A few months ago, one of my mom's booty calls snuck into my room and..."
        a3 "He took advantage of me."
        a3 "I started to resent my mom after that. In a big way, I blamed her for it."
        a3 "Eventually, I ran away from home and [player_name] came to my rescue."

        scene 38karts

        l "H-he... raped you?"

        a3 "Y-yeah. I'm... recovering."

        scene 37karts with dissolve

        l "I can't imagine what that must have been like, Avalon."
        l "Did you... are you... okay?"

        scene 45karts

        a3 "I'm not the same. That man took something from me and I know
            I'll never get it back."
        a3 "There will always be a piece of me that's broken."

        scene 44karts with dissolve

        a3 "But I've had supportive friends and family. And [player_name] has been--"
        a3 "Well, Leah, I need to tell you something about [player_name] and I."

        scene 37karts

        l "You're together, aren't you?"

        a3 "How did you--?"

        l "He started to tell me yesterday just before you intervened. I knew what
            he was going to say."
        l "He could love you, his niece, but... he couldn't love me."

        scene 42karts

        a3 "I don't think that's it at all!"
        a3 "He told me that he rushed things with me because he regretted running away
            from you. He didn't want to make the same mistake."
        a3 "I think if you would have just given him time to process..."

        scene 38karts

        l "You... you think so?"

        scene 37karts with dissolve

        l "Well, I guess it doesn't matter now."

        if polygamy == True:

            if octavia == True:

                scene 41karts

                a3 "I wouldn't say that. [player_name] and I are dating someone you haven't
                    met yet. Her name is Octavia."
                a3 "So we're open to the idea of a less traditional relationship."
                a3 "I'm not saying we have to jump into anything but the
                    possibility is there!"

                scene 38karts

                l "That does sound unusual. I don't know if that would be
                    something I would be interested in."
                l "But then again, I've never really considered it."
                l "Would that mean that you and I would--"
                l "Er, you know, also be involved?"

                scene 43karts

                a3 "Absolutely. And Octavia too! I know it sounds overwhelming to
                    imagine it but I've had so much fun sexually lately."
                a3 "There are worlds of pleasure that we're only just beginning
                    to explore with each other."
                a3 "And you're, like, freakishly hot and fun and smart! I'm sure
                    you'd fit right in with us."

                scene 39karts

                l "Well, you're not shy at all. Just laying it all right out there,
                huh?"

                scene 37karts with dissolve

                l "I didn't expect you to be so sexually active. Is that unusual
                    for someone whose been abused?"

                scene 44karts

                a3 "I've had trouble understanding it myself. Ever since I started
                dating [player_name], sex is almost all I think about."
                a3 "It's like if I can enjoy sex, then that man that raped me doesn't
                    win."
                a3 "It's silly, I know. I can't explain why I'm connecting it that way."
                a3 "But it's working for me. [player_name] and I are taking it slow, we havent
                    had sex yet."
                a3 "Octavia and I are only playing around pretty mildly so far."

                scene 38karts

                l "I can see that you don't like to disappoint people, Avalon."
                l "But you can't just invite me into something like that right away."

                scene 37karts with dissolve

                l "I mean, I'm not saying 'No' but I... I haven't even met Octavia."

                scene 41karts

                a3 "Okay! First step, we'll meet Octavia! And then we'll go from there!"

                a3 "I didn't mean to throw all that at you right away but you're right,
                I don't want to see you disappointed."
                a3 "No matter what though, you're [player_name]'s only [persistent.leah_rel]
                so I want us to be close."

                scene 36karts

                l "I'd like that too, Avalon. I'm disappointed that I missed
                    my chance with [player_name]."
                l "But that doesn't mean I want us to be anything less than good
                    friends."

                scene 37karts with dissolve

                l "I wouldn't mind meeting your partner, Octavia, though."

                scene 41karts

                a3 "I'll see if she's available to come over today."

                stop music fadeout 2.0

                a3 "But we better get out of here, our time is about up."
                a3 "Let's go see if [player_name] is back from his therapy session."

                jump precube_octavia

            else:

                scene 41karts

                a3 "I wouldn't say that. [player_name] and I are dating someone you haven't
                    met yet. Her name is Dallas."
                a3 "So we're open to the idea of a less traditional relationship."
                a3 "I'm not saying we have to jump into anything but the
                    possibility is there!"

                scene 38karts

                l "That does sound unusual. I don't know if that would be
                    something I would be interested in."
                l "But then again, I've never really considered it."
                l "Would that mean that you and I would--"
                l "Er, you know, also be involved?"

                scene 43karts

                a3 "Absolutely. And Dallas too! I know it sounds overwhelming to
                    imagine it but I've had so much fun sexually lately."
                a3 "There are worlds of pleasure that we're only just beginning
                    to explore with each other."
                a3 "And you're, like, freakishly hot and fun and smart! I'm sure
                    you'd fit right in with us."

                scene 39karts

                l "Well, you're not shy at all. Just laying it all right out there,
                huh?"

                scene 37karts with dissolve

                l "I didn't expect you to be so sexually active. Is that unusual
                    for someone whose been abused?"

                scene 44karts

                a3 "I've had trouble understanding it myself. Ever since I started
                dating [player_name], sex is almost all I think about."
                a3 "It's like if I can enjoy sex, then that man that raped me doesn't
                    win."
                a3 "It's silly, I know. I can't explain why I'm connecting it that way."
                a3 "But it's working for me. [player_name] and I are taking it slow, we havent
                    had sex yet."
                a3 "Dallas and I are only playing around pretty mildly so far."

                scene 38karts

                l "I can see that you don't like to disappoint people, Avalon."
                l "But you can't just invite me into something like that right away."

                scene 37karts with dissolve

                l "I mean, I'm not saying 'No' but I... I haven't even met Dallas."

                scene 41karts

                a3 "Okay! First step, we'll meet Dallas! And then we'll go from there!"

                a3 "I didn't mean to throw all that at you right away but you're right,
                I don't want to see you disappointed."
                a3 "No matter what though, you're [player_name]'s only [persistent.relationship]
                so I want us to be close."

                scene 36karts

                l "I'd like that too, Avalon. I'm disappointed that I missed
                    my chance with [player_name]."
                l "But that doesn't mean I want us to be anything less than good
                    friends."

                scene 37karts with dissolve

                l "I wouldn't mind meeting your partner, Dallas, though."

                scene 41karts

                a3 "I'll see if she's available to come over today."

                stop music fadeout 2.0

                a3 "But we better get out of here, our time is about up."
                a3 "Let's go see if [player_name] is back from his therapy session."

                jump precube_dallas

        else:

            scene 45karts

            a3 "Please don't hate me, Leah. I didn't mean to take him away from
                you."
            a3 "I didn't even know about you until a few days ago."
            a3 "[player_name] and I didn't plan this. I think we both just needed
                a strong relationship so we sort of... fell into each other."

            scene 44karts with dissolve

            a3 "It happened fast, but we both needed the healing power
                of a strong relationship."
            a3 "I don't know where either of us would be without each other right now."
            a3 "You're important to [player_name], Leah. So you're important to me.
                I want you to be apart of our life."

            scene 38karts

            l "I guess you've both had a pretty rough life, huh?"
            l "Well, I am disappointed that I missed my chance with [player_name]."
            l "But maybe it will ultimately be the best this way."

            scene 37karts with dissolve

            l "It will take me some time to come to terms with this but I do
            still want to be a part of [player_name]'s life."
            l "And I'd like to get to know you better too."

            scene 41karts

            stop music fadeout 2.0

            a3 "You have no idea how great that is to hear, Leah. I was so nervous
                about this!"
            a3 "Let's head home so you can spend more time with [player_name]!"
            a3 "Come on!"

            if octavia == True:
                jump precube_octavia
            else:
                jump precube_dallas


    label precube_octavia:

        if polygamy == True:

            scene 1octprecube with fade

            bi "{i}How does she just show up at my doorstep like that?{/i}"
            bi "{i}If she hadn't run away six months ago, where would my life be
            right now?{/i}"
            bi "{i}Would her and I have dated? Would she have pushed me to
                reconnect with Avalon sooner?{/i}"
            bi "{i}Would Avalon have stayed over with Leah and I at my house when
                Sharol had Tyler over?{/i}"
            bi "{i}The possibilities if she hadn't left are wreaking havoc on my mind.{/i}"
            bi "{i}If there's one person that can help me through this chaotic
            thinking, it's certainly--{/i}"

            scene 3octprecube

            play music "audio/tomorrows_rain.mp3"

            o2 "[player_name]? You look lost in thought. Where are you
                right now?"

            scene 2octprecube

            b "Octavia. I was just thinking about you, actually. A lot has happened
                in the last twenty-four hours."
            b "I could use your support right now. Will you sit with me?"

            o2 "Of course, [player_name]."

            scene 4octprecube with dissolve

            b "You look especially lovely today, Octavia. I love your outfit."

            o2 "Oh I cherish your compliments, [player_name]. Thank you for that."
            o2 "So tell me about your [persistent.leah_rel], Leah. You said she showed up last
                night?"
            o2 "Why haven't you mentioned her before?"

            scene 13octprecube with dissolve

            b "Well, I spent several months with her and then she wanted more
                from our relationship. She wanted something intimate."
            b "I just didn't know how to react so I panicked and ran."

            scene 11octprecube with dissolve

            b "I couldn't find her after that. She was just gone. I thought I'd
                never see her again."
            b "But last night, she just showed up out of the blue. I can't seem
                to process my feelings about everything now."

            o2 "Where did she go that you couldn't find her?"

            scene 13octprecube with dissolve

            b "A business endeavor of some sort. A research and development
                project."
            b "From what I understood, they didn't let her contact anyone while
                the project was in development."

            scene 5octprecube

            o2 "Everyone reacts to rejection in different ways. Many people
                fear it so much that when it happens, it activates their fight
                or flight response."
            o2 "I hope you don't hold it against her for running away. Our primal
                instincts can be quite powerful and out of our control."
            o2 "As for where she will fit into your life now that she's back,
                there's plenty of room in our circle for her. Of course there is!"

            scene 11octprecube

            b "I just can't stop thinking about what life would be like if
            I hadn't rejected her."
            b "Avalon and I might not have gotten together but maybe she wouldn't
            have been attacked?"
            b "Then again, I also wouldn't have met you..."
            b "My brain is spinning."

            scene 8octprecube

            o2 "I can see that. Your heart rate is elevated trying to keep your mind
                in supply of energy for all those thoughts."

            scene 5octprecube with dissolve

            o2 "Let me put it at ease for you; the universe simply doesn't work like that."
            o2 "Every decision you make is based off of your previous experiences.
                And all your previous experiences are consequences of previous choices."
            o2 "If you rewind time right now and press play, the exact same thing
                would happen because every consequence of choice leads into your next decision."
            o2 "Our lives are a domino effect; a chain reaction of decisions leading to
                consequences leading to decisions."
            o2 "Time only has one path for us, [player_name]. We're just along for the ride."

            b "Y-you mean fate?"

            scene 8octprecube with dissolve

            o2 "In so many words."
            o2 "But my point is that regret is not useful. Persevere and make
                the best decisions with the information you have moving forward."
            o2 "That's all any of us can do. We can't change the past."
            o2 "You have a second chance with your [persistent.leah_rel], [player_name]. Don't
                waste it lamenting over past decisions that you can't change."

            scene 9octprecube

            b "Okay, yeah. I understood some of that. I should take this opportunity
                to bring her into my life."
            b "Avalon is getting along with her so well but that's no surprise."
            b "She's a walking positive charge!"

            scene 7octprecube

            o2 "I'm glad you and Avalon worked everything out. No more secrets between
                you and her, alright?"

            b "No more secrets. I promise!"

            o2 "How are you handling the incident with your father? Avalon told
                me you found him deceased in his office?"

            scene 11octprecube

            b "It was a horror to see. I've never seen a man hanged like that.
                The slight swaying of his lifeless body..."
            b "It's haunting, to say the least."
            b "But I'm taking it rather well, all things considered. I'm more
                worried about Penny."

            scene 6octprecube

            o2 "Penny? She was there?"

            b "Y-yeah, she found him. She was crying when I walked in."

            o2 "Oh that's terrible. Penny doesn't handle death well."

            scene 13octprecube

            b "Yeah, she seemed unusually upset. I could tell she felt guilty for
                his death."
            b "We actually bonded yesterday. I consoled her after she found Gladstone
                and she helped me when Avalon left."

            scene 10octprecube with dissolve

            b "Actually, I saw on the news earlier that some guy--"

            scene 8octprecube

            o2 "I saw it too. I don't know what that girl is up to."
            o2 "I'm going to have to chastise her later."

            b "She left behind a coin?"

            o2 "Penny joined a community of children back where she's from when
                she was nine. They used to call her Sixpence."
            o2 "Apparently when they found her, that's all she had on her. A single
                coin. A Sixpence."
            o2 "My guess would be that she left one behind as a signature."
            o2 "But let's keep all that between us."

            scene 12octprecube

            b "That girl is something else."

            o2 "Isn't she?"

            scene 5octprecube

            o2 "Did you know she came over to America by stowing away on a U.S.
                Navy Aircraft Carrier. I don't even know how she got on to it."
            o2 "The darn thing never made port near where she'd come from!"
            o2 "She was hiding so well, I should never have found her. But by a stroke
                of luck, I sure did."
            o2 "I could tell right away she just wanted passage. So I talked with her
                for a while and ended up helping her sneak into our country."
            o2 "I pulled some strings, got her the documents she needed to be here
                legally and everything else is history."

            scene 10octprecube

            b "It sounds like there's a lot about Penny I don't know."
            b "Are you sure she's not an alien or a super spy or something?"

            o2 "I'm positive!"

            scene 9octprecube with dissolve

            b "You really take care of people, huh?"
            b "You truly are an incredible woman, Octavia."

            if polygamy == True:

                scene 14octprecube with dissolve

                b "Would you stand with me?"

                o2 "Oh? If you'd like, [player_name]."
                o2 "Was there a specific reason?"

                b "There is."

                scene 15octprecube with dissolve

                o2 "Mm!"

                scene 16octprecube with dissolve

                o2 "You're taking the initiative today."

                b "This last week has been trying and emotional. But you've always
                    been the one person I can always lean on."
                b "My life is immeasurably better with you in it."

                o2 "That's an awfully sweet thing to say. But it goes both ways."
                o2 "I felt so empty when Penny and I parted. Being with you is the
                    first time I've felt whole since."

                b "Well I think that calls for another kiss."

                scene 15octprecube with dissolve

                pause

                scene 17octprecube

                sun "Uh oh. Somebody got caught with their hands in the cookie jar."
                sun "Or tongue, as it were!"
                sun "I didn't take you for the cheating type, Mr. [player_name]."

                scene 18octprecube

                b "It's not what you think! I mean, well, it is what you think."
                b "But it's... complicated. You see, the thing is..."
                b "Well, here's what--"

                scene 19octprecube with dissolve

                o2 "Avalon, [player_name] and I are in a polyamorous relationship."
                o2 "That means we're all intimate with each other in a three-way
                    relationship."
                o2 "We're still working out all the details but we're always open
                    and honest with each other."

                scene 21octprecube

                sun "What!? Is that a real thing? You guys all bang each other
                    all the time!?"

                o2 "That's not quite--"

                scene 22octprecube with dissolve

                sun "Can I join!? Please?? You can do whatever you want to me!"

                scene 20octprecube

                b "That's a strange response."

                o2 "It's a little more complicated than that."
                o2 "Are you feeling lonely, Sun Mei?"

                scene 22octprecube

                sun "Nope! I just really want to have sex!"

                o2 "Is that so?"

                scene 24octprecube with dissolve

                o2 "Would you mind if I put my hand on you, Sun Mei?"

                sun "Not at all! You can touch me where ever you want!"

                scene 25octprecube with dissolve

                sun "Oh. Your hands are warm. You can move down, if you want."

                o2 "Not subtle at all, are you?"
                o2 "Sun Mei, have you been having dreams?"

                sun "Mm, yeah! Almost every night there's a girl that crawls into
                    my dream and we do bad things together!"

                o2 "I see."

                scene 23octprecube with dissolve

                o2 "Do you feel like you're being sexually repressed at home, Sun
                    Mei?"
                sun "I'm not supposed to touch myself but it makes me want to do
                    it even more!"
                o2 "That's what I thought. Let me give you my number. Call me
                    tomorrow, alright?"
                sun "Really!? Alright, yeah, I'll do that! Thank you, mysterious
                    lady!"

                scene 24octprecube with dissolve

                stop music fadeout 2.0

                sun "I can take you to see my gran-- I mean, Dr. Yu now."

                o2 "Thank you, Sun Mei."

                jump thecube_octavia

            else:

                scene 17octprecube

                sun "I hope I'm not interrupting anything."
                sun "Dr. Yu is ready to see you now."

                scene 18octprecube

                b "Oh, it's time already?"
                b "I thought we had a little longer. Time, uh, time flys, doesn't it?"

                scene 19octprecube with dissolve

                o2 "[player_name] is a little nervous today. It's been a trying
                    few days."
                o2 "But we're ready."

                scene 21octprecube

                sun "There's nothing to worry about! Grandpa is skilled
                    at his job!"

                scene 22octprecube with dissolve

                stop music fadeout 2.0

                sun "And he's got something special planned for you today."
                sun "Most people love it! Come on, I'll take you to him."

                o2 "Thank you, Sun Mei."

                jump thecube_octavia

    label thecube_octavia:

        play music "audio/plastic_dragon.mp3"

        scene 1octtherapy with fade

        dr "It is nice to see you again, [player_name]. And I see you have brought
            a friend with you today?"

        scene 6octtherapy

        b "I did. This is Octavia. Is it alright that she sits in with me on this?"
        b "Yesterday's session left me a little uncomfortable. She has an uncanny
            ability to calm me down so I asked her here today."

        scene 1octtherapy

        dr "Of course, [player_name]. It is your session, after all."

        scene 2octtherapy with dissolve

        dr "It is nice to meet you, Ms. Octavia."

        o2 "It's a pleasure to meet you as well, Doctor."

        dr "May I inquire about you before we begin? Can you tell me about yourself?"

        scene 7octtherapy

        o2 "Sure, I don't mind at all. I went into the military right after I graduated
            High School."
        o2 "I had a natural talent at reading people's emotions so when I expressed
            an interest in foreign relations,"
        o2 "I was granted access to special classes at Westpoint."
        o2 "After four years, I began working as a diplomat in the United States
            Air Force. I retired nearly a year ago."

        scene 2octtherapy

        dr "It would seem you've had led an exciting life, Ms. Octavia."
        dr "Four years is a lot of time to train to retire so early."

        scene 8octtherapy

        o2 "I traveled to many countries and I saw vast diversity, conflict and
            hardships."
        o2 "I went into the military to improve the world but I must confess,
            the endeavor felt... fruitless."
        o2 "I wondered if my influence could be more beneficial in a more concentrated
            area. So I retired from the military and began undertaking smaller goals."
        o2 "I rescued a panther who is now my loyal companion. I helped and subsequently
            fell in love with a beautiful young woman."
        scene 9octtherapy with dissolve

        o2 "And now I'm building a relationship with [player_name] and Avalon."

        b "Whose lives you've made immeasurably better. I can attest to that!"

        o2 "Thank you, [player_name]."

        scene 7octtherapy with dissolve

        o2 "I've found new purpose and it's been profoundly rewarding."

        scene 2octtherapy

        dr "I must say, I have found much the same to be true for myself as well."
        dr "I am happy to hear that you are happy."

        scene 1octtherapy with dissolve

        dr "You seem to have yourself a wonderful friend, [player_name]."
        dr "Tell me, how have you been since we last spoke?"

        scene 5octtherapy

        b "W-well, actually, after our session yesterday, I went and found my father
            had hanged himself."
        b "And Leah, my [persistent.leah_rel] that I told you about, showed up at my doorstep
            at midnight."
        b "It's... it's been a chaotic twenty-four hours."

        scene 4octtherapy

        dr "That must have been difficult to bear witness to."
        dr "Life seems to be relentless in providing you trials, [player_name]."
        dr "How did your reunion with your [persistent.leah_rel] go?"

        scene 5octtherapy

        b "Not as well as it should have. She was on some sort of secret business
            trip and didn't tell me."
        b "I just... I feel like she..."

        scene 4octtherapy

        dr "Abandoned you?"

        b "Y-yeah."

        dr "[player_name], I would like to try something. It's a personality test
        that will help me better understand you."
        dr "It can also help you better understand yourself."
        dr "It will require you to be in a relaxed state. Is this something you
            would be willing to try?"

        b "If you think it would help."

        scene 3octtherapy with dissolve

        dr "May I ask for your assistance if I require it, Ms. Octavia?"

        o2 "Of course."

        scene 6octtherapy

        b "I guess I'll need to be laying down for this?"

        dr "That is correct."

        scene 9octtherapy with dissolve

        b "Would you mind if I use your lap for my head?"

        o2 "Not at all, [player_name]."

        scene 10octtherapy with dissolve

        o2 "Are you comfortable?"

        b "Very."

        scene 11octtherapy with dissolve

        dr "Let us begin. [player_name], please close your eyes and focus on my
            words."

        b "Alright."

        scene 12octtherapy with dissolve

        dr "Can you feel the warmth of the sun on your skin?"

        b "Mhmm."

        dr "I want you to imagine that you are in a desert. A vast plane of
            sand and rocks."

        scene 2thecube with fadefast

        dr "Can you see it?"

        scene 3thecube with dissolve

        b "Yes. I can see it. It looks as though it's almost dusk, the sun is about to set."
        b "There's a surprising amount of greenery here. Most of the plants
            are managing to survive despite the heat and lack of water."

        dr "Everything within your desert will have meaning, [player_name]. Perhaps
            the surviving plant life represents your own perseverance."
        dr "Look around yourself. See if you can find a cube. And when you do,
            describe the cube to me."

        scene 4thecube with dissolve

        b "I don't see any cubes. Mostly just rocks. Is it supposed to be buried?"

        dr "Where the cube is, [player_name], is up to you to decide."

        b "I guess I could look around a bit. Maybe it's--"

        scene 5thecube with dissolve

        b "Oh! Okay, yes. There is a cube here."

        dr "How large is it? What's it made of? Where is it in relation to yourself?"

        scene 6thecube

        b "It must be about 3 feet tall. It looks like it's made out of copper."
        b "I can't imagine it weighing less than a ton but it's floating in the
            air as if it's weightless."
        b "As if the laws of physics don't apply to it. It's defiant and doesn't
            adhere to the rules."

        o2 "And it's made of copper? Could you be picturing Penny, [player_name]?"

        dr "The cube is supposed to represent yourself."
        dr "Is it possible--"

        b "Wait wait, it's changing. I can... I can see into it."

        scene 7thecube with dissolve

        b "There's another cube inside it. A smaller cube made of brick."
        b "It's like the copper cube is protecting the square made of bricks."

        o2 "You've built walls to protect yourself. But you still feel small
            and vulnerable, don't you, [player_name]?"
        o2 "And Penny has taken care of you lately."

        b "She has. I don't know if I could have made it through yesterday
            without her."
        b "And she put that scumbag that hurt Avalon behind bars. Something I couldn't
            do."
        b "She's really taken care of us."

        dr "[player_name], look around once more. See if you can find a ladder."

        scene 8thecube with dissolve

        b "Okay, yes. There's a ladder here."

        dr "Where is it in relation to the cube."

        b "Across from it. They're apart."

        dr "The ladder represents your goals, [player_name]."
        dr "As it is away from yourself, your goals may involve taking care of
            others rather than prioritizing yourself."
        dr "That's very--"

        scene 9thecube with dissolve

        b "Octavia!?"

        o2 "Yes, [player_name]?"

        b "No, I mean, you're here at the top of the ladder."

        scene 11thecube

        b "You're reaching out to me, trying to help pull me up the ladder."
        b "But... but you're glowing. You have great big white wings and a golden
            halo."

        o2 "[player_name] has compared me to an angel on multiple occassions."
        o2 "I imagined it was just compliments but I guess that's how you genuinely
            see me. I'm truly flattered."

        dr "Octavia has been a guiding hand for you, has she?"
        dr "You must reciprocate that generosity. Be sure you
            are there for her as well."

        b "I... I will. I've been so distracted lately but she deserves more from
            me."

        o2 "Oh, [player_name]. You've given me more than you know."

        dr "I want you to look around once more. Is there a horse in the distance?
            Or nearby, perhaps?"

        scene 12thecube

        b "A horse in the desert? I can't imagine--"

        scene 13thecube with dissolve

        b "Woah. It's... not a horse. At least, not entirely. It's a girl with
            the body of a horse."

        o2 "A centauride, [player_name]? That's quite an unusual thing to conjure."

        dr "Please, describe this creature to us."

        b "There's something so familiar about her. I can't quite place it."
        b "She's timid, she's afraid of me. I don't think she's had good experiences
            with people like me in the past."

        scene 14thecube with dissolve

        b "It's okay, I won't hurt you. It's a big world out there. Maybe we can
            help each other?"
        b "What do you say? Can you trust me?"

        scene 15thecube with dissolve

        b "She's an exceptionally beautiful creature, to be sure. She doesn't appear
            to be very trusting but I think she's warming up to me."

        dr "Can you tell me why she's afraid of you, [player_name]?"

        b "She's been hurt before. She's not like other people, she's... unique.
            Special."

        scene 16thecube with dissolve

        b "She's letting me get closer to her. It doesn't seem she sees me as a
            threat anymore."

        dr "Are there any flowers that stand out? Growing out of the ground or
            perhaps somewhere else?"

        scene 17thecube with dissolve

        b "Oh, y-yes! They're in her hair."

        b "It's like when she's happy, they blossom and flourish. When she's
            scared or sad, they wilt and disappear."
        b "She rejects them when she's unhappy."

        scene 18thecube with dissolve

        b "She's taken to me all of the sudden!"

        stop music fadeout 2.0

        b "I feel a connection between us. We're... we're somehow meant for each other."
        b "And now that she's happy, the flowers have started to bloom."

        scene 19thecube

        b "S-something startled her! She's uneasy, agitated."
        b "Hey, it's alright. Nothing is going to hurt you."
        b "I'll protect you."

        play sound "audio/arrow_body.mp3"

        scene 20thecube with vpunch

        b "No! Please don't hurt her!"
        b "How could I let this happen!? It's my fault!"

        o2 "Wake up, [player_name]."

        scene 13octtherapy

        b "Ah! Th-they hurt her. Why? Why would they do that?"
        b "I didn't stop it..."

        o2 "Shh. It's alright, [player_name]. Look at me."

        scene 14octtherapy with dissolve

        b "Octavia?"

        o2 "It's me. Everything is fine. I'll take care of you."

        b "I must have fallen asleep. It... it turned into a nightmare..."

        scene 15octtherapy

        dr "That's quite some talent you have there, Ms. Octavia."

        o2 "One that I've mastered over many years."

        dr "I would like to reflect on this and I believe [player_name] needs some
            rest. It would be best if we ended our session early today."

        o2 "I'll take him home. We'll be fine. Thank you, Dr. Yu."

        if monogamy == True:
            jump pullingteeth
        else:
            jump postcube_octavia

    label precube_dallas:

        scene 1dalprecube with fade

        bi "{i}How does she just show up at my doorstep like that?{/i}"
        bi "{i}If she hadn't run away six months ago, where would my life be
            right now?{/i}"
        bi "{i}Would her and I have dated? Would she have pushed me to
            reconnect with Avalon sooner?{/i}"
        bi "{i}Would Avalon have stayed over with Leah and I at my house when
            Sharol had Tyler over?{/i}"
        bi "{i}The possibilities if she hadn't left are wreaking havoc on my mind.{/i}"
        bi "{i}If there's one person that can help me through this chaotic
            thinking, it's certainly--{/i}"

        scene 2dalprecube with vpunch

        play music "audio/disturbed_mind.mp3"

        d "Boo!"

        b "Gah! What the hell!?"

        if polygamy == True:

            scene 3dalprecube with dissolve

            b "Dallas! You scared the living daylights out of me."
            b "You're lucky I noticed it was you before I launched into
                full on attack mode and pulverized you."
            b "You cheated death today, girl."

            scene 4dalprecube with dissolve

            b "What're you--"

            scene 5dalprecube with dissolve

            d "Mwah!"

            scene 6dalprecube with dissolve

            b "That was not yours to take, Dallas."

            d "I know. That's why I had to steal it!"

            b "You sure are affectionate today. What's gotten into you?"

            d "I like the idea of... you know, us. It's nice having someone."
            d "Especially someone like you."

            scene 7dalprecube with dissolve

            b "Thanks, Dallas. I wanted to talk to you about us."
            b "I know we haven't had a lot of time to build our relationship yet."
            b "But I want you to know that you're important to me and I want to make
                time for us."
            b "Things are just complicated right now."

            scene 11dalprecube

            d "Don't even worry about it, man. It works for me."
            d "I get wrapped up in my own things all the time. I'll be consumed by
                work or busy with a project and I won't have time for a relationship."
            d "Especially with opening that salon soon, I'm going to be busy
                trying to make that work."
            d "So, you know, we don't have to be constantly together. Both of
                us having Avalon makes things easier for me to distance when I have to."

            d "Hey, tell me about last night. What happened?"

            scene 8dalprecube

            b "Oh, right. I... have a [persistent.leah_rel], Dallas. I met her about nine
                months ago."
            b "We spent a few months getting to know each other and then--"

            scene 10dalprecube with dissolve

            b "She wanted more from our relationship. She kissed me and I panicked."

            d "Whoa, that's heavy."

            b "She disappeared after that. And then last night, she just showed up
                at my doorstep. I haven't seen her in six months!"

            scene 12dalprecube

            d "Damn, that's wild. How're you holdin' up?"

            b "I'm still processing it."

            scene 11dalprecube with dissolve

            d "Well, you never know what she's been through. Maybe she doesn't handle
                rejection well."
            d "Give her another chance, you big burly dope."

            scene 9dalprecube

            b "You have the most unusual way of making me feel better."

            scene 10dalprecube with dissolve

            b "I do wonder what things would be like now if I hadn't rejected
                her though."
            b "Where would I be? Where would Avalon be? Would we have still
                become involved in some way?"

            scene 13dalprecube

            d "I won a few tickets from a competition on the radio a year ago. Avalon
                and I decided to go together."
            d "Just as we were leaving for the concert, I spilled my drink all over
                my shirt. I was so frustrated, it almost ruined my night."
            d "But I changed shirts and we went to the concert. Turned out the drummer
                of the band and I were wearing the same damn shirt."

            scene 11dalprecube with dissolve

            d "They pulled us backstage because of it and we partied until
                two in the morning! It was so freakin' cool, man."

            b "That's... neat."

            d "My point is, doofus, that we live in a perpetual state of chaos."
            d "Sometimes good things lead to bad things and sometimes bad things
                lead to good things."
            d "We have a lot less control over the direction of our lives than
                we'd like to believe."
            d "I've found it's just best to, you know, enjoy the ride, man. Push
                in the direction you wanna go but ultimately surrender to fate."

            scene 8dalprecube

            b "Wow, that was profound. Who are you and what have you done with Dallas?"

            d "I'm more than just a pretty face, [player_name]."

            b "I know. Trust me, I really know. That's why I asked you here today."
            b "If there's anyone who can cheer me up, it's you. It's always you."
            b "You're magic, Dallas."

            scene 14dalprecube with dissolve

            d "You know, a lot of people tell me I'm pretty. But only you and
                my parents make me feel this special. Thank you, [player_name]."

            b "Oh, you see me as a parental figure?"

            d "Well, you do spank me sometimes."

            scene 15dalprecube with dissolve

            b "Right on this ass here."

            d "You like my ass, [player_name]?"

            scene 16dalprecube with dissolve

            b "I like turning it red!"

            d "I have been a little bad lately. Maybe I need--"

            sun "Uh oh, someone just got caught red-handed!"

            scene 17dalprecube with vpunch

            b "Shit! Sun Mei!"
            b "It's not what it looks like! Or, no, it is what it looks like. But
                it's not what you think!"
            b "We're, you know, in a relationship..."

            sun "I thought you were in a relationship with Avalon?"

            b "I am! You see, here's the thing. We-- Er, all of us..."
            b "We do, together, the stuff..."
            b "Help me out here, Dallas!"

            d "You're doing so good though."

            scene 18dalprecube with dissolve

            d "We're all partners together. Avalon, [player_name] and I are in
                a three-way relationship."
            d "She and I are... trying something unique. We kind of share [player_name]."
            d "We're not cheating, it's more like a dating circle."

            b "Don't mention 'Circles' to me, Dallas. I don't like your circles."

            scene 20dalprecube

            sun "Oh gosh, that sounds amazing! Does that mean you get to have
                sex with her too!?"
            sun "Is there room for one more? Can I join!?"

            scene 19dalprecube

            b "What the fuck..?"

            d "Er, it's not a book club, Sun Mei. We're not exactly taking applications."
            d "Avalon, [player_name] and I have known each other for a long time."

            sun "We can get to know each other!"

            scene 21dalprecube with dissolve

            d "How about we start as friends, Sun Mei?"

            sun "Mm... Okay!"

            d "Here, I'll give you my number and we can hang out tomorrow. Cool?"

            sun "Yeah, that's awesome! Thank you, tan lady!"

            stop music fadeout 2.0

            d "Dallas."

            sun "Thank you, Dallas."
            sun "I'll take you to see Dr. Yu now. Follow me."

            jump thecube_dallas

        else:

            scene 11dalprecube with dissolve

            d "I got you good, [player_name]. You scare so easy."

            d "Hey, tell me about last night. What happened?"

            scene 8dalprecube

            b "Oh, right. I... have a [persistent.leah_rel], Dallas. I met her about nine
                months ago."
            b "We spent a few months getting to know each other and then--"

            scene 10dalprecube

            b "She wanted more from our relationship. She kissed me and I panicked."

            d "Whoa, that's heavy."

            b "She disappeared after that. And then last night, she just showed up
                at my doorstep. I haven't seen her in six months!"

            scene 12dalprecube

            d "Damn, that's wild. How're you holdin' up?"

            b "I'm still processing it."

            scene 11dalprecube with dissolve

            d "Well, you never know what she's been through. Maybe she doesn't handle
                rejection well."
            d "Give her another chance, you big burly dope."

            scene 9dalprecube

            b "You have the most unusual way of making me feel better."

            scene 10dalprecube with dissolve

            b "I do wonder what things would be like now if I hadn't rejected
                her though."
            b "Where would I be? Where would Avalon be? Would we have still
                become involved in some way?"

            scene 13dalprecube

            d "I won a few tickets from a radio competition a year ago. Avalon
                and I decided to go together."
            d "Just as we were leaving for the concert, I spilled my drink all over
                my shirt. I was so frustrated, it almost ruined my night."
            d "But I changed shirts and we went to the concert. Turned out the drummer
                of the band we went to see and I were wearing the same damn shirt."

            scene 11dalprecube with dissolve

            d "They pulled us backstage because of it and we partied until
                two in the morning! It was so freakin' cool, man."

            b "That's... neat."

            d "My point is, doofus, that we live in a perpetual state of chaos."
            d "Sometimes good things lead to bad things and sometimes bad things
                lead to good things."
            d "We have a lot less control over the direction of our lives than
                we'd like to believe."
            d "I've found it's just best to, you know, enjoy the ride, man. Push
                in the direction you wanna go but ultimately surrender to fate."

            scene 8dalprecube

            b "Wow, that was profound. Who are you and what have you done with Dallas?"

            d "I'm more than just a pretty face, [player_name]."

            b "I know. Trust me, I really know. That's why I asked you here today."
            b "If there's anyone who can cheer me up, it's you. It's always you."
            b "You're magic, Dallas."

            scene 12dalprecube

            d "Wha-- you... you think so?"

            scene 11dalprecube with dissolve

            d "Thanks, [player_name]. You do know how to make me feel pretty special."

            scene 7dalprecube

            b "Well, I appreciate you being her to help me out today."
            b "It helps having a friend here with me."

            d "You're welcome!"

            scene 17octprecube

            sun "Excuse me. I don't mean to interrupt but Dr. Yu is ready for you now."

            scene 17dalprecube

            b "Oh, it's that time already, is it?"
            b "Um, yeah, alright. Let's go."

            d "Hey, I'll be here with you. No worries, right?"

            stop music fadeout 2.0

            scene 20dalprecube

            sun "Oh, that's so nice that you're here to help your friend."
            sun "I'll take you back to Dr. Yu now. Follow me."

            jump thecube_dallas

    label thecube_dallas:

        scene 1daltherapy with fade

        play music "audio/plastic_dragon.mp3"

        dr "It is nice to see you again, [player_name]. I am glad you were able
        to make it today."

        scene 2daltherapy with dissolve

        dr "And I see you have a friend with you today?"

        scene 3daltherapy

        b "Yesterday's session rattled me a bit so I asked her to join me."
        b "I hope that's alright?"

        dr "Of course, Mr. [player_name]."

        scene 5daltherapy with dissolve

        d "I dig your pad, Dr. Yu. This place is incredible!"
        d "I actually have some experience with therapy but I've never had a
        session in a place like this. You must have a successful practice."

        scene 2daltherapy

        dr "I have been very fortunate in my success, yes. But much of my garden
        I maintain myself."
        dr "I find it very relaxing, especially as I get older."
        dr "Would you mind if I inquired about you, Ms. Dallas? Can you tell
        me about yourself?"

        scene 5daltherapy

        d "Sure! I've been good friends with Avalon since we were kids. We graduated
        few months ago but I've been on my own for a little more than three years."
        d "My parents decided that they wanted to travel the world but I was more
        keen to set down roots. So I stayed behind."
        d "I recently lost my job but thanks to the help of my friends, I have a
        very promising and exciting opportunity starting soon."
        d "Things are great for me right now. I'm excited for the future."

        scene 2daltherapy

        dr "That is wonderful to hear, Ms. Dallas. It sounds like you're an
        indepedent and capable young woman."
        dr "[player_name] is lucky to have a friend like you."

        scene 1daltherapy with dissolve

        dr "And how are you today, [player_name]?"

        scene 3daltherapy

        b "Not well. I went to see my father to inquire about Leah, who I told you
            about yesterday, and I..."
        b "I found him in his office. He'd hanged himself."
        b "And then Leah showed up at my doorstep late last night as well. Now
        I have a lot of conflicting feelings about that."

        scene 4daltherapy

        dr "I must say, I am surprised at the amount of drama that seems to follow
            you, [player_name]."
        dr "It is as if a dark cloud has attached itself to you."

        b "It does feel that way sometimes."

        dr "I would like to try an exercise with you, [player_name]."
        dr "It will help me to understand you better and perhaps help you understand yourself better
        as well."
        dr "Would you be willing to give it a try?"

        scene 3daltherapy

        b "Uh, sure. That sounds interesting enough. What do we need to do?"

        dr "First, we need you in a relaxed position. Laying down is preferable."

        scene 6daltherapy with dissolve

        b "Would you mind if I used your lap?"

        d "Not at all! Come here, big guy."

        scene 8daltherapy with dissolve

        d "Comfortable?"

        b "I am."

        scene 9daltherapy with dissolve

        dr "[player_name], I would like you to close your eyes."

        b "Alright."

        scene 10daltherapy with dissolve

        dr "I want you to imagine that you are in a desert. A vast plane of
            sand and rocks."
        dr "Feel the warmth of the sun on your skin and a dry breeze drifting through
            your hair."

        scene 2thecube with fadefast

        dr "Can you see it?"

        scene 3thecube with dissolve

        b "Yes. I can see it. It looks as though it's almost dusk, the sun is about to set."
        b "There's a surprising amount of greenery here. Most of the plants
            are managing to survive despite the heat and lack of water."

        dr "Everything within your desert will have meaning, [player_name]. Perhaps
            the surviving plant life represents your own perseverance."
        dr "Look around yourself. See if you can find a cube. And when you do,
            describe the cube to me."

        scene 4thecube with dissolve

        b "I don't see any cubes. Mostly just rocks. Is it supposed to be buried?"

        dr "Where the cube is, [player_name], is up to you to decide."

        b "I guess I could look around a bit. Maybe it's--"

        scene 5thecube with dissolve

        b "Oh! Okay, yes. There is a cube here."

        dr "How large is it? What's it made of? Where is it in relation to yourself?"

        scene 6thecube

        b "It must be about 3 feet tall. It looks like it's made out of copper."
        b "I can't imagine it weighing less than a ton but it's floating in the
            air as if it's weightless."
        b "As if the laws of physics don't apply to it. It's defiant and doesn't
            adhere to the rules."

        d "And it's made of copper? That makes me think of Penny. Does the
        cube represent her?"

        dr "The cube is supposed to represent yourself."
        dr "Is it possible--"

        b "Wait wait, it's changing. I can... I can see into it."

        scene 7thecube with dissolve

        b "There's another cube inside it. A smaller cube made of brick."
        b "It's like the copper cube is protecting the square made of bricks."

        d "A cube made of bricks? That sounds more like you, [player_name]."
        d "Encased inside of Penny's cube though..? Do you feel like she's
            protecting you?"

        b "She has. I don't know if I could have made it through yesterday
            without her."
        b "And she put that scumbag that hurt Avalon behind bars. That was something I couldn't
            do."
        b "She's taken care of us."

        dr "[player_name], look around once more. See if you can find a ladder."

        scene 8thecube with dissolve

        b "Okay, yes. There's a ladder here."

        dr "Where is it in relation to the cube."

        b "Across from it. They're apart."

        dr "The ladder represents your goals, [player_name]."
        dr "As it is away from yourself, your goals may involve taking care of
            others rather than prioritizing yourself."
        dr "That's very--"

        scene 9thecube with dissolve

        b "Dallas!?"

        d "Y-yeah??"

        b "No, I mean, you're here at the top of the ladder."

        scene 10thecube

        b "You're reaching out to me, trying to help pull me up the ladder."
        b "But... but you're wearing plate mail and carrying a sword. You look
            like a warrior! You're confident and strong."

        d "Is that how you see me? I... don't know what to say. That's flattering."

        b "Also, I can see your panties."

        d "Oh yeah, that sounds more like me."

        dr "Dallas has been a guiding hand for you, has she?"
        dr "You must reciprocate that generosity. Be sure you
            are there for her as well."

        b "I... I will. I've been so distracted lately but she deserves more from
            me."

        d "Remember when you came to my rescue at the police station? Trust me,
        [player_name], I know I can count on you."

        dr "I want you to look around once more. Is there a horse in the distance?
            Or nearby, perhaps?"

        scene 12thecube

        b "A horse in the desert? I can't imagine--"

        scene 13thecube with dissolve

        b "Woah. It's... not a horse. At least, not entirely. It's a girl with
            the body of a horse."

        d "Isn't that called a Centaur? Why would you be picturing that of all things?"

        dr "Please, describe this creature to us."

        b "There's something so familiar about her. I can't quite place it."
        b "She's timid, she's afraid of me. I don't think she's had good experiences
            with people like me in the past."

        scene 14thecube with dissolve

        b "It's okay, I won't hurt you. It's a big world out there. Maybe we can
            help each other?"
        b "What do you say? Can you trust me?"

        scene 15thecube with dissolve

        b "She's an exceptionally beautiful creature, to be sure. She doesn't appear
            to be very trusting but I think she's warming up to me."

        dr "Can you tell me why she's afraid of you, [player_name]?"

        b "She's been hurt before. She's not like other people, she's... unique.
            Special."

        scene 16thecube with dissolve

        b "She's letting me get closer to her. It doesn't seem she sees me as a
            threat anymore."

        dr "Are there any flowers that stand out? Growing out of the ground or
            perhaps somewhere else?"

        scene 17thecube with dissolve

        b "Oh, y-yes! They're in her hair."

        b "It's like when she's happy, they blossom and flourish. When she's
            scared or sad, they wilt and disappear."
        b "She rejects them when she's unhappy."

        scene 18thecube with dissolve

        b "She's really taken to me all of a sudden!"

        stop music fadeout 2.0

        b "I feel a connection between us. We're... we're somehow meant for each other."
        b "And now that she's happy, the flowers have started to bloom even more."

        d "Huh. Sounds like you're talking about A--"

        scene 19thecube

        b "S-something startled her! She's uneasy, agitated."
        b "Hey, it's alright. Nothing is going to hurt you."
        b "I'll protect you."

        play sound "audio/arrow_body.mp3"

        scene 20thecube with vpunch

        play music "audio/heartbeat_of_the_hood.mp3"

        b "No! Please don't hurt her!"
        b "How could I let this happen!? It's my fault!"
        b "I should have been there!"

        d "What's happening, Doctor? Can you pull him out of this?"
        d "[player_name], snap out of it! Wake up!"

        scene 11daltherapy

        b "Ah! Ugn. Wha-- I... they hurt her."
        b "I couldn't do anything. I couldn't protect her."

        d "Hey, look at me."

        scene 12daltherapy with dissolve

        d "It wasn't your fault. You didn't do anything wrong."
        d "Her mother should have been the one to prevent that shit. You've been
            nothing but good to Avalon!"

        scene 13daltherapy

        d "I didn't know he blamed himself. We can't let him believe that.
        There's gotta be something we can do!"

        b "I... I shouldn't have left her for so long..."

        scene 14daltherapy

        dr "Ms. Dallas, this is not something we can do immediately."
        dr "We both must help him overcome this mindset."
        dr "I think it best that we end the session early today. [player_name]
        needs rest."

        stop music fadeout 2.0

        scene 13daltherapy

        d "Okay, yeah, that sounds like a good idea."
        d "I'll take care of him."

        if monogamy == True:
            jump pullingteeth
        else:
            jump postcube_dallas

    label postcube_octavia:

        if _in_replay:
            $ player_name = renpy.input("What would you like to name the MC?")
            if player_name.strip() == "":
              $ player_name = "Byron"

        scene 1octpostcube with fade

        play music "audio/tomorrows_rain.mp3"

        o2 "Welcome to my home, [player_name]. I'm surprised that you're only
        just now seeing it."
        o2 "I suppose we've been a little pre-occupied with recent events, haven't we?"

        b "That's an understatement. This is captivating, Octavia. The view is...
        well, it's very you."

        o2 "Oh?"

        b "It's tranquil and calming to look at. No violent waves from the
        water, no obnoxious neon lights. Just a settled river and a quiet town."
        b "It's beautiful."

        scene 2octpostcube with dissolve

        o2 "Come on in, let me show you around."

        b "I didn't mean to suggest you're boring if that's--"

        o2 "You were correct in your statement, [player_name]. My life has had enough excitement,
        I want calm. I want tranquil."

        b "Me too. I've had enough drama for three lifetimes."

        scene 3octpostcube with dissolve

        o2 "Oh! It looks like someone has decided to hang out downstairs today."
        o2 "That's strange for her."

        b "You have company? Who is--?"

        scene 4octpostcube with dissolve

        b "W-wait, is that...?"

        o2 "Good afternoon, Sleepyhead."

        scene 5octpostcube

        o2 "Did you miss me, Maize?"

        b "I thought you were pulling my chain. You have an actual full-grown
            panther!?"

        o2 "I'm not a leg-puller, [player_name]. I'll always be frank with you."
        o2 "Come meet my friend, Maize. Don't be rude."

        scene 6octpostcube with dissolve

        o2 "That's a good girl!"

        b "I am positive these are not domesticated animals, Octavia. She's
        dangerous, isn't she?"

        o2 "Not at all!"

        scene 7octpostcube with dissolve

        o2 "Come here, Sweetie."

        b "Goddamn, that's a big cat! It looks hungry, Octavia. Are you sure
        it's not going to eat us? It looks like she's salivating!"

        o2 "You're silly, [player_name]."

        scene 8octpostcube with dissolve

        o2 "Maize is a rescue. Like I told Dr. Yu, I needed purpose after the
        military. So I took in Maize and we look after each other now."

        b "Can you imagine someone trying to rob this place?"
        b "They would sneak in, rummage through your stuff for a moment and then
        die from a heart attack after Maize jumps out of the shadows at them."

        o2 "She wouldn't hurt anyone. Can I have some affection, Maize?"

        scene 9octpostcube with dissolve

        o2 "Hi there, Sweet Girl."

        b "Seriously? You can plant your face right into hers?"
        b "She's just an oversized housecat!"

        o2 "She loves pets. Go on, don't be shy, [player_name]."

        scene 10octpostcube with dissolve

        b "Wow! She dwarfs me. Are you sure she is alright in such a confined space?"

        o2 "I have special trainers that come and take her out to an open field
        to play for several hours every other day."
        o2 "They take such good care of you, don't they, Maize?"

        o2 "Would you mind giving us some privacy for a little while, Maize?"

        scene 11octpostcube with dissolve

        b "Look at that! She listens? How'd you do that? How does she understand
        you?"
        o2 "She's an incredibly smart feline, [player_name]. She knows quite a
        few words. One being 'privacy'."
        b "What a magnificent creature. Awesome."

        o2 "I've got two magnificent creatures in my house right now."

        b "Oh, you have a second cat? Where?"

        scene 12octpostcube with dissolve

        o2 "No, I'm talking about you, Silly."

        b "I don't know. I'm not feeling very magnificent today."
        b "Especially after how I reacted when Leah showed up last night."

        scene 13octpostcube with dissolve

        o2 "I don't want you to dwell on that right now. I want you to be here,
        with me."

        b "Is that why you sent Maize upstairs? You want some 'alone time' with me?"

        o2 "Very perceptive, [player_name]. What gave it away?"

        b "I'd say it's the wanting eyes you have right now."

        o2 "Let's take this conversation to the bed, shall we?"

        scene 14octpostcube with dissolve

        o2 "Come on, [player_name]. You're not going to make me wait, are you?"

        b "Hang on. I just want to look at you for a moment. Just as you are."
        b "You truly are a vision to behold, Octavia. To define a woman in all
        her glory would be to define you."

        o2 "Oh, [player_name], I am sufficiently blushing. Please don't make
        me wait any longer!"

        scene 15octpostcube with dissolve

        o2 "Moving in for a kiss?"

        b "Actually, I'm after something else."

        o2 "Hmm? What are you--"

        scene 16octpostcube with vpunch

        b "Your pants!"

        o2 "Whoa! I didn't expect that, [player_name]. You surprised me."

        b "It wasn't too aggressive was it?"

        o2 "I can handle aggressive. Do you want to be rough with me, [player_name]?"

        scene 17octpostcube with dissolve

        b "Nope. I wanted to catch you off guard. Now I'm going to switch gears
        to keep you on your toes."
        b "Your gorgeous, beautiful ivory toes."

        o2 "You crazy man."

        b "What is that you're wearing? A onesie?"

        o2 "It's a bit unique, isn't it? Do you like it."

        b "I love it."

        scene 18octpostcube with dissolve

        b "But I love these legs more. Considerably more."
        b "I don't think there's a rough patch on you, Octavia. You're smooth
        all around."

        o2 "I don't remember you being quite this taken with my body before, [player_name]."

        scene 19octpostcube with dissolve

        b "I was nervous before. It usually takes me a few romps in the hay to get
            comfortable being intimate with someone."
        b "Is that strange?"

        o2 "You're eager to please but afraid to disappoint. I wouldn't consider
        you strange or dare to compare you to other people."
        o2 "I adore you just the way you are."

        b "Well that melted me right down into putty. That was super nice!"

        scene 20octpostcube with dissolve

        o2 "Nice enough for a reward?"

        b "Maybe, what did you have in mi--"

        scene 21octpostcube with dissolve

        b "The Grail! Who is being rewarded here? Me or you??"

        o2 "Both of us?"

        b "It's been a while since I've done this. Beware the beard!"

        scene 1tacodinner with dissolve

        b "Mm. Mhmm."

        show tacodinner with dissolve

        o2 "Ugn! Keep going, keep going."
        o2 "I never guess you'd be so good with your tongue, [player_name]. Oh,
            exceptional!"
        o2 "Press harder! Ooh! Circles, do circles with your tongue."
        o2 "Yes! Like that. Perfect! Now wriggle it inside of me, [player_name]."

        o2 "That's good, oh, that's very good."
        o2 "Okay, stop stop!"

        scene 21octpostcube with dissolve

        b "What? Did I do something wrong?"

        o2 "No, I don't want to finish yet. I want to finish with you."

        scene 22octpostcube with dissolve

        b "You don't have to ask me twice!"
        b "Come on.. stupid... zipper!"

        play sound "audio/zipper.mp3"

        scene 23octpostcube with dissolve

        o2 "Whenever you're ready, [player_name]."

        b "Here, let me just..."

        scene 24octpostcube

        o2 "Oh! You're going to hold me up like this?"
        o2 "Such a strong man I'm with today!"

        b "I can pull you into me this way. I don't want to hurt you though so
        tell me if it's uncomfortable."

        o2 "I will. Let's start, I'm ravenously excited right now!"

        scene 1liftandthrust

        b "I love the way your body curves, Octavia. And you're so light."

        show liftandthrust with dissolve

        o2 "Oh! Oh! Incredible! Keep going!"

        b "You're squeezing me so hard!"

        o2 "I can't help it. The pleasure is tremendous, it's making my whole
        body contract!"
        o2 "Harder, [player_name]. Don't be afraid to hurt me!"

        b "Oh, shit, when you talk like that..."

        o2 "Finish inside me. I want your semen inside me. Make me yours, [player_name]!"

        b "I'm cumming!"

        scene 21liftandthrust with dissolve

        b "Gaaah!"

        o2 "Ugn! I can feel it! It's exploding into me!"
        o2 "I feel like it's going to pierce my womb, [player_name]!"

        scene 25octpostcube with dissolve

        b "Wah! Shit! I'm still cumming."
        b "Damn. I think I got it on your shirt."

        o2 "I don't mind at all! This performance was fantastic."
        o2 "Thank you, [player_name]."

        b "The pleasure was mine, I assure you."

        scene 26octpostcube with dissolve

        if persistent.meetthepussy == False:
            $ renpy.notify("You've unlocked 'meetthepussy' in the Scene Gallery on the Main Menu!")
            $ persistent.meetthepussy = True

        o2 "Any stress I may have held in my body is gone. I feel absolutely renewed."

        b "I have to say, I feel the same. You know how to make me feel
        like a man, Octavia."

        o2 "Mm, and I enjoyed every second of it!"



        $ renpy.end_replay()

        jump pullingteeth

    label postcube_dallas:

        if _in_replay:
            $ player_name = renpy.input("What would you like to name the MC?")
            if player_name.strip() == "":
              $ player_name = "Byron"

        scene 1dalpostcube with fade

        play music "audio/bored_to_death.mp3"

        d "You like to work out when you're stressed, right? So I brought us to
            the gym!"
        d "We can get sweaty and stinky while we release all our stress, dude!"

        b "This is the Yoga room. There are no weights here."

        d "We have to stretch first! Come on, man. You don't want to pull anything.
            Especially what with your old age and all."

        b "Ugh!"

        d "And none of that bullshit fake stretching you did before! That was just
        showboating!"

        scene 2dalpostcube

        b "Take it easy on the shouting, Dallas. There's someone else here."
        b "We don't want to be inconsiderate."

        scene 3dalpostcube

        d "Because I'm just a loud, dumb blonde. Is that it, [player_name]?"

        b "Your words, not mine."
        b "Come on, Dallas. You know what I think of you."

        d "Some sort of warrior Goddess, apparently. I'm still wrapping my
        head around that! I can't believe you see me that way."

        scene 4dalpostcube

        b "That whole thing was bizarre. I felt like I was there."

        d "You have some issues, dude. You need to work through that shit."

        b "Yeah, no joke. But that's what I'm going to a therapist for."

        scene 5dalpostcube with dissolve

        d "Hey, eyes forward, [player_name]. Don't be that guy."

        scene 6dalpostcube with dissolve

        b "I was just admiring her form! What's that move called? The Reverse
        Flamingo?"

        d "Yeah yeah, I'm sure you're real interested in her 'form', [player_name]."

        scene 7dalpostcube with dissolve

        b "What were your therapy sessions like? Did you ever do hypnosis or anything
        like that?"

        d "Nope! My sessions were pretty standard. It was mostly just me talking
        and them listening."
        d "That seemed to be enough though. Saying it all out loud helped me
        understand it better."
        d "Then I was able to..."

        scene 8dalpostcube with dissolve

        d "come up with ways to prevent--"

        scene 9dalpostcube with dissolve

        d "Are you serious right now? What am I, chopped liver?"

        b "Shit! Sorry!"

        d "I'm telling you about my life and you're distracted by a pretty girl?"

        b "Fuck, I'm a dick. I'm sorry!"

        scene 10dalpostcube with dissolve

        d "I'm just bustin' your balls, [player_name]. I don't care."
        d "According to an article I read, guys feel a sensation of like, being rewarded
            when they look at a girl they find attractive."

        b "Yeah, I can't help it sometimes."

        d "You need some attention from a cute girl, [player_name]?"

        scene 11dalpostcube with dissolve

        d "You need some affection? Huh, huh?"

        b "What the hell? What are you doing?"

        d "If looking at hot women makes you feel rewarded, what's this do for you?"

        b "Knock it off, Dallas. Come on, we're in public."

        stop music fadeout 2.0

        scene 12dalpostcube

        d "If you like looking, you must love touching!"
        d "Ooh la la, [player_name], touch me. Put your hands all over me."

        play music "audio/disturbed_mind.mp3"

        d "I don't mind. You can grab whatever you w--"

        scene 13dalpostcube with dissolve

        d "Hey! What the hell!"
        d "What are you doing??"

        b "What?"

        scene 14dalpostcube

        d "Dude, you have an erection. I was just messing around!"

        b "Are you serious right now? What did you think was going to happen!?"

        d "It's involuntary? I thought you could like, turn it on and off or something!?"

        b "You have got to be joking."

        scene 15dalpostcube with dissolve

        d "Ahaha. Oh man, my bad, [player_name]. My bad!"
        d "You've got to work out with that thing now, huh?"
        d "That's got to be so embarrassing! Ahaha!"

        scene 16dalpostcube

        b "It's not funny, Dallas! I can't exercise like this!"
        b "Ugh, I'll have to wait it out. I can't believe you're laughing at me!"

        d "Wait, I have an idea."

        scene 17dalpostcube with dissolve

        d "Let's see what we're working with here."

        b "Wait, Dallas, no! There's too many people here!"

        d "It's a week day! Everyone's at work! Well, except that girl that
        just left..."

        b "We're standing in front of several huge windows! Are you crazy!"

        scene 18dalpostcube with dissolve

        d "Whoopsie! There go the shorts. Damn, I really got you excited, didn't I?"

        b "If you're doing this, do it fast! We're going to fucking jail if we get
            caught!"

        d "Don't be dramatic! We'd probably just get a slap on the wrist."

        scene 19dalpostcube

        d "This thing is a freakin' monster, man. What do you feed it."

        b "Dirty blondes, apparently."

        d "Hilarious, [player_name]."

        scene 21dalpostcube with dissolve

        d "Mm, damn this thing is sexy."

        b "Chow! You've got cold hands!"

        d "I just wanna make out with it."

        scene 20dalpostcube with dissolve

        d "Mwah!"

        scene 21dalpostcube with dissolve

        d "I love you, my special little dick monster."

        b "What the fuck, Dallas? Dick Monster? Really?"

        d "Yeah. Dick Monster."

        scene 1cheekinit with dissolve

        b "What are you--"
        b "Are you putting it in your mouth!?"

        show cheekinit

        d "Mmph, Mmph! Mmmhmm."

        b "Ugn! Wow! That's good, that's good. Alright, keep going!"
        b "How are you sucking that hard? You're like a little hoover on my
        dick!"
        b "Watch the teeth, watch the teeth!"

        d "Mhm mhm."

        b "I can feel my head slamming into your cheek, Dallas."
        b "Can you take in more??"

        scene 21dalpostcube with dissolve

        d "Fuck no! This thing is way too big!"
        d "But... I know one way I could take more of it."
        d "Lie down. Quick!"

        b "You cannot be serious."

        d "Do it!"

        scene 22dalpostcube

        b "This is literally the worst idea in the history of ideas."
        b "Someone could walk in at any second!"
        b "And then shit is going to hit the fan, Dallas!"

        scene 23dalpostcube

        b "Holy fuck! How'd you get undressed so fast?!"

        d "I am going to put your dick so far up my cooch, we may never get it out."

        b "What?! How would that even work? The physics of it--"

        d "Shut up. This is happening."

        scene 24dalpostcube

        d "Gah! I can feel it against my pussy. Mmff! Yes!"

        b "I hate myself for totally getting off on this."

        d "It's hot, right?! The possibility of getting caught. It makes this
        so much better!"

        b "Until we're in prison for life. Hurry up!"

        scene 25dalpostcube

        d "It's kind of cute that you're acting like a scared little bitch right now."

        b "Don't call me a little bitch! You're being crazy!"

        d "I am strangely into this, honestly."

        b "Alright, yeah, it's a little sexy. But seriously, lets go!"

        d "Let me just wiggle around a bit here and--"

        scene 1rodehard

        d "Oh shit shit! It's in!"

        b "Goddammit, you're tight! How am I not tearing you apart right now?"

        d "I think you are! Ugn!"

        show rodehard

        d "Ahh ahh! I can... I can take it. I'm more used to it now. I can take it!"

        b "Stop squeezing so tight, Dallas! You're gonna pinch it off!"

        d "I can't help it! You're too big!"
        d "I think you're battering my womb! Fuck!"
        d "Oh, you're going to ruin me, [player_name]!"

        b "Shit, I'm finishing, Dallas. I'm... I'm coming!"

        scene 26dalpostcube with vpunch

        d "Fuck! Yes! Fill me up, [player_name]! Yes! Yes!"
        d "I can feel it so deep inside me! There's so much cum!"

        b "I'm cumming so hard it hurts! Goddammit!"

        d "This! Is! Amazing!!"

        scene 27dalpostcube with dissolve

        d "Ugn. Oh. It's over. Thank G--"


        scene 28dalpostcube with dissolve

        d "Fuck."

        b "No. Nope. Don't you dare tell me someone is there."

        scene 29dalpostcube

        sierra "Oh my goodness. I--"
        sierra "I didn't mean to--"

        scene 30dalpostcube with dissolve

        sierra "I just forgot my shoes."
        sierra "I didn't see--"
        sierra "I mean, I only saw--"

        scene 31dalpostcube with dissolve

        sierra "I can just buy new shoes. I've been meaning to anyway."
        sierra "Or you know what, maybe I don't even need shoes at all."
        sierra "I just need... some alone time..."

        scene 32dalpostcube

        if persistent.rodehard == False:
            $ renpy.notify("You've unlocked 'Rode Hard' in the Scene Gallery on the Main Menu!")
            $ persistent.rodehard = True

        b "Get your shorts on, Dallas! We gotta get the fuck out of here!"

        d "Ahaha. Did you see her face? She was stunned! She had no idea
            how to react!"

        b "She's probably calling the cops right now, Dallas!"
        b "I'm too pretty to go to prison! Get your shit and lets go!"

        stop music fadeout 2.0

        d "Ahaha. I don't think she's using her fingers to dial a phone number, [player_name]."
        d "That girl is probably knuckle deep in her own cooter right now! Ahaha!"

        $ renpy.end_replay()

        jump pullingteeth

    label pullingteeth:

        scene 1pullingteeth with fade

        play music "audio/a_way_out.mp3"

        pause

        merc "Faith? The door was open so I let myself in. Are you here?"

        scene 2pullingteeth

        merc "If you need to be alone, I can--"

        f "I'm here."

        scene 3pullingteeth with dissolve

        merc "Last night didn't go so well so I thought I'd check on ya."

        scene 4pullingteeth with dissolve

        merc "What're you doin' down there?"

        scene 5pullingteeth

        f "I failed, Merc. I failed my father, I failed myself. I feel defeated."
        f "The life I knew is over. Nothing is ever going to be the same. And
        I couldn't even get vengeance on the person that took it all from me."

        merc "We ain't dead and we ain't in jail. You could count that as a win."

        f "That just makes it worse. We were so far beneath her, she didn't even
        feel it necessary to kill us."

        scene 6pullingteeth with dissolve

        merc "You have options. You can try again if you want. Sometimes it's better
        to just accept defeat and move on to other things though."
        merc "'S up to you but I found out last night my boss killed himself in
        his office. I got no reason ta kill 'er now."

        f "What about avenging Lance's asshole?"

        merc "That was a dick move on that detectives part but ain't worth killin' for."

        scene 11pullingteeth

        merc "Jus' can't help ya no more on this matter, Faith. There ain't nothin'
        in it for Lance and me."
        merc "I can give you yer money back but, well, I have another--"

        scene 8pullingteeth

        f "Don't... worry about it. I'm not concerned about money right now.
            I'm concerned about where I go from here."
        f "You wanna know something messed up, Merc?"

        merc "Hm?"

        f "It's been kind of nice without him around."

        merc "Your dad?"

        f "Mhmm. I haven't had to worry about him, haven't had to take care of
        him. There's a freedom I haven't experienced before."
        f "But it's bogged down by this heavy guilt I have for feeling that way."

        scene 11pullingteeth

        merc "I always figured prison was inevitable for me. Never thought I'd go
        this long without bein' put away. Just somethin' I accepted."
        merc "Some kind of goddamn miracle that I ain't been sentenced away for life
            if you ask me."
        merc "If I... if I had a daughter though, I'd give anything to keep her from bein'
        incarcerated. I wonder if your daddy felt the same way."
        merc "If he does, it'd be a damn shame for you to feel guilty for somethin'
        he'd want so desperately for you to have;"
        merc "Freedom."

        scene 10pullingteeth

        f "He did want that for me. I know he did."
        f "He traded himself for my release."

        scene 8pullingteeth with dissolve

        f "Feelings contradict reason sometimes, don't they?"

        merc "Truer words, Faith."

        f "Being forced to submit to that damn detective though. Ugh! It's like..."

        merc "Pulling teeth?"

        scene 9pullingteeth with dissolve

        stop music fadeout 2.0

        f "You did not just use that phrase. You've gotta be kiddin' me."

        scene 13pullingteeth

        merc "It looks like you can still smile. Bet there is more of them in your
        future too."
        merc "Maybe things ain't gonna be so bad."

        scene 9pullingteeth

        f "Merc, you got the worst of it yesterday. How are you the one cheerin'
        me up? Shouldn't you be pissed?"
        f "You really don't get angry anymore, do you? That conk on the head
        has you chipper as a fuckin' bluejay."

        scene 12pullingteeth

        merc "I got hit on the head?!"

        f "Er, yeah, you don't remember now..?"

        scene 13pullingteeth with dissolve

        merc "Nah, I'm just fuckin' with ya. It ain't affect my long-term memory."

        scene 9pullingteeth

        f "Ha. I'll admit, you had me goin'."

        scene 14pullingteeth

        lance "If you're givin' him a blowie, there's literally a bathroom right
        over here."
        lance "Unless you're into the exhibitionist shit."

        scene 15pullingteeth

        f "Oh hey, Lance. Why don't you come have a seat. There's a nice, warm
        spot right next to me."

        lance "Nah, I'm good."

        f "Come on, buddy. It's real cozy down here."

        lance "You know I can't sit down, Faith! Stop fuckin' around!"

        scene 16pullingteeth with dissolve

        f "Oh man, you're such a pussy, Lance!"

        lance "I ain't a pussy, I got burn blisters on my fuckin' taint. A lesser
        man would be dead!"

        f "Stop! Stop it! You're just making me laugh harder! I'm dying here!"

        scene 14pullingteeth

        lance "Listen, Chica. We just had a business opportunity open up."
        lance "Between Merc and myself, we got the brawn. But we need someone
        who is good with paperwork and shit."
        lance "It's all fuckin' legit, too. Well, mostly legit. We could make
        some serious cash here, Faith. You down?"

        scene 15pullingteeth

        f "Well, fuck, I don't know. Can you give me some actual information
        on what the hell you're tryin' to drag me into?"

        lance "Yeah, pick your depressed ass up off the ground and I'll show you."

        f "Alright, Lance. Let's see what half-brained idea you've cooked up. Show
        me."

        if octavia:
            jump octmeets
        else:
            jump dalmeets

    label octmeets:

        play music "audio/tomorrows_rain.mp3"

        scene 1octmeets with fade

        pause

        play sound "audio/dooropen.mp3"

        scene 2octmeets with dissolve

        o2 "Hm?"

        l "I'm just saying, if we were the same weight, I would have won everytime!"

        a3 "You're probably right!"

        scene 3octmeets

        a3 "We'll have to invite [player_name] next time. He must weigh a lot so
        we could easily beat him at Go Karts!"

        l "Hey, that's true! He might not be able to go at all!"

        a3 "Or maybe he would just pick up the Go Kart like a toy and run around
        the track with it under his arm."

        l "Ha! Maybe!"

        scene 5octmeets

        o2 "Good afternoon, Avalon."

        a3 "Oh, hey Octavia!"

        o2 "[player_name] told me you were spending time with Leah."

        scene 6octmeets with dissolve

        o2 "You must be her?"

        l "Yes, nice to meet you."

        o2 "[player_name] speaks fondly of you. It's a pleasure to make
        your acquaintance."

        scene 7octmeets

        l "Oh, does he?"

        a3 "Leah, this is Octavia. We only just met a week ago but she's one of the
        nicest people I've ever known."
        a3 "You'll love her, I promise!"

        scene 5octmeets

        o2 "You're too kind, Avalon."

        scene 6octmeets with dissolve

        o2 "I heard you were away on business for a few months?"

        l "Oh, yeah, I just got back."

        o2 "Was it a successful venture?"

        scene 8octmeets

        l "Yes, we completed our project early and my Team and I received paid time off for
        the next six weeks."

        o2 "May I ask what your business was?"

        l "Of course. We were developing an artifical organ. We still have some
        hurdles to conquer before it's ready for human trials but we made progress."

        o2 "Fascinating!"

        scene 9octmeets with dissolve

        a3 "Isn't it? I thought so too!"
        a3 "Oh, where's [player_name]? I found a place for sale online that I thought
        Leah might be interested in."

        a3 "I was thinking we could all go check it out?"

        scene 5octmeets

        o2 "[player_name] had a rather emotional session today so he's resting."
        o2 "Why don't you leave him a text message to meet us there?"

        a3 "Okay, that's a good idea."

        scene 10octmeets

        o2 "What happened with your home, Leah?"

        l "Well, since I was going to be gone so long, I had my company sell it for me."
        l "It was quite small so I was going to upgrade after I finished with the project."

        a3 "You'll love this place I found, Leah. And it's close by!"

        stop music fadeout 2.0

        scene 1leahsnewpad with fade

        a3 "Hrm. It's just this one room? It looked bigger online."

        o2 "It seems to be a studio apartment. I'm of the opinion that it is actually
        quite lovely. Simple, yet unique."

        l "I don't need anything large since it's just me so..."

        scene 2leahsnewpad

        play music "audio/soft_reminder.mp3"

        l "This could actually work for me."

        o2 "It will look significantly different with furniture and appliances."
        o2 "There's also a second story!"

        a3 "Hmm. Yeah. The ad said there was an exceptional view out the windows too."

        scene 3leahsnewpad

        a3 "Woah! They weren't lying!"

        o2 "Avalon, you startle me when you get excited all of the sudden like that."
        o2 "What did you see?"

        a3 "Look look!"

        scene 4leahsnewpad with dissolve

        a3 "We're like, in the air! This place must have been built on a cliff!"
        a3 "It's beautiful! You can see the river and mountains. This is epic!"

        l "Yeah, it looks like you hit the view jackpot here. I wouldn't mind waking
        up to that."

        o2 "It's lovely, Leah. Maybe Avalon needs to be a real estate agent?"

        l "Maybe!"

        scene 5leahsnewpad

        a3 "This place would sell itself!"

        l "Can you imagine having a cup of coffee, sitting in a chair in front
        of this window and looking out over this beautiful scenery?"

        o2 "I believe I can imagine that. And it sounds like a wonderfully peaceful
        way to enjoy a morning."

        scene 6leahsnewpad

        a3 "Wait, I heard that they laid out snacks upstairs! Let's go see!"

        o2 "Okay, Avalon. Lead the way."

        l "I wouldn't mind seeing the upstairs anyway."

        scene 7leahsnewpad

        l "I love how excited she is about this. I have not been jubilant like
        that about anything in years. Especially not four walls, you know?"

        o2 "It's endearing, isn't it? So much energy and excitement. It's inspiring
        to be around her."

        l "I can already see that."

        scene 8leahsnewpad

        a3 "Ooh, there's little cake squares! They're pretty small, but there are a lot!"

        o2 "Make sure you leave some for other people, Avalon."

        a3 "Of course! I'll leave, you know, three or four at least!"

        scene 9leahsnewpad

        a3 "Do you two want to hang out here while we wait for [player_name]?"
        a3 "We can talk and get to know each other better!"

        scene 10leahsnewpad

        o2 "Sure, that sounds nice. If Leah would like to?"

        l "Yeah, I'd like to see what [player_name] thinks so that's a great idea."

        a3 "Excellent!"

        stop music fadeout 1.0

        jump appleorchards

    label dalmeets:

        scene 1dalmeets with fade

        play music "audio/disturbed_mind.mp3"

        pause

        play sound "audio/dooropen.mp3"

        scene 2dalmeets with dissolve

        d "Hm?"

        l "That was so much fun, Avalon. We'll have to do that again sometime."

        scene 3dalmeets

        a3 "Heck yes! We'll have to invite more people, too!"
        a3 "[player_name] might be over the weight limit though."

        l "Ha. Yeah. I bet the kart wouldn't even go!"

        a3 "Maybe not!"

        scene 4dalmeets

        d "Hey, Avalon! I was wondering when--"

        scene 5dalmeets with dissolve

        d "Goddamn! Who's the tall glass of water?"
        d "Oh shit, is this Leah? I imagined [player_name] with tits, not this...
            Irish Goddess."


        scene 6dalmeets

        a3 "Jeez, Dallas! Not subtle at all, are you? And yes, this is Leah."

        l "Oh, you're Dallas? Avalon mentioned you. It's uhm, nice to meet you."

        d "Likewise as hell."

        a3 "Behave, Dallas!"

        scene 8dalmeets

        d "[player_name] told me you just showed up out of the blue last night."
        d "Where did you disappear to? Why come back now?"

        scene 7dalmeets

        l "I was on a business trip. I was hidden away from the world while my team
        and I worked on a project."
        l "It's finished now so I wanted to see [player_name] again."

        scene 9dalmeets with dissolve

        a3 "There's a house for sale I found online that I thought Leah might want
        to see. We were just about to head over to it."
        a3 "Where's [player_name]? I want him to join us."

        d "He had a rough therapy session. He's resting right now."

        l "Is he alright?"

        scene 8dalmeets

        d "That guy has a lot of shit to work through. But he's a tough son of
        a bitch. I'm sure he'll be just fine."
        d "And now he's got his [persistent.leah_rel] here to support him too!"
        d "He hit the jackpot with us, didn't he?"

        scene 9dalmeets

        a3 "I'll text him the address and he can meet us there when he's up."
        a3 "You ready to go?"

        d "Sure! Let's do it."

        scene 10dalmeets with dissolve

        stop music fadeout 2.0

        d "So Leah, tell me about this crazy business adventure?"

        l "Oh, sure. It's not as interesting as you might think though."

        scene 11leahsnewpad with fade

        play music "audio/soft_reminder.mp3"

        d "Oh shit, this isn't too bad. It's wide open and it has an upstairs? Kickass."

        a3 "It looked bigger online. I thought there were more rooms. Is this all of it?"

        scene 12leahsnewpad with dissolve

        l "It sort of reminds me of my old home. It's more spacious though."

        d "No walls between the living area and the kitchen. A very modern design,
        if you ask me."

        l "I must say, it's rather appealing to me."

        scene 13leahsnewpad with dissolve

        a3 "Oh, look! Wow!"

        d "Hm? Did you see something?"

        a3 "Yeah, come on! I want to see this!"
        a3 "The ad said it's the best part!"

        scene 14leahsnewpad with dissolve

        a3 "Look at this view! It's incredible!"

        l "That is a unique overlook. This place must be built on a cliff."

        scene 15leahsnewpad with dissolve

        d "That certainly is something. I hope you're not afraid of heights, Leah!"

        l "Not particularly."

        a3 "How do you clean the outside of the window though..?"

        scene 16leahsnewpad with dissolve

        a3 "Oh, they said there are snacks upstairs!"
        a3 "Come on, let's go see!"

        d "Slow your roll there, Crazy."
        d "Are you trying to beat the ants to them or something?"

        l "She has so much spunk. Is she always like this?"

        d "I have never met another person as jubilant. And her positivity is
        infectious."

        scene 18leahsnewpad

        a3 "Little cakes! And there's plenty too!"
        a3 "Come on, you guys!"

        d "Hold your horses, we're coming."

        scene 9leahsnewpad

        a3 "What do you say? Do you want to hang out here while we wait for
        [player_name]?"
        a3 "We can get to know each other better!"

        scene 19leahsnewpad

        d "Well I've certainly got time."

        l "Yeah, I'm up for it."

        a3 "Great! Let's dig in!"

        jump appleorchards

    label appleorchards:

        scene 1justascratch with fade

        play music "audio/a_quiet_thought.mp3"

        pause

        play sound "audio/cellvibe.mp3"

        "*Bzzz* *Bzzz*"

        scene 2justascratch with dissolve

        b "Hm?"

        "*Bzzz* *Bzzz*"

        bi "{i}I must have fallen asleep. How long have I been out?{/i}"

        scene 3justascratch with dissolve

        bi "{i}It's Avalon. They're looking at a potential new house for Leah?{/i}"
        bi "{i}That makes sense. She needs a place to live now.{/i}"
        bi "{i}Avalon wants me to meet them there. Hm.{/i}"
        bi "{i}Looks like it's not too far away at all. I'll text her that I'll
        be there soon.{/i}"

        scene 4justascratch with fadefast

        bi "{i}With Leah back, my father gone, and Avalon on the mend, I can't help
        but to be excited for the future.{/i}"
        bi "{i}This might be the happiest I've ever been in my whole life. And it
        looks like things are just going to get better from here.{/i}"

        scene 5justascratch with dissolve

        bi "{i}Things are finally starting to look up. I guess good things do come
        to those who wait.{/i}"
        bi "{i}I sure am a lucky--{/i}"

        play sound "audio/dooropen.mp3"

        scene 6justascratch with dissolve

        bi "{i}Did I just hear the front door open? Are they back already?{/i}"
        b "Girls? Did you just get home? I'm in the kitchen."

        scene 7justascratch

        stop music

        pause

        play sound "audio/dooropen.mp3"

        scene 8justascratch with vpunch

        play music "audio/a_way_out.mp3"

        s "You son of a bitch."

        b "S-Sharol?"

        s "It's your fault, [player_name]. My whole wrecked {b}fucking{/b}
        life is your fault."

        scene 9justascratch

        b "My fault? What are you talking about? Have you been drinking?"
        b "Is that... is that a gun, Sharol?"

        scene 10justascratch

        s "They loved you more than me. My own fucking parents loved {b}you{/b}
        more than {b}me{/b}!"
        s "And then I finally found happiness in Johnny. He went off to find
        your daddy and it got him killed. His death is {b}your{/b} fault, [player_name]!"
        s "And now you've taken my daughter. The only thing I have left and you
        turned her into your fuck doll!"

        scene 11justascratch

        b "I'm sorry, Sharol. I didn't mean to get Johnny in trouble. I didn't
        know my father was a monster."
        b "Can't we talk about this? Please? Can you just put the gun down?"

        b "Avalon and I aren't just fooling around, we're in l--"

        s "Don't!"

        scene 13justascratch

        s "You may have taken everything from me, [player_name]."
        s "I won't let you take everything from her. I won't!"
        s "Somebody has to stop you. {b}I{/b} have to stop you."

        scene 12justascratch

        b "Please, Sharol. Don't do this. You'll take us both away from her."
        b "She won't make it without us. She needs us."
        b "Please don't--"

        stop music

        play sound "audio/revolver.mp3"

        scene black with vpunch

        "..."
        "... ..."
        "... ... ..."

        "Some people say their life flashes before their eyes just before they die."
        "They relive their best moments just before they take their last
        breath."
        "I didn't see my life. I only saw..."

        scene 1goldenorchard with fade

        play music "audio/heaven_and_above.mp3"

        "Johnny."

        j "Hey, buddy. It's been a long time. You've had quite an exciting week,
        haven't you?"

        b "Johnny?"

        j "Yeah, it's me, pal. Listen, I wanted to thank you for taking such
        good care of my little girl."

        scene 2goldenorchard with dissolve

        j "I would have given anything to be there for her and to watch her grow up."
        j "And I'm sorry I wasn't there for you, [player_name]. I know you needed
        a friend more than anyone else. I let you down, pal."
        j "Unfortunately, we don't always get to choose our fate, do we?"

        b "I forgive you! It wasn't your fault! I shouldn't have--!"

        scene 4goldenorchard with dissolve

        j "Slow down there, Cowboy."
        j "Life weaves a complicated web and we can never know where each string
        will take us when we follow one."
        j "What happened to me was not your fault."
        j "I wanted to find your father. That was my own choice."

        scene 3goldenorchard with dissolve

        j "Sharol is blinded by anger. She can't see past her own tragedies."
        j "She's mad at the universe for everything bad that's happened to her."
        j "She doesn't understand that nobody lives a life without bad things happening
        once in a while."

        b "I couldn't help her. I tried. I just--"

        scene 4goldenorchard with dissolve

        j "I don't think anyone could have helped her. Trauma affects everyone differently."
        j "For some, trauma plays on their empathy and they don't want to see anyone
        else suffer the way they did."
        j "Others just become angry and vengeful."
        j "Sharol never drifted in either direction. She wallowed in depression and
        let her life pass her by. Until..."
        j "Well, until she shot you, [player_name]."

        j "Our actions have consequences. I don't know what the future holds for her now."
        j "Only time will tell."

        b "Is that an orchard behind you?"

        scene 5goldenorchard with dissolve

        j "It is. Beyond those apple trees is my new sanctuary, [player_name]."
        j "I was healed of all my wounds, all my trauma. And now that is my paradise
        where I get to live on forever."

        b "Can I see it?"

        scene 4goldenorchard with dissolve

        j "I'll show it to you one day, [player_name]. But not today."
        j "You still have to take care of my little girl. Keep her safe, keep
        her happy. For me, buddy."

        scene black with dissolve

        j "And if you can find it in your heart, please forgive Sharol."

        b "No... no wait! Please don't leave me again, Johnny!"

        stop music fadeout 1.0

        b "Please!"

        "Come back to me, [player_name]."
        "Focus your eyes on me."

        scene 14justascratch with Dissolve(4.0)

        "That's it. Take deep breaths and follow my voice."

        p "You bumped your head pretty good when you fell backwards."

        b "What..? What happened?"

        p "You were shot, [player_name]. Right now you're in shock."

        b "Am I... am I going to die?"

        scene 16justascratch

        play music "audio/your_hand_in_mine.mp3"

        p "You're going to be alright, [player_name]. It looks like I got here
        just in time."

        b "Sharol was here. She had a gun. She shot me?"

        scene 17justascratch with dissolve

        p "The bullet grazed your cheek. It looks like the wound isn't deep.
        You won't even need stitches."

        b "What happened?"

        p "I came over to check on you and meet Leah. I walked in to find Sharol
        with a gun pointed at you."
        p "I've never moved so quickly before in my entire life. I just barely
        managed to get to her before she pulled the trigger."
        p "Well, not quite fast enough, obviously."

        b "Where is she?"

        scene 18justascratch with dissolve

        p "I hit her pretty hard, [player_name]."
        p "I've already called for help, they should be here any minute."

        b "Is she going to be alright?"

        p "I don't know for sure. I used a considerable amount of force when I elbowed
        her in the head."
        p "She could have brain swelling, or even hemorrhaging."
        p "I did what I thought I had to in order to save your life."

        scene 19justascratch

        p "I explained the situation to the operator when I called for an ambulance."
        p "They know what to expect. It's... all I could do."

        scene 20justascratch

        p "Let's get you up off the floor, [player_name]. Here, take my hand."

        b "Where did your earring go?"

        p "My earring? I didn't wear any jewelery today."
        p "You must have hit your head pretty darn hard."

        scene 21justascratch with dissolve

        b "Ugn. I feel like my brain has been scrambled inside my skull."
        b "This all feels so unreal."

        p "Yeah, that feeling is going to linger for a few days. Let's just take
        it one moment at a time."

        scene 22justascratch with dissolve

        p "Relax here while I guide the paramedics in. One will be around to check
        on you after they make sure Sharol is stable."

        b "She was so angry at me, Penny. I never knew she was so angry..."

        p "Rest, [player_name]. I'll check on you soon."

        stop music fadeout 2.0

        scene black with fade

        bi "{i}My mind slowly drifted back to reality. There was a piece of
        memory missing between the gunshot and waking up to Penny in front of me.{/i}"
        bi "{i}The paramedics told me the bump on my head wasn't serious.{/i}"
        bi "{i}They'd taken Sharol by ambulance before Avalon came home. She fought
        to understand what had happened for a while.{/i}"
        bi "{i}And then... she cried. A lot.{/i}"

        "24 Hours Later"

        scene 1aftermath with fade

        pause

        play music "audio/heartbeat_of_the_hood.mp3"

        r "I didn't know. I just didn't know. I mean, I knew she was upset but
        I didn't think she was {b}this{/b} upset."

        scene 2aftermath with dissolve

        b "She's been depressed for years. I tried to help but she's stubborn."
        b "I knew she blamed me for Johnny. I feel guilty about that every damn
        day. He was my best friend."
        b "But I didn't know how angry she was about Avalon and I. Heck, I didn't
        even know that she knew about us."

        scene 3aftermath with dissolve

        r "Her and I talked about it. As long as Avalon is happy, tha's all that
        matters. But she just couldn't see it that way."

        b "Avalon and I just sort of happened. I didn't plan it. And I had no
        idea how opposed Sharol was going to be..."

        r "Jesus, man. I'm... I'm real glad you're alright. You must have somethin'
        watchin' over you, [player_name]."

        b "Yeah, I'm not usually superstitious but you could certainly say I
        found a lucky Penny and it saved my life."

        r "What happens now?"

        b "We wait. Hopefully she'll wake up soon."

        scene 1aftermath

        bi "{i}Randall and I spoke to each other a little every once in a while. But mostly,
        we just sat silently.{/i}"
        bi "{i}Sharol had some brain swelling but nothing that seemed permanent.
        It was just a matter of waiting for her to wake up.{/i}"
        bi "{i}And eventually, she did.{/i}"

        scene 4aftermath with dissolve

        sg2 "{i}Ugn. What..? Where am I?{/i}"

        scene 5aftermath with dissolve

        r "Sharol? Baby, are you awake?"

        sg2 "Am I... Am I in a hospital?"

        b "You don't remember?"

        scene 6aftermath with dissolve

        b "You got hit in the head, Sharol. You're recovering right now."

        sg2 "Your face, you... did I do that?"

        b "Yeah, Sharol. You got drunk and you took a shot at me with Randall's
        pistol."

        scene 8aftermath with dissolve

        r "But we ain't worried about that right now. We want you to focus on resting."

        scene 9aftermath

        sg2 "I just got so drunk, I wasn't thinking straight. I can't believe I
        did that."
        sg2 "Am I... am I going to prison?"

        scene 7aftermath

        r "The official story that we gave was that you tripped while you was
        drunk and pinged your head off a countertop."
        r "Ain't nobody know about no gun but us, alright?"
        r "We're gonna get it all figured out, but first you're gonna get better."

        play sound "audio/dooropen.mp3"

        scene 10aftermath

        b "Penny? What are you doing here?"

        scene 11aftermath

        p "Now that Sharol is awake, I'm going to need a few minutes alone with her."
        p "I'll be brief, but this is important."

        scene 7aftermath

        r "I'll be back in two shakes, baby."
        r "And you just holler if you need me."

        sg2 "A-alright..."

        scene 12aftermath

        play sound "audio/doorclose.mp3"

        p "It's nice to finally meet you, Sharol."

        sg2 "Who're you?"

        p "I'm the person that gave you that nasty head injury. It arguably saved
        you and your brother from rather awful fates."

        sg2 "Y-you?"

        scene 13aftermath with dissolve

        p "I managed to pull your arm away just in time. And then I planted a firm
        elbow into your head. I may have used a bit too much force, for which I apologize."
        p "I don't get scared very often anymore. But when I saw you pointing that
        gun at [player_name], I felt it. I felt afraid."

        scene 14aftermath with dissolve

        p "The consequences of his death by your hands would have been considerable."
        p "I could see it, Sharol. Like a reality split off from this one where
        I was just a second too late, I could see it."
        p "I saw Avalon at [player_name]'s funeral, utterly inconsolable. His death
        would go on to ruin the rest of her life, entirely."
        p "And I could see you in prison, haunted by guilt until the day you finally decide to end your own
        life."
        p "Leah would have lived the rest of her life wondering 'What if..?'"
        p "Your actions affect more than you ever truly know."

        scene 15aftermath with dissolve

        p "I know you're in pain, Sharol. I know your husband was taken from you
        and all these years you couldn't move on from his death."
        p "I've felt the pain of loss before too, so when I suspected foul play
        regarding Johnny, I went headlong after the man that did it."
        p "This won't bring you the closure you're hoping it will, but..."

        scene 16aftermath with dissolve

        p "He's dead, Sharol. The man that killed your husband is dead. He
        hanged himself to spare himself from incarceration."

        sg2 "He's dead? You're sure??"

        p "Yeah, I'm sure. I saw it first hand."
        p "I know you don't want to hear this, but Avalon loves [player_name] the
        same way you loved Johnny."
        p "You almost did the same thing to your daughter that Gladstone did to you."

        sg2 "What!? No, she can't... She's just confused!"

        p "She's happy, Sharol. I assure you, she is. Let her be."

        scene 17aftermath with dissolve

        p "There is a fork in the road. You have two paths in front of you."
        p "On one path, you stay angry at the universe for taking your husband from you.
        You'll be miserable, you'll continue to hurt others, and you will die alone."
        p "The other one, you let go of your anger, get sober, and allow yourself
        to be happy again."
        p "I encourage you to take the latter. I have a good friend who is drawing
        up a plan for you as we speak."
        p "If you follow it to the letter, you'll find happiness again. I promise."
        p "I'll have this agenda delivered to your home. You'll find it there when
        you arrive after you're released from here."
        p "Whether you choose to follow it or not is up to you."

        scene 19aftermath with dissolve

        sg2 "I'll look at it."

        p "I lost four of my good friends when I was younger. I felt very
        much as you do now. Angry and alone and hateful."

        stop music fadeout 2.0

        p "I tried to run away from my pain. I decided to stow away on an American
        vessel and head to the States."
        p "I was tucked away in a cubbyhole when a young woman happened upon me.
        How unlikely it was for her to discover me..."

        play music "audio/no_goodbyes.mp3"

        p "I remember her eyes locking onto mine. They were the most beautiful
        eyes I'd ever seen."

        scene 18aftermath with dissolve

        p "She helped me into the country. She gave me shelter and food, and took care of
        me when I couldn't take care of myself."
        p "We fell in love and the world just... washed away. We were completely
        and entirely consumed by one another."
        p "I was able to find happiness again even after all my trauma."
        p "You can too, Sharol. You just have to let people in to help you."

        scene 20aftermath with dissolve

        p "That's all I have to say. I hope you make the right decision."
        p "If you don't, I might not be there to save you next time."

        sg2 "She'll never forgive me..."

        p "She will. Don't let it go to waste."

        scene 21aftermath with fadefast

        play sound "audio/doorclose.mp3"

        sg2 "How could I do that? What the hell was I thinking?"
        sg2 "I'm sorry, [player_name]. I'm so sorry."
        sg2 "Avalon... she'll never forgi--"

        play sound "audio/dooropen.mp3"

        scene 22aftermath

        a3 "Mom? Are you alright?"

        sg2 "Avalon? You're here?"

        a3 "Yeah, Mom. I'm here."
        a3 "You... you shot [player_name], Mom. I know you were angry about us but
        I didn't think you would go that far."
        a3 "What were you thinking?"

        scene 23aftermath

        sg2 "I don't know. I wasn't thinking, Avalon.
        I was drunk and angry. I'm just so afraid he's taking advantage of you."
        sg2 "[player_name] has done nothin' but take things from me my whole life."
        sg2 "I don't want him to take from you too."

        scene 24aftermath

        a3 "Taken from you? What are you talking about, Mom?"
        a3 "What's he taken from you?"

        scene 23aftermath

        sg2 "He took your father away, Avalon. The day after he went searching for
        [player_name]'s father, he wound up dead."
        sg2 "I know it wasn't a coincidence!"

        scene 24aftermath

        a3 "Daddy died trying to help [player_name] find his father. You're twisting
        it to make it [player_name]'s fault, but it's just not."
        a3 "You have to stop doing that. You can't keep blaming other people for
        your misfortunes."
        a3 "I love [player_name]. He was there for me when I was growing up, and
        now he's been there for me through my recovery."
        a3 "We're happy together. And you need to make peace with that if you
        want us to have a relationship in the future."

        sg2 "Y-you'll forgive me?"

        scene 25aftermath with dissolve

        a3 "[player_name] and I are going away for a few days. Even after we
        return, I'm not going to see you right away."
        a3 "You need to get better. If you do that, then... I think I can."
        a3 "I think I can forgive you."

        scene 26aftermath

        sg2 "Okay, I'll try to do better. For you, Avalon. I love you, Sweetie."

        a3 "I love you too, Mom. I'll come visit you in a few weeks."
        a3 "Until then, Randall says he's gonna be around to take care of you."

        stop music fadeout 2.0

        sg2 "Thank you, Avalon."

        a3 "Bye, Mom."

        scene black with fade

        "48 hours later"

        if dallas and monogamy:
            jump senet
        elif octavia and monogamy:
            jump opromance
        else:
            jump nseven

        label senet:

        scene 1senet with fade

        play music "audio/disturbed_mind.mp3"

        d "Penny?"
        d "Am I at the right place?"

        scene 2senet with dissolve

        p "You are! Come on in."
        p "Join me upstairs."

        scene 3senet with dissolve

        d "This place is pretty freakin' cool, Penny."

        p "You like it?"

        d "Yeah, I dig it. It wasn't easy to find though! You're tucked away
        in the woods quite a ways."
        d "But what's with the bunk bed downstairs?"

        scene 4senet

        p "It's unusual, I know. I guess you'd call it nostalgia."
        p "There was a boy several years younger than I that I used to look over."
        p "I slept above him so I could keep a better watch over him."

        d "Oh? Where is he now?"

        p "I found some relatives of his in the States and sent him to live with them.
        I felt he would be safer that way."

        scene 5senet

        d "Do you miss him?"

        p "Terribly. But I visit him from time to time."

        d "You'll have to introduce me one day."

        p "I'll be sure to do that."

        scene 6senet with dissolve

        p "But before we continue with any more conversation, I think a proper
        'Hello' is in order."

        d "Oh? What did you have in mind?"

        scene 7senet with dissolve

        p "Mm."

        scene 6senet with dissolve

        d "We should have more 'Hellos'. A lot more!"

        p "Oh yeah?"

        d "Oh yeah!"
        d "What is that you have set up behind you?"

        scene 8senet

        p "This is a board game called Senet. It was popular thirty-five hundred years
        ago in Ancient Egypt. Would you like to learn how to play?"

        d "I'd love to. Is it complicated?"

        p "It's quite simple actually. My friends and I back home would sometimes
        change the rules slightly to keep things interesting though."

        scene 9senet with dissolve

        d "Some of those pieces look like pawns from Chess. Is this game like
        that?"

        p "It more closely plays like Backgammon, actually."
        p "Please, have a seat."

        scene 10senet with dissolve

        d "How did you stumble upon something like this, Penny?"

        p "I grew up just outside of Egypt. My parents and I
        were vacationing there around fifteen years ago."

        d "It started as a vacation but they decided to move there?"

        p "No, they never returned for me one day. I found out later
        they had been killed by a band of thugs while out picking up breakfast."

        scene 15senet with dissolve

        d "Wait, what? Are you serious? Your parents died while you were
        in a foreign land?"
        d "What did you do? How old were you?"

        scene 16senet

        p "I was nine at the time. I waited for a few days but I was eventually forced
        from the hotel I was staying at due to lack of payment."
        p "They kept all of our things though to make up for the bill. I was left
        with the clothes on my back and no one around to help."

        scene 15senet

        d "Holy shit. That's fuckin' intense! How... I mean, how are you here
        right now?"
        d "You were nine years old? I started working when I was fourteen but
        five years earlier... there's no way I could have figured things out."

        p "It was sink or swim for me. And... I swam."

        scene 13senet with dissolve

        d "You're a beast, girl. That's incredible."
        d "You gotta tell me everything. I mean, there must have been so much
        that happened between then and now, right?"

        scene 11senet

        d "You were nine? And this was fifteen years ago? So you're... twenty-four
        now?"

        p "Yes. And I'll tell you everything, I will. But it's a long story and
        today is supposed to be a relaxing day for me."
        p "I try to take lazy days after stressful events. Recharge the batteries,
        you know?"

        d "Yeah, that stuff with [player_name] was bonkers-ville. Avalon's mom is a looney
        toon."

        scene 13senet

        d "Alright, a lazy day it is! We have plenty of time to get to know each
        other better. Let's play!"

        scene 12senet

        p "So this is a Knucklebone, or a Senet stick, and there are four of them."
        p "You take all four of them and throw them down onto the table."
        p "If one lands with the smooth part facing up, you get a point. A point translates
        into one of your pieces moving one square forward."

        d "So they're like dice?"

        scene 14senet with dissolve

        p "Exactly. I threw down the one I was holding. What we have here is two
        face up, so that's two moves."
        p "If you get three face up, you get to go again."

        d "And if I land on one of your pieces?"

        p "They switch spots unless you're on a safe space, which is any one
        of the hieroglyphs. Save for the squiggly one!"
        p "If you land there, you get transported back to the very middle
        hieroglyph; the ankh."
        p "I've modified the rules for us to keep things simple. We can add more
        of the rules later."

        scene 13senet with dissolve

        d "Okay, sounds reasonable. What happens if I win?"

        p "I'll reward you."

        d "And if I lose?"

        p "I'll punish you."

        scene 17senet with dissolve

        d "That does make things interesting."

        p "I thought you might like that."

        d "Well let's get this party started then."

        p "You'll be the pawns and I'll take the other pieces. Which means you get
        to go first."

        scene 19senet

        p "I told you a bit about my past. Tell me about yours?"
        p "How did you meet Avalon?"

        scene 18senet

        d "I've known her for so long, I barely remember our first encounter."
        d "If I recall correctly, we were assigned a project to do together in
        fourth grade. It may have been fifth grade."

        scene 22senet with dissolve

        d "She was just the same person then as she is now; sweet and innocent."
        d "The project had a competition after everyone finished and we won."

        scene 21senet

        d "After that, we started eating together at lunch and hanging out at
        each others houses after school. The rest is history."
        d "How'd you meet your bunkmate?"

        scene 20senet

        p "He was starving so I shared some of my bread with him."

        scene 25senet with dissolve

        p "I remember him just sitting there, lost inside his own head. So calm
        for being so young."

        d "How old was he?"

        scene 19senet with dissolve

        p "He was five at the time, waiting for his brother to return with food."

        d "Wow, so how old were you at the time?"

        p "I was still nine. It turns out I was quite good at finding clever ways
        to survive. For a few months, I did pretty well on my own."

        scene 18senet

        p "When his brother returned, he saw me sharing my food and asked if I'd
        like to join them. There were three other kids in their group."

        d "What is his name? The one you shared your food with?"

        scene 24senet with dissolve

        p "Cassian. I became rather fond of him over the next several years."
        p "He is... special to me."

        d "Were you... involved?"

        scene 27senet

        p "No, it wasn't like that. My relationship with him is more familial in nature. I was
        very protective of him, especially after his brother perished."

        scene 15senet

        d "Oh, that's terrible. I guess it was pretty rough for you guys, huh?"
        d "But you and he made it out? He must be an interesting man now."

        scene 21senet with dissolve

        d "I hope I get to meet him one day."

        p "I'll be sure to introduce you in the future, Dallas. He lives close by."

        scene 20senet

        p "I can't believe your luck this game."

        scene 25senet with dissolve

        d "You said there were four others, right? Where are they now."

        scene 16senet

        p "When I was nineteen, I returned to our home and they were... murdered."
        p "Raiders attacked while I was on an errand. Cassian was fortunate enough
        to have been out purchasing supplies."

        d "Jesus."

        p "After that, I sent Cassian off to live with his Aunt I'd found a few years prior."
        p "I should have done that earlier, I just... I wanted to keep him close."
        p "Once I knew he was safe, I--"
        p "Well, I finished some business and then headed for the states myself."

        scene 15senet

        d "I shouldn't have pried. I'm sorry. I can't imagine you like talking about that."

        scene 19senet

        p "Really, it's alright. I had support when I came here. And all that feels
        like a past life now."
        p "If you and I are starting something, it's important we know about each other."
        p "Right?"

        scene 18senet

        d "Well, I'm sure you already know a lot about me."
        d "You did some digging when you decided to offer me that salon, right?"

        scene 27senet

        p "I did but I'd rather hear your perspective of things."

        scene 26senet

        d "Oh shit. This is the last piece. Did I..."
        d "Did I win?"

        scene 27senet with dissolve

        p "It looks like you sure did."
        p "I guess that means you get a reward. Is there something in particular
        you'd like, Dallas?"

        scene 28senet

        d "Well there is one thing I've had my eye on since I got here."

        p "Is that right?"

        scene 29senet with dissolve

        d "I want you."

        p "I had a feeling that might be your desire. Shall we move this downstairs?"

        d "You sleep on the top bunk, don't you?"
        d "Show me."

        label bunked:

        scene 30senet with fade

        p "You're not afraid of heights, are you, Dallas?"

        d "I'm far too aroused to be afraid of anything right now. Not even fear
        could distract me from that thirst in your eyes."

        p "There is no amount of willpower in the world that could keep a man or
        woman from being desperate for affection from such beauty, Dallas."
        p "And I mean that both physically and..."

        scene 32senet with dissolve

        p "Mm!."

        scene 31senet with dissolve

        p "What's in that head, too. Mature, confident, independent. You're a
        strong woman, Dallas."
        p "There is nothing more desirable to me than that."

        d "I'm not feeling especially strong right now. In fact, I'm feeling very..."

        d "Vulnerable."

        p "Have you ever tried eating a woman out while she does the same to you?"

        d "I haven't but it sounds exciting."
        d "Show me, Penny."

        scene 35senet with dissolve

        p "This position will allow us to both take care of each other at the same time."

        p "How is the view back there?"

        scene 34senet with dissolve

        d "Pretty freakin' good! I didn't realize how petite your little pussy was
        until now."

        p "No biting!"

        d "I won't bite but I'm way too horny to be gentle."

        p "I'll just have to brace myself, won't I?"

        scene 33senet with dissolve

        p "Let's make a game of it; whoever cums first has to finish off the other."

        p "Try as hard as you can to make me climax before I bring you to orgasm."

        d "I do like to be competitive. You're on!"

        scene 38senet with dissolve

        d "Oh! Your tongue! You move it so fast!"
        d "It feels amazing!"

        p "Try mimicking my tongue-work."

        scene 36senet with dissolve

        p "Mmhmm."

        scene 39senet with dissolve

        p "Ahh. Yeah! Just like that!"
        p "Don't stop, don't stop!"

        scene 36senet with dissolve

        p "Mmm!"

        scene 40senet with dissolve

        d "Gah! How are you getting your tongue so deep!?"
        d "Harder! More!"
        d "Oh, fuck!"

        scene 38senet with dissolve

        p "Ooh shit. Dallas, I'm..."
        p "I'm going to burst!"

        scene 38senet with vpunch

        p "Ahh! Fuck yes!"
        p "Ugn!"

        scene 41senet with dissolve

        d "Wow. That didn't take much. I do like winning but that was too easy!"

        p "I know. I haven't been taking care of myself lately and I'm more
        sensitive to touch than most people."
        p "I just... need to catch my breath."

        d "Why aren't you taking care of yourself?"

        p "I lost interest in masturbating myself after having had a partner for
        many years."
        p "But enough about that, come sit on my face so I can finish you off."

        d "Are you sure!? You still look exhausted!"

        p "Seriously, I'm good. Let's do this."

        scene 43senet with fadefast

        d "Are you comfortable down there?"
        d "Can you breathe?"

        scene 44senet

        p "I can right now but I'm mildly afraid of drowning!"
        p "I can't believe how wet you are right now. You might get my engine
        revving again!"

        scene 43senet

        d "I haven't had someone experienced bury their face in my pussy before."
        d "You have no idea how excited I am!"

        scene 44senet with dissolve

        p "I have a little bit of an idea of how excited you are."
        p "At this angle, I should be able to get my tongue deep inside you."

        d "Oh fuck yes! Do it!"

        scene 46senet with dissolve

        d "You have great tits for being so petite, Penny."

        p "Same could be said for you, tiny Dallas!"
        p "You stand confident which makes you look taller but you must be five foot nothing!"

        d "Less talking, more tonguing!"

        scene 45senet with dissolve

        d "Oh fuck, yeah! You've got it so deep! How is your tongue that long!?"
        d "It's so bumpy and rough! I love it!"

        d "Yes! Taste me, Penny! Lick my pussy clean! Oooh fuck!"

        scene 47senet with vpunch

        d "Daah! I'm cumming!"
        d "Keep going! Press harder! Go deeper!"
        d "Ahh!"

        scene 49senet with fadefast

        d "Ugn. I am spent, girl. I am fuckin' dead right now."
        d "That was awesome! Goddammit, I have needed some good sex!"

        p "I agree. Talk about the best stress reliever."

        scene 48senet with dissolve

        if persistent.bunked == False:
            $ renpy.notify("You've unlocked 'Bunked' in the Scene Gallery on the Main Menu!")
            $ persistent.bunked = True

        p "Do you want to stay the night? I could use the company."

        d "I don't think I could leave even if I wanted to."
        d "My legs are completely numb!"

        scene 50senet with dissolve

        p "But do you want to stay?"

        d "Oh hell yes I want to stay!"

        stop music fadeout 2.0

        $ renpy.end_replay()

        jump nseven

        ## Octavia Mono-Path, Last Scene. ##

        label opromance:

        scene thedoll15

        play music "audio/tomorrows_rain.mp3"

        p "Hey, Octavia! I let myself in. I hope that's alright?"

        o2 "My home is your home, Penny."

        p "Is Maize here? I've missed her. Is she upstairs?"

        scene thedoll14

        o2 "Maize is with one of her handlers today. I wanted to speak to you
        alone without interruption."

        p "Does it have something to do with that doll you have beside you?"

        o2 "It does. Please, have a seat."

        p "Alright then."

        scene thedoll13 with dissolve

        o2 "About a year ago, I ended our relationship but I never gave you a proper
        reason as to why."

        p "Oh I remember. Everything between us was going so well, I was certainly
        perplexed by your termination of our relationship."
        p "You came back from a mission overseas one day and you were... different."

        o2 "I shouldn't have pushed you away. And I especially shouldn't have done
        so without giving you a proper reason."

        scene thedoll12 with dissolve

        o2 "This doll is part of the reason. Or, at least, a representation of
        the reason."

        p "It's rather plain-looking. Was it a gift from someone?"

        o2 "It was supposed to be a gift for someone."

        scene thedoll11 with dissolve

        o2 "I joined the military to travel and promote diplomacy and peace around
        the world."
        o2 "I dreamed of convincing foreign dictators to work together, take care of
        their citizens and implement social wellness programs for their society."
        o2 "I wanted to show everyone the benefits of cooperating. Everyone
        gets more when we collaborate together!"

        scene thedoll07

        p "Uh huh. I remember the first time you told me that. It's what made me
        fall in love with you."
        p "I had spent so many years just trying to survive. And then, just as
        I was ready to give up, I woke up to you."
        p "You cleaned me up, gave me food and clothing, and you gave me hope. I'd
        never had a White Knight before. I was absolutely smitten."

        scene thedoll09

        o2 "Is that so? You were rather stoic the first time we spoke."

        scene thedoll10 with dissolve

        o2 "A lot happened between then and now. I couldn't manage to change the
        world as I'd hoped to."

        o2 "Just before the end of our relationship, I was stationed in Africa to
        help facilitate a deal between the United States and a mining company there."

        scene thedoll11 with dissolve

        o2 "I was picking up supplies at a local convenience store when I noticed
        a little girl drooling over a candy bar she couldn't afford."
        o2 "So I bought her two!"
        o2 "Her mother invited me over to their home for supper as a 'Thank you'.
        How could I refuse?"

        scene thedoll10 with dissolve

        stop music fadeout 2.0

        o2 "When I arrived, they offered me a slice of stale bread. It's all they had."
        o2 "Can you imagine that, Penny? All that we've accomplished as a collective
        and they have to live with so little..."

        scene thedoll08

        play music "audio/a_way_out.mp3"

        p "I can imagine that, actually. I lived that way for a while."
        p "You tried to help, didn't you?"

        scene thedoll09

        o2 "I had to try, Penny. How could I not?"
        o2 "I gave them all the money I had on my person. It wasn't even much,
        a few hundred dollars."

        scene thedoll08

        p "That's probably more than their entire household made in a year, Octavia."

        scene thedoll10

        o2 "But it was nothing to me. And so much to them."
        o2 "I came back the next day with groceries for them and this little doll
        for the young child."
        o2 "They... they were..."

        scene thedoll08

        p "They tried to spend the money and someone noticed."
        p "And they wanted that money for themselves, didn't they?"

        scene thedoll04

        o2 "They burned them alive, Penny. The mother, the father..."
        o2 "And the child."
        o2 "What kind of world do we live in that people could do such a thing?"
        o2 "And they did it over just a few dollars, Penny!"

        scene thedoll06

        p "You saw the worst of people and it took the fight out of you."

        o2 "I can't save the world. I couldn't even save that little girl..."
        o2 "And I couldn't face you, Penny. After I gave up on the world, I
        couldn't face you."

        scene thedoll03 with dissolve

        p "Do not despair, my love."

        scene thedoll02 with dissolve

        stop music fadeout 2.0

        p "Humanitiy is on a path and a single person cannot alter it."
        p "But you have helped so many and inspired many others."
        p "It wasn't your ability to save people that I fell in love with. It was
        your desire to save people that captured my heart."

        scene thedoll01

        p "Do you remember when you found me?"
        p "I felt the same way; hopeless. I'd given up."
        p "And you rescued me, Octavia. Do you remember..?"

        scene stowaway77 with fade

        play music "audio/tomorrows_rain.mp3"

        o3 "Hello? Is someone in here?"
        o3 "I heard someone sneeze while I was walking by."
        o3 "If there's someone here, please announce yourself."

        scene stowaway76

        o3 "If this is a prank, I'll warn you that I'm a trained combatant!"

        scene stowaway75 with dissolve

        o3 "If you leap out at me in an attempt to scare me, I may attack!"
        o3 "... Huh. There's nobody here."

        scene stowaway74 with dissolve

        o3 "I guess I was hearing things. A ship this large can be pretty spooky
        sometimes."

        "Achoo!"

        scene stowaway73

        o3 "Alright, now I know I heard someone sneeze!"
        o3 "Come out of there!"
        o3 "If I have to come in after you, it will not be a pleasant experience
        for you!"

        scene stowaway71 with vpunch

        po "sa'udafie ean nafsi."

        scene stowaway70 with dissolve

        o3 "Oh my goodness!"
        o3 "Is that Arabic? How did you get in here? How long have you been hiding
        here?"

        scene stowaway69

        o3 "You're covered in filth and clearly dehydrated. You may be sick as well."
        o3 "Do you speak English? Can you tell me what you're doing here?"

        scene stowaway68

        o3 "It's alright, I'll help you."
        o3 "You must be starving. I have food and water I can give you."
        o3 "You're not here to hurt anyone, right? You're just trying to survive."

        scene stowaway67

        o3 "You can trust me. I want to help you."
        o3 "Take my hand. Go on, I don't bite."

        scene stowaway66

        po "Ugn..."

        o3 "Careful!"

        scene stowaway65 with vpunch

        o3 "I got you! Oh, you poor thing. You must be terribly malnourished."
        o3 "Let's get you back to my bunk where we can get you cleaned up."
        o3 "We'll have to be careful; we can't let anyone know you're here..."

        scene stowaway64 with fadefast

        o3 "I've cleaned you up and put you into some clean clothes but that's all I
        can do for now."
        o3 "There was a beautiful young lady under all that grime, wasn't there?"

        scene stowaway63 with dissolve

        o3 "Rest now and get better. I'm so eager to hear your story."
        o3 "We have to be careful now; if they find out I'm harboring a stowaway,
        I'll be in a considerable amount of trouble."

        scene stowaway62 with dissolve

        o3 "I hope I don't regret helping you. But how could I turn away someone
        so desperately in need of help?"
        o3 "I have no idea what to do with you now though."

        scene stowaway61 with dissolve

        o3 "I guess we'll figure it out when you wake up, won't we? One step at a time."

        scene stowaway60 with dissolve

        o3 "I guess I better get some rest myself. Everything will work out."

        scene stowaway59 with dissolve

        o3 "Yeah, we're going to be just fine, young lady. Everything will work out."
        o3 "For both of us."

        scene stowaway58 with fadefast

        pause

        scene stowaway57

        pause

        scene stowaway56

        pause

        scene stowaway55

        pause

        scene stowaway54 with vpunch

        po "la! la tamut min fadlika!"
        po "la ymkn 'an yakun hqyqyana!"

        scene stowaway53 with dissolve

        po "'ana faqat 'urid 'an 'arah maratan 'ukhraa."
        po "'ana faqat aryada..."

        scene stowaway52 with dissolve

        po "Ugn..."

        scene stowaway51 with dissolve

        pause

        scene stowaway50

        o3 "Oh you poor thing. What happened to you?"
        o3 "I'm not sure if you're suffering from sickness or..."
        o3 "From a broken heart."
        o3 "I hope we're able to communicate when you wake up."

        scene stowaway49 with fadefast

        o3 "I could only sneak out some strawberries from the cafeteria."
        o3 "I hope the young lady wakes up soon so I can get some food into her belly."

        scene stowaway48 with dissolve

        o3 "Oh! You're awake!"
        o3 "I'm so glad, I was worried I'd have to get nourishment into you intravenously."
        o3 "How are you feeling? Are you in any pain?"

        scene stowaway47

        o3 "I have some medicine if you're feeling any discomfort."
        o3 "Hmm... Perhaps you can't understand me."

        scene stowaway46 with dissolve

        o3 "Here you are. Some food so you can get your strength back."
        o3 "Go ahead, take them. I brought them just for you."

        scene stowaway45 with dissolve

        o3 "If you're especially thirsty, I can get you some water too."
        o3 "Here you are."

        scene stowaway44 with dissolve

        o3 "They're really good, I promise. We have to keep them frozen so they stay
        fresh but you can't even tell they were frozen."
        o3 "I know you'll probably want more than that but I don't want you to eat too
        much too fast."

        scene stowaway43

        o3 "I've heard stories of starving children being given too much food all
        at once and they eat so fast, they hurt themselves!"
        o3 "But if you want--"

        scene stowaway42 with dissolve

        stop music fadeout 2.0

        o3 "Hm? What's this?"
        o3 "Are you offering me one?"

        scene stowaway41 with dissolve

        o3 "That's alright. I've had plenty to eat today."
        o3 "You're welcome to have that entire bowl all to yourself. I really don't mind."

        scene stowaway40 with dissolve

        o3 "Wait a moment, you're not offering that to me out of generosity, are you?"
        o3 "You're afraid I've poisoned it!"

        play music "audio/aint_it_funny.mp3"

        scene stowaway39

        o3 "Okay, if you insist, I'll have one just to prove I didn't mess with it."
        o3 "You took the leaves off of it and everything. How kind of you."

        scene stowaway38 with dissolve

        o3 "Aaah."

        scene stowaway37 with dissolve

        o3 "Omn. Mm. Yeah, that's a good berry."
        o3 "It's very sweet and juicy. Mm. I may have gotten the best of the entire
        bunch."
        o3 "I bet you regret giving it me now, don't you?"

        scene stowaway36

        o3 "They look awfully delicious, don't they?"

        scene stowaway35 with vpunch

        o3 "Oh no! I must have gotten one of the poisoned ones!"
        o3 "My plan has backfired!"
        o3 "Now I'm going to perish because I decided to poison you after you woke
         up instead of just offing you while you were asleep."

        scene stowaway29

        o3 "I'm like one of those terrible villains in a cheesy action spy movie!"
        o3 "Woe is me, woe is me! I'm dying from, you know, the poisoned berry!"

        scene stowaway30 with dissolve

        o3 "I have only one request; don't let anyone know I went out like this."
        o3 "Tell them I died heroically saving a kitten or something."

        scene stowaway31 with dissolve

        o3 "Oh no, everything is getting dark. I can feel death's embrace."

        po "Mhmm."

        o3 "Here I go. I'm dying."

        scene stowaway34

        o3 "Hm?"

        scene stowaway33 with dissolve

        play sound "audio/swallow.mp3"

        "*Gulp*"

        scene stowaway32 with dissolve

        o3 "Just kidding!"
        o3 "I almost had you going there, didn't I?"

        stop music fadeout 1.0

        scene stowaway28

        po "I wasn't worried they were poisoned. I can't recall a time I slept
        that long or that deeply."
        po "I thought perhaps I was being sedated. I see now I was mistaken."

        scene stowaway27 with dissolve

        play music "audio/tomorrows_rain.mp3"

        o3 "She speaks! And in fluent English as well."
        o3 "Color me impressed."

        po "That's an interesting turn of phrase. I had not heard that one before."

        o3 "Well, you're welcome to have it, if you'd like. It's all yours!"

        scene stowaway26

        o3 "I'm Octavia, by the way. Is there a name you'd like me to call you?"

        po "Si-- Ehem. You can call me..."
        po "Hmm. How about Penny?"

        o3 "Alright. It's nice to meet you, Penny."

        scene stowaway25

        po "That was an entertaining performance, Octavia. Albeit, a touch dramatic."

        o3 "Oh you liked that?"

        po "Dinner and a show. What's not to like?"

        scene stowaway24 with dissolve

        po "I can't help but wonder; why did you help me? You should have turned
        me in."
        po "What if they find me in your room? You'll surely be punished."
        po "There's no benefit here for you."

        scene stowaway26 with dissolve

        o3 "I'd be happy to explain it to you."
        o3 "First I'd like to know why you're on a United States Navy Aircraft
        Carrier. And how did you even manage to get aboard?"

        scene stowaway24

        po "I'm trying to make my way to a friend that I sent off to America."
        po "I made a promise, both to him and myself, that I'd see him again. And
        make sure he's doing well."

        o3 "Ooh, a boy, huh?"

        scene stowaway25 with dissolve

        po "Don't mistake my affection for him as romantic interest. He is special
        to me but our bond is more familial in nature."
        po "I took care of him as he grew up. I favored him over my other group mates."

        o3 "It sounds like a motherly love."

        po "I suppose it is."

        scene stowaway27 with dissolve

        po "And now your reason for helping me?"

        o3 "Oh yes. Let me explain."

        scene stowaway22 with dissolve

        po "Hm?"

        o3 "Would you mind if I sat with you?"

        po "That's fine."

        scene stowaway19 with dissolve

        o3 "When I found you in the locker, you were filthy and sickly."
        o3 "You didn't strike me as having malicious intent. You just looked...
        desperate."
        o3 "I can only deduce that determination was to make it to America to
        see that boy."
        o3 "You posed no threat to me in the condition you were in."
        o3 "I wanted to know your reason for being aboard this vessel before making
        a decision I couldn't retract later."

        scene stowaway17

        po "You wanted to judge me for yourself. Does that mean you think you're a
        better judge than your judicial system?"
        po "It sounds as if you don't trust your own people to make the best decisions."

        scene stowaway20

        o3 "That's a rather unusual way to look at it. You're not entirely wrong."
        o3 "We have universal laws that apply to everyone equally."
        o3 "Though I'm of the opinion that everyone should be judged based on their
        unique circumstances."
        o3 "If two ducks quack, which one do you have for dinner? The one that quacks
        to alert you to danger or the one that wakes you up in the middle of the night?"

        po "Both, I'd imagine. Duck is delicious."

        o3 "No, neither! You simply teach the obnoxious duck not to quack in
        the middle of the night!"

        scene stowaway17

        po "You speak of redemption. Not everyone can be redeemed. Sometimes
        it's best to simply remove someone from society."

        o3 "Every life has worth, Penny. And everyone can be taught. It's the
        responsibility of our community to teach the value of moral decency."

        po "So you're saying if you'd rescued me and found out I was responsible
        for malicious and terrible acts,"
        po "you would take it upon yourself to teach me the errors of my ways and set me on a
        righteous path?"

        scene stowaway20

        o3 "I'd sure try!"

        po "And what if you failed and I hurt someone? Or many people?"

        o3 "And what if I did help you and instead you went on to save thousands of lives??"
        o3 "We can't predict the future but we can do our best to be good to one another.
        And if we all work together, imagine the wonders we could create!"

        scene stowaway18 with dissolve

        o3 "That's what I want to do, Penny. I want to make the entire world
        a better place. For everyone!"
        o3 "I want to show people the benefits of community and sharing."
        o3 "And through unity, I want to see how magnificent our collective can
        become!"
        o3 "Think of it, Penny. Think of the wonders we could create, all that
        we could explore, and everything we could learn. But we have to work together!"

        scene stowaway14

        po "Er... I..."
        po "That's a lot of passion, Octavia."
        po "You believe you can influence the entire world that much?"

        scene stowaway20

        o3 "I'm sure I can! Absolutely!"
        o3 "And who knows, maybe you'll be there to help me."

        scene stowaway15

        po "Er. No, I..."
        po "I mean, I don't have..."

        scene stowaway13 with dissolve

        po "Ehem. Is that a shower? Would you mind if I used it?"

        o3 "Oh, the shower..? Yes, you can use it."

        scene stowaway12 with dissolve

        o3 "Of course you can. There should be plenty of hot water as well."

        po "Thanks. I shouldn't be long."

        scene stowaway11

        o3 "Sure. It can be a little complicated in there. Just turn the--"

        scene stowaway10 with dissolve

        po "I'm sure I can figure it out."

        o3 "Oh. Alright. Just let me know--"

        scene stowaway09 with dissolve

        o3 "Woah! I should, um, give you some privacy."
        o3 "I will find you a towel and leave it on the bed for you."
        o3 "If you need anything, just shout. I'll be in the living area."

        scene stowaway08 with dissolve

        o3 "Wow. You are not shy at all."
        o3 "That surprised the heck out of me..."

        scene stowaway07 with dissolve

        pause

        scene stowaway06 with dissolve

        pause

        scene stowaway05 with dissolve

        pause

        scene stowaway00 with dissolve

        stop music fadeout 2.0

        pause

        scene stowaway04 with fade

        pause

        scene stowaway03 with vpunch

        po "Hey!"

        o3 "Gah!"

        po "What are you doing?"

        scene stowaway85 with dissolve

        o3 "I'm going to sleep so I can be rested for tomorrow."

        po "There's plenty of room on the bed for both of us. There's no
        reason for you to sleep on the floor."

        o3 "Oh no, it's fine. Really. I don't mind."

        po "I will not deprive you of your bed, Octavia. I won't take 'No' for
        an answer."

        o3 "In that case, I suppose it would be fruitless to argue with you."

        scene stowaway01 with dissolve

        o3 "Are you comfortable? I can scoot over more."

        po "I have plenty of room. And... Octavia?"

        o3 "Yes?"

        po "Thank you. Seeing {i}him{/i} again is the only thing that kept me going."
        po "It means a lot that you're helping me make that happen. In fact, it means the world to me."

        o3 "You're welcome, Penny. It sounds like he's a very lucky young man to have you in his life."

        po "Once upon a time, perhaps..."
        po "Anyway, good night, Octavia."

        o3 "Good night. Penny."

        label mre:

        stop music fadeout 2.0

        scene stowsex01 with fade

        pause

        scene stowsex02 with vpunch

        po "Octavia."

        o3 "Gah!"

        scene stowsex03 with dissolve

        o3 "What happened? Is something wrong? Was I snoring?"

        po "No. Everything is fine. I just wanted to tell you that you surprised me
        earlier with what you said. I didn't know how to respond."
        po "Where I came from, we didn't have time to think about healing the world."
        po "It was hard enough just to take care of ourselves."
        po "But I want that too. I've watched those that I love live in poverty and in
        pain. I don't want others to have to go through that too."

        scene stowsex04 with dissolve

        o3 "Is that so? You were so stoic, I wasn't sure how my speech was
        received."
        o3 "I'm glad to hear you want to help too. But I believe right now, you
        need rest. You're still very weak from dehydration and malnutrition."
        o3 "Assuming we manage to get you into the States, I'd be happy to give
        you the tools to do some good in the world."
        o3 "I still don't know anything about you though. How do I know you're
        not just buttering me up?"

        po "Everyone I care about was murdered save for one person. Today was the first
        day in months that I didn't feel like I was drowning in despair."

        scene stowsex03 with dissolve

        o3 "E-everyone? How..?"

        po "I don't want to dwell on my past right now. I want to revel in the gift
        that you've given me today."

        o3 "What gift is that?"

        po "Hope."

        scene stowsex05 with dissolve

        play music "audio/your_hand_in_mine.mp3"

        o3 "Mmh."

        scene stowsex06 with dissolve

        o3 "Oh my. I don't think this is a good idea, Penny. We barely know each other,
        we just met."

        po "I know enough. I want this. Do you want this?"

        o3 "It has been a while since I've been with anyone. Being in the
        military has made it difficult to find companionship."

        scene stowsex07 with dissolve

        po "So let's enjoy each other. For one night, we can forget our tragedies
        and lose ourselves in a primal indulgence."
        po "What do you say?"

        o3 "It would be hard to say 'No' to that."

        po "Let's get you out of those clothes then, Octavia. We can get to know
        each other... intimately."

        o3 "Such a clever young woman you are. And persuasive to boot."

        scene stowsex09 with fadefast

        o3 "Alright, Miss Penny, you've got me disrobed. Now what would you like to
        do?"

        po "You're in excellent shape. You must take care of yourself."
        po "I'm rather jealous, I've let myself go over the last few months."

        o3 "I suppose I'll just have to whip you back into shape."

        scene stowsex08

        po "I do like the sound of that. Perhaps you should go easy on me tonight though."
        po "You wouldn't want to break your new playmate, would you?"

        o3 "I'm not sure I could if I tried. I can tell that you're exceptionally hardy."

        po "In that case, perhaps don't go easy on me."

        scene stowsex10 with dissolve

        po "What's that around your neck? It has your name on it."

        o3 "My dog tags? It's so that if I'm wounded or killed, I can be easily
        identified if someone finds me."

        po "You don't have to worry about that. I'll keep you safe."

        o3 "Is that so? Do you usually play the protector, Penny?"

        po "Usually. I'm predominantly quite formidable."

        o3 "I don't doubt that."

        scene stowsex11 with dissolve

        po "Mmh."

        scene stowsex12 with dissolve

        po "Lean back."

        o3 "Oh? Alright. Do you prefer being on top, Penny?"

        po "I prefer to be the one in control. It's rare indeed for me to be
        vulnerable in the way you found me."
        po "But tonight is not about control. It's about losing control, giving in
        and it's about..."

        show prepstowrub with dissolve

        po "Pleasure."

        o3 "Wow. I haven't had someone touch me like this in a long time. It's
        exhilarating, to say the least!"

        po "I've had to abstain from sex for a long time. It's thrilling to
        finally be able to let myself indulge."

        o3 "Abstinence? W-why?"

        po "As the leader of my group, I needed to command their respect and
        obedience. Romance would only serve to complicate that role."

        o3 "It sounds as if you speak from experience?"

        show pstowrub with dissolve

        po "Let's focus on each other for now. We can get to know one another
        later."

        o3 "Ooh, you're quite vigorous with your hand now. It feels exceptional!"

        po "It's not too much, is it?"

        o3 "No, keep going. Keep going!"

        po "I'm... I'm becoming rather exhausted actually. I may have overestimated
        my strength here."

        o3 "It's okay, it's alright. You can stop. In fact, I think perhaps it's my
        turn."

        scene stowsex15 with vpunch

        po "Ouch."

        scene stowsex16 with dissolve

        po "Not so rough. I'm still on the mend here."

        scene stowsex17 with dissolve

        o3 "I apologize, Penny. I guess I got a little too excited there."

        po "Normally I wouldn't mind a little roughness."

        o3 "You did your best to please me. Now it's my turn to please you."

        scene stowsex18 with dissolve

        po "Yes! Wow! You have so much control over your tongue. I can feel it
        wriggling inside me!"
        po "Oh, that! Keep doing that! Keep flicking my clitoris with your tongue!"
        po "Now gently suck on my clit. Y-yes, like that! Don't stop!"

        scene stowsex19 with vpunch

        po "Ahh! I'm exploding! I'm cumming!"

        o3 "Goodness! So intense!"

        po "I can't... I can't stop shuddering."
        po "I'm so depleted and satisfied at the same time. Ugn!"

        scene stowsex20 with dissolve

        po "Dah. Wow! That was just spectacular. For claiming to be so lonely
        lately, you sure do know how to eat a girl out."

        o3 "It's like riding a bicycle, I suppose. You never forget how."

        if persistent.mre == False:
            $ renpy.notify("You've unlocked 'MRE' in the Scene Gallery on the Main Menu!")
            $ persistent.mre = True

        po "I'm sorry I wasn't able to reciprocate fully. I overestimated my energy
        level. I still need more time to recover."

        o3 "You need more sustenance too. Why don't we sleep for now and I'll
        bring you food in the morning."

        po "You're good people, Octavia. Thank you."

        $ renpy.end_replay() ## End Replay ##

        scene stowsex21 with fadefast

        pause

        scene thedoll01 with fade

        p "I fell so deeply in love with you that night. I think about it all the time,
        I cherish that memory."
        p "Humanity has its own destiny, Octavia. We will play such a small
        role in that, no matter what we do."
        p "You may not be able to save the world, but you mean the world to me."
        p "You saved my life, you gave me a second chance. You showed me I could
        still have a future and that I could be happy."

        o2 "Oh, Penny..."

        p "Be with me. Let's make each other happy again. We can work together to
        find a way to put some positivity out there in the world."

        p "I love you, Octavia."

        o2 "I love you, too. And thank you, Penny. I needed this."

        jump nseven


        label nseven:

        scene 1nseven with fade

        play music "audio/your_hand_in_mine.mp3"

        b "This thing weighs a ton, Avalon. You know we're only going to be gone
        for a few days, right?"

        a3 "You didn't tell me where we were going so I packed... I don't know, everything?"

        b "I wanted it to be a surprise. Are you surprised?"

        a3 "Is it a vacation home or--"

        scene 2nseven with dissolve

        a3 "Whoa, what?! No way! Is that real, Uncle!?"

        b "Yeah, it's real. Real expensive! We're going to have to be frugal
        with our finances until next year after this vacation."

        a3 "It's going to be so worth it though!"

        scene 3nseven

        a3 "Come on, Uncle! Let's go see it!"

        b "Watch out for crabs! And seagulls!"

        a3 "What about sharks!?"

        b "Oh there's only one shark you have to be concerned about, Avalon."

        a3 "Ahaha. You're such a goon!"

        scene 4nseven with dissolve

        a3 "Wow! It's been forever since I've been to the beach.
        I don't remember it being this incredible!"

        a3 "And it's right in the backyard!? Can you imagine waking up to
        this everyday? That would be amazing!"

        scene 5nseven with dissolve

        b "You like it?"

        a3 "Yeah! And the sky is so clear, there's not a cloud up there. This
        is the perfect weekend for a beach vacation."

        b "You want to check out the inside?"

        a3 "Sure!"

        scene 6nseven

        a3 "Ooh. You know it's an expensive couch when it's curved like this!"

        b "Is that how nice things work? They're more valuable if they're crooked?"

        a3 "Yeah, I think so!"

        scene 7nseven with dissolve

        a3 "It's so soft! It must be so expensive!"

        b "And you're rubbing your dirty shoes all over it. I hope I don't have
        to pay extra if we leave this place filthy when we leave."

        scene 8nseven with dissolve

        a3 "I could fall asleep right here, Uncle. Doesn't a nap sound wonderful?"

        b "It's a small couch. If we slept together on it, I'd have to sleep on
        top of you."

        scene 9nseven with dissolve

        a3 "Join me, come sit down."

        scene 10nseven with dissolve

        if octavia:
            a3 "Why didn't you invite Octavia to join us? She would love it here."
            a3 "She always likes to be close to water wherever she lives."

        else:
            a3 "Why didn't you invite Dallas to join us? She'd be as ecstatic as
            I am to be here."

        b "She insisted that I spend the first day alone with you. She said she'll
        come tomorrow to spend the day with us."
        b "She is worried about you. I'm worried about you too.
        How are you holding up after everything?"

        scene 14nseven with dissolve

        a3 "Every time I think about it, I see your face again. I see the scratch
        from the bullet on your cheek."
        a3 "I see it in my head and I can't stop thinking that I've never felt so lucky
        in my entire life."
        a3 "That scratch was a winning lottery ticket for us. It was a miracle."

        scene 16nseven

        b "I still can't believe it myself. I thought for sure I was dead."
        b "In fact, I think I hallucinated when I fell backwards and hit my head."
        b "I saw your father."

        a3 "W-what?"

        b "I saw Johnny when I was unconscious."

        scene 15nseven with dissolve

        b "He was just as positive as ever. Just as positive as you."
        b "Your dad said he'd have given anything to watch you grow up."
        b "And he asked me to forgive Sharol. So I'm... I'm going to try."
        b "I mean, I think it was just a dream but something about it felt so real."
        b "So I'm going to try to forgive her."

        scene 14nseven

        a3 "Penny asked the same of me. She said I should give my mom another
        chance."
        a3 "How could I refuse? She saved your life, I owe her so much..."

        scene 13nseven with dissolve

        a3 "But she has to earn it! She can't just keep going like this anymore."
        a3 "Mom either gets her shit together or she can't be a part of our life."

        scene 15nseven

        b "I don't want to worry so much about this right now. This is our vacation."
        b "Why don't we change and go get some sun? What do you think?"

        scene 12nseven

        a3 "You just want to see me in a bikini!"

        b "A bikini? Avalon, this is a nude beach. We have to go out there naked!"

        a3 "You're a liar! You're so bad!"

        b "Okay, you got me."

        scene 11nseven with dissolve

        a3 "Let me go change and I'll meet you out there."
        a3 "And... thanks, Uncle. This was a great idea. I'm excited to spend
        time alone together."

        b "Me too."

        scene 18nseven with fadefast

        ai3 "{i}Okay, I brought my skimpiest bikini! And it has no straps so when
        I ask him to put lotion on me, he'll have easy access to my chest.{/i}"

        ai3 "{i}I can't wait to feel his big, strong hands rubbing lotion all
        over my exposed body. Oof!{/i}"

        ai3 "{i}I'm getting too excited. I hope you're ready for all this sexiness,
        Uncle!{/i}"

        scene 19nseven with dissolve

        ai3 "{i}Oh it looks like he's already out there.{/i}"
        ai3 "{i}I swear, if he makes one more shark joke, I'm gonna bite him!{/i}"

        scene 20nseven

        stop music fadeout 2.0

        b "Oh yeah, this is the life."

        b "I think we might be moving here permanantly, Avalon."

        scene 21nseven with dissolve

        a3 "We would run out of money in like, one year."

        b "Worth it."

        a3 "You're not going to fall asleep out here, are you?"

        b "I'm obviously already asleep because the girl of my dreams is here."

        a3 "Ooh, here I thought you were a grizzly bear but you're obviously a..."

        b "Here it comes."

        a3 "Camembert!"

        b "Your cheese comments are cheesier than my cheesy jokes, Avalon."

        scene 22nseven with dissolve

        a3 "Mm, you were right. This is nice! I might fall asleep too."

        b "I know, right?"

        a3 "Oh but I'll burn if I do. What can I do to prevent that?"

        b "I brought some suntan lotion. Do you need it?"

        ai3 "{i}Yes, here's my chance!{/i}"

        scene 23nseven with dissolve

        play music "audio/aint_it_funny.mp3"

        a3 "Um, can you put it on me, Uncle?"

        b "Eh?"

        a3 "You know, the lotion. Can you put it on me?"

        b "Oh, uh, sure."

        scene 24nseven with dissolve

        b "Let me just grab it here."

        ai3 "{i}Oh my god, this is going to be so hot. Rub it on me, Uncle.
        Rub it all over me!{/i}"

        scene 25nseven with dissolve

        b "Are you sure you want me to put it on you?"

        a3 "Oh yeah."

        b "Alright. Here you go."

        scene 26nseven with dissolve

        b "Heads up!"

        a3 "Huh? Heads u--"

        scene 27nseven with dissolve

        a3 "Oof!"

        b "There you are. I put it right on your stomach."

        scene 28nseven with dissolve

        a3 "That's not what I meant, Uncle!"
        a3 "I wanted you to rub it on me!"

        b "You should have been more specific."

        scene 29nseven with dissolve

        a3 "Take it back and do it right!"

        b "What? Take it ba--"

        scene 30nseven with vpunch

        b "Ow!"

        a3 "Oops! I'm sorry! I didn't mean to do that."

        scene 31nseven with dissolve

        b "You're so dead, Avalon!"

        a3 "Oh shit!"

        b "Don't run, you'll only die tired!"

        a3 "Not if I get away!"

        scene 32nseven

        b "There's hell to pay now! You're goin' down, Girlfriend!"

        a3 "You're too slow, Uncle! I was a cheerleader and you're fat!"
        a3 "You'll never catch me!"

        b "You're only making things worse for yourself!"

        scene 34nseven with dissolve

        b "Do you know what happens to bad girls, Avalon?"

        a3 "They get ice cream!"

        scene 33nseven

        b "No, they don't get ice cream. They get punished!"

        a3 "I've never heard that before. I think you're mistaken!"

        b "No, I'm sure!"

        scene 34nseven with dissolve

        a3 "What are you going to do to me if you catch me, Uncle?"

        b "Oh, I have some ideas."

        a3 "Is that right? Well, you'll have to catch me first!"

        scene 35nseven

        b "You can't get away, Avalon! Even if you're faster, I have the stamina
        of a stag!"
        b "I'll get you eventually!"

        ai3 "{i}Oh, I'm counting on it. Keep chasing me, Uncle. Chase me right
        into the bedroom...{/i}"

        scene 36nseven with fadefast

        play sound "audio/doorclose.mp3"

        b "It's a dead end, Avalon. There's no way out of here except through
        this door."

        b "I hope you're prepared for your pun--"

        scene 37nseven with dissolve

        b "Gah! What are you doing?"
        b "Why are you... erhm.."

        scene 38nseven with dissolve

        a3 "Topless?"
        a3 "I thought maybe you could find it in your heart to forgive me?"
        a3 "I hear boobs can have a hypnotic effect on some men. Perhaps you forgot
        why you were chasing me at all?"

        b "Nope, I remember. You're still getting punished."

        scene 39nseven with dissolve

        a3 "Wait, what?"

        b "Naughty girls get punished, Avalon. I don't make the rules, I just don't
        argue with them."

        a3 "What are you going to do to me, Uncle?"

        b "Oh something terrible, Avalon. I'm going to..."

        show tickle

        b "Tickle you to death!"

        a3 "Ahaha. Stop, stop! It's too much!"

        b "I know all your ticklish spots, Avalon."

        a3 "Show mercy, Uncle! Ahaha!"

        b "Are you sorry for hitting me in the face with suntan lotion?"

        a3 "Yes! I'm sorry, Uncle! Ahaha. I didn't mean to!"

        stop music fadeout 2.0

        scene 42nseven with dissolve

        b "Okay, I guess you can live. Since you apologized so desperately."

        a3 "You're so generous. Thank you."

        b "Seriously, why did you take your top off? I didn't bring you
        here just trying to get lucky."
        b "We can just relax this weekend."

        scene 43nseven with dissolve

        play music "audio/touching_moment.mp3"

        a3 "I know, Uncle. It's just that... I don't know how long we have together."
        a3 "You almost died a few days ago. What if we keep waiting and then..."

        scene 44nseven with dissolve

        b "You're worried about that? But the odds are so slim. We'll
        probably never run into a situation like that again."
        b "We'll have years together, Avalon. Decades. We'll be fine."

        scene 47nseven

        a3 "You don't know that..."
        a3 "You can't know that!"
        a3 "Ever since we got together, our lives have been chaotic."
        a3 "What if the same thing that happened to mom happens to me? What if I
        lose you? I won't ever heal from that. I won't ever recover!"

        scene 46nseven

        b "I worry about things too, Avalon. I worry that maybe I'm a bad influence
        on you."
        b "I mean, I'm technically your Uncle. That's so taboo, we're not supposed
        to be together."
        b "What if there are consequences later that we don't see right now?"

        scene 49nseven

        a3 "You feel that way? Do you regret being with me?"
        a3 "I couldn't bear it if you said you did!"

        scene 45nseven

        b "Not for a second. I'm the happiest I've ever been and it's because
        of you."
        b "And we make a good team. We take care of each other."

        scene 46nseven with dissolve

        b "But we can't predict the future. Maybe our relationship will have
        consequences later on."
        b "Maybe an accident happens that takes one of us away from the other."
        b "I hope not! But it's possible. We just have to enjoy the time we
        have together, Avalon."

        scene 45nseven with dissolve

        b "I don't even care what we do together. We can watch scary movies
        together or take long drives together."
        b "Or we can have vigorous, wild, insane sex for days on end!"
        b "As long as I'm with you, I don't care what we're doing. I'm happy
        just being next to you."

        scene 49nseven

        a3 "I don't want to experience only some of those things, Uncle."
        a3 "Call me greedy, but I want it all! I want the movies and the road trips..."
        a3 "And the sex!"

        scene 45nseven

        b "I'm just as greedy as you are. I want it all too."
        b "But we can ease into the sex. We'll take it slow."

        scene 48nseven

        a3 "Slow doesn't mean not at all though!"
        a3 "So... can we fool around now then?"

        b "Jeez, there's no stopping you. Alright, what do you want to do?"

        a3 "Um... Stand up!"

        scene 50nseven

        b "Like this?"

        a3 "Exactly! By the way, how do you always manage to find the worst underwear?"

        b "It was on sale."

        a3 "Of course it was."

        scene 51nseven with dissolve

        label all_the_way:

        if _in_replay:
            $ player_name = renpy.input("What would you like to name the MC?")
            if player_name.strip() == "":
              $ player_name = "Byron"
            play music "audio/touching_moment.mp3"

        a3 "I did some studying online and learned a lot about sex recently, Uncle."

        b "You mean you've been watching porn?"

        a3 "Educational porn!"

        scene 52nseven with dissolve

        b "Woah!"

        a3 "You're already this hard? It doesn't take much, huh?"

        b "Nope."

        scene 1tantalize

        a3 "Okay, so, one thing I noticed that I thought was important
        was 'teasing'."

        b "Oh? Are you going to make fun of me and call me silly names or..?"

        a3 "Don't be obtuse, Uncle. You know what I mean."
        a3 "This kind of teasing."

        show tantalize with dissolve

        b "Yow! Yes, that is very tantalizing! Did you learn this online?"

        a3 "No, it's something of my own design. I'm sure it's been thought of
        before though. What hasn't been??"
        a3 "But apparently there's a lot of nerves in the penis. I figured this
        might make you yearn for more."
        a3 "Do you want more, Uncle? Do you want me?"

        b "I do but I wanted you before too. This is making me more excited, though!
        I feel almost desperate for you to grab it or suck on it or..."

        a3 "Or what? Is there anything specific you want to do to me right now?"

        b "Last time I told you what I wanted to do to you, you had a panic attack."

        a3 "I won't this time! I promise!"

        a3 "Last time we were fooling around, you said you wanted to have sex with me,
        right?"
        a3 "You want to put your big, hard penis inside my wet vagina, don't you, Uncle?"

        b "What's happening right now? What is this?"

        a3 "It's dirty talk! It's part of the fun. We're supposed to talk about
        what we want to do to each other and use bad words and stuff."

        b "You didn't say any bad words."

        a3 "Well, I need practice!"

        scene 53nseven

        a3 "And now, we stop."

        b "What? Why?"

        a3 "Because, Uncle, the penis is sufficiently teased. Now we confuse it
        by leaving it alone for a moment."
        a3 "And then, just as it starts to wonder where the attention went, we..."

        scene 54nseven with vpunch

        a3 "Sneak attack it! Surprise!"

        b "Gah! You didn't surprise my penis; you surprised me!"

        show lilstroke with dissolve

        a3 "And then we do a little bit of stroking. But just a little!"
        a3 "Do you like this, Uncle? Do you like it when I tug on your penis?"

        b "You're gripping harder than you did the last time we were messing around."

        a3 "I'm more comfortable with it now."

        b "I can see that!"

        a3 "Okay, Uncle, my knees are starting to hurt from the carpet. Let's
        move to the bed."

        scene 56nseven

        b "Will this work for you?"

        scene 57nseven with dissolve

        a3 "Yeah, this is perfect."

        b "You're really into this today, aren't you?"

        scene 58nseven

        a3 "You've let me go at my own pace every time we've been intimate
        and you always stop when I ask you to stop."
        a3 "You've made it easy for me to be comfortable with you, Uncle."
        a3 "And I've been around your penis enough that it doesn't
        scare me like it did before."
        a3 "It's actually sort of cute."

        b "Don't call it cute!"

        scene 60nseven with dissolve

        a3 "Mwah!"

        scene 58nseven with dissolve

        a3 "Sorry, Penis!"

        b "Hmm. I don't think he's forgiven you yet."

        a3 "Does he need another kiss?"

        b "I think he does, yeah."

        scene 60nseven with dissolve

        a3 "Mwah!"

        scene 58nseven with dissolve

        pause

        scene 60nseven with dissolve

        a3 "Mwah!"

        scene 58nseven with dissolve

        a3 "How about now?"

        b "Nope. He's still mad at you. I guess you're going to have to try harder."

        scene 59nseven with dissolve

        a3 "What!? Your penis needs to practice forgiveness, Uncle. I think it
        needs Jesus."

        b "He's not into dudes."

        a3 "I guess it's up to me then. I'll just have to atone somehow, won't I?"

        b "What did you have in mind?"

        a3 "I do have one idea..."

        scene 60nseven with dissolve

        a3 "Mwah!"

        scene 1handnsuck with dissolve

        a3 "Omn."

        b "Ugn! Wow. I did not see that coming."

        b "Can you... can you keep going?"

        a3 "Mhmm."

        show handnsuck with dissolve

        b "Oh fuck yes, Avalon. That's perfect!"

        ai3 "{i}I'm still a bit timid about putting any more of him in my mouth.
        He's so big, I feel like I'd choke for sure!{/i}"
        ai3 "{i}I can taste a little bit of his semen already. That must be the
        precum, right?{/i}"
        ai3 "{i}It tastes so good! It's mildly sweet with a thick texture.
        I can't explain it but I just love the way it feels in my mouth.{/i}"

        b "Can you go faster?"

        scene 59nseven with dissolve

        a3 "I'm going too slow? You don't like it?"

        b "No! I love it! But the more I enjoy it, the more I want it faster and harder."
        b "Does that make sense?"

        a3 "Yeah! I can try to go faster."

        scene 1handnsuck with dissolve

        b "Don't hurt yourself though!"

        show handnsuck2 with dissolve

        b "Ugn! Yeah, like that! That is fantastic! You're so amazing, Avalon!"

        ai3 "{i}Oh, I love his compliments. And I love pleasing him.{/i}"
        ai3 "{i}I can feel his leg tensing up so much now. And I can see his
        abs flexing everytime I go down.{/i}"
        ai3 "{i}He's really enjoying this!{/i}"

        b "Keep going, keep going!"

        ai3 "{i}Oh yes, Uncle, I want you to have me! I want you to have all of me!{/i}"
        ai3 "{i}Whatever you want, you can have! I love you, I want you to have
        everything!{/i}"

        ai3 "{i}Wait, I don't want him to cum yet, I want to give him more. I have to stop!{/i}"

        scene 61nseven with dissolve

        b "What? What happened? Are you alright?"
        b "Are you having a panic attack?"

        a3 "No."

        b "Did I go too far? We can stop if you want."

        a3 "No, I don't want to stop. I just want to... erm..."

        scene 62nseven with dissolve

        b "What are you doing, Avalon?"

        a3 "I'm taking these off. I want to be naked with you."

        scene 63nseven with dissolve

        b "Oh. Okay. I'm not going to lie, being naked is pretty awesome."
        b "Especially when your partner is naked too. It's... sensual, you know?"

        a3 "Uh huh."

        scene 64nseven with dissolve

        b "Oof. Wow, you just jumped right onto me, didn't you?"
        b "Are you... are you comfortable?"

        a3 "Yeah."

        b "You seem unusually shy all of the sudden."

        scene 65nseven with dissolve

        a3 "I'm sorry. I just... I love you, Uncle."

        b "I love you too, Avalon. What spurred that?"

        a3 "I get so focused on having sex because I selfishly want to so I can feel
        whole again."
        a3 "I believe it's somehow part of my recovery."
        a3 "But it's also something we're supposed to want to share together because
        we love each other."

        scene 66nseven with dissolve

        a3 "I don't want to be selfish anymore. I want us to have sex because it's
        something we want. I want it, and you want it too."
        a3 "I love you, I want to please you. So... I want to have sex!"

        b "I want that too but I don't want you to move backwards if we go too fast. I want to
        make sure we're moving at the right pace."
        b "But I don't know what the right pace is."
        b "I do know that you're pressing yourself into my penis right now though and
        it's making it hard for me to think!"

        scene 67nseven with dissolve

        a3 "I know, I feel it too. It's making me even more horny than I already
        was!"
        a3 "You worry about me and it makes me love you even more. But I want to
        decide the pace at which we progress."
        a3 "I don't know if I'm ready for sex yet but... I want to try!"

        b "Okay. Just... go slow. Alright?"

        a3 "Mhmm. Let me sit up here..."

        scene 68nseven with dissolve

        a3 "Oh! It slid right into position. Wow."
        a3 "Okay, Uncle, I'm going to try to take just a little bit of it."
        a3 "I just want to see how the tip feels inside me."

        b "Be careful. Make sure your legs don't get exhausted. You might just fall
        right down onto it."

        a3 "Don't worry, I have strong legs!"

        scene 1easydoesit with vpunch

        a3 "Ah, ah!"

        b "Chow! There's a lot of nerves in the head, Avalon!"
        b "That felt crazy! Like electricity just shot through me!"

        a3 "Yeah, I felt that too! I want... I want more..!"

        show easydoesit with dissolve

        a3 "Ugn! I can feel it stretching me! I didn't think it would feel this good!"

        b "I'm-- Gah! I'm glad you're enjoying it..."
        b "My mind is blank, my head is spinning. Don't... don't stop!"

        a3 "This is sex, right? We're having sex? I'm giving you what you want?"

        bi "{i}She thinks this is what I want?{/i}"
        bi "{i}I do want it but it's not all I want. I hope she's not doing this
        just to please me.{/i}"
        b "You've always given me what I want, Avalon. Because what I want... is you."
        b "In no uncertain terms."

        scene 69nseven

        a3 "I didn't mean it like that. I do want to please you though."
        a3 "You make me happy, everyday! I want to give you that happiness back."
        a3 "In every way!"

        b "Wow, I've never had someone want to reciprocate this passionately before..."
        b "That's heavy, Avalon."

        scene 71nseven with dissolve

        a3 "Yeah, we're supposed to be more focused on the sex here. It does feel
        like it's getting too intense, both emotionally and sexually..."
        a3 "Maybe we can take a break?"

        b "That might be for the best. We can pick this up later."

        a3 "Erm. My um... my foot is slipping a little bit, Uncle."

        b "Oh? Let me see if I can help you off."

        a3 "Wait, don't move your hand!"

        scene 72nseven with vpunch

        a3 "Ow! Ow ow!"
        a3 "My vagina!"

        b "Gah! Avalon, you... you fell down!"

        scene 74nseven with dissolve

        a3 "Oh fuck. It's... it's inside me, isn't it?"
        a3 "It went all the way?"

        scene 73nseven with dissolve

        b "Holy shit. Are you alright? Avalon?"

        a3 "Y-yeah, I'm alright."

        scene 75nseven with dissolve

        a3 "I was so wet, it just slid right in when I fell."
        a3 "I didn't even know it could go that deep. It feels so weird."
        a3 "What um, what does it feel like to you? Do you like it, Uncle?"
        a3 "Do you like being inside me like this?"

        b "Yeah, it feels... moist. But warm. I can feel you squeezing and releasing."
        b "But I'm also worried! What are you feeling?"

        scene 76nseven with dissolve

        a3 "Mostly I'm confused. It didn't feel like this at all before."
        a3 "I'm a little freaked out but I... I like this!"

        scene 77nseven with dissolve

        a3 "It's right here, Uncle. Inside me. All the way inside me."

        b "It doesn't hurt?"

        a3 "No. I do feel full though."

        scene 78nseven with dissolve

        b "We've certainly gone far enough for today. Let's see if we can get you off,
        okay?"
        b "We'll go a little more slowly in the future. No more accidents!"

        a3 "Okay. Let me do it though. Just... just hold still."

        scene 79nseven with dissolve

        a3 "I need to get my leg up. Oof. I felt you shift inside me when I moved."
        a3 "It's tingling parts of me I didn't even know could be tingled!"

        b "If this goes on much longer, I might have a panic attack intense enough
        for both of us. You're making me nervous."

        scene 1keepgoing with dissolve

        a3 "Okay, I'm going to get off you now. Don't move."

        b "Alright."

        scene 15keepgoing with dissolve

        b "Nyo! That is just hitting all the buttons!"

        a3 "You.. you like that? Just me going up?"

        b "Yeah, you're squeezing. That definitely does it for me."

        a3 "Okay, well..."

        scene 31keepgoing with vpunch

        a3 "Dah! Ooh!"

        b "Ugn! What the hell, Avalon? What are you doing??"

        scene 78nseven with dissolve

        a3 "I'm sorry. You said you liked it so..."

        b "But you don't have to. We can stop here."

        a3 "I want to do it. I want to have sex with you, Uncle!"

        show keepgoing with dissolve

        b "Easy does it!"

        a3 "Oh fuck, it's so intense! I feel like I'm impaling myself. It's
        so strange going in and out of me!"

        b "You're in control. You can stop whenever you want."
        b "But I'm not going to lie, please don't! This is phenomenal!"

        a3 "Oh, yes! You like this, Uncle? Do you like fucking your niece?"

        b "Your dirty talk is getting a lot better. And slightly warped..."

        a3 "I'm sorry, I can dial it back."

        b "I don't mind it but can you try going faster?"

        a3 "Yeah, I can go faster."

        show keepgoing2 with dissolve

        b "Yes! Like that!"

        a3 "I feel so exhausted, like I'm about to pass out. But I can't stop myself!"
        a3 "I want to fuck you until you cum inside me! I want it all, Uncle!"

        b "Keep going! I'm going to finish!"

        a3 "Yeah, fill me up! I'll take it all! Whenever you're ready!"

        b "Ugn! Shit! Here it comes!"

        scene 29keepgoing with vpunch

        a3 "Aahh! It's shooting inside me!"

        b "Oh, fuck, Avalon! I've never cum this hard before in my life!"
        b "Press down harder!"

        scene 31keepgoing with vpunch

        b "Dyaah!"

        a3 "I'm cumming, Uncle! I'm cumming too!"
        a3 "There's so much fluid inside me and it's so warm!"

        a3 "Ah! I can't... I can't hold anymore!"
        a3 "I have to get off!"

        scene 80nseven with dissolve

        a3 "Oh fuck. Goddamn. That was too much. I can't believe how much you came."
        a3 "It's pouring out of me."

        b "That's by far the most intense climax I've ever experienced."
        b "That was heaven!"

        scene 78nseven with dissolve

        a3 "You liked it? I didn't mess it up?"

        b "No, you were amazing. You did so good."
        b "The dirty talk was a nice touch. Although I kind of feel guilty for
        having sex with my niece now..."

        a3 "Well, you're not actually my Uncle. Not biologically..."

        if persistent.alltheway == False:
            $ renpy.notify("You've unlocked 'All the Way' in the Scene Gallery on the Main Menu!")
            $ persistent.alltheway = True

        b "Still. It might be a little messed up. It sure was hot in the middle of us
        having sex though!"

        a3 "Forbidden fruit, right? It's the sweetest."

        b "Yeah, I guess it is."

        $ renpy.end_replay()

        scene 81nseven with dissolve

        b "How do you feel? Was that too much? How are you doing?"

        a3 "Fantastic, actually! I know you think it was too fast but that's
        exactly how far I personally wanted to go."

        b "You did?"

        a3 "Yeah, I knew if I just did it, it wouldn't be as scary as I'd built
        it up in my head."
        a3 "And it wasn't scary at all! It was a lot of fun!"

        scene 83nseven with dissolve

        b "Well, good, I'm glad to hear that."
        b "For our first time, you were impressively stimulating. I didn't expect
        the tantalizing and the dirty talk."
        b "I thought our first time would be simple."

        scene 82nseven

        a3 "I wanted it to be special so I tried hard to research it."
        a3 "I um, I want to practice more too. Like, a lot more!"

        b "One day at a time!"

        a3 "Yeah, we have time. Right?"

        scene 81nseven with dissolve

        b "Yeah, we have plenty of time, Avalon."
        b "I love you."

        a3 "I love you too!"
        a3 "I better go clean up. I'll be right back!"

        scene 84nseven with fade

        #unlocks mono path button on main menu and display notification
        if persistent.monoUnlock == False:
            $ persistent.monoUnlock = True
            $ renpy.notify("You've unlocked the Monogamy Scenes on the main menu!")

        bi "{i}I knew there were going to be more hardships in the future for Avalon
        and me.{/i}"
        bi "{i}But the worst was behind us. I knew it was. And terrible as
        it was, we were stronger for it.{/i}"
        bi "{i}Whatever life had in store for us, we could handle anything. Together.{/i}"

        ai3 "{i}I was so worried after what Mom did to [player_name]. I thought
        we might never be free from misfortune.{/i}"
        ai3 "{i}Sitting here with Uncle's arms wrapped around me and the sun
        pouring down on my face, I felt renewed hope.{/i}"
        ai3 "{i}With friends and family like ours, we could handle anything. Together.{/i}"

        stop music fadeout 2.0

        if octavia and polygamy:
            jump octpolyend
        elif dallas and polygamy:
            jump dalpolyend
        elif octavia and monogamy:
            if persistent.monoUnlock == False:
                $ renpy.notify("You've unlocked the Mono Scenes on the Main Menu!")
                $ persistent.monoUnlock = True   
            jump whatif_s
        else:
            jump postavalon

        ## Octavia's Polyamorous Ending ##
        label octpolyend:

        scene octbeach01 with fade

        play music "audio/a_quiet_thought.mp3"

        a3 "Okay, Uncle, there's one Macaroon left. I've had three and you've only
        had two."

        b "That means I should get it, right? It's only fair!"

        scene octbeach03 with dissolve

        a3 "Hmm. I'm a little worried you're going to get fat, Uncle [player_name]. Maybe
        I should do us both a favor and eat it for you."
        a3 "We have to think of your health, after all!"

        b "What!? I'm not getting fat!"

        a3 "I distinctly recall seeing some love-handles in development last night."

        scene octbeach02

        b "You just want it all to yourself!"
        b "Sharing is caring, Avalon. Come on, give it to me. You wouldn't want to be
        selfish, would you?"

        a3 "Okay, but only because I love you so much!"

        b "Yes!"

        scene octbeach06 with dissolve

        b "Come to papa, macaroon!"
        b "Be careful when you feed it to me, Avalon. I am still ravenously hungry.
        I might take a finger with it!"

        a3 "Don't bite me, Uncle!"

        b "I make no promises!"

        scene octbeach04

        b "Hey! What are you doing?!"
        b "That's supposed to be mine!"

        scene octbeach05 with dissolve

        a3 "Omnomn!"
        a3 "I'm sorry, Uncle. I couldn't help myself. My willpower has its limits."

        b "But I thought you loved me!"

        a3 "Yeah but I also love macaroons, Uncle. You wouldn't make me choose between
        the two, would you?"

        b "No, I guess that wouldn't be fair..."

        play sound "audio/doorbell.mp3"

        "*Ding dong*"

        scene octbeach07

        a3 "That must be Octavia! She's finally here!"

        b "It's a long drive, I'm sure she's probably exhausted."

        a3 "Come in, Octavia!"

        scene octbeach08

        play sound "audio/doorclose.mp3"

        o2 "Hey, you two! Oh my, that view is something, isn't it?"

        b "It's as gorgeous as it is expensive!"

        o2 "You worry far too much about such trivial matters such as money, [player_name]."

        b "Trivial until the rent is due!"

        o2 "Fair point."

        scene octbeach09

        a3 "Octavia! I'm so glad you're here! I missed you!"

        o2 "I missed you too, Avalon! How are you today?"

        scene octbeach10

        a3 "I'm better now! Thanks for coming. I could use your advice and
        support right now."

        o2 "Of course, Sweetie. I'll always be here for you. But I'm glad you and [player_name]
        have had some time alone first."
        o2 "What do you need advice on?"

        scene octbeach11 with dissolve

        a3 "Everything is so foggy right now. [player_name] almost got shot, Mom is in the
        hospital..."
        a3 "I was kind of hoping we could do that meditation thing again. Maybe you
        can help me clear my head."

        o2 "Of course. How about later tonight?"

        a3 "Yes! Alright!"

        scene octbeach12 with dissolve

        o2 "And how are you, [player_name]? Has a day at the beach put you at ease
        a bit?"

        b "Avalon and I are doing well. We're both still a little
        rattled but we're moving in the right direction."

        o2 "I'm glad to hear that."
        o2 "Would you mind terribly if I showered quickly? The drive left me rather
        a mess."

        b "Oh sure, I'll show you where it is."

        label octpolyreplay:

        stop music fadeout 1.0

        scene octshower02 with fade

        if _in_replay:
            $ player_name = renpy.input("What would you like to name the MC?")
            if player_name.strip() == "":
                $ player_name = "Byron"

        play sound "audio/shower.mp3"

        play music "audio/tomorrows_rain.mp3"

        pause

        a3 "Um, Octavia?"

        scene octshower03 with dissolve

        o2 "Oh. Avalon? What are you doing in here?"

        menu:
            "{b}Additional Dialogue Choice{/b}"

            "Shampoo":
                a3 "I just wanted to make sure you, uhm, had..."
                a3 "Plenty of shampoo! Yeah."

                o2 "Actually, I could use some. Did you bring any with you?"

                a3 "Er, bring what with me?"

                o2 "Shampoo?"

                a3 "Oh right! Um, no, I didn't bring any with me."

                o2 "Is there perhaps another reason you're here, Avalon?"

            "Slippery":
                a3 "I thought I'd let you know the floor is rather slippery
                in here."

                o2 "Oh? It feels like there's an adequate amount of traction on
                the floor to me."

                a3 "Right! I meant the, uhm, the tub! It's quite slippery."

                o2 "Have you used the bathtub?"

                a3 "What bathtub?"

                o2 "Is there another reason you're here, Avalon?"

            "Forgot Something":
                a3 "I forgot something!"

                o2 "Did you? What did you forget?"

                a3 "I forgot..."

                o2 "You silly girl. Was there another reason you've decided to
                stumble in here, perhaps?"

        scene octshower04

        stop sound fadeout 60

        a3 "Okay, you got me. Thinking about you taking a shower got me excited."
        a3 "I thought I'd come see if maybe you wanted some entertainment
        while you were in here?"

        o2 "You're such a naughty girl, Avalon. What is fueling your enormous
        sexual appetite, I wonder?"

        scene octshower05 with dissolve

        a3 "I dunno. I just like it when we fool around. It's fun!"
        a3 "And you're so much more confident and experienced than I am. It
        helps me enjoy it more."
        a3 "[player_name] is a little timid about sex. We still have fun! But it's
        different with you..."

        o2 "Well, I must admit, your sudden intrusion and expression of interest
        in sexual activities does have me a touch aroused myself."
        o2 "Alright then, Avalon. But you can't very well join me with your
        clothes on. Off with them."

        a3 "Yes, ma'am!"

        scene octshower06 with dissolve

        a3 "Oh, um, [player_name] and I had sex last night. We went all the way."

        o2 "That's a very big step, Avalon. He didn't pressure you?"

        a3 "Not at all!"

        o2 "Did you pressure him?"

        a3 "Uhm, maybe a little bit..."

        scene octshower07 with dissolve

        o2 "Don't forget that [player_name] has his own demons. You need to
        respect his boundaries as much as he needs to respect yours."

        a3 "I know. He was just enjoying himself so much last night, I didn't
        want to stop. I wanted to give him more and more."

        a3 "And the sex was ultimately an accident if you can believe it.
        I fell right onto his penis!"

        o2 "Uh huh."

        a3 "No, really!"

        scene octshower08 with dissolve

        o2 "Come here, funny girl."

        a3 "You don't have to tell me twice!"

        scene octshower09 with dissolve

        o2 "You certainly are a sight to behold. Such a beautiful young woman."

        a3 "You're really pretty too."

        scene octshower10 with dissolve

        o2 "And so sweet and innocent too."

        a3 "Well, not so innocent anymore! I had sex last night all on my own
        accord!"

        o2 "Certainly proud of that, aren't we?"

        a3 "Yeah, I mean, I feel renewed. I've fallen in love with two of
        the most wonderful people in the world."
        a3 "I've had a tremendous amount of fun over the last week."
        a3 "And I have now had consensual, raunchy, dirty sex!"
        a3 "I don't want for anything anymore. I have everything."

        scene octshower11 with dissolve

        o2 "Mmh."

        scene octshower10 with dissolve

        o2 "I'm so glad to hear that, Sweetie. And you can have me as long
        as you want."
        o2 "Where is [player_name] right now?"

        a3 "He said he was going to lie down for a bit."

        o2 "Do you think we should go surprise him? Two naked, soaking wet
        women waking him up. I bet he'll just melt!"

        a3 "Oh my God, yes! We totally should do that! Let's go!"

        stop sound
        stop music fadeout 1.0

        scene octpoly01 with fade

        o2 "My goodness. He falls asleep rather quickly, doesn't he?"

        a3 "Sometimes I think he could sleep all winter if he wanted to."
        a3 "Like a bear in hibernation!"

        scene octpoly02

        a3 "Let's see if we can wake him up."
        a3 "[player_name]. Wake up, [player_name]. We have a treat for you."

        b "Erm. Mmh."

        a3 "Wake up, [player_name]!"

        scene octpoly03 with vpunch

        b "Gah! What..? Where..?"
        b "... Holy crap! Are you naked? And soaking wet? What's going on??"

        a3 "We came to surprise you! Are you surprised?"

        scene octpoly06

        b "Extremely! Why do you have that predatory look in your eyes, Avalon?"

        a3 "Because I'm getting ready to pounce on my prey! Rawr!"

        scene octpoly05 with dissolve

        b "And Octavia? You're all wet and naked too??"

        o2 "That's right, [player_name]. Do you think you can handle both of
        us at the same time?"

        b "No way! I can barely handle you girls one at a time!"

        scene octpoly04

        o2 "We'll just have to go easy on you, I guess."

        b "You promise?"

        o2 "Nope. But I can promise that you're going to have a great time,
        [player_name]."

        scene octpoly07 with dissolve

        a3 "What do you say, Uncle? Do you want to play with us?"

        b "You're extremely persuasive when you're naked, Avalon."

        a3 "I can go put clothes on if you want."

        b "No, don't!"

        a3 "That's what I thought."

        o2 "It's not fair that we're completely naked yet you still
        have clothing on."
        o2 "We'll just have to do something about that."

        scene octpoly08 with dissolve

        a3 "What do you think, Uncle? Do you like our little surprise?"

        b "I love it! But I have to say, I hardly know what to do with just
        one of you girls."

        scene octpoly09 with dissolve

        o2 "That's alright, [player_name]. It's a new experience for all of us."
        o2 "Let's just have fun with it and experiment a little bit."

        b "Dah! My shorts!"

        scene octpoly10 with dissolve

        o2 "Look at what we have here! It seems you're excited to experiment
        with us, [player_name]."

        scene octpoly09 with dissolve

        a3 "Wow, she's not timid at all when it comes to sex!"

        b "Octavia knows what she wants. You gotta give her that."

        scene octpoly11 with dissolve

        a3 "I know what I want too. I want you."

        b "Who's the cheesy one now, Avalon?"

        a3 "I am! I make fun of you for being cheesy but I secretly like it."

        b "It's not a secret, I knew."
        b "That is a heck of a grip you have there, Octavia! Yow!"

        o2 "This should help take your mind off things, [player_name]."

        a3 "How about a kiss?"

        o2 "What a marvelous idea!"

        scene octpoly12 with dissolve

        o2 "Ohmm."

        a3 "Mmmh."

        scene octavabj01 with dissolve

        a3 "Oh. Is she... is she about to give you a blowjob?"

        b "Boy, I sure hope so!"

        show octavabj with dissolve

        a3 "Look at her go! That's amazing, Octavia! I wish I could do it like that!"
        a3 "How does it feel, Uncle?"

        b "Ph-phenomenal! I can feel the tip of my penis hitting the back of
        her throat."
        b "How are you not gagging!?"

        a3 "Oh man, I have to practice until I can do it like that!"

        b "You d-don't mess around, Octavia. Mmfn!"

        scene octpoly14

        b "Woah, what are you doing? Is something wrong?"

        o2 "Not at all! I'm just uncontrollably horny right now."
        o2 "I need my own satisfaction, [player_name]. I can't help myself."

        scene octpoly13

        a3 "I get like that too sometimes! I just can't help myself around him."
        a3 "Why is that?"

        o2 "We're sexual creatures by design and [player_name] is a strong,
        charming and an easy-going man. He appeals to our womanly desires."
        o2 "It's easy to find him sexually appetizing."

        a3 "Are you going to have sex with him?"

        o2 "Oh I just must!"

        scene octpoly15 with dissolve

        o2 "But only if it's alright with you, of course!"
        o2 "I don't want to step on your toes if you'd like to go first?"

        a3 "No, I want to learn from you! But what should I do?"

        scene octpoly16

        o2 "You could sit on his face."

        a3 "W-what? Isn't that something perverts say just to be obnoxious?"

        o2 "Well, yes, but it really can be quite enjoyable!"
        o2 "Give it a try. Turn towards the headboard and mount [player_name]'s face
        like a bicycle."

        a3 "Oh wow. That... yeah, alright. Let's give it a try!"

        show octava3sum with dissolve

        a3 "Ooh, Uncle. Y-your tongue is so rough."

        o2 "You're just so big, [player_name]! You stretch me out too much!"

        b "I can't help it."

        a3 "Don't talk, Uncle. Just keep eating my pussy!"

        b "Mkay."

        o2 "You're going to ruin me, [player_name]! I can't believe
        you can reach so far into me!"

        a3 "It gets me so much wetter when you talk like that, Octavia!"
        a3 "Keep going, Uncle [player_name]! Keep going! Put your tongue inside
        me!"

        scene octpoly17 with dissolve

        o2 "It's too much! I'm climaxing! My vagina feels like it's going to explode!"
        o2 "My legs are giving out! Oooh!"

        a3 "A-are you okay back there, Octavia?"

        b "What's going on?"

        scene octpoly18 with dissolve

        play sound "audio/bodyfall.mp3"

        "*Thud*"

        a3 "Octavia? Did you fall??"
        a3 "Oh my God, are you okay?"

        b "What happened? She fell over from too much pleasure?"
        b "I should have warned her, my penis basically has superpowers.
        It's a Super Dick."

        scene octpoly19

        a3 "Are you alright, Octavia? Sounded like you hit the ground pretty hard!"

        b "Yeah, jeez, you didn't hurt yourself did you?"

        scene octpoly20

        o2 "I'm in Heaven! I just loved it, [player_name]! My legs couldn't
        hold me up anymore."
        o2 "They're still shaking, in fact! Thank you, [player_name]! Thank you!"

        b "Uhh, you're welcome?"

        a3 "You really like sex, huh, Octavia?"

        o2 "Oh very much, yes!"

        scene octpoly22

        a3 "No wonder we get along so well. I like sex too! Now that I'm not
        so timid about it, I've been able to enjoy it a lot more!"

        b "You girls are going to wear me out, aren't you?"
        b "I guess I won't have to hit the gym anymore; we can get our exercise
        this way!"

        a3 "Yeah! Sexercise! I heard about that on the internet."

        scene octpoly21

        o2 "I believe it's your turn to take [player_name] for a ride, isn't it?"

        a3 "Yeah it is!"

        o2 "I just need a moment to recover. Maybe a short nap."

        a3 "No nap!"

        o2 "Okay, no nap. I'll just need a moment while I regain the feeling
        in my legs."

        scene octpoly23 with fadefast

        b "Are you ready, Avalon? You're looking at me like a scared doe.
        Are you uncomfortable?"

        a3 "I'm a little nervous, I guess. I thought a threesome would be fun
        but it seems sort of intense all of a sudden."

        o2 "She's right, it is a little fast. Perhaps we should dial it back a bit?"

        scene octpoly24 with dissolve

        a3 "No! I, um, I want to do it. I don't want to stop just because I
        get scared."
        a3 "I always regret not going further and I'm always happy when I push
        through. So... it's worth it!"

        o2 "Sometimes it's important to push your limits and test yourself.
        But don't push too hard, Avalon."
        o2 "You don't want to move backward either."

        scene octpoly25 with dissolve

        b "Yeah, we've got plenty of time to experiment. No need to push too hard."
        b "Just don't lose this flexibility, Avalon. This is great!"

        a3 "You like how flexible I am?"

        b "Yeah, we can put you into all kinds of positions and try crazy
        Kamasutra-level stuff!"

        scene octpoly26

        b "I'll even help you out with your yoga. Especially if you're doing
        hot yoga! Or naked yoga!"

        a3 "You're such a dope, Uncle! You're just trying to make me laugh, aren't you?"

        o2 "He uses humor to lighten the mood."
        o2 "It's too bad his jokes aren't very funny."

        b "She's full of crap. I'm hilarious."

        scene octpoly27 with dissolve

        a3 "Okay, Uncle, I think I'm ready. You can put it inside me now."

        b "Alright, clear the runway! We're preparing for insertion!"

        a3 "If you do a countdown, I'm leaving."

        b "Fair enough."

        scene bavaboned00 with dissolve

        a3 "Nya. The pressure of your dick is making me so wet, Uncle."
        a3 "D-don't stop. I want it."

        o2 "Go slow at first, [player_name]."

        b "Well, let's try a little further here..."

        scene bavaboned13 with vpunch

        a3 "Dah! You fill me up so much, Uncle [player_name]! My head is fuzzy!"
        a3 "It feels like my mind is in disorder and all I want is for you
        to fuck me."
        a3 "Ooh, please fuck me, Uncle!"

        b "When you talk like that, I feel like I'm going to lose control!"

        show bavaboned with dissolve

        a3 "Ah! Ah! Ah! Yes! Just like that!"

        o2 "S-slow down, [player_name]. You don't want to hurt her."

        a3 "Hurt me, Uncle! Break me! I want it!"

        b "I don't know who to listen to!"

        a3 "Make me yours, Uncle! Make me yours with your cum! Cum inside of me!
        Fill me up!"

        o2 "If that's what she wants, be a gentleman and give it to her, [player_name]."

        b "Hard to argue with that!"
        b "Prepare yourself, Avalon! I'm about to finish inside you!"

        a3 "I'm going to cum too! Give yourself to me, Uncle! Empty your fluids
        deep inside my pussy!"

        b "You're getting good at the dirty talk. Jesus fuck!"

        scene octpoly28 with vpunch

        b "Ooh shit, I'm cumming!"

        a3 "Don't pull out! Leave yourself inside of me, Uncle [player_name]!
        Don't pull out until I'm completely full!"

        scene octpoly28 with vpunch

        b "There's more! There's so much more! It feels like my penis is going to explode!"

        a3 "I never thought I could have an orgasm this intense! It's almost painful!"
        a3 "I love it!"

        scene octpoly29 with dissolve

        b "Shit, I have to sit down. I can't even see, my vision is totally blurry."

        a3 "That... was awesome. There is so much of him inside me, Octavia."
        a3 "I feel like I just had a four-course meal, that's how full I am!"

        o2 "I'm jealous! And I'm so proud of you. Well, except for the dirty talk."
        o2 "Where did you learn to speak like that, you bad girl?"

        a3 "The internet."

        o2 "I should have known."

        scene octpoly30 with dissolve

        a3 "I think he broke my vagina, Octavia. I feel like Humpty Dumpty."
        a3 "I don't think all the King's horses and all the King's men can ever
        put me back together again."

        o2 "You're talking crazy, Avalon. I think he broke your brain, too."

        scene octpoly31

        b "I'm going to need a few minutes girls, my head is in a daze right now."
        b "That was the best sex I've ever had. And a threesome! That's a notch
        on the old belt."

        scene octpoly32

        o2 "Take your time, [player_name]! We're going to go finish our shower."

        a3 "Where are we going to sleep tonight, Octavia? That bed is full of
        water and all sorts of other fluids."

        o2 "We'll have to wash the sheets before bed tonight. Twice, probably."

        a3 "Hey, Octavia?"

        o2 "Yes, Sweetie?"

        a3 "I love you."

        o2 "Aw, Avalon. I love you, too!"

        if persistent.twowet == False:
            $ renpy.notify("You've unlocked 'Two Wet' in the Scene Gallery on the Main Menu!")
            $ persistent.twowet = True

        $ renpy.end_replay() ## End Replay ##

        scene octpoly33 with fade

        ai3 "I'd fallen in love with my Uncle. A strange enough event on its own."
        ai3 "But the twists of fate also brought both of us Octavia; the kindest and
        most caring person we'd ever met."
        ai3 "Together we formed a bond strong enough that no amount of trauma could
        keep us from finding the joy and love in life."
        ai3 "Together, we found our happily ever after."

        jump postavalon

        ## Dallas's Polyamorous Ending ##
        label dalpolyend:

            stop music

            scene black with dissolve

            "The next day."

            scene dalbeach01 with fade

            ai3 "{i}Uncle fell asleep while we were cuddling. I think I'll let him
            rest for a bit.{/i}"
            ai3 "{i}I wonder if he hasn't been sleeping enough? He looked so much
            younger when we spent time together several years ago.{/i}"
            ai3 "{i}It's almost as if he aged ten years in the span of only a few
            actual years. Maybe he was stressed more than I realized...{/i}"

            play sound "audio/dooropen.mp3"

            d "Hey, Avalon!"

            scene dalbeach02 with dissolve

            a3 "Dallas?"
            a3 "Wow, you're here already? You must drive like a lunatic."

            scene dalbeach03

            d "Yeah, Girl. I missed you."

            a3 "Don't you ever knock?"

            d "You knew I was coming! Why would I bother kno--"

            scene dalbeach04

            a3 "Shh!"

            d "What the hell?"

            a3 "[player_name] is asleep. I don't want to wake him."

            scene dalbeach06

            d "He's got the beach right outside and he decided to take a nap?"
            d "You only have this place for another day, right?"

            a3 "He's been through a lot lately. He needs rest!"
            a3 "Wait, I have a better idea! I know something he would like
            way more than a nap. Did you bring the outfits!?"

            scene dalbeach07 with dissolve

            d "Oh yeah, Girl. I brought them. I'm so stoked about your idea."

            a3 "We should do it now! We'll surprise him with them! He'll wake up to
            two sexy cosplay girls! We gotta do it!"

            d "That sounds fuckin' awesome. Hell yeah."

            scene dalbeach05

            a3 "Go get them from your car and we'll put them on."
            a3 "This is gonna be epic."

            label dalpolyreplay:

            scene dalpoly01 with fade

            if _in_replay:
                $ player_name = renpy.input("What would you like to name the MC?")
                if player_name.strip() == "":
                    $ player_name = "Byron"

            play music "audio/disturbed_mind.mp3"

            d "He's fast asleep, isn't he?"

            a3 "Let's change that."
            a3 "Uncle [player_name]. Wake up, [player_name]. We have a surprise
            for you."

            b "Mnf mm..."

            d "Let me try."

            scene dalpoly02 with vpunch

            d "Rawr! Wake up!"

            b "Gah! What happened? Is someone hurt?"
            b "... Oh what the hell is this?"

            a3 "I'm a bunny girl and Dallas is a fox girl! It's sexy, right?"

            b "W-wait, is this a sex thing? Are you trying to seduce me!?"

            d "Is it working?"

            scene dalpoly03

            a3 "Come on, Uncle. You liked it when I wore the bunny costume
            before, didn't you?"
            a3 "This one is a little different than the other one though. There's
            a lot less of it!"
            a3 "And this time, nobody is going to interrupt us. That means you'll
            have plenty of time to do whatever you want to me."

            b "A-anything?"

            a3 "Anything!"

            scene dalpoly04

            d "And now you have your bunny girl {b}and{/b} your fox girl too!"
            d "Double the fun, [player_name]."

            b "I don't know, Dallas. You look like a biter!"

            d "These claws aren't just for looks, I'm a scratcher too!"

            scene dalpoly05

            b "I thought we were supposed to be on vacation. This was meant
            to be a relaxing trip, Avalon."
            b "Two girls at once though. That sounds like work! Heck, I might
            not even survive this!"
            b "You both look like you mean business!"

            a3 "You'll be fine! It'll be fun!"

            scene dalpoly06 with dissolve

            d "Don't be timid, [player_name]. We worked hard picking these
            out for you."
            d "You're not going to let all that effort go to waste are you?"

            b "Wait, what?"

            d "We thought you'd like this."

            scene dalpoly07 with dissolve

            b "This is... for me? You girls did this because you thought I'd like it?"

            d "Yeah, of course! You're good to us. You deserve a treat!"

            a3 "We love you, Uncle! And we figured you'd love this!"

            b "I don't even know what to say. I've never had a gift this exceptional
            before."

            scene dalpoly08 with dissolve

            d "Well, that's easy. I can tell you exactly what to say."
            d "Just say 'I want to fuck you, Dallas.'"
            d "And then take me from behind like you own me, [player_name]."

            b "Did you learn how to dirty talk from the internet too?"

            d "W-what? No. That's just what I want. Who learned dirty talk from the internet?"

            show avamasturbait with dissolve

            ai3 "{i}Dallas is so goddamn sexy when she's seducing someone. She's
            like an unstoppable vixen!{/i}"
            ai3 "{i}It makes me so wet watching her work. She's irresistible!{/i}"
            ai3 "{i}I just want to watch Uncle fuck her raw until she's screaming
            with delight!{/i}"

            scene dalpoly12 with vpunch

            d "Avalon!"

            a3 "W-what!?"

            d "What the hell are you doing?"

            a3 "I was watching you seduce Uncle and I got excited! I like to watch
            sometimes..."

            d "No, Ma'am! You're not just going to watch today,
            you're going to join us!"

            a3 "Fine!"

            scene dalpoly13

            d "So what do you say, Big Boy? Do you want to take me from behind again?"

            b "I do recall you being rather uncomfortable in that position the
            last time we tried it because of the girth of my cock, Dallas."

            d "You go too deep from behind! But practice makes better, right?"

            scene dalpoly14 with dissolve

            d "Mmh!"

            scene dalpoly13 with dissolve

            d "I think I just need more training, [player_name]. Do you want to
            train your little fox girl?"
            d "Do you want to tame this pussy and make it do whatever you want?"

            b "It sounds to me like that's what you want."

            d "We can want the same thing, can't we?"

            scene dalpoly14 with dissolve

            d "Mmmh."

            scene dalpoly13 with dissolve

            d "Come on, let's get into a better position."

            b "Lead the way, Foxy Lady."

            show comehither

            d "Come here, Avalon. Plant that booty right in front of me."
            d "I want to taste that cute little pussy while [player_name] fucks
            me from behind."

            a3 "You don't have to tell me twice! That sounds kind of hot!"

            scene dalpoly17

            a3 "Like this?"

            d "Hell yeah. We're going to have to get rid of your pesky panties
            though."
            d "Or else I'm just going to eat right through them!"

            a3 "Don't ruin my costume, Dallas!"

            d "Then take 'em off, Girlfriend!"

            scene dalpoly18 with dissolve

            b "Damn, Dallas. You've got just the sexiest little butt. And look,
            my penis fits perfectly in between your cheeks!"
            b "It's like your ass was designed for this dick."

            d "I bet it would fit even better with my panties off, [player_name]."
            d "Why don't you help me out of them while you're back there? And
            don't be gentle!"

            b "You fuckin' got it!"

            scene dalpoly19

            d "Mmm! How many licks does it take to get to the center of this pussy."
            d "Let's find out! One lick."

            a3 "O-oh, fuck. You're not shy with those licks at all! I didn't even
            know a tongue could flatten out that much and cover so much area!"

            d "Two licks."

            a3 "Do you like this, Uncle? Do you like watching me get eaten out
            by the girl you're about to fuck from behind?"

            b "I can only get so hard!"

            d "Three licks!"

            a3 "Ah ah! Do it, Uncle. Fuck her while she eats me out! I want to see
            you fuck her!"

            b "I hope you're ready, Dallas!"

            d "Fuck. Yes."

            scene avadalsex00 with dissolve

            d "S-shit, it's as big as I remember."

            b "That's just the tip!"

            a3 "Don't stop licking my pussy, Dallas. Keep going!"

            show dalavasex with dissolve

            d "Aah! Ahh! It's... it's too big for me!"

            a3 "Focus on my pussy, Dallas! Don't stop!"

            d "Omn. Mmh."

            b "If you tighten up anymore, you're going to break my dick off, Dallas!
            Loosen up!"

            d "I can't!"

            b "Relax your pussy. Jesus!"

            d "I can't!"

            a3 "I'm going to cum! Fuck, this is too thrilling! I'm going to orgasm!"
            a3 "Aaah! My pussy is on fire!"

            d "O-okay, stop stop!"

            scene dalpoly22 with vpunch

            d "It's too much from behind! I don't wanna do it that way anymore!"

            b "You insisted on it!"

            a3 "Oh fuck, my orgasm is still going. My whole body is tingling. Oof!"

            d "I was wrong! I thought I would have loosened up but I didn't. And
            I think you got bigger!"

            b "I probably have. I've never been this aroused in my entire life. It's
            extremely possible my dick leveled up."

            scene dalpoly21 with dissolve

            a3 "Is it that intense, Dallas?"

            b "No! She's just all talk and then no follow-through!"

            d "You're the one with the swollen cock! You need some Benadryl or
            something for that thing!"

            scene dalpoly20 with dissolve

            d "It's because he can fit himself entirely inside me at that angle."
            d "And my pussy is too small and it doesn't go deep enough. He's
            just too big for me."

            a3 "Do you think I could take it?"

            d "Are you ready for actual sex, Avalon? I didn't figure you would
            go all the way today."

            a3 "Well, yeah, we uhh... we had sex last night, actually."

            d "Nice. Why don't you give it a try then, Avalon? You might be able
            to accommodate his monster cock."
            d "But I want a front-row seat to this show!"

            scene dalpoly23 with dissolve

            a3 "What do you say, Uncle? Do you want to try it from behind with me?"
            a3 "I bet I can take it better than Dallas. You can fuck me as hard as you want
            and for as long as you can!"

            d "Hey! It's not a competition!"

            a3 "But if it were, we would totally win. Right, Uncle?"

            b "If you're up for it, we could give it a try."

            d "You weren't lying, [player_name]. This girl is getting nuts with
            the naughty talk."

            b "I know, right? Avalon is getting really into the dirty talk.
            She's on the road to becoming a very naughty girl, indeed!"

            d "Yeah, you could say she's on the naughty road!"

            b "Alright, Avalon, get your booty over here."

            a3 "Okay but let me take my top off first! I know you like my breasts!"

            d "Oh good idea, I'll follow suit!"

            scene dalpoly24 with fadefast

            d "Oh fuck yes, this position is perfect! I can see everything!"

            a3 "Err, I feel really exposed from this position."

            d "I know, it's fuckin' awesome, right?"

            a3 "Actually, since it's Uncle behind me, it is sort of arousing..."

            b "Let me know if it gets uncomfortable. Ready to go?"

            a3 "Yeah! I'm ready!"

            show avadalbehind with dissolve

            a3 "W-wow! Ow ow! Shit!"
            a3 "You're right, Dallas! It goes so deep! It feels like it's stirring
            up my insides!"

            d "I can see everything from this angle. I can even feel your pussy juices
            splashing onto my face."
            d "Fuck, it's getting me so horny!"

            b "I have just the perfect grip because of your tight waist, Avalon."
            b "I can fuck you so deep and so hard like this!"

            a3 "I feel like my insides are going to burst! But it feels
            so wonderful at the same time!"
            a3 "Hurt me, Uncle! Fuck me so hard you break me! And then fill
            me to the brim with your cum!"

            d "Jesus fuck, I need to take notes!"
            d "Ooh God, I think I'm going to cum first!"

            b "Avalon, I'm... I'm about to finish!"

            a3 "Give me everything you have, Uncle! I want it all inside me!"

            b "Here it comes!"

            scene dalpoly25 with vpunch

            a3 "Aah! Oh my God, it's so warm! There's so much! I can feel it
            stretching me out!"
            a3 "Ugn! I don't think I can h-hold it all, Uncle! I'm going to burst!"

            b "Just hold on a little longer! I don't think I can control myself enough
            to stop now!"

            a3 "My head feels fuzzy! I'm getting dizzy!"

            scene dalpoly26 with dissolve

            d "Your pussy is never going to be the same again, Avalon."
            d "[player_name] just wreck that thing."

            a3 "P-pull out now, Uncle! I can't handle any more!"

            scene dalpoly27 with vpunch

            b "Dah! I'm out!"

            d "Oh shit, look at that cum spraying out!"

            a3 "Oh fuck, ow! My pussy is so sore. Ugn!"

            scene dalpoly28 with vpunch

            play sound "audio/bodyfallmat.mp3"

            b "Oof. I am done. My energy level is down to zero."
            b "I can't even feel my legs right now. This was too incredible
            for my feeble mind to handle."
            b "Two gorgeous teenagers in costumes eager for my dick. By God, no
            man deserves this."

            scene dalpoly29

            d "Holy fuck, Avalon! He filled you all the way up! There's so much
            semen in here!"

            a3 "Ugn. My whole body is numb."

            d "You're a champion, girlfriend!"
            d "You've got like, the perfect little pussy to hold cum in too. It's
            as if your pussy is a cum holster!"

            scene dalpoly30 with dissolve

            d "I am so jealous right now! I want his fluids inside of me too!"
            d "I should have held out longer. Damn, I missed an epic climax!"

            scene dalpoly31 with dissolve

            a3 "I'm dead, Dallas. Uncle fucked me to death and now I'm dead."
            a3 "I must be in Heaven. I can't think, I can't see straight."
            a3 "I can only feel. And I feel incredible! Like I just got hit
            by a pleasure train."
            a3 "Choo choo. Chugga chugga, choo choo."

            d "You're talkin' crazy now, Avalon. I think [player_name] screwed
            the sanity out of you."

            scene dalpoly32

            d "Come on, [player_name]! You must have more gas in the ol' tank!"
            d "Fuck me one more time. Fill me up like you did Avalon."

            b "No! Go away, Dallas. I'm completely spent!"

            d "No way! A big, strong man like you? I bet you got another romp
            in you!"

            b "A bomb only explodes once, Dallas!"

            scene dalpoly33 with dissolve

            d "Look at my sexy fox ears, [player_name]!"
            d "And I have my perfect tits out for you too!"
            d "I've kept this body in perfect condition. You're into tan, fit
            girls, right?"
            d "You've got a hot eighteen year old ready to fuck right in front of
            you. All you gotta do is get hard again, I'll even do all the work!"

            b "S-shit. You're very persuasive..."

            scene dalpoly34 with dissolve

            d "Yes! There it is! Guys are freakin' easy, man!"
            d "I am going to ride that thing so hard right now! Woohoo!"

            scene dalreverse00

            d "Ooh, yes! I've got the tip in! How does it feel, [player_name]?"
            d "Do you like this tight, teenager pussy? I'll spread my legs for
            you any time, [player_name]. And anywhere!"

            b "I get it, Dallas! You're horny! Stop talking and start bouncing!"

            d "Oh you got it, Big Boy! But first, let me see that cum-filled pussy,
            Avalon!"
            d "I want to see what I have to look forward to."

            scene dalpoly37

            a3 "You mean this cum-filled pussy, Dallas?"
            a3 "Is this what you want? You want [player_name] to gush his manly seed
            deep inside your tight pussy?"

            d "God, I love dirty-talking Avalon! You are the fuckin' best!"

            show dalreverse

            d "Oooh, here we go! I love being in control!"
            d "It's so much better when I can stop before you go too deep."

            b "I don't like it. I prefer to be the one in control."

            d "Too bad! It's my turn!"

            b "I'm not complaining, this still feels fantastic and I don't even
            have to do anything."
            b "And your skin feels like moist silk. I can't get enough of your
            body, Dallas."

            d "Don't say moist to me! I hate that word!"

            b "F-fuck, I'm getting close, Dallas."

            d "Yes! Finish! Explode into me, make me your messy little cum-whore!"

            b "You don't like the word moist but you're okay with the word whore!?"
            b "G-gah! Here it comes! Brace yourself, Dallas!"

            scene dalpoly38 with vpunch

            d "Aah! It's inside me! It's so slimy and gooey inside my pussy!"
            d "More! More, [player_name]! Don't stop until my stomach is distended
            and I can't hold anymore!"
            d "I want it all! Give it to me!"

            scene dalpoly36 with dissolve

            d "Oooh yes! That's it! I have all of you now, don't I?"

            b "That's all I have to give, Dallas. I'm completely tapped out now."

            a3 "I should have recorded that. I want to watch you ride him over
            and over again, Dallas."

            d "Me too! I'd watch that all day! Ugn, my pussy is so full right now."

            scene dalpoly39 with dissolve

            b "Ugh. I'm so spent. You fucked me so hard, my dick is on fire right now,
            Dallas."
            b "I need a vacation from this vacation."

            d "You better recover quickly because I am so going to fuck you again
            later, [player_name]."

            b "You'll have to fuck me while I'm asleep then because this nap
            I'm about to take is going to be of an epic length!"

            scene dalpoly40

            if persistent.cosplay == False:
                $ renpy.notify("You've unlocked 'Cosplay' in the Scene Gallery on the Main Menu!")
                $ persistent.cosplay = True

            d "Check it out, Avalon. We're both full with his cum now."

            a3 "Oh God, that is just the best thing ever."
            a3 "It's like we're tagged now, you know? Like we're both his forever."

            d "Yeah, it feels that way. I love it. I wish I could keep his seed
            inside me forever."

            a3 "I don't think that's a good idea. But I'm sure he'll give you
            more any time you ask."

            d "Our lives are going to be so incredible, Avalon! We hit the jackpot, didn't we?"

            a3 "Yeah, we're really lucky. I'm excited about the future."
            a3 "Come on, let's go get cleaned up."

            d "Right on."

            $ renpy.end_replay() ## End Replay ##

            stop music fadeout 1.0

            scene dalpoly41 with fade

            ai3 "{i}Dallas inspired us to be more confident, try new things and
            push forward into the future.{/i}"
            ai3 "{i}She's the part of our relationship that acts as a guiding hand
            reminding us how fun life can be.{/i}"
            ai3 "{i}With her, we're more than the sum of our parts. We can handle
            anything and no amount of trauma can stop us from being happy together.{/i}"
            ai3 "{i}The perfect start to a perfect life with the two people I love
            the most. I couldn't ask for more.{/i}"

            jump postavalon


        ## Jump to Post Avalon ##
        label postavalon:

        scene avalon with fade

        "Thank you for playing!"

        if persistent.monoUnlock == False:
            $ renpy.notify("You've unlocked the Mono Scenes on the Main Menu!")
            $ persistent.monoUnlock = True

        ## Post Avalon ##

        scene 1postavalon with fade

        play music "audio/soft_reminder.mp3"

        pause

        scene 2postavalon

        pause

        play sound "audio/doorknock.mp3"

        "*Knock* *Knock*"

        scene 3postavalon with dissolve

        l "Hmm?"

        scene 4postavalon

        l "Who is it?"

        p "We haven't met yet. My name is Penny and I'm a friend of Avalon and [player_name]."

        l "Oh, uhm, come on in then."

        play sound "audio/dooropen.mp3"

        scene 5postavalon with dissolve

        p "Thank you. I hope I'm not coming at a bad time?"
        p "I know it's only been a week since the incident with [player_name] and Sharol.
        I wasn't sure how long I should wait to speak with you."

        scene 6postavalon

        l "You're {b}the{/b} Penny, then? The one that saved his life?"

        p "Yes, that's right."

        l "Thank you so much for that. I'm still reeling from the shock of it all
        but I'm glad he's okay. Sincerely, thank you."
        l "I'm glad you found me. Avalon talks about you quite often. You're a detective,
        if I'm not mistaken?"

        scene 7postavalon

        p "Former. I've decided to give up on that venture and pursue... something else."

        l "Oh?"

        p "That's partially why I'm here, actually."

        scene 8postavalon with dissolve

        l "I certainly wouldn't mind the company. I have two months vacation
        and I'm not entirely sure how to spend it."
        l "Please have a seat."

        p "Thank you."

        scene 9postavalon with dissolve

        p "I've done my homework on you. Your work at Pridwen has been innovative."
        p "From what I've heard, you've had some creative solutions to problems
        others would have deemed unsolvable."

        l "You give me far too much credit. I assure you, whomever told you that
        was exaggera--"

        p "They weren't."

        scene 10postavalon with dissolve

        p "I reviewed some of the documentation on your artificial heart design."
        p "I haven't the education to understand most of it but I understood enough."
        p "What you proposed could not only lead the way for artificial hearts, but
        a host of other solutions to medical ailments too."

        scene 15postavalon

        l "W-what? How did you see that research? It's under lock and key within
        the corporation. You couldn't--"

        p "I have my ways."

        l "Well, everything I've proposed is theoretical. There is decades of research
        still to do."
        l "And the synthetic organ my team and I developed isn't even functional yet."

        scene 10postavalon

        p "They said you were humble. I do have some business I'd like to discuss
        with you, Leah."
        p "But before we get into that, I'd like to know how you're doing?"

        scene 11postavalon with dissolve

        p "I heard through the grapevine that you had become smitten with [player_name]
        only to return home to find him with someone else."
        p "And then he was almost murdered by his sister that you've never even met
        the day after your reunion."
        p "How are you holding up?"

        scene 17postavalon

        l "Not well. I had this vision that would replay in my mind over and over
        while I was away."
        l "I would knock on [player_name]'s door, he would swing it open and we
        would apologize profusely to each other."
        l "And then he would hold me tightly before kissing me with a long
        and passionate embrace."
        l "We would live out the rest of our lives burning only for each other."

        scene 13postavalon

        p "You're in love with your [persistent.byron_rel]?"
        p "That's very... what's the word I'm looking for here?"
        p "Alabama?"

        scene 15postavalon

        l "Well, it's not like we grew up together or anything..."

        p "I won't judge."

        scene 17postavalon with dissolve

        if polygamy:
            l "Avalon asked if I'd be interested in a polyamorous relationship with them."
            l "But to be honest, I don't have those kind of feelings for her."
            l "She's so nice and sweet and adorable but there's just no fire between
            us."
            l "I'd only be in it for [player_name]. It wouldn't end well for any
            of us in the long run."

        else:
            l "I guess by running away, I lost my only chance with him."
            l "I'm trying to accept things the way they are but I can't help
            secretly hoping things don't work out between him and Avalon."
            l "That way, maybe I'll have a chance with him again. It's terrible of
            me, isn't it?"

        scene 13postavalon

        p "No matter how we play out the future in our minds, it will always surprise us."
        p "You'll find the right person for you, Leah."
        p "And who knows? They might be a lot closer than you think."

        scene 16postavalon

        l "You are quite the optimist, Ms. Penny."
        l "What was this business you were speaking of earlier?"

        scene 12postavalon

        p "Oh we're jumping back to that?"
        p "Well, I have reached the limit of my engineering capabilities."
        p "I'm looking for a professional to help me work on some non-lethal tactical
        weaponry."

        scene 15postavalon

        l "That's not really what I utilize my talents for, Penny."

        p "I know! It'll be quite a change for you!"

        l "I'm not sure I'm interested in this."

        scene 11postavalon

        p "The society that we live in breeds uncertainty. Most people simply don't
        know or understand the importance of community."
        p "They're just trying to get by in a harsh society that none of us
        seem to truly fit in with."
        p "Some people try to improve their nation, like you, and others gear more
        towards malicious behaviors for profit, prestige or power."
        p "I want to help nudge people towards the former. Especially those that
        are walking the line."

        scene 13postavalon with dissolve

        p "To do that, I'll have to put myself in harm's way. Helping people
        that are leaning towards villainy will be dangerous."
        p "I'll need every advantage and that means equipment that will protect
        me in my endeavor."
        p "To that end, you would be saving people. Just as you will be saving
        people with your medical innovations."

        scene 17postavalon

        l "I'm not sure I understand what exactly you mean, Penny."
        l "You're asking me to make weapons and weapons notoriously have not been
        used to help people. They've been used to hurt."
        l "I think... I think I need to sleep on it. Perhaps you can send me
        some of your ideas and I'll have a look?"

        scene 18postavalon

        p "That sounds like a great idea. I'll send some of my ideas over to you."

        l "Oh, you're leaving?"

        p "I've made you uncomfortable enough for today. I'll see myself out."

        stop music fadeout 1.0

        scene 19postavalon with dissolve

        p "It was a pleasure, Leah."
        p "Farewell for now."

        scene 20postavalon with dissolve

        play music "audio/sneaking_up_on_you.mp3"

        p "Oh, one last thing before I go."
        p "I was thinking about updating my wardrobe. I'll need something to wear
        when I confront would-be evil-doers."

        scene 21postavalon with dissolve

        p "I'll need to keep my identity a secret as well. So I was thinking I might need something...
        heroic?"
        p "Penny for your thoughts?"

        play sound "audio/coinflip.mp3"

        scene 22postavalon with dissolve

        pause

        scene black with dissolve

        "Penny will return in..."
        "Penny for Your Thoughts."

        scene 23postavalon with vpunch

        l "Ow!"

        scene 24postavalon with dissolve

        l "Did you just throw a coin at me??"

        scene 25postavalon with dissolve

        p "Oh my God, I'm so sorry!"
        p "I thought you would catch it."

        show c_and_p with fade

        pause

        "Coming soon..."

        pause

        stop music

        jump whatif_s

    label outroseven3:

        scene 1myraoutseven with fade

        m "Hey there! You've reached the end of the story for Avalon."
        m "We sincerely hope you've enjoyed reading it."

        scene 2myraoutseven with dissolve

        m "And yes, this was the final part of the novel. The story of Avalon
        is now complete."
        m "I know there was some build-up regarding Leah so let me nip your doubts
        in the bud before we continue."

        scene 7myraoutseven with dissolve

        m "There is going to be a Bonus Episode! We don't want to give away any
        details about it because it's going to be a very special treat to our fans."

        scene 2myraoutseven with dissolve

        m "But we will say that it largely involves [player_name] and Leah."
        m "We can't say yet when you can expect it because we honestly have
        no idea how long or how involved it's going to be."

        scene 6myraoutseven with dissolve

        m "This also means we won't be able to give you any spoiler images in
        our weekly progress report."
        m "We hope you'll bear with us through these few weeks, or months, while we
        prepare this for you all."

        scene 3myraoutseven with dissolve

        m "We're also going to use the Bonus Episode to experiment with some new
        techniques for writing."
        m "We're going to add a narrator and change some of the more stylized features
        of the characters to be a bit more natural."
        m "Avalon also still needs a little polish. With a little elbow grease,
        we think we can pretty up the novel a bit."

        scene 2myraoutseven with dissolve

        m "That means our time with Avalon isn't quite done yet. There's still much
        to do!"
        m "On the main menu is a link to our Discord. Lockheart loves to hear from
        his fans so be sure to come chat with him."
        m "And if you loved it, please consider supporting us on Patreon!"

        scene 8myraoutseven with dissolve

        m "Thank you so much for taking the time to enjoy our story. We hope
        you genuinely had a great time with Avalon on her journey."
        m "And don't forget, after we're finished with this Bonus Episode, we'll be
        working on Penny for Your Thoughts."
        m "Farewell for now!"

        return

    label outroseven2:

        scene 2myraoutseven with fade

        play music "audio/something_good.mp3"

        m "Hang on there, Tiger! We know there are some parts missing. The Mono and
        Poly paths conclusions will be on the next release."
        m "We're going to spend the next four to six weeks on approximately eight
        total scenes to conclude the Mono and Poly paths."
        m "After the next release, we're going to focus on a bonus Act Eight that
        will focus on Leah's content."
        m "We have at least two more releases before Avalon is complete."

        scene 6myraoutseven with dissolve

        m "I know a lot of you are disappointed that Avalon is ending. Some of
        you are even angry."
        m "We would love to continue Avalon's story for years to come. But unfortunately,
        we didn't understand this community when we first started."
        m "And our skills weren't great in the beginning either. You'll notice
        the lighting is quite atrocious before Act 6."
        m "We've learned so much and while we appreciate our fans dearly, we know
        we're in a niche group right now."
        m "We want to branch out and reach a larger audience."

        scene 2myraoutseven with dissolve

        m "Penny for Your Thoughts is something we feel strongly will appeal to
        a larger audience."
        m "It will have all the humor of Avalon and more! With a bit less drama
        and more sexual content."
        m "And we're still going to see many of the characters from Avalon appear
        in Penny's game."

        scene 3myraoutseven with dissolve

        m "We can't tell you anything more about the bonus act for Avalon.
        We want it to be a surprise when we release it."
        m "We hope to have the Mono and Poly path content released around
        early to mid December."
        m "Then we may have the bonus Act Eight completed and released
        mid to late February."

        scene 7myraoutseven with dissolve

        m "We're so glad you enjoyed Avalon! Our work is going to be free for
        as long as we can keep it that way."
        m "But we do need support to keep making novels. If you like our
        work, please consider supporting us on Patreon."

        scene 8myraoutseven with dissolve

        m "As always, come tell us what you thought of Avalon on our Discord."
        m "You can find the link to both our Patreon and our Discord on
        the main screen."
        m "Farewell for now! And we'll see you again soon!"

        return

    label outroseven:

        play music "audio/something_good.mp3"

        scene 1myraoutseven with fade

        m "Hey there! It's me again, Myrabelle! Did you miss me?"
        m "It's been a while since I've done an outro for Avalon."
        m "And, of course, seeing me means you've reached the end of the current
        content for Avalon."

        scene 3myraoutseven with dissolve

        m "There's been a lot going on recently. If you weren't aware, this will
        be Avalon's last Act. The next release will wrap up the story."

        scene 6myraoutseven with dissolve

        m "I know a lot of you are going to be sad to see it end. It feels like
        there's so much more we could do with Avalon."
        m "But we designed this story to be a practice run. It wasn't
        supposed to be this long."
        m "And we made a lot of mistakes!"

        scene 7myraoutseven with dissolve

        m "But we've learned a lot! And we're going into our next project with
        new skills and a better understanding of what our audience wants!"
        m "Our next project is going to be called Penny for Your Thoughts. And, yes,
        it's going to follow Penny in an adventure all her own."
        m "If you didn't guess the theme of her game from this release, well, I'm
        sure the community would be happy to tell you."

        scene 3myraoutseven with dissolve

        m "But we're getting ahead of ourselves here! We've still got to finish up
        Avalon. And then we have a bonus Act 8 that we're going to work on."
        m "We're going to lay the foundation for Penny for Your Thoughts while
        we work on Act 8."
        m "We can't give an accurate estimate of the next and final release of Act 7.
        We simply don't know for sure how involved it's going to be."

        scene 7myraoutseven with dissolve

        m "But don't worry! We'll keep you updated on our progress. We have a
        Progress Report out every Monday on our Patreon page!"

        scene 2myraoutseven with dissolve

        m "There's one more thing we want to mention. We've been working with a
        partner recently."
        m "Her name is Eris Discordia and she's going to help out with the coding
        for Penny for Your Thoughts."
        m "She's also going to be working on her own project called Harem Highlander.
        Be sure to give your support to her on her journey!"

        scene 7myraoutseven with dissolve

        m "We love hearing from our fans so please come hang out with us in our
        Discord and tell us what you thought of Avalon!"
        m "And if you loved your experience, please consider supporting us
        on Patreon so we can bring you faster, bigger and better updates."

        scene 1myraoutseven with dissolve

        m "Thanks so much for reading our story. We'll see you next time for the
        final part of Act 7!"
        m "Farewell for now!"

        return

        label notready:

        stop music

        scene 8xianne5 with fade

        x "Umm, yeah, so it's not quite ready yet."

        scene 9xianne5 with dissolve

        x "But you're excited, aren't you?"
        x "You should be. It's going to be amaze-balls."
        x "Soon, friend. Soon..."

        return
