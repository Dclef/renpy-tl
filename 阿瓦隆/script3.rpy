

## Day Three - Start

label act_three:

    scene black

    $ player_name = renpy.input("What would you like to name the MC?")
    if player_name.strip() == "":
        $ player_name = "Byron"

    menu:
        "Choose your path:"

        "Octavia's Path":
            $ octavia = True

        "Dallas's Path":
            $ dallas = True

    $ persistent.galleryName = "[player_name]"

    jump act_three_s

label act_three_s:

    stop music fadeout 2.0

    scene avalon with fade

    if persistent.actThree == False:
        $ renpy.notify("You've unlocked Act Three in Act Select on the Main Menu!")
        $ persistent.actThree = True

    pause

    scene avalonactthree with dissolve

    pause

    scene 1yogamorning with fade

    play music "audio/bored_to_death.mp3"

    ai2 "{i}I can't believe that happened last night.{/i}"
    ai2 "{i}I don't know what came over me to think I should ask for a kiss.{/i}"
    ai2 "{i}Now I can't seem to get my mind off of it...{/i}"
    ai2 "{i}Maybe a morning exercise will help clear my head.{/i}"

    scene 2yogamorning

    ai2 "{i}I'm sure Uncle is going to sleep in late, he's been so exhausted lately.{/i}"
    ai2 "{i}I wonder what was going on in his mind when he kissed me?{/i}"
    ai2 "{i}He tells jokes when he's nervous and he made that silly one
        about my nose.{/i}"
    ai2 "{i}But was he nervous because he likes me too?{/i}"

    scene 3yogamorning

    ai2 "{i}Or was he afraid to say 'No' and he didn't want to kiss me?{/i}"
    ai2 "{i}It can't be that!{/i}"
    ai2 "{i}That kiss was amazing!{/i}"
    ai2 "{i}There was so much electricity between our lips, I thought I was going
        to explode!{/i}"

    scene 4yogamorning with dissolve

    ai2 "{i}And the last thing he said to me...{/i}"
    ai2 "{i}'My Avalon.'{/i}"
    ai2 "{i}It was as if he was saying that I may not have been enough for my father
        to keep him sober.{/i}"
    ai2 "{i}But I'm enough for him. I'm enough for Uncle [player_name]...{/i}"

    scene 5yogamorning with dissolve

    ai2 "{i}But does that mean I'm enough as just his niece?{/i}"
    ai2 "{i}Or that he wants to be more...{/i}"
    ai2 "{i}I mean, that was way more than just a goodnight kiss!{/i}"
    ai2 "{i}That was hot!{/i}"

    scene 6yogamorning with dissolve

    ai2 "{i}But it's wrong, isn't it?{/i}"
    ai2 "{i}Even if he isn't my uncle by blood, it's still wrong.{/i}"
    ai2 "{i}... Right?{/i}"
    ai2 "{i}Ugh!{/i}"
    ai2 "{i}Thinking about how wrong it is just makes me want it more!{/i}"

    scene 7yogamorning with dissolve

    ai2 "{i}I've always heard that the forbidden fruit is the sweetest.{/i}"
    ai2 "{i}I didn't understand that before but now I'm starting to.{/i}"
    ai2 "{i}I don't want to misunderstand what happened last night.{/i}"
    ai2 "{i}But I want what I want.{/i}"
    ai2 "{i}And I want him.{/i}"

    scene 8yogamorning with dissolve

    ai2 "{i}I can't stop thinking about cuddling up to him last night.{/i}"
    ai2 "{i}Him placing his large hand gently on my head.{/i}"
    ai2 "{i}His lips pressing hard against mine.{/i}"
    ai2 "{i}His warmth, his taste...{/i}"

    scene 9yogamorning with dissolve

    ai2 "{i}Uhfn!{/i}"
    ai2 "{i}I'm so excited right now!{/i}"

    stop music fadeout 2.0

    ai2 "{i}I can't focus on my exercise at all!{/i}"
    ai2 "{i}I haven't touched myself in over a month.{/i}"
    ai2 "{i}Well, maybe a nice, hot shower will calm me down. {/i}"

    scene 10yogamorning with fade

    play sound "audio/shower.mp3"

    ai2 "{i}Oh yes!{/i}"
    ai2 "{i}This is very relaxing. {/i}"
    ai2 "{i}Wash away all those dirty thoughts, Avalon.{/i}"
    ai2 "{i}I shouldn't worry too much about what our relationship is right now.{/i}"
    ai2 "{i}I'm sure the only way to find out is by spending time with him.{/i}"
    ai2 "{i}He said we might go shopping today.{/i}"

    stop sound fadeout 3.0

    scene 11yogamorning with fadefast

    ai2 "{i}But even if he doesn't think of me as more than just his niece now,{/i}"
    ai2 "{i}maybe I can push him in that direction..?{/i}"

    scene 12yogamorning with dissolve

    a2 "Oh! Uncle."
    a2 "You startled me a little."
    a2 "I just finished with my shower."
    a2 "Did you..."

    scene 14yogamorning

    ai2 "{i}Why does he have that dumbfounded expression on his face..?{/i}"

    b "Y-you're all wet and wearing... just a towel..."
    b "You look... you look..."

    scene 13yogamorning

    a2 "Clean?"
    a2 "You're welcome to use the shower now."
    a2 "I may not have left much hot water though."
    a2 "Sorry about that."

    scene 14yogamorning

    b "T-that's alright,"
    b "I think I'll be taking a cold shower this morning."
    b "A {b}very{/b} cold shower..."

    scene 13yogamorning

    a2 "Oh, alright, well--"
    ai2 "{i}Wait, is he excited right now?{/i}"
    ai2 "{i}Because of me??{/i}"
    ai2 "{i}He does want more from our relationship!{/i}"
    ai2 "{i}Oh but right now, I need to have fun with this!{/i}"

    scene 15yogamorning with dissolve

    a2 "Enjoy your shower, Uncle."
    a2 "And thanks for spending time with me last night."
    a2 "I had a really nice time."

    b "You're uhh... welcome."
    b "It was my pleasure, really."

    a2 "And I know how much you like nose kisses, so..."

    scene 16yogamorning with dissolve

    a2 "Mwah!"

    scene 15yogamorning with dissolve

    a2 "I'll meet you in the kitchen after I'm done getting ready."
    a2 "And we can talk about what we want to do today."
    a2 "You said we could go shopping, remember?"

    b "Shopping?"
    b "Sure, yep, shopping."
    b "I uhh, remember that."

    a2 "Okay, I'm going to go get dressed."
    a2 "See you soon, Uncle [player_name]."

    scene 17yogamorning with dissolve

    ai2 "{i}If he wasn't completely smitten with me before, he is now.{/i}"
    ai2 "{i}And that'll teach him to kiss me on the nose instead of the lips!{/i}"
    ai2 "{i}Now he knows how it feels!{/i}"
    ai2 "{i}Punishment sentenced and served.{/i}"

    bi "{i}What the hell just happened?{/i}"
    bi "{i}That kiss last night...{/i}"
    bi "{i}It's like it woke up an entirely different person inside of her.{/i}"
    bi "{i}She's like a confident, fired up little vixen now!{/i}"
    bi "{i}I really need that cold shower...{/i}"

    scene 1kitchenmorning with fade

    bi "{i}I have that appointment with the detective this morning.{/i}"
    bi "{i}I'll have to tell Avalon about it.{/i}"
    bi "{i}She's awfully keen on when I'm not being fully truthful with her.{/i}"
    bi "{i}But she also seems understanding so maybe this will go well.{/i}"
    bi "{i}I don't want her there with me for the meeting though.{/i}"
    bi "{i}I just... don't know what to expect from it.{/i}"

    scene 2kitchenmorning

    a2 "Hey, Uncle!"
    a2 "I decided to wear something a little different today."
    a2 "What do you think?"

    scene 3kitchenmorning

    b "Wow!"
    b "You look... phenomenal!"
    b "It's like you're back to your old self before the doom and gloom look you
        adopted recently."
    b "Are you hungry?"

    scene 8kitchenmorning

    a2 "I could eat!"
    a2 "But what's this?"
    a2 "It doesn't look like what you would normally eat."

    menu:
        "{b}Additional Dialogue Choice{/b}"
        "Four Dozen Eggs?":
            a2 "Don't you have to eat like, four dozen eggs every morning?"
            a2 "You know, to help you get large?"

        "Five Dozen Eggs?":
            a2 "Don't you have to eat like, five dozen eggs every morning?"
            a2 "So you can be roughly the size of a barge?"


    scene 4kitchenmorning

    b "I usually eat healthier than this but I woke up this morning with a sweet
        tooth."
    b "After seeing you earlier though, I think I've had all the sweetness
        I can handle!"

    scene 9kitchenmorning

    a2 "Are you sure we're not having corn on the cob this morning?"
    a2 "Because that was so corny!"

    scene 4kitchenmorning

    b "Did you sleep well last night?"
    b "I hope those stories about your dad didn't keep you up."

    scene 10kitchenmorning

    a2 "Mm, yeah, I slept well."
    a2 "But I thought a lot about that kiss this morning..."
    a2 "I kind of wanted to talk to you about that."

    scene 5kitchenmorning

    b "Oh!"
    b "Uhh, yeah."
    b "I'm... sorry if it was weird."
    b "I just--"

    scene 9kitchenmorning

    a2 "It wasn't weird!"
    a2 "I really enjoyed it!"
    a2 "And I think, if you liked it too, maybe we can do it more often?"
    a2 "I've been really happy here with you, Uncle."
    a2 "I really want to hold on to that happiness."
    a2 "And maybe chase it further, you know?"

    scene 6kitchenmorning

    b "Having you here has been a real pleasure, Avalon."
    b "I feel the same way."
    b "If you want to try moving in a new direction with our relationship,
        I'm all for that."
    b "But I want to take it slow so we don't rush into anything we're not prepared for."
    b "We'll have to iron out some of the details as we go but..."
    b "Yeah, if you want, let's chase it."

    scene 8kitchenmorning

    a2 "Really?!"
    a2 "Because I don't want you to think you have to just for me."
    a2 "Is it really what you want??"

    scene 6kitchenmorning

    b "Yeah, it's really what I want."
    b "I promised to take you shopping today, right?"
    b "Why don't we do that?"

    scene 13kitchenmorning

    a2 "Yeah??"
    a2 "I'd love that!"
    a2 "I really want to get more clothes like this outfit."
    a2 "Like I used to wear."

    scene 7kitchenmorning

    b "Certainly!"
    b "But listen, I have to see that detective this morning."
    b "So while you do some shopping--"

    scene 11kitchenmorning

    a2 "I told you that isn't important."
    a2 "You're really going through with it?"

    scene 5kitchenmorning

    b "I thought you would be alright with it."
    b "It's just a meeting anyway."
    b "It's important to me."

    scene 11kitchenmorning

    a2 "Why can't you just cancel it and go shopping with me?"
    a2 "You know this is going to be more complicated than just a meeting."
    a2 "And there could be... repercussions."
    a2 "Please don't."

    scene 7kitchenmorning

    b "You're so dramatic!"
    b "And I know the difference between your real sad and your fake sad."
    b "You big faker!"
    b "But I'm not going to lie, your fake sad is kind of..."
    b "Sexy."
    b "Is it strange that it's turning me on?"

    scene 10kitchenmorning

    a2 "Uncle, don't say that kind of stuff..."
    a2 "Now you're getting me excited."

    scene 6kitchenmorning

    bi "{i}I wonder if I can get her more aroused.{/i}"
    bi "{i}A guess a little experiment wouldn't hurt.{/i}"
    bi "{i}I'll stop if it seems to be upsetting her.{/i}"

    play music "audio/aint_it_funny.mp3" fadein 3.0

    b "And seeing you in that towel earlier with water dripping
        down your otherwise naked body."
    b "It was absolutely intoxicating watching you glistening and glimmering from the wet droplets clinging to your
        moist skin."
    b "I couldn't have been any more stunned than if I'd been clubbed over the head."

    scene 14kitchenmorning

    a2 "Stop it, Uncle."
    a2 "I know what you're doing."
    a2 "I'll give you one chance to knock it off."

    scene 7kitchenmorning

    b "And that kiss last night, my god!"
    b "If I would have held my lips to yours any longer, I don't think I would have been able to stop."
    b "I would have had to ravish you right then and there."

    scene 14kitchenmorning

    a2 "I warned you, Uncle."
    a2 "I gave you a chance and you didn't take it."
    a2 "You're not going to like where this road ends."

    scene 15kitchenmorning with dissolve

    b "What are you going to do?"
    b "Kiss me again with those luscious and delectable lips?"
    b "Press your firm, gorgeous body against me once more?"

    scene 16kitchenmorning with dissolve

    a2 "You're only making this worse on yourself, Uncle [player_name]."
    a2 "But if you take it all back now, we can get on with our day."
    a2 "Nobody has to suffer."
    a2 "Last chance."

    b "I'm calling your bluff."
    b "I don't think--"

    scene 17kitchenmorning

    b "Oh really??"
    b "You're going to knock a bottle of water on the floor?"
    b "Avalon is going to throw a temper tantrum like a child?"

    a2 "It's not a temper tantrum, Uncle."

    scene 18kitchenmorning with dissolve

    b "Well, I'll have you know those waters aren't cheap."
    b "They've got a hint of cherry flavor to them."
    b "It really compliments the bundt cake."

    scene 19kitchenmorning with dissolve

    b "Oh, you're not in the mood for it now?"
    b "That's alright."
    b "We can save it in some Tupperware so you can eat it later."

    scene 20kitchenmorning with dissolve

    b "What... what're you doing?"
    b "Stop that."
    b "Don't climb on--"

    scene 21kitchenmorning with dissolve

    b "Whoa..."
    b "You know, it probably would have been easier to just walk around to me."
    b "But no, it's fine."
    b "I can see you're trying to make a--"

    scene 22kitchenmorning with dissolve

    b "...point."

    a2 "Uncle."

    b "Yes, my beautiful Avalon?"

    scene 23kitchenmorning with dissolve

    a2 "Say."
    a2 "You're."
    a2 "Sorry."

    b "You know what?"
    b "I might be a little..."
    b "tiny bit..."
    b "Sorry."

    scene 25kitchenmorning

    a2 "Great!"
    a2 "Now let's get going!"
    a2 "We don't want you to be late for your appointment."
    a2 "Things to do, Uncle!"
    a2 "No time to dilly dally!"

    b "You can't be serious!"

    scene 24kitchenmorning

    b "You're just going to leave me wanting??"
    b "I said I was sorry!"
    b "Come on!"

    ai2 "{i}That's right, Uncle.{/i}"
    ai2 "{i}Squirm!{/i}"
    ai2 "{i}And the next time you decide to tease me,{/i}"
    ai2 "{i}you better keep in mind that I'm way better at it!{/i}"

    stop music fadeout 2.0

    scene 1clothingshop with fade

    bi "{i}There are plenty of clothing stores down this street.{/i}"
    bi "{i}Avalon should have a multitude of options while I head to this appointment.{/i}"
    bi "{i}This one is quite small but it's the first in the row of shops.{/i}"

    scene 2clothingshop with dissolve

    b "Here we are!"
    b "Use the credit card I gave you wisely."
    b "Whatever you buy is coming out of the funds I've built for you."

    scene 4clothingshop

    a2 "Thank you for taking me shopping today."
    a2 "Are you really sure you can't stay?"
    a2 "You can still cancel the appointment..."

    scene 3clothingshop

    b "Don't worry so much!"
    b "It's just a meeting."
    b "What's the worst that could happen?"

    scene 4clothingshop2

    a2 "Well, you're meeting him at a lingerie store so he's probably a pervert."

    b "No! Well, maybe..."
    b "Perhaps it takes a pervert to catch a pervert?"

    a2 "I don't think--"

    scene 5clothingshop with dissolve

    cl "Hello!"
    cl "Was there anything I could help you find today?"
    cl "Or are you just browsing?"

    a2 "I wouldn't mind some help, actually."

    scene 4clothingshop

    a2 "Be careful!"
    a2 "I'll see you when you're finished."

    scene 6clothingshop with dissolve

    bi "{i}She went straight in for a kiss!{/i}"
    bi "{i}No teasing this time.{/i}"
    bi "{i}Or maybe she's just that worried about this meeting?{/i}"
    bi "{i}I shouldn't be doing this...{/i}"
    bi "{i}But I can't stop myself either.{/i}"
    bi "{i}I have to go.{/i}"

    scene 7clothingshop with dissolve

    ai2 "{i}Maybe a kiss will remind him what's really important?{/i}"
    ai2 "{i}Maybe if I hold him tight enough, or kiss him passionately enough,{/i}"
    ai2 "{i}maybe he'll stay..?{/i}"
    ai2 "{i}No.{/i}"
    ai2 "{i}I can see that he's determined and I can't deter him.{/i}"
    ai2 "{i}I have a terrible feeling this won't end well.{/i}"
    ai2 "{i}For either of us...{/i}"

    scene 8clothingshop with dissolve

    a2 "Promise me."

    b "Promise what?"

    a2 "Promise me that you will abandon this if it gets too dangerous."
    a2 "Okay?"

    b "It won't get out of hand."
    b "I promise."

    a2 "Alright."
    a2 "Come back to me soon, Uncle."

    scene 9clothingshop

    b "Oops."

    a2 "I mean..!"
    a2 "Did I say 'Uncle'?"

    menu:
        "{b}Additional Dialogue Choice{/b}"
        "Runcle!":
            a2 "I mean Runcle!"
            a2 "His name is Runcle!"
            a2 "I have a disability, sometimes I can't pronounce my R's."
            a2 "I'm very self-conscious about it."
            a2 "My therapist says it's best to just avoid talking about it altogether."

        "Dunkle!":
            a2 "I mean Dunkle!"
            a2 "He was a basketball champion and a hunk back in his prime."
            a2 "You know, a long long time ago."
            a2 "So we used to call him Dunkle and it kind of stuck!"

        "Carbuncle?":
            a2 "I mean Carbuncle!"
            a2 "You know, like a red gem."
            a2 "Cause he's a redhead and--"
            a2 "Ehem."

    scene 10clothingshop with dissolve


    a2 "Anyway, I'm looking for fashionable apparel that is both stylish and affordable."

    scene 11clothingshop with dissolve

    bi "{i}That recovery was masterfully performed.{/i}"
    bi "{i}She sure is quick and witty when she wants to be.{/i}"
    bi "{i}I guess her theory is that if she talks quickly enough, they'll get
    confused and forget about what just happened?{/i}"
    bi "{i}It looks like it worked!{/i}"
    bi "{i}I could learn a thing or two from her. {/i}"

    scene 1lingeriestore with fade

    bi "{i}So here I am at the lingerie store.{/i}"
    bi "{i}I'm staring at bras and panties on shelves and on mannequins.{/i}"
    bi "{i}Waiting for an unknown person with whom I'm going to share intimate details of
        mine and Avalon's life.{/i}"
    bi "{i}Standing here thinking about all this, I am...{/i}"

    scene 2lingeriestore

    bi "{i}Desperately uncomfortable!{/i}"
    bi "{i}This place is ginormous!{/i}"
    bi "{i}How many different types of panties could there possibly even be?!{/i}"
    bi "{i}And why are they combining letters {b}and{/b} numbers for bra sizes??{/i}"
    bi "{i}I thought bras were form-fitting or something.{/i}"
    bi "{i}There isn't just small, medium and large??{/i}"

    scene 3lingeriestore with dissolve

    n "Hello!"
    n "Can I help you, sir?"

    scene 4lingeriestore with dissolve

    b "Gah!"
    bi "{i}I've been found out!{/i}"
    bi "{i}Someone with a sweet, innocent little voice has caught me looking at
        women's undergarments!{/i}"
    bi "{i}Quick, explain that you're lost and confused!{/i}"

    n "Are you looking for something specific?"
    n "I'd be happy to help!"

    scene 12lingeriestore with dissolve

    bi "{i}Wha!{/i}"
    bi "{i}She's so tiny!{/i}"

    scene 13lingeriestore with dissolve

    bi "{i}And wearing nothing but sexy lingerie!{/i}"
    bi "{i}Is she even legal?!{/i}"
    bi "{i}She's like, four feet tall!{/i}"
    bi "{i}Stop looking at her chest, [player_name]!{/i}"

    scene 12lingeriestore with dissolve

    bi "{i}Quit staring!{/i}"
    bi "{i}Say something!{/i}"
    bi "{i}Say anything!{/i}"

    b "I-I was just..."
    b "Browsing."

    scene 5lingeriestore

    n "Are you shopping for someone specific?"

    scene 7lingeriestore with dissolve

    n "Don't break my heart and say you're here to buy for your girlfriend."

    bi "{i}Is she... flirting with me??{/i}"

    scene 12lingeriestore

    b "N-no, I'm sorry, I'm actually not browsing."
    b "I'm waiting for someone."
    b "I didn't... pick the location."

    scene 6lingeriestore

    n "It's alright, Sweetie."
    n "You don't have to be nervous."
    n "I don't bite."

    scene 7lingeriestore with dissolve

    n "Unless you're into that kind of thing."

    bi "{i}Smile and laugh!{/i}"
    bi "{i}Act like it's a joke!{/i}"

    scene 14lingeriestore

    b "Ha."
    b "I usually stick to the basics."

    if octavia == True:
        jump no_spank
    else:
        jump spank_someone

    label spank_someone:

    b "I did spank someone the other day though."

    bi "{i}Why are you telling her that?!{/i}"

    scene 5lingeriestore

    n "Oh, you're a 'Pain for Pleasure' kind of guy, huh?"
    n "That's naughty!"

    jump show_me

    label no_spank:

    b "Biting seems extreme but nibbling sounds like it could be fun."

    bi "{i}Why the hell would you say that!?{/i}"

    scene 5lingeriestore

    n "Oh, I like the sound of that!"
    n "I bet it would be absolutely tantalizing!"

    label show_me:

    scene 8lingeriestore with dissolve

    n "Maybe we can go into the backroom and... experiment?"
    n "I usually charge one hundred but for a cutie like you,"
    n "I'd only charge eighty."
    n "What do you say, Big Boy?"
    n "I promise to earn every penny."

    bi "{i}She's a prostitute!?{/i}"
    bi "{i}Wow, eighty bucks is a really good deal...{/i}"
    bi "{i}No! Stop this!{/i}"
    bi "{i}It's wrong!{/i}"

    scene 15lingeriestore

    bi "{i}She just grabbed my crotch!{/i}"
    bi "{i}What is with this girl!?{/i}"

    n "Oooh, I see your biceps aren't your only big muscles."
    n "And you're so hard!"
    n "If you get any more worked up, you might pop the button right off your jeans!"

    scene 9lingeriestore

    b "S-stop."

    n "Oh?"

    b "I'm sorry, Miss..?"

    n "Nicole."

    scene 16lingeriestore

    b "I'm sorry, Miss Nicole."
    b "You're a very beautiful young woman."
    b "But I'm simply not interested."

    scene 17lingeriestore with dissolve

    b "You seem like a nice girl."
    b "I can't imagine why you would resort to..."
    b "This line of work."
    b "But I'd be happy to give you a little money if you need it."
    b "Just... not for sex."

    scene 10lingeriestore

    n "Well, aren't you just a regular White Knight?"
    n "You're the type that likes to save the poor damsel in distress, huh?"
    n "A hopeless romantic."
    n "A girl could really fall for a guy like you."

    de "Yo, bitch!"

    scene 11lingeriestore with dissolve

    n "Hmm?"

    de "Why don't you stop playin' with that faggot and come help out a real man?"

    scene 19lingeriestore

    de "Walk that fine ass over this way, girl."
    de "Daddy is feelin' hungry today!"

    scene 10lingeriestore

    n "Excuse me, Sir."
    n "I have to tend to another customer."

    scene 21lingeriestore

    de "Aw yeah, bitch."
    de "You're lookin' fine as hell!"
    de "Where have you been all my life?"

    scene 22lingeriestore

    n "Hey there, Cutie."
    n "Was there something I could help you with?"

    de "Yeah, bitch, I'd like to buy that top right off the rack."
    de "{b}Your{/b} rack."

    scene 23lingeriestore with dissolve

    n "Oh, such a clever boy!"
    n "I find clever boys sexy!"
    n "I don't think you're here to shop though, Handsome."
    n "Is there something else you're interested in?"

    scene 24lingeriestore with dissolve

    de "Fuck yeah there is."
    de "This fuckin' ass is what I'm interested in."
    de "Come on, bitch, every girl has her price."
    de "I got rolls like you wouldn't believe."
    de "So how much?"

    n "Oh!"
    n "So feisty!"
    n "Let's move this to the back so we can have some fun."
    n "We don't want any interruptions."

    scene 20lingeriestore

    bi "{i}This guy is a joke.{/i}"
    bi "{i}I can't believe he would talk to someone in such a demeaning way!{/i}"
    bi "{i}And she's playing right into it!{/i}"
    bi "{i}What is wrong with this woman?{/i}"

    scene 25lingeriestore

    de "Fuck yes!"
    de "Lead the way, bitch."
    de "I can't wait to taste that pretty little cunt."
    de "Mm!"

    n "Oh you bad boy!"
    n "This way."

    scene 26lingeriestore with dissolve

    bi "{i}I have to wait for this detective but...{/i}"
    bi "{i}This lady is about to get herself into some serious trouble.{/i}"
    bi "{i}That guy is going to hurt her.{/i}"
    bi "{i}I've got to stop this.{/i}"

    scene 27lingeriestore with dissolve

    bi "{i}They went down that way.{/i}"
    bi "{i}I can hear them in one of the changing rooms.{/i}"
    bi "{i}It's got to be...{/i}"

    scene 28lingeriestore

    bi "{i}That one.{/i}"

    de "Damn those titties are little."
    de "I bet they're still delicious though."

    n "Business before pleasure, Sweetie."
    n "It's two hundred dollars upfront."

    de "Pff, chump change!"
    de "Here's two Benjamins, bitch."
    de "Now take off those fuckin' clothes!"

    n "Let me just put the money away, Honey."

    de "God damn, hurry the fuck up."
    de "Wait, what's that?"
    de "What are you--"

    play sound "audio/taser.mp3"

    "*BZZT*"

    scene 29lingeriestore with dissolve

    de "Uhng!"

    scene 30lingeriestore with dissolve

    bi "{i}What the hell?{/i}"
    bi "{i}He's... out cold?{/i}"
    bi "{i}And she's--{/i}"

    scene 31lingeriestore with dissolve

    play music "audio/sneaking_up_on_you.mp3"

    n "Ehehe."

    bi "{i}She tased him??{/i}"
    bi "{i}And she's smiling.{/i}"
    bi "{i}Is she having fun with this?{/i}"
    bi "{i}What have I gotten myself into today?!{/i}"
    bi "{i}Shit, she's coming towards me.{/i}"

    scene 32lingeriestore

    n "[player_name], I presume?"

    b "How do you--"
    b "Wait, you're the detective?!"

    n "Please have a seat in the other room."
    n "I'll be right with you."

    b "R-right."
    b "Sure."

    scene 1lingerie2 with fadefast

    b "{i}So Nicole was actually the investigator from Penny for Your Thoughts
        this whole time?{/i}"
    b "{i}That was a really convincing performance. I'm glad I didn't take her
        offer.{/i}"
    b "{i}What if I had though? Would she have tased me!?{/i}"
    b "{i}She looks like a child though. How could she be a private detective?{/i}"
    b "{i}What did I get myself into?{/i}"

    scene 2lingerie2 with dissolve

    p "You're here!"
    p "I was afraid I may have scared you off with the disguise."
    p "And the taser."
    p "I apologize but after researching you, I was quite intrigued. I didn't
        want to delay this meeting so I overlapped it with another... engagement."

    scene 3lingerie2

    b "Intrigued? By what exactly?"
    b "I assure you, I'm just a regular Joe, Ms. Nicole."

    p "My name is Penny. Nicole is a pseudonym."

    b "Oh. Penny then."
    b "Wait, you chose Nicole because it sounds like... nickel?"

    p "Mhmm."

    b "Coin puns? Really?"

    scene 4lingerie2

    p "Anyway!"

    scene 2lingerie2 with dissolve

    p "You're here about your father, I presume?"

    b "No."

    p "Your sister, then?"

    b "Sharol? No. Well, sort of."

    p "Sharol? No, I mean--"
    p "Nevermind."

    scene 6lingerie2 with dissolve

    p "This is why I was intrigued. There are a lot of things goin' on with you,
        Mr. [player_name]."
    p "As astute as I usually am, I can't imagine which problem you've come to me for."

    b "Wow, you did your homework, huh?"
    b "And all in one night? That's impressive."

    p "I get that a lot."

    scene 7lingerie2 with dissolve

    b "I didn't think I had {b}that{/b} many problems but thinking about it, I guess
        I have had a rather dramatic life so far."

    p "So what are you here for specifically?"

    scene 8lingerie2 with dissolve

    b "My niece. She was sexually assaulted several months ago."
    b "I... I want to find the guy that did it."

    scene 11lingerie2

    p "I'm sorry to hear about that, [player_name]."
    p "I'll do what I can to help."

    scene 9lingerie2 with dissolve

    p "I'm sure I can find him for you."
    p "Is there anything you can tell me about him?"
    p "A name, home address, the color of his hair? Does he have any scars or tattoos?"

    scene 16lingerie2

    b "I don't know that much."
    b "I know his name is Seth and he's a dentist."

    scene 17lingerie2 with dissolve

    b "It's... it's not enough, is it?"
    b "My sister knows him!"

    scene 37lingerie2 with dissolve

    b "You could ask her, right?"
    b "Find out where she met him, search for clues there?"
    b "Maybe interview a few people, find out what they know."
    b "Or maybe study the tire treads on the ground from when he left her place! Yeah!"
    b "And find the make and model of his car by those treads, narrow it down to a few thousand
        vehicles, figure out which one was purchased near where Sharol met him..."

    scene 17lingerie2 with dissolve

    b "And then we'll find out there are only a few cars nearby that fit the description."
    b "And... and we show Sharol pictures of all the owners!"
    b "Wow, maybe I don't even need you."

    scene 12lingerie2 with dissolve

    p "Yeah, it looks like you've got it all figured out."
    p "You should do that and let me know how it works out for you."

    scene 13lingerie2

    b "I'm no stranger to sarcasm, Penny."
    b "Alright, fine, maybe I need your help a little bit."
    b "Where do we start?"

    scene 12lingerie2

    p "{b}We{/b} don't start anywhere."
    p "{b}I{/b} believe I already found him."

    scene 15lingerie2

    b "That's impossible!"
    b "We haven't even found the tire tracks yet!"

    scene 9lingerie2

    p "I did some research on Sharol last night. She used her insurance to
        pay for a dental appointment several months ago."
    p "If the man that hurt your niece really is a dentist as he said he was,
        I'm confident that's where she met him."
    p "The most likely suspect is a man named Tyler that works at the dental office
        Sharol went to. Seth was likely an alias to keep his
        identity a secret."
    p "Answers are often much simpler to find than we like to imagine, [player_name]."

    scene 15lingerie2

    b "I-- That--"

    scene 13lingerie2 with dissolve

    b "I was just about to recommend all that."

    scene 9lingerie2

    p "Let's discuss price, Mr. [player_name]."
    p "Usually I charge based on my client's wealth."

    b "I'm broke."

    scene 10lingerie2 with dissolve

    p "You're a terrible liar!"
    p "Your father gave you quite a sum, Sir!"
    p "I'll only char--"

    scene 15lingerie2

    b "Wait, what!?"
    b "How do you know about that!"
    b "I-- I mean, no! I got that money from a fitness app that I sold the rights to!"

    scene 12lingerie2

    p "Ooh. It was a secret, was it?"
    p "Well, I won't tell anyone."
    p "But this is going to set you back five thousand dollars."

    b "What!?"

    scene 11lingerie2 with dissolve

    p "A lot of people can't afford to hire me, [player_name]."
    p "People just like you who similarly need my help."
    p "I can do a lot of pro bono work with that money."

    scene 16lingerie2

    b "R-really?"

    p "And I'll put Tyler away for life, Mr. [player_name]. You can be sure of it."

    b "I'd be helping Avalon {b}and{/b} others..."
    b "Well, in that case,"

    scene 14lingerie2 with dissolve

    b "Deal!"

    scene 17lingerie2

    pause

    scene 18lingerie2 with dissolve

    p "Which credit card would you like to pay with?"

    b "Is that my wallet!?"
    b "You little thief!"

    scene 19lingerie2 with dissolve

    b "Give that back, you mischievous little pixie!"

    scene 20lingerie2 with dissolve

    p "Take this, you Degenerate!"

    scene 21lingerie2 with dissolve

    p "Hiyaa!"

    scene 22lingerie2

    e "Penny, don't you throw that--!"

    scene 23lingerie2 with vpunch

    pause

    scene 24lingerie2 with dissolve

    pause (.3)

    scene 25lingerie2 with dissolve

    e "Great. That's great."
    e "I come out here to help you and you hit me in the face with--"
    e "What is this? A wallet?"

    scene 26lingerie2

    p "Goodness me!"
    p "I thought you were that degenerate coming after me for revenge!"
    p "You shouldn't sneak up on people, Officer. You could get hurt."

    e "You knew it was me, Penny!"

    scene 28lingerie2 with dissolve

    p "Maybe I did. Maybe I didn't."
    p "Who can say for sure?"

    scene 27lingerie2

    e "Dammit, Penny. This is the last day I have to put up with this."
    e "The last day!"

    scene 29lingerie2 with dissolve

    e "Did she take this without your permission, Sir?"
    e "Did she steal this from you?"

    scene 30lingerie2

    b "Ye--"

    p "No, don't tell him!"

    scene 31lingerie2 with dissolve

    p "You'll get me in trouble!"

    b "Erm."

    scene 30lingerie2 with dissolve

    b "She, um..."

    scene 31lingerie2 with dissolve

    b "Well..."

    scene 30lingerie2 with dissolve

    b "Yeah, she stole it."

    scene 33lingerie2 with dissolve

    p "You dick."

    scene 32lingerie2

    e "You can't keep getting away with this crap, Penny!"

    p "You know I used a taser on the last guy that upset me."
    p "You know that, don't you, [player_name]?"

    e "You assaulted two people today, including a police officer."

    p "And that man that upset me? He's right outside of this room. Unconscious."

    e "And you stole a man's wallet!"

    p "He shit himself, [player_name]. Did you know that?"
    p "His pants are full of his own feces from being tased. By me. Because he upset me."

    e "You should be facing serious criminal charges, Penny!"
    e "And that's only for what you've done this morning!"

    p "I advise wearing a diaper from now on, [player_name]. Fair warning."

    scene 34lingerie2

    e "I just... I can't. I can't do it anymore."
    e "Tomorrow, I make detective and you'll be someone else's problem."

    p "Don't be so dramatic!"
    p "I stopped a criminal for you!"

    scene 35lingerie2 with dissolve

    e "Here's your wallet back, Sir."

    b "Oh, thank you."

    scene 36lingerie2 with dissolve

    e "Wrap this meeting up, Penny!"
    e "You're going to help me carry this piece of dirt to my patrol car."

    scene 28lingerie2 with dissolve

    p "Fine!"
    p "Your flashlight is on, by the way."

    scene 12lingerie2 with dissolve

    p "He's in a mood today."
    p "I should help him out so let's finish up here."
    p "I'll text you my account information so you can wire the money."

    scene 7lingerie2 with dissolve

    b "I appreciate your help, Penny."
    b "Thank you."

    scene 38lingerie2 with dissolve

    b "I didn't get you in trouble, did I?"

    p "Ha. No."

    b "What's the plan moving forward?"
    b "What's your next move?"

    scene 39lingerie2 with dissolve

    p "You seem to fancy yourself a junior detective."
    p "What do you think I should do?"
    p "Penny for your thoughts?"

    play sound "audio/coinflip.mp3"

    scene 40lingerie2 with dissolve

    b "What the--?"

    scene 41lingerie2 with dissolve

    b "What is this?"

    scene 68lingeriestore

    b "A penny?"
    b "Very clever!"
    b "Well, I think you should--"

    scene 42lingerie2

    b "Gah! She's gone!"
    b "I've been tricked!"

    stop music fadeout 2.0

    scene 64lingeriestore with dissolve

    bi "{i}I have to admit, this whole thing was pretty exciting.{/i}"
    bi "{i}Penny seems like a very unusual person. {/i}"
    bi "{i}I can't really pin down her personality type.{/i}"
    bi "{i}But if she can help, I really don't care how weird she is.{/i}"

    scene 65lingeriestore with dissolve

    bi "{i}Hmm?{/i}"
    bi "{i}What's that?{/i}"

    scene 67lingeriestore with dissolve

    bi "{i}Wow, is that what I think it is?{/i}"
    bi "{i}I didn't know they sold those here.{/i}"
    bi "{i}I wonder if Avalon would appreciate one of those..?{/i}"
    bi "{i}No way, that's crazy!{/i}"
    bi "{i}But maybe...{/i}"

    scene 1thegift with fade

    ai2 "{i}I bought so many cute outfits today!{/i}"
    ai2 "{i}I can't wait to wear them all.{/i}"
    ai2 "{i}I'm glad they had the hair dye I was looking for.{/i}"
    ai2 "{i}I think it's time to go back to my natural color.{/i}"

    scene 2thegift with dissolve

    ai2 "{i}And tonight, I bought something special to wear.{/i}"
    ai2 "{i}I really hope Uncle [player_name] likes it...{/i}"

    scene 3thegift

    play music "audio/touching_moment.mp3"

    b "Avalon?"
    b "I bought something for you."
    b "Would you like to open it?"

    scene 4thegift

    a2 "That gift is for me?"
    a2 "I was wondering what that was."
    a2 "Did you get it at the lingerie shop?"

    scene 6thegift

    b "I did."
    b "They had some... 'things' for sale other than lingerie."
    b "I thought this might be something you would appreciate."

    scene 5thegift

    a2 "Thank you, Uncle."
    a2 "That's very sweet."
    a2 "But are you sure?"
    a2 "I know how you like to save money and this seems a bit frivolous."

    scene 6thegift

    b "You can consider this a gift for saving so much money today."
    b "I don't know how you spent so little and got so much."
    b "It looks like you're better at being frugal than I am!"

    scene 5thegift

    a2 "I found coupons on my phone and there were some really great 'buy one,
        get one' deals today!"
    a2 "And since they didn't have any stipulations on combining promotions,
        I got some outfits for a steal!"

    scene 7thegift with dissolve

    ai2 "{i}Hmm...{/i}"
    ai2 "{i}I'm really curious what he would have found at a lingerie store
        that isn't lingerie.{/i}"

    scene 8thegift

    b "Okay, so, before you open this..."
    b "Just remember, i-it's just a gift for you to use when, and if, you want."
    b "And it's not a big deal or anything so..."

    scene 9thegift

    ai2 "{i}What an adorable little box.{/i}"
    ai2 "{i}It's got a cute bow tie on top and everything.{/i}"
    ai2 "{i}Now let's see here, I think the top just pops off?{/i}"

    scene 10thegift with dissolve

    ai2 "{i}Aha!{/i}"
    ai2 "{i}And inside we have...{/i}"
    ai2 "{i}Hmm, what is this thing?{/i}"
    ai2 "{i}A plastic, cylindrical shaped object...{/i}"

    scene 11thegift with dissolve

    stop music fadeout 2.0

    ai2 "{i}Is this?!{/i}"
    ai2 "{i}Is this what I think it is!?{/i}"
    ai2 "{i}It is!{/i}"
    ai2 "{i}What the hell??{/i}"

    scene 12thegift with dissolve

    a2 "Uncle, this is..!"
    a2 "Why would you give this to me??"
    a2 "This is really inappropriate!"
    a2 "What were you thinking??"

    scene 15thegift

    b "Shit!"
    b "I'm so sorry!"
    b "I don't know why I got you that, it was a terrible idea!"
    b "Please forgive me!"

    scene 16thegift

    b "I'll take it back right away."
    b "And we'll just forget this ever happened."

    scene 13thegift

    a2 "No!"
    a2 "I..."
    a2 "I want it..."
    a2 "I was just surprised."
    a2 "That's all."

    scene 17thegift

    b "Are... you sure?"
    b "I thought it might be something you would enjoy."
    b "But if it's not, we can get rid of it."
    b "It's really no big deal!"

    scene 14thegift

    a2 "I've never had a toy before."
    a2 "I don't even know how it works."
    a2 "Can you..."
    a2 "Can you show me?"

    scene 18thegift

    menu:
        m2 "If you choose not to, we simply skip a small scene where [player_name] shows Avalon how to use the toy. You decide!"
        "Uhh, sure.":
            jump toy_play

        "That wouldn't be appropriate.":
            jump toy_skip


