


label act_six:

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

    jump act_six_s

label act_six_s:

    scene avalon with fade

    if persistent.actSix == False:
        $ renpy.notify("You've unlocked Act Six in Act Select on the Main Menu!")
        $ persistent.actSix = True

    stop music fadeout 2.0

    pause

    scene avalonactsix with dissolve

    pause

    scene 1bnightmare with fade

    morton "How the hell am I supposed to get into this crate?"
    morton "I packed the crowbar inside the crate,"
    morton "but to get into the crate, I need the crowbar!"

    yb "Um, Mr. Morton?"

    scene 2bnightmare with dissolve

    morton "[player_name]!"
    morton "Come on in, kid."
    morton "I thought I might see you today."

    scene 4bnightmare with dissolve

    yb "It looks like some of your things were delivered."
    yb "Is this car your first job?"

    morton "That's right, my man."
    morton "It's all comin' together."

    scene 5bnightmare with dissolve

    morton "Took me all day yesterday to haul these boxes over here."
    morton "Now it's gonna take me all day to unpack 'em."
    morton "But it should make for a pretty sweet shop once it's all done."

    scene 6bnightmare

    yb "That's really cool, Mr. Morton."
    yb "I'm happy for you."

    scene 8bnightmare

    morton "You been keepin' at your workouts, kid?"
    morton "You haven't been slackin', have you?"

    scene 7bnightmare

    yb "No way! Check out these cannons!"
    yb "I was hoping I could borrow some tape while I'm here."

    scene 9bnightmare with dissolve

    yb "'Cause I'm so ripped!"
    yb "This isn't even my final form, Mr. Morton."

    scene 10bnightmare

    morton "Okay, [player_name], okay!"
    morton "You keep pointin' them guns at me, I'mma think you're robbin' me."

    scene 17bnightmare

    yb "Nah, I wouldn't rob you, Sir."
    yb "They've got way better stuff at the shop down the street."
    yb "I'd go after them instead."

    scene 12bnightmare

    morton "You're a funny guy, [player_name]"
    morton "But I'm sure you didn't come just to chat with ol' Morton."

    scene 15bnightmare

    yb "I don't mind, Mr. Morton."
    yb "It's nice hanging out with someone that laughs at my jokes and doesn't make fun of my hair."

    scene 11bnightmare with dissolve

    yb "I get teased about being ginger all the time."
    yb "I've even gotten beat up a few times, just for having red hair."

    scene 12bnightmare

    morton "You know what I learned a few years ago, [player_name]?"
    morton "You gotta have thick skin. Focus on the good people, ignore the bad."
    morton "And decent folk like us, we gotta stick together."
    morton "You dig?"

    scene 14bnightmare

    yb "Yeah, I dig, Mr. Morton."
    yb "It's hard sometimes though. Especially when people get..."
    yb "You know. Violent."

    scene 16bnightmare

    morton "Violence is a tool for the ignorant, [player_name]."
    morton "Unfortunately, it's a tool frequently utilized. But you can't just let
        people hurt you."
    morton "Stop by here when you've got some free time."
    morton "I'll teach ya some boxing techniques so you can defend yourself."

    scene 15bnightmare

    yb "That'd be rad, Sir!"
    yb "I'll do that!"
    yb "Thank you!"

    scene 18bnightmare

    morton "I know you're here for somethin' else right now though."
    morton "After hearing the story about your friend's guitar,"
    morton "I decided to take some extra time on this."

    scene 19bnightmare with dissolve

    morton "I've worked with jewelry some. Not much, but some."
    morton "This is my best work."

    yb "Wow, really?"
    yb "Johnny misses that guitar."
    yb "I'm sure he'll love this."

    scene 20bnightmare with dissolve

    morton "There ya are."
    morton "It should be quality enough to last a lifetime."

    scene 21bnightmare

    yb "This is awesome!"
    yb "How'd you make it?"

    morton "A trade secret!"
    morton "You didn't leave me a lot to work with."
    morton "I had to use every bit of metal there was."

    scene 22bnightmare with dissolve

    yb "This is impressive, Mr. Morton."
    yb "You have no idea how much I appreciate it."

    scene 23bnightmare

    morton "It was my pleasure."
    morton "And remember, stop by anytime."
    morton "I might even put ya to work!"

    yb "I will."
    yb "Thanks again!"

    scene 24bnightmare with fade

    yb "Johnny!"
    yb "I've got a present for you, man!"
    yb "You're going to love it."

    play music "audio/a_way_out.mp3"

    scene 25bnightmare

    yb "I found a guy that said he could make something out of the metal from your
        broken guitar."
    yb "It took a week, but I got it!"

    scene 26bnightmare with dissolve

    yb "Oh, sorry."
    yb "Did I wake you?"

    scene 27bnightmare with dissolve

    yb "I didn't know you were sleeping."
    yb "Johnny?"

    scene 28bnightmare with dissolve

    yb "Johnny..?"
    yb "Are you--"
    yb "No..."
    yb "No, no. Please, no."
    yb "Please get up."

    scene 29bnightmare with dissolve

    yb "You can't be gone. You can't!"
    yb "I can't do this without you, man."
    yb "You can't leave me."
    yb "You're all I have."

    scene 30bnightmare with dissolve

    yb "Please don't do this to me."
    yb "I'm not strong enough."
    yb "Please..."

    if monogamy == True:
        scene 1abwakesix with vpunch

        stop music

        b "Johnny!"

        a3 "Wha..!"
        a3 "Uncle??"

        scene 2abwakesix with dissolve

        a3 "A-are you okay?"
        a3 "What's wrong?"

        b "I..."
        b "I saw him."
        b "He was so still. And his eyes, there was..."
        b "There was no one behind them."

        a3 "You mean... you mean my dad?"

        scene 3abwakesix with dissolve

        a3 "Oh, [player_name]. I'm so sorry."
        a3 "Do you have nightmares like this a lot?"

        b "Uhn. Yeah. A few times a month."
        b "They're not usually this bad though."

        a3 "That's a lot, Uncle."
        a3 "You've been living like this for all these years?"

        b "I kept thinking it would get better."
        b "But it..."

        a3 "It hasn't."
        a3 "Lay back down."

        scene 4abwakesix with dissolve

        a3 "In the morning, we'll go see Dr. Yu."
        a3 "He'll know what to do."

        b "If you think that's best."

        ai3 "{i}I've been so focused on myself, I hadn't even considered how hurt
            [player_name] might be.{/i}"
        ai3 "{i}How has he lived like this for so long?{/i}"
        ai3 "{i}What kept him going?{/i}"

        jump wakesix

    else:
        if octavia == True:

            scene 2abowakesix with fade

            pause

            scene 1abowakesix

            pause

            scene 3abowakesix with dissolve

            o2 "Wha--!"
            o2 "F-fear..?"

            scene 4abowakesix with dissolve

            o2 "[player_name]?"
            o2 "[player_name], calm down."
            o2 "Everything is alright. You're here with us."

            a3 "Hm..?"

            scene 5abowakesix with dissolve

            a3 "What's... what's going on?"

            o2 "[player_name] is having a nightmare."
            o2 "It's a bad one."

            a3 "He's... what?"

            o2 "[player_name], you have to settle down."
            o2 "Wake up."

            scene 6abowakesix with vpunch

            b "Johnny!"
            b "D-don't..!"
            b "Don't leave me..."

            o2 "Look at me, [player_name]."

            scene 8abowakesix with dissolve

            b "Huh?"
            b "Where..?"

            o2 "It's me, it's Octavia."
            o2 "Everything is alright. You're alright."
            o2 "Take a deep breath."

            b "I had a nightmare."

            scene 7abowakesix with dissolve

            a3 "Johnny?"
            a3 "You... you had a dream about my dad?"
            a3 "Was it..?"

            scene 9abowakesix with dissolve

            b "When I found him. Yeah."
            b "I remember it so vividly."
            b "He was pale. And still. Just, so still..."

            a3 "I'm so sorry, Uncle."
            a3 "Are you okay?"

            b "I just need a minute."

            o2 "Do you have these nightmares often, [player_name]?"

            b "A few times a month."

            o2 "That's a lot. You need to talk to someone, [player_name]."
            o2 "I had no idea you were hurting so much."

            a3 "We'll go see Dr. Yu in the morning."
            a3 "Let's go to bed for now though, alright?"

            b "Mhmm."

            scene 10abowakesix with dissolve

            ai3 "{i}I had no idea [player_name] was in so much pain.{/i}"
            ai3 "{i}I've been so focused on myself, I hadn't thought he might
                be struggling.{/i}"
            ai3 "{i}What's kept him going all these years if he's hurting that badly..?{/i}"

            jump wakesix

        else:

            scene 1abdwakesix

            pause

            scene 2abdwakesix with vpunch

            b "Johnny!"

            a3 "Wha--!"

            d "Nyah!"

            scene 3abdwakesix with dissolve

            a3 "U-uncle?"
            a3 "Are you alright?"

            d "What's wrong? What happened?"

            b "I saw him. I saw him again."
            b "He was... he was gone..."

            a3 "You mean my dad?"
            a3 "You had a nightmare about my dad?"

            b "I can't... I can't breathe."

            a3 "Hey, look at me."

            scene 4abdwakesix with dissolve

            a3 "You're here with us."
            a3 "We'll take care of you."
            a3 "Just take a deep breath."

            b "It was so real."
            b "I felt like I was there all over again."

            a3 "Do you have these nightmares often?"

            scene 3abdwakesix with dissolve

            b "A few times a month."
            b "They're not usually this bad."

            d "Shit, man. That's... that's a lot."

            a3 "We need to go see Dr. Yu in the morning."
            a3 "He'll know what to do."

            d "Let's get you to bed, Big Guy."
            d "Come on."

            scene 5abdwakesix with dissolve

            a3 "I had no idea you were in this much pain."
            a3 "Why didn't you tell me?"

            b "I've just sort of gotten used to it."

            d "I don't think you get used to nightmares like that, [player_name]."

            ai3 "{i}How did I not notice how hurt he is?{/i}"
            ai3 "{i}I must have been too wrapped up in my own troubles.{/i}"
            ai3 "{i}How has he kept on for so long like this..?{/i}"

            jump wakesix

    label wakesix:

        stop music fadeout 1.0

        scene 1wakesix with fade

        bi "{i}I can't believe how real that nightmare was.{/i}"
        bi "{i}I thought with my life going so well now, I wouldn't have those dreams
            anymore.{/i}"
        bi "{i}I guess I was wrong...{/i}"

        play sound "audio/doorknock.mp3"

        a3 "Uncle [player_name]?"
        a3 "Are you in there?"

        scene 2wakesix with dissolve

        b "Yeah, I'm here."
        b "You can come in."

        play sound "audio/dooropen.mp3"

        scene 3wakesix with dissolve

        play music "audio/no_goodbyes.mp3"

        a3 "Hey, you."
        a3 "I was waiting for you."
        a3 "Are you ready to go?"

        b "I'm ready."
        b "I sat down for a moment."
        b "But then I... I couldn't get up."
        b "Isn't that strange?"

        scene 4wakesix with dissolve

        a3 "That nightmare got to you, didn't it?"

        b "Johnny always seemed so confident in what he was doing."
        b "It was as if he had life figured out."
        b "He was my guide, he got me through each day."
        b "Without him, I just feel..."

        a3 "Lost."

        b "Yeah."

        scene 5wakesix with dissolve

        a3 "I feel the same way, Uncle."
        a3 "I never know what the right answer is, or which direction to go."
        a3 "Maybe you and I can figure it out together?"

        b "Yeah, I'd like that."

        scene 6wakesix with dissolve

        b "Thank you, Avalon."
        b "You are your father's daughter."
        b "I see him when I look at you."

        a3 "That must make our kisses a little awkward, huh?"

        b "Yeah, that's why I have to close my eyes when we make out."

        a3 "Come on, Silly. Let's get going."
        a3 "We don't want to be late."

        scene 7wakesix with dissolve

        a3 "What do you think I'd be like if my dad was still around?"

        menu:
            "{b}Additional Dialogue Choice{/b}"

            "Guitar":
                b "I imagine you'd be a bitchin' guitarist chick in a
                    kickass rock n' roll band jammin' about anti-authority
                    rebel ideals."

                a3 "You think I'd be that cool??"

                b "I think you're already that cool."

                a3 "Pew pew! Cheese gun, fire!"

            "Motorcycle":
                b "I picture you wearing a leather jacket riding on a sweet motorcycle
                    livin' carefree with confidence unmatched by your peers."

                a3 "You think I'd be that badass??"

                b "Yeah but like, not more badass than me."

                a3 "If I'm not more badass than you in this scenario, how am
                    I riding a motorcycle?!"

                b "I'm going to need some aloe vera for that burn!"

            "Tattoos":
                b "Inked! I could see you having a sleeve of tattoos with a snake
                    wrapped around a dagger that's piecing through a skull."
                b "Or something equally freakin' awesome."

                a3 "I'm not into tattoos at all though! You think I'd be
                    that different?"

                b "I don't know. But I know whoever you would have turned out to be, I'd
                    still love the hell out of you."

                a3 "Careful, Uncle! You're going to attract mice with all that cheese!"

        scene 8wakesix with dissolve

        if monogamy == True:
            if octavia == True:
                a3 "I called Octavia earlier."
                a3 "She's going to meet us there."
            else:
                a3 "I called Dallas earlier."
                a3 "She's going to meet us there."

        else:
            if octavia == True:
                a3 "Octavia went home to change."
                a3 "She's going to meet us there."

            else:
                a3 "Dallas went home to change."
                a3 "She's going to meet us there."

        a3 "Uncle?"

        scene 9wakesix with dissolve

        a3 "Hey. What's wrong?"
        a3 "What are you looking at?"

        scene 10wakesix with dissolve

        a3 "Is.. is that where you found my dad?"

        b "Yeah, it is."
        b "He left the house to your mom when he passed but she couldn't bear to live in it."
        b "So she gave it to me."
        b "I didn't change anything. I kept all his stuff the same way."

        a3 "You found him on that couch? How can you still... be around it?"

        b "I don't know. I guess I just like being reminded that he was here."
        b "Even bad memories of him are still memories of him."
        b "Let's... let's get going, Avalon."

        scene 11wakesix with dissolve

        ai3 "{i}It's been so many years since then.{/i}"
        ai3 "{i}He really couldn't move on?{/i}"
        ai3 "{i}Can I... can I help him look forward?{/i}"

        scene 12wakesix with dissolve

        bi "{i}I shouldn't be dragging Avalon down like this.{/i}"
        bi "{i}She's come so far. I don't want her to move backward.{/i}"
        bi "{i}I have to pull myself together...{/i}"

        stop music fadeout 2.0

        scene 1fml with fade

        pause

        scene 2fml with dissolve

        merc "Look at him."
        merc "He's sound asleep."
        merc "He must be exhausted from yesterday."

        scene 3fml with dissolve

        f "Aw, yeah."
        f "Poor fella."

        scene 4fml with dissolve

        play music "audio/drummers_game.mp3"

        merc "Wait, what are you--?"

        scene 5fml with vpunch

        f "Wake up, Lance!"

        lance "Ah! Earthquake!"

        scene 6fml with dissolve

        f "I said be ready by nine!"
        f "Get your ass up!"

        scene 8fml

        lance "You said 'Be here by nine'!"
        lance "I'm here!"
        lance "I've got third-degree electrical burns on my anus!"
        lance "I'm on the mend, Goddammit!"

        scene 6fml

        f "And there are no earthquakes here, you mustachioed mutant!"

        merc "Yeah, she's right. We don't get those here."

        scene 8fml

        lance "That's why I was so scared!"
        lance "Idiot!"

        f "Get your shit together, Lance!"

        lance "I can't get my shit together! I can't even poop!"

        scene 9fml

        pause (.3)

        scene 10fml

        f "Come with me, Merc."
        f "We gotta fix you up."

        merc "Fix me?"
        merc "I didn't know I was broken."

        stop music fadeout 2.0

        scene 11fml with dissolve

        f "I stopped by the local convenience store before I came here."
        f "I found some cover-up that should be your shade."

        play music "audio/black_mermaid.mp3"

        merc "You want me to wear makeup?"
        merc "That's a little emasculating though, ain't it?"

        f "You have a dick on your face, Merc."
        f "Your masculinity is already toes up."

        lance "Better to be a queen than a queer, Merc!"
        lance "Where's the damn... tv remote..?"

        scene 12fml with dissolve

        f "Nobody will even notice you're wearing cover-up."
        f "I've gotten pretty good with this stuff over the years."

        merc "Hmm. Yeah? Alright, I trust ya."

        f "There's a lot of money here. Thought you guys were runnin' dry?"

        merc "Nah, it's all counterfeit. We use it for playin' cards."
        merc "It ain't good for nothin' else."

        scene 13fml with dissolve

        f "O-oh."

        merc "Shit. I'm too close, ain't I?"
        merc "A gal like you probably don't like turnin' around to see
            a big cock all the sudden."

        lance "Nah, they love that shit, man!"

        scene 14fml with dissolve

        f "Here, just turn your head."
        f "I need to apply this."

        scene 16fml

        lance "Your name is Faith, right?"
        lance "What an unusual coincidence."
        lance "My next girlfriend's name is Faith."

        merc "Really??"

        scene 24fml

        f "In your fuckin' dreams, you waddling cumduck!"

        lance "... What?"

        f "You heard me!"

        lance "What's a cumduck?"

        f "It's a duck that waddles about like a deformed penguin and splashes
            around in its own filth and semen!"

        lance "Uncalled for, man!"

        merc "I didn't know there were ducks that did that."

        scene 19fml with dissolve

        merc "Those are some creative insults you've been slingin'."
        merc "Where'd you hear those?"

        f "Well, that's a long story."

        merc "I don't think I'm goin' anywhere for a while."

        scene 18fml with dissolve

        f "Alright, well, it's a game my father and I used to play."
        f "He was... unique."

        merc "How so?"

        scene 20fml with dissolve

        f "He wasn't like normal people."
        f "His brain worked differently."
        f "He was... deranged. Disturbed."

        merc "Medicated?"

        f "No. We tried. Nothin' helped."

        scene 18fml with dissolve

        f "But he was still my father."
        f "I called him a 'bag of rabbit ass' once and he laughed and laughed."
        f "So we started playing a game a few times a week."
        f "We would come up with creative insults and fire them at each other."
        f "It was one of the few things we could bond over."

        scene 19fml with dissolve

        merc "Wow, that's pretty neat."
        merc "Did you have a favorite?"

        scene 18fml with dissolve

        f "Mhmm."
        f "He called me a 'Cosmic Dragon Fart' once."
        f "One of the rules to the game was you have to explain the insult."
        f "And he explained that one as 'A fart so potently acidic, it could
            dissolve the entire planet!'"
        f "'And if you were to ignite it, you'd cause a Big Bang!'"

        merc "Ahaha!"

        scene 15fml

        lance "Can we not talk about anuses right now!?"
        lance "Or what comes out of them!"
        lance "You need some fuckin' sensitivity training, man."

        scene 24fml

        f "You sure it's your butthole that's hurting and not your vagina,
            ya whiny little bitch!"

        lance "Hey, women are strong and beautiful creatures!"
        lance "So I take that as a compliment!"

        scene 21fml

        merc "Yeah, we respect women."

        f "What are you guys? Some sort of backward ass feminists?"

        merc "Feminists? Lance, what is that?"

        scene 15fml

        lance "Fuck no, we ain't no man-hatin', shit-spewin' feminists!"

        f "Feminism is about supporting female rights!"

        lance "Not no more, it ain't!"
        lance "We advocate without affiliation with any group."
        lance "Just 'cause we support one gender don't mean we condemn the other!"

        scene 26fml

        f "Where the fuck did that come from?"

        lance "I listen to a lot of podcasts."

        merc "We don't get out much."

        scene 21fml with dissolve

        f "And you just agree with everything he says, Merc?"

        merc "Well, he makes some good points."
        merc "I think..?"

        scene 15fml

        lance "Merc took the business end of a baseball bat to the back of the
            dome a few years ago."
        lance "His memory is all fucked up and he loses his train of thought pretty frequently."
        lance "But you better leave him alone about it or else I'll power through
            this pain and kick your ass!"

        scene 21fml

        f "I'm... sorry to hear that, Merc."
        f "That must be difficult to live with."

        merc "Mm. I don't think so."

        scene 19fml with dissolve

        merc "I feel pretty good today."
        merc "Especially now I won't have to walk around with a penis on my face."

        f "I'm glad I could help."

        scene 22fml with dissolve

        f "We gotta get the bitch that did this!"
        f "She may have turned your face into a lewd art gallery and ruined Lance's
            asshole."
        f "But she took my father away from me!"
        f "She's gotta pay!"

        scene 23fml with dissolve

        merc "Yeah!"
        merc "I can't believe she tricked me twice!"
        merc "But there's no way she can handle all three of us."

        scene 17fml with dissolve

        lance "I think I'm going to have to sit this one out guys."
        lance "And I don't mean that literally. I'm having a lot of trouble
            sitting..."
        lance "As much as I wanna bury that detective, I don't figure I'll be much use."

        scene 24fml

        f "For fuck's sake, Lance!"
        f "What {b}are{/b} you good for!?"

        lance "Let's see how well you do after making a Jacob's Ladder
            with your fuckin' ass cheeks!"

        scene 23fml with dissolve

        merc "Who is Jacob? And why does he have a ladder?"

        f "No, Jacob's Ladder is--"
        f "You know what, let's just focus on getting you finished up here."
        f "A little more and..."

        scene 28fml

        f "There we go!"
        f "All better."
        f "And you can't even notice you're wearin' makeup."

        merc "Really? That's great!"
        merc "Thank you."

        scene 27fml with dissolve

        f "You're welcome."
        f "Too bad we can't fix Lance's ugly mug."

        lance "Fuck you! I'm gorgeous!"

        scene 29fml with dissolve

        f "Without Lance, it's just you and me, Merc."
        f "But we do have one advantage;"
        f "We know where Penny lives."

        stop music fadeout 1.0

        scene 1btherapist with fade

        play music "audio/one_step_closer.mp3"

        a3 "So..."
        a3 "Are you feeling any better now?"
        a3 "Dreams fade over time, right?"

        bi "{i}I didn't. I felt heavy, weak.{/i}"
        bi "{i}That dream sapped the life out of me, my energy was just...gone.{/i}"
        bi "{i}But I couldn't do that to Avalon. I have to keep her spirits raised.{/i}"
        bi "{i}I have to act alright, even if I'm not.{/i}"
        bi "{i}For her.{/i}"

        scene 2btherapist with dissolve

        b "Yeah, I'm feeling a lot better."
        b "The car ride helped clear my head."

        scene 3btherapist with dissolve

        b "How was your date with Penny last night?"
        b "Did you have a good time?"

        scene 4btherapist

        a3 "I did! I've never met anyone like Penny before."
        a3 "She took me to a museum and showed me a Tyrannosaurus-rex!"
        a3 "And then she treated me to my favorite meal in the whole world!"
        a3 "She's so nice!"

        scene 6btherapist

        b "A Museum? For a date?"
        b "I thought you'd go to a club or something?"
        b "Well, I don't really know what girls do for fun these days."
        b "How'd she know your favorite food is Ramen?"

        scene 7btherapist

        a3 "I guess she's taken an interest in me."
        a3 "She tried to help me, too."
        a3 "Penny told me I should psyche myself up in the morning,
            be ready to take on the world every day."

        b "Did you try it this morning?"

        a3 "Well, no, I was a bit distracted..."

        scene 6btherapist

        b "I'm sorry, Avalon. That's my fault."
        b "I should be stronger for--"

        a3 "Stop."

        scene 4btherapist

        a3 "You've taken good care of me."
        a3 "Let me take care of you."

        b "I just--"

        scene 11btherapist

        sm "Mr. [player_name]?"
        sm "Dr. Yu can see you now if you're ready."

        if polygamy == True:

            scene 10btherapist

            b "Oh, right. Yes, I'm ready."
            bi "{i}I'm nervous about this.{/i}"
            bi "{i}Sharing private details of my life with a complete stranger...{/i}"
            bi "{i}How bizarre.{/i}"

            scene 9btherapist with dissolve

            ai3 "{i}Sun Mei is looking delicious today!{/i}"
            ai3 "{i}That tiny waist, those long legs...{/i}"
            ai3 "{i}I bet [player_name] could utterly destroy that little pu--{/i}"

            scene 12btherapist with dissolve

            ai3 "{i}Whoa! What the hell!{/i}"
            ai3 "{i}What has gotten into me?{/i}"
            ai3 "{i}Why am I thinking like that??{/i}"

            scene 13btherapist

            sm "If you'll just follow me this way, Sir."
            sm "I'll take you to the Gardens."

            b "The... Gardens?"

            scene 15btherapist with dissolve

            sm "Hm?"

            scene 12btherapist

            ai3 "{i}Oh crap! I think she just noticed me!{/i}"
            ai3 "{i}I should have been more subtle about ogling her.{/i}"
            ai3 "{i}She's probably so uncomfortable right now!{/i}"

            scene 14btherapist

            pause

            scene 16btherapist with dissolve

            pause (.4)

            scene 14btherapist with dissolve

            ai3 "{i}Did she..?{/i}"
            ai3 "{i}Did she just wink at me?!{/i}"

            scene 12btherapist

            ai3 "{i}She did!{/i}"
            ai3 "{i}She totally did!{/i}"

            scene 9btherapist with dissolve

            ai3 "{i}Oh my God, there is a river flowing through my panties right now.{/i}"
            ai3 "{i}I have got to get control of myself.{/i}"
            ai3 "{i}What is happening!?{/i}"

            jump atherapy_waiting

        else:

            b "Oh. Yes, I'm ready."

            scene 13btherapist

            sm "If you'll follow me this way, Sir."
            sm "I'll take you to the Gardens."

            b "Gardens?"

            sm "That's right."

            jump atherapy_waiting

        label atherapy_waiting:

        if octavia == True:
            if monogamy == True:
                scene 2aowait with fadefast

                o2 "Oh, Avalon."

                scene 1aowait with dissolve

                o2 "There you are."
                o2 "I got your message. Is everything alright?"
                o2 "Where is [player_name]?"

                scene 2aowait with dissolve

                a3 "Hey Octavia!"
                a3 "Um, yeah. Everything is alright."

                scene 7aowait with dissolve

                a3 "[player_name] went back to see Dr. Yu already."
                a3 "You just missed him."

                scene 3aowait with dissolve

                o2 "So what happened exactly?"
                o2 "You said he had a nightmare?"
                o2 "Does this happen often?"

                scene 4aowait

                a3 "Yeah, I think it does happen often."
                a3 "I'm pretty worried about him."
                a3 "Hopefully he'll be up for talking more about it after this."
                a3 "I want to do everything I can to help him!"

                scene 5aowait

                o2 "I'll be here to help as much as I can as well."
                o2 "You just let me know if there's anything I can do."

                scene 6aowait with dissolve

                a3 "Thank you, Octavia."
                a3 "How um... how was your night?"

                scene 5aowait

                o2 "Oh, Penny stopped by."
                o2 "We've decided to try again with our relationship."
                o2 "We're still in the early stages of our reunion but it's
                    looking positive."

                scene 3aowait with dissolve

                o2 "I am a bit concerned though."
                o2 "She says she's going to give up on her career as a detective
                    to be with me."
                o2 "I'm just not sure that's what she wants."

                scene 4aowait

                a3 "You didn't support her career choice?"
                a3 "Maybe I shouldn't pry but... why didn't you?"

                scene 3aowait

                o2 "My time in the military wasn't always pleasant."
                o2 "In fact, it was quite taxing sometimes."
                o2 "I don't condemn Penny's work, I just don't want it in my life."
                o2 "I want to distance myself from bad people and... well, her work
                    bleeds into our life."
                o2 "Often, unfortunately..."

                scene 4aowait

                a3 "She's giving up on being a detective to be with you then?"
                a3 "That sounds sort of romantic. But also sad."

                scene 6aowait with dissolve

                a3 "As long as you're both happy, I think that's what's important."

                scene 5aowait

                o2 "She insists that she can find something else."
                o2 "Besides, we're mostly in a trial period right now."
                o2 "We're going to take it slow and see how we feel about the
                    new direction of our lives."

                scene 7aowait

                a3 "That sounds great."
                a3 "Maybe we can go on a double date some time!"

                o2 "Yeah, maybe!"
                o2 "How was your date last night with Penny, by the way?"

                a3 "Oh I have to tell you all about it!"
                a3 "It was so great!"

            else:

                scene 1aowait with fadefast

                o2 "Oh, Avalon."

                scene 2aowait with dissolve

                o2 "There you are."
                o2 "Did [player_name] already go in to see the therapist?"

                a3 "Hey, Octavia! You just missed him."

                scene 7aowait with dissolve

                o2 "How is he doing?"

                a3 "Better!"
                a3 "But..."

                scene 4aowait with dissolve

                a3 "My father's death may be affecting him still."
                a3 "Not to mention grandma's and grandpa's passing."
                a3 "Do you think he may be hurting more that we realize?"

                scene 3aowait

                o2 "I did get that impression, yes."
                o2 "But let's not jump to any conclusions just yet."
                o2 "We'll see how this session goes and then find out if he feels like
                    opening up to us when it's through."

                scene 4aowait

                a3 "Okay. But Octavia..."
                a3 "I keep thinking about this morning, when I woke up and you were
                    talking to him?"

                o2 "Oh, yes?"

                a3 "He was asleep when I woke up."
                a3 "How did you know he was having a nightmare?"

                scene 5aowait

                o2 "Since my hand was on his chest, I could feel his heart racing."
                o2 "His body temperature raised and his back muscles tense."
                o2 "Even his teeth were grinding subtly."
                o2 "There were quite a few signs."

                scene 6aowait

                a3 "That's a lot to be able to pay attention to while you were asleep."
                a3 "Do those skills have something to do with your job in the military?"
                a3 "What would you even use those skills for?"

                scene 3aowait

                o2 "Well, yes."
                o2 "Mostly I was employed for my skills as a diplomat. I was especially
                    good at it because I could read the person across from me."

                a3 "Like a human lie detector?"

                o2 "Yes, but much more than that as well."

                scene 5aowait with dissolve

                o2 "I can usually tell when someone needs to urinate based on how
                    they hold themselves. Subtle movements speak volumes!"

                scene 6aowait

                a3 "You 'mostly' served as a diplomat?"
                a3 "What else did you do?"

                scene 3aowait

                o2 "Well, I used my skills for interrogation occasionally."
                o2 "It wasn't pleasant when I was asked to do that."

                scene 4aowait

                a3 "Did you..."
                a3 "Did you torture people?"

                scene 5aowait

                o2 "Absolutely not!"
                o2 "I wouldn't have even if I were asked."
                o2 "But I never needed to. I'm that good!"

                scene 7aowait with dissolve

                a3 "That's really cool, Octavia."
                a3 "I like hearing about your life. You're interesting."

                o2 "Thank you!"
                o2 "We've got plenty of time so you're welcome to ask me anything you
                    want!"

                a3 "Okay, how about..."

                jump b_dryu

        else:
            if monogamy == True:

                scene 1adwait with fadefast

                d "Hey, Avalon!"
                d "What's the haps, girl?"
                d "You said something happened with [player_name]?"

                scene 2adwait

                a3 "Hey, Dallas!"
                a3 "Yeah, come sit down."
                a3 "I'll explain."

                scene 3adwait with dissolve

                d "What's up?"

                a3 "So, [player_name] had a nightmare last night."
                a3 "It was a pretty nasty one."
                a3 "Apparently he saw my dad when he was... well, when he was gone."
                a3 "He said he has the same nightmare pretty often."
                a3 "I'm worried about him."

                scene 4adwait2

                d "Shit. That's terrible."
                d "I never really knew the whole story."
                d "[player_name] and your dad knew each other, right?"

                scene 3adwait

                a3 "They were really close."
                a3 "[player_name] found him on the couch when he was a teenager."

                scene 4adwait2

                d "You said he overdosed, right?"
                d "So [player_name] found him when he was just a kid?"
                d "That must have messed him up pretty bad."

                scene 3adwait

                a3 "Yeah, I think it did."
                a3 "But that's why we're here!"
                a3 "I hope this therapist can help him."

                scene 5adwait with dissolve

                a3 "But how are you?"
                a3 "Did you have a good morning?"

                scene 4adwait with dissolve

                d "Yeah, uhm, Penny stopped by last night."
                d "She wanted to..."
                d "Uhm, play?"
                d "So I dressed up as a supervillain and we..."
                d "Bow-chicka-wow-wow."

                scene 5adwait

                a3 "Oh my God! You... carpet-munching slutbag!"

                d "It's not like that!"

                scene 4adwait with dissolve

                d "We're going to give it a shot."
                d "You know. A relationship..."
                d "Penny and I are going to set up a date soon."

                scene 3adwait

                a3 "That's... great?"
                a3 "I guess I'm just shocked. It seems fast."
                a3 "The more I think about it though, it does seem like a smart match..."

                scene 4adwait

                d "I gotta tell you everything that happened last night!"
                d "It was hot!"

                a3 "No! My innocent ears! I won't hear it!"

                scene 5adwait with dissolve

                a3 "... Alright, I'm a little curious. Tell me everything!"

            else:

                scene 1adwait with fadefast

                d "Hey, Avalon!"
                d "Damn, that tummy looks bangin' this morning."
                d "Nice outfit choice!"
                d "Did [player_name] go back already?"

                scene 2adwait

                a3 "Hey, Dallas!"
                a3 "Thanks for the compliment? I feel both sexy and objectified."
                a3 "Anyway, yes, you just missed him."
                a3 "Come keep me company while we wait!"

                scene 3adwait with dissolve

                a3 "That was pretty freaky this morning, right?"
                a3 "It scared me when he woke up screaming my dad's name."

                d "Yeah, what was that about?"

                a3 "Apparently [player_name] has nightmares about when he found my Dad
                    overdosed on the couch."

                d "He's the one that found him!?"

                a3 "Yeah, it did a number on him too."

                scene 4adwait2

                d "Damn. That's gotta take its toll on someone."
                d "Is he alright?"

                scene 5adwait

                a3 "Well, he's got two wonderful gals to take care of him!"
                a3 "I'm sure with our support, he'll be fine."
                a3 "Right?"

                scene 4adwait

                d "I like the way you think!"
                d "With enough tugging, he'll be all better!"

                a3 "Ye-- wait, what?"

                jump b_dryu

        label b_dryu:

        stop music fadeout 1.0

        scene 17btherapist with fade

        play music "audio/plastic_dragon.mp3"

        bi "{i}It's Sun Mei, isn't it?{/i}"
        bi "{i}Why is she looking at me like she's starving and I'm a ham sandwich?{/i}"
        bi "{i}I must be seeing things. Maybe that's just how she looks at people?{/i}"

        scene 18btherapist with dissolve

        sm "I know this is your first session."
        sm "It's normal to be a little nervous at first."
        sm "But don't worry, that passes pretty quickly."

        scene 19btherapist

        b "I am admittedly a touch nervous. I'm just not sure what to expect."
        b "I just... talk to him?"
        b "Right?"

        scene 20btherapist

        sm "You can say as much or as little as you want."
        sm "The session lasts one hour."
        sm "Most people come once a week."

        b "Oh, I see. Alright, well, I guess--"

        scene 21btherapist with dissolve

        sm "Oh no!"
        sm "I've fallen!"

        scene 22btherapist with dissolve

        b "Careful! I got you."

        sm "Oh, thank you!"
        sm "I must have tripped."

        b "O-on what? You were standing still..."

        sm "How clumsy of me."

        scene 23btherapist with dissolve

        sm "I'm so lucky a big, strong man was here to catch me."
        sm "With large, muscular arms and a broad chest."
        sm "However can I repay you?"

        b "W-what!? Repay me??"

        dr "Sun Mei!"

        scene 24btherapist with vpunch

        sm "Ah!"

        scene 26btherapist

        dr "We have discussed this at length!"
        dr "This is not how you conduct yourself in the presence of others."
        dr "You must control yourself! And your urges!"

        scene 25btherapist

        sm "I just tripped, Grandpa."
        sm "Mr. [player_name] here saved me from a terrible fall."
        sm "That's all! I swear!"

        bi "{i}I am desperately uncomfortable right now.{/i}"

        scene 26btherapist

        dr "We shall discuss your behavior later."
        dr "Please conduct yourself professionally, especially while at work."
        dr "You will chase off all my patients at this rate!"

        scene 25btherapist

        sm "Okay, okay!"
        sm "I'm sorry!"

        dr "Please Mr. [player_name], this way."

        scene 27btherapist with dissolve

        dr "I sincerely apologize for my granddaughter."
        dr "She is... unique."

        b "Wow, this place looks incredible, Doctor."

        dr "I maintain it myself."
        dr "I find a relaxing environment helps my patients open up about themselves
            more easily."

        scene 28btherapist with dissolve

        b "And your granddaughter, Sun Mei, is one of your patients?"

        dr "Let's focus on you, Mr. [player_name]."

        b "Of course. I apologize."
        b "But she did say... I don't have to talk about everything. Right?"

        dr "I'm here to help you, my friend."
        dr "The more you say, the better I can help."

        b "I see."

        scene 29btherapist with dissolve

        dr "Would you like to have a seat?"
        dr "You're welcome to stand if you prefer."

        b "A seat sounds great."
        b "I've felt rather... heavy, today."

        scene 31btherapist with dissolve

        dr "May I ask what has you feeling this way?"
        dr "And do you feel this way often?"

        scene 38btherapist

        b "Well, I... I lost my best friend when I was fifteen."
        b "I came home and he was on the couch. He was... he was gone."
        b "And yeah, I guess I would say that I feel this way a lot."
        b "I usually spend time at the gym when I'm feeling down. It helps."

        scene 37btherapist

        dr "I am sorry to hear about your friend."
        dr "You must exercise a lot, judging by your physique."
        dr "Thirteen years is a long time to hold on to this event."
        dr "Is there perhaps more?"

        scene 30btherapist

        b "Well, I was adopted. My mother died when I was five."
        b "Cancer."
        b "My adoptive father had a heart attack several years ago."
        b "My adoptive mother took her life a year after."
        b "There was a time when all I had was Avalon."

        scene 38btherapist with dissolve

        b "And then, one day, she just didn't have time for me anymore."
        b "I felt like I'd lost her too for a while."

        dr "And the time when she was not in your life, what happened?"

        scene 36btherapist with dissolve

        b "I don't... I don't want to talk about that."
        b "It's... it's just..."

        scene 37btherapist

        dr "Mr. [player_name], it sounds as if this was a difficult period for you."
        dr "If you haven't discussed this with anyone and it is troubling you this much,"
        dr "I fear it will do great harm."
        dr "I am here to assist you in your recovery."

        scene 38btherapist

        b "Well, this is confidential, right? I guess it's alright to tell you."
        b "I found my father a few years ago. And I went to meet him."
        b "It was not a pleasant encounter. But he did tell me about someone he
            thought might be his daughter. And then he bribed me to leave him alone."
        b "I contacted the woman he thought might be his daughter and
            explained the situation to her."
        b "A week later, I went to visit her..."

        stop music fadeout 2.0

        scene 1leah2 with fade

        play music "audio/soft_reminder.mp3"

        l "Hmm."
        l "I wonder what he looks like?"
        l "He must have red hair like me, right?"

        play sound "audio/doorbell.mp3"

        pause (.2)

        scene 2leah2 with dissolve

        l "That's him!"
        l "He's here!"

        scene 3leah2 with dissolve

        l "Okay, deep breath, Leah."
        l "It's no big deal."
        l "He's just a regular guy."

        scene 4leah2 with dissolve

        l "H-hey."

        lb "Oh, hey. You're uhh, Leah, yeah?"

        l "The one and only!"
        l "Or, no, I guess there are other Leahs out there."
        l "Anyway, come on in!"

        scene 6leah2 with dissolve

        lb "Thanks. It's nice to meet you, Leah."

        l "Likewise! I'm... pretty excited about this."

        lb "You're excited to let a stranger into your home?"
        lb "What if I'm a total goon?"

        scene 8leah2

        l "That's weird of me to say, isn't it?"
        l "We should probably get that out in the open right now. I'm weird."
        l "I'm a weirdo."
        l "B-but, I mean, you're not a stranger if... you know..."
        l "Did you.. did you get the results back?"

        scene 7leah2

        lb "Yeah, I did."
        lb "That's uhh, why I stopped by."
        lb "And it looks like..."

        "Define relationship:"
        $ persistent.leah_rel = renpy.input("莉亚对[player_name]来说是什么？(按'回车'为'妹妹')。")
        if persistent.leah_rel.strip() == "":
          $ persistent.leah_rel = "妹妹"

        $ persistent.byron_rel = renpy.input("[player_name]对莉亚来说是什么？(按'回车'为'哥哥'。)")
        if persistent.byron_rel.strip() == "":
            $ persistent.byron_rel = "哥哥"

        $ persistent.relationship = renpy.input("他们彼此之间是什么关系？ (按'回车'为'兄妹'。)")
        if persistent.relationship.strip() == "":
            $ persistent.relationship = "兄妹"

        if persistent.relationship.strip() == "兄妹":
 
            lb "It was positive!"
            lb "We're [persistent.relationship]!"

            jump forward_unto_leah

        else:
            scene 6leah2 with dissolve

            lb "It was negative."
            lb "We're not related."

            scene 6leah2 with dissolve

            lb "But we can still be friends!"

            jump forward_unto_leah

        label forward_unto_leah:

        scene 9leah2

        l "Really!?"
        l "I have a [persistent.byron_rel]!?"
        l "Pinch me, I must be dreaming!"

        scene 10leah2

        l "Hug! Hug, hug!"
        l "We have to!"

        lb "Oh, yeah, alright."
        lb "Bring it in, [persistent.leah_rel]!"

        scene 11leah2 with dissolve

        lb "Whoa, jeez. I expected a regular hug!"
        lb "You wrapped around me like a boa constrictor."

        l "A special occasion calls for a special hug!"

        lb "Don't squeeze too tight, I had beans earlier."

        l "And he's funny!? Did I win the lottery today!? Uhh, yes I did!"

        scene 12leah2 with dissolve

        l "We have so much to talk about!"
        l "We can't spend all day in front of the door."
        l "There's so much to learn about each other!"

        lb "You put your crazy pants on today, huh?"

        l "Everyday!"

        scene 13leah2 with dissolve

        l "Come on! I'll race ya!"

        lb "To... the table? It's literally right in front of us."

        l "I'm going to win!"
        l "Pick up your feet, lazy!"

        scene 15leah2 with dissolve

        lb "This looks like a coffee table from a cafe."
        lb "Where'd you get this?"

        l "From a Cafe."
        l "They were replacing these old ones with new ones,"
        l "So I snagged one!"
        l "I got it for a steal."

        lb "You got it for a steal or you stole it?"
        lb "There's a difference."

        scene 14leah2 with dissolve

        l "What are you? The table police?"
        l "Money was tight for a while so I just took what I could get."
        l "I don't have much but I love what I have."

        scene 23leah2

        lb "Oh. I'm sorry."
        lb "I wish I had something to offer but I don't have any money myself."
        lb "I can't really help you out..."

        scene 16leah2

        l "Money troubles are all in the past."
        l "I --"

        scene 17leah2 with dissolve

        l "Eh? Oh, huh."
        l "I forgot I made this."

        lb "When did you make it?"

        l "Yesterday."

        scene 18leah2 with dissolve

        l "Anyway!"
        l "I went to college after High School."
        l "It was expensive! So I've been struggling to pay off the loans."

        lb "How much did you have to pay back?"

        l "One hundred and fifty thousand."

        scene 25leah2

        lb "That's a lot of money, Leah!"
        lb "You'd have to sell, like, fifteen kidneys to get that kind of cash."

        scene 24leah2 with dissolve

        lb "Alright, here's the plan."
        lb "We knock over a few ATMs, take the cash."
        lb "Then we go to Vegas and, using special card counting techniques,
            we quadruple our money."
        lb "And {b}then{/b}--"

        scene 20leah2

        l "Say no more, I'm in!"
        l "But actually, I've already paid back the money."
        l "You came up with that plan fast. It's almost as if you've already
            been planning this scheme..."

        lb "You can't prove that!"

        scene 18leah2 with dissolve

        l "So, I went to school for Biomechanical Engineering."
        l "After I received my master's degree, I started working!"
        l "I... actually make quite a lot of money."
        l "It didn't take long at all to pay off the loan."

        scene 25leah2

        lb "Wow, Pyrometal Engineering. That's impressive."

        l "Biomechanical Engineering."

        lb "Right. That's what I said."
        lb "But uh... what is that exactly?"

        scene 18leah2

        l "Well, I do research and development for mechanical systems that
            help people with disabilities or disorders live better lives."
        l "I only started a year ago though. We haven't had any breakthroughs yet."
        l "What, um... what do you do?"

        scene 24leah2

        lb "I don't really like working. It's not for me."
        lb "I'll do odd jobs here and there to keep my head above water,"
        lb "And I have a few people that give me some cash to help them exercise."
        lb "I get by."

        scene 21leah2

        l "Oh no. My only [persistent.byron_rel] is a useless bum??"
        l "Do [persistent.byron_rel]s come with a return policy?"
        l "Perhaps I can exchange you for a better one?"

        scene 26leah2

        lb "I am both offended and hurt."
        lb "Also, I might need to borrow five bucks for gas."

        l "Walk!"

        scene 22leah2 with dissolve

        lb "I just haven't had good experiences with work."
        lb "The entire structure of businesses seems degrading and backward."
        lb "You're supposed to submit yourself to someone else's authority and give
            them control over you."
        lb "I don't like the idea of someone else having that power over me."

        scene 20leah2

        l "There has to be a leader in any organized group or else you just have
            chaos."
        l "If nobody had to take responsibility for their actions, contribute to
            society or listen to authority... well, that's Anarchy."
        l "Are you an Anarchist, [persistent.byron_rel]?"

        scene 24leah2

        lb "Oh no, I fully agree that people should be held responsible for their
            actions and listen to authority."
        lb "But I believe I should be an exception to that rule."
        lb "That's all."

        l "You're bananas!"

        scene 27leah2

        l "So what's your life like?"
        l "Do you have a family or a girlfriend?"
        l "Give me the deets, buddy!"

        scene 25leah2

        lb "W-well, I'm not sure where to start."
        lb "My adoptive parents passed away a few years ago."
        lb "Their daughter, Sharol, and I aren't close."

        scene 23leah2 with dissolve

        lb "But Sharol had a daughter. We were close for a while."
        lb "She... she sort of lost interest in me when she turned fifteen though."
        lb "I haven't seen her in a while."

        scene 19leah2

        l "That's so sad. I'm sorry to hear that."
        l "I hope you're able to reconnect."
        l "What about her father?"

        scene 23leah2

        lb "He... died."
        lb "He was my best friend."
        lb "But I... well, I'd rather not talk about that."

        scene 22leah2 with dissolve

        lb "What about you?"
        lb "Where's ol' mom and dad?"
        lb "Brothers? Sisters?"

        scene 27leah2

        l "Nope!"
        l "My adoptive parents moved out of the country, so I don't see them
            very often."
        l "They adopted me when they couldn't get pregnant. I was their only adopted kiddo."
        l "I stayed here when they moved so I could go to college. So it's just me!"

        scene black with dissolve

        stop music fadeout 2.0

        b "I didn't want to tell her about the money I'd gotten from dad."
        b "Not yet..."
        b "We started spending time together. A lot of time."
        b "I kept my phone close. I kept expecting Avalon to call one day because
            she missed me."
        b "But that call never came..."

        dr "So you continued to spend time with Leah?"

        b "Yeah, we just kept getting closer and closer..."

        scene 29leah2 with dissolve

        play music "audio/aint_it_funny.mp3"

        l "Before we can move the new table in, we have to move the old table out."
        l "That's where you come in!"

        scene 28leah2

        lb "You could help, you know."
        lb "This would go a lot faster if you just grabbed the other end."

        scene 29leah2

        l "Let's use this as an opportunity for a teaching moment."
        l "We'll help you get used to listening to authority."
        l "Now, take this outside, [persistent.byron_rel]."
        l "Chop chop!"

        scene 28leah2

        lb "I don't want a lesson in servitude, thank you!"

        l "Remember to lift with your legs."

        lb "I know how to lift!"

        scene 30leah2 with dissolve

        lb "Stupid... [persistent.leah_rel]..."
        lb "Ugh! It... it won't fit!"

        l "Turn it! Flip it sideways!"
        l "Tetris the shit out of that table!"

        lb "I hate Tetris!"

        scene 31leah2 with vpunch

        lb "Oof!"
        lb "Okay, I got it!"

        l "Good job, loyal worker bee!"

        scene 32leah2 with dissolve

        lb "There's just one more thing we gotta get rid of."

        l "What? No, that was all."
        l "There's nothing else."

        lb "Oh, there's definitely one more thing that's gotta go."

        scene 33leah2

        lb "You!"

        l "What!? Ah!"

        scene 34leah2 with vpunch

        l "Ahaha. No no, I'm not supposed to go!"
        l "You big dummy!"

        lb "We absolutely must get this out of here."
        lb "It's really loud and obnoxious. We can't keep it in the house."

        l "I'm not obnoxious!"

        lb "And the back end on this thing is way too big."
        lb "I'm not sure it's going to fit through the doorway!"

        l "Hey, my butt isn't that big!"

        scene 35leah2 with dissolve

        l "Ahaha. I'm going to have to write you up for this!"
        l "You've got disciplinary action in your future, Mister!"

        lb "You can't discipline me! You're not my supervisor!"

        stop music fadeout 1.0

        scene black with dissolve

        b "We just... connected."
        b "There was a sort of chemistry between us."
        b "Without Avalon around, I didn't have anyone else."

        dr "I see. Please, continue."

        b "Well, the weeks went by and we spent a lot of time together..."

        scene 36leah2 with fade

        play music "audio/your_hand_in_mine.mp3"

        l "I'm changing, I'll be out in a second. Don't look!"

        lb "I'm going to be honest with you, Leah. This new table looks like
            butt."

        l "What!? It's an antique! It was really expensive!"

        lb "An antique? So it's not just butt, it's old butt."

        l "It's been restored!"

        scene 37leah2 with dissolve

        lb "You can polish a turd but... it's still a turd."
        lb "So is this what you're going to do with your big paychecks?"
        lb "Buy furniture that doesn't match with anything else in your tiny
            home?"

        l "What do you mean 'Doesn't match'?"

        scene 38leah2 with dissolve

        lb "It's completely out of place here!"
        lb "It looks like it is from the seventeenth century or something."

        l "Okay, Martha Stewart!"
        l "I'm sorry you don't approve of my Feng Shui, but it's staying!"

        scene 39leah2 with dissolve

        lb "What's Dungshay?"

        l "I don't know. I heard a smart person say it once."
        l "I think it fits this context but I'm not sure how or why."

        lb "I tried using a big word to sound smart once."
        lb "Someone was admiring feet and I said they had really nice mitosis."
        lb "They called me out on it though."

        scene 39leah2 with dissolve

        l "Isn't that when water goes through a solid or something?"

        lb "I think that's osmosis."

        l "I thought osmosis had something to do with space?"

        lb "Because... it sounds like Cosmos?"

        scene 40leah2 with dissolve

        lb "Didn't you go to college?"

        scene 41leah2 with dissolve

        lb "Oops!"

        scene 42leah2

        pause (.7)

        scene 43leah2 with dissolve

        pause (.3)

        scene 44leah2 with dissolve

        l "Hey!"
        l "I said I was changing!"

        scene 45leah2

        lb "Sorry! I figured you were done."
        lb "I did {b}not{/b} do that on purpose!"

        l "You didn't see anything right?"

        lb "What?"

        l "It's polite to say you didn't see anything."

        scene 46leah2 with dissolve

        lb "Of course I saw something. I saw your breasts!"
        lb "How could I not? They're like little planets!"

        scene 47leah2 with dissolve

        lb "Hey, if I throw a marble at one, will it orbit your boob like a little moon?"
        lb "Like a... a boob moon!"
        lb "I bet there's a lot of astronauts that would like to travel to that des--"

        stop music
        play sound "audio/pillow.mp3"

        scene 48leah2 with vpunch

        pause

        scene 49leah2 with dissolve

        lb "Real mature, Leah."
        lb "You really took the high road on this one."
        lb "I'm so proud of you."

        scene 50leah2 with dissolve

        play music "audio/soft_reminder.mp3"

        lb "Hm?"

        l "It's okay, [persistent.byron_rel]."
        l "I forgive you for being a pervert."

        lb "Let's not forget that you're the one with no door to your bedroom."
        lb "And you could have changed in the bathroom!"

        l "Excuses, excuses!"

        scene 51leah2 with dissolve

        lb "So what are we watching?"

        l "It's a movie about a man that's a lot like you, actually."
        l "He calls himself 'The Dude' and he's a lazy, pot-smoking bum!"

        lb "Oh, does he work?"

        l "Nope!"

        lb "A man after my own heart."

        scene 52leah2 with fadefast

        "An hour and a half later."

        scene 53leah2 with dissolve

        lb "He just wanted to go bowling with his friends and drink milk."
        lb "Why did things have to get so complicated?"
        lb "Poor guy."
        lb "Alright, let's get you to bed, Leah."

        scene 54leah2 with dissolve

        pause

        scene 56leah2 with dissolve

        pause

        scene 55leah2 with dissolve

        pause

        scene 57leah2 with dissolve

        l "Hmm?"
        l "What... what's going on?"

        lb "You fell asleep during the movie."
        lb "I brought you to your bed."

        l "Oh. Mm. Thank you."

        lb "You're welcome. I'll be on the couch if you need anything."

        l "No. Stay with me."

        lb "Are you sure?"

        l "Mhmm. My bed is big enough for two."

        scene 58leah2 with dissolve

        lb "Just to warn you, I drool when I sleep."
        lb "Like, a lot. I've soaked entire pillows before."

        l "Well, we can't have that. I guess I'll have to put a sock in your mouth
            or something."

        lb "I tried that once. I woke up and the sock was gone!"
        lb "I think I swallowed it."

        scene 59leah2

        lb "I noticed this before. What is it?"

        l "It's a tattoo."

        lb "Oh, you must be part of the Triple O."

        l "What's that?"

        lb "The Obvious Observations Organization."
        lb "I know it's a tattoo, doofus. What's it for?"

        scene 66leah2 with dissolve

        l "I have a heart condition called Autoimmune Myocarditis."

        lb "What's that?"

        l "My own immune system has a tendency to attack my heart."

        lb "That... sounds serious."

        l "Well, it was. I spent a lot of time in hospitals when I was younger."
        l "And my favorite sound was the beeping of the heart monitor."
        l "It meant my heart was still beating. I was still alive."

        scene 62leah2

        lb "That must have been really difficult."
        lb "I'm sorry I wasn't there for you, Leah. Sincerely."

        scene 61leah2 with dissolve

        lb "I guess that's what the tattoo is then?"
        lb "A heartbeat?"

        l "It's kind of silly, right?"

        lb "I don't think it is."
        lb "Are you better now?"

        scene 66leah2 with dissolve

        l "I was part of a clinical drug trial a few years ago."
        l "It was an experimental therapy for my specific condition."
        l "Statistically, it was a failure. It didn't help most people."
        l "But I guess I got lucky. I haven't had any trouble since."

        lb "That's incredible!"

        l "Yeah, but some damage had already been done."
        l "I have a higher than normal risk of a heart attack."
        l "So I have a pacemaker."

        scene 59leah2 with dissolve

        lb "A pacemaker? Shouldn't there be a bump here then?"
        lb "And a scar?"

        l "Mhmm. Part of the trial was to test a pacemaker about the
            size of a bullet."
        l "They put it in through a small incision in my armpit."
        l "No scar, no bump!"
        l "Cool, huh?"

        scene 61leah2 with dissolve

        lb "Is that what got you into the Biomechanical Engineering field?"

        l "It is!"
        l "I want to be able to help people the way I was helped."

        lb "That's noble."
        lb "But that means you've got machine parts inside you."
        lb "Which makes you... a Cyborg!"

        scene 66leah2 with dissolve

        l "What?! No!"
        l "I'm just a regular person!"

        lb "Yeah, a regular person modified with cybernetic enhancements!"

        l "It just insures my heart keeps beating! It doesn't give me superpowers!"

        show leah_bot

        lb "'Beep, Boop.'"
        lb "'I am Leahbot 5000.'"
        lb "'I drink motor oil and eat children.'"
        lb "'Boop, Beep.'"

        scene 65leah2

        l "Stop!"
        l "You're such a dork sometimes."
        l "Anyway, I was wondering, um.."
        l "How did you find out about me?"
        l "I mean, you sent me a letter saying you thought we might be siblings."
        l "The next thing I know, I'm getting a DNA test to find out if I'm related
            to someone I've never even met."

        scene 62leah2 with dissolve

        lb "Oh, yeah, about that..."
        lb "I met father for the first time about a year ago."
        lb "He asked me never to darken his doorstep again."
        lb "In exchange, he gave me some money and some information about mom and you."
        lb "I don't know if he did it out of guilt or... or what."

        l "You met him??"
        l "Is he--?"

        scene 61leah2 with dissolve

        lb "He's a fiend, Leah."
        lb "Trust me."

        l "How, um, how much money did he give you..?"

        scene 62leah2 with dissolve

        lb "Actually, quite a lot. I didn't tell you before because...
            well, I didn't know you yet."
        lb "I just didn't know what to expect when I met you so I kept it a secret."

        scene 61leah2 with dissolve

        lb "I'm happy to share it with you though!"
        lb "I mean, now that we've gotten to know each other."
        lb "You might be able to get some replacement parts for your android body!"

        scene 65leah2

        l "You make jokes a lot when things get serious."
        l "But no, I don't need any money. You can keep it."

        lb "Seriously?"

        l "Yeah, [player_name], you're a bum. You need it more."
        l "Sloth."

        stop music fadeout 2.0

        scene 68leah2 with dissolve

        b "It was that night that I realized we were getting..."
        b "Too close."
        b "I mean, we were [persistent.relationship]. I didn't want to complicate that."

        dr "I understand."
        dr "But you haven't seen her in a while? Did something happen?"

        b "One day, we went to the local neighborhood pool together..."

        scene 69leah2 with fade

        play music "audio/soft_reminder.mp3"

        lb "Leah!"
        lb "Hey!"

        scene 70leah2 with dissolve

        l "[player_name]!"
        l "I wasn't sure you were going to make it."
        l "You're late!"

        scene 71leah2

        lb "I lost track of time at the gym."
        lb "How are you today, [persistent.leah_rel]?"

        scene 72leah2

        l "I'm doing very well."
        l "I have a question for you though."

        lb "Shoot."

        l "What's it like at the Y.M.C.A.?"
        l "Is it fun to hang out with all the boys?"

        scene 73leah2

        lb "I'll have you know these were on sale for a really good price."
        lb "I practically got them for a steal."

        l "You got them for a steal or you stole them?"
        l "There's a difference."

        lb "Don't use my own jokes against me. They're trademarked. I'll sue."

        scene 72leah2

        l "Do they charge by square inch of fabric?"
        l "If so, what did that cost? A quarter?"

        scene 74leah2

        lb "I'm sorry, I couldn't hear you over how good I look."
        lb "Wearing less just accentuates my incredibly sexy physique, Leah."
        lb "I wouldn't want to deny the ladies a show, would I?"

        scene 75leah2

        l "Stop! There's not even any ladies here, you goofball!"
        l "Look around. It's literally just us."

        l "And being strong doesn't make you look any less creepy with those girly
            boyshorts you're wearing."
        l "Look, they have little hearts on them!"
        l "Hearts are my thing!"

        scene 76leah2

        lb "Well look at you!"
        lb "You're wearing a flannel pattern."
        lb "Flannel is my thing!"

        scene 77leah2

        l "I-I know..."
        l "I didn't use to like flannel but it's..."
        l "I don't know, it's growing on me."

        scene 78leah2 with dissolve

        stop music fadeout 2.0

        l "Is that why you've got little hearts on your shorts?"
        l "Am I growing on y--"

        scene 79leah2

        play music "audio/aint_it_funny.mp3"

        lb "No more talking!"
        lb "It's time for swimming!"

        l "Wait, what are you--"

        scene 80leah2 with vpunch

        l "Ah!"

        lb "I hope you're ready, [persistent.leah_rel]!"
        lb "'Cause you're going in the hard way!"
        lb "Mwahaha!"

        l "No, no! Please, don't!"
        l "Stop! Let me down!"

        scene 81leah2 with dissolve

        lb "W-what?"

        l "You're scaring me!"
        l "Please put me down!"

        lb "I'm just playing around, Leah."
        lb "It's just water."

        l "Please, [player_name]. Please put me down."

        scene 82leah2 with dissolve

        lb "Okay, here."

        l "Thank you."

        scene 83leah2 with dissolve

        lb "I'm sorry, Leah."
        lb "I didn't mean to scare you."
        lb "I was just goofing ar--"

        scene 84leah2 with vpunch

        l "Gotchya, sucker!"

        scene 85leah2

        lb "This betrayal will not be forgotten!"

        scene 86leah2

        play sound "audio/splash.mp3"

        l "Oh yeah!"
        l "You mess with the queen, you get the guillotine!"
        l "Ahoo, ahoo, ahoo!"

        scene 87leah2 with dissolve

        lb "Aw man, you got me good!"
        lb "I'm so damn proud of you right now."
        lb "I can't even believe it."

        l "You're too easy."

        scene 88leah2

        l "I've noticed you have a weakness for girls in distress."
        l "And it is so easy to play on that."

        scene 89leah2 with dissolve

        lb "You were so convincing!"

        l "I took acting lessons in high school."
        l "I really disliked it though."
        l "In fact, I had a serious urge to burn the stage down!"

        lb "Oh, I'm glad you didn't!"
        lb "That would have made for a terrible story."

        l "You mean that would have been a terrible decision?"

        lb "Yeah, what did I say?"

        l "Story."

        stop music fadeout 2.0

        scene 90leah2 with dissolve

        lb "Ugh! I must be exhausted from having been brutally assaulted a
            moment ago."

        scene 91leah2 with dissolve

        lb "Some crazy redhead pushed me into a big hole in the ground!"

        l "At least that hole had water in it!"

        scene 92leah2 with dissolve

        play music "audio/soft_reminder.mp3"

        l "Hey, I uhh..."
        l "I have something to tell you."

        lb "Oh?"

        l "Yeah, but uhm..."
        l "It's a secret."

        scene 93leah2 with dissolve

        l "So I have to whisper it to you."

        lb "Whoa, what are you--"

        l "I like you, [player_name]."
        l "These last months that we've spent together, they've been some of the
            best days of my life."
        l "After my foster parents left, I felt so alone. I didn't have anyone."
        l "But now, with you, I'm... happy."
        l "I know we're [persistent.relationship], but I..."
        l "I want more."

        scene 96leah2

        lb "This is a bad idea, Leah."
        lb "We shouldn't."
        lb "We can't!"

        scene 94leah2

        l "We don't have anyone else, [player_name]."
        l "Everyone else has abandoned us."

        lb "But we're--"

        l "Who cares??"
        l "Nobody has to know we're [persistent.relationship]."
        l "This could be our only chance for a relationship."

        scene 96leah2

        lb "We need to take a step back."
        lb "This is complicated. We should think about it."

        scene 95leah2

        l "You've felt it, haven't you?"
        l "The spark between us?"
        l "We would be happy together, [player_name]."
        l "I can make you happy."

        stop music fadeout 1.0

        scene 97leah2

        l "Mm."

        scene 98leah2 with dissolve

        play music "audio/heartbeat_of_the_hood.mp3"

        lb "I said 'No'."
        lb "Please get off me, Leah."

        scene 99leah2 with dissolve

        l "Why are you being like this?"
        l "You know you feel the same way."

        lb "I don't know what I feel, Leah."
        lb "You're my [persistent.leah_rel]. I'm not sure I want to be more than that."
        lb "I'm not sure I {b}can{/b} be more than that."

        l "W-why not..?"

        lb "Look, I think we should spend some time apart."
        lb "I'm going to go."

        scene 100leah2

        l "W-wait! Please!"
        l "I'm sorry!"
        l "Please don't leave me..."

        lb "This was a mistake. We can't..."
        lb "I have to go."

        l "I'll apologize again! I'm sorry!"
        l "I'll say it a thousand times if you want!"
        l "I'm sorry, I'm sorry!"

        lb "Goodbye, Leah."

        scene 101leah2

        l "No, no!"
        l "What have I done??"
        l "I'm sorry!"
        l "I'm sorry..."

        stop music fadeout 2.0

        scene black with fade

        pause

        scene 37btherapist with dissolve

        play music "audio/plastic_dragon.mp3"

        dr "It sounds as if she did not take the rejection well."
        dr "What were your feelings regarding her confession of love?"
        dr "And do you believe you could have handled the situation better?"

        scene 36btherapist

        b "I hurt her..."
        b "I just panicked. For so many reasons, I didn't think it was a good idea."
        b "And having her just corner me like that, I..."
        b "I needed time to think about it. And I should have articulated that
            to her better. I see that now."
        b "She was beautiful, talented, smart. I'm... I'm a mess. I can barely
            pull myself out of bed most mornings."
        b "I wanted better for her. She deserved better."

        scene 33btherapist

        dr "You keep referring to Leah in the past tense."
        dr "Did something happen to her?"
        dr "Is she no longer around?"

        scene 34btherapist

        b "I spent three days pacing around my house."
        b "I couldn't think of anything other than what happened at the pool."
        b "I couldn't think about anything other than her..."
        b "Three days past and I made a decision; I wanted to be with her."

        dr "So you went to see her?"

        scene 36btherapist with dissolve

        b "I tried. She wasn't home. She wasn't answering her phone."
        b "Days past and I couldn't get in touch with her. I stopped by her place
            every day."
        b "I called the police after a week. I contacted everyone I could that
            might know what happened to her."
        b "She just vanished. I don't even know if she's alive..."

        scene 37btherapist

        dr "That must have been frightening."
        dr "How long has it been?"
        dr "You have still not heard anything?"

        scene 34btherapist

        b "It's been six months. And no, I haven't heard anything."
        b "But Avalon, she did the same thing to me."
        b "She wanted a relationship from me and... I was conflicted about it."
        b "I was too afraid to say 'No'. I was afraid that what happened to Leah..."
        b "Would happen to her..."

        dr "But you are happy with Avalon?"

        scene 30btherapist with dissolve

        b "Immensely."
        b "I wouldn't trade what I have with her for anything in the world."
        b "But... I would have preferred more time to contemplate an intimate relationship, I guess."
        b "I wish... I wish we went slower with our relationship."
        b "I worry that our partnership isn't healthy for her. I worry that
            she would be better off with someone else."

        scene 31btherapist

        dr "I do not mean to marginalize your feelings but that is quite common
            for people to feel that way."
        dr "After my discussion with Avalon yesterday, I can tell her relationship
            with you has helped greatly to accelerate her recovery."
        dr "You are obviously the most influential person in her life right now."
        dr "And as far as I can tell, you affect each other in a mutually positive
            way."

        scene 33btherapist with dissolve

        dr "But [player_name], I am extremely concerned about your mental wellbeing."
        dr "You have endured some terrible things in your life."
        dr "Our time is up for today, but I must insist that you return regularly."
        dr "A dam can only hold back the raging river for so long before it crumbles."

        scene 30btherapist

        b "Well, I do feel better."
        b "It's kind of nice to be able to unload some of this."
        b "Alright, I'll make an appointment with Sun Mei."

        dr "Let me walk you out."

        scene 39btherapist

        dr "Do not give up hope on Leah, Mr. [player_name]."
        dr "There are many possible reasons for her to disappear."
        dr "She very well may be back."

        b "Thank you, Dr. Yu."
        b "I'll try to stay positive."

        stop music fadeout 2.0

        if octavia == True:
            play music "audio/tomorrows_rain.mp3"

            scene 8aowait with fadefast

            a3 "Wow, Octavia! You're really strong!"
            a3 "I can't believe you can hold me up like this!"

            o2 "I told you I could carry you."
            o2 "I've had backpacks that were heavier than you!"

            a3 "How far could you throw me?"

            o2 "Pretty far, I'm sure!"
            o2 "At least a few feet."

            a3 "That's impressive!"
            a3 "Don't though."

            o2 "I wouldn't!"

            scene 10aowait

            b "Hey, girls."
            b "Aw, piggyback rides!?"
            b "Can I go next??"

            scene 9aowait

            a3 "Hey, Uncle!"

            o2 "[player_name], it's nice to see you."
            o2 "I think you're a little too heavy for me."
            o2 "How was your session? Do you feel any better?"

            a3 "Yeah! Tell us everything!"

            scene 11aowait

            b "It went well. You were right, this was a good idea."
            b "Dr. Yu was very helpful. I feel better!"
            b "But..."

            scene 13aowait with dissolve

            b "I have to... run an errand."
            b "Alone."
            b "It should only take me a few hours."
            b "Can you take Avalon home, Octavia? I'll meet you there soon?"

            scene 12aowait

            o2 "Oh. Alright then, we'll see you at home."

            scene 14aowait

            pause

            scene 15aowait

            a3 "I waited here for him so we could talk after."
            a3 "And then he just leaves..?"

            o2 "He may need some personal time to process everything."
            o2 "A first session can bring a lot of feeling to the surface."
            o2 "Let's give him some space."

            stop music fadeout 2.0

            jump at_home_six

        else:
            play music "audio/disturbed_mind.mp3"

            scene 6adwait with fadefast

            d "What if our specialty at the salon was that we could {b}uncut{/b}
                hair?"

            a3 "What do you mean?"
            a3 "Are you talking about hair extensions?"

            d "No, no, like we can add back your natural hair."
            d "As in, you know, reverse your haircut."

            a3 "You would take their old hair clippings and re-attach them somehow?"

            d "No, we just roll back the haircut."

            a3 "Did you think this out at all before you brought it up to me?"

            d "I did not."

            a3 "Maybe you should let that idea bake a little longer, Dallas."
            a3 "It's still raw."

            d "I'll do that."

            scene 8adwait

            b "Hey, girls."
            b "What's going on here?"
            b "Are you braiding each other's hair?"

            scene 7adwait

            a3 "Hey, Uncle!"

            d "Lookin' good in the pink today, [player_name]."
            d "Nah, we're brainstorming ideas for the salon."

            a3 "It's not going well. I think we need more brainpower."

            scene 10adwait with dissolve

            d "How did it go? Do you feel better?"

            a3 "Yeah, tell us everything!"
            a3 "How was it??"

            scene 9adwait

            b "It went well. I do feel... better."
            b "And I do want to talk about it."
            b "But..."

            scene 11adwait with dissolve

            b "I need to take care of something. Alone."
            b "It shouldn't take long, I'll be home in a few hours."
            b "Dallas, can you take Avalon home?"

            scene 12adwait

            d "Uhh, sure."
            d "If that's what you want."

            scene 13adwait

            pause

            scene 14adwait

            a3 "What was that about?"
            a3 "We waited here to talk to him after and then he just leaves?"

            d "Well, it is his first therapy session."
            d "Maybe he needs to process some things."

            a3 "I hope he's alright..."

            stop music fadeout 2.0

            jump at_home_six

        label at_home_six:

        if monogamy == True:
            ## Monogamy Sex Scene for Act Six - Mid ##
            label avasolosix_vibe:

            if octavia == True:
                scene 1aoactout with fade

                play music "audio/tomorrows_rain.mp3"

                a3 "Thanks for bringing me home, Octavia."
                a3 "Do you think [player_name] is alright?"
                a3 "He looked rather depressed..."

                scene 2aoactout with dissolve

                o2 "I'm sure he's just processing his session."
                o2 "He will need time to organize his thoughts before he opens
                    up to someone else."
                o2 "Give it time."

                a3 "Okay."

                scene 5aoactout

                a3 "Thank you for being there for me today."
                a3 "It would have been pretty boring sitting there for an hour
                    alone."

                scene 3aoactout

                o2 "It was my pleasure, Avalon."
                o2 "I enjoy our time together."
                o2 "Penny left in a panic this morning."
                o2 "She didn't tell me what it was about."
                o2 "I'm a little worried about her."

                scene 6aoactout

                a3 "That seems unusual."
                a3 "Have you texted her?"

                scene 8aoactout

                o2 "I don't want to distract her."
                o2 "Whatever is the matter, she's a tough cookie."
                o2 "She'll handle it and we'll talk tonight."
                o2 "Are you hungry?"

                scene 5aoactout

                a3 "Actually, I am."
                a3 "Should we go out to eat?"

                o2 "I can make something here."

                a3 "That sounds good!"

                scene 6aoactout with dissolve

                a3 "I, um, I'm feeling a bit sweaty."
                a3 "Would you mind if I took a quick shower?"

                scene 3aoactout

                o2 "Not at all."
                o2 "I'll put together a lunch for us and it should be
                    ready by the time you're done."

                a3 "Thank you, Octavia!"

                stop music fadeout 1.0

                jump avasolosix

            else:

                scene 1adactout with fade

                play music "audio/disturbed_mind.mp3"

                a3 "Dallas?"

                d "Mhmm?"

                a3 "Do you think [player_name] is alright?"
                a3 "He seemed sort of depressed before he left?"

                scene 2adactout with dissolve

                d "Yeah, I got that vibe too."
                d "I don't know, girl. He's pretty independent. Maybe he needs
                    to analyze the whole thing alone first."
                d "You know, let it all sink in. Organize his feelings?"

                scene 4adactout

                a3 "I guess that makes sense."
                a3 "I'm just worried about him."

                scene 5adactout

                d "Let's give him some time."
                d "He's a tough guy, Avalon."
                d "I bet he's alright."

                a3 "Yeah, he is strong..."

                d "Let me make us lunch!"
                d "I bet he'll be back by the time it's done."

                scene 3adactout

                a3 "Do you mind if I take a shower while you make lunch?"
                a3 "I'm feeling a bit sweaty today."

                scene 6adactout

                d "Ooh, feeling the need for some special relief?"
                d "Need to flick the bean?"

                a3 "What!? No!"

                d "It's cool, girl. You don't have to say."
                d "You go take care of yourself, I'll prepare us some food."

                scene 4adactout

                a3 "I really need a shower!"

                d "Uh-huh."

                a3 "Whatever. I'll... be back shortly."

                d "Enjoy!"

                jump avasolosix

        else:
            if octavia == True:
            ## Octavia Sex Scene for Act Six - Mid ##
                label aoactout:
                if _in_replay:
                    $ player_name = renpy.input("What would you like to name the MC?")
                    if player_name.strip() == "":
                        $ player_name = "Byron"

                scene 1aoactout with fade
                play music "audio/tomorrows_rain.mp3"

                a3 "Thanks for bringing me home, Octavia."
                a3 "You really think [player_name] is alright?"
                a3 "I'm worried about him."

                scene 2aoactout with dissolve

                o2 "He is."
                o2 "[player_name] is an independent person. He's learned to process
                    his feelings on his own."
                o2 "I'm sure he'll start sharing with you more and more as your
                    relationship blossoms."
                o2 "Give it time."

                a3 "You mean as {b}our{/b} relationship blossoms?"

                scene 3aoactout with dissolve

                o2 "Oh, you're very keen to the idea of this, aren't you?"
                o2 "Well, we did have a wonderful date."
                o2 "But we still shouldn't move too quickly."

                scene 5aoactout

                a3 "[player_name] and I have something really special. I couldn't
                    be happier than when I'm with him."
                a3 "But having you with us makes my relationship with [player_name]
                    feel more..."
                a3 "Complete."
                a3 "We're more than the sum of our parts."

                scene 3aoactout

                o2 "Oh, Avalon. Those are some of the kindest words I've ever heard."
                o2 "You're too sweet."

                scene 6aoactout

                a3 "W-well, I may have an ulterior motive."
                a3 "Now that we're home, I'd like to know what happened with you
                    and [player_name] last night."
                a3 "I mean, {b}after{/b} your date."

                scene 7aoactout

                o2 "O-oh. Yes. I guess we should discuss that, shouldn't we?"
                o2 "Admittedly, it went a bit further than I'd intended."
                o2 "We--"

                scene 6aoactout

                a3 "No."
                a3 "I don't want you to tell me."
                a3 "I... want you to show me."

                scene 8aoactout

                o2 "You little devil. What's gotten into you?"
                o2 "You were an innocent woman when I met you."
                o2 "And now you're asking for sex rather directly."
                o2 "How did we land here, sweet Avalon?"

                scene 5aoactout

                a3 "We had so much fun the other day after I cut your hair."
                a3 "I've been thinking about it a lot."
                a3 "It's hard to explain but I..."

                scene 6aoactout with dissolve

                a3 "I'm finding myself aroused a lot ever since I got together with
                    [player_name]."
                a3 "It's like I can't help myself."
                a3 "I just want more and more and more."

                scene 8aoactout

                o2 "We certainly should discuss that in greater detail."
                o2 "But for now..."
                o2 "Go to [player_name]'s room. I'll meet you there in a moment."
                o2 "I need to... prepare."

                a3 "Yes!"

                scene 9aoactout with fadefast

                ai3 "{i}It's as if my desire for sex has been dialed to the max!{/i}"
                ai3 "{i}I can't even think straight lately.{/i}"
                ai3 "{i}And after finding out that Octavia enjoys sex so much,
                        and after she was so forward after I cut her hair...{/i}"
                ai3 "{i}I just can't help myself. I {b}lust{/b} for her.{/i}"
                ai3 "{i}Ugh. Why am I like this?{/i}"

                o2 "Avalon?"

                scene 10aoactout with dissolve

                a3 "Hm?"
                a3 "O-oh, Octavia. You're..?"

                scene 11aoactout

                o2 "In my underwear?"
                o2 "Yes. I didn't want to wrinkle my clothes while we..."
                o2 "Mmm, play."

                scene 12aoactout with dissolve

                o2 "I also brought your little toy."
                o2 "For 'demonstration' purposes."
                o2 "You said you wanted me to show you what [player_name] and
                    I did last night?"

                a3 "Y-yeah. I did. I... do."

                scene 13aoactout with dissolve

                o2 "Well, we can't do a proper reenactment with your clothes on,
                    can we?"

                a3 "No?"

                o2 "So let's get you out of these clothes, shall we?"
                o2 "Go on, Avalon. Off with them."

                a3 "Okay."

                scene 15aoactout with dissolve

                pause

                scene 14aoactout with dissolve

                a3 "What should I do next?"

                o2 "You're not quite finished undressing, are you?"

                a3 "You... want me to take my pants off too?"

                o2 "Of course."
                o2 "We were naked, so you'll have to be too."

                a3 "[player_name] was completely naked??"

                o2 "Does that arouse you, Avalon."

                a3 "It.. it does, actually. Yeah."

                scene 16aoactout with dissolve

                a3 "Well, I guess I better get these off then."
                a3 "Erhm, come on. Stupid button."

                scene 17aoactout with dissolve

                a3 "There we go."

                scene 18aoactout with dissolve

                a3 "Okay, I'm completely naked now."
                a3 "What should I do next?"

                o2 "Crawl up on the bed and lie down."

                a3 "Did you guys--"

                o2 "No spoilers. Go on, Avalon."

                scene 19aoactout with dissolve

                o2 "Look at that caboose!"
                o2 "Those cheerleading workouts were effective, weren't they?"

                a3 "You like my butt? Really?"

                o2 "I do. Lie down, Avalon."

                scene 20aoactout with dissolve

                a3 "Like this?"

                o2 "That's exactly where [player_name] was."

                a3 "You saw his... his penis?"

                o2 "Oh yes."

                scene 22aoactout with dissolve

                a3 "What did it look like?"
                a3 "Is it big?"

                o2 "You want to hear about it?"

                a3 "Is that unusual?"
                a3 "I've been curious but I'm also a little afraid."

                scene 21aoactout with dissolve

                o2 "Well, there was nothing scary about it."
                o2 "In fact, he was a nervous nelly last night."

                a3 "Why?"

                o2 "He's afraid of rejection, like most people."
                o2 "So he didn't want to do anything I might dislike."

                a3 "What did you do?"

                o2 "I took the lead for our first sexual endeavor to put him at
                    ease."
                o2 "I took his hand and placed it on my breast to let him know
                    he could touch me."

                scene 23aoactout with dissolve

                o2 "And then I took his impressively hard erection in my hand and
                    stroked it back and forth."
                o2 "Just to get a feel for it, figuratively and literally."

                a3 "What... what did it feel like?"

                scene 24aoactout with dissolve

                o2 "It was warm to the touch. I could feel his excitement pulsating
                    through it while I ran my hand back and forth over it."
                o2 "It made me extremely aroused and soon enough,
                    I knew I had to have it inside me."

                scene 25aoactout with dissolve

                a3 "So you--"

                o2 "Don't interrupt."
                o2 "I persuaded him onto the bed in the same position you're in
                    now."
                o2 "And then I crawled on top of him, taking another firm grasp
                    of his penis as I mounted him."

                scene 26aoactout with dissolve

                o2 "And with him between my legs, I pressed his firm penis against
                    my feminine slit and thrust my hips back and forth."

                a3 "Oh my God, that sounds so maddeningly enticing."

                o2 "It absolutely was!"
                o2 "And it wasn't long until I couldn't resist anymore."

                scene 27aoactout with dissolve

                o2 "I pressed the tip of his cock against my dripping-wet pussy and began
                    to slide it inside of me."
                o2 "Only a little at first."

                scene 28aoactout with dissolve

                o2 "His girth was considerable, you see."
                o2 "So I had to stretch to accommodate him."

                a3 "He... he's that big?"
                a3 "Did it hurt?"

                o2 "Only a little and only at first."
                o2 "We had to start by forcing his tip inside me. Like this."

                scene 29aoactout with dissolve

                a3 "Oh! It's inside me!"

                o2 "Mhmm. As was he inside of me."

                a3 "Keep going. Please keep going!"

                o2 "Well, eventually I was bored with trying to take
                    all of him inside me slowly."
                o2 "So I just let myself..."

                scene 12aoactout_vibe with vpunch

                o2 "Fall down onto him."

                a3 "Ah ah!"

                o2 "And then I lifted myself up off him..."
                o2 "And fell back down."

                scene 24aoactout_vibe with vpunch

                a3 "Yah! It's in, it's in!"
                a3 "It's so deep!"

                o2 "I lifted myself up, and fell back onto him."
                o2 "Again and again."

                show aoactout_vibe with dissolve

                a3 "Gah! Wow!"
                a3 "It feels really good!"
                a3 "Please keep talking! Tell me more!"

                o2 "I couldn't help but moan with delight after every time I slammed
                    back down onto him."
                o2 "The pressure he applied inside of me set me ablaze with excitement."
                o2 "And just as I was about to climax, he erupted inside me!"

                scene 30aoactout with vpunch

                a3 "Ahh!"
                a3 "I'm cumming!"

                o2 "Ohh? That really did it for you, didn't it?"

                scene 32aoactout with dissolve

                a3 "It's so powerful! I can't... I can't stop!"
                a3 "Ohh!"

                scene 31aoactout with dissolve

                o2 "You're having multiple orgasms?"

                a3 "Yes! Yes!"
                a3 "I'm so dizzy!"
                a3 "It's so intense!"

                scene 33aoactout with dissolve

                a3 "Ooh. It's... it's over."
                a3 "Ugn. So... tired..."

                o2 "Well that was exceptional."
                o2 "You're rather eager for [player_name]'s affection, aren't you?"

                scene 34aoactout with dissolve

                if persistent.actitout == False:
                    $ renpy.notify("You've unlocked 'Act it Out' in the Scene Gallery on the Main Menu!")
                    $ persistent.actitout = True

                o2 "Avalon?"
                o2 "Did you fall asleep again?? You've made a habit of that!"
                o2 "You bad girl."

                stop music fadeout 2.0

                $ renpy.end_replay() ## End Replay ##

                jump hangedman

            else:
            ## Dallas Sex Scene for Act Six - Mid ##
                label adactout:
                if _in_replay:
                    $ player_name = renpy.input("What would you like to name the MC?")
                    if player_name.strip() == "":
                      $ player_name = "Byron"

                scene 1adactout with fade
                play music "audio/disturbed_mind.mp3"

                a3 "So, um, I was waiting for us to get home."
                a3 "I wanted to ask about last night."
                a3 "What did you and [player_name]... you know..."
                a3 "Do?"

                scene 2adactout with dissolve

                d "Oh yeah, we need to talk about that, don't we?"
                d "Let me start by telling you about the date."
                d "Avalon, it was... it was wonderful. I've never been on a date
                    like that before."
                d "He was genuine and fun. You've got yourself a real man, girl.
                    Hell of a catch."

                scene 3adactout

                a3 "You mean {b}we've{/b} got a hell of a catch."
                a3 "Come on, Dallas. You're a part of this now."

                scene 4adactout with dissolve

                a3 "I mean, I don't know exactly how it's all going to work."
                a3 "But I know I'm eager to find out!"

                scene 5adactout

                d "Yeah? I mean, yeah."
                d "I'm still trying to wrap my head around it."

                scene 4adactout

                a3 "I wanted to know what happened {b}after{/b} the date..."

                d "Well, we came back here and--"

                scene 3adactout with dissolve

                a3 "No. I don't want you to tell me."
                a3 "I want you to show me."

                scene 6adactout

                d "Oh!"
                d "Sure, I can show you."
                d "But for that, I'll need to prepare."
                d "I'll be right back."

                scene 7adactout

                a3 "Am I supposed to wait here?"

                d "Yep. [player_name] and I didn't get very far when we got back from our date."

                a3 "Oh... OH! You two were that... eager..?"

                d "Mhmm. Be right back!"

                play sound "audio/dooropen.mp3"

                scene 8adactout with dissolve

                ai3 "{i}Okay, I have to be quick!{/i}"
                ai3 "{i}This is going to completely surprise her!{/i}"

                scene 9adactout with dissolve

                ai3 "{i}Come on, stupid button..!{/i}"
                ai3 "{i}Arg!{/i}"

                scene 10adactout with dissolve

                ai3 "{i}Goodbye, pants!{/i}"

                scene 11adactout with dissolve

                ai3 "{i}And then we dive into a cute little position here...{/i}"

                scene 12adactout with dissolve

                d "Alright, Avalon. First, we--"

                scene 13adactout with dissolve

                d "What the hell??"
                d "What are you doing?"
                d "Why are you naked already??"

                scene 14adactout

                a3 "Surprise! It's Naked Man!"
                a3 "Or.. Naked Woman. Whatever."
                a3 "It's supposed to get you laid like, seventy percent of the time."

                scene 15adactout

                d "Oh honey, you were already going to get laid. I'd never turn you down."
                d "What the hell is Naked Man?"

                scene 16adactout

                a3 "Iunno, I saw it on a television show."
                a3 "You invite someone over and when they leave the room, you strip!"
                a3 "And when they come back... Surprise naked person!"
                a3 "It's cute, right?"

                d "Yeah, it's cute."

                a3 "But it's also..."

                scene 17adactout with dissolve

                a3 "Kind of hot. Yeah?"

                scene 18adactout with dissolve

                d "Did you just flash your cootch at me!?"
                d "Damn girl, what's gotten into you?"
                d "A few days ago, you wouldn't let me touch you."
                d "Now you're spread eagle on the couch??"

                scene 17adactout

                a3 "It's hard to explain. I've just been really excitable lately."
                a3 "But come on, does it matter?"
                a3 "Show me what you guys did last night..."

                scene 19adactout

                d "Fine, but I'm going to inquire about this again later!"
                d "You don't go from a prude shut in to a saucy super-horndog
                    overnight."
                d "Bend over and I'll show you where we started."

                scene 20adactout

                a3 "W-wait, what? Bend over??"
                a3 "You guys started like that?"
                a3 "T-that's a little... advanced. Isn't it?"

                d "Scared?"

                scene 21adactout with dissolve

                a3 "I'm not scared!"
                a3 "But I don't want that thing in my butt, Dallas!"
                a3 "No 'Oopsies! It slipped'!"

                d "Don't point that freakishly big toe at me!"
                d "Bend over!"

                a3 "Alright, fine!"

                scene 22adactout with dissolve

                a3 "Like... like this?"
                a3 "On all fours?"

                d "Perfect!"

                scene 23adactout

                a3 "This seems like a vulnerable position."
                a3 "I... I can't see what you're doing back there."
                a3 "Is that the point? Suspense? Anticipation?"

                scene 24adactout

                a3 "Do you start off gentle with a little teasing--?"

                scene 25adactout with vpunch

                play sound "audio/faceslap.mp3"

                a3 "Ow!"
                a3 "My ass!"

                scene 26adactout with dissolve

                a3 "What the hell, Dallas!?"
                a3 "I thought we were supposed to be having fun?"
                a3 "Now you're beating me??"
                a3 "What did I do to deserve that??"

                d "It's supposed to be arousing!"

                scene 27adactout with dissolve

                d "You know, S and M? Pain for pleasure?"

                a3 "What?!"
                a3 "Isn't pain the opposite of pleasure?"

                d "They can go hand in hand!"

                a3 "Don't hit me, Dallas!"
                a3 "I don't like that."

                d "Okay, okay! You're the one that said you wanted me to show you what [player_name]
                    and I did..."

                scene 28adactout

                d "How about this?"

                a3 "Oh! I can feel it!"
                a3 "Go slow, go--!"

                scene 29adactout with vpunch

                a3 "Gah!"
                a3 "Too fast, too fast!"

                d "Mehp. My bad."
                d "In my defense, it sort of just slid right in."

                scene 28adactout with dissolve

                d "Let's try this again."

                a3 "You and [player_name] really went this far after one date?"

                d "Um, yeah."
                d "It was phenomenal. We gotta get you some real dick, Ava."

                a3 "Let's um, focus on the task at hand first."
                a3 "And we can talk about that la--"

                show adactout_doggy with dissolve

                a3 "Whoa whoa!"
                a3 "Ah!"

                d "You are soaked, girlfriend!"
                d "You're squeezing so tight, you're pushing it back out!"

                a3 "Keep going, keep going!"
                a3 "Ohh!"

                d "[player_name] was like, twice the thickness of this little thing."
                d "I'm not sure he would even fit in this tight hole."

                a3 "Mmhhaa."
                a3 "Tell me more!"

                d "When he was fucking me from behind, I thought he was going to
                    tear me in half!"
                d "And since I was bent over like you are now, he was able to go
                    deep!"
                d "Like, super deep!"
                d "I was screaming with both pleasure and pain."

                a3 "Oooh!"
                a3 "He's-- Gah! He's really that big?"

                d "Yep! After I couldn't take it anymore, I collapsed on the couch."
                d "But he wasn't done with me yet!"

                a3 "W-what? What did he do next??"

                d "He picked me up and fucked me while holding me in the air!"
                d "And at the very moment I couldn't possible handle anymore,
                    he exploded inside of me!"

                scene 30adactout with dissolve

                a3 "Gah! Okay, enough!"
                a3 "I'm cumming!"
                a3 "My vagina is quivering! It's like it won't stop!"

                d "Oh, this is a good one, huh??"

                a3 "It's still... going... Ugn!"

                d "Multiple orgasms!?"
                d "I'm jealous."

                scene 31adactout

                a3 "Oooh. It's... it's calming down."
                a3 "Thinking about [player_name]... that really set me over
                    the edge. That was wonderful."

                d "If thinking about him makes you that excited, you should let
                    him fuck you. Duh."

                a3 "I'm trying! I am..."

                scene 32adactout with dissolve

                a3 "Mm. Thank you, Dallas."

                scene 33adactout with dissolve

                d "You're welcome."
                d "Don't pass out! It's my turn!"

                scene 34adactout with dissolve

                if persistent.nakedman == False:
                    $ renpy.notify("You've unlocked 'Naked Man' in the Scene Gallery on the Main Menu!")
                    $ persistent.nakedman = True

                d "Goddammit."
                d "When am I going to learn?"
                d "I have to let her get me off first and {b}then{/b} I get her off."
                d "Shit."

                stop music fadeout 2.0

                $ renpy.end_replay() ## End Replay ##

                jump hangedman

        label avasolosix:
        if _in_replay:
            $ player_name = renpy.input("What would you like to name the MC?")
            if player_name.strip() == "":
              $ player_name = "Byron"

        scene 1avasolosix_vibe with fadefast

        play music "audio/temporary_solution.mp3"

        ai3 "{i}I can't explain it but I feel an overwhelming need for release
            today.{/i}"
        ai3 "{i}I haven't had much time to myself lately.{/i}"
        ai3 "{i}I think... maybe I can take care of myself real quick?{/i}"

        scene 2avasolosix_vibe with dissolve

        ai3 "{i}I can't take too long.{/i}"
        ai3 "{i}Lunch will be ready soon.{/i}"

        scene 3avasolosix_vibe with dissolve

        ai3 "{i}Oof. This shirt was a terrible idea today.{/i}"
        ai3 "{i}Without a bra on, I can feel every gust of wind on my breasts.{/i}"
        ai3 "{i}And the fabric of that shirt keeps rubbing against my nipples.{/i}"
        ai3 "{i}They're so sensitive lately.{/i}"

        scene 4avasolosix_vibe with dissolve

        ai3 "{i}Let's get these off.{/i}"
        ai3 "{i}Erm, come on. Stupid button.{/i}"

        play sound "audio/zipper.mp3"

        scene 5avasolosix_vibe with dissolve

        ai3 "{i}And then we have our new friend here.{/i}"
        ai3 "{i}I haven't had a chance to test it out yet.{/i}"
        ai3 "{i}Not by myself.{/i}"

        scene 6avasolosix_vibe with dissolve

        ai3 "{i}It's so long!{/i}"
        ai3 "{i}How could this possibly fit inside someone??{/i}"
        ai3 "{i}Well, we don't have to go crazy with this today.{/i}"
        ai3 "{i}Just a little experiment.{/i}"

        scene 8avasolosix_vibe with fadefast

        ai3 "{i}Mm, that feels amazing.{/i}"
        ai3 "{i}Is it weird that I hate getting into the shower, but when I'm in the
            shower, I hate getting out?{/i}"
        ai3 "{i}I mean, what's that about?{/i}"

        scene 7avasolosix_vibe with dissolve

        ai3 "{i}No! I can't get distracted!{/i}"
        ai3 "{i}I need to masturbate so I can think clearly again.{/i}"
        ai3 "{i}A little self-appreciation here will go a long way.{/i}"
        ai3 "{i}Let's see if we can get into a comfortable position in.{/i}"

        scene 9avasolosix_vibe with fadefast

        "*Bzzz*"

        ai3 "{i}Ahh, yes. That's how you turn it on.{/i}"
        ai3 "{i}I don't want too much power. Just a light vibration for our first time.{/i}"
        ai3 "{i}Alright, my little friend. Be good to me today!{/i}"

        scene 10avasolosix_vibe with dissolve

        ai3 "{i}Prepare yourself, Vagina!{/i}"
        ai3 "{i}Because we've got incoming!{/i}"
        ai3 "{i}This is going to be epic.{/i}"

        scene 11avasolosix_vibe with vpunch

        ai3 "{i}Dah!{/i}"
        ai3 "{i}Oh wow, that feels amazing!{/i}"
        ai3 "{i}It's like a flood of pleasure. Uhgn!{/i}"

        show good_vibrations with dissolve

        ai3 "{i}Mm, yes!{/i}"
        ai3 "{i}I'm in love with this thing!{/i}"
        ai3 "{i}I can't believe my Uncle got this for me.{/i}"
        ai3 "{i}It's awesome!{/i}"
        ai3 "{i}I can just imagine him pressing {b}himself{/b} against my vagina.{/i}"
        ai3 "{i}Rubbing the tip of his penis up and down my soaking wet lips...{/i}"
        ai3 "{i}Before finally piercing into me!{/i}"

        play sound "audio/doorknock.mp3"
        "*Knock* *Knock*"

        scene 12avasolosix_vibe with vpunch

        a3 "Ah!"

        if octavia == True:

            scene 14avasolosix_vibe with dissolve

            o2 "Avalon?"
            o2 "You've been in there a while and lunch is ready."
            o2 "Are you alright?"

            scene 13avasolosix_vibe with dissolve

            if persistent.goodvibrations == False:
                $ renpy.notify("You've unlocked 'Good Vibrations' in the Scene Gallery on the Main Menu!")
                $ persistent.goodvibrations = True

            a3 "Y-yes! I'm fine!"
            a3 "I'm just finishing up!"
            a3 "I'll be right out!"

            scene 14avasolosix_vibe with dissolve

            o2 "I made sandwiches."
            o2 "They're getting soggy so don't be long."

            ai3 "Ugh. How embarrassing..."

            stop music fadeout 2.0

            $ renpy.end_replay() ## End Replay ##
            jump hangedman

        else:

            scene 14avasolosix_vibe with dissolve

            d "Hey, girlfriend!"
            d "Lunch is ready so pull that vibrator out of your butt and come eat."

            scene 13avasolosix_vibe with dissolve

            a3 "I'm just taking a shower!"
            a3 "I'm not masturbating!"

            scene 14avasolosix_vibe with dissolve

            if persistent.goodvibrations == False:
                $ renpy.notify("You've unlocked 'Good Vibrations' in the Scene Gallery on the Main Menu!")
                $ persistent.goodvibrations = True

            d "I can hear the vibrator, Avalon."
            d "Stop messing around, you can play with yourself later."
            d "I made hotdogs!"

            ai3 "Ugh! I'm so embarrassed!"
            ai3 "Kill me."

            stop music fadeout 2.0

            $ renpy.end_replay() ## End Replay ##
            jump hangedman

        label hangedman:

        ## Byron goes to see his biological father at his office. ##

        scene 1hangedman with fade

        bi "{i}On the car ride to the therapist, Avalon told me about Penny's encounter
            with my father.{/i}"
        bi "{i}It sounds like she's well on her way to putting him away for the rest of
            his life.{/i}"
        bi "{i}This might be my last chance to ask him if he had anything to do with Leah's
            disappearance.{/i}"
        bi "{i}He must know where she is. He must!{/i}"

        play sound "audio/elevatordoor.mp3"

        scene 2hangedman with dissolve

        bi "{i}He told me if I ever showed up on his doorstep again, there would
            be consequences...{/i}"
        bi "{i}I hope I don't regret this.{/i}"
        bi "{i}Here goes nothing.{/i}"

        scene 3hangedman with fadefast

        pause

        play sound "audio/dooropen.mp3"

        scene 4hangedman with dissolve

        p "Who--"
        p "[player_name]?!"

        scene 5hangedman with dissolve

        b "Penny?"
        b "What are you doing here?"

        scene 6hangedman with dissolve

        p "I could ask you the same thing."
        p "You know you shouldn't be here. It's dangerous."
        p "Or... it was..."

        scene 7hangedman

        b "Was? What does that mean?"
        b "I came to ask my father a question."

        scene 8hangedman with dissolve

        b "Where is--"

        scene 9hangedman with vpunch

        b "{b}Ah!{/b}"

        play music "audio/flight_path.mp3"

        scene 10hangedman

        b "Is that... Is that my father?"
        b "Why is he..? But he wouldn't..."
        b "How did this happen?"

        p "Look away, [player_name]."

        scene 11hangedman with dissolve

        b "I think I'm going to be sick."
        b "What happened?"
        b "Why are you here, Penny?"

        p "I planted a camera in his office when I was here yesterday."

        scene 12hangedman with dissolve

        p "When it became obvious what he was about to do, I rushed over here to stop him."
        p "I was too late."

        b "But... but he wouldn't do this..."

        scene 13hangedman

        p "Those are the same words that have been repeating in my head."
        p "He'd lost his fortune and his power over the last few years."
        p "And I was about to dig up the last few pieces of evidence I needed
            to have him incarcerated for the rest of his life."
        p "The only thing he had left was the possibility that stupid spear was
            authentic."

        scene 14hangedman with dissolve

        p "And I convinced him it was a fake as a prank."
        p "He did this because of me."
        p "I've never inspired someone to take their own life before, [player_name]."
        p "It feels awful! I mean, {b}really{/b} awful!"

        scene 15hangedman with dissolve

        p "I'm... I'm a horrible person..."

        b "No. No, you're not, Penny."

        p "How could I let this happen?"

        scene 16hangedman with dissolve

        p "No! Get away from me!"
        p "I don't want to be consoled!"
        p "I don't want--"

        scene 17hangedman with vpunch

        p "Oof. Goddammit, [player_name]..."

        b "{b}He{/b} was a horrible person, not you."
        b "You stopped two people that harmed or threatened to harm people I love."
        b "You're my hero, Penny."

        p "Heroes don't kill people."

        scene 18hangedman with dissolve

        b "Some do..."

        p "I don't want to be that kind of hero."
        p "I just want to help people."

        b "You've helped me tremendously. And I'm so grateful."

        scene 19hangedman with dissolve

        p "Thank you, [player_name]."

        stop music fadeout 2.0

        bi "{i}We held each other in silence for several minutes.{/i}"
        bi "{i}It was clear to me at that moment that nobody is immune to trauma.{/i}"
        bi "{i}Penny must have called the police before I arrived.{/i}"
        bi "{i}They showed up several minutes later.{/i}"

        scene 20hangedman with fade

        ## Penny and Byron are being detained while police investigate
        ## Gladstone's death.

        play music "audio/sneaking_up_on_you.mp3"

        b "So why are we here, Penny?"
        b "We didn't do anything wrong, did we?"
        b "Are we in trouble?"

        p "No, they need to investigate the scene to make sure we didn't have
            anything to do with your father's demise."
        p "Once they're satisfied that we were not involved, they'll send someone
            in to release us."
        scene 26hangedman with dissolve

        b "It sounds like you've been in this situation before."
        b "Private Detectives like yourself usually just gather evidence, right?"
        b "Why would you be here often?"

        scene 23hangedman

        p "I wouldn't say I'm here often. You make it sound like I make a habit
            out of leaving a mess."
        p "I am arguably more hands-on than most other gumshoes. That would be
            a fair statement."

        b "Like Manbat?"

        scene 25hangedman with dissolve

        p "Don't compare me to him!"
        p "He's a humorless drama queen! And his moral compass is questionable
            at best."
        p "He claims he doesn't kill people but then he leaves someone with several
            ruptured organs and multiple broken bones."
        p "You think people don't die from those injuries? They do!"

        b "I like Manbat."

        p "You're dead to me."

        scene 26hangedman

        b "So you're alright with killing people?"
        b "You seemed genuinely upset about what happened to my father."

        scene 21hangedman

        p "I bend the rules. Heck, I break the rules! I don't recognize anyone's
            authority. I do what I believe is best for society and the individuals
            within it."
        p "But there are consequences to being contumacious. If everyone was
         anti-authority like I am, we would have chaos and anarchy."

        b "You condemn a lifestyle you yourself lead?"

        p "In a way, yes. Imagine if someone could wipe out the entire
            world's population of mosquitos."
        p "That would eradicate their spread of diseases."

        scene 27hangedman

        b "I've heard that mosquitos don't have any benefit to nature or humanity."
        b "This would be a good thing, wouldn't it?"
        b "If you had this capability, you'd have a moral obligation to go through with
        it."

        scene 23hangedman

        p "You've been surfing the world wide web, haven't you?"
        p "As far as I know, that's correct. And I'm sure someone in that position
            would feel exactly that; a moral obligation to our society!"

        scene 24hangedman with dissolve

        p "But what if an unforeseen consequence was that their solution also,
            inadvertently, destroyed the world's population of bees too!"
        p "Sharing this idea with their peers before executing the plan could
        have revealed this oversight and prevented a catastrophe."

        scene 28hangedman

        b "You're not making a very good argument in your favor, Penny."
        b "You're say you are anti-authority and then arguing in favor of authority."
        b "Rules in society are decided upon by the majority to keep the system
            afloat."

        scene 23hangedman

        p "Yep! A society cannot flourish if it cannot maintain order."
        p "People who break the rules, as I do, should absolutely be stopped!"

        scene 24hangedman with dissolve

        p "I'm convinced that what I'm doing is in the best interest of society."
        p "I have the skills and ability to stop the mosquitos and I feel a sense of
            moral obligation to do so."
        p "And it just so happens that no one has been able to stop me. Yet."

        b "But... what if you kill the bees too?"

        scene 21hangedman with dissolve

        p "That's why I try not to kill people, [player_name]. It's the line that I don't cross."
        p "If I kill someone, I'm a murderer. Society takes that very seriously. And
            if I continue killing, I'm a serial killer."
        p "At that point, society will send their best after me. I'll have special
            agents assigned to hunt me down."
        p "And multiple branches of the judicial system will be coming for me."
        p "Right now, I'm just a nuisance but I'm mostly helpful. So they don't
            really want to stop me."

        scene 26hangedman

        b "So you limit how far you're willing to go to kill the mosquitos so
            you don't anger the bees."

        p "It's more than that but for simplicities sake, yes."

        b "I understand. Is that why you were upset about my father's death?"

        scene 21hangedman with dissolve

        p "No. I'm not upset that he's dead. I'm upset that he killed himself
            because of something I did. Or at least what I did played a part."
        p "I get bored easily, [player_name]. And these criminals, they're notoriously
            stupid. Even Gladstone wasn't as clever as he liked to imagine he was."
        p "He knew how to avoid getting in trouble with the police by playing the system."
        p "Being outside the system myself and not abiding by the rules allows me to take down
            even would-be criminal masterminds with relative ease."

        scene 27hangedman

        b "You're saying it's easy to dismantle entire criminal enterprises?"
        b "That doesn't sound easy. Are you sure you're not like, a super person?"

        scene 23hangedman

        p "Well, sure! I spent my childhood surviving in a hostile environment and
            then my teenage years studying and learning."
        p "And when I came to America, I had extensive military training from
            a friend."
        p "But that's neither here nor there."

        scene 21hangedman with dissolve

        p "My point is that... I like to play with my food before I eat it! It
            keeps me entertained and stimulated so I can enjoy my work."
        p "The prank I pulled on Gladstone was supposed to be... just a prank."

        scene 20hangedman with dissolve

        p "I... I inspired someone to take their own life, [player_name]."
        p "I didn't even know I was capable of that."

        b "I'm sorry you feel that way, Penny. I am."
        b "But I'm glad he's dead."

        scene 24hangedman

        p "He was a threat to you and yours. And now he's not."
        p "I wish things had gone differently but I'm happy you're safe now. From him."
        p "On that note, now that he's gone it's time to tell Avalon the truth."

        scene 29hangedman

        b "I know. And I will."
        b "She's not going to take it well."

        p "She'll understand."

        b "I hope you're right."

        scene 21hangedman

        p "You never said why you went to see him. What question did you need to ask your father?"
        p "It must have been important to risk so much."

        scene 20hangedman with dissolve

        b "I wanted to ask him about Leah. She disappeared several months ago.
            I thought he might know what happened to her."
        b "Or maybe he was the reason she was missing."

        p "Your [persistent.leah_rel]? I'll look into it for you."

        b "For another five grand??"

        p "No, [player_name]. I'll do it because you're a friend."

        scene 21hangedman with dissolve

        p "Some of the things you said earlier, they meant a lot to me."
        p "I appreciate it more than you know."

        b "Oh. Well, you're welcome."

        stop music fadeout 2.0

        play sound "audio/dooropen.mp3"

        scene 30hangedman with dissolve

        p "Oh look, they sent the rookie to talk to us."

        b "Evans?"

        play sound "audio/doorclose.mp3"

        scene 31hangedman with dissolve

        det "It's nice to see you too, Penny."
        det "Although I would have preferred under different circumstances."

        scene 32hangedman with dissolve

        det "And [player_name], I'm surprised you're here."
        det "But let me put your mind at ease before we continue. You're not in any
            trouble."

        scene 33hangedman

        b "That's a relief. I'm too pretty to go to prison."
        b "They'd eat me alive!"

        p "Are we free to go, Detective Hotshot? Or was there something else?"

        det "You're free to go. But before you do, I need to talk to you about
            something."

        scene 36hangedman

        det "You can't do this anymore, Penny. It's... it's over."
        det "You've broken too many rules too many times."
        det "Whoever was protecting you from on high, they can't anymore. You've
            gone too far this time."
        det "You're done."

        scene 34hangedman

        p "What the hell, Evans!?"
        p "Too far? I stopped a criminal that law enforcement couldn't for over
            forty years!"
        p "You can't stop me, you need me!"

        scene 37hangedman

        det "You think we're all just a bunch of clowns with guns, Penny!?"
        det "I guess we should all just turn in our stars and let you take over
             the precinct. Because you've got it all figured out, right?!"
        det "You are not the judge, jury, and executioner, Penny. You're a rogue!
            A vigilante!"

        scene 40hangedman

        b "P-penny? Are you alright?"

        scene 41hangedman

        p "Let's get one thing straight, Evans; You don't get to talk to me
            like that!"
        p "You and your stupid judicial system don't want Penny's help? Fine!
            Consider her retired!"
        p "One day, a little girl is going to be tugging at your pant leg asking
            why her mother isn't around anymore."
        p "You tell her the truth, Evans. You tell her that your incompetent system
            couldn't save her mom from a murderous psychopath!"
        p "And you live with that!"

        scene 42hangedman

        play sound "audio/doorclose.mp3"

        b "Was all that really necessary, Evans? That was harsh."
        b "I know she doesn't play by the rules but she's helped a lot of people."
        b "Namely... me."

        scene 43hangedman

        det "Penny is out of control, [player_name]."
        det "I've got an entire file drawer full of illegal acts she's performed.
            Breaking and entering, theft, destruction of property, public intoxication."

        b "Public intoxication?"

        det "She wasn't even drunk, [player_name]. She put on a show so she could steal someone's
            wallet!"
        det "She's arguably the biggest criminal in the city! She's got more infractions
            against her than the next top three criminals on my list combined!"

        scene 42hangedman

        b "How big is the folder containing all the people she's helped?"

        scene 43hangedman

        det "It's bigger, [player_name]."
        det "That's why I threw in with her. But I can't anymore."
        det "The state isn't going to condone this any longer. In fact, it never did."
        det "The harsh reality is that the person protecting her is gone. And the replacement
            isn't going to put up with Penny."

        scene 44hangedman with dissolve

        b "I understand, Detective. She's right about what she said though."
        b "You couldn't stop my father. But she could.
            Sometimes the long arm of the law isn't long enough."

        scene 45hangedman with dissolve

        det "Don't let her take you down with her, [player_name]."

        b "You paid a heavy price today for your loyalty to the system, Detective."
        b "The cost was a Penny. And that's a price I'm not willing to pay."

        jump talk_in_private

        ## Byron heads home to tell Avalon about the secrets he's been
        ## keeping from her.

        label talk_in_private:

        if octavia == True:
            scene 5secrets with fade

            a3 "Octavia, I have a question."

            o2 "Ask away!"

            a3 "If you could change anything from your past, what would it be?"
            a3 "It can be anything!"

            scene 2secrets with dissolve

            o2 "Hmm. That's a good question, Avalon."
            o2 "If I could go back, I would have met you and [player_name] sooner."
            o2 "That way I could have had even more time with you and him."

            scene 5secrets with dissolve

            a3 "Aw. That's nice, Octavia."
            a3 "We should have some wine with all that cheeeese."

            scene 2secrets with dissolve

            o2 "Silly girl."

            play sound "audio/dooropen.mp3"

            scene 7secrets with dissolve

            o2 "[player_name]! There you are."

            a3 "Finally! Where'd you go?"

            scene 9secrets

            b "Hey, girls."
            b "You two look comfortable."

            scene 11secrets with dissolve

            b "I uh, don't mean to interrupt but can I talk with you in private for
                a moment, Avalon?"
            b "It shouldn't take long."

            a3 "Okay!"

            scene 5secrets

            a3 "I'll be right back and then I'll tell you what I'd change!"

            scene 2secrets with dissolve

            o2 "Alright, Sweetie. I'll be here."

            jump secrets

        else:

            scene 1secrets with fade

            a3 "I already told you, Dallas. You can't 'uncut' hair."

            scene 4secrets with dissolve

            d "My research is inconclusive."

            scene 3secrets with dissolve

            a3 "No, it's not."
            a3 "'Uncutting' hair is preposterous and doesn't make any sense."
            a3 "That concludes the research. The end!"

            scene 4secrets with dissolve

            d "I remain unconvinced. There must be something we've missed."
            d "Perhaps the archives are incomplete."

            play sound "audio/dooropen.mp3"

            scene 6secrets with dissolve

            a3 "Uncle! Jeez, where have you been?"
            a3 "It's been like, three hours!"

            d "Everything alright, buddy?"

            scene 9secrets

            b "Hey, girls. Sorry about earlier."
            b "But it was important."

            scene 11secrets with dissolve

            b "Avalon, can I talk to you in private for a moment?"
            b "It'll only take a few minutes."

            scene 8secrets

            a3 "Um, alright. Sure."

            d "Er, I guess I'll just be here then."

            jump secrets

        ## Byron tells Avalon his secrets in her room.

        label secrets:

        scene 6absecrets with fadefast

        a3 "You know, I'm kind of mad at you for just leaving earlier."
        a3 "I wanted to talk to you about your session!"
        a3 "But I forgive you. Where'd you go? Why did you want to talk in private?"

        scene 3absecrets

        b "Slow down, Avalon. I'm going to tell you everything. I promise."
        b "You're jubilant today. I'm glad you're having a good day."

        scene 2absecrets with dissolve

        b "I was keeping some secrets from you, Avalon. I had reasons for doing so
            but now those reasons are gone."

        scene 7absecrets

        a3 "Is this about what you and Penny spoke about the other night?"
        a3 "I thought you couldn't tell me because it wasn't safe?"
        a3 "Did something change?"

        scene 2absecrets

        b "Yes, something changed. But first, I wanted to tell you..."
        b "Avalon, I have a [persistent.leah_rel]. I didn't find out about her until a year ago."
        b "After you and I disconnected, I started spending time with her."
        b "We spent about six months getting to know each other. And we... grew close."

        scene 8absecrets

        a3 "Penny told me about Leah. I didn't know you spent so much time with her
            though."
        a3 "But why didn't you ever introduce me to her? Where is she now?"
        a3 "I don't understand. Why--"

        scene 1absecrets

        b "She's gone, Avalon."
        b "One day, we were spending time together and she... she kissed me."
        b "She wanted more from me. She wanted a relationship. I panicked and ran."

        scene 7absecrets

        a3 "O-oh. You panicked because she's your [persistent.leah_rel]? Was that why you rejected
            her?"
        a3 "I'm your niece, sort of. Being with Leah wouldn't have been
            much different, would it have been?"
        a3 "Wait, did you have reservations about us?!"

        scene 3absecrets

        b "N-no! I mean, I do wish we would have taken things slower but I
            didn't want to say 'No' to you."
        b "I didn't want to make the same mistake with you that I made with Leah."
        b "And despite my reservations at first, I'm happy with you! Really happy!"

        scene 6absecrets

        a3 "Okay, well, I wish you would have told me. We could have, like, gone
            on dates and stuff first. I don't know."
        a3 "But whatever! I wanna meet her. We should find her!"

        scene 4absecrets

        b "No, Avalon. I--"
        b "I searched for her. She's gone. She didn't just move, she disappeared."
        b "I think... I think she's dead."

        scene 8absecrets

        a3 "Oh. But you're not sure? We should find out for sure, Uncle."
        a3 "Maybe... maybe Penny can help?"

        scene 1absecrets

        b "I asked her. She's going to look into it for me. As a favor."
        b "But I talked to Dr. Yu about Leah and it brought it all to the surface."
        b "After my session with him, I went to visit my father. I thought he might
            know where Leah was."

        scene 7absecrets

        a3 "What?? Why wouldn't you just ask Penny?"
        a3 "I thought your father was dangerous."
        a3 "We could have just paid Penny again. For that, it's worth the money."

        scene 2absecrets

        b "He's dead, Avalon."

        a3 "W-what?"

        b "He hanged himself in his office. I found him when I went there for answers."
        b "Penny was there, she found him first."

        a3 "Oh my God. Is she alright? Are you??"

        scene 1absecrets with dissolve

        b "It was a shock but we're both alright."
        b "But his death eliminates any threat he posed to us."
        b "That means I don't have any obligation to keep the secrets he told me."
        b "This might change things for us so before I tell you, I want to let you know
            that you have more money than I implied."

        scene 8absecrets

        a3 "What? Why would that matter?"
        a3 "We're a team, aren't we? Why wouldn't you just keep it and we'll,
            you know, build a life together with it."
        a3 "Why do we need to separate it?"
        a3 "How much did you give me?"

        b "Half a million dollars."

        scene 7absecrets with dissolve

        a3 "W-whoa. That's... that's a lot of money, Uncle."
        a3 "What would I even do with that?"

        scene 2absecrets

        b "It's enough that you can build a life for yourself."
        b "With or without me. It's yours, no matter what happens."

        scene 6absecrets

        a3 "No, I want to be with you. I want to build a life with you."
        a3 "Nothing is going to change that."

        b "You don't know that."

        a3 "I.. I do! I love you."

        scene 4absecrets

        b "Your father didn't kill himself, Avalon. He didn't overdose."
        b "At least, not by his own hands. Gladstone hired someone to do it."
        b "My father killed yours."

        scene 7absecrets

        a3 "What? No. That's... that's not possible."
        a3 "Why would he even do that? That doesn't make sense."
        a3 "You... you're wrong."

        scene 1absecrets

        b "I'm not. I told Johnny I wanted to know who my real father was."
        b "So Johnny searched for him. And he found him."
        b "When I visited my father for the first time, many years later, he let
            slip that Johnny stumbled upon something when he visited him."
        b "Something he wasn't supposed to see. And my father killed him because of it."
        b "He gave me a lot of money to stay quiet about it. And he said if I told anyone,
            he'd kill them."
        b "I guess he didn't just kill me because I'm his son."

        scene 9absecrets

        a3 "No."
        a3 "No, no. That can't be. It just... it can't."
        a3 "You got that money years ago. That means you've known for years??"
        a3 "I thought my father abandoned me for drugs."
        a3 "I've been so angry at him my whole life..."

        scene 4absecrets

        b "I'm so sorry, Avalon. I didn't know what else to do."
        b "Your safety was paramount. I couldn't tell you! I--"

        scene 10absecrets

        a3 "That's why you left me?"
        a3 "That's why you spent so many years away from me?"
        a3 "You couldn't look at me knowing you couldn't tell me about my father?"

        b "I'm sor--"

        a3 "You should have told me!"
        a3 "I don't care about my safety, you should have told me!"

        scene 11absecrets

        b "Avalon, wait."

        a3 "No! Leave me alone!"

        b "Let me just--"

        play sound "audio/dooropen.mp3"

        if octavia == True:
            scene 13secrets

            a3 "I want to leave, Octavia."
            a3 "I want to leave right now!"

            scene 14secrets with dissolve

            a3 "Please, Octavia. Please take me away from here!"
            a3 "I can't stay!"

            scene 16secrets

            o2 "Slow down, Avalon."
            o2 "What's wrong? What happened?"

            scene 17secrets

            a3 "He's a liar!"

            b "Avalon, please!"
            b "Can we just talk about this?"

            scene 18secrets with dissolve

            b "I'm sorry, I just did what I thought--"

            scene 19secrets with vpunch

            a3 "{b}Don't touch me!{/b}"

            scene 21secrets

            b "P-please."
            b "Please don't do this, Avalon."
            b "I love you."

            scene 20secrets

            a3 "I didn't mean--"
            a3 "I can't. I can't be here!"
            a3 "I have to leave!"

            scene 22secrets

            b "Avalon!"

            scene 23secrets with dissolve

            o2 "I don't know what's going on but she clearly needs time, [player_name]."
            o2 "Give her a chance to cool down. I'll talk to her."

            scene 24secrets

            b "I can't lose her, Octavia. I can't."
            b "She's everything to me."

            scene 23secrets

            o2 "Let me take care of her and then I'll call you tonight."
            o2 "We'll get it figured out."
            o2 "Don't lose hope."

            scene 25secrets

            bi "{i}I knew this would happen.{/i}"
            bi "{i}I knew she would hate me for this.{/i}"
            bi "{i}But what choice did I have?{/i}"

            jump lost_it_all

        else:

            scene 14secrets with fadefast

            a3 "I want to leave, Dallas! I want to leave right now!"
            a3 "Please take me away from here!"

            scene 10secrets

            d "Whoa, what's going on?"
            d "What happened? What's wrong?"

            scene 17secrets

            a3 "He's a liar, Dallas!"

            b "Please, Avalon!"
            b "Can we just talk about this?"

            scene 18secrets with dissolve

            b "I just did what I thought was right."
            b "I didn't mean--"

            scene 19secrets with vpunch

            a3 "{b}Don't touch me!{/b}"

            scene 21secrets

            b "Avalon, I... I'm sorry."
            b "But don't do this. Please don't do this."
            b "I only did what I thought was right."

            scene 20secrets

            a3 "I'm sorry. I can't."
            a3 "I... I have to go!"

            scene 22secrets with dissolve

            b "Avalon, wait!"

            scene 12secrets with dissolve

            d "She needs to cool off, [player_name]. Give her some time."
            d "I'll take her back to my place and I'll call you later."

            scene 15secrets

            b "I can't lose her, Dallas. I can't."
            b "She's everything to me."

            scene 12secrets

            d "I know. It's okay."
            d "Just give me a few hours, alright?"
            d "I'll call you."

            scene 25secrets

            bi "{i}I knew this would happen.{/i}"
            bi "{i}I knew she would hate me for this.{/i}"
            bi "{i}But what choice did I have?{/i}"

            jump lost_it_all

        label lost_it_all:

        scene 1lostitall with fadefast

        p "[player_name]? Are you here?"
        p "Avalon texted me about ten minutes ago."

        scene 2lostitall with dissolve

        p "She said you might not be doing so well."
        p "Are you--"

        scene 3lostitall with dissolve

        p "[player_name]? What's wrong?"
        p "Did something happen?"

        play music "audio/heartbeat_of_the_hood.mp3"

        scene 4lostitall

        b "I've got nothing left. It's all gone."
        b "Everything I loved is gone!"
        b "My parents abandoned me. My father killed my best friend."
        b "My foster parents are dead."

        scene 5lostitall with dissolve

        b "Leah disappeared. She was my only [persistent.leah_rel] and she's gone! And now..."
        b "And now Avalon hates me! She... she left me!"
        b "I can't... I can't go on anymore. It's too hard!"

        scene 6lostitall with dissolve

        b "What are you doing? No, get off!"
        b "I don't want your help!"
        b "I deserve this! I deserve to be abandoned!"

        p "No, you don't."

        scene 7lostitall with dissolve

        b "I lied to her, Penny. She won't forgive me for this."

        p "She will."

        b "I lost it all. I lost everything."

        p "You didn't."

        scene 8lostitall with dissolve

        p "Just focus on me right now. Catch your breath."
        p "Be here with me. Don't think about anything else."

        b "She's not coming back, Penny. She's--"

        scene 9lostitall with dissolve

        p "Shh. I've been where you are now."
        p "You have to let the despair pass, [player_name].
            It will, I promise. And I'll be here with you until it does."
        p "You're not alone. I'm here with you."

        scene 10lostitall with dissolve

        bi "{i}My mind was drawn back to a few days ago when I first
            met Penny. I saw her so differently then.{/i}"
        bi "{i}Today I feel like I got to see a different side of her.{/i}"
        bi "{i}She was right, the gloom slowly lifted and I didn't feel like
            things were hopeless after a while.{/i}"
        bi "{i}I wanted to believe Avalon would forgive me. But I wouldn't blame
            her if she didn't.{/i}"
        bi "{i}Only time would tell. So that's what I did, I gave it time...{/i}"

        if octavia == True:

            play music "audio/tomorrows_rain.mp3"

            scene 2aovent with fade

            a3 "I spent my whole life angry at my father for something he didn't even do!"
            a3 "How could he not tell me? How could he keep that a secret from me?"
            a3 "And he didn't tell me about Leah either."
            a3 "We're supposed to be together but we're not!"
            a3 "People in a relationship are supposed to communicate but he keeps so
            	much from me..."

            o2 "Oh sweetie. Things are just not that black and white."
            o2 "[player_name] has been alone for so long. And your relationship with him
            	is so new."
            o2 "He's going to make mistakes and so will you. You'll learn and grow together."

            scene 3aovent with dissolve

            o2 "Someone has come to visit you, Avalon."
            a3 "I don't want a visitor."

            o2 "I think you won't mind this one."
            o2 "Say 'Hello', Maize."

            scene 4aovent with dissolve

            a3 "Oof. M-Maize? Where were you hiding?"
            o2 "It takes a lot to coax her downstairs sometimes.
                But she gets especially affectionate when I'm sad."
            a3 "She does? She must make for an especially compassionate companion then,
                huh?"
            o2 "She has a strong maternal instinct, I think it's common with female felines."

            scene 6aovent with dissolve

            a3 "Alright, this visitor is okay. I don't mind Maize. But I don't want to
                see anyone else!"
            a3 "It's nice to see you too, Maize. Thank you for being here for me today."

            o2 "Avalon, did [player_name] tell you why he kept the truth about your father from you?"

            a3 "He did. He said his father threatened to hurt anyone that he told."

            scene 7aovent with dissolve

            o2 "That sounds like a good reason to keep it from you."

            a3 "He could have told me. His father never would have known!"

            o2 "I don't think [player_name] was willing to take that risk."

            a3 "And he took money from him."

            o2 "What did he do with that money?"

            a3 "Well, he gave a lot of it to me..."
            a3 "I know he's trying, Octavia. He's just doing what he thought was best for me.
                I'm just--"

            o2 "Shocked."

            a3 "I need time to think about all this. It's a lot to take in. I understand
                why he did what he did, but..."

            o2 "Take as much as you need to think. And I'll be right here if you
                want to talk more."

            stop music fadeout 2.0

            jump breaking_in

        else:

            play music "audio/disturbed_mind.mp3"


            scene 1advent with fade

            a3 "I just don't know what to do, Dallas."
            a3 "[player_name] knew that my father didn't kill himself."
            a3 "He knew for years and didn't tell me!"

            d "Why wouldn't he tell you that?"

            a3 "Because his father said he'd hurt anyone he told."

            d "His father? Why would he--"

            scene 3advent with dissolve

            a3 "Because [player_name]'s father killed mine."

            scene 4advent with dissolve

            d "Whoa. That's heavy."
            d "Damn. [player_name]'s dad was fuckin' scum, huh?"
            d "But... [player_name] was trying to protect you?"

            scene 3advent with dissolve
            d "That's why he didn't tell you about your dad, right?"

            a3 "I don't care! He should have told me!"
            a3 "He should have told me anyway..."

            scene 2advent with dissolve

            d "That's a shitty position for him to be in."
            d "I don't envy that at all."
            d "I understand where you're coming from but... woof."
            d "I wouldn't know what to do either if I were him."

            a3 "I know. I know that!"
            a3 "I just... I need time. I need to think..."

            d "Take all the time you need."
            d "I can get us some chocolate? You want some chocolate?"

            scene 3advent with dissolve

            a3 "Yeah. I do. I want some chocolate."

            d "Okay, I'll be right back."

            stop music fadeout 2.0

            jump breaking_in


        label breaking_in:

        play music "audio/black_mermaid.mp3"

        scene 1bombscare with fade

        f "We're going to have to break the glass if we want to get into her house."

        merc "We don't want to tip her off that we're here when she comes back."
        merc "And one thing I've learned over the years is to always try the
            simplest solution first. Pays off more often than you'd think."

        f "There is no way Penny would leave her door unlocked. You're wasting your--"

        play sound "audio/dooropen2.mp3"

        scene 2bombscare with dissolve

        f "No fuckin' way!"

        merc "Maybe she ain't as clever as we thought."

        f "Or maybe she didn't expect anyone to know where she lives. Either way,
            she just made this so much easier for us."
        f "And I ain't carryin' blanks in my revolver this time!"

        scene 3bombscare with dissolve

        f "Pretty clever testing the door first, Merc. It sounds as if you've been
            doing this for a while. Kill a lot of people?"

        merc "Not as many as you might think. A dead person hasn't got much use.
            Clients tend to prefer 'em alive and payin'."

        f "Today we make Penny pay. With her life!"

        merc "Yes! For ruining Lance's butthole."

        scene 4bombscare with dissolve

        f "What? No, for taking my father away from me! Are you seriously doing
            this to avenge Lance's anus?"

        merc "Uhh, no? I'm doing this for all of us!"

        scene 5bombscare with dissolve

        merc "Aha! Right here. We'll hide behind this counter and wait for her to
            return home."

        f "Is there room enough for both of us to sit there?"

        merc "It'll be tight but yeah, we can fit."

        scene 6bombscare with dissolve

        merc "We'll sit in wait right here. She'll be none the wiser that
            we're even at her place!"

        merc "And as soon as she walks through her front door..."

        scene 7bombscare with dissolve

        merc "We blast her!"

        f "She'll never see it comin'. I like the sound of that."

        scene 8bombscare with dissolve

        f "You're sure she can't see us from back here?"

        merc "Maybe move your leg in. It's sticking out a little."

        scene 9bombscare with dissolve

        stop music fadeout 2.0

        f "Shit. Is that better?"

        merc "Perfect! We're practically invisible now. She won't know we're
            here until it's too late!"

        f "Perfect."

        scene 11lostitall with fade

        label post_despair:

        ## After Byron calms down, he has a cute moment with Penny.

        play music "audio/touching_moment.mp3"

        p "Life is pretty hard sometimes for most people. But I looked into you,
            [player_name]. You've had it especially rough."
        p "I used to run with a group of kids when I was younger. There were six of
            us and I was the last to join. We survived by taking care of each other."
        p "We grew close to each other, we became like family. But we led a hard life and
            not all of us survived. In fact, only two of us ultimately did."
        p "We took care of each other, leaned on one another. It's how we got by
            in the harshest of times. It's how we dealt with loss."

        scene 12lostitall with dissolve

        b "I'm sorry you had to go through that. I think about that a lot though.
            I mean, not your situation specifically but how life is hard for everyone."
        b "No matter how bad it gets for me, someone out there has had it worse."

        scene 13lostitall with dissolve

        p "But the people who find the strength to keep fighting are the ones
            who have supportive friends and family."
        p "Before I left the police station, I heard what you said to Evans. I wanted
            to say that it means a lot to me that you're in my corner."
        p "Most people don't agree with the way I handle things."

        scene 12lostitall with dissolve

        b "Most people haven't seen the world through your eyes. Or mine. They
            like to believe the world is fair, or that it can be fair."
        b "But it can't be fair. It never will be. You try to help people and you'll do anything
            to that end. It's noble, Penny. Of course I support that."

        stop music fadeout 1.0

        scene 13lostitall with dissolve

        p "I appreciate that, [player_name]. I really do."

        play music "audio/aint_it_funny.mp3"

        p "But what was that you said there at the end of your talk with Evans?"

        scene 14lostitall with dissolve

        p "'You paid a heavy price today, Detective. The cost was a Penny.'"

        b "It was clever!"

        p "'And that's a price I'm not willing to pay.'"

        b "It was a play on your name. You do it all the time!"

        scene 15lostitall with dissolve

        p "Ahaha! You're such a dork sometimes. It didn't even make sense."

        b "It- it totally made sense. Your name is Penny and that's what it cost him!"
        b "It's clever!"

        p "And it's a price you're not willing to pay. Ahaha. That part had me
            in stitches!"

        b "What about you?"

        show nuh_uh with dissolve

        b "'You don't get to talk to me like that, Evans!'"
        b "'You might be the law but I'm above the law and you don't get to
            talk to me like that, Evans!'"

        p "What the hell, [player_name]? I don't sound like that!"
        p "And why are my eyes crossed in this reenactment?!"

        b "'Don't you know who I am? I'm Penny, bitch. You don't get to
            talk to me like that!"

        p "I didn't even say that!"

        scene 18lostitall with dissolve

        p "Knock it off, [player_name]! That's not how it went at all!"

        b "That's exactly how it went! My reenactment was spot on!"

        p "No, it wasn't! You're misrepresenting me!"

        b "What?? That was my best impersonation ever! It's perfect!"

        scene 19lostitall

        p "Take it back, [player_name]. I'll give you one chance to take it back."

        b "No! It's my masterpiece of imitation! My Magnum Opus!"

        scene 20lostitall with dissolve

        p "If you're not going to take it back, there will be consequences."

        b "What are you doing? Why are you grabbing my earlobe? Don't do that."

        p "Take. It. Back!"

        b "No!"

        scene 21lostitall with vpunch

        b "Ow! My earlobe!"

        p "I warned you!"

        b "You're tugging too hard! Ow!"

        p "Take it back!"

        scene 22lostitall with dissolve

        p "H-hey, what are you doing? Let go of my arm, [player_name]."

        b "Oh you're in trouble now, Penny!"

        scene 23lostitall

        p "Gah! Hey, you can't just pick me up like this!"
        p "Put me down, ya brute!"

        b "Wow, you must weigh hardly anything at all! Do you have bird bones or something?
            You're light as a feather!"

        scene 24lostitall with dissolve

        b "I could hold you up like this all day. How's it feel to be totally
            helpless, Penny?"
        b "Like a little mouse!"

        scene 26lostitall

        p "You know I have a perfect opening to knee you in the balls, right?"
        p "I could end your legacy here and now, [player_name]."

        scene 25lostitall

        b "N-no, I'm sure you can't reach. I'm holding you too far away!"
        b "You're bluffing!"

        p "Am I?"

        scene 27lostitall with dissolve

        b "I'm sure of it! There's no way you can--"

        play sound "audio/faceslap.mp3"

        scene 28lostitall with vpunch

        b "Ow!"

        scene 29lostitall

        p "Ahaha! Classic misdirection! And you totally fell for it! You're
            so gullible!"
        p "All brawn and no brains, eh [player_name]? Maybe spend less time
            at the gym and more time at the library."
        p "Ahaha!"

        scene 30lostitall

        b "Very clever, Penny. But the jokes on you, I didn't even feel that."
        b "My beard absorbed the blow completely. It's basically a furry
            shield for my face."

        scene 31lostitall

        stop music fadeout 1.0

        p "Mehp. Hold on. My butt is vibrating, I must have gotten a notification."

        scene 32lostitall with dissolve

        p "Well, well. What do we have here? My motion detectors in my house are
            going off."
        b "Motion detectors? What does that mean? People are in your house?"

        p "Mhmm. I'm looking at them right now. It looks like they're going to
        try to ambush me when I get home."

        scene 33lostitall

        pause (.5)

        scene 34lostitall with dissolve

        b "Woah, what? They're going to try to kill you?"

        p "The guns they're carrying would indicate that as a high likelihood!"

        b "Are you going to call the police?"

        scene 35lostitall

        p "Nah, I can handle these goons."
        p "This was fun, [player_name]. We should do it again sometime. Hopefully
            with less drama though!"

        scene 36lostitall

        b "Uhh, yeah. This was... nice, actually. Thank you, Penny. I feel better."

        p "You're welcome!"

        b "I hope Avalon doesn't hate me forever but... well, whatever happens, I just
            want her to be happy."
        b "I've given her enough money to start a life. I hope it's enough..."

        scene 35lostitall

        p "You can never know what the future holds. Stay positive! She might be back
            before you know it."
        p "I have to go deal with these trouble-makers. I'll check back with you
            later and make sure you're alright."
        p "Bye for now, [player_name]."

        jump bombscare

        label bombscare:

        scene 10bombscare with fade

        play music "audio/black_mermaid.mp3"

        merc "We might be here for a while. I thought the story you told earlier
            about your dad was kind of cool."
        merc "Can you tell me more about him? What did he do for work?"

        scene 11bombscare with dissolve

        f "His work? He was a dentist. It seemed like the only time when he was
            calm and docile was when he was working on teeth."
        f "I asked him about it once and he said the only good memories he had of
            his childhood was when he lost a tooth."
        f "He would hide it under his pillow at night and he'd find a couple
            dollars in its place the next morning."

        scene 12bombscare with dissolve

        f "He was terrible with numbers though. I had to take care of the paperwork
            and accounting."
        f "Shit, I had to take care of everything that wasn't cleanin' and fixin'
            teeth!"
        f "Why are you really askin' me about this? Are you tryin' to get in
            my pants, Merc?"

        scene 16bombscare

        merc "I wouldn't use those words but I think you're interesting."
        merc "You barged into an assassin's den with confidence I ain't seen
            in a woman before. And the first thing ya did was take charge!"
        merc "You're a brick house to boot. So, I mean, I'd like to get to know ya better."
        merc "But I ain't just chasin' poon here! I respect women."

        scene 14bombscare

        f "You gotta stop listenin' to Lance about how to treat women, Merc."
        f "It's like he's got the right idea but it's all twisted and deformed!"

        scene 12bombscare with dissolve

        f "We do like compliments though and those were some pretty good ones."
        f "How is a mercenary like you such a sweetheart?"

        scene 16bombscare

        merc "According to Lance, I've been different since I got conked on the head."
        merc "That baseball bat must have rattled a few wires loose or somethin'."
        merc "Sometimes I get angry about somethin' nowadays but then I'll zone
            out and the rage just... disappears. It's weird."

        scene 13bombscare

        f "Now that sounds like a nice disorder to have. I wish my anger would
            subside, even if just for a moment."

        merc "I can pistol-whip ya if you want."

        scene 12bombscare with dissolve

        f "No, don't pistol-whip me, Merc. I doubt I would have the same outcome as
            you but thanks for the offer."

        scene 13bombscare with dissolve

        f "Are you even into this then? Do you want to go after Penny or are
            you just followin' along?"

        scene 16bombscare

        merc "I ain't just goin' along. I don't think havin' a dick on my face
        warrants me killin' her."
        merc "But she devastated Lance, he'll never poop right again. And she
            took your dad away from you. So I figure we're doin' what needs to be done."
        merc "Besides, I got orders to take her out. That's how I make my living."
        merc "If I don't kill her, I don't eat."

        scene 15bombscare

        f "I still can't believe she took my father away from me. He's all I had."
        f "I tried so hard to keep him out of trouble but it was impossible!
            He just couldn't control himself."
        f "If I had just done more to help him..."

        scene 18bombscare

        merc "Hey, don't do that. Don't blame yourself. Sounds like you did a lot
            for him. He was lucky to have ya."
        merc "You ain't responsible for his bad decisions. You've got your own
            life to live."

        stop music fadeout 2.0
        merc "Heck, we can walk away from this right now and you won't have to risk
            yourself to avenge your father."

        scene 14bombscare

        f "No, Merc! She has to pay for what she did! I'm gonna put a bullet
            right between her stupid little eyeba--"

        play sound "audio/bombbeeping.mp3"

        "*Beep*"

        scene 21bombscare with dissolve

        f "What the hell? What is that? It sounds like something's beeping."

        merc "It's comin' from the bathroom. We should probably check it out."

        scene 22bombscare

        stop sound

        play music "audio/rumors_about_us.mp3"

        merc "Careful, Faith. Could be anything behind that door. Penny is a
            tricky one."
        merc "She used a flashbang on me that looked like an egg!"

        scene 23bombscare with dissolve

        f "She put blanks in my gun. When I tried to shoot her, she acted like she
            was catching the bullets."
        f "Trust me, I know what a trickster she can be."

        merc "Just open the door slowly, alright?"

        play sound "audio/doorslide.mp3"

        scene 24bombscare with dissolve

        f "I don't see anything. Sounds like the beeping is coming from somewhere
            next to the tub."

        merc "Well, let's get in there and figure out what it is. We don't want
            Penny hearin' it when she comes back."
        merc "We gotta surprise her!"

        scene 25bombscare with dissolve

        f "Okay, is that what I think it is? That can't be what it looks like."

        merc "Oh shit, how the hell did she get one of those?!"

        scene 26bombscare

        merc "That's... that's the business end of a fuckin' missile! That's a
            warhead!"

        f "Merc, why does it say '30' on it? That must mean minutes, right?"

        scene 27bombscare with dissolve

        merc "That would be seconds."

        scene 28bombscare

        merc "We gotta get the fuck outta here! If we start runnin' now, we
            might be able to make it out of the blast radius."

        f "Stop eyeball fucking it and let's go th--"

        scene 29bombscare with vpunch

        play sound "audio/doorbolt.mp3"

        f "Tell me that was not the door locking!"
        f "Tell me we are {b}not{/b} trapped in here!?"

        scene 30bombscare with dissolve

        merc "Shit! It is locked! We... we have to break it down!"

        f "There's no time! We have to disarm this thing!"

        scene 31bombscare

        merc "Wait! Do you even know what you're doing??"

        f "I have no idea! But there's gotta be an off switch or something, right?"
        f "This ain't the movies. You just... you just flip a toggle or press a button
            and it'll disarm. Right!?"

        scene 32bombscare

        stop music fadeout 2.0

        merc "I don't know! I read the 'Anarchist's Cookbook', not 'Warheads for Dummies'!"
        merc "And I ain't even messed with explosives after I blew up a cow on accident."

        f "Wait, what? A cow?"

        merc "Yeah, I was--"

        f "We don't have time for a story! What should I do!?"

        play music "audio/sneaking_up_on_you.mp3"

        scene 33bombscare with dissolve

        merc "Okay, okay! These things ain't generally designed to deter you
            from deactivatin' them. It's.. it's a missile, it goes off on touchdown."
        merc "Nobody's gonna be disarmin' it in mid-freakin' air!"

        f "Okay, what's that mean? I should be able to stop it?"

        scene 34bombscare with dissolve

        merc "Yeah! Just find the wire that connects the timer to the bomb and
            cut it!"

        f "I... I don't have any scissors!"

        merc "Just rip it out!"

        f "Are you sure!?"

        merc "No."

        f "Fuck it. Here goes nothing!"

        scene 35bombscare with dissolve

        merc "Ughn!"

        f "There! I... I pulled out the yellow one."
        f "It... it stopped. The timer stopped. I think we did it!"

        scene 36bombscare with dissolve

        merc "Faith... she's..."

        f "Merc, I did it! It's deactivated!"
        f "Wow, I disarmed a bomb. I'm like, the baddest bitch ev--"

        scene 37bombscare with vpunch

        p "{b}Boom!!{/b}"

        f "Yaaahh!"

        scene 40bombscare with dissolve

        p "Scared you, didn't I?"
        p "You saw the bomb and became completely focused on it. It's called
            tunnel vision and it used to happen to me a lot."
        p "It was one of my biggest weaknesses, actually!"

        f "M-merc?"

        scene 39bombscare

        p "He's taking a nap. He'll be out for a while. So that gives you and I
            plenty of time to have a little talk!"

        scene 38bombscare

        p "I can see that you're in shock right now. I had you going with
            that exclaimed explosion, didn't I?"
        p "You'll come back to your senses in a moment."

        scene 42bombscare

        p "You simply have no idea how outmatched you are, do you? Did you know
            I took down an entire army once?"
        p "I guess one might have considered it a small militia and not
            an actual army but even still!"
        p "And here you are with your little revolver. Such a naive girl, aren't
            you?"
        p "And you actually believed I would blow up my own house, Faith? Really? You are far too
            gullible."

        scene 41bombscare

        f "I-its not real? You were just fucking with me again?"

        p "Uh huh. That's right."

        f "B-but how did you even know I was here?"

        p "I see everything!"

        scene 43bombscare with dissolve

        f "You see everything? Like a deity? No, no. You're fucking with me again!"

        scene 48bombscare with dissolve

        p "O ye, of little Faith."
        p "Okay, fine, I have a surveillance system set up in my house. It's quite
            sophisticated and quite hidden."
        p "I allowed you to live your life, Faith. I gave you a chance.
            And this is how you repay me?"

        scene 45bombscare

        f "You took my father away from me! I'll never forgive you! So you... you
            better just kill me because I'll never stop hunting you!"
        f "He's all I had. And now I'll never see him except through a window!"
        f "I'll never talk to him except through a dirty, corded phone!"

        scene 47bombscare

        p "I get it, Faith. I took something you loved away from you and you're
            mad at me for it. And you have every right to be."
        p "But he hurt a lot of people much worse than I hurt you. Society will
            never forgive him for what he's done."
        p "And neither will the fathers, mothers, sisters, and brothers of those
            he hurt. Do you understand, Faith?"
        p "I didn't do this to hurt you. I did this to stop him from hurting
            more people."

        scene 46bombscare

        f "It's not his fault! He... he's sick. He just couldn't help it."
        f "I tried to stop him. I tried! But he was impossible to control."

        scene 48bombscare

        p "He's not your responsibility anymore, Faith. You have a chance to live
            your life without his sickness looming over you."
        p "He left you his dental practice, right? Make something of it! Or sell
            it and find something else. Go live your life, Faith."
        p "And trust me when I say this; if you come after me again..."

        scene 49bombscare with dissolve

        p "It will be the last time. And you can take that to the bank."

        scene 44bombscare

        f "Oh Christ, the bank? Because your name is Penny? You really play off
            the coin puns, huh?"
        f "That's just.. awful."

        scene 48bombscare

        p "Listen, I have bigger fish to fry. You can stay here while you wait for
            your partner to wake up. It'll give you time to consider what I've said."
        p "If you take any snacks from the refrigerator, don't touch the eggs."

        scene 44bombscare

        stop music fadeout 2.0

        f "I hate that you're trying to bond with me right now."

        scene 45bombscare with dissolve

        f "I'll never forgive you!"

        scene 46bombscare with dissolve

        f "My father was a monster but he was {b}my{/b} monster. He's all I had."

        p "I did what needed--"

        f "Just go..."

        scene 48bombscare

        p "Goodbye, Faith."
        p "I hope I don't see you again."

        jump nightsix

        ## Byron and Avalon go a little further in bed.

        label nightsix:
            if _in_replay:
                $ player_name = renpy.input("What would you like to name the MC?")
                if player_name.strip() == "":
                  $ player_name = "Byron"

        scene 1nightsix with fade

        bi "{i}I can't stop seeing my father hanging from the ceiling. I've
            seen death before but that... that was something more.{/i}"
        bi "{i}It also opened doors I was dreading stepping through. Well, one
            specific door.{/i}"
        bi "{i}I knew I'd have to tell Avalon about her father one day. And I knew
            it would devastate both of us.{/i}"
        bi "{i}It isn't knowing that hurt her, it's that I hid it for so long.
            I just hope she doesn't hate me forev--{/i}"

        scene 2nightsix

        play music "audio/your_hand_in_mine.mp3"

        a3 "Uncle? Are you... are you awake?"

        scene 3nightsix

        b "Avalon! I didn't hear you come in. What are you doing here?"
        b "Is everything alright?"

        scene 2nightsix

        a3 "Everything is fine. I snuck in a few minutes ago. We should
            be better about locking the front door."
        a3 "I um.. I wanted to talk to you about what happened earlier."
        a3 "I have some things I'd like to say."

        scene 3nightsix

        b "Of course. We can talk in the kitchen if you want?"

        scene 4nightsix with dissolve

        a3 "Here is fine."

        b "What are you doing?"

        scene 5nightsix with dissolve

        b "Gah! Is this my punishment? I have to sleep without a blanket?"
        b "But my feet get cold easily!"

        scene 6nightsix with dissolve

        a3 "I don't want anything between us, Uncle. I have a lot I want to say."
        a3 "No being silly right now! This is a serious talk."

        scene 7nightsix

        b "Okay, that's fair. No jokes."
        b "I'm really sorry about earlier, Avalon. I shouldn't have kept those
            things from you."
        b "I just--"

        scene 8nightsix with dissolve

        a3 "Shh. Let me speak first. I have a lot to say and I don't want you to
            interrupt."

        scene 9nightsix with dissolve

        a3 "You hurt me, [player_name]. Worse than I ever thought you could. I
            don't know if I can ever forgive you for not telling me the truth about my dad."
        a3 "But... I also understand that you were in an impossible situation.
            I don't know what I would have done in your position."
        a3 "That's not all you did though. You left for years! And then you found out you
            have a [persistent.leah_rel] and you never told me about her!"
        a3 "I know everyone has secrets, everyone keeps some things to themselves.
            But you kept too much. We're supposed to be a team!"
        a3 "You can't lie to me. You can't keep things from me! Not anymore."
        a3 "If you do, I won't come back next time. Do you understand?"

        scene 10nightsix

        b "I understand. You're right, I made a lot of mistakes. And I'm sorry."
        b "I can't promise that I won't make more mistakes. In fact, I can assure you
            that I will."
        b "But I won't lie to you again. We'll keep everything in the open.
            I promise."
        b "I don't know how to be in a relationship, Avalon. I've been alone
            for so long. This is new to me."

        scene 14nightsix

        a3 "We'll figure it out. Together. We're partners!"

        scene 16nightsix with dissolve

        a3 "I... I was worried about you when I left earlier. You had a dream about
            my dad, you found your father after he'd hanged himself."
        a3 "And then I shouted at you again as I left..."
        a3 "I was worried about you. Did Penny stop by? I asked if she would check
            on you..."

        scene 11nightsix

        b "She did. And thank you for that. Penny and I bonded quite a bit today."
        b "I'm not sure I would have been able to get through today if it weren't
            for her."
        b "We might need to return the favor to her. Evans told her she can't
            assist the police anymore. She was pretty upset."

        scene 17nightsix

        a3 "Wait, you're saying she can't be a detective anymore?"
        a3 "But she's amazing! Why would they do that??"

        scene 10nightsix

        b "Well, she told me herself that she breaks a lot of rules. According
            to Evans, she's no better than the criminals."

        a3 "Did you tell him to go to hell!?"

        b "N-no! He's a cop! But... I did side with Penny. She might be a bit of a
            nut but she's been such a boon for us..."
        b "I'm sure it's frustrating for Evans though. He's got his hands tied
            by rules and regulations. Watching Penny do whatever she wants..."
        b "That's got to be hard."

        scene 15nightsix

        a3 "I guess I didn't think about it like that."

        scene 14nightsix with dissolve

        a3 "Well, I still think they could benefit from having her around!"
        a3 "But anyway, I um... I have something for you."

        b "Oh, what is--"

        scene 18nightsix with dissolve

        ai3 "{i}The moment my lips pressed against his, I forgave him.{/i}"
        ai3 "{i}He didn't hide the truth about my father to hurt me. He did it
        to keep me safe.{/i}"
        ai3 "{i}He would sacrifice anything and everything to protect me. And I
            could see that when he looked at me.{/i}"
        ai3 "{i}I could feel that when he touched me.{/i}"

        scene 19nightsix with dissolve

        bi "{i}I was so afraid when she left. I thought I might drown in sorrow.{/i}"
        bi "{i}Feeling her lips press against mine lifted the darkest depression
            I had ever felt.{/i}"
        bi "{i}I have to change, I have to be better now. I'm not alone anymore.
            For her, I have to be a better man.{/i}"

        scene 20nightsix with dissolve

        a3 "I forgive you."

        b "W-what? Already? I thought you might never forgive me??"

        a3 "I know! But... I forgive you!"
        a3 "I love you."

        b "I love you, too, Avalon."

        scene 21nightsix with dissolve

        a3 "Gah! What... what is that?"

        b "Shit, sorry. I got a little excited."

        scene 22nightsix with dissolve

        a3 "It's your penis?"

        b "Yep. I've got the prettiest girl in the world on my lap. It's hard
            to keep him calm under the circumstances."

        a3 "H-he's pressing into my... my..."

        scene 23nightsix with dissolve

        b "Sorry, I didn't mean for him to interrupt us. I can go pour ice water
            on him if you want? Calm his ass down."

        a3 "No, it's alright. I think I've got a better way to handle him."

        scene 24nightsix with dissolve

        b "Wait, you're taking off your shirt?"
        b "That's just going to exacerbate the problem!"

        scene 25nightsix with dissolve

        a3 "I know! I wanna play."

        b "I thought I might not see these again for a while."

        a3 "You like my boobs, huh?"

        b "It's a crying shame they're locked behind a shirt most of the time."

        a3 "You know, I haven't seen all of you yet."

        scene 26nightsix with dissolve

        b "That's true. Last time--"

        a3 "I know what happened last time. I want to try again."
        a3 "Come on. Take off your underwear."

        scene 27nightsix with dissolve

        b "Are you sure?"

        a3 "Yeah! I'll be fine!"
        a3 "I want this. I promise."

        b "Alright, off they go then!"

        scene 28nightsix

        ai3 "{i}Okay, maybe this was a bad idea. I can feel the anxiety creeping
            up!{/i}"
        ai3 "{i}But I want this! Come on, Avalon! Pull yourself together!{/i}"

        scene 29nightsix with dissolve

        ai3 "{i}What was it Dr. Yu said? Focus on my ring, right? Take a deep breath,
            and remember that [player_name] loves me.{/i}"
        ai3 "{i}And I know he'll stop if I ask him to. He wouldn't do anything to hurt
            me.{/i}"
        ai3 "{i}Yeah! I've got this!{/i}"

        b "O-okay. They're gone."

        scene 30nightsix with dissolve

        a3 "Ah! What the devil!? That thing is a monster!"

        b "I warned you! I wasn't comparing it to an ancient legendary shark to
            be funny. I was trying to prepare you!"

        a3 "Uncle, I think it's inflamed. Are you sure you don't have an infection?
            Maybe you need a doctor?"

        b "No, it's supposed to look like this! It's just a little above average
            in size. It's not infected!"

        scene 31nightsix with dissolve

        a3 "It's supposed to look like that? You're sure?"

        b "I mean, mostly sure. I haven't exactly seen a lot of other penises to
            compare it to."

        a3 "It's not as scary as I'd imagined in my head. I feel kind of
            silly for being so afraid of it before."

        b "I only use my penile powers for good."

        a3 "It's... it's kind of cute."

        scene 32nightsix with dissolve

        b "Hey! Don't emasculate him like that! He's not cute. He's a rugged and
            powerful beast!"

        a3 "Okay! I'm sorry! Sheesh. Are all guys this defensive about their
            penises?"

        b "I don't know. But if not, they should be!"

        scene 33nightsix with dissolve

        a3 "Anyway! I uhm, I want to touch it."

        b "He doesn't bite."

        a3 "It's so freakishly big. That cannot be normal."

        b "Thank you."

        scene 34nightsix with dissolve

        a3 "Wow! It's so hard! How do you walk around with this thing?"

        b "It's usually a lot less potent when you're not around."

        a3 "Oh yeah! It's flaccid when you're not ready for sex, right?"
        a3 "I looked it up on the internet!"

        b "Online pornography is the internet's greatest gift to mankind."

        a3 "I thought the greatest thing to come from the internet was instantaneous
            global communication but porn sounds right too."

        scene 35nightsix with dissolve

        a3 "Ooh. It's squishy! Like, rubbery."

        b "You're... you're grabbing it wrong. It's not pottery clay!"

        scene 36nightsix with dissolve

        a3 "What do you mean? How am I supposed to hold it?"

        b "Well, you have to grip it like..."
        b "Like a baton! When you did cheerleading, you practiced with a baton
            sometimes, right?"

        a3 "Uhh, yeah. So..."

        scene 37nightsix with dissolve

        a3 "Let me get into a better position here. And then I put my hand around
            it like..."

        scene 38nightsix with dissolve

        a3 "This?"

        b "Mhaw, wow! Yep!"

        scene 39nightsix with dissolve

        a3 "You really liked that? It's that easy!?"

        b "It's not that easy! But... yeah, I mean, you gripping it feels really good."

        a3 "I can feel your heartbeat through your penis. That's so crazy!"

        scene 38nightsix with dissolve

        a3 "Okay, so what do I do now?"
        a3 "You have to pull on it, right?"

        b "Y-yeah, pull up and then push down over and over."

        scene 39nightsix with dissolve

        a3 "Alright, let's give it a try. Tell me if I'm doing anything wrong."

        show avalon_hj with dissolve

        b "Oof, wow! Your grip is so light and gentle. It's tantalizing!"

        a3 "Is that a good thing? Should I grip harder?"

        b "No no, I like it this way. It's-- Wow! It's nice!"

        a3 "Is there anything I can do to make it feel even better?"

        b "Oh man, I'd love to put it inside you."

        scene 40nightsix with dissolve

        a3 "Inside... me? But the last time..."

        b "Shit, I shouldn't have said that."

        a3 "It wouldn't fit though. It would hurt me..."

        scene 41nightsix with dissolve

        b "I'm sorry, Avalon! I should have phrased that better."
        b "I just meant, when you're ready--"

        a3 "I don't feel good. My heart is racing. I'm having trouble breathing."

        b "We can stop here. It's okay."

        a3 "Can you... can you go stand next to the hallway? Please?"

        b "What? The hallway? Okay, yeah, sure."

        show avalon_breath

        ai3 "{i}Just breath, Avalon. Deep breaths. Calm down.{/i}"
        ai3 "{i}I hate this! Stupid, stupid anxiety! I don't want to be like this
        anymore! I want to be able to enjoy my life...{/i}"
        ai3 "{i}Come on, I can do this. I'm okay, dammit! I don't want to quit.
            I don't want to be controlled by this...{/i}"

        scene 45nightsix

        b "Are you alright? I can get you some water? Or a shirt so you can cover up?
            Whatever you need."
        b "I got carried away. I wasn't thinking when I said that."
        b "I hate not being able to comfort you."

        scene 44nightsix

        a3 "You put your boxers back on?"

        b "Yeah, I thought that might make you more comfortable."

        a3 "It's not your fault. It's my memories. I want to have sex, Uncle, I do!"
        a3 "I don't know why I keep having panic attacks. I just can't help it."

        scene 45nightsix

        b "I know. I don't care about the sex, I can wait. I just don't like seeing you
            in pain like this."
        b "And now you've condemned me to the back of the room and all I can do is
            watch you suffer. It's killing me!"
        b "You need to be in control so I'm giving you that but it means that I'm
            not in control. It's not easy for me..."

        scene 46nightsix

        a3 "Aw, Uncle. I'm feeling better. Come here, I want to put my arms around you."

        b "Are you sure?"

        a3 "Yeah! My heart is calming down and I feel less panicked. Come here!"

        scene 48nightsix with dissolve

        a3 "Sometimes I get so wrapped up in myself and my trauma that I forget
            you've got pain too. It's not very fair of me."
        a3 "When I look up at you, I see you as this towering pillar of strength."

        scene 51nightsix with dissolve

        a3 "But when you talk like that, I remember that you're a person just like me.
            Confused and vulnerable and just trying to do what's right."
        a3 "We've both had pain and it's not fair that I forget about yours so often."

        scene 49nightsix

        b "I don't feel my pain when you're around, Avalon. It's like I have blinders
            on and all I see is you."
        b "You give my life purpose. The responsibility I feel for your happiness,
            it drives me forward."
        b "And knowing that I'm the cause of your panic attacks, it's the worst
            pain..."

        a3 "It's not you!"

        scene 52nightsix

        a3 "I mean, it is you but... Ugh. It's so stupid!"
        a3 "I want sex. I really want it! But every time I think about a man
            on top of me, inserting themselves inside me..."
        a3 "I want sex and I'm terrified of it at the same time. My mind, [player_name],
            it's just broken."

        scene 49nightsix

        b "I just don't understand. Why do you want sex then? Why don't we just
            enjoy each other's company for a few weeks?"
        b "Why are you so obsessed with sex?"

        scene 48nightsix

        a3 "After you kissed me for the first time, I just can't help myself.
            I'm horny, like, all the time now!"
        a3 "I've never felt like this before and I'm not sure exactly why it's happening
            but I'm overwhelmed with lust."

        scene 53nightsix with dissolve

        a3 "I like thinking about you ripping my clothes off and ravishing me!"
        a3 "It gets me wet imagining your big, rough hands running across
            my naked body."
        a3 "And I think about your lips pressing against my nipples and flicking them
            with your wiggling tongue."

        scene 52nightsix with dissolve

        a3 "But then, when I think about you spreading my legs and..."
        a3 "Well, I can't get farther than that in my head. I start to get
        uncomfortable."

        scene 49nightsix

        b "Then let's take that off the table for right now. We won't have sex!"
        b "We can do whatever else you want to do but no actual sex."
        b "Would that help? Knowing that it won't happen."

        scene 51nightsix

        a3 "Actually, yeah, it does kind of help."
        a3 "We won't have sex yet! Okay, yeah, it does make me feel better."

        scene 54nightsix with dissolve

        a3 "Mwah!"

        scene 48nightsix with dissolve

        a3 "Thank you, Uncle."

        b "You're welcome."

        scene 55nightsix with dissolve

        a3 "Let's continue where we left off. It's my turn, right?"

        b "Wait a minute, no! We didn't finish with me!"

        a3 "Too bad!"

        scene 56nightsix with dissolve

        b "How did I fall in love with such a cheater?"

        a3 "Whatever, you like it."

        b "Alright, your turn. But only because you're so cute!"
        b "What do you want?"

        scene 57nightsix

        a3 "I uhh, I hadn't thought that far ahead."
        a3 "What do people usually do at this point?"

        b "I can tickle your feet."

        a3 "No! I don't want that! I want... you know, fingered I guess?"

        scene 58nightsix

        b "Okay, we'll have to get rid of these though. Is that alright?"

        a3 "Umm..."
        a3 "Yeah, let's do it!"

        scene 59nightsix

        ai3 "{i}He's being so gentle this time.{/i}"
        ai3 "{i}Oh my God, he's going to see my vagina. I hope he likes it!{/i}"

        scene 1avalon_thumbrub with dissolve

        b "You're naked!"

        a3 "Y-yeah. Do you like it?"

        b "Your vagina?"

        a3 "Yeah, I mean, do you... do you think it looks okay?"

        b "It looks great!"

        show avalon_thumbrub with dissolve

        b "It feels nice too."

        a3 "W-whoa! Wow! You're... you're really turning me on right now!"

        b "It's so smooth and wet. I can glide right across you, Avalon."

        a3 "That's making me really horny, [player_name]..!"

        scene 60nightsix with dissolve

        b "Do you want to go one step further? We can stop here if you prefer."

        a3 "N-no, I said I wanted you to finger me. I think..."
        a3 "I think you should! I want it."

        b "Let's just try a little at first."

        a3 "O-okay."

        scene 1avalon_fingered with dissolve

        a3 "Ah!"
        a3 "Is that... just the tip?"

        b "Yeah."

        a3 "I... I like it. I want it inside me. Keep going."

        show avalon_fingered with dissolve

        a3 "Ooh! Your finger is so big!"

        b "Is it okay?? It's not too much, is it?"

        a3 "It feels amazing! Keep going. Harder!"
        a3 "Push it in further!"

        b "I... I can't. That's as far as I can go."

        scene 61nightsix with dissolve

        a3 "Okay, stop, stop. I can't... It's not enough. I just want more."
        a3 "But I'm not ready for anything more yet. Let's just stop here."

        b "Are you sure? I can go get that toy I bought you."

        a3 "No, it's fine. Maybe next time."

        b "Well this was fun. We can try more next time, right?"

        a3 "No! I'm not done with you. Stand up!"

        b "Really?"

        scene 62nightsix with dissolve

        a3 "I really want to let you finish, Uncle. I'm sure you're frustrated
            by now. And I don't mind!"

        a3 "I want to play with it more anyway. Is that alright?"

        b "Yep!"

        scene 62nightsix2 with dissolve

        a3 "There it is! Jeez, it still seems unreal to me. It should not be this thick!"
        a3 "Is the tip supposed to be pink like this or is he a little shy and blushing?"

        b "He's not shy!"

        scene 63nightsix with dissolve

        a3 "So I just grab it like this, right? I can't get my hand around it though."
        a3 "Is there a specific way you want me to work on this thing?"

        b "Mm, well, you could tug on it while looking up at me. That's pretty sexy."

        scene 1avalon_hj2 with dissolve

        a3 "That's all? That's so easy though!"

        b "Those are some pretty blue eyes you have there, Avalon."

        a3 "Aw, thank you! Should I start?"

        b "Absolutely!"

        show avalon_hj2 with dissolve

        b "Yaagh! Those tiny little hands are freakin' great!"

        a3 "It's so long, Uncle! I can feel it twitching too!"

        b "You're so gentle with it. I'm used to a more aggressive approach. But
            this is much better!"

        a3 "I'm getting wet playing with your penis."
        a3 "I kind of wish I didn't make you stop fingering me earlier."

        b "Avalon, I'm... I'm about to finish!"

        scene 24avalon_hj2 with dissolve

        a3 "Wait! I want to taste it."

        b "R-really?"

        a3 "Yeah! Here."

        scene 20avalon_tasteit with dissolve

        a3 "Mm mmh!"

        b "Goddammn, Avalon. You're really going the extra mile here!"
        b "You're uh.. you're going to have to keep stroking it though."

        a3 "Mmhmm!"

        show avalon_tasteit with dissolve

        b "Oh fuck, yes! I love that! Keep going!"

        a3 "Mm mmhmm!"

        b "Brace yourself, Avalon!"
        b "I'm... I'm cumming!"

        scene 64nightsix with vpunch

        a3 "Mm!"

        scene 65nightsix with dissolve

        b "Gaah!"
        b "Hold on, there's more!"

        scene 66nightsix with vpunch

        a3 "MMH!"

        scene 67nightsix with dissolve

        b "Ugnh!"
        b "One more, Avalon. Just hang on!"

        scene 68nightsix with vpunch

        a3 "MMMH!!"

        scene 69nightsix with dissolve

        b "Oooh fuck yes!"
        b "That's all of it. That was amazing!"

        scene 70nightsix with dissolve

        a3 "Mm mmhmm?"

        b "Wait! Don't spit it out! You'll get it on the carpet!"
        b "Um, shit! Can you... can you swallow it?"

        scene 71nightsix with dissolve

        play sound "audio/swallow.mp3"

        b "Holy shit."

        scene 72nightsix with dissolve

        a3 "Aaah!"

        scene 73nightsix with dissolve

        a3 "I swallowed it! It's gone!"

        b "Impressive. Good job. How was it?"

        a3 "It wasn't bad at all! It's sort of sweet, actually."
        a3 "Did you enjoy it??"

        b "That was incredible, Avalon. Thank you!"

        a3 "You're welcome!"

        if persistent.pastthepanic == False:
            $ renpy.notify("You've unlocked 'Past the Panic' in the Scene Gallery on the Main Menu!")
            $ persistent.pastthepanic = True

        $ renpy.end_replay()

        scene 75nightsix with fadefast

        b "Ooh man, this day did not end like I thought it would at all."
        b "I guess you never know what the future might hold, huh?"

        scene 76nightsix with dissolve

        a3 "Ohh yeah, we definitely nailed it this time. I'm glad we didn't stop
            when I started to freak out!"
        a3 "Imagine the greatness we would have missed out on."

        scene 77nightsix with dissolve

        a3 "But I appreciate that you were so patient with me."
        a3 "I, uhm... I needed that. Thank you."

        b "Of course! I could have waited longer, you know?"

        stop music fadeout 2.0

        a3 "You shouldn't have to!"

        play sound "audio/doorbell.mp3"

        scene 78nightsix with dissolve

        a3 "What the heck?"

        b "Huh. Must be Penny. She said she was going to check on me tonight."
        b "Wait here, I'll go check."

        a3 "O-okay."

        scene 79nightsix with fadefast

        b "Penny, I don't mind you stopping by but you should have called first."
        b "At least you didn't interrupt something this time."

        scene 80nightsix with dissolve

        b "We just fini--"

        scene 81nightsix

        b "Wha!"
        b "It's... it's you..!"

        jump act_seven_s

        label outro_six:

        scene 7outrokixx with fade

        ts "Boo! Cliffhangers suck! Down with Lockheart!"

        scene 1outrokixx with dissolve

        ts "Come on, man. It's not like we can't guess who it is."
        ts "Do you think we're that stupid?"

        scene 2outrokixx with dissolve

        ts "So they filled me in on what the crap this is. Apparently,
            my universe is acting as an outro for some lame story?"
        ts "I can't quite describe how small and insignificant that makes me feel."
        ts "But I read the story and I'll admit, it's pretty good."

        scene 5outrokixx with dissolve

        ts "It would have been way better if I was the star though. I might not
        be top-heavy but I have a cute butt, dammit!"
        ts "Whatever. I don't care. What the balls am I supposed to say here?"

        scene 3outrokixx with dissolve

        ts "Let's talk about what just happened in this last Act, shall we?"
        ts "A lot of people are going to be confused about how we found Gladstone
            earlier."
        ts "I mean, there's no damn villain in this story now!"

        scene 6outrokixx with dissolve

        ts "Maybe the main villain hasn't even revealed herself yet! Maybe it's a
            badass archer that keeps getting kicked out of every community she joins."
        ts "A devious yet adorable little double-ponytailed halfling with a cute butt!"

        scene 5outrokixx with dissolve

        ts "It's not. It's not me. I'm still pissed about being a stupid outro!"

        scene 4outrokixx with dissolve

        ts "I did hear a rumor that there's still one big surprise in store in Act
        Seven."
        ts "I guess you'll have to wait and see!"

        scene 3outrokixx with dissolve

        ts "So here's the down-low. We have to finish Act Seven, we're going to work
            on a bonus Act Eight and then we have to go back and polish up a few scenes."
        ts "We're going to try to make Avalon as exceptional as possible before we
            {b}possibly{/b} put it on Steam."

        scene 2outrokixx with dissolve

        ts "Avalon hasn't been a terribly popular story. People have been very divided
            on it."
        ts "So as we finish up with Avalon, we're going to take everything we learned
            and put that knowledge and love into Penny for Your Thoughts."
        ts "We're also going to force you to love her. Yeah, seriously. The next act
            is going to solidify your deep and desperate love for Penny."

        scene 3outrokixx with dissolve

        ts "We'll keep you updated with what's going on with the next release."
        ts "Remember, it's important that you tell us what you liked and didn't like
            about Avalon so we can make our next piece of work awesome!"
        ts "Thanks for your support! We'll see you again soon!"
        ts "Bye for now!"

        return


        scene 1outrosix with fade

        play music "audio/violet_shimmer.mp3"

        nq "Greetings!"
        nq "I am Queen Naudica and you've reached the end of the current content
            for Avalon."
        nq "Myrabelle is a bit pre-occupied so she asked me to step in for her."
        nq "She's my sister!"

        scene 2outrosix with dissolve

        nq "She asked me to tell you something..."
        nq "Hmm. It seemed important. What was it?"
        nq "It had something to do with Avalon. I'm sure of that."
        nq "Mostly sure..."

        scene 3outrosix with dissolve

        cas "More. Acts."

        nq "No, that wasn't it."
        nq "It was something about additional content due to the new girl, yes?"

        scene 4outrosix with dissolve

        nq "Oh yes! Lockheart is going to make more than seven acts for Avalon!"
        nq "There's a lot more to explore with Leah and her interaction with
            everyone else."
        nq "Well, this is assuming, of course, that people want to see more of Leah."
        nq "If that isn't the case, we'll end Avalon at seven acts."
        nq "So let us know if you liked her or not, please!"

        scene 3outrosix with dissolve

        nq "Was there more?"
        nq "I'm sure there was..."

        cas "Penny."

        scene 4outrosix with dissolve

        nq "Oh yes! Penny!"
        nq "We're sorry you didn't get to see her in this release."
        nq "The next release is going to feature her heavily though!"
        nq "I'm confident you're really going to like the direction Lockheart
            is going to go with her."

        play sound "audio/arrow_wood.mp3"

        pause (.2)

        scene 5outrosix with vpunch

        nq "Goodness!"
        nq "Was that an arrow??"

        scene 7outrosix

        ts "Excuse me! Yeah, over here."
        ts "This is the Archer's Den. You're obviously not an archer."
        ts "So I'm going to have to ask you to promptly exit."
        ts "Jeez, no respect. We get no respect! This is clearly our area,
            there's archery stuff all over the place."
        ts "Ugh!"
        ts "Why are you talking to the air, by the way? That's really creepy."
        ts "And why does that target dummy have so many arrows in it's crotch?
            What lunatic is aiming strictly at genitalia!?"

        scene 6outrosix

        nq "Castle, what is that tone?"
        nq "I don't believe I've ever heard it before."

        cas "Audacity."

        nq "Excuse me, Miss Archer. I'll only be another moment. Please come back
            later."

        scene 7outrosix

        ts "Of all the places! You chose here!? And at the very time of my practice
            session. Ugh!"
        ts "Can't you do this somewhere else? Why are you here? There's plenty of other
            places you could be talking to yourself like a loon!"

        scene 9outrosix

        nq "I was wandering around rather aimlessly if I'm being honest."
        nq "I stumbled in here by chance. I'd forgotten how big this room is!"

        scene 10outrosix

        ts "Yeah well, we archers are the most important military assets so it
            only makes sense our room would be spacious."
        ts "Look, are you going to leave or am I just going to have to
            fire my arrows while you're downrange?"

        scene 8outrosix

        nq "You realize you're speaking to your Queen, don't you?"

        ts "Queen!? Well, I didn't vote for you."

        nq "That's not--"

        ts "And seeing as how you've been talking to yourself for the past
            several minutes, I'd say you're not fit to be Queen."
        ts "Perhaps you are crazy and delusional? And this 'Queen' position is
            something you just made up!"

        scene 11outrosix with dissolve

        nq "Castle, would you politely ask the young archer here to come back
            later?"

        cas "With. Pleasure."

        ts "Ha! What's he going to do? Stare me into submiss--"

        scene 12outrosix with dissolve

        ts "Wah!"
        ts "What the crap?!"

        scene 13outrosix with dissolve

        ts "What sorcery is this!?"
        ts "Is that a damn golem??"

        scene 14outrosix with dissolve

        ts "By the winds!"
        ts "That thing is huge!"
        ts "Why is it named Castle? Is it part of the castle? Or is the actual
            friggin' castle!?"

        scene 16outrosix with dissolve

        ts "Oh boy."
        ts "I'm in trouble."

        scene 15outrosix with dissolve

        ts "This is my life."
        ts "I've always got my foot in my mouth."
        ts "Consequences, Tsera. Consequences."

        scene 17outrosix

        cas "Go. Away."
        cas "Or. Be. Squish."

        scene 18outrosix

        ts "A golem of few words, I see."
        ts "Yet still effectively communicating your intentions."
        ts "Quite intimidating. Indeed."

        scene 19outrosix with dissolve

        ts "Fine!"
        ts "I'm famished. I was considering taking an early lunch anyway."
        ts "So I'll go. But not because you told me too! You fat rock!"
        ts "And if I come back and you're still here... Winds help you!"

        scene 20outrosix with dissolve

        ts "Stupid Queen and her stupid, dumb butt-faced golem!"
        ts "Ugh!"
        ts "Don't they know who I am!?"
        ts "Dammit!"

        scene 21outrosix with dissolve

        nq "Thank you, Castle!"

        cas "Queen. Too. Soft."

        nq "I know. I know."
        nq "But she's right! We're in her territory!"

        cas "All. Castle. Yours."

        nq "Sharing is caring!"

        scene 22outrosix with dissolve

        nq "Thank you so much for taking the time to enjoy Avalon!"
        nq "Lockheart is going to get started on the second half of Act 6 right away."
        nq "There's much to do!"

        scene 23outrosix with dissolve

        nq "That's all we have to share with you on this release."
        nq "We'll see you on the next!"
        nq "Farewell!"

        scene 24outrosix with dissolve

        nq "Say 'Goodbye', Castle."

        cas "Goodbye."

        return
