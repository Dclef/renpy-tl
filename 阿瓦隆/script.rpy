# The script of the game goes in this file.


define b = Character("[player_name]", color="#FF8000", image="byron")
define bi = Character("[player_name]", color="#FF8000", image="byron_thinking")
define yb = Character("[player_name]", color="#FF8000", image="ybyron")
define lb = Character("[player_name]", color="FF8000", image="lbyron")
define a = Character("阿瓦隆", color="#0080FF", image="avalon")
define a2 = Character("阿瓦隆", color="#0080FF", image="avalon2")
define a3 = Character("阿瓦隆", color="#0080FF", image="avalon3")
define ai = Character("阿瓦隆", color="#0080FF", image="avalon_thinking")
define ai2 = Character("阿瓦隆", color="#0080FF", image="avalon_thinking2")
define ai3 = Character("阿瓦隆", color="#0080FF", image="avalon_thinking3")
define s = Character("莎罗尔", color="#4B8A08", image="sharol")
define sh = Character("莎罗尔", color="#4B8A08", image="sharol_black")
define sg1 = Character("莎罗尔", color="#4B8A08", image="sharolg1")
define sg2 = Character("莎罗尔", color="#4B8A08", image="sharolg2")
define o = Character("奥克塔维娅", color="FFFF00", image="octavia")
define o2 = Character("奥克塔维娅", color="FFFF00", image="octavia2")
define o3 = Character("奥克塔维娅", color="FFFF00", image="militaryoctavia")
define oi = Character("奥克塔维娅", color="FFFF00", image="octavia_thinging")
define d = Character("达拉斯", color="FF00FF", image="dallas")
define di = Character ("达拉斯", color="FF00FF", image="dallas_thinking")
define w = Character("女服务员", color="4B088A", image="waitress")
define r = Character("兰德尔", color="FFBF00", image="randall")
define sm = Character("孙梅", color="00BFFF", image="sunmei")
define sun = Character("孙梅", color="00BFFF", image="sunmei")
define j = Character("约翰尼", color="228B22", image="johnny")
define cl = Character("店员", color="FFA500", image="clerk")
define n = Character("妮可", color="b87333", image="nicole")
define de = Character("败类", color="808000", image="degenerate")
define p = Character("佩妮", color="b87333", image="penny")
define e = Character("埃文斯", color="1E90FF", image="officerevans")
define det = Character("埃文斯", color="1E90FF", image="evans")
define m = Character("米拉贝尔", color="8A2BE2")
define m2 = Character("米拉贝尔", color="8A2BE2", image="myrabelle")
define f = Character("费思", color="FFA500", image="faithb")
define fg = Character("费思", color="FFA500", image="faithg")
define t = Character("泰勒", color="8B0000", image="tyler")
define ps = Character("佩妮", color="b87333", image="penny")
define ps2 = Character("佩妮", color="b87333", image="penny")
define psi = Character("佩妮", color="b87333", image="pennys_thinking")
define ps3 = Character("佩妮", color="b87333", image="penny")
define p3 = Character("佩妮", color="b87333", image="penny")
define po = Character("佩妮", color="b87333", image="stowawaypenny")
define k = Character("肯尼迪", color="00FF7F", image="kennedy")
define suzi = Character("苏子", color="FFFFFF", image="suzi")
define merc = Character("默克", color="DC143C", image="merc")
define dr = Character("余医生", color="09FF00", image="dryu")
define lance= Character("兰斯", color="DAA520", image="lance")
define x = Character("仙恩", color="B50000", image="xianne")
define glad = Character("格莱斯顿", color="A1A1A1", image="gladstone")
define ben = Character("本森博士", color="1E90FE", image="benson")
define morton = Character("莫顿", color="30F200", image="morton")
define l = Character("莉娅", color="FF3838", image="leah")
define ts = Character("泽拉-基克斯", color="F00F34", image="tserakixx")
define cas = Character("城堡", color="D3D3D3", image="castle")
define nq = Character("诺迪卡女王", color="00FFFF", image="naudica")
define sid = Character("西德尼", color="228b88", image="cassidy")
define pat = Character("帕特里夏", color="ff7f50", image="patricia")
define sierra = Character("茜拉", color="f7ff1e", image="sierra")


## Bonus Act Character Definitions ##
define l2 = Character("莉娅", what_suffix="\"", what_prefix="\"", color="FF3838")
define b2 = Character("[player_name]", what_suffix="\"", what_prefix="\"", color="FF8000")
define a4 = Character("阿瓦隆", what_suffix="\"", what_prefix="\"", color="#0080FF")
define s2 = Character("莎罗尔", what_suffix="\"", what_prefix="\"", color="#4B8A08")
define pn = Character("佩妮", what_suffix="\"", what_prefix="\"", color="#b87333")
define oe = Character("埃文斯", what_suffix="\"", what_prefix="\"", color="#1e90ff")
define hw = Character("亨利·韦斯特", what_suffix="\"", what_prefix="\"", color="#33BEFF")
define mi = Character("米莉", what_suffix="\"", what_prefix="\"", color="ffbf00")

## Bonus Act Variables ##
default lewd = 0
default wholesome = 0
default caughtncum = False
default persistent.lewdlingerie = False
default persistent.limitedtime = False
default persistent.bonusnightlewd = False
default persistent.bonusnightwholesome = False

define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define purpleflash = Fade(0.1, 0.0, 0.5, color="#8A2BE2")
define fade = Fade(0.5, 1.0, 0.5)
define fadefast = Fade(0.5, 0.0, 0.5)
define slowdissolve = Dissolve(2)

default player_name = "Byron"
default monogamy = False
default polygamy = True

define WhichGirl = "none"
default octavia = False
default dallas = False

default persistent.the_real = False
default persistent.relationship = "friends"
default persistent.leah_rel = "friend"
default persistent.byron_rel = "friend"

#Mono Code Unlock Variable Set
default persistent.monoUnlock = False

#Acts Unlock / Locked
default persistent.actOne = True
default persistent.actTwo = False
default persistent.actThree = False
default persistent.actFour = False
default persistent.actFive = False
default persistent.actSix = False
default persistent.actSeven = False
default persistent.whatif = False

#Scenes Unlocked / Locked

default persistent.showme = False
default persistent.experimentation = False
default persistent.bunnygirl = False
default persistent.playhard = False
default persistent.lovefordallas = False
default persistent.closeyoureyes = False
default persistent.ninjina = False
default persistent.darkwhisper = False

default persistent.medusaboobs = False
default persistent.nakedman = False
default persistent.actitout = False
default persistent.goodvibrations = False
default persistent.likeitrough = False
default persistent.considerablegirth = False
default persistent.mre = False
default persistent.bunked = False

default persistent.pastthepanic = False
default persistent.meetthepussy = False
default persistent.rodehard = False
default persistent.alltheway = False
default persistent.twowet = False
default persistent.cosplay = False

## Screen Text Box Opacity Variable

## Customizing text for easier reading.
style say_label:
    font "georgia.ttf"
    size 55
    kerning 2
    outlines [ ( 3, "#000000", 0, 0) ]
style say_dialogue:
    font "georgia.ttf"
    size 42
    kerning 2
    outlines [ ( 3, "#000000", 0, 0) ]


screen choice_menu():

    tag menu # This ensures that any other menu screen is replaced.


    #Imagebutton code
    imagebutton auto "images/choiceone/octaviachoice_%s.webp" xpos 1100 ypos 0 focus_mask True action [ SetVariable("WhichGirl","octavia"), Jump("library_research") ]
    imagebutton auto "images/choiceone/dallaschoice_%s.webp" xpos 300 ypos 0 focus_mask True action [ SetVariable("WhichGirl","dallas"), Jump("computer_research") ]


# The game starts here.