label toy_play:
    if _in_replay:
        $ player_name = renpy.input("What would you like to name the MC?")
        if player_name.strip() == "":
          $ player_name = "Byron"

    play music "audio/cause.mp3"

    b "I think I've got a pretty basic idea of how it works."
    b "If you're sure that's what you want, I can show you."

    scene 19thegift with fade

    b "See the button just above my thumb here?"
    b "If you press that button, it turns on."
    b "And then you rotate the bottom to increase intensity."
    b "Like this."

    scene 20thegift with dissolve

    "*Bzzz.*"

    scene 21thegift with dissolve

    a2 "Oh!"
    a2 "I can hear it."

    b "It's actually quite fierce."
    b "I didn't realize how powerful it was going to be."
    b "Go on, feel it."
    b "Touch the tip with your finger."

    a2 "O-Okay."

    scene 22thegift with dissolve

    a2 "Wow, that is really intense."
    a2 "It's so much more potent than my cell phone when it vibrates."
    a2 "How does it do that?"

    scene 23thegift

    b "There's a motor inside that spins a small weight."
    b "It simulates the effect of vibration."

    a2 "And it feels good when you use it on yourself?"

    b "Yeah, let me show you."

    scene 24thegift

    b "If you press it to your skin like this, it triggers a tingling sensation."
    b "Do you feel it?"

    a2 "Uh-huh."

    b "And you can start moving it around to get used to it."

    scene 25thegift with dissolve

    b "Run it along your skin slowly."
    b "Concentrate on the part of your body that it's on."
    b "Do you feel your body getting warmer?"

    a2 "Yeah."

    b "You're getting a little bit excited?"

    a2 "Mhmm..."

    b "How about..."

    scene 26thegift with dissolve

    b "Now?"

    a2 "Oh!"
    a2 "Uncle, it's really sensitive there!"
    a2 "It's too much!"

    b "Turn around."

    a2 "W-what?"

    b "Face the other direction."

    a2 "Okay..."

    scene 27thegift with fade

    b "Just like when you exercise, you want to warm up first."
    b "Once you're starting to feel more aroused, you can start moving down."
    b "There's no reason to rush, you want to take your time."
    b "Enjoy the experience and savor the feelings."

    scene 28thegift with dissolve

    a2 "Are you sure we should keep going?"
    a2 "This.. might be too fast."

    b "Do you want me to stop?"

    a2 "I..."
    a2 "No..."

    scene 29thegift with dissolve

    b "The more we move down, the more profound the pleasure will be."
    b "And the anticipation of where we're going to go next can be just as enticing."
    b "Do you know where we're going to go next?"

    a2 "W-where..?"

    scene 31thegift with dissolve

    b "Here."

    a2 "That's... so close..!"

    b "Close to what?"

    a2 "Close to a {b}really{/b} sensitive area, Uncle!"

    scene 32thegift with dissolve

    a2 "I can feel your hand on my stomach, too."
    a2 "It's like all the places on me that you're touching are on fire."

    b "Because you're so stimulated, you're extra aware of everywhere I'm touching
        you."
    b "Can you feel my body pressing into yours?"

    a2 "Yes, I really can!"

    b "And how do you feel..."

    scene 33thegift with dissolve

    b "Now?"

    a2 "Mmf!"

    b "Your body is getting so hot, Avalon."
    b "I can feel the heat radiating off of you."
    b "Let's see what happens if we do..."

    scene 34thegift with dissolve

    b "This."

    a2 "Oh!"

    b "How is this?"

    a2 "I can't..!"
    a2 "It's too much!"

    scene 35thegift with dissolve

    a2 "Uncle, if you touch me there..!"
    a2 "I feel like I'm about to explode!"
    a2 "I'm going to--"

    stop music fadeout 2.0

    scene 36thegift

    play sound "audio/bodyfallmat.mp3"

    a2 "Oof!"

    scene 37thegift with dissolve

    a2 "Wha.."
    a2 "Did you..?"

    scene 38thegift with dissolve

    a2 "Did you just push me down?"
    a2 "What the hell, Uncle?!"
    a2 "Why did you do that??"

    scene 39thegift

    b "Remember this morning, when you climbed up on the table and leaned
        in for a kiss?"
    b "And then you got up and left without following through with it."
    b "Payback is a bitch, ain't it?"

    scene 41thegift

    a2 "Are you serious!?"
    a2 "You went through all that just to get back at me??"
    a2 "That's so devious!"

    scene 40thegift

    b "I will always beat you at your little games, Avalon."
    b "You will lose every time."

    scene 41thegift

    a2 "I'm actually impressed."
    a2 "I didn't think you would go to such lengths to get me back."
    a2 "You know this means war, though, right?"

    scene 42thegift

    b "As I said, I'll win in the end."
    b "You better be prepared for the consequences."
    b "It sure looked like you were enjoying the gift though."
    b "I think your nipples are poking through your sweater."

    scene 43thegift

    a2 "Probably!"
    a2 "That little thing is wild!"
    a2 "My vagina is on fire right now."
    a2 "I'm going to have to change my underwear."
    a2 "I can't believe you denied me the ending..."

    scene 44thegift

    b "Here, take it."
    b "It's all yours."
    b "You can have as many 'endings' as you'd like."
    b "And you can show it off to one of your girlfriends if you want."
    b "Come meet me in the living room when you're all fixed up."
    b "There's actually a lot I want to discuss with you."

    scene 45thegift

    if persistent.showme == False:
        $ renpy.notify("You've unlocked 'Show Me' in the Scene Gallery on the Main Menu!")
        $ persistent.showme = True

    a2 "Okay, I'll be right there."
    a2 "And thank you for the present!"

    $ renpy.end_replay()
    jump dont_go

    label toy_skip:

    scene 18thegift

    b "Actually, I got that for you so that you could experiment with it on your
        own."
    b "It's a very basic vibrator."
    b "You just press the 'On' button and... well, you know the rest."
    b "I have some things I'd like to talk to you about."
    b "Meet me on the couch when you're all done?"

    scene 13thegift

    a2 "Uhm."
    a2 "Alright."
    a2 "Let me just put this away and I'll be right there."

    label dont_go:

    scene 1dontgo with fade

    bi "{i}I've been putting off talking to her about what happened
        with the detective.{/i}"
    bi "{i}But I need to do it.{/i}"
    bi "{i}I don't think she understands why I need to get this guy.{/i}"
    bi "{i}It's just... it's important!{/i}"

    if octavia == True:
        bi "{i}I invited Octavia over, she should be here shortly.{/i}"
        jump after_invited

    else:
        bi "{i}I invited Dallas over, she should be here shortly.{/i}"
        jump after_invited


    label after_invited:

    bi "{i}Her and Avalon can have some girl time while I clear my head at the gym.{/i}"
    bi "{i}Hmm, I wonder if it would help her recover faster if she fooled around with
            a girlfriend first.{/i}"
    bi "{i}Would I be alright with something like that though?{/i}"

    menu:
        "{b}Game Altering Choice{/b}\nMonogamy: One Sexual Partner\nPolyamory: Multiple Sexual Partners"
        "Monogamy":
            $ monogamy = True
            $ polygamy = False
            b "No, she shouldn't be with anyone else."
            b "I should be all that she needs."
        "Polyamory":
            $ polygamy = True
            $ monogamy = False
            b "Yeah, why not, right?"
            b "It might be easier for her to be intimate with a female companion."

    scene 2dontgo

    a2 "Alright, Uncle, I'm ready to chat!"

    scene 4dontgo with dissolve

    a2 "So what did you want to talk about?"
    a2 "It sounded important but with you, you never know."
    a2 "Maybe you just need me to explain how babies are made?"

    scene 5dontgo

    b "Damn, your quips are getting so good."
    b "It's like watching a gorgeous version of me except with nicer boobs."
    b "Please have a seat."

    scene 6dontgo

    b "Listen, I wanted to talk to you about us for a moment."
    b "More specifically, I wanted to talk to you about me."
    b "Yesterday we were just Uncle and Niece."
    b "We took a giant leap overnight."
    b "I know we're moving fast."
    b "I don't think either of us can stop that."
    b "I don't think we would want to!"
    b "But there are things you need to know about me."

    play music "audio/no_goodbyes.mp3"

    scene 7dontgo with dissolve

    pause

    scene 8dontgo with dissolve

    a2 "I've known you for a long time, Uncle."
    a2 "What could you tell me about you that I don't already know?"

    scene 11dontgo

    b "There's a reason I've been single all these years."
    b "I'm not good at relationships."
    b "I've been alone most of my life."
    b "Even when I was around people, I still felt like I was alone..."
    b "I've gotten so used to it, I don't really know how to be more than... just me."
    b "You understand?"

    scene 16dontgo

    a2 "Yeah, I understand."
    a2 "Except that you're forgetting something."
    a2 "A {b}big{/b} something."

    scene 15dontgo

    b "I don't think I am."
    b "What do you think I'm forgetting?"

    scene 8dontgo

    a2 "Uncle, there's always been one person that you've gravitated towards."
    a2 "One person you always wanted to be around."
    a2 "Come on, you jumped through hoops to see me!"
    a2 "If there's anyone you should be with, it's me."

    scene 13dontgo

    b "I... I didn't really think about that."
    b "I just didn't want to catch you off guard if--"

    scene 16dontgo

    a2 "If you need some alone time once in a while?"
    a2 "Uncle, I'll need space sometimes too."
    a2 "Don't worry so much!"

    scene 9dontgo

    b "Okay, that's fair."
    b "We'll work it out as we go."
    b "I'm just nervous, I guess."

    scene 10dontgo

    a2 "I'm... nervous too."
    a2 "I'm afraid I pushed myself into a relationship with you because I need
        support right now."
    a2 "And I need something that will remind me that the world isn't all bad."
    a2 "I know we should have moved slower but... I need this."
    a2 "I need you."

    scene 17dontgo

    b "Man, if I had a nickel for every time I heard a lady say that to me."
    b "I'd have like, jars full of nickles."
    b "Jars and jars."
    b "So many jars."

    scene 16dontgo

    a2 "Okay, things got too serious so you have to make a joke to lighten the
        mood."
    a2 "It's kind of annoying sometimes!"

    scene 14dontgo with dissolve

    a2 "But... it's also kind of nice."
    a2 "I don't like it when things are too serious either."

    scene 15dontgo

    b "Well, while we're being so serious."
    b "I wanted to explain why I bought that gift for you."
    b "I... like sex."
    b "Sex is kind of amazing."

    scene 12dontgo

    a2 "I-I know that."
    a2 "And, you know, we will..."
    a2 "One day."
    a2 "Probably..."

    scene 17dontgo

    b "Calm down, Avalon."
    b "I just mean that I think it might be a while before we take that step."
    b "Because... you know."
    b "The incident."
    b "And I thought a toy might help you discover, or rediscover, your sexuality."
    b "You'll have full control over the situation if it's a solo endeavor."

    scene 14dontgo

    a2 "That... makes sense."
    a2 "Actually, that makes a lot of sense."

    scene 17dontgo

    b "It made sense until you asked me to show you how it works."
    b "I actually didn't expect that."
    b "It seems like you're healing a lot faster than I'd imagine someone could."
    b "I don't know how, or why, but--"

    scene 10dontgo

    a2 "It's... because of you."
    a2 "I don't feel sad anymore."
    a2 "When I'm with you, I don't hurt anymore..."

    scene 17dontgo

    b "I'm glad to hear that."
    b "But I still want you to take your time with the more intimate relationship
        experiences."
    b "At least with me."
    b "Just... for my own peace of mind."

    if monogamy == True:
        jump monogamy1
    else:
        jump polygamy1

    label polygamy1:

    b "And that's why I was going to say..."

    scene 15dontgo with dissolve

    b "If you want to play around with, you know, one of your girlfriends..."
    b "I'm alright with that."
    b "It would probably be easier with a girl, right?"
    b "And I know you and Dallas had a thing once."

    scene 12dontgo

    a2 "How'd you know that??"
    a2 "Oh my god, did Mom tell you she walked in on us!?"
    a2 "That was so long ago!"

    scene 14dontgo with dissolve

    a2 "Why... would you be alright with that though?"
    a2 "It's cheating, isn't it?"

    scene 17dontgo

    b "I'm not threatened by the prospect of you leaving me for a woman."
    b "It's hard to explain but I really don't mind if you have a little fun
        with a girlfriend."

    scene 16dontgo

    a2 "Do you want to watch?"

    scene 13dontgo

    b "C-could I?"

    scene 16dontgo

    a2 "Nope."

    scene 17dontgo

    b "Fair enough."

    label monogamy1:

    b "I also wanted to tell you about what happened with the detective."
    b "The whole thing was pretty bizarre."
    b "I'm still trying to wrap my head around it."

    scene 14dontgo

    a2 "I was wondering when you were going to tell me about that."
    a2 "I've been curious but I didn't want to pry."

    scene 15dontgo

    b "Well, it turned out that the investigator happened to be a woman."
    b "And she tried to seduce me at first."

    scene 12dontgo

    a2 "What?!"
    a2 "What the hell kind of investigator does that?"
    a2 "Uncle, I think you accidentally hired a hooker."

    scene 9dontgo

    b "She was undercover, apparently."
    b "I guess she just booked my appointment at the same time she was pursuing
        a drug dealer."
    b "Apparently, she came on to me as... practice?"
    b "She offered herself to me for eighty bucks."

    scene 12dontgo

    a2 "Eighty dollars!?"
    a2 "Wow, that's a really good deal..."

    scene 13dontgo

    b "That's exactly what I said!"

    scene 9dontgo with dissolve

    b "But I didn't take the deal."
    b "The other guy did though."
    b "You should have seen it!"
    b "She lured him in with the promise of sex, led him to a changing
        room and zapped him with a taser."

    scene 14dontgo

    a2 "She used sex to manipulate him into doing exactly what she wanted?"
    a2 "Wow, that's... exciting."
    a2 "Hmm..."

    scene 9dontgo

    b "Afterwards, we had a meeting in another room."
    b "She's surprisingly cunning but also very..."
    b "I don't know what word to even use."
    b" Playful?"
    b "She's very confident she can find the guy though."
    b "In fact, she might have already found him."

    scene 12dontgo

    a2 "What!?"
    a2 "Is that even possible??"
    a2 "How?"

    scene 9dontgo

    b "With her phone."
    b "She did a quick search on her cellphone and found him right away."
    b "Apparently, he might actually go by Tyler."
    b "I hired her."
    b "I had to!"
    b "She's absolutely bananas but she's also incredible!"

    scene 14dontgo

    a2 "Okay."
    a2 "That's good, I guess."
    a2 "How much did she charge?"

    scene 13dontgo

    stop music fadeout 2.0

    b "W-well, it was kind of expensive."
    b "But she's worth it!"
    b "She charged, erm..."
    b "Five thousand."

    scene 18dontgo

    a2 "Five thousand dollars?"
    a2 "Are you kidding me?"
    a2 "What the hell were you thinking?"

    scene 13dontgo

    b "It's worth it!"
    b "It's worth it to have this guy put behind bars."
    b "I'd... I'd pay anything to--"

    scene 18dontgo

    a2 "To get revenge?"
    a2 "I asked you to let it go."
    a2 "I begged you to leave it alone."
    a2 "And now you're spending that kind of money after I pleaded?"

    scene 11dontgo

    b "I have to, Avalon."
    b "What if I don't and he hurts someone else?"
    b "What if he does what he did to you to other people?"
    b "What if he does worse..?"

    scene 21dontgo

    a2 "And what if he hurts you?"
    a2 "What if he {b}kills{/b} you?!"
    a2 "What do I have when you're gone?"
    a2 "Did you think about that at all?"

    scene 15dontgo

    b "Why would he come after me?"
    b "He doesn't know--"

    scene 18dontgo

    a2 "You think he won't find out?"
    a2 "Are you sure?"
    a2 "Would you bet your life on it?"
    a2 "Would you bet mine?"

    scene 22dontgo

    b "N-no, I wouldn't do that!"
    b "He won't find out though!"
    b "How could he?"

    scene 10dontgo

    a2 "Just tell me you're done, Uncle."
    a2 "Just say that you've done as much as you're going to do."
    a2 "The investigator you hired will handle it from here and you
        don't have to do anything else with it."
    a2 "Tell me that."

    scene 13dontgo

    b "I-I'm done."
    b "I am!"
    b "I hired Penny, she'll take care of it from here."
    b "If--"
    b "{b}When{/b} she finds something incriminating on him, she'll submit it
        to the authorities."
    b "It's finished."

    scene 8dontgo

    a2 "Good."
    a2 "Thank you, Uncle."
    a2 "Now what's the plan for the rest of the day?"

    if octavia == True:
        jump octavia_dontgo
    else:
        jump dallas_dontgo

    label octavia_dontgo:

    ##Octavia Act Three

    scene 9dontgo

    b "I haven't been to the gym in a while."
    b "I invited Octavia over for a bit."
    b "I figured you could spend time with her while I go exercise?"
    b "I won't be long."

    scene 16dontgo

    a2 "Oh yeah?"
    a2 "Those guns aren't going to polish themselves, huh?"

    scene 17dontgo

    b "Exactly!"

    play sound "audio/doorbell.mp3"
    "*Ding Dong*"

    scene 15dontgo with dissolve

    b "That should be her now, actually."

    scene 1octdontgo with fade

    b "Octavia!"
    b "Please come in."
    b "Thank you so much for coming."

    o "[player_name], it's so nice to see you again."
    o "How are you?"

    b "I'm doing well."

    scene 2octdontgo with dissolve

    b "No glasses today?"

    o "Oh."
    o "No, I decided to wear contacts instead."

    b "You look lovely without."

    o "You're too kind, [player_name]."

    scene 3octdontgo

    a2 "Hey Octavia!"
    a2 "Wow, you look so pretty today!"

    scene 4octdontgo

    o "Thank you!"
    o "And I like the new look you're trying out."

    scene 3octdontgo

    a2 "It's actually an old look."
    a2 "I got a whole bunch of new clothes today!"
    a2 "I can't wait to show you!"

    scene 5octdontgo

    o "Sure!"
    o "I'd love to see what you got!"

    scene 6octdontgo

    a2 "Mm, I really like your hugs."
    a2 "They're so soothing."

    o "Aw."
    o "You can have as many as you want."

    b "Octavia, I've got to run out for a bit."
    b "But I'll be back shortly."

    o "Alright."
    o "Sounds like we're going to have more girl time, Avalon."

    scene 7octdontgo

    a2 "I actually thought this day would go in a completely different direction."

    o "Me too."
    o "I like the way it's going right now though!"

    jump tyler_house

    ##Dallas Act Three

    label dallas_dontgo:

    scene 9dontgo

    b "I haven't been to the gym in two days."
    b "I invited Dallas over for a bit."
    b "I figured you could spend time with her while I go exercise?"
    b "I won't be long."

    scene 16dontgo

    a2 "Oh yeah?"
    a2 "Those guns aren't going to polish themselves, huh?"

    scene 17dontgo

    b "Exactly!"

    scene 8dontgo

    a2 "When do you think you'll be--"

    scene 1daldontgo with dissolve

    d "What're you guys doin'?"

    a2 "Gah!"

    scene 3daldontgo with dissolve

    d "What??"
    d "What happened?"

    a2 "You just let yourself in!?"
    a2 "That's so rude!"
    a2 "You didn't even knock!"

    d "You invited me over!"
    d "You knew I was coming, why would I knock?"

    a2 "What if we were... indisposed?"

    scene 2daldontgo with dissolve
    d "Were you??"
    d "Did I miss something sexy??"

    scene 3daldontgo with dissolve

    a2 "N-no, we were just--"
    a2 "Hey, don't distract me!"
    a2 "You're an intruder!"

    scene 5daldontgo with fade

    d "So what's goin' on?"
    d "Looked like you guys were gettin' pretty chummy."

    a2 "Why are you wearing a bathing suit top..?"

    d "You don't like it?"
    d "I can take it off if you want."

    scene 4daldontgo

    a2 "You slut."
    a2 "[player_name] is going to the gym so we'll have some girl time until he gets back."

    scene 6daldontgo with dissolve

    b "I shouldn't be long."

    scene 7daldontgo

    d "Don't overdo it, [player_name]."
    d "An ol' ticker like yours could give out under too much stress."
    d "Make sure you've always got some baby aspirin with you."

    scene 6daldontgo

    b "Why are you wearing half of a jacket?"
    b "Did you buy that thing at Baby Gap?"
    b "Do they charge per inch of fabric now or something?"

    scene 5daldontgo

    d "Hey, let's watch that movie you were talking about the other day."

    a2 "Oh yeah!"
    a2 "Sure, that sounds good!"

    scene 7daldontgo with dissolve

    d "See ya later, [player_name]."

    label tyler_house:

    scene 1tylerhouse with fade

    play music "audio/sneaking_up_on_you.mp3"

    pause

    scene 2tylerhouse with dissolve

    pause (.3)

    scene 3tylerhouse with dissolve

    pause (.3)

    scene 4tylerhouse with dissolve

    pause

    scene 5tylerhouse

    pause

    scene 6tylerhouse with dissolve

    pause (.2)

    scene 7tylerhouse

    pause (.2)

    scene 6tylerhouse

    pause (.2)

    scene 8tylerhouse

    pause

    scene 9tylerhouse with dissolve

    pause

    scene 10tylerhouse

    "*Click*"

    scene 11tylerhouse

    pause (.5)

    scene 12tylerhouse

    pause (.5)

    scene 13tylerhouse with dissolve

    pause

    scene 14tylerhouse

    pause

    scene 15tylerhouse

    pause

    scene 17tylerhouse with dissolve

    pause

    scene 16tylerhouse

    ps "You, Miss Faith, are just cute as a button, aren't you?"
    ps "What secrets are you hiding..?"

    scene 18tylerhouse

    pause

    scene 19tylerhouse with dissolve

    pause

    scene 20tylerhouse

    pause

    scene 21tylerhouse with dissolve

    pause

    scene 22tylerhouse with dissolve

    pause

    scene 23tylerhouse with dissolve

    stop music fadeout 2.0

    ps "Oh?"

    scene 24tylerhouse

    play sound "audio/wood_footsteps.mp3"

    ps "Hm?"

    stop sound

    play sound "audio/dooropen.mp3"

    scene 25tylerhouse

    play music "audio/impulse.mp3"

    pause

    scene 26tylerhouse

    pause

    scene 27tylerhouse

    t "I know you're here."
    t "I heard you skitter across the room like a cockroach."
    t "What are you doing in my home?"

    scene 26tylerhouse

    pause

    scene 28tylerhouse

    pause

    fg "Daddy?"

    scene 29tylerhouse

    t "What the hell..?"
    t "Faith?"

    fg "I can't believe you bought me a bicycle!"
    fg "Thank you so much, Daddy!"

    scene 30tylerhouse

    stop music fadeout 2.0

    pause

    scene 31tylerhouse with dissolve

    t "What is this?"

    scene 19tylerhouse with dissolve

    t "It's a... speaker?"
    t "Damn!"

    scene 27tylerhouse with dissolve

    t "It's a decoy!"
    t "Don't expect me to fall for that twice!"
    t "I'll get you next time..."

    if octavia == True:
        jump aroom_oct
    else:
        jump aroom_dal

    label aroom_oct:

    scene 1aroomoct with fade

    a2 "And this is my room!"
    a2 "Well, I mean, I guess it's Uncle [player_name]'s room."
    a2 "But he lets me use it."

    scene 2aroomoct

    o "Wow!"
    o "It's decorated in a feminine fashion."
    o "But you just moved in."
    o "Does that mean [player_name] has had this room for you for a while?"

    scene 1aroomoct

    a2 "Oh, yeah, I mean, it's sort of always been for me."
    a2 "I used to stay here once in a while."
    a2 "[player_name] kept it for me even while we weren't really speaking."

    scene 4aroomoct

    o "Maybe he was always hoping you'd come back into his life."
    o "And as fate would have it, here you are!"

    scene 3aroomoct

    a2 "Octavia, I was wondering..."
    a2 "Umm."
    a2 "That thing we did at the pool?"
    a2 "Can we... can we do that again?"

    scene 4aroomoct

    o "Oh, sure."
    o "I'd be happy to!"
    o "You'll need to wear something more comfortable for it to work."
    o "Do you have something you can change into?"

    scene 1aroomoct

    a2 "I have a bathing suit I was wearing this morning to exercise."
    a2 "It was really comfortable."

    scene 2aroomoct

    o "I'll wait outside while you get dressed."
    o "When you're ready, just lie down on the bed and we'll get started."

    a2 "Okay, thank you, Octavia!"

    scene 5aroomoct with fade

    o "Avalon, before we start, I want to explain to you what this is."
    o "It's a form of hypnosis to help you relax."

    a2 "Oh."
    a2 "Why didn't you tell me before?"

    o "I didn't know if you had a preconceived notion of what hypnosis was."
    o "I wanted you to experience it yourself so you would know whether you liked or disliked it."

    scene 6aroomoct with dissolve

    a2 "Like cheesecake?"

    o "Cheesecake?"

    a2 "Yeah, people call it cheesecake but it doesn't taste anything like cheese."
    a2 "It's actually sweet and creamy."
    a2 "So if you tell someone, you know, 'Have some cheesecake!'"
    a2 "They might respond 'Ugh, I hate cheese!'"
    a2 "So it's better just to let them taste it first."

    scene 7aroomoct

    o "Yes, that's a very good analogy!"
    o "That's quite clever, Avalon."
    o "Are you ready to get started?"

    scene 5aroomoct

    a2 "Yeah, I'm ready."

    o "I've found the best way for me to connect to the person I'm with
        is through physical contact."
    o "I'm going to place my hand on you and you just tell me if you're uncomfortable."
    o "Alright?"

    a2 "A-alright, sure."

    scene 10aroomoct with dissolve

    o "I'm going to place one hand on your chest here."

    a2 "Okay, yeah, that's... that's fine."
    a2 "Your hands are really warm."

    o "And one hand..."

    scene 11aroomoct with dissolve

    o "Here."

    a2 "Oh!"
    a2 "Alright, y-yes, that's fine."

    o "Your heart is racing."
    o "Please let me know if you're uncomfortable."

    a2 "N-no, it's just..."
    a2 "It feels... intimate?"

    o "It should."
    o "Physical contact helps connect you and I to each other."
    o "Sort of like building a bridge between two points."

    scene 8aroomoct

    play music "audio/let_her_go.mp3"

    a2 "I think I understand."
    a2 "What happens now?"

    o "Take a moment to get used to my hands."
    o "Allow your heart to slow a bit."
    o "Take a deep breath."
    o "And release."

    scene 9aroomoct with dissolve

    o "Focus your attention on my hand resting against your chest."
    o "Feel the pressure against your skin and the warmth from my palm and fingers."
    o "Take another deep breath."
    o "And let it out."

    scene 12aroomoct with dissolve

    o "Imagine laying outside in a field of grass."
    o "With the sun beating down on your bare skin."
    o "And the clouds are slowly drifting in the sky."
    o "Take another deep breath."
    o "And let it out."

    scene 13aroomoct with dissolve

    o "Is there anything specific you want to talk about today, Avalon?"

    scene 14aroomoct with dissolve

    a2 "Yeah."
    a2 "I want to talk about [player_name]."

    scene 13aroomoct with dissolve

    o "How are things going with you and [player_name]?"

    scene 14aroomoct with dissolve

    a2 "We're seeing each other now."
    a2 "I asked him for a kiss last night and then we just sort of..."
    a2 "Fell into each other."
    a2 "I'm so happy that, sometimes, I feel like I'm going to burst."
    a2 "The only thing is..."

    o "Yes?"

    scene 15aroomoct with dissolve

    a2 "He won't let it go."
    a2 "The guy that hurt me, he won't quit pursuing him."
    a2 "I told him I don't care about him anymore."
    a2 "I told him to let it go."
    a2 "But he won't..."
    a2 "He hired a private detective for an outrageous amount of money."

    o "Who?"

    a2 "I guess her name is Penny."

    o "Penny!?"
    o "Oh, uhh, c-continue."

    scene 16aroomoct with dissolve

    a2 "I just want to move on and enjoy my life."
    a2 "I don't want to dwell on the past or on things I can't change."

    o "Why do you think he's pursuing this?"

    a2 "I don't know."

    o "Why aren't you?"

    a2 "Because while it's the worst thing that's ever happened to me,"
    a2 "it's also the best."

    scene 14aroomoct with dissolve

    a2 "It brought me to Uncle [player_name]."
    a2 "And when I'm wrapped up in his arms, I know that nothing bad will happen again."
    a2 "Sometimes I think I had to endure that one terrible moment so the rest
        of my life could be..."
    a2 "Bliss."
    a2 "With him."

    scene 17aroomoct with dissolve

    a2 "Mm."

    o "What are you thinking about, Avalon?"

    a2 "Uncle bought me a toy today."

    o "A toy?"

    a2 "A vibrating toy."

    o "Oh!"

    a2 "I've never had one before."
    a2 "I'm kind of excited to try it."
    a2 "I haven't had a release in a while."

    if monogamy == True:
        jump monogamy2
    else:
        jump polygamy2