label start:
    $ game_new = True

    stop music fadeout 1.0

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene 2myraintro with fade

    play music "audio/something_good.mp3"

    m "Hi there!"
    m "I'm Myrabelle and I'm here to be your guide before you get started!"

    scene 3myraintro with dissolve

    m "We'd like to warn you beforehand that there are moments in Avalon
    that can be rather dramatic."
    m "But this story is more than just drama. It's also wholesome, romantic, and humorous."
    m "If you invest in the characters, we promise you'll find a lot to love here."

    scene 5myraintro with dissolve

    m "All the characters in Avalon are over the age of eighteen."
    m "We don't condone incest or sexual relations with minors."
    m "No animals were harmed while making Avalon; real or otherwise!"

    scene 4myraintro with dissolve

    m "Let's name the main male character."
    m "By default, his name is Byron. You can just press 'Enter' to keep his
        default name."

    $ player_name = renpy.input("主角的名字？")
    if player_name.strip() == "":
      $ player_name = "Byron"

    m "Alright, we'll call the main character [player_name]!"

    scene 3myraintro with dissolve

    m "There are two types of choices in Avalon; {b}Game Altering{/b} and {b}Additional Dialogue{/b}."
    m "{b}Game Altering{/b} choices will fundamentally change the game. We'll be
    transparent about exactly what these choices do when you encounter them."
    m "There are four total paths in Avalon. Act One will offer a choice between
        one of two side characters; Dallas or Octavia."
    m "And Act Three will offer the choice of either a Polyamorous Relationship or a
        Monogamous Relationship."
    m "We recommend the Polyamorous Path first as it offers the most content."

    scene 4myraintro with dissolve

    m "{b}Additional Dialogue{/b} choices just add fun alternatives to some of the character's speech."
    m "They will not alter the game in any significant way."
    m "We'll have the choices marked appropriately as you play."
    m "There are no wrong choices and no game overs."

    scene 5myraintro with dissolve

    m "After you finish each Act, the next Act will be unlocked in the Act Select menu."
    m "Without further ado, please enjoy Avalon!"

    stop music fadeout 2.0

    scene myrabellelockheart with fade
    pause
    scene avalon with fade
    pause
    scene avalonactone with dissolve
    pause

    scene 1a with fade
    pause

    play sound "audio/cellvibe.mp3"

    scene 2a
    pause

    scene 3a

    b "Ugh..."

    scene 4a

    stop sound

    b "Erhm.. Hello?"

    play music "audio/evil_aliens.mp3"

    sh "[player_name]?"

    b "No, this is [player_name]'s message inbox."
    b "Leave a message after--"

    sh "Listen, Moron, Avalon and I argued last night.
        I heard her sneak out a while ago."

    b "So call the police."

    sh "She's an adult now, [player_name]."
    sh "If she wants to leave the house at three o'clock in the morning
        and go stay at a rundown, shithole motel, that's up to her."

    b "How do you know she's at a motel?"

    sh "It's called technology, Meathead.
        I tracked her phone with GPS."
    sh "[player_name], I'm done dealin' with this shit. I did my job as a parent.
        She's eighteen and still alive."
    sh "Whoopdy fuckin' do."

    b "That's messed up, Sharol."
    b "Why are you calling me then?"

    sh "Ever since I stabbed you in the leg with a pen,
        you've been avoiding me."

    b "Because you stabbed me in the leg with a pen."

    sh "I know you haven't seen Avalon in a while because she's a selfish little brat
        and doesn't care about anyone but herself."
    sh "But I also know you still love her so if you want to be her
        knight in shining armor, or whatever, she's at Motel 99."

    b "You've got to be kidding me. You're dumping your daughter off on me?"

    sh "It's your choice, [player_name]. You can help her or not."
    sh "I don't give a fuck what you do. The motel is ten minutes away from you."
    sh "You can help her out or let her rot. Either way, she ain't welcome here anymore."

    b "Sharol, you can't just--"

    stop music fadeout 1.0

    "*Click*"

    bi "{i}Of course she would hang up on me.{/i}"

    scene 5a

    bi "{i}Obviously I'm going to go get her.
        I can't let her stay at a motel. Especially that one.{/i}"
    bi "{i}A place like that could traumatize a young woman.
        A place like that could traumatize me!{/i}"

    scene 6a with fade

    bi "{i}Ack! This is certainly the place but it smells awful here.{/i}"
    bi "{i}This place must be downwind from a sewage treatment plant.
        Ugh! I'll have to move quickly before the nausea takes hold. {/i}"

    scene 7a

    bi "{i}Hmm. I could head to the main office. Or...{/i}"
    bi "{i}There's only one room light on. I'll check that out first. {/i}"

    scene 8a

    bi "{i}I don't want to get stabbed here today. {/i}"
    bi "{i}If I find Avalon quickly enough, maybe I can leave here without being
        mugged... {/i}"
    bi "{i}I can't believe she would come to a place like this.{/i}"
    bi "{i}Maybe she had nowhere else to go. This place is disgusting but it's cheap. {/i}"
    bi "{i}It's probably the only room she could afford. {/i}"

    scene 9a

    bi "{i}There she is! {/i}"
    bi "{i}I wonder what's with the goth look? And what is she doing? {/i}"
    bi "{i}It looks like she is just sitting there all frowny faced,
        staring at a TV that isn't even on. {/i}"

    scene 10a with dissolve

    play music "audio/no_goodbyes.mp3"

    b "Knock knock!"
    b "Hey, Snotnapkin! What're you doin'?"

    scene 11a with dissolve

    a "Ah!"

    b "It's just me, Doofus."
    b "Come on, let's get out of here before the roaches carry us away."
    b "They probably have a whole roach lair underneath this place. It's probably
        terrifying!"

    scene 12a with dissolve

    a "Go away!"

    b "Did you just turn away from me? Seriously??"
    b "I'm here to save you from the awful wallpaper that is infesting that room."
    b "I mean, seriously, look at it."
    b "It looks like someone just took a turd and
        smeared it all over the wall in a hideously absurd pattern."

    a "I don't need your help. Just go home."

    b "Let me tell you how this is gonna go down, Missy."
    b "I'm going to start singing Justin Bieber as loud as I can and
        I'm not going to stop until you come out of that room."

    a "You wouldn't..."

    scene 13a with dissolve

    b "Despacito!"
    b "Quiero respirar tu cuello despacito,"

    a "That's not even Justin Bieber!"
    a "He just weaved some of his lyrics into someone else's work!"

    b "Don't care."

    scene 14a with dissolve


    b "Deja que te diga cosas al oído,"

    a "Ugh! Please stop!"

    scene 13a with dissolve
    b "Para que te acuerdes si no estás conmigo,"

    a "How do you even know this terrible song?"

    b "I studied it so I could annoy people with it."

    scene 14a with dissolve

    b "Despacito!"

    scene 15a with dissolve

    a "Okay! Jesus."
    a "Just stop! I'll come out..."

    b "Attagirl."

    scene 16a2 with fade

    a "Hey, Uncle [player_name]."
    a "Look, I'm fine here. I don't need your help."

    scene motelbyronsmile

    b "Oh, you frequent places like this?"
    b "You're just a regular ol' tourist traveling the land in search of adventure?"

    scene 16a2

    a "Just leave me alone..."

    scene motelbyronfrowning

    stop music fadeout 1.0

    b "I just had a conversation with your vile mother
        and I'm at a motel that smells like the devil's crotch."
    b "You can give me five minutes, can't you?"
    b "We can even talk here if you want."

    scene 16a2

    a "Ugh. Fine, whatever. Don't try to convince me to go back home though!
        I'm not going!"

    scene 5motel with fadefast

    play music "audio/a_way_out.mp3"

    b "So you and your mom had a disagreement?
        It must have been bad if it drove you from home."
    b "What happened?"

    scene 2motel

    a "She keeps bringing guys home. And they're gross!"
    a "They say nasty things to me sometimes and they're always walking
        around half-naked."
    a "I just couldn't take it anymore, Uncle!"
    a "I told her that it has to stop. She can't do it anymore!"

    scene 1motel with dissolve

    a "But she just started yelling at me!"
    a "So I started yelling back. I called her a dumb slut."
    a "And then she said she wishes I'd never been born."

    scene 5motel

    b "Ouch. Yes, that does sound like something drunken Sharol would say."
    b "She couldn't survive without you, Avalon."
    b "You cook her meals, clean the house. Somebody would have found her passed
        out and drowned in the tub if it wasn't for you."
    b "She doesn't wish that you were never born, you know that."
    b "But... I get it. I do. That would be a terrible thing to hear."

    scene 6motel with dissolve

    b "Your mom is a functional alcoholic and a harlot. She has been for fifteen years."
    b "I know it's not news to you but maybe hearing it out loud will bring some clarity."
    b "She doesn't give a shit about anyone but herself. She can't help
        but forever wallow in her own self-pity."
    b "When your father passed, she couldn't handle it. She couldn't recover."


    scene 5motel with dissolve

    b "Listen to me, I can't help your mom. I doubt that anybody can. Her only comfort is the bottle."
    b "I hope I'm wrong, I really do. But if the last fifteen years have taught me anything,
        it's that she isn't going to change."
    b "But you, Avalon. I can help you."

    scene 2motel

    a "I can take care of myself! I don't need your help..."

    scene 7motel
    b "You're staying at a No-Tell Motel, Avalon!"

    a "W-what's that?"

    b "It's a motel where men bring whores. It's a dirty, filthy place that you
        should never have to lay eyes on!"
    b "You cannot make it out in the world with the clothes on your back
        and a couple of bucks in your pocket."

    scene 6motel with dissolve

    b "I ain't sayin' you gotta stay with me forever. Let me just give you a leg up."
    b "I'll let you have the guest room at my place.
        It's always been your room anyway. I haven't changed it."
    b "And tomorrow, I can help you find a job if you want."
    b "Once you have a steady paycheck, we'll find you your own place."

    scene 1motel

    a "I have more than a couple of bucks! I've got like, $44 I think..."
    a "And some change, too!"

    scene 8motel

    b "I've got $44, I think."

    scene 6motel with dissolve

    b "That's what you sound like."

    scene 4motel

    a "Okay, Butthead, I get it. I need a little help."
    a "I didn't have any of this planned out before I left."
    a "I probably should have packed a few bags or something..."

    scene 2motel with dissolve

    a "I'll take you up on your offer but I'm going to pay you back!"

    scene 8motel

    b "I'm Avalon and I'm going to live under a bridge like a troll."
    b "'Cause I'm a rebel now and I don't need anyone!"

    scene 4motel


    a "Stop mocking me. You look dopey enough without contorting your face like that."
    a "And I'm not saying I couldn't have figured things out for myself!"

    scene 1motel with dissolve

    a "I haven't seen you in a long time. I'm not even sure I know who you are anymore."
    a "But helping me out like this... I guess you haven't changed, huh?"
    a "Thank you for coming, Uncle [player_name]."

    scene 5motel

    b "You're welcome, Avalon. It's nice to see you again. You're right, it has been a while."
    b "Enough with the sentimental crap. Come on, get your shit."
    b "Let's get outta here before we get shot. Or mugged. Or... shugged?"
    b "You know, a combination of shot and mugged..."


    a "Swing and a miss, Uncle."

    stop music fadeout 2.0

    scene 17a with fade

    b "Come inside quickly, Avalon. Before the sun comes up and you melt."
    b "Because apparently, you're a vampire now."
    b "Seriously, what's with the goth look all of the sudden?"

    scene 18a with dissolve

    play sound "audio/doorclose.mp3"

    b "You used to be a preppy cheerleader who loved pink kittens and
        had perfume flatulence."
    b "What happened?"

    scene 19a with dissolve

    a "I just felt like a change. I got tired of being the preppy cheerleader."
    a "Everyone always expected me to be upbeat and happy."
    a "I didn't want those expectations looming over me anymore."
    a "So I changed my appearance to look... more the way I feel."

    scene 18a with dissolve

    b "That sounds a bit dramatic. But fair enough!"
    b "I would love to hear more about your little Avril Lavigne transformation
        but I have to get some sleep."
    b "I'm sure you remember where your room is. We can talk more after we get some
        rest."

    scene 21a with dissolve

    b "So give me a hug and I'll see you tomor--"

    scene 22a with vpunch

    a "{b}Don't touch me!{/b}"

    scene 23a

    play music "audio/flight_path.mp3"

    b "Whoa."
    b "T-take it easy, Ava. I was just saying goodnight..."
    b "I didn't mean any harm."

    scene 24a

    a "I... I'm sorry. I didn't-- I shouldn't have--"
    a "I'm so sorry."

    scene 25a

    b "It's fine. I'm sorry too."

    scene 26a with dissolve

    b "Goodnight."

    scene 27a with fade

    bi "{i}I have a memory of a time my friend wanted to show me his 12 gauge shotgun. {/i}"
    bi "{i}He said I should try it out and take a shot at a pumpkin he'd sat atop a fence post.{/i}"
    bi "{i}I remember the weight of it, the feel of the cold steel and the smell
            of gunpowder.{/i}"
    bi "{i}I took aim, cocked the shotgun, and fired. {/i}"

    scene 28a with dissolve


    bi "{i}I thought I knew what to expect after seeing action movies on TV but I was wrong.{/i}"
    bi "{i}The concussion shook my entire body and the recoil threw me off balance. {/i}"
    bi "{i}I toppled backward and fell to the ground. {/i}"

    scene 29a with dissolve

    bi "{i}My friend laughed without pause. {/i}"
    bi "{i}I just laid there as the shock had me paralyzed. {/i}"
    bi "{i}The surprise of it all, the loud, unexpected bang and the violent, harsh recoil locked up my whole body. {/i}"
    bi "{i}Avalon's scream took me right back to that moment. {/i}"
    bi "{i}The surprise and passion of her reaction trapped me in a daze. {/i}"
    bi "{i}I felt completely stunned, just like when I fired that shotgun. {/i}"
    bi "{i}And the worst part is that I knew exactly why she reacted that way... {/i}"

    stop music fadeout 2.0

    scene recoveryqoute with fade
    pause (5)

    scene 30a with fade

    a "Uncle [player_name]?"

    scene 32a

    a "Um.. Uncle [player_name]?"

    scene 33a

    b "Ehm.. Wha-- Oh. Good morning, Avalon. Did you sleep alright?"

    scene 32a

    a "Not really. I thought a lot about what happened last night."
    a "I shouldn't have yelled at you. I don't know what came over me."
    a "Did you... did you sleep on the couch because of me? Because I shouted at you?"

    scene 33a

    b "You shook me up pretty good. I'm a big guy, not many people can rattle me."
    b "But that shout last night sure did catch me by surprise!"
    b "Are you part barbarian? Because I seriously felt the ground shake."
    b "I'm pretty sure there's a crack in the entrance hallway mirror."

    scene 34a

    a "I know you're just joking around but I am sorry. You didn't deserve that."
    a "If I upset you, I can leave. I can go back to the motel. I wouldn't blame you
        if you wanted me to go."

    scene 35a

    b "I don't want you to leave. I forgave you the moment you shouted at me."
    b "Avalon, I'd like to tell you a story. Would you sit with me?"
    b "It won't take long, I promise."

    a "Um... Okay. Sure."

    scene 37a with dissolve

    play music "audio/touching_moment.mp3"

    b "When I was in high school, there was this girl in some of my classes. I had
        a huge crush on her."
    b "She approached me one day out of the blue. I couldn't believe my luck!"
    b "I have to assume she was confused about who I was because she asked me to show
        her how to skateboard."
    b "I'd never even been on a skateboard. But like hell if I was going to tell her that!"

    scene 38a

    a "Wow, she asked you for lessons? She must have been desperate."

    scene 37a

    b "Storytime means I tell the story and you be quiet."

    a "Fine, fine. Continue."

    b "Well, she was struggling to put her second foot up on the board."
    b "She was wobbling like a bounce-back clown. It was quite hilarious."
    b "But when I went to put my hand on her back to help her balance, she..."

    scene 39a with dissolve

    b "She snapped at me. Just like you did last night."
    b "And I remember being so angry at her. I couldn't believe she would shout at me like that."
    b "I felt offended and angry and just... so upset."
    b "I avoided her for days after that. I wanted nothing to do with her."

    scene 40a with dissolve

    a "I'm sorry, Uncle. I really am! I didn't mean to do it."
    a "Do you want nothing to do with me now? Just like you didn't want anything
        to do with her..."

    scene 39a

    b "I would never abandon you as I did her, Avalon. In fact, I've regretted
        that decision ever since. I should have helped her."
    b "I found out later that she was assaulted. I didn't get all the details but
        I know she was assaulted... sexually."
    b "She went to a party and some guy took advantage of her while she was intoxicated."

    scene 40a

    a "That's terrible. Do you know if she ever recovered?"
    a "Did she ever get better? Can you be fixed when something like that happens?"

    scene 39a

    b "I don't know if she got better or not. Graduation was a few days later and
        I never saw her after that."
    b "I do know they caught the guy that did it. He was sentenced to five years in prison."
    b "I heard a rumor that he was murdered in his jail cell."
    b "I've felt so guilty over the years for abandoning her and even more
        guilty because I never attempted to repair our relationship."


    scene 41a with dissolve

    b "But I swore I'd never make that mistake again."
    b "And I'm sure as hell not going to make that mistake with you."
    b "So I need you to tell me, Avalon..."
    b "Who hurt you?"

    stop music fadeout 2.0

    scene 40a

    a "I can't-- I don't want to talk about it."

    scene 43a with dissolve

    a "I have to go!"

    scene 44a

    bi "{i}Well, now I know for sure. She's been sexually abused.{/i}"
    bi "{i}All this time I spent apart from her... I should have been there to stop it!{/i}"
    bi "{i}I've got to help her but she's not comfortable enough to talk to me about it yet. {/i}"
    bi "{i}It's been so long since I've seen her that she doesn't trust me anymore. {/i}"
    bi "{i}I may not have been able to repair my relationship with that friend of mine but
        I have to with Avalon. I have to!{/i}"
    bi "{i}I think it's time to do some research. {/i}"

    scene skybg

    m2 "This next choice will determine the main secondary potential love interest in Avalon."

    show dallaschoice_idle at center with dissolve

    m2 "This is Dallas! She's been Avalon's best friend for most of her life."
    m2 "Dallas is a feisty and flirtatious young woman. She's a strong, hardworking
        gal and a lot of fun!"
    m2 "Choose this path if you would prefer a more humorous path."

    hide dallaschoice_idle

    show octaviachoice_idle at center with dissolve

    m2 "This is Octavia! She's a captivating yet mysterious woman."
    m2 "Octavia is gentle, observant and extraordinarily maternal."
    m2 "Choose this path for a slightly more story-driven experience."

    hide octaviachoice_idle

    m2 "Time to choose!"

    ## This is the first decision of the game. This will decide if our second
    ## character is Octavia or Dallas.
call screen choice_menu()

label library_research:

    $ octavia = True

    scene 50a with fade

    bi "{i}Wow, it has been a long time since I've been in here. It's bigger than I remember. {/i}"
    bi "{i}There are books shelved up to the ceiling!{/i}"

    scene library

    bi "{i}It's practically devoid of people though.{/i}"
    bi "{i}With the rise of digital libraries and e-books, I guess reading
            paper and ink is becoming less popular.{/i}"
    bi "{i}Still, virtual libraries certainly don't have a magnificent
            presence quite like this. {/i}"

    scene 51a

    b "*Sniff* *Sniff*"

    scene 52a with dissolve

    b "Bleh!"
    bi "{i}I really should have taken a shower before I left. {/i}"
    bi "{i}And changed clothes. {/i}"

    scene 51a with dissolve

    b "*Sniff* *Sniff*"

    scene 52a with dissolve

    b "Ugh!"
    bi "{i}I might actually have to burn these clothes. {/i}"

    scene 53a

    bi "{i}Let's see if we can find some assistance. There's a woman over there.{/i}"
    bi "{i}Judging by that classic librarian outfit, I'd wager she works here. I'll ask her for help.{/i}"
    bi "{i}I'd be here for days searching for a book otherwise. The Dewey Decimal System is a joke...{/i}"

    scene 54a

    bi "{i}Oops! I may have gotten a little too close here. I can see right up her skirt at this angle. {/i}"
    bi "{i}Are those granny panties? I didn't know people still wore those!{/i}"
    bi "{i}Not exactly fashionable or trendy, but maybe they're really comfortable? {/i}"
    bi "{i}Gah! I can't just stand here having a conversation with myself in my head,
        especially looking up her skirt like this. {/i}"
    bi "{i}I have to say something. {/i}"
    b "Excuse me!"
    bi "{i}Shit, that was louder than I meant. I hope I didn't--{/i}"

    scene 55a

    o "Woah...!"
    o "Oh no!"

    scene 56a

    o "Ahh!"
    bi "{i} Oh shit, she fell! {/i}"
    bi "{i} I shouldn't have shouted! {/i}"
    bi "{i} Why the hell would I shout in a library? {/i}"
    bi "{i} If I position myself just right, I should be able to... {/i}"

    scene 57a with hpunch

    o "Oof!"
    b "Gotchya! That was quite a fall. I'm glad I was here to catch you!"
    b "While I have you here, I was hoping you could help me find a book on rape?"

    scene 58a with dissolve

    o "W-what?!"
    o "Please put me down!"

    b "Oh, of course!"
    b "Here you are..."

    scene 59a with fadefast

    o "I appreciate you catching me but I wouldn't have fallen at all if you hadn't
        shouted."
    o "Please be more careful in the future."

    b "I'm truly sorry."

    o "Umm, tell me again what you're looking for?"

    scene 64a

    b "My niece was sexually assaulted and I'm not sure how to help her."
    b "There must be literature on the subject, right? Could you help me find something
        I could read to educate myself?"
    b "I want to help her."

    scene 59a

    o "Oh, I'm sorry to hear that."
    o "But in the future, maybe don't mention rape when you're holding a girl
        tightly in your arms..."
    o "You wouldn't want people to think you're a pervert, would you?"

    scene 63a

    b "That is sound advice! Out of context, I could see how that question might be unusual.
        And frightening..."
    b "I apologize. Can we start over? I'm not usually like this, I think you
        just caught me off guard."

    scene 60a

    o "It's alright. I say things absent-mindedly sometimes too."
    o "I don't mean to toot my own horn, but I know a few things about
        psychology and recovery."
    o "I've had some experience with helping people recover too!"

    b "Oh, are you in college?"

    scene 59a with dissolve

    o "No. I studied psychology on the side as a hobby."
    o "But I am very knowledgeable on the subject."

    scene 64a

    b "I'm sure you know more than I do. Would you mind if I pick your brain?"
    b "I have absolutely no idea how to help my niece, but I'm desperate."
    b "Any advice at all would be a tremendous help."

    scene 62a

    o "I wouldn't mind at all. I'd be happy to help!"
    o "How about we discuss it over lunch? There's a diner down the street."
    o "Would you like to have coffee with me?"

    scene 64a

    b "That sounds great. And it's on me, I insist!"
    b "I'm [player_name], by the way."

    scene 62a

    o "I'm Octavia. It's a pleasure to meet you."
    o "I have to wrap up a few things here. Can I meet you there in twenty minutes?"

    scene 64a

    b "Sure, I'll see you there."

    scene 1cafe with fade

    play music "audio/tomorrows_rain.mp3"

    b "So my phone rings at three o'clock in the morning."
    b "I reluctantly answer it. To my surprise, it's my sister Sharol."

    scene 5cafe

    o "Biological sister?"

    scene 3cafe

    b "Uhh, actually, no. I was adopted by her parents when I was five."
    b "I don't remember my biological mother, but I know I was with her until then."
    b "Frank and Wendy were my adoptive parents. They didn't seem to have much
        time for Sharol and I when we were growing up."
    b "How could you tell I was adopted?"

    scene 7cafe

    o "If I told you, it would freak you out. I don't want to make a bad impression
        during our first get-together."
    o "I assure you, it's not that interesting anyway. I'd bore you with the
        details."
    o "We should focus--"

    scene 1cafe

    b "Nope. Now I have to know. You've piqued my interest!"
    b "And you could not possibly bore me. I'm simple and easily amused. It's my
    best quality, actually!"

    scene 7cafe

    o "You're not simple. I can tell that already. But easily amused, perhaps."
    o "I really shouldn't explain this to you. If you're insistent though, I will."
    o "As long as you promise not to run for the hills!"

    scene 1cafe

    b "I've got my running pumps on today so... no promises."

    scene 6cafe

    o "You jest but I'm serious."

    scene 5cafe with dissolve

    o "You came alone to the library which on its own wouldn't be unusual."
    o "But you also didn't shower today. I can tell by your odor."
    o "It's pungent enough that you perhaps didn't shower yesterday either."
    o "Putting aside my deduction for a moment, you need to shower more.
        Hygiene is important, [player_name]."

    scene 3cafe

    b "I know! I almost made my dumb self pass out earlier when I sniffed
        my armpit. I usually don't forget deodorant when I go out. Honest!"
    b "I hope it's not unbearable. I'm desperately sorry!"

    scene 6cafe

    o "There! That too!"
    o "I'll get to that in a moment! But for now, let me continue."

    scene 5cafe with dissolve

    o "You're used to being alone, hence the reason you didn't shower today."
    o "You probably didn't even think about it because you're not used to being around people."
    o "Independence can be a classic sign of an adoptee."
    o "You're very apologetic, which strongly suggests that you need people to like you."
    o "And it looks like you've put a lot of effort into exercising."
    o "You've grown a beard in a time when it's becoming much more popular and accepted."
    o "And you have auburn hair naturally but it's slightly more dramatically red closer to the root,
        which means you dye your hair to make it less noticeably red."
    o "Redheads often get teased and can be thought of as outsiders, so I assume you dye it
        to be more accepted by society."
    o "I'd wager you've done all these things to fit in better and you're striving for acceptance."
    o "Now, all these things together don't necessarily mean you were adopted, but they're good indicators."

    scene 2cafe

    b "That was incredible! You might know me better than I know myself."
    b "And we've only just met!"
    b "I would run but my jaw is firmly planted on the floor right now."

    scene 6cafe

    o "I knew I should have made you promise you wouldn't!"

    scene 1cafe

    b "Octavia, that was genuinely impressive."
    b "Are you a sage? I'd believe you if you said you were!"
    b "I'm absolutely flabbergasted right now."

    scene 7cafe

    o "Thank you. I've had some training in observation and psychoanalysis."
    o "I see things others often wouldn't and can break those observations down into
        useful information."
    o "Consequently, I can quickly exhaust my interest in things because I unravel their
        mysteries too quickly and become bored with them."

    scene 3cafe

    b "I imagine that includes people. I'll try not to bore you, Octavia."
    b "But honestly, I'm not sure I can keep up with your spectacular intellect."
    b "I wouldn't consider myself an idiot, but perhaps right at average."
    b "You're clearly a cut above!"

    scene 5cafe

    o "No, really, I'm not--"

    scene 8cafe

    w "Excuse me, I apologize for making you wait. I'll be your waitress for today."
    w "What can I get you? A menu first, perhaps?"

    scene 9cafe

    b "Just coffee for me. Light creme, no sugar. Oh! And one of those, um, cute
        little straws!"
    b "I just think those things are cute as hell."
    b "You can't always tell by listening to me but I'm totally straight."

    scene 10cafe

    o "I'll have the same. Hold the straw."

    scene 8cafe

    w "Okay, I'll have that out right away! And if you need anything at all, just
        wave and I'll be here in no time."
    w "Seriously, anything at all! I'll be here in two shakes!"

    scene 7cafe

    o "Hrm. She seemed desperate to serve you today."
    o "It wasn't attraction she was feeling towards you though. She just wants your approval."
    o "Is there a story here?"

    scene 3cafe

    b "Well, it's not a story so much as it is that I left a rather large
        tip the last time I was here."

    o "Oh?"

    b "Yeah, well, I leave a large tip every time."
    b "I watched a documentary on restaurants once and it was mostly about how
        waitresses rely on tips to make a living."
    b "That has to be rough most days, right? Relying on the good nature of other
        people?"
    b "I just want to do my part."

    scene 5cafe

    o "And you've made enough money that you don't have to work."
    o "So you can leave large tips like that."

    scene 2cafe

    b "Wow, you can tell that too!?"
    b "I don't even wanna know."
    b "That's a lie, tell me!"

    scene 6cafe

    o "Well it's Tuesday and you're not working. Someone unemployed, with expenses
        and a mortgage, wouldn't leave a large tip."
    o "You either live with your parents or you've got a nice nest egg set up
        so you don't have to work right now."
    o "And since we've established how independent you are, I assumed the latter."


    scene 3cafe

    b "That one was less impressive."

    scene 5cafe

    o "Some things are more obvious than others, Mr. [player_name]!"
    o "But let's get back to your story. I'm curious to know more about you."
    o "Is there anything more you can tell me about your parents?"
    o "And are you close with your sister, Sharol?"

    scene 3cafe

    b "I guess I should start with my adoptive parents then. They were in
        their mid-forties and wanted another child."
    b "But they decide the risk of having a child with defects was too
        high due to their age."
    b "At least, that's what they told everyone."

    scene 5cafe

    o "But the truth was..?"

    scene 1cafe

    b "I think they were afraid of having another child like Sharol."
    b "She was manipulative and apathetic. Unusually so."
    b "I always got the impression that Frank and Wendy didn't like her."
    b "They would never admit it. Who would tell people they don't like their own
        child, right?"

    scene 3cafe with dissolve

    b "There was just something not right about her and there never has been."
    b "Frank and Wendy wanted a normal kid. At least, that's the impression I got
        when they spoke about my adoption."
    b "They didn't want to risk their genetics producing another... Sharol."

    scene 5cafe

    o "Do you believe she may have a disorder?"
    o "Perhaps she is a sociopath?"

    scene 3cafe

    b "I can't say for sure but I don't think so."
    b "When she married to Avalon's father, she seemed... better."
    b "When he was with her, she was tolerable. Sometimes even pleasant."

    scene 7cafe

    o "Love can change a person, Mr. [player_name]."
    o "Perhaps she doesn't have a psychological disorder.
        There could be thousands of reasons for her behavior."
    o "Let's get back to Avalon. What happened there?"

    scene 2cafe

    b "Right!"

    scene 4cafe

    b "Well, Sharol tells me her daughter, Avalon, ran away."
    b "So I go find her, bring her back to my place and I say good night to her."
    b "When I went to give her a hug--"

    scene 5cafe with dissolve

    o "She flipped her lid, didn't she?"

    scene 2cafe

    b "Yes! It was quite terrifying!"
    b "She shouted at me and it felt like a foghorn just rattled my soul!"
    b "I've spent time with Avalon in the past. I love her."
    b "But I have never heard her scream like that at anyone."

    scene 5cafe

    o "That is a classic reaction from someone who has been sexually abused."
    o "My recommendation would be to try to find some common ground.
        Do something together that you both enjoy."
    o "Be there for her when she's ready to talk but don't force it."

    b "Okay, that seems like great advice."

    scene 7cafe with dissolve

    o "Rape victims often feel a loss of control and they need to regain that control."
    o "Let her take the reigns when you can. Don't confine her or force her to do anything."

    scene 1cafe

    b "Okay, wow, that sounds reasonable as well."
    b "A therapy session this good must be expensive. How much am I going to owe you?"

    scene 7cafe

    o "Oh, I don't know if you can afford my fee even as well off as you are."
    o "Perhaps you would allow me the pleasure of your company again?
        Shall we plan another date?"

    scene 3cafe

    b "Oh, a date? Well, Octavia, you seem like a person that's out of this world."
    b "And I mean that in the best way. So I'd be interested in spending more time with
        you. No question!"
    b "But as for dating, I want to focus on Avalon right now..."

    scene 1cafe with dissolve

    b "Would you mind if we all did something together?"

    scene 7cafe

    o "Sure! That sounds great. She's more likely to open up to a female acquaintance anyway."
    o "And if she's even half as entertaining as her Uncle, I'm sure I'll adore her!"

    scene 2cafe

    b "You flatter me! Stop it. Stop it some more."

    o "You goof."

    b "Let me put your number into my phone and I'll text you tomorrow."

    stop music fadeout 2.0

    jump night_one

    label computer_research:

    $ dallas = True


    scene 70a with fade

    bi "{i}Where do I even start?{/i}"
    bi "{i}'How to help a victim of sexual assault?'{/i}"
    bi "{i}'Getting someone to open up about a horrific ordeal?'{/i}"

    scene 71a with dissolve

    bi "{i} Let's try 'How to help someone recover from a traumatic event.'{/i}"

    bi "{i}Ah, here we go. There's a lot of information here but to start with... {/i}"
    bi "{i}'To get someone to open up to you, don't force them to speak but be available to them.' {/i}"
    bi "{i}'Find something you both like and share an experience. They will be
        more likely to open up if they are comfortable.' {/i}"
    bi "{i}'A typical side effect of sexual abuse is the feeling of a loss of control.'{/i}"
    bi "{i}Okay, sounds reasonable! First, I'll let her know I'm here if she needs me. {/i}"
    bi "{i}And then I'll try to socialize with her through similar interests
        and allow her to be in control when I can.{/i}"

    play sound "audio/doorbell.mp3"

    "*Ding dong*"

    scene 72a

    bi "{i}The doorbell? Who could that possibly be?{/i}"

    scene 83a with fade

    bi "{i} Hm? I hear voices. One is Avalon, so I guess she got the door.{/i}"
    bi "{i}And the other is familiar. Could it be..?{/i}"
    scene 81a

    a "Thanks for coming! I know you've been working a lot lately."
    a " I didn't pull you away from anything, did I?"
    a "I just... I could use a friend right now."

    scene 82a

    d "Work has been crazy lately. Everyone is on edge for some reason! I've been
        thinking about taking some time off."
    d "And you know I always have time for you, Dingbat. You just need to call more!"
    d "What's been goin' on? Why are you at your Uncle's place?"

    scene 83a

    bi "{i}Oh man, it's Dallas! She's an absolute wildcard! I spent some time
        with her when she used to hang out with Avalon years ago.{/i}"
    bi "{i}She was a cheerleader with Avalon at the time. Dallas has been a loyal
        friend to her most of her life.{/i}"

    scene 86a with dissolve

    bi "{i}I'm not usually one to eavesdrop, but I might get some valuable information here. {/i}"
    bi "{i}Perhaps a tiny bit of subterfuge will be more helpful than harmful. {/i}"

    scene 81a

    a "I argued with my mom. I ran away from home and [player_name] came to my
        rescue."

    scene 84a with dissolve

    a "She's just been so terrible lately. I can't stand all the gross guys she
        brings home!"
    a "Especially after... you know."
    a "I can't move on from what happened to me. I'm getting worse."
    a "I wake up drenched in sweat, shaking and scared. I never want to leave the house..."
    a "I don't want to be like this anymore..."

    scene 85a

    d "You've got to let people in, Avalon. What happened was awful but you can get better."
    d "I'm not saying what happened to me was the same. Not even close. But it was similar."
    d "I recovered when I let people in and started talking through the event. You have
        to do the same."
    d "We'll spend more time together. Okay? We'll get you through this."

    scene 86a

    bi "{i}Dallas was sexually assaulted too? I can't even imagine that.{/i}"
    bi "{i}She's a tough cookie, probably the strongest woman I've ever met. If someone
        attacked her, I'd be willing to bet she made them regret it!{/i}"
    bi "{i}But if Dallas went through something similar then maybe she can help me
        help Avalon?{/i}"
    bi "{i}I'll try to find a moment to sit her down and talk to her about this. I
        wouldn't mind reconnecting with her so this is a good opportunity for that too.{/i}"

    scene 82a

    d "Why are you here though? I thought you and your Uncle had a falling out or
        something?"
    d "He used to hang around all the time and then he was just gone."
    d "Have you tried talking to him about what happened?"


    scene 84a

    a "I haven't talked to him about anything yet. It's been so long since I've
        seen him, things are still kind of... awkward."
    a "He tried to hug me yesterday and I yelled at him. I don't know what
        came over me but he didn't deserve that."
    a "I know he's only trying to help me. I guess I'm just bitter towards men
        in general right now. But he's not 'men', he's... you know, [player_name]."

    scene 82a

    d "Yeah, I remember him being one of the good ones."
    d "With all the horny teenagers we had to deal with, it was nice being around
        a man like him once in a while."

    scene 81a

    a "You like him because he doesn't grab your ass every time you turn around!"

    scene 85a

    d "You say that like you're joking but that's spot on! He was playful but not
        constantly trying to grope me."
    d "Guys that only think with their dicks are, honestly, kind of fucking boring."
    d "[player_name] was fun to be around. And I remember him being supportive
        of you. So yeah, he's got my mark of approval."

    scene 86a

    bi "{i}Gah! I'm going to tear up here. That was so nice!{/i}"
    bi "{i}And now I feel like a complete piece of shit for eavesdropping. I was not
        supposed to hear all that!{/i}"
    bi "{i}Okay, enough subterfuge. It's time to reveal myself and stop hiding like a
        creepy stalker!{/i}"

    scene 83a

    b "Hey, Ava! I thought I sensed the presence of pure evil."
    b "I know you've been into a darker theme lately. Did you start worshipping
        the Dark Lord and summon a demon?"

    scene 89a with dissolve

    b "Ah! Not a demon."
    b "Something much worse!"

    scene 87a

    a "Hey, Uncle [player_name]. You remember Dallas, right?"
    a "I called her and asked her to stop by to visit. We were going to spend some
        time together. Do you mind?"

    scene 91a

    b "Hello, Sorceress. It's been a long time."
    b "If I had known you were coming, I would have prepared a baby kitten for
        you to eat."

    scene 92a

    d "Hey, [player_name]. I don't eat kittens, only scrawny little men."
    d "And it looks like you might be on the menu soon. Have you lost some
        gains, dude?"

    scene 91a

    b "No! You can't even play that card! I'm the biggest I've ever been. Don't call
        me scrawny!"
    b "It sounds like you've gotten considerably more fiendish. As I would have expected."
    b "Have you used your devil magic to turn any guys into toads lately?"

    scene 92a

    d "Why would I turn guys into toads? Aren't I supposed to turn a toad into a prince?"
    d "Weak sauce, [player_name]. You need better material."

    scene 96a

    b "Damn, that's a good point. Why would you want toads hangin' around? That'd be awful..."

    scene 91a with dissolve

    b "So what's with the bomber jacket? Were you a pilot in World War Two?"
    b "I can imagine you terrorizing people from the sky but not in a plane."
    b "Maybe on a broom though!"

    scene 97a

    d "You know, I was going through my concoctions earlier and I found something
        rather special."
    d "It just so happens that I brought it with me today. I think you'll really like
        it, [player_name]."
    d "Do you want it?"

    scene 94a with dissolve

    d "It's just in my back pocket here..."

    scene 91a

    b "What trickery is this, Dallas?"

    scene 96a with dissolve

    b "What's tha--"

    scene 95a

    play music "audio/aint_it_funny.mp3"

    pause

    a "Oh shit. Is that the circle?"
    a "Did you look right at it, Uncle!?"

    scene 99a

    b "Wait a minute, Dallas! Don't do anything crazy!"
    b "I didn't mean it when I called you a witch! I was just messin' around!"

    scene 98a

    d "You know what has to happen now, [player_name]!"

    a "Brace for impact, Uncle!"

    scene 99a

    b "Wait wait!"

    scene 100a

    pause (.5)

    scene 101a

    pause (.3)

    scene 100a

    pause (.5)

    scene 102a

    b "Ow my balls! Goddammit!"
    b "You've got an arm like a boxer, Dallas! Shit!"

    scene 103a with dissolve

    d "I call that 'Circle takes the Square'. Because if you look at the circle,
        I punch you square in the dick."

    b "Ooow! That's so fucked up, Dallas. You went full hay-maker instead of a
        light sack tap! You're the worst!"

    d "You look at the circle, you gotta pay the piper. The bill comes due."

    b "I forgot about the circle game. But now my children will never know about
        the circle game. Because I can't have children now."
    b "You've taken my legacy from me, Dallas. My legacy!"

    d "Don't be so dramatic!"

    a "You'll get her back, Uncle [player_name]. I'm sure of it!"

    d "It's nice to see you again, [player_name]."

    b "The pleasure... wasn't mine. Ugh!"

    scene 104a with dissolve

    a "Is it alright if we hang out here for a while?"

    b "Yeah, sure, whatever."
    b "I'm just going to ice my balls and hope my penis still works."

    scene 105a with dissolve

    stop music fadeout 1.0

    a "Feel better soon, Uncle. And thank you for taking me in."
    a "I'm doing better already."

    b "Uhh... you're welcome, Avalon."

    bi "{i}She just touched my arm? Maybe she's starting to feel more comfortable with me already. {/i}"
    bi "{i}Or maybe it has something to do with Dallas being here..?{/i}"

    scene 107a with fade

    pause (2)

    scene 108a

    d "Hey, Gorilla. Are you passing out?"

    b "No, I was just resting my eyes a bit."

    d "I heard you slept on the couch last night. You're getting too old for that.
        You're going to throw out your back."

    scene 109a

    b "You wound me, Dallas. I'm only twenty-eight!"
    b "By the way, you got some shit on your face."

    scene 108a

    d "Yeah, it's called 'Makeup'. We're girls, [player_name]. We wear makeup sometimes."

    b "Where's Avalon?"

    d "She passed out while we were watching 'The Evil Dead' so I'm going to head home."

    scene 110a

    b "Before you go, do you have a minute? I'd like to talk to you about her."

    scene 111a with dissolve

    play music "audio/disturbed_mind.mp3"

    d "Of course! What's up?"

    b "I have a confession to make before I start."

    scene 9cdallas

    d "You don't know how to work the dials in the shower?"
    d "That would explain why you smell like wet dog."
    d "And all the food and shit in your beard. Do you even wash that thing?"

    scene 6cdallas

    b "I forgot to shower today. And don't talk trash about the beard! I found a skittle
        in it the other day. It was a delicious surprise!"
    b "And at least my hair doesn't look like I've recently been electrocuted."
    b "You've got to stop sticking random things you find into power outlets, Dallas."

    scene 4cdallas with dissolve

    b "Listen, I eavesdropped on your conversation at the front door earlier."
    b "I shouldn't have done it but I thought I might learn something I could use to help Avalon."
    b "I'm worried about her. She's been on edge since I took her in."

    scene 12cdallas

    d "You were eavesdropping? That seems a bit out of character for you."
    d "But I guess I understand. You're curious about Avalon since
        you haven't seen her in a while, aren't you?"
    d "How long were you listening? Did you hear..?"

    scene 5cdallas

    b "I heard you experienced something similar to what happened to Avalon?"
    b "Before you scold me, as you should, I wanted to say that I'm glad you're
        doing better. And I'm sorry whatever happened to you... happened."
    b "You're a tough gal so I know you can handle damn near anything life throws at you."
    b "But still, you shouldn't have to endure stuff like that."
    b "If you don't mind me asking, what happened?"

    scene 9cdallas

    d "Damn, the sincerity is pouring out of you today."
    d "All those big muscles but you're just a big ol' teddy bear!"
    d "Don't worry though, we'll get you on some testosterone supplements and
        turn you into a man, [player_name]. There's still hope for you!"

    scene 5cdallas

    b "You don't have to tell me about it if you don't want to, Dallas."
    b "But deflecting serious inquiries with bad jokes is my department."
    b "Come on, tell me. If it helps, you can pretend I'm your Daddy."
    b "Wait, no, that's--"

    scene 13cdallas

    d "Seriously? You had to make it weird!?"
    d "I'm not dodging the question, I just enjoy teasing you. It's therapeutic for me."
    d "I'll tell you what happened to me, it's not a secret."

    scene 7cdallas

    b "Okay, go on. What happened?"

    scene 11cdallas

    d "My cousin was over at my place one day and we were talking about some sex
        scene in a movie. I can't even remember which one."
    d "He started getting real handsy all of the sudden. Grabbing at me and getting aggressive, you know?"
    d "Eventually, it just went too far. But I couldn't get him to stop."

    scene 12cdallas with dissolve

    d "I told him to knock it off but he was just out of control. He pinned me down and started rubbing himself on me."
    d "Then he started tearing at my clothes and broke the strap on my bra. Once he saw
        my breasts, he turned absolutely savage!"
    d "I finally managed to wriggle a leg free before he was able to get my pants down."

    scene 8cdallas with dissolve

    d "I kicked him so hard in the face, he was out cold. Blood flew so far out of his nose,
     it soaked my wallpaper."
    d "Last I heard, he's got a deviated septum now because I hit him so hard!"

    scene 12cdallas with dissolve

    d "But it messed me up pretty good. The whole event was so bonkers, I couldn't believe it."
    d "It went far enough that I was having nightmares about it."
    d "He didn't rape me, it didn't go that far. But I mean, he would have,
        you know? If I hadn't stopped him..."
    d "I still get nervous sometimes when I'm around guys. I know it's not reasonable
        to think that every guy is going try something like that but..."
    d "I don't know. I can't help it."

    scene 5cdallas

    b "I understand. That's what scares me the most about other people. You just never
        know what they're thinking."
    b "They could have the best intentions or the worst. You can't know what thoughts
    are rolling around in someone else's head."
    b "Did you recover though?"

    scene 8cdallas

    d "I did but I had help, [player_name]."
    d "There was a school counselor that I saw a few times a week for a while."
    d "And, you know, Avalon was there for me too. We started spending more time together
        after that."
    d "But I sought her out because I needed support. She's done the opposite.
        She has shut herself off from people..."

    scene 5cdallas

    b "I did the same thing when I was bullied back in High School. I used to shy
        away from people because... well, people are the ones that hurt me."
    b "I still have the same mentality. Being alone keeps me safe from other people."

    d "That's not healthy."

    b "Probably not. But sexual abuse is worse than what happened to me.
        And from what I gather, something to that degree happened to Avalon."
    b "Will you help me help her? Where do I even start?"

    scene 8cdallas

    d "Of course I'll help! I've been trying myself but..."
    d "I think she needs someone like you that she looks up to. I bet together we could help her."

    scene 4cdallas

    b "Maybe she looked up to me once upon a time but now that we've been apart for so long,
        I'm not sure what she thinks about me."
    b "We used to be so close and I let that bond slip away. I've got to rebuild it
        if I'm going to help her."
    b "Is she bitter that I haven't been around?"

    scene 9cdallas

    d "She would talk about you once in a while after you left. She never made it sound like she
        was mad or bitter towards you."
    d "But what the hell, man!? Where have you been?"
    d "Do you even work? How the hell do you afford this place?"

    scene 1cdallas

    b "I developed and sold a fitness app for a rather large sum of money."
    b "I'm doing quite well for myself now! I don't have to work anymore."

    scene 9cdallas

    d "Wait, how well are you doing exactly? Well enough you could buy a yacht and sink it just for fun?"
    d "Or the kind of well off where you can afford the extra soft toilet paper at the grocery store?"
    d "What's that called? Middle class? Come on, [player_name]. How much money have you got? "

    scene 2cdallas

    b "If I don't buy a yacht like a snobby prick then I could retire right now
        and live off what I have in the bank. But I'd have to be frugal with my money."

    scene 3cdallas with dissolve

    b "Is that a good enough answer for you?"

    scene 10cdallas

    d "My eyes are up here, ya ape!"

    scene 9cdallas with dissolve

    d "You ain't rich enough for me to drop my trousers right here, ya know."
    d "This puss is too expensive for your poor ass."
    d "Maybe you could get a dimestore hooker though."

    scene 5cdallas

    b "Why would you wear something like that if you don't want guys to look?!"

    scene 9cdallas

    d "Oh no, I want you to look but I also want to make you feel guilty for looking."

    b "What the hell? Why!?"

    d "I want people to find me attractive. Doesn't everyone?"
    d "But I don't want you to think I'm easy. I have standards!"
    d "So I wear cute outfits but I remind guys that I'm more than just tits and
        an ass when I feel like I need to."

    scene 2cdallas

    b "So you're putting bait on the hook but you're not going to reel in just any
        ol' bass that goes for it, right?"
    b "I get it. Men are built so they're more attracted to physical attributes
        and you play off that."

    scene 13cdallas

    d "Yup! I know a lot of women like to condemn men for that attribute. But it
        is what it is. I'm not going to rewire men's brains."
    d "And, I dunno, I like being desirable to the opposite sex so I do
        what it takes to be desirable."
    d "In fact, I try to use whatever I have in my arsenal to get the best results
        for myself in all walks of life."
    d "I work hard to get promotions at work, I save up for the things I'd like to buy
        and I exercise for the body I wish to have."

    b "That sounds smart, actually."

    d "I like to think so. Do what it takes to get what you want, right?"

    scene 11cdallas with dissolve

    d "On another note, I have a question for you. Are you related to Avalon?"
    d "I had a class on biology last year and they mentioned some things about genetics."
    d "As far as I can tell, you don't share any genetic features with Avalon. You're
        both different from each other physically."

    scene 5cdallas

    b "I was adopted. Avalon and I aren't related by blood. She calls me her Uncle
        but I'm technically not."

    scene 6cdallas with dissolve

    b "You didn't know that? What the hell, Dallas? How did you not know?"

    scene 8cdallas

    d "Why would I know that? We don't like, hang out and shit."
    d "And even if we did, why would I give a crap if you're adopted?"

    scene 4cdallas

    b "You're saying you don't give a crap if I was adopted but you literally just asked."
    b "I retract my statement earlier about you being smart."

    scene 9cdallas

    d "Alright, you got me there. But there will be plenty of time to get to know each other
        better moving forward. We're going to help Avalon together, right?"
    d "Call me when you're planning to do something with her and I'll join if I can."
    d "Just take a damn shower before we see each other again. And wear deodorant!"

    scene 1cdallas

    stop music fadeout 1.0

    b "Let me get my phone out of my pocket so we can exchange numbers."
    b "It's just right here in my sweater pocket..."

    scene 13cdallas

    d "Sure. Did you change phone numbers?"

    scene 14cdallas with dissolve

    d "If not, I'm pretty sure I still have--"

    scene 15cdallas with dissolve

    d "Is that..? Shit."

    scene 1cdallascircle

    play music "audio/aint_it_funny.mp3"

    pause

    scene 7cdallas

    b "Oh Dallas, you poor sucker. You just messed up so bad."

    scene 16cdallas

    d "Wait, [player_name]. Remember I'm small and fragile!"
    d "You wouldn't hurt a pretty little girl like me, right?"

    scene 17cdallas

    d "Gah! No no, let me go! Ah!"

    scene 18cdallas with dissolve

    d "Oof!"
    d "Okay, [player_name]! You got me! I've learned my lesson!"
    d "And I'm sorry about your balls earlier. There! I apologized!"
    d "You can let me down now, right?"

    b "No exceptions, Dallas. You looked at the circle. The bill comes due."
    b "Technically, you hit me in three places. My penis and both of my testicles."
    b "So we have to multiply your punishment by three, right? An eye for an eye!"

    scene 19cdallas with dissolve

    d "That's cheating! You're just making this up! It doesn't sound reasonable at all!"
    d "Let's just talk about this for a minute! I'm sure we can come to an agreement?"

    b "Time for talking is over. Retribution is the only language you'll understand!"

    d "Is that from the bible? That's dark, man! Come on, [player_name]. Don't--"

    scene 20cdallas

    pause (.3)

    scene 19cdallas

    play sound "audio/buttslap.mp3"

    d "Ow! My ass! I've learned my lesson, friend! I'll never strike you in
        the testicles again. Scouts honor!"

    b "No dice. Two more to go!"

    scene 20cdallas

    pause (.3)

    scene 19cdallas

    play sound "audio/buttslap.mp3"

    d "Goddammit! Don't do it open palm! It's so much worse that way!"

    b "Don't make me lick my hand first! I'll do it! One more."

    scene 20cdallas

    pause (.3)

    scene 19cdallas

    play sound "audio/buttslap.mp3"

    d "Ow, shit! Stop spanking me! You're going to break me!"

    b "Are you going to be a good girl from now on?"

    d "Yes, yes! Put me down!"

    scene 21cdallas with dissolve

    d "Goddammit, [player_name]! My ass is on fire! Who taught you to spank like that?"

    scene 22cdallas with dissolve

    b "Spanking is not a skill, Dallas. It's a calling."
    b "You like to name your little circle games, right?"
    b "I call that 'A Perfect Circle'. Because if you look at the circle,
        I spank you on your perfect little ass."

    scene 23cdallas with dissolve

    d "You think my ass is perfect?"

    scene 22cdallas with dissolve

    b "Well, not anymore. I'm pretty sure I just broke it."
    b "It was very firm though! Keeping up with your exercises even after you
        graduated?"

    scene 23cdallas with dissolve

    d "Yes, and thank God for it! Otherwise, I think you would have sundered me in
        two! You spank too hard!"
    d "I'm going to get you back for this. You know that, right? Your goin' down, man!"

    scene 22cdallas with dissolve

    b "When you think about getting revenge, remember this moment."
    b "And remember that I only used twenty percent of my strength."
    b "If I had used one hundred percent, you'd be dead right now."

    scene 23cdallas with dissolve

    d "As fun as this is, I have to use the restroom and then head home."
    d "How about next time we leave my innocent ass out of these disputes?"
    d "I'm going to have so much trouble sitting down now..."

    b "No promises, Dallas!"

    d "You just like touching my ass, don't you?"

    b "Only if I'm getting to pound it. Er, wait--"

    d "Phrasing!"

    scene 22cdallas with dissolve

    b "Bathroom is down the hall. I think there's some lotion in there too. You might
        need it for, you know, your ass."

    scene 24cdallas

    d "No way, man! I can guess what you use that for!"
    d "Damn, my butt burns so bad. It's probably redder than a raspberry."

    stop music fadeout 2.0

    scene 25cdallas with fade

    bi "{i}Alright, so Avalon is sleeping right now. It's still relatively early.{/i}"
    bi "{i}I'll take a shower and afterward, maybe she'll be awake.{/i}"

    d "Hey [player_name], I hope this works as an apology for punching you in the balls earlier."

    scene 27cdallas

    b "Hmm? What're you--?"

    scene 26cdallas

    d "What do you think? Can you ever forgive me?"

    scene 28cdallas

    b "You know, I might be able to find a way after all..!"

    scene 29cdallas

    d "Good! I wonder how you'll apologize to me for the spankings..?"

    b "W-what do you want?"

    d "I'm sure you'll think of something! Don't forget to call, [player_name]."

    scene 28cdallas

    bi "{i}Wow! I did not expect that! Maybe she didn't hate those spankings as much
        as she claimed.{/i}"
    bi "{i}Damn, I need a cold shower now. Like, a very, {b}very{/b} cold shower. {/i}"

    jump night_one

    ## This is the first night with Avalon. Each night, their relationship will
    ## grow more and more sexual.

    label night_one:

    scene 1nightone with fade

    bi "{i}I got a lot of great information today to help Avalon.{/i}"
    bi "{i}So tonight, I'll see if she wants to spend some time together.{/i}"
    bi "{i}And I'll let her decide the pace at which she wants to open up.{/i}"

    scene 2nightone

    bi "{i}But what should we do together? What's she interested in?{/i}"
    bi "{i}We're probably not going to practice cheerleading moves together.{/i}"
    bi "{i}Maybe we could watch a movie--?{/i}"

    scene 3nightone

    a "Uhh... Uncle [player_name]..?"

    scene 4nightone

    b "Avalon! I thought you were asleep?"

    scene 3nightone

    a "I woke up. You're almost naked..? Did you take a shower?"

    play music "audio/no_goodbyes.mp3"

    a "Why are you still wet coming out of the bathroom? Did you forget a towel?"

    scene 6nightone

    b "I don't bring clothes to the bathroom with me. I just walk to my room to
        dress. I guess I'm not used to company. And I prefer to air dry."
    b "I didn't mean to make you uncomfortable. Shoot, I wasn't thinking at all!
        I should--"

    scene 5nightone

    a "It's alright, I'm not uncomfortable. I am a little concerned though."

    scene 7nightone with dissolve

    a "What's with those boxers? They've got little flowers on them."
    a "I thought you were coming out of the bathroom but now I think
        maybe you're coming out of the closet?"
    a "This explains so much, Uncle!"

    scene 9nightone

    b "Take shots at my masculinity as much as you want, Avalon. I've got plenty
        to spare!"
    b "And I'm too straight to be gay. These were on sale and they're comfy!"

    scene 7nightone

    a "Well, I'm just glad you didn't walk out of there wearing heels and a skirt!"
    a "Mom had a guy over once and-- No, no. I don't even want to remember that."
    a "You really couldn't afford anything else?"

    scene 9nightone

    b "You don't stay rich by spending all your money, Avalon. Besides, I'm not rich."
    b "I literally have just enough right now that I can retire and live off what
        I have in the bank."
    b "But that's only {b}if{/b} I spend conservatively. And die around the age of sixty-eight..."

    scene 5nightone

    a "Does that money have something to do with why Mom stabbed you with a pen?"
    a "I remember hearing you guys argue about money before you started screaming
        in pain."

    scene 9nightone

    b "Yes, your mother found out I came into some money. I told her I was setting some
        aside for--"

    scene 6nightone with dissolve

    b "Well, it's not important."

    scene 9nightone with dissolve

    b "But I wasn't going to give her any of the money I'd made so she got angry and stabbed me."
    b "I was willing to give her some money but only if she-- I shouldn't say. It's not
        my place."

    a "I kind of want to know what you set some aside for..."

    scene 6nightone

    b "It was for you, Avalon. I set aside some for you so that you would have options after school."
    b "I was going to give it to you after you graduated and let you decide what
        to do with it."
    b "I know you graduated a month ago. I've just been wrapped up in my own mess
    and I haven't had a chance to give it to you yet."

    scene 3nightone

    a "Wait, what?! Why would you set aside money for me like that??"
    a "I've been so shitty to you for the last few years. Why would you do that?"
    a "No, no. I can't accept it. You shouldn't have set any aside!"

    scene 9nightone

    b "Calm down, Avalon. You weren't shitty to me. You had other priorities."
    b "You were involved with Cheerleading, hanging out with friends, and going to parties."
    b "You were just doing what kids do. And you seemed happy. Being happy is all I ever wanted for you anyway."
    b "And it wasn't your fault, I didn't reach out to you either. I think we both were just
        in our own worlds for a few years."
    scene 8nightone

    a "I remember you used to come over to visit me. It's been a while."
    a "Even before Mom decided to autograph your femur, you stopped visiting so much."
    a "I guess I did have other priorities. I didn't mean for us to lose touch though.
        I'm sorry about that, Uncle [player_name]."
    a "We can spend time together now if you want."

    scene 5nightone with dissolve

    a "I mean, not right now. You probably need to put some clothes on."

    scene 9nightone

    b "Right! And yeah, I'd love to reconnect, Avalon."
    b "How about over a movie? Dealer's choice!"

    scene 7nightone

    a "Who's the dealer?"

    b "You are."

    scene 8nightone with dissolve

    a "Oh, alright. That sounds great, Uncle.
        I'll go grab one from my room and we can watch it together."

    a "And... thanks for keeping this room for me. It even
        still had these old pajamas you bought me."
    a "They're not exactly my style anymore and they're a little small now..."

    scene 9nightone

    b "It looks like they still fit just fine! They're helping you show
        off those cheerleading abs!"
    b "It looks like I could do my laundry on those abs!"
    b "Do you need some Benadryl? 'Cause you are looking {b}swoll{/b}, girl!"

    scene 7nightone

    a "Stop! You're such a dork sometimes! And I've heard the laundry one before."
    a "Unoriginal jokes, Uncle [player_name]? And I thought you were better than that."
    a "Tsk tsk!"

    scene 9nightone

    b "Someone has to keep the legacy of these exceptional jokes alive.
        I'm just accepting that responsibility."
    b "I'm so benevolent and giving that way. Like Santa Claus or..."
    b "Jesus."

    scene 8nightone

    a "You steal people's jokes, justify it, and then manage to find a way to
        compare yourself to Jesus."
    a "That's... actually impressive, Uncle. And arrogant. But in a very... you kind
        of way."

    stop music fadeout 2.0

    a "Anyway, let me go pick out a movie. I'll meet you in the living room."

    scene 10nightone with fade

    ai "{i}He's so frugal with his money yet he set aside some for me so
        I could have options after I graduated. He cares about me.{/i}"
    ai "{i}Thinking back... he's always cared about me. I must have been too
        naive to see it before. {/i}"
    ai "{i}And this whole time I've been here, he's been so accommodating. And kind.
        And sweet...{/i}"

    scene 11nightone

    ai "{i}And wow, that body! I've seen him without a shirt on before
        but only when I was younger.{/i}"
    ai "{i}It didn't make me feel like this back then.
        But seeing him now, almost naked, is making me feel so...{/i}"
    ai "{i}Warm.{/i}"

    scene 12nightone with fade

    a "Hey! I've got the perfect movie picked out. You're going to love it, I promise!"

    scene 13nightone

    b "Excellent. I know you're a bit of a movie fanatic so I have high expectations!
        What're we watching?"
    b "I'm down for 'Wall-E' but I'm secretly hoping for '10 Things I Hate About You'."
    b "God damn, that Julia Stiles can act!"

    scene 17nightone

    menu:
        "{b}Additional Dialogue Choice{/b}"

        "Julia Stiles is a gem!":
            a "Yeah, I kind of want to have her babies."

        "Who the hell is Julia Stiles?":

            a "Sorry, Uncle, I'm not familiar with actresses from your time."
            a "When was she popular?"
            a "1950's?"

            b "We're only ten years apart in age!"

    scene 15nightone

    a "But no, none of those! We're watching... 'The Thing'!"

    scene 14nightone with dissolve

    a "It's about an alien organism that takes the shape of people and dogs and stuff..."
    a "And eats them! It's epic!"

    scene 16nightone

    b "That sounds horrifying! Why would anyone watch that?"
    b "Especially over a quality modern take on William Shakespeare's 'The Taming of the Shrew'?"

    scene 14nightone

    a "Because it's scary! And there's no CGI here, Uncle!
        It's all real-life special effects and puppeteering."
    a "The gore is so detailed and realistic, it's incredible considering the
        year the movie came out. It's a true horror masterpiece!"

    scene 18nightone

    b "I didn't know you developed an interest in horror movies. The last thing
        we watched together was... Milo and Otis, wasn't it?"
    b "Damn, that movie gets me emotional every time."

    a "You cried so much! I was embarrassed for you!"

    scene 16nightone with dissolve

    b "You like that horror stuff though? You like being scared?"

    scene 17nightone

    a "Yeah, I really do. As long as there's not, you know, {b}actual{/b} danger."
    a "Being scared releases little bits of adrenaline. It makes me feel awake
        and alive! It's a rush, you know?"

    scene 15nightone

    a "And scary movies are great to cuddle up to a partner with! Dallas and I--"
    a "Well, it's not important. But really, they can be a lot more fun than you think!"
    a "Trust me. Give it a chance. I'll turn you into a fan too!"

    scene 18nightone

    b "When you talk about it, you make it sound pretty great.
        I've never really thought about it that way."
    b "I'm down to try something new. Especially with you. You've convinced me!
        Let's watch it!"

    scene 17nightone

    a "Before we start, I was hoping we could talk for a moment? I just had some
        things I wanted to get out in the open."

    scene 15nightone

    bi "{i} This might be what I was waiting for!{/i}"
    b "Yeah, of course. You can always talk to me about anything. What's on your mind?"

    scene 20nightone

    play music "audio/one_step_closer.mp3"

    a "Well, Dallas was over earlier and we talked about how hard things have been for me lately."
    a "Her and I talked a little bit about you and how we used to be close. You're
        someone I used to lean on for support."
    a "I need that support again but I--"
    a "I've had really bad experiences with men lately and you're a guy. So it's
        just been a little bit... difficult."
    a "I know I shouldn't be like that. It's not fair to you. I just can't help it."

    scene 27nightone

    b "You're right, I'm a guy. And I know that guys have traditionally
        been a negative part of your life."
    b "I love you, Avalon. I always have. And I'd never do anything to hurt you."
    b "But I can understand that doesn't change your past experiences. So I'll be
        here if you need me and I'll give you space when you need too."
    b "And hopefully, in time, we can rebuild the relationship we used to have."

    scene 22nightone

    a "I just don't understand why guys are always so nasty to me! They look at me
        as an object and nothing else!"
    a "The men mom brings over and the boys at school. I'm more than just a cheerleader,
        you know?"
    a "I more than just an object..."

    scene 27nightone

    b "I've had largely negative experiences with people too, Avalon. Not in the same
        way as you, not at all like that. But to some degree, I do understand."
    b "That's why I live alone. That's why I don't have a lot of friends or associates."
    b "I just... I don't like people in general. But you and I, we had something special.
        In a lot of ways, we took care of one another. I shouldn't have let that go."

    b "Maybe fate brought us back together so we can lean on each other for support?
        And maybe together, we can tolerate the world?"
    b "What do you say? Do you want to give it a shot?"

    scene 20nightone

    a "Wow, that was inspiring. You're going to make me cry, Uncle."
    a "I accept your proposal! As long as you promise not to ogle my boobs
        like every other guy I meet."

    scene 24nightone

    menu:
        "{b}Additional Dialogue Choice{/b}"
        "Pff! I'm looking at your boobs right now!":
            b "That's what peripheral vision is for."
            b "I'm {b}always{/b} looking at your boobs."

        "I prefer bigger boobs.":
            b "Your boobs are too small."
            b "I only take notice of triple D cups!"

        "I prefer dudes.":
            b "That's because I prefer the company of men."
            b "Bring on the sausages!"

    scene 23nightone

    a "You're terrible! We need to put a filter on you, Uncle. I only hope you're joking! "

    scene 24nightone

    b "Yeah, I'm joking."

    scene 25nightone with dissolve

    b "You know, I think I joke a lot because it's important to me that people like me."
    b "People like to laugh so if I make them laugh, they'll appreciate my company."
    b "When people like you, they have less of a desire to hurt you."

    scene 27nightone with dissolve

    b "I'm damaged, Avalon. I've had a lot of terrible things happen in my life
        and I've mostly not recovered."
    b "I know something happened to you. Something terrible. We don't have to talk
        about it right now."
    b "But I want you to know that I want to help. And maybe we can both heal
        a little bit if we work together towards it."
    b "You have this aura about you, Avalon. You just radiate this energy that is
        so positive and uplifting. The world is a better place with you in it."
    b "It's healing for me to be around you. And I want the same to be true about
        me for you."

    scene 20nightone

    a "Wow, that's nice, Uncle. A little cheesy but I liked it."
    a "I didn't know you were hurting though. You never talked about anything
        like that."
    a "I like the idea of us helping each other. Yeah, let's do it."

    scene 27nightone

    b "I still have that money for you. I'm going to give you a card you
    can use to buy whatever you want."
    b "We'll go pick up your stuff from your moms tomorrow, you can stay here and
        do something with that money."
    b "You can go to college, start a business or just take some time off. Anything
        you want!"
    b "Does that sound alright? Do you want to live with me for a while?"

    scene 19nightone

    a "I don't have much of a choice..."

    b "But if you did?"

    scene 21nightone with dissolve

    a "I'd say 'Yes'."

    scene 24nightone

    b "I'm glad to hear that. It'll be nice having you around again."

    scene 27nightone with dissolve

    b "I also want to focus on your recovery. We don't have to talk about it
        right now but I have some ideas that might help you."

    a "Recreational drugs?"

    scene 24nightone with dissolve

    b "Yeah, I have a Colorado River Toad on order."
    b "If you lick it, you get a pretty wicked psychedelic high."
    b "We'll trip balls like hippy hillbillies."

    scene 23nightone

    a "Oh gross, Uncle! I was thinking of pot or something!"
    a "What is it with you and frogs lately? You're so weird sometimes!"

    scene 25nightone

    b "You can get warts on your tongue though. From the toad, I mean."

    scene 24nightone with dissolve

    b "We'll have to be extra careful with them!"

    scene 23nightone

    a "You're nasty, Uncle [player_name]!"

    scene 27nightone

    b "I know that you don't want to be touched right now but I heard through the grapevine that maybe it's a control thing?"
    b "So I'll let you make the decisions on hugging and, you know, physical contact."
    b "I won't touch you or try to hug you unless you initiate it. Does that sound okay?"

    scene 20nightone

    a "You didn't have to make it sound so strange but yeah, I understand. It
        sounds like a good idea for now."

    scene 21nightone with dissolve

    a "I'm actually much more comfortable with you now. I guess we're rebuilding
        already!"
    a "But I like the idea of having control. Especially at this time in my life."

    scene 26nightone

    stop music fadeout 2.0

    a "Poke."
    a "Baby steps! Maybe tomorrow I'll use two fingers."
    a "Er, wait, that sounded weird. You know what I mean!"

    scene 24nightone

    b "That was pretty adorable. Alright, let's watch the movie, goofball."

    scene 28nightone with fade

    play music "audio/a_quiet_thought.mp3"

    bi "{i}Our lives are filled with moments.{/i}"
    bi "{i}Most of those moments are unremarkable like brushing your teeth,
        getting into your car or washing the dishes.{/i}"

    scene 29nightone with dissolve

    bi "{i}But then there are moments that are so wonderful we cherish them forever.{/i}"
    bi "{i}They're the ones we fall asleep thinking about and wake up thinking about.{/i}"

    scene 30nightone with dissolve

    bi "{i}We don't always know right away that we're having one of those moments.{/i}"
    bi "{i}Sometimes we only know when it's too late and the moment has passed.
        And we didn't hold on to it as tightly as we wish we had.{/i}"

    scene 31nightone with dissolve

    bi "{i}But then there are moments that we know exactly how important they
        will be to us. Those are the best ones.{/i}"

    scene 32nightone with dissolve

    bi "{i}They are the highlights of our lives. The ones worth chasing, worth
        living for.{/i}"

    scene 33nightone with dissolve

    bi "{i}They make it worth it to get out of bed in the morning knowing that even
        though the chances might be slim, they may happen!{/i}"

    scene 34nightone with dissolve

    bi "{i}This was one of those moments. It was the peak of the mountain.
        The happiest I knew I could ever be.{/i}"
    bi "{i}Right here, holding her...{/i}"

    scene 35nightone with dissolve

    stop music fadeout 1.0

    bi "{i}But for every ying, there is a yang. And with the possibility of
        wonderful moments, there's always the possibility of terrible ones.{/i}"
    bi "{i}Avalon had experienced one of the most terrible things a woman ever might
        encounter in her life.{/i}"
    bi "{i}And no matter how perfect a day she might have, that moment will haunt
    her forever...{/i}"

    scene 36nightone with vpunch

    a "{b}Ahh!{/b}"

    scene 37nightone

    b "What? Avalon, what's going on? What's wrong? Talk to me."

    scene 38nightone

    a "It happened again! I saw it all over again. I can't see it anymore. I can't!"
    a "Please! Stop haunting me!!"

    b "Look at me, Avalon. You're alright, you're with me. "

    scene 39nightone

    a "I'm so scared. I just want it to stop! Stop, stop! Please..!"

    b "Look at me, Avalon. I'm here with you. Nobody's going to hurt you."
    b "I'm going to protect you. I promise."

    a "Uncle?"

    b "Yeah, it's me."

    scene 40nightone with dissolve

    a "Uncle [player_name]?"

    b "You're okay. You're not in danger. I won't let anything happen to you again."

    scene 41nightone

    a "I saw it. It happened again. It keeps happening in my nightmares!"

    b "I've got you. You're safe."
    b "I'm not going to let anyone hurt you."

    play music "audio/heartbeat_of_the_hood.mp3"

    scene 42nightone

    a "I remembered it again. I keep remembering it."
    a "I was sleeping in my room when I felt something on top of me. He... he woke
        me up. He was so heavy on top of me..."
    a "His hand was over my mouth. He said if I screamed, he'd kill me. I was so scared."

    scene 41nightone

    a "He pulled my pants down... I struggled, I tried to push him off me!"
    a "But then he hit me..."

    scene 43nightone with dissolve

    a "He hit me so hard, I blacked out and when I woke up he was inside me."
    a "And he was thrusting back and forth..."
    a "I couldn't stop him, Uncle. I couldn't..."

    scene 42nightone

    a "I thought it was never going to end. I just wanted it to be over."
    a "It hurt so bad..."

    scene 44nightone

    b "Ava, who? Who was it? Tell me his name."

    a "It was someone Mom brought over."

    bi "{i}I'll fucking kill her. {/i}"

    a "I only ever saw him that once..."

    b "Do you remember his name?"

    a "I just got his first name. It was Seth."

    scene 42nightone

    bi "{i}She sobbed for nearly twenty minutes. All I could do was hold her tightly,
        and continue to reassure her that she was safe.{/i}"

    scene 44nightone

    stop music fadeout 1.0

    bi "{i}But I was seething with rage. Avalon would be changed forever.{/i}"
    bi "{i}She will always be damaged by this. She will always be broken because of
        this man.{/i}"
    bi "{i}I knew I had to be strong for her but on the inside, my blood was boiling.
        I wanted vengeance.{/i}"

    jump act_two_s