label polygamy2:
    if _in_replay:
        $ player_name = renpy.input("What would you like to name the MC?")
        if player_name.strip() == "":
          $ player_name = "Byron"
    scene 18aroomoct

    a2 "I'm actually feeling very aroused right now though."

    o "Oh you poor girl."
    o "I'm sorry I can't help you."

    a2 "Do..."
    a2 "Do you want to?"

    scene 19aroomoct

    o "I'm not going to let you cheat on [player_name]."
    o "It wouldn't be right."

    a2 "He says I can play with girls."
    a2 "Just not guys."

    o "Oh?"
    o "Well, as long as he's alright with it, I can take care of you."
    o "Since you're already warmed up, let's start..."

    scene 20aroomoct with dissolve

    o "Here."

    a2 "Oh!"
    a2 "Mmhn."

    o "Wow."
    o "You're so warm down here, Avalon."
    o "You really need this, don't you?"

    a2 "Yeah."
    a2 "I haven't been getting aroused very often. Not since... Well, you know."

    o "I understand."
    o "Let's try a little movement."

    show octaviatreatment

    a2 "Ung!"
    a2 "Please don't stop!"

    o "You shouldn't go so long without relief, Avalon."
    o "I want you to start taking care of yourself."

    a2 "I-I will."
    a2 "Uuunn!"

    o "Let's add some more stimulation."

    scene octaviatreatment2

    a2 "Ohoh!"
    a2 "Yes, like that!"

    o "Masturbating is a great way to release stress."
    o "You'll become frustrated and aggressive if you don't treat yourself once in a while."
    o "You understand?"

    a2 "I understand."
    a2 "I'll--"

    scene 28aroomoct

    a2 "OH GOD!"
    a2 "I'm cumming!"

    o "My goodness, Avalon."
    o "Your orgasms are so intense."

    scene 29aroomoct

    a2 "Oh god!"

    o "I've never seen such a reaction before!"
    o "And you finished so quickly!"
    o "You've really gone too long without, haven't you??"

    scene 30aroomoct

    stop music fadeout 2.0

    a2 "Aahh..."
    a2 "Thank you, Octavia..."

    o "Y-you're welcome."
    o "I'm certainly going to have to talk to [player_name] about your... situation."
    o "Are you alright with that?"

    scene 31aroomoct

    o "Avalon?"
    o "I want you to wake up now, Avalon."

    scene 32aroomoct with dissolve

    o "Are you alright?"
    o "Your heart rate is steady..."
    o "Did you fall asleep!?"
    $ renpy.end_replay()
    jump livingoctavia

    label monogamy2:

    o "Are you excited to try out your new toy?"

    scene 14aroomoct with dissolve

    a2 "Yeah!"
    a2 "I'm a little nervous though too."

    o "There's no reason to be nervous."
    o "It's important to please yourself."
    o "Do you want to wake up now, Avalon?"

    a2 "Actually, I think I want to sleep for a while..."

    scene 7aroomoct

    o "Okay, I'm going to let you rest then."
    o "Sweet dreams, Avalon."

    stop music fadeout 2.0

    ## Octavia with Byron in the Living Room

    label livingoctavia:

    scene 1livingoctavia with fade

    bi "{i}That was a great workout!{/i}"
    bi "{i}I hope the girls are doing alright.{/i}"

    scene 3livingoctavia

    play music "audio/tomorrows_rain.mp3"

    o "Welcome home, [player_name]. I hope I didn't startle you."
    o "It looks as though you've had a sufficient workout. How was it?"

    scene 2livingoctavia

    b "It was great! I've been slacking off a bit so I had to hit it hard today."
    b "Fortunately, it wasn't too crowded. I didn't have to wait on a machine
    at all!"
    scene 3livingoctavia

    o "You're quite passionate about your exercises, aren't you?"
    o "Come sit with me, [player_name]. I'm eager to hear more about you."

    scene 4livingoctavia with dissolve

    b "Where is Avalon? Did you guys have a good time?"
    b "I feel bad for leaving right after you arrived. Exercising helps me clear my head
    and I needed it more than ever today."

    scene 5livingoctavia

    o "I understand, [player_name]. No need to apologize."
    o "Avalon fell asleep while we were conversing. Can you believe it??"
    o "I think she might be part cat. I'm rather fond of cats, though, so I don't
    actually mind if she is."

    scene 7livingoctavia with dissolve

    o "I noticed you don't take yourself too seriously. I've read that playful teasing
    can be bonding between two people if done playfully."
    o "Would you mind if I did an impersonation of you at the gym?"

    scene 10livingoctavia

    b "I would pay actual money to see you do an impersonation of me at the gym."
    b "I'm really excited about this now. Don't go easy on me!"

    scene 13livingoctavia

    o "'Check out these guns, ladies!'"
    o "'I had a push-up contest with myself earlier.'"
    o "'And I won!'"

    scene 6livingoctavia

    b "That..."
    b "Was amazing!"
    b "I think my favorite part was that I won the contest."
    b "Okay, this is my impersonation of you."

    scene 12livingoctavia

    b "'I forgot to turn my bedside lamp off one night.'"
    b "'I woke up with a sunburn!'"

    scene 5livingoctavia

    o "Because I'm so pale, right? That's very humorous, [player_name]!"
    o "Alright, I have one more of you."

    scene 13livingoctavia with dissolve

    o "'Oh man, I totally forgot to work out today.'"
    o "'I got too distracted by a mirror.'"

    scene 6livingoctavia

    b "That actually happened to me once!"
    b "Okay, last one of you."

    scene 14livingoctavia with dissolve

    b "'Strange men tend to catch me when I fall so it actually {b}didn't{/b}
    hurt when I fell from Heaven!'"

    scene 9livingoctavia

    o "Wha--! Is that how you see me, [player_name]?"
    o "I'm not an Angel, I have flaws just like everyone else."
    o "And I don't always do the right thing when I should..."

    scene 8livingoctavia

    b "I'm so sorry! I didn't mean anything by that."
    b "You just-- I mean, you're always so compassionate and caring."
    b "And... even Angels can make mistakes, right?"

    scene 7livingoctavia

    o "Yeah, I guess maybe they can. I didn't mean to seem offended, I'm afraid
    compliments haven't been aimed in my direction in a while."
    o "I should have received that better. Genuinely, thank you. You've
    made me blush, [player_name]."

    scene 10livingoctavia

    b "Honestly, I never really know what to make of you."
    b "When I think of 'Octavia', I picture a golden, glowing question mark."
    b "The only thing I really know about you is..."

    scene 4livingoctavia with dissolve

    b "How you make Avalon and me feel. It's not hard to explain either."
    b "You're like the moment after the storm has passed."
    b "The cool breeze blowing in, the sun peeking out over the horizon."
    b "Everything feels calm and settled when you're around."

    scene 9livingoctavia

    o "[player_name], that's... really sweet and poetic."

    scene 7livingoctavia with dissolve

    o "That just made my day."
    o "Thank you."

    scene 4livingoctavia

    b "You're welcome!"
    b "What did you say to Avalon to make her pass out?"
    b "I don't think I've ever seen her fall asleep during a conversation before."

    scene 5livingoctavia

    o "I actually wanted to talk to you about that!"
    o "To help her recover, I hypnotized her to help relieve some of her stress."

    scene 6livingoctavia

    b "O-oh, you uh... You know how to do that?"
    b "You're full of surprises."

    scene 7livingoctavia

    o "Don't worry, I only use my powers for good!"
    o "I tried it on her at the spa and she responded really well to it."
    o "She asked me to do it again today. A lot of people find it helpful and
    it looks like she's one of them."

    scene 4livingoctavia

    b "That's spectacular. I really appreciate you helping her out, Octavia."
    b "It truly means the world to me that you've decided to help me in this endeavor."
    b "Avalon is special to me. In ways I can't even describe."

    scene 11livingoctavia

    o "She also told me you bought her a toy."

    b "Gah!"

    o "A {b}sex{/b} toy."

    b "I--!"

    scene 8livingoctavia

    b "I-it was just to help her! She's going to be afraid of intercourse with
    a partner for a while, right?"
    b "I thought maybe she could still enjoy sex if it was, you know, a solo endeavor."
    b "I messed up here, didn't I? I'm an idiot."

    scene 7livingoctavia

    o "It's alright, [player_name]. I understand your reasoning behind it."
    o "It probably wasn't the best idea. Sex, in any capacity, needs to be her choice
    to endulge in or reject."
    o "I see you had good intentions but let her decide the pace at which she opens
    up to things like that."

    if monogamy == True:
        jump monogamy4
    else:
        jump polygamy4

    label monogamy4:

    o "A toy as a gift implies that you yourself have sex on the mind."
    o "She may interpret the gesture as a request for her to be more sexual with you."
    o "Do you understand?"

    scene 8livingoctavia

    b "I understand. I'll be more careful in the future. Jeez, I wish I would have
    asked you first now..."
    b "I'm really not sure what to do in this situation. I tried to take it back
    but she wanted to keep it."

    scene 5livingoctavia

    o "Is that so? Perhaps she is ready to explore the possibility of opening up
    to sex now. It seems early in her recovery but everyone is different."

    scene 7livingoctavia with dissolve

    o "You must remember to take into account your own feelings as well."
    o "Are you sure you're even comfortable with her using a toy?"
    o "Some men feel like a toy replaces them."

    scene 6livingoctavia

    b "I'm not really intimidated by a piece of plastic."
    b "Do you think I might be subconsciously?"

    scene 7livingoctavia

    o "Well, there's one way to find out."
    o "I could hypnotize you!"

    scene 10livingoctavia

    b "Oh, I've had training in the ways of the force."
    b "I'm mentally fortified against your dark arts."

    scene 11livingoctavia

    o "Look into my eyes, [player_name]."
    o "Feel my influence in your mind."
    o "These are not the droids you're looking for."

    scene 10livingoctavia

    b "It's official, I adore you."
    b "You can do whatever you want to me."

    scene 5livingoctavia

    stop music fadeout 2.0

    o "Great!"
    o "Lie down here on the couch and we'll get started."

    jump byronhypnosis

    label polygamy4:

    o "She has been feeling sexually frustrated though. It seems she hasn't been
    taking care of herself for quite some time now."

    b "Taking care of herself? How do you mean?"

    o "Sexually. She asked if I would assist her so I did."

    scene 10livingoctavia

    b "Sorry, I'm not quite understanding."
    b "You assisted her? With what?"
    b "Can you explain it bluntly for me?"

    scene 5livingoctavia

    o "I stimulated her vagina until she orgasmed!"

    scene 8livingoctavia

    b "... Awesome."
    b "I mean..!"
    b "Sorry, I'm still not getting it."
    b "Can you explain it to me with more detail."
    b "Please, leave nothing out."

    scene 11livingoctavia

    o "The details are confidential."
    o "I won't kiss and tell."

    b "There was kissing!?"

    o "You'll get nothing out of me."
    o "My lips are sealed!"

    scene 7livingoctavia with dissolve

    o "She assured me you wouldn't mind but I still wanted to be forthcoming with you."
    o "I don't want anything like that to harm our relationship."

    scene 4livingoctavia

    b "I'm a bit surprised but I don't mind at all."
    b "I want her to enjoy the pleasures of sex but I wasn't sure she would be able to
        with me after what happened to her."
    b "I thought maybe exploring other avenues for release might be a good way to
        ease into it."
    b "Am I way off on this?"

    scene 7livingoctavia

    o "Nope!"
    o "She's likely more comfortable with female companions right now."
    o "And sharing your partner can be a lot of fun!"
    o "But we'll have to monitor your's and Avalon's emotional state."
    o "Sharing can ultimately lead to feelings of jealousy
        and then resentment."
    o "You might not even be consciously aware of these feelings."

    scene 4livingoctavia

    b "I thought about that."
    b "I don't feel that way right now but if it's subconcious..."
    b "Well, how would I find out?"

    scene 5livingoctavia

    o "I could hypnotize you!"
    o "We can find out all sorts of things you might not even know are dwelling within
        your mind."
    o "How about it?"

    scene 10livingoctavia

    b "Oh I'm immune to hypnotism."
    b "You see, my muscles are so large and packed with oxygen and energy that
        I can't be put to sleep."
    b "In fact, I never sleep."
    b "That's how strong I am."

    scene 13livingoctavia

    o "'Rawr, I'm [player_name]!'"
    o "'I'm so strong, I don't go to sleep. Sleep comes to me!'"
    o "'And then we high five and work out together!'"

    scene 6livingoctavia

    b "Wow, you're a much better [player_name] than me!"

    scene 4livingoctavia with dissolve

    stop music fadeout 2.0

    b "Alright, let's try this hypnosis."
    b "Do you like, swing a pocket watch in front of my eyes like a pendulum or what?"

    scene 7livingoctavia

    o "Lie down here on the couch and we'll get started."

    label byronhypnosis:

    scene 16livingoctavia with fade

    play music "audio/let_her_go.mp3"

    o "Are you comfortable?"

    b "Yes."

    o "For this to work, I have to make physical contact with you."
    o "Is that alright?"

    scene 18livingoctavia

    b "Octavia, if you want to feel my muscles, you can."
    b "You don't have to make up stuff in order to grope me."
    b "I really don't mind."

    scene 16livingoctavia

    o "You tell jokes when you're nervous."
    o "It's an obvious tell."
    o "You'd be terrible at Poker."
    o "I'm going to put my hand on you now."

    scene 17livingoctavia with dissolve

    o "Is this alright?"

    b "Y-yeah."

    o "Let me know if you become uncomfortable."

    scene 19livingoctavia

    b "Your hand, it's... warm."
    b "But it doesn't feel like body heat."
    b "It feels like... Sunlight?"
    b "It's like it's spreading to my whole body, too."
    b "How--"

    o "Take a deep breath, [player_name]. Focus on my voice."

    scene 21livingoctavia with dissolve

    b "O-Okay, sure."
    b "Your... voice..."

    o "Imagine you're looking up at the stars."
    o "Each individual star in the sky is its own world."
    o "And they're all so very far away from each other."
    o "But all part of the same great, big universe."
    o "Take a deep breath."
    o "And let it out."

    scene 22livingoctavia with dissolve

    o "Imagine yourself as one of those stars."
    o "You're a world of your own shining brighter than any other."
    o "But you can see all the other worlds glowing too."
    o "You're not alone, [player_name]."
    o "Take another deep breath."
    o "Let it out."

    scene 23livingoctavia with dissolve

    o "All those other worlds admire you for your glow."
    o "They all wish they could be closer to you."
    o "They want to orbit around you forever."
    o "And all you have to do is to let them."
    o "Take a deep breath."
    o "Let it out."

    o "How do you feel, [player_name]?"

    scene 24livingoctavia with dissolve

    b "I feel..."
    b "calm."

    o "Is there anything you want to talk about?"

    b "I want to talk about Avalon."

    o "How are things going between you two?"

    b "She's so incredible."
    b "We're having so much fun discovering each other right now."
    b "I just wish..."
    b "I wish I hadn't failed her..."

    o "How did you fail?"

    scene 26livingoctavia with dissolve

    b "I let something terrible happen to her."
    b "I wasn't there to stop it."
    b "And now, she's hurt."
    b "It's all my fault."

    o "And you think going after the man that did it will absolve you?"

    b "W-Will it?"

    o "[player_name], what happened wasn't your fault."
    o "Spend time with Avalon, that's what she really needs."

    scene 24livingoctavia with dissolve

    b "Okay."

    scene 27livingoctavia

    stop music fadeout 2.0

    a2 "Octavia?"

    scene 28livingoctavia with dissolve

    o "Shh."

    ai2 "{i}What's going on?{/i}"
    ai2 "{i}Is she hypnotizing Uncle [player_name]..?{/i}"

    scene 30livingoctavia with dissolve
    pause (.3)
    scene 29livingoctavia
    pause (.3)
    scene 30livingoctavia
    pause (.3)
    scene 29livingoctavia
    pause

    scene 31livingoctavia with dissolve

    play music "audio/touching_moment.mp3"

    a2 "What's... going on?"

    o "Watch this."

    scene 32livingoctavia with dissolve

    o "[player_name], I'm going to ask you some questions."
    o "I want you to answer as honestly as you can."

    b "Alright."

    scene 33livingoctavia

    ai2 "{i}Oh!{/i}"
    ai2 "{i}Her hand..?{/i}"
    ai2 "{i}She's being more affectionate all of the sudden.{/i}"
    ai2 "{i}Is she going to be like this more often?{/i}"

    scene 34livingoctavia with dissolve

    ai2 "{i}I hope so.{/i}"
    ai2 "{i}I always feel calm when she's around.{/i}"
    ai2 "{i}She said she uses touch to connect with people.{/i}"
    ai2 "{i}I want to be connected to you too, Octavia.{/i}"

    scene 23livingoctavia

    o "Why did you grow out your beard, [player_name]?"

    scene 24livingoctavia with dissolve

    b "Well, I'm rich now and I knew I had to start acting rich."
    b "So I got a fur coat for my face."
    b "Nothing says 'I can afford it!' like a fur coat."

    scene 35livingoctavia

    o "Mhmhmm."

    ai2 "{i}She's... holding back laughter.{/i}"
    ai2 "{i}She's really enjoying this.{/i}"

    scene 23livingoctavia

    o "What do you think of the Platypus, [player_name]?"

    scene 25livingoctavia

    b "Ridiculous animal."
    b "A bill like a duck, a tail like a beaver and venom like a snake."
    b "You can't be everything!"
    b "Pick a species, you greedy prick!"

    scene 35livingoctavia

    o "Mhmhmhmmm."

    ai2 "{i}She's trying so hard to laugh quietly.{/i}"
    ai2 "{i}I've never seen her this giddy before.{/i}"
    ai2 "{i}She's having so much fun.{/i}"

    scene 23livingoctavia

    o "Alright, [player_name]."
    o "I want you to wake up now."
    o "Open your eyes."

    scene 22livingoctavia with dissolve

    pause (.3)

    scene 21livingoctavia with dissolve

    b "Mm, wow."
    b "I feel great!"

    scene 37livingoctavia

    o "I'm so happy to hear that."

    a2 "What's your deal with Platypuses?"

    scene 38livingoctavia

    b "Platypuses?"
    b "I got bit by one when I was young."
    b "The bite hurt for weeks."
    b "It was terrible!"
    b "Why do you ask?"

    scene 37livingoctavia

    a2 "No reason."

    ai2 "{i}We spent a while longer chatting.{/i}"

    if monogamy == True:

        ai2 "{i}We told [player_name] what he told us about his beard and the platypus.{/i}"
        ai2 "{i}I think he laughed harder than Octavia did!{/i}"

    else:
        ai2 "{i}Octavia told me she helped me climax while I was hypnotized.{/i}"
        ai2 "{i}I was pretty embarrassed but the way she talks about it...{/i}"
        ai2 "{i}It felt like it was really no big deal.{/i}"
        ai2 "{i}We told [player_name] what he told us about his beard and the platypus.{/i}"
        ai2 "{i}I think he laughed harder than Octavia did!{/i}"

    jump night_three

    ## Dallas and Avalon in her room

    label aroom_dal:

    scene 1aroomdal with fade

    d "Like, I get that they're supposed to be giant underground worms."
    d "And they can like, sense you through vibrations in the ground."
    d "But why do they just look like oversized, flaccid dicks?"

    scene 2aroomdal with dissolve

    d "You know what I--"
    d "Goddammit."

    scene 3aroomdal

    d "Every time."
    d "You fall asleep every time we watch a movie and I never learn."
    d "I knew I shouldn't have let you change into something comfortable."
    d "It probably just made it easier for you to pass out."

    scene 4aroomdal

    d "Ooooaah."
    d "Damn, girl, you're makin' me tired now."

    scene 5aroomdal with dissolve

    d "Well, I guess I'll go to the living room and wait for [player_name] to get home."

    if monogamy == True:
        jump monogamy3
    else:
        jump polygamy3

label polygamy3:
    if _in_replay:
        $ player_name = renpy.input("What would you like to name the MC?")
        if player_name.strip() == "":
          $ player_name = "Byron"

    d "Hmm?"
    d "What's that?"

    scene 6aroomdal

    d "You got some weird pink, plastic thing under your bed."
    d "Oh I can take a look?"
    d "You really don't mind?"
    d "Let's see here..."

    scene 8aroomdal with dissolve

    d "This is..."
    d "What is this thing?"

    scene 7aroomdal

    d "It looks kind of like a penis."
    d "But then again, a lot of things look like a penis to me."
    d "Hmm..."

    scene 9aroomdal with dissolve

    d "Here's the button right here."
    d "This isn't gonna blow up or something, is it?"
    d "Fuck it, let's just press it."

    "*Brzzzz*"

    play music "audio/disturbed_mind.mp3"

    scene 10aroomdal

    a2 "Guh!"
    a2 "Wha--"

    d "I know what this is!"
    d "It {b}is{/b} a dick!"
    d "Avalon, this is a vibrator!"

    scene 11aroomdal with dissolve

    a2 "Dallas, where did you get that?!"
    a2 "P-put it back!"
    a2 "You don't know what that thing is capable of!"

    d "Oh but I want to know!"
    d "You gotta let me try this thing!"
    d "I've never used a toy before!"

    scene 12aroomdal with dissolve

    a2 "No, Dallas, don't!"
    a2 "That thing is wild!"

    d "You already tried it?"

    a2 "Maybe..."

    scene 13aroomdal

    d "You... slut!"
    d "Where did you get it?"

    a2 "[player_name] bought it for me..."
    a2 "We're kind of dating now."

    d "Is he gonna be mad when I put it in your cooter?"

    a2 "What!?"
    a2 "Get that thing away from me!"

    scene 14aroomdal

    a2 "B-but no, he said I can play around with girls."

    d "Uhh, then why are you resisting me??"
    d "Let me just try it!"

    a2 "Okay but take it easy!"
    a2 "You have to go slow with that thing."

    scene 15aroomdal

    d "Aw man, this is going to be epic."
    d "I can't believe you didn't tell me you and [player_name] are a thing now."
    d "And I doubly can't believe he's totally fine with us bangin'."

    a2 "We're not bangin'!"
    a2 "Go slow with--"

    scene 16aroomdal

    a2 "Mmf!"

    d "You gotta lube it up first."
    d "Get your spittle all up on it."
    d "Work your tongue around it or somethin'."

    scene 17aroomdal with dissolve

    a2 "Mmm fmf Mmmf!"

    d "What?"
    d "Don't talk, just suck."

    a2 "Mffmm Fmm!"

    scene 18aroomdal with dissolve

    d "What're you sayin'?"

    a2 "Idiot!"
    a2 "It's a vibrator, it vibrates!"
    a2 "You're gonna chip my teeth off."
    a2 "Have you ever heard of 'foreplay'??"
    a2 "You don't need to.. 'lube it up' if you get my lady juices flowing first."

    d "Oooh, right."

    scene 19aroomdal with dissolve

    d "Anticipation or whatever, right?"
    d "I have to get you all excited about it."
    d "Like this?"

    a2 "Y-yeah, just move it around I think."
    a2 "Slow and steady, you know?"

    scene 20aroomdal with dissolve

    d "And then down a little..?"

    a2 "Ooh, yes!"
    a2 "Like that!"

    d "Damn, you're kind of easy when it comes to this stuff."
    d "And... boring."

    scene 20aroomdal2

    a2 "I-I know, I just..."
    a2 "I haven't touched myself in months."

    d "What?!"
    d "Is that even possible!?"

    a2 "I stopped after..."
    a2 "You know."

    d "I stopped for a while after I was attacked too."
    d "Well, I mean, like two days but..."
    d "It was a long time for me."
    d "Lower now?"

    scene 21aroomdal

    a2 "Oh!"
    a2 "M-my nipples are sensitive!"
    a2 "It feels really good!"

    d "Fuck, I wish I was this easy to excite."
    d "This is like playing Whack-A-Mole with Mjolnir."
    d "It's too easy!"

    scene 22aroomdal with dissolve

    d "Woah!"
    d "You're getting frisky!"

    a2 "I'm sorry, I can't help myself."

    d "Pff, I don't mind."
    d "Grab as much tit as you want, girl."
    d "Just remember, they're attached."

    scene 23aroomdal with dissolve

    d "Let's keep moving dow--"

    a2 "Oh!"
    a2 "It's so close!"

    d "Jeez, you're so dramatic."
    d "I can't believe you react like this."

    a2 "It's like my body is on fire!"

    scene 23aroomdal2 with dissolve

    d "What about now?"

    a2 "Oh no!"
    a2 "It's too much!"
    a2 "I can't--"

    scene 25aroomdal with dissolve

    a2 "Oh fuck!"
    a2 "I'm cumming!"

    d "I barely even touched your clam!"

    a2 "It won't stop!"
    a2 "OOH GOD!"

    d "I think we need a priest!"
    d "Fuck, this is hot!"

    scene 26aroomdal with dissolve

    if persistent.experimentation == False:
        $ renpy.notify("You've unlocked 'Experimentation' in the Scene Gallery on the Main Menu!")
        $ persistent.experimentation = True

    a2 "Aaahhh..."
    a2 "Thank you, Dallas..."

    d "Anytime, girlfriend."
    d "Maybe try to last more than five seconds next time..."

    scene 27aroomdal

    d "This thing is amazing!"
    d "I've gotta get me one of these!"
    d "No no, I can't."
    d "I'd never leave the house!"
    d "Fuck it, I'm fine with that."

    d "Alright Avalon, now do me."

    stop music fadeout 2.0

    scene 28aroomdal

    d "Ava--?"
    d "Goddammit."
    d "Again?!"

    $ renpy.end_replay()
    label monogamy3:

    scene 1livingoctavia with fade

    bi "{i}That was a great workout!{/i}"
    bi "{i}I may have even overdone it today.{/i}"
    bi "{i}Hmm?{/i}"
    bi "{i}Is that... Dallas?{/i}"

    scene 1livingdallas

    bi "{i}It is Dallas.{/i}"
    bi "{i}And she's asleep!?{/i}"

    scene 2livingdallas with dissolve

    bi "{i}Oh you poor fool, Dallas.{/i}"
    bi "{i}You fell asleep at the wrong house.{/i}"
    bi "{i}This is the greatest gift the universe could have given me.{/i}"
    bi "{i}I can't waste it!{/i}"

    scene 3livingdallas

    play music "audio/aint_it_funny.mp3"

    bi "{i}I have to move fast but quietly!{/i}"
    bi "{i}There's no time to lose!{/i}"
    bi "{i}She could wake up at any moment!{/i}"

    scene 4livingdallas with dissolve

    bi "{i}Where is it, where is it??{/i}"
    bi "{i}Not in here...{/i}"
    bi "{i}Damn!{/i}"
    bi "{i}How could I forget where I put it!?{/i}"
    bi "{i}Aha!{/i}"
    bi "{i}Found you!{/i}"

    scene 5livingdallas with dissolve

    bi "{i}Still sleeping??{/i}"
    bi "{i}Yes!{/i}"

    scene 4livingdallas with dissolve

    bi "{i}Damn.{/i}"
    bi "{i}I've got to brush some of the dust off this thing...{/i}"
    bi "{i}Alright, good enough!{/i}"

    scene 6livingdallas with dissolve

    bi "{i}Let's see if we can get this thing to stand up.{/i}"
    bi "{i}Work with me, buddy!{/i}"

    scene 7livingdallas with dissolve

    bi "{i}And now we make sure it's oriented properly.{/i}"
    bi "{i}Little to the left...{/i}"
    bi "{i}Perfect!{/i}"

    scene 8livingdallas with dissolve

    bi "{i}Alright, now we have to make some noise.{/i}"
    bi "{i}What do zombies say?{/i}"
    bi "{i}'I vant to suck your blood!'{/i}"
    bi "{i}No no, that's vampires.{/i}"
    b "Brraaiiinnss..."

    scene 9livingdallas with dissolve

    d "Huh?"

    scene 10livingdallas

    d "What's going on?"
    d "What is--"

    scene 11livingdallas with dissolve

    d "{b}Ahhh!{/b}"
    d "[player_name], help me!"
    d "Please help!"
    d "It's going to get me!"

    scene 9livingdallas
    pause (1)
    scene 12livingdallas with dissolve

    b "Bahaha!"
    b "I got you so good, Dallas!"
    b "It's just cardboard!"

    scene 13livingdallas

    d "I-it's a joke?"
    d "You were messing with me??"

    scene 12livingdallas

    b "Yeah!"
    b "Ahaha!"
    b "You really thought it was gonna eat you."
    b "I can't stop laughing!"

    scene 15livingdallas

    d "Oh my god, I was so scared."
    d "You got me really good, [player_name]."
    d "Shit."

    scene 14livingdallas

    b "You should have heard yourself!"
    b "'Help me, [player_name]. Please!'"
    b "Bahaha!"

    d "Come here."

    b "Alright."

    stop music fadeout 2.0

    scene 16livingdallas with dissolve

    b "Damn, Dallas."
    b "I am never going to let you live this down."
    b "This is the greatest day ever."

    scene 17livingdallas

    d "You did good, [player_name]."
    d "I don't think I've ever been that scared in my life."
    d "I guess I'm going to have to up my game now."

    scene 18livingdallas with dissolve

    d "Give me your hand."

    b "No way!"
    b "You're gonna hurt me!"

    d "[player_name], give me your hand."

    b "Alright."

    scene 19livingdallas with dissolve

    b "Be gentle with it."
    b "I use this hand to give life."
    b "And occasionally, when called for, to take it!"

    d "You're full of shit."

    scene 20livingdallas with dissolve

    d "Here."
    d "Can you feel my heartbeat?"

    b "Wow, I do!"
    b "I didn't know you had a heart, Dallas."
    b "I thought you were just three imps wearing a person suit."

    d "It's beating fast, right?"

    scene 21livingdallas

    b "Damn, it really is!"
    b "I guess I really get your blood pumping, huh?"
    b "I've been known to have that effect on beautiful women."

    d "You think I'm beautiful?"

    scene 22livingdallas with dissolve

    a2 "Ehem."
    a2 "What's going on out here?"
    a2 "Why was Dallas screaming like a madwoman?"

    scene 23livingdallas with dissolve

    b "Hey, Avalon."
    b "You see that Halloween decoration behind you?"
    b "I woke her up with it!"
    b "Her heart's racing like she just ran a marathon."

    scene 24livingdallas with dissolve

    b "Will you come sit with me?"
    b "I'm basking in my victory right now."

    scene 25livingdallas with dissolve

    a2 "Are you alright, Dallas?"
    a2 "I know you guys like to play around but I've never heard you scream
        like that."

    d "I'm just plotting my revenge now."

    b "I expect nothing less!"

    scene 26livingdallas

    d "You two look pretty cute together."
    d "I don't suppose you guys would be down for a threesome??"

    a2 "No, Dallas!"

    scene 25livingdallas

    bi "{i}We spent a while chatting between each other.{/i}"

    if monogamy == True:
        bi "{i}I've always known Dallas to be a strong support for Avalon.{/i}"
        bi "{i}I'm glad Avalon has such a close friend, especially someone like Dallas.{/i}"

    else:
        bi "{i}It came up that Dallas and Avalon had a pretty raunchy experience while
        I was gone.{/i}"
        bi "{i}Apparently Avalon had some pent up sexual energy she was finally able to release.{/i}"
        bi "{i}I've always known Dallas to be a strong support for Avalon.{/i}"
        bi "{i}I'm glad Avalon has such a close friend, especially someone like Dallas.{/i}"

    ## Night Scene with Byron and Avalon, then Penny

label night_three:
    if _in_replay:
        $ player_name = renpy.input("What would you like to name the MC?")
        if player_name.strip() == "":
          $ player_name = "Byron"

    scene 1nightthree with fade

    bi "{i}Whew, I may have gone a little too hot with that shower.{/i}"
    bi "{i}I haven't had a full night sleep in two days.{/i}"
    bi "{i}I almost passed out on my feet in there!{/i}"

    scene 2nightthree with dissolve

    bi "{i}I think I'll go straight to bed.{/i}"
    bi "{i}I bet Avalon is already asleep.{/i}"
    bi "{i}Never in my life have I met someone who can sleep as much as that girl{/i}."

    a2 "Uncle!"
    a2 "Come quick!"

    scene 3nightthree with dissolve

    b "Hmm?"

    bi "{i}I guess she's not asleep.{/i}"

    a2 "Something terrible has happened!"

    bi "{i}She doesn't sound sincere at all.{/i}"
    bi "{i}She sounds playful.{/i}"

    scene 4nightthree with dissolve

    b "Uh-huh."
    b "What happened?"
    b "Did you run out of--"

    scene 5nightthree with dissolve

    b "Ah!"
    b "What are you..?"
    b "What is that!?"

    play music "audio/cause.mp3"

    show 6nightthree2:
        yalign 1.0
        linear 5.0 yalign 0.0

    pause

    scene 6nightthree with dissolve

    a2 "I was naughty, Uncle."
    a2 "A fairy came and turned me into a bunny girl as punishment."
    a2 "Whatever will I do?"

    scene 7nightthree

    b "It's... not even my birthday."
    b "This is so amazing, it's like looking into the eyes of God..."
    b "Except there's way better cleavage here."
    b "It's so beautiful, I might weep."
    b "Not because of the beauty, but because my erection is so intense that it
        actually hurts."

    a2 "Okay, enough."
    a2 "I anticipated the jokes but I didn't expect them to be so ridiculous."

    b "But I have one more!"

    a2 "No!"

    scene 8nightthree with dissolve

    a2 "Just kiss me, you idiot."

    b "I can do that."

    scene 9nightthree with dissolve

    bi "{i}Her lips are so soft and moist, it's entrancing kissing her.{/i}"
    bi "{i}Feeling her body press into mine lit me on fire.{/i}"
    bi "{i}This was so incredibly sexy, I could barely even believe it was really happening.{/i}"
    bi "{i}So much for taking it slow...{/i}"

    ai2 "{i}I could feel his hard, broad body pressing into mine.{/i}"
    ai2 "{i}Standing here now, kissing him, pressing my lips against his...{/i}"
    ai2 "{i}I was dripping with anticipation of what would happen next.{/i}"

    scene 10nightthree

    bi "{i}I could feel myself losing control.{/i}"
    bi "{i}I want to touch her, I need to feel her!{/i}"
    bi "{i}I can't help myself!{/i}"

    scene 11nightthree with dissolve

    a2 "Mm!"

    scene 12nightthree

    ai2 "{i}Oh!{/i}"
    ai2 "{i}He just grabbed my butt and moved my panties down!{/i}"
    ai2 "{i}He's pulling me into him!{/i}"

    scene 13nightthree with dissolve

    ai2 "{i}Oh fuck, it's hot when he's a little rough.{/i}"
    ai2 "{i}I wonder what he wants to do to me? {/i}"
    ai2 "{i}I wonder if I can find out..?{/i}"

    scene 8nightthree with dissolve

    a2 "Do you think we should move this to the bed?"

    stop music fadeout 2.0

    b "Uhh, sure."
    b "If that's what you want."

    a2 "Alright."
    a2 "But I get to be on top."

    scene 14nightthree with fade

    play music "audio/touching_moment.mp3"

    bi "{i}I gazed deep into her eyes, and she peered back into mine.{/i}"
    bi "{i}For several moments, we didn't speak or move.{/i}"
    bi "{i}We were completely absorbed in each other.{/i}"
    bi "{i}Her eyes had captured my soul and I was completely under her spell.{/i}"
    bi "{i}I love her.{/i}"

    scene 15nightthree with dissolve

    ai2 "{i}He looked up at me with desire in his eyes that I'd never seen before.{/i}"
    ai2 "{i}I could see his every want, his every need.{/i}"
    ai2 "{i}And I wanted to give it all to him.{/i}"
    ai2 "{i}Whatever he wants of me, he can have.{/i}"
    ai2 "{i}I love him.{/i}"

    scene 16nightthree

    b "This is the best moment of my life."

    scene 17nightthree

    a2 "The outfit is pretty great, right?"
    a2 "I almost went with the cat version but I figured you were
        more of a bunny guy."

    scene 16nightthree

    b "No, I mean, every time I'm with you,"
    b "every time your eyes are locked onto mine."
    b "It's like every sequential moment is the best moment of my life when
        you're with me."

    scene 23nightthree

    a2 "I--!"
    a2 "That's really how I make you feel?"

    scene 16nightthree

    b "Yeah."
    b "That's really how you make me feel."

    scene 17nightthree

    a2 "Thank you."
    a2 "But let's save the romantic talk for after playtime."
    a2 "Remember when you said you wanted to ravish me?"
    a2 "Well, here's your ch--"

    scene 19nightthree with dissolve

    a2 "Ah!"
    a2 "What the..?"

    scene 20nightthree with dissolve

    a2 "Uncle, your erection..."
    a2 "It's pressing into my..."
    a2 "Into my..."

    b "Vagina?"

    a2 "It's so big."

    scene 18nightthree

    b "Yeah, they used to think the Megalodon was extinct."
    b "But I happen to know that there is exactly one left in the world."
    b "And it's in my pants!"

    scene 21nightthree

    a2 "Stop it, Uncle!"
    a2 "No jokes while we're being intimate!"
    a2 "Especially ones about your penis!"

    scene 22nightthree

    b "Aw, come on!"
    b "Jokes are basically my superpower!"
    b "You can't take that away from me!"

    scene 21nightthree

    a2 "I said 'No'!"
    a2 "You will respect the sanctity of the bedro--"

    scene 19nightthree with dissolve

    a2 "Oh!"
    a2 "It's harder."
    a2 "I can't..."

    show abdry

    pause

    a2 "I can't help myself."
    a2 "Oh, fuck."

    b "Avalon, you're..."
    b "You're grinding on my--"
    b "Mmmffuck."

    a2 "It feels so good."
    a2 "I can't stop myself!"

    scene 24nightthree

    a2 "Ah!"

    scene 25nightthree with dissolve

    a2 "Uncle, you're grabbing my breast."

    b "These are amazing!"

    scene 24nightthree with dissolve

    a2 "Do you... do you like them?"

    b "Very much!"
    b "They feel even better than they look."
    b "I didn't know that was even possible."

    scene 26nightthree with dissolve

    a2 "You can... take my top off."
    a2 "If you want..."

    b "A-are you sure?"
    b "We can stop here if it's too much."

    a2 "No, I want you to see me."
    a2 "I want you to see..."
    a2 "All of me."

    stop music fadeout 2.0

    b "Alright."
    b "If you're sure."
    b "Let's see if we can--"

    play sound "audio/doorbell.mp3"

    "*Ding Dong*"

    scene 27nightthree with dissolve

    if persistent.bunnygirl == False:
        $ renpy.notify("You've unlocked 'Bunny Girl' in the Scene Gallery on the Main Menu!")
        $ persistent.bunnygirl = True

    a2 "What the..?"

    b "You've got to be kidding me!"
    b "Now of all times!?"

    $ renpy.end_replay()

    scene 1nightthree_p with fade

    ai2 "{i}Uncle let whoever it is into the house.{/i}"
    ai2 "{i}I can hear them talking.{/i}"
    ai2 "{i}It sounds like he's a bit agitated.{/i}"
    ai2 "{i}It's definitely a woman he is talking to.{/i}"
    ai2 "{i}A young woman, by the sound of it.{/i}"
    ai2 "{i}I guess...{/i}"
    ai2 "{i}I guess it's safe to go see.{/i}"

    scene 2nightthree_p with dissolve

    play music "audio/rumors_about_us.mp3"

    b "Whatever it is, I'm sure it could have waited until tomorrow."

    p "I assure you, it's important."

    b "Can you just--"

    scene 3nightthree_p with dissolve

    p "Whoa!"
    p "You have a stripper over?!"
    p "And here I thought you were a gentleman."

    b "What??"
    b "I don't have a stripper over."

    p "Well what do you call {b}her{/b}??"

    b "Penny, is this one of your games?"
    b "I don't--"

    scene 4nightthree_p with dissolve

    b "Gah!"

    p "Wait a minute."
    p "Is that your niece??"
    p "I think I see what's going on here..."

    scene 5nightthree_p

    a2 "Listen, whoever you are, I'm not a stripper!"
    a2 "Just because I'm pretty doesn't mean I'm some floozy!"
    a2 "How rude!"

    p "Feisty! I like her."

    b "A-Avalon."

    scene 6nightthree_p with dissolve

    a2 "What?!"
    a2 "She's being--"

    b "Avalon, your ears."

    a2 "What?"
    a2 "What about my ears??"

    b "Your {b}other{/b} ears."

    scene 7nightthree_p with dissolve

    pause (.2)

    scene 8nightthree_p

    a2 "Oh! Shit!"
    a2 "Umm..!"

    menu:
        "{b}Additional Dialogue Choice{/b}"
        "Easter!":
            a2 "We were just... preparing for Easter!"

            p "In June?"

        "Mascot!":
            a2 "I'm practicing for tryouts to be the new school Mascot!"

            p "You graduated and your school mascot is a bear."

        "Adopting!":
            a2 "We... we were thinking about adopting a pet rabbit so we wanted to live a day
            in the life of a rabbit to better understand--"

            p "Nope."

    menu:
        "{b}Additional Dialogue Choice{/b}"
        "Free gift!":
            a2 "The ears were a free gift at the grocery store for buying carrots!"

            p "That doesn't explain why you're wearing them around the house
                in your underwear."

        "Children!":
            a2 "I read stories to children on the weekend and these are part of my
                costume!"

            p "You wear sexy bunny ears for children?"
            p "I really hope not."

        "Baby Bunnies!":
            a2 "I'm raising baby bunnies and I wear the ears so they'll think of me
                as--"

            p "Don't go there."
            p "Just... don't."

    menu:
        "{b}Additional Dialogue Choice{/b}"
        "Part of the Job!":
            a2 "I'm a magician's assistant and this is part of my stage attire!"

            p "So you're saying the magician pulls {b}you{/b} out of his hat?"

        "Jump!":
            a2 "They're... magic ears!"
            a2 "Yeah, that's right!"
            a2 "They help me jump higher!"

            p "You're really reaching now."

        "Headphones!":
            a2 "They're headphones!"
            a2 "You can't see them but they have earbuds."
            a2 "And, uhh, these were on sale for a really good deal and they got
                exceptional reviews!"

            p "Oh yeah?"
            p "What song were you listening to?"

            a2 "What... Does the Fox Say?"

            p "If you hadn't used a song related to an animal, I may have bought
                that one."
            p "So close!"

    p "Those were some snappy excuses though!"
    p "Color me impressed!"

    scene 9nightthree_p with dissolve

    b "Perhaps we should continue our conversation in the kitchen?"

    p "That's fine."

    scene 10nightthree_p with fade

    b "Uhh, Penny?"

    p "What?"

    b "Is there something wrong with the chair?"

    p "How should I know?"
    p "I'm not a carpenter."

    b "No, I mean--"

    scene 11nightthree_p with dissolve

    a2 "She knows what you mean, Uncle."
    a2 "Sometimes at restaurants, they put the table too high and the seats too low."
    a2 "It makes me feel like a little kid when I sit in those booths."
    a2 "I hate that feeling."

    scene 12nightthree_p2 with dissolve

    p "I hate it too!"
    p "You're a pretty witty gal, huh?"

    scene 10nightthree_p with dissolve

    p "I might be falling in love with this girl, [player_name]."
    p "Is she always so incredible?"

    scene 12nightthree_p

    a2 "That's why you were standing on your tippy-toes, right?"
    a2 "You must do that a lot."
    a2 "I can imagine it's frustrating always having to look up at people."

    scene 12nightthree_p2

    p "It's not all bad!"
    p "Being this short makes it really easy for me to hide, even in plain sight!"
    p "And I can pass for a child with the right hair and clothing."
    p "My size is actually a big reason why I'm a detective."

    scene 12nightthree_p

    a2 "You find the advantages in everything, I bet."
    a2 "That's really cool."
    a2 "I wish I could be more like that."

    scene 14nightthree_p

    b "Penny, why are you here?"
    b "Did you find something?"

    scene 10nightthree_p

    p "Yes!"
    p "I found nothing!"

    b "Wait, what?"

    p "I found something."
    p "Nothing!"

    scene 12nightthree_p

    a2 "It sounds like there's more to the 'nothing' that you found."
    a2 "Can you break it down for us?"

    scene 12nightthree_p2

    p "I went to Tyler's house to have a look around while he was at work."
    p "But I found a whole bunch of nothing!"
    p "No newspapers, no mail, no computer."
    p "Nothing!"
    p "There was even an entire room with nothing at all inside of it."

    scene 14nightthree_p

    b "I don't understand."
    b "You came here to tell us that you didn't find anything?"
    b "And this couldn't wait until tomorrow??"
    b "We were in the middle of something, Penny."

    scene 15nightthree_p

    p "[player_name], you have a relatively clean house."
    p "But how many rooms in your home have literally nothing in them?"
    p "I couldn't even find dust in the high places at his house."
    p "When was the last time you dusted your ceiling fans?"
    p "And his yard was completely void of anything at all!"

    scene 12nightthree_p

    a2 "Your assumption being his house was a sort of... display?"
    a2 "He doesn't actually live there, he just maintains it for appearance?"
    a2 "I guess if the police ever had reason to search his house, they'd find..."
    a2 "Well, they would find exactly what you found."
    a2 "Nothing."

    scene 12nightthree_p2

    p "Look at you go!"
    p "Damn, beauty and brains."
    p "What're you doing with this dope?"

    scene 12nightthree_p

    a2 "Have you seen his abs?"
    a2 "Those alone make him worth keeping around."

    p "That's true!"

    a2 "And he's rich!"

    b "Come on, I'm sitting right here!"

    scene 11nightthree_p with dissolve

    b "If you're going to talk about me behind my back, at least have the decency to do it when my back
        is actually turned!"

    a2 "Uncle, you know why I'm really with you."

    b "My Megalodong."

    a2 "Exactly!"

    scene 10nightthree_p with dissolve

    p "You guys are really silly!"

    scene 12nightthree_p2 with dissolve

    p "It's kind of adorable."

    scene 12nightthree_p

    a2 "So, Penny, you found nothing."
    a2 "In the whole house?"

    scene 12nightthree_p2

    p "Actually, Tyler showed up while I was searching."
    p "So I didn't get to explore the entire house."

    scene 13nightthree_p

    a2 "He almost caught you?"
    a2 "What happened?"

    p "Well..."

    scene 12nightthree_p2

    p "When I heard him coming down the hall, I launched myself into a hiding spot."
    p "But he knew I was there."
    p "So when he entered the room, he came right at me!"

    b "Here we go."

    play music "audio/aint_it_funny.mp3"

    scene 16nightthree_p with dissolve

    p "So I knew I had no choice but to fight my way out!"
    p "I said 'Look, pal, this can only end one of two ways!'"
    p "'And both are real bad for you!'"
    p "But he didn't take my warning."
    p "He took a swing at me but I was too fast!"
    p "I was like..."

    scene 17nightthree_p

    p "Whack!"
    p "And I caught him right in the jaw!"
    p "But he was tough, this one."
    p "So I hit him again!"

    scene 18nightthree_p

    p "Kerchow!"

    scene 17nightthree_p

    p "Fwhap!"

    scene 18nightthree_p

    p "Bang!"

    a2 "Bang!?"
    a2 "Someone had a gun??"

    scene 19nightthree_p

    p "Er!"
    p "I mean..."
    p "A gun?"
    p "Uhh..."

    scene 20nightthree_p with dissolve

    p "YES!"
    p "We both had {b}two{/b} guns!"
    p "And we were just about to have ourselves an old fashioned Mexican standoff."
    p "But then, some lunatic pulled the pin on a grenade."
    p "And that lunatic..."
    p "Was me!"

    scene 22nightthree_p

    b "Penny, this story has gone way too far."
    b "Do you just keep going until someone stops you?"
    b "Does anyone ever actually buy into this shit?"

    scene 21nightthree_p

    a2 "Bravo!"
    a2 "That performance was spectacular, Penny!"
    a2 "I felt like I was actually there!"
    a2 "Have you taken acting lessons??"
    a2 "Because they are really paying off!"

    p "Thank you, thank you."
    p "It's all totally true, by the way."
    p "Especially the part about the grenade."

    scene 10nightthree_p

    stop music fadeout 2.0

    p "It's official."
    p "I absolutely love this girl, [player_name]."
    p "You must let me take her out one night."

    scene 11nightthree_p with dissolve

    a2 "Oh!"
    a2 "I'd love that!"
    a2 "You wouldn't mind, would you Uncle?"

    b "Uhh, no."
    b "I don't mind."
    b "It's completely up to you."

    scene 12nightthree_p2 with dissolve

    p "Avalon, I'd hate to do this to you."
    p "I have to leave but would you mind if [player_name] and I spoke privately first?"

    scene 11nightthree_p with dissolve

    b "Er, I really don't know what this could be about."
    b "I'm sure Avalon can stay."

    a2 "It's fine, Uncle."
    a2 "I'll meet you in my room after you're done."

    scene 12nightthree_p with dissolve

    stop music fadeout 2.0

    a2 "It was nice to meet you, Penny."
    a2 "And... thank you."
    a2 "For what you're doing."

    scene 12nightthree_p2

    p "You're welcome!"
    p "And I assure you, the pleasure was all mine."

    scene 56nightthree with fade


    ai2 "{i}It's been ten minutes and they're still talking...{/i}"
    ai2 "{i}What could she want to talk with Uncle about in private?{/i}"
    ai2 "{i}It can't be good, right?{/i}"
    ai2 "{i}Will he lie to me about it when he comes back..?{/i}"

    b "Avalon?"

    scene 57nightthree with dissolve

    a2 "Yeah, I'm here."

    b "Can I come in?"

    a2 "Yes."

    scene 58nightthree with dissolve

    b "So, I have to tell you--"

    a2 "Don't..."
    a2 "Don't lie to me."
    a2 "If you can't tell me what you talked about, it's alright."
    a2 "But I don't want you to lie to me."

    b "Avalon, I'm not going to lie to you."
    b "But, no, I can't tell you what we talked about."

    a2 "Is it... bad?"

    b "Avalon, I--"
    b "Erhm..."
    b "Yeah."
    b "It's bad."

    scene 59nightthree with dissolve

    a2 "Whatever it is, don't let it come between us."
    a2 "Just..."
    a2 "Make it right and then we'll keep going the way we have been."
    a2 "Together."

    b "Yeah."
    b "Everything will work out."

    scene 60nightthree with dissolve

    b "Everything is going to be just fine."

    bi "{i}I hope...{/i}"

    jump act_four_s


    ## This is the original scene when Penny meets Byron, after she reveals
    ## that she is not Nicole, but in fact the Detective Byron set a meeting
    ## with online. This scene was updated several times.

    label old_penny:

    scene 33lingeriestore with fade

    bi "{i}So Nicole was the investigator from Penny for Your Thoughts the whole time?{/i}"
    bi "{i}And she was testing me?{/i}"
    bi "{i}Wait, Nicole?{/i}"
    bi "{i}Nickle...{/i}"
    bi "{i}Is her name a play on words?{/i}"
    bi "{i}Coin puns, really?{/i}"
    bi "{i}I can't hire this person, she's nuts!{/i}"
    bi "{i}And she's got to be a teenager!{/i}"
    bi "{i}Fuck, [player_name], what have you gotten yourself into??{/i}"

    scene 34lingeriestore


    p "Mr. [player_name], twenty-eight years old, lives alone and recently came into a rather large
        sum of money."
    p "Which is fortunate since you haven't been able to hold a job for more than a year."
    p "Adopted by Frank and Wendy after your mother passed away when you
        were five."
    p "And I'm guessing the reason you asked for a consult today has something
        to do with your biological father?"

    b "How did you--"
    b "Why would you--"

    scene 4lingeriep with dissolve

    p "Breathe it in, Good Sir!"
    p "I know it's a lot!"
    p "It can be intimidating standing in the presence of such a magnificent intellect!"

    b "I'm not here about my father."

    scene 1lingeriep with dissolve

    p "Awww..."
    p "I was so sure."
    p "Now everything I just said seems so much less impressive."
    p "Dammit."


    b "It... was still impressive."

    scene 4lingeriep with dissolve

    p "YES!"
    p "Bask in the radiant glow of my excellence!"
    p "Greatest."
    p "Detective."
    p "Everrrr."
    p "You can kiss my boot if you'd like, Peasant."

    b "Nicole, can we--"

    p "Penny."

    b "What?"

    scene 34lingeriestore with dissolve

    p "My name is Penny."
    p "Nicole is a pseudonym."

    b "Because it's a play on words, right?"
    b "Do you also go by..."
    b "Diamond?"
    b "You know, because it kind of sounds like Dime..."

    p "Oh no, I get it."
    p "It's a bit of a stretch."
    p "Maybe leave the puns to a professional, Sir Knight."

    scene 38lingeriestore with dissolve

    p "What do you want, by the way?"
    p "If this isn't about your father, what do you need a private eye for?"

    scene 39lingeriestore

    b "Can we talk about the guy you just lit up like a Christmas tree?"

    scene 38lingeriestore

    p "Oh, that guy?"
    p "Nope."
    p "Classified."
    p "Eyes only, I'm afraid."
    p "But I can tell you he deserved every volt."

    scene 39lingeriestore

    b "Alright but why did you offer yourself to me for eighty dollars?"
    b "And... what if I would have taken it?"
    b "Would you have zapped me too?"

    scene 38lingeriestore

    p "Nah, I wouldn't have let it get that far."
    p "I can't believe you said 'No', though!"
    p "You're just a regular Prince Charming, aren't you?"
    p "Well, I had some time to kill before that drug dealer arrived so I figured I'd warm
        up my acting skills."
    p "And my appropriation skills!"

    scene 42lingeriestore

    b "Appropriation skills?"
    b "What did you 'appropriate'?"

    scene 51lingeriestore

    pause

    scene 53lingeriestore with dissolve

    p "Your wallet."

    scene 55lingeriestore

    b "How in the hell..?"

    scene 56lingeriestore with dissolve

    b "Gimme that, you mischievous little pixie!"

    scene 38lingeriestore

    p "There was an adorable picture of your niece in there."
    p "Is that, perchance, why you're here today?"

    scene 39lingeriestore

    b "Actually, it is."
    b "She was sexually assaulted and I wanted to hire a professional to locate
        the guy that did it."
    b "Do you know of a professional that can help me?"
    b "Like a colleague of yours?"
    b "Someone... else?"

    scene 8lingeriep

    p "Har har."
    p "You're soooo hilarious."

    scene 38lingeriestore with dissolve

    p "Come on now, what can you tell me about him?"
    p "First name, home address, hair color, scars, tattoos?"

    scene 42lingeriestore

    b "I know his name is Seth."
    b "And he's a dentist."

    scene 7lingeriep

    p "What!?"
    p "That's all you have to go on??"
    p "You bring me crumbs and I'm supposed to make a four-course meal?!"
    p "Madness, Prince! Absolute madness!"

    scene 39lingeriestore

    b "Damn, so it's not enough?"

    scene 38lingeriestore

    p "Oh don't misunderstand, I can absolutely do it!"
    p "I just want to emphasize the difficulty so that when I do find him,
        you will be profoundly impressed."
    p "As you should be."

    stop music fadeout 2.0

    b "You really like to toot your own horn, don't you?"

    scene 43lingeriestore

    play music "audio/red_head.mp3"

    e "Excuse me, Sir."
    e "I need to speak with the young lady for a moment."

    b "Uhh, sure."

    scene 44lingeriestore with dissolve

    e "What the hell, Penny?!"
    e "This guy is completely laid out!"
    e "And his drawers are filled with urine and feces!"

    scene 9lingeriep
    p "You should have seen it, Evans!"
    p "He was like 'Aw, I'm gonna suck on your boobies, bitch!'"
    p "And I was like,"

    scene 10lingeriep with dissolve

    p "'Suck on this, Punk!'"

    scene 9lingeriep with dissolve

    p "And then I used a taser on his ass!"

    scene 46lingeriestore

    e "Are you insane, Penny?"
    e "That guy could have--"

    scene 9lingeriep

    p "But he was totally resistant to the taser!"

    scene 10lingeriep with dissolve

    p "So we both put our dukes up and entered into a classic battle of fisticuffs!"

    scene 9lingeriep with dissolve

    p "But he was too slow!"
    p "So I told him 'You're not even worthy of being struck by these fists of fury!'"

    scene 10lingeriep with dissolve

    p "And that's when I pimp slapped the bitch out of him."
    p "I hit him so hard, he shit himself and passed out."

    scene 38lingeriestore with dissolve

    p "Tell him, [player_name]."
    p "Tell him that's exactly what happened."

    scene 43lingeriestore with dissolve

    b "That's not at all what happened."

    scene 8lingeriep with dissolve

    p "You, Sir, are a traitor and a douche."

    scene 43lingeriestore with dissolve

    e "She likes to exaggerate and she's extremely full of herself."
    e "Except when she's wrong about somethin' and has a complete meltdown."
    e "She swings dramatically from obnoxious arrogance to utter despair."

    scene 46lingeriestore with dissolve

    e "Why do you do this to me, Penny?"
    e "You make my job harder than it should ever be!"
    e "How am I supposed to arrest a guy who's unconscious and swimming in his
        own feces and urine?"

    scene 48lingeriestore

    p "Yes, I can see how that could be a problem."
    p "I think there is a box of tissues in one of the changing rooms."

    scene 45lingeriestore

    e "Are you suggesting I wipe his ass with tissues!?"
    e "And then what??"
    e "Fireman's carry him down to my car?"

    scene 50lingeriestore

    p "Wow, sounds like you've got it all figured out!"
    p "Let me know if you need any help though."
    p "I'm sure [player_name] here has some free time to lend a hand!"

    b "Don't sign me up for that!"

    scene 45lingeriestore

    e "You know what, Penny?"
    e "I've got a promotion coming up in a few days."
    e "Then, you'll be some other police officer's problem!"

    scene 43lingeriestore with dissolve

    e "Sorry to have bothered you, Sir."
    e "Have a nice day."

    stop music fadeout 2.0

    b "Y-you too, Officer."

    scene 39lingeriestore

    b "I can't believe you talk to him like that."
    b "He's in a position of authority."
    b "Shouldn't you show him some respect?"

    scene 35lingeriestore

    play music "audio/sneaking_up_on_you.mp3"

    p "He's a person, just like everyone else, Prince."
    p "My respect isn't given out freely no matter what position you hold in society."
    p "It's earned."
    p "Besides, we're just playing around."
    p "We collaborate on most issues and generally we both get what we want."
    p "Heck, half the reason he's getting that promotion is because of me."

    scene 40lingeriestore

    b "That's fair."
    b "You know, I kind of thought you were a crazy person at first."
    b "But it seems like you're a lot different than I imagined."

    scene 8lingeriep

    p "Thanks?"

    scene 51lingeriestore with dissolve

    pause

    scene 52lingeriestore with dissolve

    b "What are you doing?"

    p "I'm looking for this guy."
    p "Hmm..."

    b "Can you find him?"

    p "Assuming he's actually a dentist, the most likely candidate here is a man named Tyler."
    p "Which, if I'm correct, means he was using a false name."
    p "Interesting."

    scene 42lingeriestore

    b "Can we talk about the price?"
    b "What's this going to set me back?"

    scene 51lingeriestore

    p "Five thousand."

    scene 41lingeriestore

    menu:
        "{b}Additional Dialogue Choice{/b}"
        "Yen!?":
            b "You must be talking about Yen, Penny."
            b "Cause nobody would pay five thousand American dollars for this!"

        "Rupees!?":
            b "You must mean Rupees or something!"
            b "Because there is no way you're asking me for five thousand American
                dollars!"

        "Bitcoin?":
            b "You mean, like, five thousand bitcoins??"
            b "Cause that's like, fifty cents."
            b "I can swing that."

    scene 35lingeriestore

    p "Why are you complaining?"
    p "It doesn't even put a dent in all that money your father gave you."

    scene 41lingeriestore

    b "H-how did you know about that?!"
    b "Nobody is supposed to know I got that money from my biological father!"

    scene 38lingeriestore

    p "I didn't know it was a secret!"
    p "What do you tell everyone when they ask you how you afford the nice, fluffy
        toilet paper?"
    p "You're friggin' unemployed!"

    scene 39lingeriestore

    b "I've been telling people I sold a successful fitness app."
    b "It seemed simple enough and nobody seems to care to see it."
    b "It worked pretty well as a cover story, actually."

    scene 35lingeriestore

    p "Well, your secret is safe with me."
    p "Now, I've got research to do!"
    p "When you wire the money, I'll get started."

    scene 57lingeriestore with dissolve

    p "I'm not going to lie, Prince."
    p "This little meeting we had today was surprisingly enjoyable for me."
    p "Perhaps the next time we meet, it will be less business and more pleasure?"

    scene 58lingeriestore with dissolve

    b "I'm just interested in business, Miss Penny."
    b "I'll wire you the money."
    b "What's your next move?"
    b "How are you going to find dirt on this guy?"

    scene 59lingeriestore with dissolve

    p "Hmm."
    p "I don't know, Sir Knight."
    p "What do you think I should do?"
    p "Penny for your thoughts?"

    scene 60lingeriestore

    play sound "audio/coinflip.mp3"

    b "Wha--"

    scene 61lingeriestore

    stop music fadeout 2.0

    b "What did you throw at me?"

    scene 62lingeriestore

    b "Is this..?"

    scene 68lingeriestore

    bi "{i}It's a penny.{/i}"
    bi "{i}Very clever.{/i}"
    b "Maybe you should--"

    scene 63lingeriestore

    bi "{i}She's gone!{/i}"
    bi "{i}She didn't want my advice.{/i}"
    bi "{i}She only wanted to distract me.{/i}"
    bi "{i}And I fell for it.{/i}"



    return
