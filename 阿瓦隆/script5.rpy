
label act_five:

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

    jump act_five_s

label act_five_s:

    stop music fadeout 2.0

    scene avalon with fade

    if persistent.actFive == False:
        $ renpy.notify("You've unlocked Act Five in Act Select on the Main Menu!")
        $ persistent.actFive = True

    pause

    scene avalonactfive with dissolve

    pause

    play music "audio/bored_to_death.mp3"

    show p_handstand

    pause

    scene 6pcabin with dissolve

    ps2 "Whew."

    scene 7pcabin with dissolve

    pause

    scene 8pcabin with dissolve

    pause

    scene 9pcabin with dissolve

    pause

    show p_egg

    pause

    scene 14pcabin with dissolve

    pause

    scene 15pcabin with dissolve

    stop music fadeout 2.0

    pause

    scene 16pcabin with dissolve

    pause

    scene 17pcabin with dissolve

    pause

    play sound "audio/bath_fill.mp3"

    scene 18pcabin with dissolve

    pause

    scene 19pcabin with dissolve

    pause

    scene 20pcabin with dissolve

    stop sound fadeout 2.0

    pause

    scene 21pcabin with dissolve

    pause

    scene 22pcabin with dissolve

    pause

    scene 23pcabin with dissolve

    play music "audio/secretly_spying_on_you.mp3"

    pause

    scene 24pcabin with dissolve

    pause

    scene 25pcabin with dissolve

    pause

    scene 26pcabin with dissolve

    pause

    scene 27pcabin with dissolve

    pause

    scene 28pcabin with dissolve

    pause

    scene 29pcabin with dissolve

    pause

    scene 31pcabin with dissolve

    pause

    scene 32pcabin with dissolve

    ps2 "I love this weather."
    ps2 "It's as if a cloud is sitting right on the surface of the planet."
    ps2 "You could lose yourself in that fog and nobody would ever find you."

    scene 30pcabin

    ps2 "Or you could bury a body without having any random, pesky joggers accidentally
        catch you."
    ps2 "Theoretically speaking, of course."

    scene 33pcabin with dissolve

    merc "I take it you ain't talkin' to yourself."
    merc "Knew I was here, did you?"

    ps2 "You're stomping around in steel-toe boots."
    ps2 "I heard you from all the way outside."

    scene 34pcabin with dissolve

    merc "Well, I never was much keen on stealth."
    merc "Figure if I'm gonna kill someone, there's not much point in bein' subtle about it."

    scene 36pcabin with dissolve

    ps2 "You're going to kill me?"
    ps2 "And on this perfect day?"
    ps2 "It would be an awful shame to miss out on a walk amongst the clouds."
    ps2 "Perhaps we can reschedule for tomorrow?"

    scene 38pcabin

    merc "'Fraid I can't do that."
    merc "Ya been pokin' your business in the wrong places."
    merc "Now I got orders to put ya in the ground."
    merc "Got no choice, Miss Penny."

    scene 37pcabin

    ps2 "Oh, you know my name?"
    ps2 "It would be rude to know my name and not tell me yours."
    ps2 "Go on, introduce yourself."

    scene 35pcabin

    merc "Everybody just calls me Merc."
    merc "I suppose you can too, for the short time you got left."

    scene 40pcabin with dissolve

    pause

    scene 41pcabin with dissolve

    merc "Now, I know you got somethin' behind yer back."
    merc "I'm gonna need you to show it to me real nice and slow like."

    scene 42pcabin

    ps2 "Oh, this?"
    ps2 "I was just about to make breakfast!"

    scene 43pcabin with dissolve

    ps2 "Would you like an egg before you kill me?"
    ps2 "Scrambled or over easy?"

    merc "Just put it down."

    ps2 "Alright then."

    scene 45pcabin with dissolve

    ps2 "I'll set it right here on the counter."
    ps2 "Just as you've asked."

    scene 46pcabin with dissolve

    ps2 "Oops!"
    ps2 "I think I accidentally sent it rolling across the table."

    scene 47pcabin with dissolve

    ps2 "Oh dear me, I can't believe how clumsy I am."
    ps2 "I'm so embarrassed."

    scene 41pcabin

    stop music fadeout 1.0

    merc "A broken egg is about to be the least of your--"

    play sound "audio/alarm_buzz.mp3"

    scene 48pcabin with dissolve

    merc "What the..?"

    scene 49pcabin

    stop music fadeout 1.0

    merc "What is--"

    play sound "audio/flash_bang.mp3"

    scene 50pcabin

    pause .1

    scene white

    merc "Gah! Fuck!"
    merc "I'm.. I'm blind!"
    merc "I can't--"

    play sound "audio/body_punch.mp3"

    pause .35

    merc "Ugh!"

    scene black with fade

    play sound "audio/bodyfallmat.mp3"

    pause

    scene 51pcabin with fade

    play music "audio/sneaking_up_on_you.mp3"

    ps3 "Merc."
    ps3 "Merc!"

    scene 52pcabin with dissolve

    ps3 "Wake up, you lazy toolbox!"
    ps3 "I didn't even hit you that hard."

    merc "Where..?"

    scene 62pcabin with dissolve

    merc "A... chest?"

    ps3 "Yeah, that's my chest."
    ps3 "Did you get a good look, Toughness?"

    scene 54pcabin with dissolve

    merc "At what? Your little boy's chest?"
    merc "Not really. I don't have my magnifying glass with me."

    scene 55pcabin with dissolve

    pause

    play sound "audio/faceslap.mp3"

    scene 56pcabin

    merc "Ugn!"
    merc "This must be what it feels like to be slapped by a toddler."
    merc "It's surprisingly painful."

    ps3 "Hey, look at me."

    scene 53pcabin

    merc "What?"

    ps3 "Did you have a nice nap, Pumpkin?"
    ps3 "You were asleep for nearly an hour."
    ps3 "What kind of bitch assassin gets knocked out for that long after one little
        elbow to the noggin?"

    scene 54pcabin

    merc "What kind of hooker wears that much eyeliner?"
    merc "Do you have a gig at the circus later?"

    scene 55pcabin with dissolve

    merc "Are you finally going through your emo ph--"

    play sound "audio/faceslap.mp3"

    scene 56pcabin

    merc "Fuck!"
    merc "It's like a perfect open palm slap every time!"

    scene 57pcabin

    ps3 "You know, I expected Mr. Gladstone to send a more experienced goon."
    ps3 "You're really the best he's got?"
    ps3 "My disappointment is substantial."

    scene 54pcabin with dissolve

    merc "I guess he didn't think a runty boy like you would give me too much trouble."
    merc "Where'd you get an egg-shaped flashbang, anyway?"
    merc "I never seen shit like that before."

    scene 57pcabin

    ps3 "Did you like that?"
    ps3 "It's just something special I cooked up for morons like you that have
        to yap away instead of just finishing a job."
    ps3 "You had so much time to shoot me!"

    scene 54pcabin

    merc "I wasn't sure the right person was standin' before me."
    merc "They said I was supposed to kill a nosey detective."
    merc "But they didn't say anything about a pointy-nosed halfling!"

    scene 55pcabin with dissolve

    pause

    play sound "audio/faceslap.mp3"

    scene 56pcabin

    merc "Goddammit!"
    merc "Quit! Quit slappin' me with those baby hands!"

    scene 59pcabin

    ps3 "Merc, you broke into my house."
    ps3 "While I was indecent, no less."
    ps3 "I'm afraid your punishment is going to have to be quite severe."

    scene 58pcabin

    merc "I can take a tremendous amount of pain!"
    merc "You'll never break me!"
    merc "And no matter what, I ain't gonna tell you shit!"

    scene 57pcabin

    ps3 "I think you misunderstand, Merc."
    ps3 "I'm not going to physically hurt you."
    ps3 "No, no."
    ps3 "I'm going to destroy your dignity."

    merc "W-what?"
    merc "How?"

    scene 60pcabin with dissolve

    ps3 "With this!"

    merc "Is that... a pen?"

    ps3 "It's a very special pen."

    merc "You gonna gouge my eyes out with it or somethin'?"

    scene 61pcabin with dissolve

    stop music fadeout 2.0

    ps3 "No, Merc."
    ps3 "I'm going to do something much worse!"

    scene black with dissolve

    pause (1)

    show b_comp with fade

    bi "{i}Finding a professional for Avalon to talk to was always the plan.{/i}"
    bi "{i}I thought maybe I could help her myself but I'm afraid I was wrong.{/i}"
    bi "{i}I don't care about the sex, I can wait.{/i}"
    bi "{i}But for some reason, she can't.{/i}"
    bi "{i}And then when we're fooling around, I get caught up in it all and forget
        about her trauma.{/i}"
    bi "{i}It's time for us to get outside help.{/i}"
    bi "{i}Ah, here we are.{/i}"
    bi "{i}There's a highly rated therapist not too far from us.{/i}"
    bi "{i}Oh, they have an opening this morning!{/i}"
    bi "{i}Scheduled!{/i}"
    bi "{i}Now I just have to hope Avalon isn't opposed to this.{/i}"
    bi "{i}She should be out of the shower any--{/i}"

    a3 "Uncle [player_name]?"

    play music "audio/one_step_closer.mp3"

    scene 4rtherapist with dissolve

    b "Hm?"
    bi "{i}Right on cue!{/i}"

    scene 5rtherapist

    b "You look absolutely lovely today."

    a3 "Thank you."

    scene 6rtherapist with dissolve

    a3 "I'm sorry about last night."
    a3 "I know it really isn't fair to you that I..."
    a3 "You know, have those episodes."

    scene 7rtherapist

    b "I don't care about the sex, Avalon."
    b "I just want us to be happy."
    b "I worry that you're trying to rush into sex and we really don't have to."

    scene 8rtherapist

    a3 "I know that, Uncle."
    a3 "But it's important to me."

    scene 9rtherapist with dissolve

    a3 "It's important that one stupid event doesn't ruin the rest of my life."
    a3 "Because..."
    a3 "You can't let someone take so much from you so easily..."

    b "I love you, Avalon."

    scene 10rtherapist with dissolve

    a3 "I love you, too."
    a3 "What spurred that all of the sudden?"

    scene 13rtherapist

    b "I worry about you, Avalon."
    b "I don't know enough about what you're going through to help you."
    b "And I'm afraid I might be making things worse."
    b "I want you to talk to someone."
    b "A professional."

    scene 11rtherapist

    a3 "I don't think you're making things worse, Uncle."
    a3 "In fact, I feel better now than I have in months!"
    a3 "But, you're right, maybe it would help to talk to someone."

    scene 15rtherapist

    b "I was just doing some searching online and I believe I found someone."
    b "I scheduled an appointment for this morning."
    b "We'll have to leave soon to make it."

    scene 12rtherapist

    a3 "You made an appointment without asking me first?"
    a3 "You do that a lot, you know?"

    b "We can cancel..."

    scene 10rtherapist with dissolve

    a3 "No, I kind of like that you take charge, Uncle [player_name]."
    a3 "It's like this masculine, alpha male mode that you go into."
    a3 "It's sexy, actually."

    scene 14rtherapist

    b "If you like that, I was just about to mark you as my territory by peeing on you."
    b "I had asparagus last night so it should be extra musty."

    scene 12rtherapist

    a3 "Okay, less sexy."
    a3 "Now it's weird."
    a3 "You took it to the weird place, Uncle."

    b "My bad."

    scene 10rtherapist with dissolve

    a3 "Well, I'm ready to go now if you are."

    stop music fadeout 1.0

    b "Alright, let's go."

    scene 17rtherapist with fade

    a3 "This is so..."
    a3 "Chinese."
    a3 "Is it racist that all I see is how Chinese this is?"

    b "Yeah, it is."
    b "But you're right, it's really..."

    scene 16rtherapist

    b "Chinese."

    a3 "Right?"
    a3 "I mean, it's a nice waiting room."

    b "Yeah, it's not like it's bad because it's Chinese."

    a3 "No!"
    a3 "Obviously that's not what I'm saying."

    b "Maybe we should take a seat?"

    a3 "Right."

    scene 18rtherapist with dissolve

    b "I feel like a giant in here."
    b "Is that wrong to say?"

    a3 "You look really uncomfortable."
    a3 "Maybe try not to move around too much."
    a3 "Your footsteps might get mistaken for Godzilla."

    b "Too far! You took it too far!"
    b "And isn't Godzilla from Japan..?"

    scene 19rtherapist with dissolve

    b "So like, what do you think the Chinese imagine when they think of Americans?"

    menu:
        "{b}Additional Dialogue Choice.{/b}"
        "Freedom!":
            a3 "They probably picture like, a bald eagle karate-kicking Hitler in
                the balls."
            b "And is the bald eagle drinking a beer and eating a cheeseburger
                in this picture too?"
            a3 "Well, obviously."

        "Capitalism!":
            a3 "I wonder if they're jealous of our free market and how Corporations
                have complete freedom to take advantage of us due to limited restrictions
                imposed by the Government."

            b "The market will regulate itself."

            a3 "We have nothing to lose but our chains, Uncle!"

        "Obesity.":
            a3 "I read in a news article that we have the most obese people in the world."
            a3 "I wonder if they just see lumbering, gluttonous giants when they think of America."

            b "No way, you and I are in great shape!"

            a3 "Didn't you make a Donut Waffle with so much sugar that it almost killed you?"

            b "Oh right..."

        "'Merica!":
            a3 "I saw a picture online of Ronald Reagan riding a raptor with an
                automatic rifle and a rocket launcher."
            a3 "And I think that's the most American thing I've ever seen."

            b "That sounds awesome!"

    scene 21rtherapist

    sm "Excuse me?"
    sm "Avalon?"

    a3 "Yes?"

    scene 20rtherapist with dissolve

    sm "I'm Sun Mei, it's nice to meet you."

    a3 "Uhh, likewise!"

    sm "Dr. Yu will see you now."
    sm "Are you ready?"

    a3 "Sure."

    b "I'll be right out here."

    scene 22rtherapist with dissolve

    a3 "I'm admittedly a little nervous."

    sm "Most people are before their first session."
    sm "But I assure you, once you meet Dr. Yu, you'll feel right as rain."
    sm "Please follow me."

    scene 23rtherapist with fadefast

    sm "And here we are."
    sm "This is where Dr. Yu conducts his sessions."

    scene 23rtherapist2 with dissolve

    sm "This is my favorite part."

    a3 "Favorite part?"
    a3 "What do you--"

    scene 24rtherapist with dissolve

    a3 "Oh my gosh!"
    a3 "Wow!"

    sm "That."
    sm "Everyone's reaction is always so pronounced!"
    sm "I really love it."

    play sound "audio/guide_us.mp3" fadein 6.0

    scene 25rtherapist

    a3 "It's so beautiful!"

    sm "Dr. Yu is very proud of this."
    sm "Be sure to mention how much you like it!"

    a3 "I will!"

    sm "You can go see him now."

    a3 "Alright."

    scene 26rtherapist with dissolve

    a3 "I can't believe this place!"
    a3 "The upkeep must be insane."

    scene 29rtherapist with dissolve

    dr "You must be Avalon."
    dr "It is nice to meet you."

    a3 "It's nice to meet you, too, Dr. Yu."
    a3 "Do... do I bow?"
    a3 "I'm sorry, I'm not very experienced with other cultures."

    scene 27rtherapist

    dr "You can bow only if you would like to, Ms. Avalon."
    dr "Whatever you are comfortable with."

    scene 28rtherapist

    a3 "I think I'd like to try."

    scene 32rtherapist with dissolve

    a3 "Is it like this?"

    scene 33rtherapist with dissolve

    pause

    scene 32rtherapist with dissolve

    dr "That's very good, Ms. Avalon!"

    a3 "Yeah?"
    a3 "Thank you."

    scene 31rtherapist

    dr "You can also bow with your hands at your side if you prefer."
    dr "Like this."

    scene 30rtherapist with dissolve

    pause

    scene 31rtherapist with dissolve

    pause (.5)

    scene 27rtherapist with dissolve

    dr "But it is, of course, up to you!"

    scene 28rtherapist

    a3 "Okay, thank you for teaching me."
    a3 "This place is amazing, Dr. Yu."
    a3 "I've never seen anything like this before."
    a3 "It's... tranquil."

    scene 34rtherapist

    dr "Thank you, Ms. Avalon."
    dr "Would you like to have seat?"
    dr "We can also stand, if you prefer."

    a3 "Uhh, a seat sounds nice."

    scene 41rtherapist with dissolve

    dr "So, Ms. Avalon, what brings you here today?"

    scene 35rtherapist

    a3 "W-well, I guess I should start at the beginning."
    a3 "I used to live with my mom until recently."
    a3 "A few months ago, a man she had over snuck into my room and..."

    stop sound fadeout 1.0

    scene black with dissolve

    pause (1)

    scene 42rtherapist with dissolve

    play music "audio/your_hand_in_mine.mp3" fadein 2.0

    dr "I am very sorry to hear about this experience, Ms. Avalon."

    scene 41rtherapist with dissolve

    dr "But I am very glad to hear that you have such supportive friends."
    dr "Your Uncle sounds like a very nice man."
    dr "From what you've told me, however, he may benefit from treatment as well."

    scene 35rtherapist

    a3 "Yeah, he told me last night that he was the one that found my father
        after he overdosed."
    a3 "He really loved my father, too."
    a3 "I can't imagine how terrible that must have been."

    scene 41rtherapist

    dr "A great partnership is one where both parties can lean on each other in
        times when either are in emotional distress."
    dr "Let us focus on you for now."
    dr "You seem unusually interested in sexual intercourse, Avalon."
    dr "Why do you think that is?"

    scene 38rtherapist

    a3 "Oh, uhm..."
    a3 "I-I guess..."

    scene 35rtherapist with dissolve

    a3 "If I can have sex, then that means... I'm not broken anymore, right?"
    a3 "That man, he... he made me afraid of it."
    a3 "But if I stay afraid of sex, then he wins."
    a3 "And he shouldn't..."
    a3 "I'm also tired of people looking at me and thinking 'Victim'."
    a3 "And that's all they see."
    a3 "[player_name] tiptoes around me sometimes like I'm a fragile vase and..."

    scene 36rtherapist with dissolve

    a3 "And I hate that!"
    a3 "Sometimes I want him to be a little rough with me."
    a3 "But then I push him into something sexual and I have an episode which
        then causes him to be even more cautious!"
    a3 "It's awful!"

    scene 35rtherapist with dissolve

    a3 "I just... I don't want to be broken anymore."
    a3 "I want to enjoy sex."
    a3 "And I want to enjoy it with him..."

    scene 43rtherapist

    dr "That is a good answer, Avalon."
    dr "I am impressed with what a strong and positive young woman you are."
    dr "But just because something is broken, does not mean it is less valuable."
    dr "In Japan, when a bowl breaks, they do not discard it."
    dr "Instead, they repair it with beautiful resin or liquid gold."
    dr "It is called 'Kintsugi', and the act both bonds the person to the object and
        makes the object more interesting."

    scene 37rtherapist

    a3 "So you're saying if I let my friends help me heal, we'll become stronger together."
    a3 "And that my scars will make me unique and more experienced?"

    scene 41rtherapist

    dr "Yes, Ms. Avalon, that's very well put."

    scene 42rtherapist with dissolve

    dr "And it sounds as though you are experiencing panic attacks."
    dr "Sexual experiences may bring back memories of your assault, Ms. Avalon."

    scene 35rtherapist

    a3 "Yeah, I noticed that."
    a3 "And sometimes I have episodes even when I'm not doing anything at all."
    a3 "It can be so random."

    scene 41rtherapist

    dr "Ms. Avalon, that ring on your thumb, it looks important to you."
    dr "Can you tell me where you got it?"

    scene 37rtherapist

    a3 "Oh, yeah, my boyfriend gave it to me."
    a3 "He made it for my father but never had the chance to give it to him."
    a3 "It was made with the metal from a guitar my father loved."
    a3 "The ring is supposed to represent that love, both from my father and from [player_name]."
    a3 "So, that's what I see when I look at it."

    scene 43rtherapist

    dr "When you have a panic attack, I want you to try this."
    dr "Take a deep breath and count back from three."
    dr "Release your breath and focus on that ring."
    dr "Focus on how it makes you feel when you received that ring."

    scene 37rtherapist

    a3 "Okay, I'll try that."
    a3 "Thank you, Dr. Yu."

    scene 41rtherapist

    dr "I am sorry to say but our time is up for today."
    dr "You are doing very well, Ms. Avalon."
    dr "If you continue the way you have been, I am confident you will feel much better
        very soon."
    dr "And if you would like, I am happy to see you again soon."

    scene 37rtherapist

    a3 "This was really helpful, Dr. Yu!"
    a3 "Thank you so much for listening to me today, and for your advice."
    a3 "I'll definitely be back!"

    scene 41rtherapist

    stop music fadeout 1.0

    dr "Let me walk you out."

    scene 1moffice with fade

    pause

    scene 2moffice with dissolve

    play music "audio/fuzzbombs.mp3" fadein 2.0

    lance "Oh, shit."
    lance "She's giving you the puppy dog eyes {b}and{/b} biting her lip."
    lance "It's game over for you, boy."
    lance "Nobody can resist that look."
    lance "She's gonna make you her fuckin' puppet."

    scene 1moffice

    pause

    play sound "audio/dooropen.mp3"

    pause

    scene 3moffice with dissolve

    lance "Merc, buddy, I gotta tell you about this hooker I was bangin' last night."
    lance "She was so dirty, man, I found a pearl in her clam."

    scene 4moffice with dissolve

    play sound "audio/doorclose.mp3"

    lance "My crotch has been on fire all mornin'."
    lance "I'd go to the doctor but I think I might need an exterminator for these
        crabs she gave me."

    scene 5moffice with dissolve

    lance "You know you got a dick on your face?"

    scene 6moffice

    merc "Is it... is it noticeable?"
    merc "I thought maybe it wasn't that noticeable."

    scene 5moffice

    lance "There's a big black cock on your face, man."
    lance "Yeah, it's... it's noticeable."
    lance "What the fuck happened?"

    scene 12moffice

    merc "That chick Mr. Gladstone sent me to assassinate, she... she got the jump on me."
    merc "I figured she'd just kill me but she drew a penis on my face instead."
    merc "Somethin' about devastating my dignity."

    scene 7moffice

    lance "It's pretty hard to maintain your dignity when you're rockin' a nine
        inch black cock on your face."
    lance "It's pointed right at your beak, too."
    lance "If that thing blows its load, it's goin' right in your mouth, man."

    scene 10moffice

    merc "What do I do?"
    merc "I can't go out in public like this."
    merc "And I sure as shit can't tell Gladstone I failed with this on my face."

    scene 11moffice

    lance "I think the cock is gonna convey your failure without you havin' to say much."
    lance "Why don't you just wash it off, man?"
    lance "A little soap and water with some elbow grease, man, that shit should
        come right off."

    scene 8moffice

    merc "You don't think I tried that already!?"
    merc "I scrubbed for half an hour tryin' to get this off!"
    merc "It's some sort of special skin ink or somethin'."
    merc "Fuck."

    scene 9moffice

    lance "Ooh, I think I've heard of that."
    lance "It's like a temporary tattoo or somethin'"
    lance "It's supposed to last a few weeks, man."

    scene 7moffice with dissolve

    lance "Wait, you scrubbed at it for half an hour?"
    lance "So you essentially jerked off your face cock."
    lance "That's some gay shit, man."

    scene 10moffice

    merc "I'm gonna have this for weeks?"
    merc "What the hell am I supposed to do for a few weeks with this on my face?"
    merc "Do I wear a mask or..."

    scene 7moffice

    lance "Just get some cover-up."
    lance "You won't even notice it."
    lance "I mean, you'll be wearin' make up so you'll still look queer as fuck but
        'least you won't have a schlong poking you in the mustache."

    scene 11moffice with dissolve

    lance "Why don't you come watch this movie with me and we'll figure out what to
        do about that detective chick later?"
    lance "I promise, you'll feel better in an hour."

    merc "What's it about?"

    scene 13moffice with dissolve

    lance "This hippy pixie chick is trying to save her rainforest from some douchebag
        corporation that's cuttin' down all the trees."
    lance "And this human dude and some nutty bat are gonna help her."

    scene 14moffice with dissolve

    merc "Huh, yeah, that sounds pretty cool."
    merc "Is she hot?"

    lance "Yeah, man, check it out."
    lance "She's cute as hell."

    scene 15moffice with dissolve

    merc "Oh, it looks like he kind of surprised her with that kiss."

    lance "Yeah, you can't do that anymore."
    lance "That's, like, harassment now."
    lance "That's why I always pay for sex because then it's a business transaction and it's
        legit."

    scene 16moffice with dissolve

    merc "Check it out, she's totally not into it."

    lance "That's the bitch trap."
    lance "She just lured him in with a seductive gaze then pulled away when he went for the kiss."
    lance "Now he looks like a bitch."

    merc "He was too eager."
    merc "You gotta move slow enough so they see the kiss comin' or else you'll spook 'em."

    lance "For sure, man."

    stop music fadeout 2.0

    if octavia == True:
        jump bava_couch
    else:
        jump pennydhouse

    label pennydhouse:

    scene 1pennydhouse with fade

    play sound "audio/doorknock.mp3"

    pause

    d "Coming!"

    scene 3pennydhouse

    play music "audio/disturbed_mind.mp3"

    d "Oh, hello there!"
    d "Sorry, I'm not interested in any girl scout cookies."
    d "I've got a figure to maintain, you know?"

    scene 2pennydhouse

    ps3 "So we're starting our friendship out with friendly fire, are we?"
    ps3 "No, Ms. Dallas, I'm not here to sell you cookies."
    ps3 "If you ask real nice, I might help you remove your foot from your mouth though."
    ps3 "You've got it wedged in there pretty good."
    ps3 "I'm here to discuss the salon you posed interest in."
    ps3 "Are you still interested?"

    scene 4pennydhouse

    d "Oh shit!"
    d "You're Penny?!"
    d "I am so sorry, I had no idea."
    d "P-please, come in."

    scene 7pennydhouse with fadefast

    play sound "audio/doorclose.mp3"

    d "I really am sorry."

    ps3 "It's fine, it's actually not the first time I was mistaken for a girl scout."
    ps3 "To be fair though, the last time I was mistaken for one, I was dressed as one."
    ps3 "Fun story, actually."

    scene 6pennydhouse with dissolve

    ps3 "The guy I was after bought two boxes of cookies and I laced them heavily with
        laxatives."
    ps3 "He ate so many, he was hospitalized for dehydration."
    ps3 "It wasn't really the plan but it was still hilarious."

    scene 8pennydhouse

    d "Oh shit, that's epic!"
    d "I heard your pranks are wicked cool."
    d "I'm actually a huge admirer of yours."
    d "You gotta teach me, girl!"

    d "Oh, do you want anything to drink?"

    ps3 "No, thank you."

    d "Would you like to sit?"

    ps3 "Sure."

    scene 5pennydhouse with dissolve

    ps3 "Before we discuss anything, I'd first like to apologize."

    d "Apologize?"
    d "For what?"

    ps3 "For your detainment yesterday."

    d "W-what?"

    scene 14pennydhouse with dissolve

    ps3 "When I caught wind of [player_name]'s father, I wrapped up my other cases rather quickly."
    ps3 "One of those cases involved your cafe."
    ps3 "I'm the reason the police stormed it with such vigor."
    ps3 "I was made aware they were rather aggressive with you."
    ps3 "I'm sorry, Dallas."

    scene 15pennydhouse

    d "That was your doing?"
    d "Well, I mean, it didn't really bother me."
    d "It was fine, whatever."
    d "But I lost my job which I really needed..."

    scene 10pennydhouse

    ps3 "That's why I'm here."
    ps3 "A little birdie told me you were interested in the salon."
    ps3 "And I figured it was the least I could do for the trouble I caused."
    ps3 "It will take some time for me to get everything processed."
    ps3 "And there's a cost."

    scene 9pennydhouse

    d "I don't want any handouts."
    d "I can take out a loan or borrow from Avalon if I have to."
    d "But I want to earn this."
    d "And I'm confident I can turn it into a profitable and efficient business!"

    scene 10pennydhouse

    ps3 "I did my research, Dallas."
    ps3 "I saw your signature on nearly all the important documents at the cafe."

    stop music fadeout 2.0

    ps3 "You're a hard worker and you seem committed to whatever you start."
    ps3 "Although I have every intention of offering you this salon without fiscal cost,
        it would, by no means, be free."
    ps3 "There will be... a different kind of cost."

    play music "audio/sneaking_up_on_you.mp3"

    d "O-oh?"

    ps3 "It's pretty simple, I use various locations for my... operations."
    ps3 "One of these locations is where I met [player_name], actually."

    scene 11pennydhouse

    d "The lingerie store?"
    d "You have some sort of deal with the owner?"
    d "How??"

    scene 16pennydhouse

    ps3 "Very similar to the deal I'm making with you!"

    scene 10pennydhouse with dissolve

    ps3 "Now, I'll never ask you to do anything illegal and I'll never put you,
        or your staff, in danger."
    ps3 "But I may ask you to take a day off and allow me to use the building."
    ps3 "Or I might need a specific hairstyle and makeup that I can't do myself."

    scene 9pennydhouse

    d "I mean, you catch bad guys, right?"
    d "So, yeah, of course I'd be down to help."

    scene 11pennydhouse with dissolve

    d "It actually sounds pretty exciting!"
    d "Is there a story behind this Salon?"
    d "How did the government come to have it in their possession?"
    d "Did you have a hand in it??"

    scene 12pennydhouse

    ps3 "They were doing more than just cutting hair."
    ps3 "There was a second, secret business they had going on."
    ps3 "The classic money for sex."
    ps3 "I didn't really care about that but when one guy got too aggressive, they
        stabbed him to death and dumped his body in the lake."
    ps3 "They must have gotten a taste for it because guys that went there started going
        missing pretty consistently."

    scene 13pennydhouse

    d "Holy shit, that's really intense!"
    d "What did you do?"

    scene 16pennydhouse

    ps3 "I summoned forth an army of robot ninja kittens from outer space and together,
        we fought and defeated their army of megasluts!"

    scene 15pennydhouse

    d "You don't have to tell me what happened but damn, that went from zero to
        absolutely fucking bonkers real quick."

    scene 14pennydhouse

    ps3 "Alright, so the story isn't that exciting."
    ps3 "I found where they were dumping the bodies and let the police take care of it
        from there."
    ps3 "But who wants to hear that lame ass story!?"

    scene 10pennydhouse with dissolve

    ps3 "I've got a lot to do still today so I must be heading out."
    ps3 "But if I find some time, maybe you, Avalon and I can check out that salon."
    ps3 "How does that sound?"

    scene 11pennydhouse

    d "That would be fucking awesome!"

    scene 9pennydhouse with dissolve

    stop music fadeout 2.0

    d "And thank you, Penny."
    d "This is really cool what you're doing for me."
    d "I appreciate it."

    scene 10pennydhouse

    ps3 "You're welcome."
    ps3 "I'll give you a call soon."

    label bava_couch:

    play music "audio/a_quiet_thought.mp3"

    scene 1bavacouch with fade

    bi "{i}When we were younger, one of my favorite things that Avalon would do
        was to climb into my lap and cuddle up to me.{/i}"
    bi "{i}She stopped a little before she became a teenager.{/i}"
    bi "{i}Now, after our relationship developed into something new, she started
        doing it again.{/i}"
    bi "{i}And when I'm holding her, I don't have room to hold onto anything else.{/i}"
    bi "{i}I don't have room to hold on to anger, or sadness, or despair.{/i}"
    bi "{i}I only have room for her.{/i}"

    ai3 "{i}Sometimes when I would feel anxious or stressed or sad, I'd curl up in
        my bed under the sheets.{/i}"
    ai3 "{i}But despite being under a comforter, it still felt... cold.{/i}"
    ai3 "{i}Now I just find [player_name] instead and cuddle up in his arms.{/i}"
    ai3 "{i}It always feels warm here.{/i}"
    ai3 "{i}It always feels safe.{/i}"

    scene 2bavacouch with dissolve

    b "Avalon, I wanted to ask how your session went."
    b "I know it's private so you don't have to tell me."
    b "But if you want to talk about it, I'd like to listen."

    scene 3bavacouch with dissolve

    a3 "No, it's fine. I don't mind."
    a3 "I just told him what I told you."
    a3 "I don't want to live my life with the shadow of one terrible thing
        constantly looming over me."
    a3 "I want to move forward and enjoy my life."
    a3 "And no matter what, I'm going to keep fighting until it doesn't control
        me anymore."

    scene 9bavacouch with dissolve

    b "I can't say I really know how to help."
    b "But I'll always try, and I'll always be there to support you."

    scene 8bavacouch with dissolve

    a3 "I really appreciate that but..."
    a3 "Dr. Yu said you might benefit from therapy as well."
    a3 "And, I hadn't really thought about it much before but you did find my
        dad after he overdosed."
    a3 "That must have taken a toll, didn't it?"
    a3 "Mom doesn't talk about Grandma and Grandpa much but she did say you were there
        when they passed."

    scene 5bavacouch with dissolve

    b "Johnny's death certainly wasn't easy to handle."
    b "And yes, I was there when Frank had his heart attack."
    b "I remember, I called for an ambulance but..."
    b "He took his last breath in my arms before they made it."

    scene 6bavacouch with dissolve

    b "A few months later, I found Wendy in her car with it on and a hose running
        from the tailpipe into her window."
    b "I guess... she didn't know how to live without her partner."
    b "She was always good to me. I miss her."

    scene 7bavacouch with dissolve

    a3 "I didn't actually know all that."
    a3 "I can't imagine what you must have felt, Uncle."
    a3 "If..."

    scene 10bavacouch with dissolve

    a3 "If I asked you to see Dr. Yu, would you do it?"
    a3 "Would you do it for me, [player_name]?"

    scene 4bavacouch with dissolve

    b "I mean, I always had to take care of myself."
    b "I've never considered outside help."
    b "If it's important to you, I guess I can give it a try."

    scene 10bavacouch with dissolve

    a3 "It is important."
    a3 "I think in some ways, we're both broken."
    a3 "And I want us both, you know, put back together."
    a3 "So we can get the most out of our relationship and be whole again."

    scene 5bavacouch with dissolve

    b "Mm, alright."
    b "I'll schedule an appointment."

    scene 3bavacouch with dissolve

    a3 "Thank you."

    scene 2bavacouch with dissolve

    b "Avalon, I was thinking you could see your mom today."
    b "If you're up for it?"

    scene 7bavacouch with dissolve

    a3 "Yeah, that's probably a good idea."
    a3 "You said she's been a bit better with Randall around."
    a3 "I hope that's true."
    a3 "I think I should go alone though."

    scene 6bavacouch with dissolve

    b "Sure, yeah, some personal time with your mom is probably a good idea."

    scene 7bavacouch with dissolve

    a3 "Would you mind if I took your truck?"

    scene 5bavacouch with dissolve

    b "Do you still remember how to drive it?"
    b "It's been a while."

    scene 3bavacouch with dissolve

    a3 "Yeah, of course!"
    a3 "It's the first vehicle I learned to drive."
    a3 "I remember how."
    a3 "And... thank you for teaching me and helping me get my license."
    a3 "I guess that was just before I stopped seeing you for a while, huh?"

    scene 4bavacouch with dissolve

    b "Er, yeah, I'm sorry I disappeared for so long."
    b "I had something to take care of."

    scene 7bavacouch with dissolve

    a3 "Oh, that's alright."
    a3 "Maybe we can talk about where you were sometime?"

    scene 6bavacouch with dissolve

    b "Maybe."
    b "But I'd rather not today."
    b "Let's focus on you for now."

    a3 "If you insist."

    if monogamy == True:
        jump gladoffice
    else:
        if octavia == True:

            scene 8bavacouch with dissolve

            a3 "I did actually want to talk to you about something."
            a3 "Would it be crazy if we were more than... just us?"

            b "How do you mean?"

            a3 "Well, what if our relationship wasn't just the two of us?"
            a3 "What if it was three..?"

            b "You mean Octavia?"

            scene 10bavacouch with dissolve

            a3 "Yeah, do you think that's possible?"
            a3 "Like, a relationship between three people?"
            a3 "You said it was alright if I fooled around with Octavia but I'm afraid I moved past just fooling around."
            a3 "I think I'm falling for her."
            a3 "But I also love you so..."
            a3 "Why can't it be--?"

            scene 9bavacouch with dissolve

            b "A love triangle?"
            b "It's uncharted territory for me."
            b "I don't want to do anything that might jeopardize our relationship."
            b "Doesn't it make you feel uncomfortable imagining me being intimate with
                Octavia?"

            scene 8bavacouch with dissolve

            a3 "Actually, I'm kind of getting aroused at the thought."
            a3 "Imagining you and Octavia with your hands all over each other, making out
                and fondling one another..."
            a3 "Is it weird I'm excited by that?"

            scene 9bavacouch with dissolve

            b "Yeah."
            b "You're a total freak."
            b "But I still love you."
            b "If this is something you want to try, I wouldn't be opposed."
            b "Octavia is a fascinating and beautiful woman."
            b "I'd be lying if I said the idea didn't intrigue me."

            scene 3bavacouch with dissolve

            a3 "Good!"
            a3 "I'll set up a date then!"

            jump gladoffice

        else:

            a3 "And, I wanted to talk to you about something else."
            a3 "Would it be crazy if we were more than... just us?"

            b "How do you mean?"

            a3 "Well, what if our relationship wasn't just the two of us?"
            a3 "What if it was three..?"

            b "You mean Dallas?"

            scene 10bavacouch with dissolve

            a3 "Yeah, do you think that's possible?"
            a3 "Like, a relationship between three people?"
            a3 "You said it was alright if I fooled around with Dallas but I'm afraid I moved past just fooling around."
            a3 "Dallas is my best friend and I really love her."
            a3 "But I also love you so..."
            a3 "Why can't it be--?"

            scene 9bavacouch with dissolve

            b "A love triangle?"
            b "It's uncharted territory for me."
            b "I don't want to do anything that might jeopardize our relationship."
            b "Doesn't it make you feel uncomfortable imagining me being intimate with
                Dallas?"

            scene 8bavacouch with dissolve

            a3 "Actually, I'm kind of getting aroused at the thought."
            a3 "Imagining you and Dallas with your hands all over each other, making out
                and fondling one another..."
            a3 "Is it weird I'm excited by that?"

            scene 9bavacouch with dissolve

            b "Yeah."
            b "You're a total freak."
            b "But I still love you."
            b "And if this is something you want to try, I can't say I'd be opposed."
            b "Dallas and I have a certain chemistry and I am quite fond of her."
            b "Having her in our relationship feels... right."

            scene 3bavacouch with dissolve

            a3 "Good!"
            a3 "I'll set up a date then!"

            jump gladoffice

    label gladoffice:

    stop music fadeout 1.0

    scene 1gladoffice with fade

    lance "A flashbang shaped like an egg?"
    lance "That's wild, man."
    lance "And she slapped you right in the face?"
    lance "Three times!?"

    scene 2gladoffice with dissolve

    merc "Yeah, I mean, it didn't hurt at all."
    merc "She's got little hands so it was mostly just annoying."

    scene 2gladoffice with dissolve

    lance "It's the message, man."
    lance "Bein' slapped by a woman, it's more than pain."
    lance "It's like she's sayin' you were bein' offensive."
    lance "We don't deserve to be slapped, man. We respect women."
    lance "Like that hooker I was balls deep in last night, for example."
    lance "I tipped her an extra ten bucks, man!"

    scene 3gladoffice with dissolve

    merc "Yeah, no, we're respectful to women."
    merc "Heck, I held the door open for an old lady the other day."
    merc "I mean, I kind of zoned out and forgot what I was doin' while holdin' the door
        and she just walked on through."
    merc "But I still did it."

    lance "It counts, man."

    scene 4gladoffice with dissolve

    merc "What was that prostitute's name you were bangin' yesterday?"

    scene 5gladoffice with dissolve

    merc "She sounds kind of hot."

    lance "Fuck if I remember, man."
    lance "I just remember those tits."
    lance "Damn, they were floppy."
    lance "But you can't be picky when you're bargin' shoppin' for bitches."

    merc "Cash has been tight lately."
    merc "I wonder if Gladstone is going to get more work for us soon."

    lance "Don't know, man."
    lance "Seems like he might be on his way outta the game."

    scene 6gladoffice with dissolve

    play music "audio/rumors_about_us.mp3"

    merc "Yeah, maybe."

    scene 7gladoffice with dissolve

    merc "Seems like he's been distracted lately."

    scene 8gladoffice with dissolve

    lance "Hm?"
    lance "What was that?"

    scene 9gladoffice with dissolve

    merc "Probably nothin'."
    merc "Elevator has been a little wonky lately."

    scene 10gladoffice with dissolve

    play sound "audio/taser.mp3"

    lance "GAAHHH!"

    scene 11gladoffice with dissolve

    merc "L-lance!?"
    merc "Oh fuck!"

    scene 12gladoffice with dissolve

    ps3 "Missing your gun?"
    ps3 "They confiscated it downstairs, Doofus."
    ps3 "You forget already?"

    scene 13gladoffice with dissolve

    ps3 "Stick 'em up, Merc."

    merc "I-is that..?"
    merc "Is that a banana?"

    ps3 "Was the egg an egg?"

    scene 14gladoffice

    ps3 "But who knows?"
    ps3 "Maybe I'm bluffing?"
    ps3 "And if I am, I'm just a little girl, right?"
    ps3 "You could take me."

    scene 13gladoffice

    merc "It does look an awful lot like a regular banana..."

    scene 15gladoffice with dissolve

    merc "And you are pretty small."
    merc "..."

    scene 16gladoffice with dissolve

    merc "Nah, you're fucking with me."
    merc "I'm not playing your game."
    merc "Fuck that shit."

    scene 14gladoffice

    ps3 "Smart decision, Merc."
    ps3 "Now, I'm going to go have a little meeting with Gladstone."
    ps3 "Do you know what's going to happen to you if you interrupt that meeting?"

    merc "You're gonna draw a dick on my face?"

    ps3 "No, I already did that."

    merc "Well, fuck, I dunno!"

    ps3 "Exactly, Merc."
    ps3 "You don't know."
    ps3 "So stay here and take care of your dipshit friend, alright?"

    scene 16gladoffice

    merc "I am so fired."

    stop music fadeout 1.0

    scene 17gladoffice with fadefast

    pause

    scene 18gladoffice with dissolve

    pause

    scene 19gladoffice with dissolve

    pause

    play sound "audio/dooropen.mp3"

    scene 20gladoffice with dissolve

    glad "Hm?"

    scene 21gladoffice

    play music "audio/sneaking_up_on_you.mp3"

    ps3 "Mm, Mhmm."
    ps3 "Yeah."
    ps3 "Tha's a goo' banana."

    play sound "audio/swallow.mp3"

    scene 22gladoffice with dissolve

    ps3 "And this goes right..."

    scene 23gladoffice with dissolve

    ps3 "Here."

    scene 24gladoffice

    pause

    scene 25gladoffice with dissolve

    pause

    scene 26gladoffice with dissolve

    glad "Penny."
    glad "You being here means my professional henchmen failed, doesn't it?"

    ps3 "You have professional henchmen??"
    ps3 "Where?"

    scene 27gladoffice with dissolve

    glad "It does seem they've lost a step in recent years."
    glad "Though, to be honest, so have I."
    glad "I'm not the young and adventurous man I once was."

    ps3 "Yeah, your face looks like a reused condom."
    ps3 "Even your beard has wrinkles."

    scene 28gladoffice with dissolve

    glad "So you come into my office uninvited, you litter my floor with garbage and
        you make sport of my age."

    glad "What is it you want, Detective Penny?"

    scene 29gladoffice

    ps3 "I want your excuse."
    ps3 "You know how the villain always has some elaborate justification for all
        the terrible things they've done."
    ps3 "I'm especially interested in yours!"
    ps3 "Don't disappoint me now."

    scene 30gladoffice

    glad "I am no villain, girl."
    glad "I've simply accepted the way the world works."
    glad "You're either the hunter or the prey."
    glad "And I, my dear, am the hunter."

    scene 31gladoffice

    ps3 "The law of the jungle."
    ps3 "I've heard that one before."
    ps3 "I expected something better from you, Gladstone."

    scene 29gladoffice with dissolve

    ps3 "But I can work with this."
    ps3 "Today, you are not the lion."
    ps3 "You are the gazelle."
    ps3 "And I've got you by the throat."

    scene 32gladoffice

    glad "I'm sorry to disappoint you, girl."
    glad "But you don't have a gazelle."
    glad "You've got in your grasps a dying old buck."
    glad "I have long since retired."

    scene 33gladoffice

    ps3 "Retired?"
    ps3 "You sent a goon after me."
    ps3 "Albeit a shitty one but he did still aim to kill me."
    ps3 "Seems to me you're still very much active, Gladstone."

    scene 30gladoffice with dissolve

    glad "I know what you want."
    glad "You want to see me dead or imprisoned."
    glad "I may be out of the business but I've still got myself, and my collection,
        to protect."
    glad "So yes, in that regard, I am still actively protecting my interests."

    scene 35gladoffice with dissolve

    glad "I fought hard to collect artifacts throughout my life."
    glad "Most of them I sold to other collectors or museums."

    scene 37gladoffice with dissolve

    glad "But this one..."
    glad "This one is very special."

    scene 36gladoffice

    ps3 "From the grime on it and the smell, I'd wager you pulled that thing out of
        the ocean."
    ps3 "What could be so important about an old tarnished box?"

    scene 37gladoffice

    glad "Obviously, it's not the box that holds my interest."
    glad "It is what is inside the box that I am after."
    glad "This was the ultimate goal when I started collecting."
    glad "And how fortuitous for you that you get to see it."
    glad "Very few ever have!"

    scene 38gladoffice with dissolve

    glad "Napoleon searched for it for many years."
    glad "I believe he found it."
    glad "He sent a small vessel to retrieve the item."
    glad "And though the mission was a success, the vessel sank on its return."

    scene 39gladoffice with dissolve

    glad "This, my dear, is the {b}true{/b} Holy Lance."
    glad "The spear that pierced--"

    ps3 "Bahaha!"

    scene 41gladoffice with dissolve

    glad "Wah--"
    glad "You... you laugh?"
    glad "Clearly you don't understand the significance of this."

    scene 40gladoffice

    ps3 "Ahaha!"

    scene 42gladoffice with dissolve

    ps3 "You actually think you've got the Spear of Destiny in that box?"
    ps3 "You're a hilarious ol' coot, you know that?"

    scene 40gladoffice with dissolve

    ps3 "Ahaha!"

    scene 45gladoffice

    glad "I've searched my whole life for this object!"
    glad "This is it!"
    glad "You just don't understand!"

    scene 42gladoffice

    ps3 "I can assure you that box does not contain the spear that pierced the side of Christ."
    ps3 "It's a fable, a fairy tale!"
    ps3 "It doesn't actually exist!"
    ps3 "You spent your whole life searching for a myth?!"
    ps3 "Oh, you poor, gullible fool!"

    scene 40gladoffice with dissolve

    ps3 "Ahaha!"

    scene 46gladoffice with dissolve

    stop music fadeout 1.0

    glad "You're a naive little girl!"
    glad "You have no idea what lengths I have gone to for this!"
    glad "Or how much time I have spent searching!"

    scene 44gladoffice with dissolve

    ps3 "You're a worm, Gladstone!"
    ps3 "A worm wriggling through the dirt in search of ancient junk!"
    ps3 "You've hurt people. Killed people!"
    ps3 "You abandoned your family for this fruitless crusade!"
    ps3 "You would burn the entire world as long as you got a fucking trophy from it!"

    scene 46gladoffice with dissolve

    glad "You don't know what you're talking about!"
    glad "I didn't abandon anyone!"
    glad "[player_name] and Leah were a mistake!"

    play sound "audio/dooropen.mp3"

    scene 47gladoffice with dissolve

    glad "... Lance?"

    scene 48gladoffice

    lance "I'm sorry."
    lance "I came as fast as I could."
    lance "She... she got the jump on us."

    scene 49gladoffice with dissolve

    lance "I gotta catch my breath."
    lance "My asshole hurts so bad right now."

    scene 50gladoffice with dissolve

    lance "I can't believe you tased me in the anus!"
    lance "I'm gonna kick your ass, bitch!"

    scene 51gladoffice with dissolve

    lance "YAAAH!!"

    glad "Lance, watch out for the--"

    scene 52gladoffice with dissolve

    lance "Wuoh!"

    scene 53gladoffice with dissolve

    play sound "audio/bodyfallmat.mp3"

    pause

    scene 56gladoffice with dissolve

    glad "... Banana peel."
    glad "I think he knocked himself out cold."

    scene 54gladoffice

    ps3 "See what you've done, Gladstone?"
    ps3 "This moment was supposed to be enjoyable for me."
    ps3 "You ruined it!"

    scene 55gladoffice with dissolve

    ps3 "Get your affairs in order."
    ps3 "Tomorrow I'm making sure you spend your final years in a cage."

    scene 56gladoffice

    play sound "audio/dooropen.mp3"

    glad "Damn that woman."

    scene 57gladoffice with dissolve

    pause

    scene 58gladoffice with dissolve

    pause

    scene 59gladoffice with dissolve

    pause

    scene 60gladoffice with dissolve

    glad "This is it."
    glad "It has to be..."

    ## Avalon visits her mom ##

    scene 1arsharol with fade

    play music "audio/natural.mp3"

    sg2 "Avalon should be here soon."
    sg2 "It's strange, she lived here her whole life but now that she lives somewhere else,"
    sg2 "I'm nervous about her comin' over."
    sg2 "I need a drink."

    scene 3arsharol

    r "I can getchya one if ya wan' but I gotta say, I sure do like ya better sober."

    scene 2arsharol with dissolve

    sg2 "Yeah, I know I can be a bitch when I drink."
    sg2 "It's just.. it takes the edge off."

    scene 3arsharol with dissolve

    r "Nah, I don't think yer a bitch when ya drink."
    r "I just don't want ya gettin' them beer goggles."
    r "I'm perdy enough already. How you gonna concentrate if I'm even prettier?"

    scene 4arsharol with dissolve

    r "I reckon you'd turn right inta a doe in heat, Lady!"
    r "Woohee!"
    r "You already done rode me too hard. My willy needs a break."

    scene 5arsharol

    sg2 "You're a fuckin' liar."
    sg2 "You're just tryin' to keep me sober by flattering me."
    sg2 "Alright, fine, you win."
    sg2 "This time."

    play sound "audio/doorknock.mp3"

    scene 6arsharol with dissolve

    r "'Ey! That's gotta be her!"
    r "Come on in, Ms. Avalon!"

    play sound "audio/dooropen.mp3"

    pause (.5)

    scene 7arsharol

    a3 "Hi, Mom."
    a3 "And hello again, Randall."
    a3 "I let myself in."
    a3 "Old habit, I'm sorry."

    scene 8arsharol

    sg2 "It's still your home, Avalon."
    sg2 "Even if you don't live here."
    sg2 "You're welcome to come and go."

    r "Maybe call first."
    r "I ain' always wearin' pants."

    scene 9arsharol

    a3 "I'll... try to remember that."
    a3 "It's nice to see you again, Randall."
    a3 "I'm sorry if I was a little shy the first time we met."

    scene 11arsharol with dissolve

    r "Oh here, let me get that for you!"

    a3 "O-oh, uhm, okay."

    scene 10arsharol with dissolve

    a3 "Thank you, Randall."
    a3 "That's awfully nice of you."

    r "Aw, it's no problem."
    r "My momma raised me ta be a gentleman!"

    scene 12arsharol with dissolve

    a3 "Well, it would seem she did a good job."
    a3 "The world needs more good people."

    r "Ain't that the truth."

    scene 13arsharol with dissolve

    r "That's why I'm glad I found yer momma."
    r "We bring out the best in each other."
    r "It's been a very rewardin' experience!"

    scene 14arsharol

    sg2 "Yes, it has been."
    sg2 "Randall reminds me of--"
    sg2 "Well, someone I used to know."

    scene 15arsharol with dissolve

    r "Sharol invited me over for some drinks a few days ago."
    r "We found we got a lot in common!"
    r "So I says to her 'How 'bout a date?'."
    r "An' to my surprise, she said 'Yes'."

    scene 16arsharol with dissolve

    r "Best first date I ever been on."
    r "Heck, best date I ever been on period!"
    r "Now I'm absolutely smitten with her."

    scene 17arsharol

    ai3 "{i}Wha.. what's going on?{/i}"
    ai3 "{i}She's acting so different with him around.{/i}"

    scene 18arsharol with dissolve

    ai3 "{i}She's happy now? With him?{/i}"
    ai3 "{i}And she found him... after I moved out?{/i}"

    scene 19arsharol with dissolve

    a3 "Mom..?"

    scene 20arsharol

    sg2 "Yeah?"
    sg2 "What is it, Avalon?"

    scene 21arsharol with dissolve

    a3 "Randall, I don't mean to be rude but would you mind if I spoke with my mother?"
    a3 "In private?"
    a3 "Just for a moment."

    scene 22arsharol with dissolve

    r "Sure!"
    r "Don't mind at all!"

    scene 23arsharol with dissolve

    r "I'mma go watch NASCAR on the tele."

    sg2 "Oh, okay."
    sg2 "You like NASCAR?"

    r "Yeah, I don' cheer for nobody."
    r "I just like to watch the cars go in a circle."
    r "They go so fast!"

    scene 22arsharol with dissolve

    r "I'll be right outside."
    r "Let me know if you need me!"

    scene 24arsharol with dissolve

    sg2 "What is it, Avalon?"
    sg2 "Is something wrong?"

    stop music fadeout 2.0

    scene 25arsharol

    a3 "N-no, I just..."
    a3 "The last time I was here, you were drunk and fighting with [player_name]."
    a3 "Now, you're..."
    a3 "You're like a different person."

    scene 34arsharol with dissolve

    play sound "audio/doorclose.mp3"

    a3 "Is it because of me?"
    a3 "Is it because I'm not here anymore that you're..."
    a3 "Happy?"

    scene 31arsharol

    sg2 "That's awfully dramatic, don't you think, Avalon?"
    sg2 "An no, that's not..."

    scene 35arsharol with dissolve

    sg2 "It's more complicated than that."
    sg2 "When your father died, it crushed me."
    sg2 "And ever since, when I look at you, I'm reminded of him and that he's never
        coming back to me."
    sg2 "So, yes, to some degree, when you're not around, it is a touch..."
    sg2 "Easier."

    scene 34arsharol

    a3 "I guess I understand."
    a3 "But Uncle [player_name] says I remind him of dad too."
    a3 "He also said that he loves that about me."
    a3 "Why... don't you?"
    a3 "Why was that such a negative for you?"

    scene 33arsharol

    sg2 "I don't know, Avalon."
    sg2 "We're very different people, [player_name] and I."
    sg2 "But look at you!"
    sg2 "It looks like you're doing well!"

    scene 26arsharol

    a3 "Yeah, I'm really happy right now."
    a3 "Everything is great."
    a3 "Uncle [player_name] and I are working really hard to help each other recover."
    a3 "And.. it's working!"
    a3 "We're both better when we're together."

    scene 31arsharol

    sg2 "Oh, that's great."
    sg2 "Maybe you should have lived with him instead of your own mother."
    sg2 "Sounds like you would have been happier then."

    scene 30arsharol

    a3 "Please don't twist this to make you the victim again."
    a3 "Can't you just be happy that I'm happy?"

    scene 35arsharol

    sg2 "Okay, you're right, I'm sorry."
    sg2 "I don't want to fight."

    scene 27arsharol with dissolve

    sg2 "H-how about, uhm, that money?"
    sg2 "That must make things easier, huh?"
    sg2 "I heard he took you shopping."

    scene 28arsharol

    a3 "The... money? No."
    a3 "Money has nothing to do with why we're together."
    a3 "We just make each other happy."

    scene 31arsharol

    stop music

    sg2 "Wait, what?!"
    sg2 "What do you mean together?"
    sg2 "Avalon, are you..?"
    sg2 "Are you sleeping with [player_name]?!"

    scene 32arsharol

    a3 "W-we haven't slept together but..."
    a3 "We're, uh, you know, dating."
    a3 "I-I thought you knew that."
    a3 "You said the other day you could tell we were--"

    scene 29arsharol

    sg1 "I was drunk!"
    sg1 "I was just being a bitch!"
    sg1 "What the fuck, Avalon!?"
    sg1 "Are you out of your fucking mind!?"
    sg1 "You can't date your Uncle!"

    scene 30arsharol

    a3 "You don't get to tell me what I can and can't do."
    a3 "[player_name] has been there for me and has supported me."

    scene 29arsharol

    sg1 "He's only acting like he's there for you, you naive little brat!"
    sg1 "So that he can fuck you!"
    sg1 "Are you really that blind!?"

    scene 36arsharol

    a3 "You spent my childhood at the bottom of a bottle!"
    a3 "You never loved me. The only thing you loved was pitying yourself!"
    a3 "[player_name] {b}actually{/b} loves me! He takes care of me! He supports me!"
    a3 "And I support him! We're partners!"
    a3 "So yeah, he can fuck me if he wants!"
    a3 "And I'm hoping that he does, too!"

    scene 37arsharol

    s "Only sick, disgusting freaks sleep with family members!"
    s "How did I give birth to a stupid little cunt like you!?"

    scene 31arsharol with dissolve

    sg2 "Er, I'm sorry, I--"

    play sound "audio/wood_movement.mp3"

    sg2 "Avalon."

    scene 38arsharol

    sg2 "Avalon, wait!"

    r "I heard shoutin'"
    r "Everythin' alright?"

    a3 "I was just leaving!"

    scene 39arsharol

    play sound "audio/doorclose.mp3"

    sg2 "Goddammit."
    sg2 "Why do I do that?"
    sg2 "Why do I get so angry?"

    scene 40arsharol with dissolve

    r "What happened?"

    sg2 "She's in a relationship with her Uncle!"

    r "Oh, thas' crazy."
    r "She happy?"

    sg2 "Well, yeah, she said she's happy..."

    r "Come on, Shay."
    r "Let's get some fresh air and we'll talk about it."

    sg2 "Okay."

    ## AVALON CALLS PENNY THEN SIDE CHARACTER ##

    scene avcall with fade

    ai3 "{i}Okay, things with mom didn't go so well.{/i}"
    ai3 "{i}Maybe Penny will cheer me up.{/i}"
    ai3 "{i}I'd like to know what happened with Seth anyway.{/i}"
    ai3 "{i}Or, does he go by Tyler? Whatever his dumb name is.{/i}"

    a3 "Suzi."

    show suzi_ani

    play sound "audio/suzi/how_can_i_help_avalon.mp3"

    suzi "How can I help today, Avalon?"

    pause

    scene 11suziani

    a3 "Video call Penny, please."

    suzi "Calling Penny."

    "*Ring* *Ring*"

    scene 1pvcall

    ps3 "Hey, Girlfriend!"
    ps3 "How are you?"

    scene 3avcall

    a3 "Hi Penny!"
    a3 "I'm doing well."
    a3 "I like your beanie!"
    a3 "How are you today?"

    scene 2pvcall

    ps3 "I just got out of a meeting."
    ps3 "I'm not usually one to lose my composure."
    ps3 "But I did today."
    ps3 "I'm not too proud of myself right now."

    scene 2avcall

    a3 "That's alright, Penny."
    a3 "We all get frustrated sometimes and lose our cool."
    a3 "It's what makes us human!"
    a3 "I bet you'll do better next time."

    scene 1pvcall

    ps3 "You're a doll."
    ps3 "Thank you, Avalon."
    ps3 "I think I needed that today."

    if octavia == True:
        if monogamy == True:

            scene 3pvcall with dissolve

            ps3 "I know you're curious about what happened with Tyler."
            ps3 "I have an errand to run right now but I was hoping to take
                you up on the offer I made."
            ps3 "Would you like to go on a date with me tonight?"
            ps3 "We can talk about everything then."

            scene 5avcall

            a3 "U-uh, yeah, okay!"
            a3 "That sounds really nice!"
            a3 "Sure!"

            scene 3pvcall

            ps3 "Alright, tonight then!"
            ps3 "And wear something dashing."

            scene 3avcall

            a3 "I will!"
            a3 "Bye, Penny!"

            jump pquit

        else:

            scene 3pvcall with dissolve

            ps3 "I know you're curious about what happened with Tyler."
            ps3 "I'd love to discuss it with you in person."
            ps3 "There's actually a lot I'd like to talk to you about."
            ps3 "Would you like to go on a date with me tonight?"

            scene 5avcall

            a3 "U-uh, yeah, okay!"
            a3 "That sounds really nice!"
            a3 "Sure!"

            scene 3pvcall

            ps3 "Alright, tonight then!"
            ps3 "And wear something dashing."

            scene 3avcall

            a3 "I will!"
            a3 "Bye, Penny!"

            scene avcall

            ai3 "{i}Hmm.{/i}"
            ai3 "{i}A date with Penny tonight leaves [player_name] free.{/i}"
            ai3 "{i}It's the perfect opportunity for him to take Octavia out!{/i}"
            ai3 "{i}Let's see how she feels about the prospect.{/i}"

            a3 "Suzi, video call Octavia."

            suzi "Calling Octavia."

            "*Ring* *Ring*"

            scene 1ovcall

            play music "audio/tomorrows_rain.mp3"

            o2 "Hi, Avalon!"
            o2 "It's so nice to see you!"
            o2 "How are you today?"

            scene 2avcall

            a3 "I'm doing well!"
            a3 "Aw, is that Maize?"
            a3 "Hi, Maize!"

            scene 2ovcall

            o2 "We were spending some time together on her couch."
            o2 "She's been really affectionate lately."
            o2 "We've had quite a wonderful cuddle session today, haven't we?"

            scene 4avcall

            a3 "Octavia, I was wondering if you had plans tonight?"
            a3 "Penny and I are going out to discuss some things and I was hoping that
                maybe you could go on a date with [player_name]?"
            a3 "Him and I were talking about the possibility of... expanding our relationship."
            a3 "To include you."
            a3 "If, of course, you're interested?"

            scene 3ovcall

            o2 "Oh. That is a rather unusual proposal, Avalon."
            o2 "Especially given your relationship with [player_name] is just beginning."
            o2 "Are you sure this isn't moving too fast?"
            o2 "A polygamous relationship can be very emotionally tangled."

            scene 5avcall

            a3 "I-I know, I just..."
            a3 "Well, the thing is..."

            scene 2avcall with dissolve

            a3 "I've really started to fall for you, Octavia."
            a3 "I don't want to have to choose one or the other."
            a3 "I want... both of you."

            scene 6avcall with dissolve

            a3 "And, also, I'm having trouble taking care of [player_name]."
            a3 "I really want to but I keep having anxiety attacks."
            a3 "I really want him to have a release so I was hoping that, maybe,
                you could... you know, take care of him tonight?"

            scene 3ovcall

            o2 "That's really not a fair thing for you to ask of me, Avalon."
            o2 "I can't say 'Yes' to that."
            o2 "But I won't say 'No' either."
            o2 "We'll see how the night goes, alright?"

            scene 4ovcall with dissolve

            o2 "I've grown quite fond of you, Avalon."
            o2 "I'm intrigued by this idea but I'm also worried how it might affect you."
            o2 "The most important thing to me is that you're happy."
            o2 "So if anything happens that makes you uncomfortable, we'll stop immediately."
            o2 "Does that sound fair?"

            scene 5avcall

            a3 "Yes! That sounds amazing!"
            a3 "Thank you so much, Octavia!"
            a3 "You have no idea how much it means to me that you said 'Yes'!"
            a3 "I lov--"

            scene 6avcall with dissolve

            a3 "Er, I mean, I really like you."

            scene 5avcall with dissolve

            a3 "Anyway, I'll go tell [player_name] you'll be here tonight!"

            scene 4ovcall

            o2 "Okay, Sweetie."
            o2 "Bye for now."

            scene avcall

            a3 "Yes, yes, yes, yes, yes!"

            stop music fadeout 1.0

            jump pre_date

    else:
        if monogamy == True:

            ps3 "I know you're curious about what happened with Tyler."
            ps3 "I would prefer to discuss the details in person."
            ps3 "I also have other things I'd like to talk with you about."
            ps3 "Would you like to go on a date with me tonight?"
            ps3 "We can talk about everything then."

            scene 5avcall

            a3 "U-uh, yeah, okay!"
            a3 "That sounds really nice!"
            a3 "Sure!"

            scene 3pvcall

            ps3 "Also, I went over to Dallas's place earlier to talk to her about the
                salon she showed interest in."
            ps3 "I'm about to head over to her house to pick her up."
            ps3 "I'm going to take her over to see the salon."
            ps3 "Would you like to join us?"

            scene 5avcall

            a3 "Yes!"
            a3 "I'd love to!"
            a3 "I'll head right over!"

            scene 1pvcall

            ps3 "Great."
            ps3 "Please give her a call and let her know I'm coming."
            ps3 "I'll see you soon."
            ps3 "Farewell for now."

            scene avcall

            ai3 "{i}Wow, this day just keeps getting better!{/i}"
            ai3 "{i}Well, except for my time with mom...{/i}"
            ai3 "{i}Let's give Dallas a call!{/i}"

            a3 "Suzi, video call Dallas."

            suzi "Calling Dallas."

            "*Ring* *Ring*"

            scene 1dvcall

            d "Hey, girl!"
            d "What's the haps?"

            scene 4avcall

            a3 "Mm, hey, Dallas."
            a3 "Why do you look so brown?"

            scene 2dvcall

            d "I look hot, right?"
            d "I cranked up the color saturation on my phone."
            d "I look like Cleopatra!"

            a3 "You look like a hotdog."

            d "Jealousy does not become you, Avalon."

            scene 1dvcall with dissolve

            d "Whatchya want girl?"

            scene 3avcall

            a3 "Penny is going to be coming by your place soon."
            a3 "I'm coming too."
            a3 "We're going to go visit the salon!"

            scene 1dvcall

            d "Really!?"
            d "That's awesome!"
            d "Hurry on over and I'll put on some pants."

            scene 4avcall

            a3 "Dallas."
            a3 "Why are you not wearing pants?"

            scene 4dvcall

            d "I got a little excited earlier."
            d "So I'm letting the vajayjay air dry."

            scene 1dvcall with dissolve

            d "Hurry over!"
            d "See you soon!"

            scene avcall

            "*Click*"

            ai3 "{i}She got excited earlier?{/i}"
            ai3 "{i}And Penny was over earlier..?{/i}"
            ai3 "{i}Nah, couldn't be what I'm thinking.{/i}"
            ai3 "{i}Time to head over to Dallas's house!{/i}"

            jump pdsalon

        else:
            ps3 "I know you're curious about what happened with Tyler."
            ps3 "I would prefer to discuss the details in person."
            ps3 "I also have other things I'd like to talk with you about."
            ps3 "Would you like to go on a date with me tonight?"
            ps3 "We can talk about everything then."

            scene 5avcall

            a3 "U-uh, yeah, okay!"
            a3 "That sounds really nice!"
            a3 "Sure!"

            scene 3pvcall

            ps3 "Also, I went over to Dallas's place early to talk to her about the
                salon she showed interest in."
            ps3 "I'm about to head over to her house to pick her up."
            ps3 "I'm going to take her over to see the salon."
            ps3 "Would you like to join us?"

            scene 5avcall

            a3 "Yes!"
            a3 "I'd love to!"
            a3 "I'll head right over!"

            scene 1pvcall

            ps3 "Great."
            ps3 "Please give her a call and let her know I'm coming."
            ps3 "I'll see you soon."
            ps3 "Farewell for now."

            scene avcall

            ai3 "{i}Wow, this day just keeps getting better!{/i}"
            ai3 "{i}Well, except for my time with mom...{/i}"
            ai3 "{i}Let's give Dallas a call!{/i}"

            a3 "Suzi, video call Dallas."

            suzi "Calling Dallas."

            "*Ring* *Ring*"

            scene 1dvcall

            play music "audio/disturbed_mind.mp3"

            d "Hey, sexy!"
            d "What's goin' on?"

            scene 4avcall

            a3 "Uhm, hey, Dallas."
            a3 "Did someone leave you in the oven too long?"
            a3 "You look like a burnt potato chip."

            scene 2dvcall

            d "I cranked up the color saturation on my phone."
            d "I look like an Arabian Goddess!"

            a3 "You look like an Arabian leather couch!"

            d "Maybe to you because you want to sit on my face."

            scene 5avcall

            a3 "Hey!"
            a3 "Don't get me worked up right now!"
            a3 "We've got stuff to do today."

            scene 4dvcall

            d "Yeah, like gingerly putting my tongue in your--"

            a3 "Stop!"

            scene 1dvcall with dissolve

            d "Okay, seriously, what do we have goin' on?"

            scene 6avcall

            a3 "Well, two things actually."

            scene 3avcall with dissolve

            a3 "First, I'm coming over and then Penny is going to pick us up."
            a3 "We're going to go see the Salon!"

            d "Fuckin' A!"

            scene 4avcall with dissolve

            a3 "And I was thinking you and [player_name] could go on a date tonight?"
            a3 "We talked about it and he's not opposed to the idea of you, you know,
                joining us."
            a3 "What do you think?"

            scene 3dvcall

            d "R-really?"
            d "He said yes?"
            d "I-- Yeah, of course, I'd like that."

            scene 6avcall

            a3 "I actually had a favor to ask."
            a3 "[player_name] and I are trying to be more intimate but my anxiety keeps
                getting in the way."
            a3 "I know he's probably really frustrated."
            a3 "So I was hoping, maybe you could.. you know, help him out?"

            d "Fuck. Yes."

            scene 2dvcall

            d "Listen, Ava."
            d "These are really big leaps we're taking and really fast."
            d "I think it's great because I'm sure we were all pretty lonely before this week."
            d "But I want you to know..."

            scene 4dvcall with dissolve

            d "I love you, girl."
            d "And if any of this gets uncomfortable for you, I want you to tell me."
            d "And we'll pump the brakes, yeah?"

            scene 2avcall

            a3 "Aw, thanks, Dallas."
            a3 "I love you too, Bestie!"
            a3 "I'll tell you if it starts to bother me but I really doubt it."
            a3 "I'm really excited!"

            scene 1dvcall

            d "Hurry over, girl!"
            d "Let's get this party started!"

            a3 "Okay! See you soon!"

            scene avcall

            stop music fadeout 2.0

            "*Click*"

            ai3 "{i}This is so great!{/i}"
            ai3 "{i}Dallas was really happy!{/i}"
            ai3 "{i}I love seeing her like that.{/i}"
            ai3 "{i}Alright, let's get ready to go!{/i}"

            jump pdsalon

    ## PENNY QUITS HER JOB FOR OCTAVIA ##

    label pquit:


            scene 1pquit with fade

            play sound "audio/doorbell.mp3"

            pause

            play music "audio/tomorrows_rain.mp3"

            scene 2pquit with dissolve

            o2 "Coming!"

            scene 3pquit with dissolve

            ps3 "I quit."

            scene 4pquit

            o2 "Oh!"

            scene 5pquit with dissolve

            o2 "You scared me, you sneak!"
            o2 "I can't believe you got me so good."
            o2 "What did you say?"

            scene 6pquit

            ps3 "Octavia, there are two things that I cherish most in my life."
            ps3 "I love making fools of people that take advantage of or hurt others."
            ps3 "And... I love you."
            ps3 "But recently, it's become obvious that I love one far more than the other."
            ps3 "So I'm quitting."
            ps3 "I would rather be with you."

            scene 7pquit

            o2 "I see."
            o2 "You know, I used to worry about you."
            o2 "You would put on one of your cute little outfits and then go out to
                challenge some degenerate or criminal and..."
            o2 "I never knew if you were coming home, Penny."
            o2 "I didn't like that."
            o2 "Even still, it's not fair of me to ask you to quit."

            scene 8pquit

            ps3 "Oh please, Octavia."
            ps3 "You know me too well to play that card."
            ps3 "I don't care about fair. In fact, I find it boring."
            ps3 "I can find another job to be fond of."

            scene 10pquit with dissolve

            ps3 "But I can't find another you."
            ps3 "You're the only star in my sky."
            ps3 "Everything else is just dust in my eye."

            scene 11pquit

            o2 "Stop it. You know I can't resist poetry."
            o2 "Even when it's coming from you and it's awful."

            scene 9pquit with dissolve

            o2 "I would prefer to think this over, Penny."
            o2 "I don't want to make any brash decisions."

            stop music fadeout 2.0

            o2 "It's something to be carefully considered."

            scene 10pquit

            ps3 "Yeah, yeah."
            ps3 "I know you like to consider every variable."

            scene 12pquit with dissolve

            play music "audio/sneaking_up_on_you.mp3"

            ps3 "But I can already tell you're going to--"

            scene 13pquit with dissolve

            ps3 "Eh?"

            scene 14pquit with dissolve

            ps3 "Well, well."
            ps3 "If it isn't my old nemesis."
            ps3 "The purrfect assassin who cannot be wavered in her duty."
            ps3 "Not even by catnip!"

            scene 15pquit

            ps3 "You may have won our last battle, Cat."
            ps3 "But my powers have grown threefold since we last met!"
            ps3 "Today, I'm gonna bury you in your own kitty litter!"

            scene 16pquit

            ps3 "YAAHH!!"

            scene 17pquit

            o2 "Penny, I'm glad you get to see Maize again."
            o2 "And it looks like she's glad to see you too."
            o2 "But I have an appointment I must get to."

            scene 18pquit

            ps3 "She's..!"
            ps3 "She's got the upper hand, Octavia!"
            ps3 "Her only weakness is water!"
            ps3 "Quick! Fetch me the spray bottle!"

            ps3 "Oh gross, Maize! Come on!"
            ps3 "You've got your anus right in my face!"
            ps3 "Move your fat butt!"

            scene 19pquit

            ps3 "Uh oh, Maize."
            ps3 "You got your tail too close to my mouth."
            ps3 "I'm gonna bite it!"
            ps3 "I'm gonna..!"
            ps3 "OMN!"

            scene 20pquit

            ps3 "Yum!"
            ps3 "Panther tail!"
            ps3 "Thas' wha' you ge', Maize!"

            scene 17pquit

            stop music fadeout 2.0

            o2 "Penny will be back, Maize."
            o2 "We have to say 'Goodbye' for now."

            scene 21pquit

            ps3 "Okay, truce, Maize!"
            ps3 "Truce!"
            ps3 "You won the battle today but the war is far from over!"

            scene 22pquit with dissolve

            ps3 "I'm glad I got to see you today."
            ps3 "I've missed you. A lot!"
            ps3 "I'll be back soon."

            scene 24pquit

            ps3 "I love you!"
            ps3 "Bye for now, Maize."
            ps3 "And remember to stay a-Maize-ing!"

            scene 25pquit with dissolve

            play music "audio/touching_moment.mp3"

            ps3 "Oh! Wha--"
            ps3 "What are you doing?"

            scene 26pquit with dissolve

            o2 "You were right."

            scene 28pquit with dissolve

            ps3 "You'll have to be more specific."
            ps3 "I'm right about a lot of things."

            scene 29pquit with dissolve

            o2 "Here."
            o2 "Let me show you."

            scene 30pquit with dissolve

            o2 "Ohmm"

            ps3 "Mm, mhmm."

            scene 29pquit with dissolve

            ps3 "I think I understand what I was right about."
            ps3 "I could use one more hint though."

            scene 30pquit with dissolve

            ps3 "Mm"

            o2 "Mhmm?"

            ps3 "Mhmm."

            scene 29pquit with dissolve

            o2 "Understand now?"

            ps3 "Indeed I do!"

            o2 "Okay, I really have to go."
            o2 "Stop by tonight."

            ps3 "If you insist. Sure."

            scene 30pquit with dissolve

            o2 "Mm!"

            scene 29pquit with dissolve

            o2 "Ok, stop, I really have to go."

            ps3 "You're the one that keeps kissing me!"

            stop music fadeout 1.0

            jump pre_date

    ## PENNY, DALLAS AND AVALON VISIT THE SALON ##

    label pdsalon:

        scene 1pdsalon with fade

        play music "audio/disturbed_mind.mp3"

        d "I'm nervous!"
        d "This is thrilling!"

        a3 "Yeah, I'm psyched!"

        scene 2pdsalon with dissolve

        d "Hey now, look at this place!"
        d "It's not at all what I expected!"

        ps3 "What did you expect?"

        d "I don't know! I guess I thought it would be run down and dirty."

        scene 3pdsalon with dissolve

        d "Holy Moley, freakin' crap! This is {b}awesome{/b}!"
        d "Avalon, look at this place!"

        a3 "I see it. It's incredible!"

        ps3 "I'm glad you like it!"

        scene 4pdsalon with dissolve

        d "There's so much potential here!"

        scene 5pdsalon with dissolve

        d "And it's in a really busy part of town."
        d "We'll be gettin' customers without even trying!"

        a3 "That's true!"

        scene 6pdsalon with dissolve

        d "Hmm."

        scene 7pdsalon with dissolve

        d "Would you like to have a seat, Customer Avalon?"

        a3 "Oh why thank you, Stylist Dallas!"

        scene 8pdsalon

        d "Lovely weather today, isn't it, Customer Avalon?"

        a3 "Except for that bothersome humidity!"
        a3 "It's going to frizz my pretty locks."

        scene 9pdsalon

        a3 "Now Stylist Dallas, I just want a little off the sides."

        d "Of course, Customer Avalon!"

        a3 "And be sure the sides are even."
        a3 "Don't get lazy on me, Stylist Dallas!"

        d "Of course not, Customer Avalon!"

        scene 10pdsalon

        a3 "I have my idiot husband's credit card today so I'll take the works!"
        a3 "Shampoo, Conditioning, Pedicure and Manicure!"

        a3 "And take your time, Darling."
        a3 "There's no rush for me to get back home to that dolt."

        show snip with dissolve

        d "Snip, snip, snip, snip."
        d "A little cut here."
        a3 "A little cut there."

        scene 13pdsalon with dissolve

        a3 "Ahaha!"
        d "Hahaha!"

        scene 14pdsalon with dissolve

        a3 "Hm?"
        a3 "What is it, Dallas?"

        stop music fadeout 2.0

        scene 15pdsalon

        d "Um."
        d "Hang on just a second, Avalon."
        d "I'll be right back."

        scene 16pdsalon with dissolve

        ps3 "Oh, yep, here it comes."
        ps3 "The 'Thank you' hug."
        ps3 "Alright, bring it in, Dallas."

        play music "audio/cause.mp3"

        scene 17pdsalon with vpunch

        ps3 "Oof!"
        ps3 "You're the affectionate type, aren't you?"
        ps3 "Well, at least you're gentle."

        scene 18pdsalon with dissolve

        d "Thank you, Penny."
        d "This is the nicest thing anyone has ever done for me."
        d "It's going to change my whole life."
        d "I..."

        scene 19pdsalon with dissolve

        ps3 "You're welcome."
        ps3 "Uhh, why are you looking at my lips?"
        ps3 "You're not going to--"

        scene 20pdsalon

        ps3 "Mm!"

        scene 21pdsalon with dissolve

        ps3 "Wow!"
        ps3 "You just went for it!"

        d "I--"
        d "I shouldn't have done that."
        d "I was just... excited."

        ps3 "I kind of liked it."
        ps3 "I'll have to give you a reason to thank me more often."

        scene 22pdsalon

        a3 "Things are heating up a little bit in here."
        a3 "Should I wait outside?"

        if monogamy == True:
            scene 23pdsalon

            d "Oh, Avalon."
            d "I kind of forgot you were there."

            ps3 "You really tunnel-visioned in on me, huh?"

            d "A little bit..."

            scene 24pdsalon with dissolve

            ps3 "Remember, Dallas."
            ps3 "This isn't completely free."
            ps3 "I'll need your assistance from time to time."
            ps3 "And you'll have to purchase all the tools, uniforms and equipment
                for this place."

            scene 27pdsalon with dissolve

            ps3 "Which I assume you will contribute, Avalon?"

            a3 "Of course!"

            ps3 "Also, this won't be available for some time."
            ps3 "There are still documents to sign and certain favors to request."
            ps3 "So you'll take care of Dallas until we can open this place."

            scene 26pdsalon

            a3 "Yeah! Dallas and I can iron out the details but no problem!"
            a3 "Anything to help!"

            scene 27pdsalon

            ps3 "Alright, I've got to head home to get ready for our date tonight."
            ps3 "Remember to wear something fabulous!"

            scene 25pdsalon

            d "Oh, you guys have a date tonight?"
            d "That sounds nice."
            d "How do I sign up for one of those with you, Penny?"

            scene 24pdsalon

            ps3 "After that kiss earlier, I was tempted to ask you!"
            ps3 "But one date at a time, Dallas."
            ps3 "I'll call you to set something up later."

            d "Awesome!"

            ps3 "Now let's get moving, girls."

            stop music fadeout 1.0

            jump pre_date

        else:

            d "Oh, Avalon!"
            d "I'm so sorry, I shouldn't have done that."

            a3 "Actually, I really don't mind."
            a3 "That was cute!"

            scene 23pdsalon

            d "Oh, uhh, alright."

            ps3 "I believe Avalon has developed an interest in voyeurism."
            ps3 "She likes to watch other people play."
            ps3 "It's not as uncommon as you might think."

            scene 26pdsalon with dissolve

            a3 "Oh? I hadn't heard that term before."
            a3 "But I do kind of like to watch other people."
            a3 "I think it takes the stress off of me if I'm not directly involved so I
                can just enjoy from the sidelines."
            a3 "If that makes sense?"

            scene 27pdsalon with dissolve

            ps3 "I hope you didn't misunderstand."
            ps3 "There's absolutely nothing wrong with it."
            ps3 "I was just making an observation."
            ps3 "But back onto the subject of the salon."

            scene 24pdsalon with dissolve

            ps3 "Remember, Dallas."
            ps3 "This isn't completely free."
            ps3 "I'll need your assistance from time to time."
            ps3 "And you'll have to purchase all the tools, uniforms and equipment
                for this place."

            scene 27pdsalon with dissolve

            ps3 "Which I assume you will contribute, Avalon?"

            a3 "Of course!"

            ps3 "Also, this won't be available for some time."
            ps3 "There are still documents to sign and certain favors to request."
            ps3 "So you'll take care of Dallas until you can open this place."

            scene 26pdsalon

            a3 "Yeah! Dallas and I can iron out the details but no problem!"
            a3 "Anything to help!"

            scene 27pdsalon

            ps3 "Alright, I've got to head home to get ready for our date tonight."
            ps3 "Remember to wear something fabulous!"

            scene 25pdsalon

            d "And I have to get ready too!"
            d "Tonight is going to be great."

            scene 26pdsalon with dissolve

            a3 "Dallas is taking [player_name] out on a date while we go out on ours!"

            scene 27pdsalon

            ps3 "Typical voyeur. She likes to watch her partner with someone else."
            ps3 "You're kinky as hell, Avalon."
            ps3 "I like it!"

            scene 24pdsalon with dissolve

            ps3 "Plans are in motion, girls!"
            ps3 "Let's blow this popsicle stand!"

            stop music fadeout 1.0

            jump pre_date

 ## AVALON AND BYRON PREPARE FOR THEIR RESPECTIVE DATES ##
 ## OR BYRON PREPARES TO STAY HOME ALONE AND WANK OFF LIKE AN APE ##
 ## YOU KNOW, IF YOU'RE ON THE MONO PATH ##

    label pre_date:
        if monogamy == True:
            scene 19abpredate with fade

            b "Avalon, are you ready for your--"

            scene 20abpredate with dissolve

            b "Damn!"

            scene 7abpredate

            play music "audio/one_step_closer.mp3"

            a3 "Do you like it?"
            a3 "I wasn't sure about the hairstyle."

            scene 19abpredate

            b "Avalon, you look incredible."
            b "Sophisticated yet still sultry."
            b "You went all out for this, didn't you?"
            b "Actually, I wanted to ask you..."
            b "What kind of date is this, anyway?"
            b "Like a girl's night kind of date or...?"

            scene 7abpredate

            a3 "It's just a friendly outing, [player_name]."
            a3 "Nothing to worry about."
            a3 "I promise!"
            a3 "What are you going to do while I'm out?"

            scene 19abpredate

            b "I've got some exercise equipment in the office."
            b "When you get back, I should be sufficiently sweaty and stinky."
            b "Just something for you to look forward to."

            a3 "Yuck, Uncle!"

            play sound "audio/doorbell.mp3"

            "*Ding Dong*"

            scene 21abpredate with dissolve

            b "That must be Penny."
            b "I'll go let her in."

            scene 22abpredate

            play sound "audio/doorclose.mp3"

            b "Penny, it's nice to see you."
            b "You look... you look..."
            b "Unusual?"

            p3 "Thanks?"
            p3 "These are my colors, [player_name]."

            b "Ooh, because... Penny."
            b "Copper."

            p3 "Lightbulb."

            scene 23abpredate

            a3 "Oh wow, Penny!"
            a3 "You look perfect!"

            p3 "See? She gets it."

            a3 "And the little key earring is darling!"
            a3 "I wish I could be so unique!"

            scene 24abpredate

            p3 "Believe me, Avalon, you're plenty unique."
            p3 "That's why I'm so drawn to you."

            a3 "Aw, thank you."

            b "Yes, very unique!"
            b "Except for those boots."
            b "I've seen those somewhere before."

            scene 25abpredate

            a3 "Oh Penny, I'm so delighted that you're taking me out tonight!"
            a3 "Thank you so much!"
            a3 "I haven't been on a girl date in forever!"
            a3 "We're going to have so much fun!"

            scene 14abpredate with dissolve

            p3 "I'm pretty thrilled myself!"
            p3 "I'm taking you someplace rather special, too."
            p3 "You'll love it, I'm sure."

            a3 "Okay!"

            scene 15abpredate with dissolve

            a3 "We'll be back in a few hours, Uncle!"

            b "Keep her safe, Penny."

            p3 "I assure you, she's in good hands."

            a3 "Bye, [player_name]!"

            scene 16abpredate with dissolve

            p3 "It's about a half-hour trip to get there."
            p3 "Do you like jazz?"

            scene 17abpredate with dissolve

            a3 "Sure!"
            a3 "That's music with a saxophone, right?"

            p3 "You're adorable."

            scene 26abpredate

            play sound "audio/doorclose.mp3"

            bi "{i}Avalon looked so happy to be going on a date.{/i}"
            bi "{i}With friends like these, I think she's going to be just fine.{/i}"
            bi "{i}And with her back in my life, maybe I'll be just fine too.{/i}"
            bi "{i}My Avalon.{/i}"

            stop music fadeout 1.0

            jump penny_date

        else:

            scene 1abpredate with fade

            b "Avalon, this suit is..."
            b "Ugh, I think it's too tight!"
            b "I haven't worn it in years."
            b "I look stupid!"

            a3 "Er, I wasn't going to say anything unless you noticed but..."
            a3 "You do have kind of a dumbfounded look on your face all the time."

            b "No, I mean because of the suit."

            scene 2abpredate with dissolve

            b "Oh, I see what you did there!"
            b "You're saying I look dumb all the time!"

            scene 3abpredate with dissolve

            b "Very clever, Missy!"
            b "You're lucky you're so darn cute or else I'd--"

            scene 4abpredate with dissolve

            b "Wow! Avalon, you look... wow!"

            scene 5abpredate with dissolve

            play music "audio/one_step_closer.mp3"

            scene 5abpredate

            a3 "Thank you, Uncle."
            a3 "You don't think it's too much?"

            scene 6abpredate

            b "No way!"
            b "You look magnificent."
            b "Compared to you, everyone else is going to look like they're in rags!"
            b "What kind of date is this you're going on with Penny, anyway?"
            b "You taking on another lover, my insatiable Avalon?"

            scene 7abpredate

            a3 "No!"
            a3 "I don't know!"
            a3 "I didn't really think to ask what kind of date it was..."
            a3 "It's probably just a friendly girl date."

            scene 6abpredate

            b "Remember, never put out on the first date."
            b "You don't want her to think you're easy!"

            a3 "What!? You're crazy!"

            play sound "audio/doorbell.mp3"

            scene 8abpredate with dissolve

            b "Oh, that must be her!"
            b "I'll go let her in."

            scene 9abpredate with fadefast

            b "You really went with that outfit?"
            b "That was a conscious decision?"

            p3 "You're such a handsome Prince until you start flappin'
                those gums and lose all appeal."

            b "Is that a key hanging from your ear?"
            b "You know those are for opening locked things, right?"

            p3 "It's metaphorical and beyond your comprehension."

            b "What's metaph--"

            scene 13abpredate

            a3 "Oh! Penny!"
            a3 "You look perfect!"
            a3 "You're so pretty!"

            scene 10abpredate

            b "Are we looking at the same person?"

            p3 "You're sweet, Avalon."
            p3 "But look at you."
            p3 "I get to go on a date with a fairy tale Princess today, don't I?"

            scene 11abpredate

            a3 "This is going to be so much fun!"
            a3 "I can hardly contain myself!"

            scene 12abpredate

            p3 "Yeah it is!"
            p3 "I haven't been on a date in a year!"
            p3 "I'm similarly overjoyed."

            scene 14abpredate with dissolve

            a3 "Oh, I never even asked where we're going!"
            a3 "A restaurant?"

            p3 "Not exactly but you'll love it."
            p3 "Trust me."

            a3 "Okay!"

            scene 15abpredate with dissolve

            p3 "We'll be back in a few hours, [player_name]"

            b "Keep her safe, Penny."

            p3 "You know I will."

            a3 "Enjoy your date, too, Uncle!"

            b "Bye, girls."

            scene 16abpredate with dissolve

            p3 "It's about a half-hour drive to get there."
            p3 "Do you like funk?"

            scene 17abpredate with dissolve

            a3 "Yeah, it's groovy!"
            a3 "Or.. you know, yeah. It's good. I like it!"

            p3 "You're adorable."

            scene 18abpredate with dissolve

            bi "{i}Avalon looked overjoyed to be going on a date with Penny.{/i}"
            bi "{i}At first, I thought Penny might be a total nutcase.{/i}"
            bi "{i}But seeing her tonight with Avalon, maybe there's more to her than I thought.{/i}"
            bi "{i}With support like this, I think Avalon is going to be just fine.{/i}"

            stop music fadeout 1.0

            jump penny_date

    label penny_date:

    scene 1apdate with fade

    a3 "You brought me to a museum?"
    a3 "For our date?"

    p3 "Yes."

    a3 "It seems unusual, doesn't it?"
    a3 "I mean, what are we--"

    scene 2apdate with dissolve

    a3 "Whoa!!"

    p3 "I thought that might catch your eye."
    p3 "Magnificent, isn't it?"

    a3 "It's so big!"

    scene 3apdate with dissolve

    a3 "I want to get closer!"

    p3 "Hey, slow down, Avalon!"
    p3 "It's not going anywhere."

    a3 "So cool!"

    scene 4apdate with dissolve

    a3 "Were they all this big!?"

    p3 "There were some even larger, actually."
    p3 "Would you slow your roll?"

    scene 5apdate with dissolve

    p3 "You're running in heels, you're going to fall."

    a3 "I won't!"

    p3 "There is literally no reason to run."
    p3 "You're being crazy."

    a3 "I'm not!"

    scene 6apdate with dissolve

    a3 "Wow!"
    a3 "This is incredible!"

    scene 7apdate with dissolve

    a3 "'I'm a monster, I eat things! Rawr!'"

    scene 8apdate with dissolve

    p3 "That is exactly how they used to talk."

    a3 "Look at those fangs! They're as big as my arms!"

    scene 10apdate with dissolve

    p3 "Do you like it?"

    a3 "I love it."
    a3 "It's like looking at a different world."
    a3 "I uhh, actually don't know much about dinosaurs."

    scene 8apdate with dissolve

    p3 "Well, this particular dinosaur was known as the king of the tyrant lizards."
    p3 "The Tyrannosaurus rex!"
    p3 "They had no natural predators. They were the top of the food chain during their reign."
    p3 "It took a veritable act of God to wipe them out."

    scene 9apdate with dissolve

    a3 "They were really powerful, huh?"
    a3 "This is really interesting but..."
    a3 "Is there a reason you decided to take me here?"

    scene 11apdate with dissolve

    p3 "I've been through a lot of hardships in my life, Avalon."
    p3 "I struggled for a long time to get on my feet."
    p3 "One day when I was much younger, I saw a dinosaur similar to this one and... I admired it."
    p3 "Nobody told them what to do, nobody bullied them. Because they were the strongest!"
    p3 "And that's what I wanted to be. I wanted to be the strongest!"
    p3 "So I started telling myself something every morning."

    a3 "What do you tell yourself?"

    scene 12apdate with dissolve

    p3 "I'm a Tyrannosaurus rex!"

    scene 13apdate with dissolve

    a3 "Penny, you're so silly!"

    p3 "It sounds funny, right?"
    p3 "Especially because I'm so small."

    scene 11apdate with dissolve

    p3 "It's the mindset that's important."
    p3 "The world out there is harsh and unforgiving. It's going to try to defeat you
        every chance it gets."
    p3 "It doesn't take mercy on anyone."

    scene 12apdate with dissolve

    p3 "So I wake up in the morning a fighter! Ready for battle!"
    p3 "I prepare both mentally and physically! I welcome challenges and I push boundaries!"
    p3 "Because you have to stand steadfast and push back against the world, or it'll take from you!"
    p3 "Don't ever let it take from you, not without a fight!"

    a3 "Wow, Penny. You're really intense tonight."

    scene 10apdate with dissolve

    a3 "I wish I could be like that."
    a3 "Confident and strong."
    a3 "Like a dinosaur."

    p3 "But you can be."

    scene 11apdate with dissolve

    a3 "You think so?"

    p3 "You're like a Raptor."
    p3 "I've seen how clever you can be."
    p3 "And you have your pack of close friends that support you."

    scene 14apdate with dissolve

    p3 "I know it's been rough for you over the years."
    p3 "Your dad passed when you were young and you had a rough upbringing."
    p3 "Life doesn't get easier, Avalon."
    p3 "But you're too incredible, the world needs more people like you."

    scene 12apdate with dissolve

    p3 "That's why you've got to wake up in the morning ready for war!"
    p3 "Tell yourself over and over again that you won't be defeated!"
    p3 "Not by people, not by trauma, not by despair!"
    p3 "Do whatever it takes to win the war, Avalon! No quarter!"

    a3 "O-okay."

    scene 10apdate with dissolve

    a3 "Be a Raptor?"

    p3 "Build your strengths; Be clever and rely on your friends."
    p3 "Fight, tooth and claw, for your happiness."
    p3 "Be a Raptor."

    a3 "Alright. I'll try."
    a3 "Thank you, Penny."

    p3 "Would you like to eat?"

    scene 15apdate with dissolve

    a3 "There's food?"
    a3 "I didn't even notice."

    p3 "You were too focused on the T-rex."

    scene 16apdate with dissolve

    a3 "Oh! Is that Ramen!?"
    a3 "I love Ramen! It's my favorite!"

    scene 17apdate with dissolve

    p3 "I know."
    p3 "Have a seat."

    a3 "Alright, thank you!"
    a3 "It looks delicious!"

    scene 18apdate

    p3 "Avalon, I know the main thing you probably want to know about is Tyler."
    p3 "Let me start by saying... it's taken care of."

    scene 26apdate with dissolve

    p3 "I know you would likely appreciate it if I regale you with a story about
        how I made him suffer and regret his actions."
    p3 "I didn't."

    scene 25apdate

    a3 "O-oh, no, I--"
    a3 "To be honest, Penny, I was against hiring you in the first place."
    a3 "I just wanted to move on with my life."
    a3 "I mean, people like that exist. We can't stop them all..."

    scene 20apdate

    p3 "I've put away quite a few, actually!"
    p3 "We might not be able to stop them all, you're right."
    p3 "But each one we do is a countless number of people they won't hurt in the
        future."

    scene 25apdate

    a3 "That's true. I guess I lost hope a little."
    a3 "That was a stupid thing for me to say."
    a3 "I'm sor--"

    scene 18apdate

    p3 "Don't apologize!"
    p3 "I understand what you mean."
    p3 "No matter how much good is in the world, there will always be the opposing force."

    scene 20apdate with dissolve

    p3 "Consider weeds, Avalon."
    p3 "You try to pull out as many as you can by the root. And the landscape
        looks better without them!"
    p3 "But they always come back."
    p3 "It's important to be diligent though, lest they overrun."

    scene 21apdate

    a3 "Here I thought you were a T-rex but it sounds like you're a Gardener."

    p3 "Ahaha."

    a3 "Well, I don't mind that you didn't make him suffer."
    a3 "I'm just glad he won't hurt anyone else."

    scene 18apdate

    p3 "You have an impressively positive mindset, Avalon."
    p3 "You push really hard to be optimistic and find the good in things."
    p3 "When I first met you, I expected you to be..."

    a3 "In pieces?"

    p3 "Most people in your situation would be."

    scene 21apdate

    a3 "What about you?"
    a3 "You know so much about me but I know almost nothing about you."
    a3 "You must be around my age right?"
    a3 "Where are your parents?"

    scene 20apdate

    p3 "I'm six years your senior, Avalon."
    p3 "And despite being an exceptional detective, I actually don't know where my parents are."
    p3 "I woke up one day when I was nine and they were gone."
    p3 "I have no idea what happened to them."

    scene 25apdate

    a3 "Oh my gosh!"
    a3 "That's awful."
    a3 "So you must have been adopted like [player_name]?"

    scene 18apdate

    p3 "There were no services set up like that where I was."
    p3 "I wandered around hungry for a while until I got desperate."
    p3 "I started scavenging, rummaging through garbage for food."
    p3 "Whatever I could scrape up to survive."

    scene 25apdate

    a3 "J-jeez. That's..."
    a3 "That's horrible!"
    a3 "How did you go from that to--"
    a3 "Er, you know..?"

    scene 20apdate

    p3 "I happened upon a group of kids like me."
    p3 "They'd formed a little group and found clever ways to get by."
    p3 "They accepted me into their group and taught me how to cook, how to hunt,
        how to steal."
    p3 "A lot happened between then and now. Most of us didn't make it but..."
    p3 "I did."

    scene 23apdate

    a3 "Damn. All that must have made you into one badass bitch."
    a3 "I mean, it's terrible!"
    a3 "But it turned you into... you know, {b}this{/b}!"
    a3 "And I think you're awesome."

    ps3 "Thanks!"

    scene 28apdate

    ben "Ms. Penny,"
    ben "I hope I'm not interrupting?"

    ps3 "Hello, Doctor."
    ps3 "No, not at all. Please come join us."

    scene 29apdate with dissolve

    ben "Hello, Ms..?"

    scene 30apdate

    a3 "O-oh, uhm, Avalon!"
    a3 "I'm Avalon."
    a3 "It's... nice to meet you."

    scene 29apdate

    ben "It's a pleasure to meet you."
    ben "Once again, I'm sorry to interrupt."

    scene 32apdate with dissolve

    ben "Penny, I want to say that..."
    ben "I did not appreciate being asked to do this."
    ben "It was extremely uncomfortable for me."
    ben "And... and... we're not--"

    scene 35apdate

    p3 "I apologize, Doctor Benson."
    p3 "I didn't mean to put you in a position that would make you feel that way."
    p3 "But you're helping to stop a criminal."
    p3 "You're a hero."

    scene 33apdate

    ben "I don't wish to be a hero, Penny."
    ben "I want to make sure I can go home to my children and my wife."

    p3 "Did you do what I asked?"

    ben "Y-yes."

    p3 "And?"

    ben "He believed the object was a fake."
    ben "As far as I could tell..."

    scene 35apdate

    p3 "Excellent."
    p3 "A lot of people don't get to go home to their children because of him."
    p3 "You've helped save lives today."
    p3 "Thank you."

    scene 36apdate

    ben "B-but Ms. Penny, it could be the genuine artifact!"
    ben "By my estimates, it was crafted around the correct time period."
    ben "It's a significant find!"

    scene 34apdate

    p3 "It's a hunk of rusted metal."
    p3 "It's just junk."
    p3 "It has no value whatsoever."
    p3 "Why are people so obsessed with it?"

    scene 36apdate

    ben "It's... a piece of history."
    ben "That spear is part of one of the most significant moments in human history."
    ben "How can you not understand--"

    scene 37apdate with dissolve

    p3 "Okay, okay."
    p3 "If it's important to you, then I'll bring it to you."

    ben "R-really!?"

    p3 "As an apology for making you do this, yes."
    p3 "But right now, I'm going to finish my dinner with my lovely date."

    ben "A-alright, yes. I apologize. And thank you again!"

    p3 "You're welcome, Doctor. Goodbye for now."

    scene 38apdate

    ai3 "{i}I wonder what that was about?{/i}"
    ai3 "{i}It sounded awfully important.{/i}"
    ai3 "{i}He said something about a... spear..?{/i}"

    scene 39apdate with dissolve

    p3 "I'm sorry about that Avalon."
    p3 "I expected that to be a much shorter conversation."

    a3 "That's alright."
    a3 "Can I ask what that was about?"

    scene 26apdate with dissolve

    p3 "Remember when I told you I lost my composure during a meeting earlier?"
    p3 "The meeting was with [player_name]'s father."

    scene 20apdate with dissolve

    p3 "I'm going to take his ass down but first,"
    p3 "I was going to play with his dumbass henchmen. Then he went and upset me."
    p3 "So I had Benson convince him that the artifact he'd found was a fake."
    p3 "Gladstone had been searching for it most of his life. His disappointment will be immeasurable."
    p3 "What can I say? I like to play with my food before I eat it."

    scene 19apdate

    a3 "Nice work!"
    a3 "You always seem so composed."
    a3 "How did he get you worked up?"

    scene 22apdate

    p3 "He abandoned his children to search for trash."
    p3 "I just can't fathom trading family for garbage."
    p3 "He's just the worst ki--"

    scene 25apdate

    a3 "Children!? Plural?!"
    a3 "[player_name] has a family that's still alive?!"
    a3 "Does.. does he know??"
    a3 "We have to tell him!"

    scene 24apdate

    p3 "You didn't know?"
    p3 "Shit."
    p3 "I'm always so careful about slip-ups like this."
    p3 "You really have a way of disarming me."

    scene 26apdate with dissolve

    p3 "Look, I'm sure [player_name] will tell you about Leah when he's ready."
    p3 "I didn't do a lot of digging so I'm not sure exactly how they're related."
    p3 "I recommend you don't bring it up to him. Let him bring it up to you."

    scene 25apdate

    a3 "A-alright. That's going to be really hard though."
    a3 "I can't believe he didn't tell me..."
    a3 "Leah..?"

    scene 20apdate

    p3 "I have made too many mistakes today."
    p3 "Let's enjoy our meal, it's going to get cold."

    scene 21apdate

    a3 "Oh, right!"
    a3 "I know you didn't mean to tell me but..."
    a3 "I'm glad you did."
    a3 "Anyway, yes! Let's eat!"

    jump mercenaries_faith

    label mercenaries_faith:

    scene 1mlrecover with fade

    merc "I can't believe you took a taser to the taint, Lance."
    merc "You sure you're alright?"

    lance "Fuck no!"
    lance "I tried to take a dump earlier. The pain was so bad, I literally passed out on the shitter."
    lance "All that vaseline didn't do nothin' either!"
    lance "Hopefully this movie will take my mind off the pain."
    lance "Thanks for gettin' it, man."

    scene 2mlrecover with dissolve

    merc "Yeah, it's about a prostitute that falls in love with some super-rich guy."
    merc "And they like, bang on a piano and stuff."
    merc "I figured we could make fun of it."

    lance "They bang on a piano?"
    lance "How do you know? You saw it before?"

    merc "Well, yeah, a few times."

    scene 3mlrecover with dissolve

    merc "I actually like this part. They don't let her shop in their store 'cause
        she's a hooker."

    lance "Fuck those bitches, man."

    merc "But she comes back later with like, a whole bunch of shit she bought
        somewhere else."
    merc "And she's all, 'You work on commission, don't you? Big mistake!'"

    scene 4mlrecover with dissolve

    merc "Ahaha."

    lance "That does sound pretty funny, man."
    lance "Haha."

    scene 5mlrecover with dissolve

    lance "Ow ow! Fuck!"
    lance "Don't make me laugh."
    lance "My anus tightens when I laugh."

    merc "Shit. I'm sorry, Lance."
    merc "You alright, buddy?"

    scene 6mlrecover with dissolve

    lance "Yeah. I can't believe she tased me in the anus but only drew a dick on your face."

    merc "Yeah, you got the worse punishment. For sure."

    lance "I might never be able to sit down again, man."

    play sound "audio/doorknock.mp3"

    "*Knock* *Knock*"

    scene 7mlrecover with dissolve

    lance "What the hell?"

    merc "Uhh, come in!"

    scene 8mlrecover

    play music "audio/black_mermaid.mp3"

    f "Hello, boys."
    f "A little birdie told me a couple mercenaries work here."

    scene 7mlrecover

    lance "A little bird?"

    merc "You talk to birds?"
    merc "Are you like, Snow White or somethin'?"

    scene 8mlrecover

    f "Do I look like fucking Snow White to you?"
    f "Are you two the guys I'm lookin' for or not?"

    lance "Technically I'm a freelancer and he's a mercenary."

    f "The fuck is the difference?"

    scene 6mlrecover

    merc "Actually, nothin' really."

    lance "We're both professionals for hire, so, yeah."
    lance "But we gotta differentiate ourselves so..."

    scene 7mlrecover with dissolve

    lance "Hey, nice tits, by the way."
    lance "Those things real?"
    lance "They look so firm, I bet I could bounce a quarter off of 'em."

    scene 6mlrecover with dissolve

    lance "Bitches love it when you compliment their tits."

    merc "Oh yeah?"

    scene 7mlrecover with dissolve

    merc "You got real nice funbags, Miss."

    lance "Nailed it, bro."

    scene 9mlrecover

    f "For fuck's sake..."

    scene 11mlrecover with dissolve

    f "You guys want to make some money, or not?"

    scene 6mlrecover

    lance "We could use the cash."
    lance "Ain't got paid in three weeks."

    scene 7mlrecover with dissolve

    merc "What's the job?"

    scene 11mlrecover

    f "It involves a certain little detective."
    f "And from the looks of ya, I think you guys have already met her."

    stop music fadeout 2.0

    if octavia == True:
        if monogamy == True:
            jump mono_night
        else:
            jump pre_date_byron
    else:
        if monogamy == True:
            jump mono_night
        else:
            jump pre_date_byron




    ## BYRON'S PRE DATE MEET UP ##

    label pre_date_byron:

    if octavia == True:

        scene 1prebdate with fade

        bi "{i}Octavia sure is taking a while.{/i}"
        bi "{i}I thought she would be here by now.{/i}"
        bi "{i}Then again, she's probably taking extra time to look nice for this.{/i}"
        bi "{i}I hope she doesn't expect too much. I have no idea what I'm doing!{/i}"

        play sound "audio/doorbell.mp3"

        scene 2prebdate with dissolve

        bi "{i}That must be her!{/i}"
        bi "{i}I wonder why I'm so nervous about this?{/i}"
        bi "{i}My heart feels like it's going to beat right out of my chest.{/i}"

        scene 3prebdate with dissolve

        b "C-come in!"

        bi "{i}Let's see if I can just get some of the wrinkles out of this suit.{/i}"

        play sound "audio/dooropen.mp3"

        bi "{i}That's about as good as it's going to get.{/i}"
        bi "{i}Okay, greet with a compliment!{/i}"

        scene 4prebdate with dissolve

        b "Hey, Octavia! You look--"

        scene 5prebdate with dissolve

        b "Dya!"

        scene 1preodate

        play music "audio/one_step_closer.mp3"

        o2 "Hi, [player_name]."
        o2 "Did the dress surprise you?"
        o2 "It is a little more daring than my normal attire, I suppose."

        scene 4prebdate

        b "I'm sorry, ma'am. You have the wrong house."
        b "Only mortal men reside here."
        b "None worthy of a Goddess such as yourself."

        scene 2preodate

        o2 "Oh [player_name], stop it!"
        o2 "You're making me blush!"

        scene 3preodate with dissolve

        o2 "I assume that means you like it?"
        o2 "It's not too much, is it?"

        scene 4preodate

        b "No, not at all."
        b "You look divine, Octavia."
        b "You're turning me into one heck of a lucky guy."

        scene 5preodate

        o2 "You look very dapper yourself, [player_name]."
        o2 "How fortunate am I to have such a handsome gentleman escort me out tonight?"
        o2 "Are you ready to go?"

        b "Sure!"

        scene 6preodate with dissolve

        b "Should I drive or..?"

        o2 "Actually, I'll drive."
        o2 "I hope you don't mind but I took the liberty of setting something up for us."

        b "Oh?"

        stop music fadeout 1.0

        jump octavia_date

    else:

        scene 1prebdate with fade

        bi "{i}I feel like Dallas should have been here by now.{/i}"
        bi "{i}I can't believe how nervous I am about this.{/i}"
        bi "{i}I wonder if she's nervous too?{/i}"
        bi "{i}Probably not, that girl is a rock!{/i}"

        play sound "audio/doorbell.mp3"

        scene 2prebdate with dissolve

        bi "{i}Finally!{/i}"
        bi "{i}I was getting worried she wasn't going to show!{/i}"

        scene 3prebdate with dissolve

        b "Come in!"

        play sound "audio/dooropen.mp3"

        bi "{i}Alright, play it cool, [player_name].{/i}"
        bi "{i}It's just a casual date, no big deal.{/i}"

        scene 4prebdate with dissolve

        play sound "audio/doorclose.mp3"

        b "Hey, Dallas! You're la--"

        scene 5prebdate with dissolve

        b "Gah!"

        scene 1preddate

        play music "audio/disturbed_mind.mp3"

        d "See something you like, Big Guy?"
        d "I know I'm late but I wanted to look great for tonight."
        d "How'd I do?"

        scene 4prebdate

        b "I uhh, I mean..."
        b "You look..."
        b "Damn."

        scene 2preddate

        d "Yeah, that's the look I was going for."
        d "This is the same dress I wore to prom."
        d "Do you think I look sexy, [player_name]?"

        scene 6prebdate

        b "Stop. Stop doing that."
        b "These pants are a size too small so they're really tight."
        b "You're going to rip them if you do that."

        scene 3preddate

        d "What?!"
        d "How would I rip them?"
        d "I'm way over here."

        scene 4preddate with dissolve

        d "Oh!"
        d "You mean because..."

        scene 5preddate with dissolve

        d "Ahaha."
        d "I get it, I get it."

        scene 6preddate with dissolve

        b "Are you ready to go?"

        d "Yep! But I'm choosing the place!"
        d "No buts!"

        b "Alright but you're going to miss out on some top tier Tacos!"

        scene 7preddate with dissolve

        d "Yeah, that's why I'm choosing the place."
        d "I had a feeling you'd pick something lame."

        b "I don't get out much."

        stop music fadeout 2.0

        d "Well, at least you look nice in a suit."
        d "Albeit, a wrinkly one that is two sizes too small..."

        jump dallas_date

    label dallas_date:

    play music "audio/cause.mp3"

    scene 8dbdate with fade

    d "Alright, so, I know this is a bit unusual."
    d "But just hear me out!"

    scene 1dbdate with dissolve

    d "This is the cafe that I worked at before it was seized by the government."
    d "I pretty much ran this side of it."
    d "The main office is actually the building next door."

    b "You brought me to... a cafe?"
    b "For our date?"

    scene 2dbdate with dissolve

    d "I know, I know!"
    d "It's weird!"
    d "And kind of lame."
    d "But..!"

    scene 3dbdate with dissolve

    d "I just thought, you know, this was the end of one chapter."
    d "And you are, maybe, the beginning of the next for me."
    d "Well, you and Avalon."

    b "Are we even allowed to be here?"

    scene 1dbdate with dissolve

    d "Yeah, I don't like asking for favors."
    d "In fact, I despise asking for favors!"
    d "But for this, I asked if Penny could help out."
    d "She made a few calls and voilà!"

    scene 5dbdate

    b "That sounds like Penny!"
    b "But choosing this place for our date seems kind of..."
    b "I would use the word 'Cheesy'."
    b "It seems unlike you."

    scene 3dbdate

    d "Oh yeah?"
    d "What would seem more like me?"

    b "A strip club?"

    scene 4dbdate with dissolve

    d "Seriously!?"
    d "That's how you see me!?"

    scene 7dbdate

    b "Uhh, sometimes I guess."
    b "I used to only see the wild and flirtatious side of you."
    b "Lately, I feel like I'm seeing a lot more sides."
    b "It's as if I'm looking behind the curtain right now."
    b "It's kind of nice, actually."

    scene 4dbdate

    d "I... well, I don't really know what to say."
    d "I mean, I guess we do get caught up in being playful."
    d "But yeah, I'm more than just a ditzy blonde."

    scene 6dbdate

    b "Ditzy blonde is never the way I would have described you."
    b "I always knew you were incredible."
    b "Now I just know that incredible was a tremendously understating term for you."

    scene 2dbdate

    d "S-stop."
    d "I... I don't know how to respond to compliments like that."
    d "It freaks me out."

    scene 5dbdate

    b "You're not used to getting genuine compliments?"
    b "If you're going to be spending time with me,"
    b "you better make peace with them."

    scene 3dbdate

    d "You're right, I'm not used to compliments like that."
    d "Most people comment on my tits or my ass."
    d "Even girls!"
    d "But... thank you, [player_name]."

    b "Can you show me what you used to do here?"

    scene 1dbdate with dissolve

    d "Uhh, sure."
    d "I mostly just made coffee."

    b "I'd be willing to bet there is more to it."

    d "Well, yeah, here."
    d "Follow me."

    scene 9dbdate with dissolve

    d "You can be the customer and I'll take your order."
    d "So just stand in front of the register as a customer would."

    b "Alright."

    scene 10dbdate with dissolve

    d "If I would have worn outfits like this, I bet my tips would have been a lot better!"

    scene 11dbdate with dissolve

    d "Oh, hello, sir!"
    d "What can I get for you today?"

    b "Oh we're really doing this?"
    b "Alright, uhm, what... where's the menu?"

    d "Look up."

    scene 12dbdate with dissolve

    b "Hmm..."
    b "A Snickeroo?"
    b "Campsite Mokah?"
    b "Is this place for hippies?"

    d "Nah, it's mostly millennials that we get in here."

    b "Okay, what's a Turtle Mokah?"

    scene 15dbdate with dissolve

    d "Great choice, sir!"
    d "That's our most popular coffee!"

    scene 16dbdate

    b "Wait, that's not what I want."
    b "I just want to know what it is?"

    d "It's just a coffee with chocolate in it."

    b "I don't want a chocolate coffee."

    scene 13dbdate

    d "Alright, then what the hell do you want, [player_name]?"

    b "I don't know."

    d "Then you're gettin' a Turtle Mokah!"

    scene 14dbdate

    stop music fadeout 2.0

    b "Shit, alright."
    b "You drive a hard sales pitch, Dallas."
    b "Give me your best Turtle Mokah then!"

    scene 15dbdate

    d "Right away, good sir!"

    play music "audio/aint_it_funny.mp3"

    scene 17dbdate with dissolve

    d "Brrrr, Schhhh, Kschkschksch."

    b "What the hell are you doing?"

    scene 18dbdate with dissolve

    d "I'm... making your coffee."
    d "Dumbass."

    b "You're not though!"
    b "You're just making weird noises with your face hole!"
    b "You don't even have a cup."

    d "It's just roleplay!"
    d "I'm not making you real coffee."

    scene 19dbdate with dissolve

    d "Here you are, sir!"
    d "One Turtle Mokah with extra chocolate!"
    d "That'll be eight dollars."

    b "No, I don't want fake coffee."
    b "I want a real one!"

    scene 20dbdate with dissolve

    d "They confiscated everything!"
    d "I don't have the stuff to make a real one!"

    b "But I'm real thirsty, not fake thirsty!"

    scene 21dbdate with dissolve

    d "[player_name], you're going to take this fake coffee."
    d "And you're going to drink it like it's real coffee."
    d "Do you understand?"

    scene 22dbdate with dissolve

    b "Alright, fine."
    b "Give it to me."

    d "Here you are, Sir!"
    d "Please enj--"

    scene 23dbdate with dissolve

    b "This is what I think about your fake coffee, Dallas."

    d "Did you just pour that all over my counter!?"

    b "The customer is always right."
    b "It's a hard lesson you're learning today, but an important one."

    scene 24dbdate with dissolve

    d "You son of a bitch!"
    d "I'm coming for you, [player_name]!"

    b "Are you threatening a paying customer?"
    b "What a terrible business model!"

    scene 25dbdate with dissolve

    d "You're goin' down, man!"
    d "You dick!"

    scene 26dbdate

    b "I'd like to see a manager."
    b "And file a formal complaint about the service."
    b "Or lack thereof, as it were."

    d "I am the manager, you ass--"

    stop music

    play sound "audio/clothrip.mp3"

    scene 27dbdate with dissolve

    d "Shit!"
    d "My dress!"

    b "Oh my God."
    b "Are you alright, Dallas?"
    b "Did it cut you?"

    scene 29dbdate

    d "No, I'm fine."
    d "Can you believe that's the third time I've gotten snagged on that latch?"

    b "Uhh, Dallas..."
    b "You're uhh, you're kind of exposed."

    scene 28dbdate with dissolve

    d "Huh?"
    d "Damn, it ripped my skirt right off."

    b "Do you want my jacket or something to cover up with..?"

    scene 29dbdate with dissolve

    d "Your jacket?"

    scene 30dbdate with dissolve

    play music "audio/disturbed_mind.mp3"

    d "Oh, are you nervous, [player_name]?"
    d "Do cute girls in their underwear make you a little shy?"
    d "You can look, if you want."

    scene 31dbdate

    b "Why don't I get you home so you can put something on?"
    b "We can reschedule and do the date another time."

    scene 32dbdate

    d "No!"
    d "I've been really looking forward to this date!"
    d "I'm not going to let a stupid wardrobe malfunction ruin this for me."

    scene 31dbdate

    b "You--"
    b "You were looking forward to this?"
    b "Really?"

    scene 30dbdate

    d "Yeah, I was."
    d "I'm pretty into you, if you haven't noticed, Dummy."

    scene 35dbdate

    b "When it comes to women, I'm not sure about anything."
    b "But if it's important to you, and you don't care about your... situation."
    b "Please, have a seat."

    scene 34dbdate

    d "Thank you, [player_name]."
    d "I mean, once I'm sitting down, you won't be able to see my underwear anyway..."

    scene 36dbdate with dissolve

    b "Yeah, except there are giant windows right next to us."
    b "So literally anyone could peek in and see you in your panties."

    d "Imagine how jealous they'll be of you?"

    scene 37dbdate with dissolve

    b "You mean because of how nice my suit is?"

    d "No, idiot, because of how hot your date is."

    b "Right!"

    scene 39dbdate with dissolve

    b "Hey, I probably shouldn't jump right to this but I've been rather curious."
    b "I'd like to know more about your parents."
    b "They just up and left you a few years ago?"

    scene 38dbdate

    d "You make it sound like they abandoned me."

    b "They didn't..?"

    d "It's not like that."
    d "My father's parents were Romani."
    d "They--"

    b "Wait, Romani?"

    scene 40dbdate with dissolve

    d "Yeah, Gypsies."
    d "My grandparents settled down in the states after they escaped Germany during World War 2."
    d "But my dad untraditionally went off on his own in his late twenties."
    d "He didn't live like a Romani. He wanted something else, I guess."
    d "Really though, he just became a freakin' hippie."

    scene 39dbdate

    b "He grew up in the seventies then?"
    b "And your mom was..?"

    d "From Switzerland."

    scene 41dbdate with dissolve

    b "That's a weird mix."
    b "What do they call you then? I mean, someone who is part Swiss, part Gypsy."
    b "Are you... are you a Switzi?"

    scene 46dbdate

    d "What the fuck, [player_name]?"
    d "No, I'm just a regular fucking person."
    d "What abomination of a portmanteau is that shit??"

    scene 43dbdate

    b "Damn, I struck a nerve there!"

    scene 45dbdate with dissolve

    b "I mean, the mix made for one hell of a gorgeous lady."
    b "I've just never heard of that specific mixture."
    b "But what the fuck do I know? I'm not a genealogist."

    scene 40dbdate

    d "Yeah, thanks. Anyway..!"

    scene 38dbdate with dissolve

    d "My parents were travelers."
    d "They didn't like to lay down roots."
    d "And they also didn't like authority."

    b "Stick it to the man!"

    scene 40dbdate with dissolve

    d "Quiet. Let me tell the damn story."

    b "My bad. Continue."

    scene 38dbdate with dissolve

    d "Well, they never enforced things. They always treated me like an adult."
    d "Even when I was a child, they pretty much let me do whatever I wanted."
    d "And I learned about consequences the hard way."
    d "When I turned fifteen, they said they wanted to hit the road."
    d "And... I didn't want to."

    scene 39dbdate

    b "I think I get it."
    b "It's not that they abandoned you, it's more that you left the nest earlier
        than most people."
    b "You're an independent person, kind of like me."
    b "Maybe that's why we get along."

    scene 38dbdate

    d "Yeah, our situations may be unique but the outcome was similar."
    d "We both became very independent people."

    scene 44dbdate with dissolve

    d "I'm... sorry I kicked you out of my place yesterday."

    b "Yeah, what was that about?"

    d "It's just that..."
    d "Nobody has ever said they were proud of me before."
    d "Or at least, not like that."
    d "You took care of me at the police station, you keep complimenting me genuinely and
        you even kind of said you love me."
    d "I just don't know how to react to that stuff."
    d "I think I'm falling for you and it's making me... scared."

    scene 45dbdate

    b "Aw come on, don't be such a drama queen."
    b "Are you messing with me right now?"
    b "Is this one of your little games?"

    scene 42dbdate

    d "W-what?"
    d "Why would you say that?"
    d "I'm like, pouring my heart out over here and--"

    scene 45dbdate

    b "I literally wake up most mornings now thinking about you."
    b "And I don't mean that I wake up thinking about that perfectly shaped ass of yours, although it
        is incredible."
    b "I mean {b}you{/b}!"

    scene 39dbdate with dissolve

    b "Every day that you're a part of, every day that I lay eyes on you..."
    b "Is a good day."
    b "I've never had a bad day when you were around."
    b "You're the single most fun person I've ever had the pleasure to be around."
    b "Of course I'd take care of you, I'd do anything for you."
    b "Because... you're worth it. Every ounce of energy, every dollar spent, you're worth
        it all."
    b "So you're damn right I love you."

    scene 42dbdate with dissolve

    d "Whoa."
    d "I didn't know you felt that way."
    d "That's... wow. Really?"
    d "That's fuckin' heavy, man."

    scene 43dbdate

    b "Shit."
    b "I shouldn't have said all that."
    b "That was too much."

    scene 38dbdate

    d "No, I liked it."
    d "I just didn't know you felt that way."
    d "I... love you too, actually..."

    scene 40dbdate with dissolve

    d "To be honest, I've had a crush on you since freshman year."

    scene 47dbdate

    b "What?! Seriou--"

    scene 48dbdate with dissolve

    b "Oops."

    d "Oh, come on!"

    scene 49dbdate with dissolve

    b "Huh?"

    d "You did that on purpose!"

    b "What are you talking about?"

    d "So when you bend down to pick it up, you can look at my panties under the table."
    d "That's so high school, man!"

    b "Dallas, it was just an accident."
    b "I can leave it on the ground if you prefer?"

    play sound "audio/wood_movement.mp3"

    pause (1)

    scene 50dbdate

    b "Dallas, what are you doing?"
    b "Why are you walking over here?"

    d "Just admit it, [player_name]."

    scene 51dbdate with dissolve

    b "W-what the hell?"

    scene 52dbdate with dissolve

    b "Seriously, Dallas, I knocked over the water on accident."

    d "Uh huh."

    scene 53dbdate with dissolve

    d "[player_name]?"

    b "Y-yeah?"

    d "Do you want to see my panties?"

    b "Nah, I'm good."

    d "[player_name]?"

    b "Hmm?"

    d "Do you want..."
    d "To see..."
    d "My panties?"

    b "Well, if you're going to twist my arm--"

    scene 55dbdate with dissolve

    b "Ah!"
    b "Lead me not into temptation for it shall find its way to me!"
    b "I can't look away! What kind of devil vagina magic is this?!"
    b "I knew I should have taken a baby aspirin this morning. My heart
        can't take this!"

    d "You done?"

    scene 54dbdate with dissolve

    b "Yeah, sorry."
    b "The jokes just sort of pour out of me when I get excited."

    d "You mean when you get nervous."

    b "Sometimes it's the same thing."

    scene 55dbdate with dissolve

    b "Seriously though, my God!"
    b "You look phenomenal!"
    b "But this can't be a good idea, Avalon would kill us both!"

    d "Actually..."

    scene 54dbdate with dissolve

    b "Huh?"

    d "Well, she kind of asked me to take care of you tonight."
    d "Like, sexually."

    b "Seriously!?"

    d "Yeah."

    scene 55dbdate with dissolve

    b "Well, maybe it's okay if I..."

    scene 56dbdate with dissolve

    d "Damn!"
    d "Your hands are huge!"

    b "Wow, your skin is soft and firm at the same time."
    b "Touching you is sensational."

    scene 57dbdate with dissolve

    d "Yeah, you're telling me."
    d "You could drown a man with the amount of moisture in my underwear right now."

    b "You're really that wet?"

    scene 58dbdate with dissolve

    b "Wow, you are!"

    d "Whoa, fuck!"
    d "Stop stop!"

    scene 59dbdate with dissolve

    b "Shit, sorry."
    b "You tempt the hell out of me then yell at me when I go for it?"
    b "You dirty tease!"

    d "No!"
    d "I mean..!"
    d "Stop, like, long enough to take me back to your place."

    b "Ooh."
    b "Alright, yeah, let's get out of here."

    stop music fadeout 2.0

    jump dallas_sex

label dallas_sex:
    if _in_replay:
        $ player_name = renpy.input("What would you like to name the MC?")
        if player_name.strip() == "":
          $ player_name = "Byron"

    scene 1dbpostdate with fade

    b "I mean, come on, Dallas."
    b "We don't have to jump into anything right away."
    b "We can just hang out for a while, right?"

    d "Nope!"

    scene 2dbpostdate with dissolve

    d "Rawr!"

    b "What the crap!?"
    b "Take it easy, Dallas!"

    scene 3dbpostdate with dissolve

    b "Oof."

    d "I don't want to take it easy, [player_name]."
    d "I want to take it hard. Really. Really. Hard."

    b "That's the worst innuendo I've ever heard."
    b "It's too on the nose."

    scene 4dbpostdate with dissolve

    d "It wasn't supposed to be subtle."
    d "Because if it was, you'd never pick up on it."

    b "Are you insinuating that I'm a blockhead?"

    d "You're a blockhead."

    b "Not insinuating, then. Stating."

    d "Just kiss me, Stupid."

    scene 6dbpostdate with dissolve

    bi "{i}I couldn't even feel her lips as her legs were squeezing me with a vice-like
        grip.{/i}"
    bi "{i}Dallas had some power in her thighs.{/i}"
    bi "{i}Despite probably being five foot nothing, she could lay me out if she wanted.{/i}"
    bi "{i}That's what I admired about her the most; her strength.{/i}"

    scene 4dbpostdate with dissolve

    b "Are you sure Avalon is okay with this?"

    d "Avalon wants both her girlfriend and her boyfriend, she doesn't want to settle for one or the other."
    d "Avalon is a freak in the best possible way."

    b "Truth!"

    d "Yeah, she's good with this."
    d "And if it complicates things, I'll back off. Promise."

    b "Alright. If you're sure."

    d "Now let's see how fast we can get you out of that suit!"

    scene 5dbpostdate with dissolve

    bi "{i}It did seem unusual how much Avalon wanted us to be a love triangle.{/i}"
    bi "{i}But I felt the same way. I didn't want to settle.{/i}"
    bi "{i}Avalon is the apple of my eye but Dallas is also absolutely incredible.{/i}"
    bi "{i}I want her too.{/i}"

    scene 7dbpostdate with fade

    play music "audio/disturbed_mind.mp3"

    b "Wow."

    d "Hmm?"

    b "I was just thinking, this is like a fantasy come to life."

    d "You're damn right it is. At least you know how lucky you are."

    b "Oh sorry, I meant for you."

    d "I sort of ruin the romantic moments, don't I?"

    b "I think we both do. We're kind of perfect together..."

    d "Well, then let's move on from the cheesy shit."

    scene 8dbpostdate with dissolve

    d "Now this is the real prize!"
    d "This is like unwrapping a lewd Christmas gift!"
    d "I wonder what it looks like."
    d "Fuck, I'm excited!"

    b "You know, if you feel uneasy about any of this at any time, we can slow down."
    b "Or we can stop completely if you get uncomfortable."

    scene 10dbpostdate

    d "You lock that shit up right now, [player_name]!"
    d "I love Avalon, but I am {b}not{/b} her!"
    d "And I don't want to be treated like her!"
    d "Do you understand?"

    b "What the fuck, Dallas?"
    b "What's gotten into you? You psychopath."

    scene 9dbpostdate with dissolve

    d "I'm serious. I don't want to be treated like a little princess."
    d "I like this shit. And I like it rough!"
    d "Don't treat me like I'm Avalon. Treat me like I'm {b}me{/b}."
    d "And {b}I{/b} want you to fuck me like you hate me."

    b "That's extreme! But..."
    b "Alright. Alright. That's fair. I'll be... rough?"

    scene 11dbpostdate with dissolve

    d "Good boy."
    d "Now, I would like to unwrap my present!"
    d "Don't disappoint me, [player_name]!"

    b "Yes, I live to please you, Dallas."
    b "You nutcase."

    scene 12dbpostdate

    d "Whoa! What the hell, man?!"
    d "Do you have a license for this thing?!"
    d "At what point is it legally considered a Weapon of Mass Destruction?"

    b "Oh, you're impressed?"

    scene 13dbpostdate with dissolve

    d "This thing is a monster, man!"
    d "Is it this hard because of me?"
    d "Really??"

    b "Yeah, have you seen you lately?"

    d "That's true, I'm a fucking ten."

    scene 15dbpostdate with dissolve

    d "Daaamn."

    b "Woah! Take it easy there, Thunder Grip!"

    d "It's so freakishly thick."
    d "Is it supposed to be this hard?"

    scene 14dbpostdate with dissolve

    b "What are you implying? There's something wrong with it?"

    d "Well, the tip does kind of look like a tumor."

    b "It's not a tumor!"

    scene 16dbpostdate with dissolve

    d "Let me get into a better position here."
    d "I want to try to get it into my mouth."

    b "What?! It won't fit in your mouth! You got a tiny little doll's face."

    scene 17dbpostdate with dissolve

    d "Come on! Do it!"
    d "I said don't take it easy on me!"

    b "Shit. Alright."
    b "Don't say I didn't warn you."

    scene 18dbpostdate with dissolve

    d "Mmm!"
    d "Mm mm!"

    b "Wow. Guess I was wrong."
    b "It does fit if I push hard enough."

    scene 1dallasblowjob

    b "Pinch my leg or something if it gets too intense."
    b "Here we go."

    d "Mmm mm!"

    show dallasblowjob with dissolve

    b "Ooh, shit, Dallas!"
    b "That feels great!"

    d "Mmm!"

    b "How are you not gagging?"
    b "You don't have a gag reflex?"

    d "Mmm mm!"

    b "C-careful! Your teeth, watch it with the teeth!"

    scene 19dbpostdate

    d "*Cough* *Cough*"
    d "Fuck, you were right. It's too much."
    d "Ow."

    b "Oh man, I didn't hurt you, did I?"
    b "Are you okay?"

    scene 20dbpostdate with dissolve

    d "Yeah, I'm fine."
    d "It really wasn't that--"

    scene 19dbpostdate

    d "*Cough* *Cough*"
    d "Okay, maybe it was that bad."
    d "You slammed into the back of my throat too hard."
    d "Ow ow."

    b "Do you need some ice cream or something?"

    d "No, I'm good."

    scene 22dbpostdate with dissolve

    d "Here. Try the other end."
    d "You haven't damaged that shit yet."

    b "Are you serious?"

    d "Yeah!"
    d "Let's do this thing!"

    scene 23dbpostdate with dissolve

    b "You were just coughing like you were about to die."

    d "Don't be a pussy, [player_name]."
    d "You know you want me."

    show dallasbootyshake

    d "Come on, Big Boy."
    d "You can have it if you want it."
    d "All you have to do is take it."

    b "Really??"
    b "You're going to shake it at me??"

    scene 26dbpostdate with dissolve

    d "What... what are you doing?"
    d "Why are you raising your hand?"

    scene 27dbpostdate

    play sound "audio/faceslap.mp3"

    d "Oow! Fuck."

    scene 28dbpostdate with dissolve

    d "Dammit, that hurt."
    d "What the hell was that for?"

    b "For teasing me!"

    d "I'm not teasing you!"
    d "You can literally have me right now."
    d "Fuck, I'm so horny."

    b "A fan of the butt slap, are you?"

    d "Maybe..."

    scene 29dbpostdate with dissolve

    b "Well let's get these off, then."

    d "Yes!"
    d "Do it!"

    scene 31dbpostdate with dissolve

    play sound "audio/clothrip.mp3"

    pause (.3)

    d "What the fuck!?"
    d "Did you just rip my panties off??"

    scene 22dbpostdate with dissolve

    b "Shit. My bad."
    b "I got a little carried away."
    b "I'll buy you new ones!"

    d "Who cares about the panties!?"
    d "That was hot!"
    d "You need to fuck me, like, right now!"

    scene 31dbpostdate with dissolve

    b "You're sure you're ready for this?"

    d "[player_name], if you don't put that dick in my pussy right now,"
    d "I swear to Christ, I'm going to--"

    scene 30dbpostdate

    d "Dah!"
    d "What... what is that!?"

    b "That's just the tip."

    d "Are you serious?!"
    d "Wait wait!"

    b "Nope."

    scene 1dallasdoggy

    d "Ow! Ow fuck!"
    d "Stop stop!"
    d "Pull it out!"

    b "You told me not to stop no matter what, Dallas!"

    d "Fuck fuck!"

    show dallasdoggy

    d "Oh my god!"
    d "It's too big!"
    d "Ow!"
    d "You're going to break me!!"

    b "You're so tight, Dallas."
    b "It feels too good!"
    b "I can't stop!"

    d "You have to! You have to!"
    d "Aaah!"

    b "Okay, okay!"

    scene 19dallasdoggy

    pause (.5)

    scene 32dbpostdate with dissolve

    d "Oh! Thank god!"

    b "Wow, that was fantastic!"

    d "You broke it."
    d "You definitely broke it."
    d "My pussy feels like it's on fire."
    d "Fuck."

    b "Come on. Let's try another position."

    scene 33dbpostdate

    d "No!"
    d "I... I need to recover!"
    d "I can't take that thing again!"
    d "I can finish you off with a handjob, okay?"


    scene 34dbpostdate with dissolve

    b "You told me to be rough with you!"

    d "I did. I did say that!"
    d "I may have overestimated myself..."

    scene 33dbpostdate with dissolve

    b "Come on, you told me not to be a pussy."
    b "Now who's the pussy?"

    scene 35dbpostdate with dissolve

    d "Hey, don't call me a pussy!"
    d "Bitch."

    b "Then stop acting like one."
    b "I'll be gentle this time."
    b "Let's go."

    scene 36dbpostdate with dissolve

    d "Fine but you better go easy this time!"
    d "You fucking brute."

    scene 37dbpostdate

    d "Yo, look at you!"
    d "Can you seriously just hold me up like this?"
    d "You really are strong, huh?"

    b "You weigh like, eighty pounds."
    b "I'm not exactly struggling here."
    b "Damn, those are nice boobs."
    b "Good job, Dallas."

    d "I... didn't make them. Dumbass."

    scene 38dbpostdate with dissolve

    d "But... thanks. They are pretty great, aren't they?"

    b "Yeah. They are. Can I have them?"

    d "Mhmm. They're all yours."
    d "{b}I'm{/b} all yours."

    b "Well, would you look at that."
    b "I guess a little dick really changes you?"

    d "Pff. I wouldn't say little!"

    scene 37dbpostdate with dissolve

    b "You ready to give this a try?"

    d "Yeah!"
    d "Just... maybe be a bit more gentle this time."

    b "Alright."

    show dallasstanding with dissolve

    d "Ooh!"
    d "That's better, that's better."
    d "Nice and slow."

    b "This is way more sensational than I thought it'd be."
    b "It's really... {b}really{/b} working for me!"

    d "Are you going to cum?"
    d "Finish inside me, [player_name]."
    d "Please!"

    b "Oh fuck fuck!"

    scene 39dbpostdate

    d "Oh God!"
    d "I can feel it inside me!"

    scene 40dbpostdate

    d "Oh no, it's too much!"
    d "You're filling me up!"
    d "Stop stop!"

    b "I... I can't! I can't stop cumming!"

    d "Then put me down!!"

    scene 41dbpostdate

    d "Ah!"

    scene 42dbpostdate with vpunch

    d "Oof!"

    scene 43dbpostdate with dissolve

    d "Ooh my god. Your semen is..."
    d "What the hell?!"
    d "It's supposed to come out, right?"

    scene 45dbpostdate

    b "I got it in there pretty deep, didn't I?"
    b "It's like your pussy just ate it all up."
    b "Must have been hungry."

    scene 44dbpostdate

    d "This is freaky. It's definitely in there."
    d "I can feel it."
    d "My God, [player_name]."
    d "You really did a number on me tonight."

    b "You're welcome?"

    scene 46dbpostdate

    if persistent.likeitrough == False:
        $ renpy.notify("You've unlocked 'Like it Rough' in the Scene Gallery on the Main Menu!")
        $ persistent.likeitrough = True

    d "Ugh. I'm going to go try to coax your cum out of my pussy."
    d "I'll be back."
    d "Do I need to jump up and down or... or what..?"

    $ renpy.end_replay()
    scene 47dbpostdate

    pause

    stop music fadeout 2.0

    scene 48dbpostdate with dissolve

    bi "{i}That was fucking crazy.{/i}"
    bi "{i}Jeez, I really hope I didn't actually hurt her.{/i}"
    bi "{i}I think I got a little carried away.{/i}"
    bi "{i}Seeing her naked though, it drives me absolutely wild.{/i}"
    bi "{i}What a spectacular girl you are,{/i}"
    bi "{i}Dallas.{/i}"

    jump dallas_night

    ## Octavia and Byron's Date at the Library ##

    label octavia_date:

    scene 1obdate with fade

    b "The library?"
    b "Oh no, you're not going to make me get smarter so we can date, are you?"
    b "I've got some bad news, Octavia."
    b "I'm about as smart as I'm going to get."

    scene 2obdate with dissolve

    o2 "Oh, [player_name]."
    o2 "You make me laugh!"
    o2 "You silly goose!"

    b "I apologize."
    b "I get a little goofy when I'm nervous."

    scene 5obdate with dissolve

    o2 "I enjoy your sense of humor, [player_name]."
    o2 "I'm a touch nervous myself so I appreciate the levity."

    b "I get uncomfortable when things get too serious."
    b "It's nice to lighten the air."

    scene 3obdate with dissolve

    o2 "It's especially nice at this moment because I'm really not sure
        how you're going to feel about this date I've prepared."
    o2 "I know it's perhaps more romantic than it ought to be."

    scene 4obdate with dissolve

    o2 "If it's not something you're interested in, I would understand."
    o2 "I won't be offended if you would prefer to do something else."

    scene 6obdate with dissolve

    o2 "If you would like to go to a restaurant or perhaps see a movie, I'd be
        just fine with that."
    o2 "But I thought since this is where we first met that--"

    scene 9obdate with dissolve

    o2 "Oh? [player_name]?"
    o2 "Is something wrong?"

    b "Octavia, this is..."
    b "This is too much."

    scene 8obdate

    b "You set this up for our date?"
    b "For... me?"

    o2 "Well, yes."

    scene 7obdate with dissolve

    o2 "I contacted the manager of the library and asked for a favor."
    o2 "He allowed me to set this up for us."

    scene 9obdate

    o2 "You don't like it?"

    b "Nobody has ever done something like this for me before."
    b "I'm not really sure how to react."
    b "I'm not even sure I'm worth this, Octavia..."

    scene 10obdate with dissolve

    o2 "Is that how you feel?"
    o2 "You're usually such a confident man, [player_name]."
    o2 "But you have a fear of disappointing those you care about, don't you?"

    scene 11obdate with dissolve

    o2 "I may have just found your kryptonite."
    o2 "It's alright, [player_name]. You can let me see behind the curtain."
    o2 "You can let me in."

    b "Octavia, I already feel like I've failed Avalon so many times."
    b "Sometimes I wonder if she would be better off without me."
    b "I'm afraid I'm going to let you down too, eventually."

    scene 12obdate with dissolve

    o2 "[player_name], you do a lot of dopey things."
    o2 "You shouted in a library and made me fall!"

    b "Oh yeah..."

    o2 "And you bought your niece a vibrator!"

    scene 13obdate

    b "That was pretty dumb, huh?"
    b "It seemed like a good idea at the time."
    b "I mean, she did enjoy it..."

    scene 12obdate with dissolve

    o2 "You don't always do the right thing but you always have the best intentions in mind."
    o2 "And that's why I like you."
    o2 "Not for your brain, but for your heart."
    o2 "You have a good heart, [player_name]."
    o2 "And that means you could never disappoint me."

    scene 13obdate

    b "You know, you lied to me, Octavia."

    o2 "What? When?"

    b "When you told me you're not an Angel."
    b "I've never met someone more Angelic than you."

    scene 11obdate

    o2 "You are far too kind."
    o2 "Consider me sufficiently buttered up, [player_name]."
    o2 "Come now, treat me to this wonderful date."
    o2 "I'm eager to continue it."

    scene 14obdate with dissolve

    b "I've never been on a date like this..."
    b "I'm not sure how to describe it."
    b "Elegant?"

    o2 "It's just some common foods to be eaten in a library."

    scene 15obdate with dissolve

    b "Maybe it would be to anyone else."
    b "But for us, this is especially meaningful."
    b "I'm glad you took the lead on this one, I would have taken us to the Oliver Garden."

    o2 "I feared as much."

    scene 16obdate with dissolve

    o2 "Oh look at you!"
    o2 "Such a gentleman."

    b "I'm really just mimicking what I've seen in movies."
    b "I'm sure glad you're impressed though!"

    scene 17obdate with dissolve

    o2 "Thank you, [player_name]."

    b "You're welcome."

    scene 18obdate with dissolve

    o2 "I heard Avalon has a date with Penny tonight?"
    o2 "I would assume to discuss what happened with Tyler?"

    scene 19obdate with dissolve

    b "Oh, yeah."
    b "I guess that would be safe to assume."
    b "I presumed it was just a girl's night out."
    b "Do you know Penny?"

    scene 35obdate with dissolve

    o2 "I do, actually."
    o2 "We dated for a few years."
    o2 "I wanted to settle down and live a simple, peaceful life."
    o2 "But she still wants the thrill of adventure."

    scene 18obdate with dissolve

    o2 "I apologize, I shouldn't talk about my previous relationships on our date."
    o2 "That's very rude of me."

    scene 23obdate

    b "Oh, I don't mind."
    b "But you dated for several years?"
    b "Was that... legal?"
    b "She's so young."

    scene 22obdate

    o2 "Oh, [player_name]."
    o2 "She's got you quite fooled too, doesn't she?"

    scene 18obdate with dissolve

    o2 "Penny is twenty-four."
    o2 "She is three years younger than I."

    scene 23obdate

    b "Seriously!?"
    b "She looks like a teenager."
    b "And she's so petite..."

    scene 20obdate

    o2 "An attribute she takes advantage of."
    o2 "She's tricked a lot of people with her size."

    b "But not you?"

    scene 18obdate with dissolve

    o2 "Let's focus on us tonight, [player_name]."

    scene 38obdate

    b "If you're three years older than Penny, and she is twenty-four."
    b "That would mean you're only a year younger than me."
    b "We're practically the same age."

    scene 20obdate

    o2 "We are."
    o2 "I believe you're used to dating younger women."
    o2 "Can you handle a more experienced lady?"

    scene 21obdate

    b "You make it sound like you're a grandma."
    b "You've been spending too much time with that Panther of yours, haven't you?"
    b "Now you think you're a cougar."

    scene 22obdate

    o2 "Oh stop it!"
    o2 "You're such a goof!"

    scene 36obdate

    b "Do you think it's weird though?"
    b "I'm not only dating someone so young but she's also technically my niece."
    b "I mean, I took her in to protect her and help her get back on her feet."
    b "But now we're... involved."
    b "Am I... am I taking advantage of her?"

    scene 18obdate

    o2 "When I first saw you and Avalon together, I'd never seen two people more
        in love."
    o2 "It's not a traditional relationship, but it works for you two."
    o2 "I've been so inspired by your happiness together that I'm even selfishly
        trying to be a part of it."
    o2 "It's a unique situation you're in and you'll be judged harshly sometimes."
    o2 "But from what I've seen, you're both exponentially better together."

    scene 23obdate

    b "W-wow, uhm, thank you, Octavia."
    b "That actually makes me feel a lot better."

    scene 19obdate with dissolve

    b "But I don't think you're the only selfish one here."
    b "You've been such a boon for Avalon and I."
    b "I appreciate the way you've taken care of us."

    scene 38obdate with dissolve

    b "I'm really not sure how I feel about a polygamous relationship."
    b "Having two of the most wonderful people I've ever met in my life is spectacular!"
    b "But is it going to be complicated?"

    scene 37obdate

    o2 "Technically, it would be a Polyamorous relationship."
    o2 "As for complications, I really don't know, [player_name]."
    o2 "It's an experience I've yet to have as well."

    scene 23obdate

    b "I hope that didn't come out wrong."
    b "I'm absolutely thrilled at the prospect."
    b "And Avalon seems especially intrigued by the idea."

    scene 18obdate

    o2 "Don't overthink it, [player_name]."
    o2 "This is only a date."
    o2 "We're not making any commitments right now."

    b "Of course! Sorry!"

    o2 "And if things do get complicated, I'll happily digress back to just friends."

    scene 21obdate

    b "Actually, Avalon was getting a bit excited at the idea of us being intimate."
    b "Is that called something?"

    scene 20obdate

    o2 "It is."
    o2 "She may be finding herself with a Voyeurism fetish."
    o2 "She's a wildcard, isn't she?"

    scene 21obdate

    b "You're telling me!"
    b "How about you, Octavia?"
    b "Any unusual kinks I should be aware of?"

    scene 22obdate

    o2 "Oh so forward!"
    o2 "You bad man!"

    scene 24obdate with dissolve

    o2 "Perhaps I'll show you some of my interests one day."

    b "Oh, I was just teasing."

    o2 "No, you weren't."

    b "No, I wasn't."

    scene 25obdate with dissolve

    o2 "For now, how about a dance?"

    b "Unfortunately, I have two left hooves."

    o2 "Come on, [player_name]."
    o2 "I insist."

    scene 26obdate with dissolve

    b "How can I say 'No'?"

    o2 "You shouldn't want to say 'No'."

    b "You do often seem to know exactly what I want."

    scene 27obdate with dissolve

    o2 "Perhaps you're just easy to read, [player_name]."

    b "Or maybe you've got superpowers."
    b "Can you read minds, Octavia?"
    b "What am I thinking right now?"

    scene 28obdate with dissolve

    o2 "Are you sure you want me to read your mind?"

    b "Well now I'm not!"

    o2 "You're nervous about touching me but equally eager to."
    o2 "You're afraid I'll reject your affection."
    o2 "And you're afraid I'll hurt you."
    o2 "I won't."

    scene 30obdate

    b "Nah, I was thinking about those ships they put in those little bottles."
    b "How do they get those in there, anyway?"

    scene 29obdate with dissolve

    o2 "You're telling a joke to deflect."
    o2 "I must have hit a little too close to home?"

    b "You always do."
    b "It's my favorite part about you."
    b "Sometimes I think you know me better than I know myself."

    o2 "We've only just met."
    o2 "I'm sure there is a lot we don't know about each other."

    scene 30obdate with dissolve

    b "Well, I'm looking forward to getting to know you better."

    scene 31obdate with dissolve

    b "A lot better."

    o2 "Go on."
    o2 "You can kiss me."

    scene 34obdate with dissolve

    b "I can, can I?"

    o2 "If you want."

    b "You know I do."

    scene 33obdate with dissolve

    bi "{i}As I pressed my lips to hers, I felt a wave of peace wash over me.{/i}"
    bi "{i}The butterflies in my stomach stopped fluttering.{/i}"
    bi "{i}My mind stopped racing.{/i}"
    bi "{i}And a strange, cleansing heat enveloped my whole body and seemed to burn away
        all my doubts.{/i}"

    scene 34obdate with dissolve

    b "Octavia."

    o2 "Yes?"

    b "That kiss was absolutely divine."
    b "I feel like I'm floating."

    o2 "Hmm. Well."
    o2 "Perhaps another will bring you back down to Earth?"

    scene 32obdate with dissolve

    bi "{i}Octavia stole the next kiss and another wave hit me like a gust of wind.{/i}"
    bi "{i}And once again, a warmth spread through me and comforted me.{/i}"

    scene 28obdate with dissolve

    o2 "Perhaps we can continue this date at your place?"

    b "Sure."

    scene 27obdate with dissolve

    bi "{i}So with our eyes locked onto each other, we left.{/i}"
    bi "{i}We spent the evening so entranced by one another,{/i}"
    bi "{i}we never even took one bite of our meals.{/i}"

    jump octavia_sex

label octavia_sex:
    if _in_replay:
        $ player_name = renpy.input("What would you like to name the MC?")
        if player_name.strip() == "":
          $ player_name = "Byron"

    ## OCTAVIA SEX AT BYRONS HOUSE ##

    scene 1obpostdate with fade

    b "S-so I'm not real sure what happens next."
    b "You're sure Avalon is really okay with us..."
    b "You know..."

    scene 2obpostdate with dissolve

    o2 "Yes, I'm sure."
    o2 "She was quite insistent that we enjoy ourselves, actually."

    b "Oh yeah? Should we--"

    scene 3obpostdate with dissolve

    b "Mmf!"

    bi "{i}Octavia really knew how to take control.{/i}"
    bi "{i}She seemed confident in our actions.{/i}"
    bi "{i}So I let her lead.{/i}"

    scene 5obpostdate with dissolve

    o2 "Trust me, [player_name]."
    o2 "I won't let anything happen to your relationship with Avalon."
    o2 "I promise."

    b "You're very convincing. Especially when you're pressing into me like this..."

    o2 "Mhmm. I can be very..."

    scene 3obpostdate with dissolve

    b "Mmm..."

    scene 5obpostdate with dissolve

    o2 "Compelling."
    o2 "I'm going to go freshen up."
    o2 "I'll meet you in your room."

    b "A-alright."

    o2 "And don't be wearing that suit when I come in."

    scene 6obpostdate with dissolve

    bi "{i}She is so intense sometimes.{/i}"
    bi "{i}I simultaneously feel anxious and at ease.{/i}"
    bi "{i}You are an extraordinary woman,{/i}"
    bi "{i}Octavia.{/i}"

    scene 7obpostdate with fade

    bi "{i}She's been in there a while.{/i}"
    bi "{i}Should I wear a shirt?{/i}"
    bi "{i}No no, this is fine.{/i}"
    bi "{i}Push ups! I should do some push-ups!{/i}"
    bi "{i}Dammit, I wish I was more confident about what to do here...{/i}"

    o2 "[player_name]?"

    scene 8obpostdate with dissolve

    b "Oh. You... wow, you look beautiful."

    scene 10obpostdate

    play music "audio/tomorrows_rain.mp3"

    o2 "Thank you."
    o2 "And look at you."
    o2 "Such a big, strong man."

    scene 9obpostdate

    b "You think so?"
    b "I feel pretty small right now, for some reason..."

    scene 10obpostdate

    o2 "I hope you don't mind but I borrowed this robe."
    o2 "It was in the bathroom."

    scene 11obpostdate

    bi "{i}Ah, the perfect opportunity for a joke!{/i}"
    bi "{i}Levity is always a good thing, right?{/i}"

    b "I'm sorry, Octavia, but that's Avalon's robe."
    b "You'll have to ask her if you can wear it."
    b "Which means, until she says yes..."

    scene 13obpostdate

    o2 "Oh, is that how it is, [player_name]."
    o2 "You're so bad!"

    scene 15obpostdate with dissolve

    o2 "But I guess it is your house and your rules."
    o2 "It would be rude of me to disobey."
    o2 "I'd better remove this, hadn't I?"

    scene 14obpostdate

    b "W-wait, I was kidding!"
    b "You can wear it forever if you wa--"

    scene 16obpostdate with dissolve

    b "Ah!"
    b "You didn't have anything on under it?!"
    b "You're... you're..!"

    scene 17obpostdate

    o2 "Nude?"
    o2 "What do you think?"
    o2 "Do you like the way I look naked, [player_name]?"

    scene 18obpostdate with dissolve

    b "Yes!"
    b "I didn't expect you to be so..."
    b "I mean, you're in really great shape."

    scene 19obpostdate

    o2 "I was in the military for many years."
    o2 "Even outside of it, I still take care of myself."
    o2 "I don't work out quite as hard as you but I eat well and exercise regularly."

    scene 20obpostdate

    b "O-oh, y-yeah, that makes sense."
    b "I d-didn't think about that."
    b "You're uhh, you're really close to me..."

    scene 21obpostdate

    o2 "Am I making you nervous?"

    b "Maybe a little..."

    o2 "Would you like to touch me, [player_name]?"

    b "C-could I?"

    scene 22obpostdate with dissolve

    o2 "If you'd like to."

    b "You're towering over me right now."
    b "It's sort of intimidating, actually..."
    b "But, yeah, I would like to touch you."

    o2 "Alright."

    scene 23obpostdate with dissolve

    o2 "Give me your hand."

    b "Oh, this one?"
    b "Sure, yeah."
    b "It's all yours."

    scene 24obpostdate with dissolve

    o2 "And place it here."

    b "Gah!"

    o2 "How is that, [player_name]?"
    o2 "Do you like how I feel?"

    b "They're firm!"
    b "I can feel your nipple pressing into my palm."

    o2 "That's because I'm immensely aroused right now."
    o2 "Especially now that your hand is on my breast."

    b "Yeah? What if I grab you..."

    scene 25obpostdate with dissolve

    b "Here?"

    o2 "Oh! Well, there you are!"
    o2 "I thought a push in the right direction might get you going."

    scene 26obpostdate

    b "Oh, you were waiting for me to be more forward?"

    o2 "Of course."

    b "I'm afraid of doing something wrong."
    b "I just... I really like you. I don't want to ruin it."

    o2 "Oh, [player_name]. Stand up."

    scene 27obpostdate with dissolve

    o2 "If you do something I don't like, I'll tell you."
    o2 "And I'll help push you in the right direction."
    o2 "Don't be afraid to take what you want from me."

    b "Alright. Yeah. That sounds fair."

    o2 "Now, I'm naked here but it looks like you're still wearing your boxers."
    o2 "That doesn't seem right, does it?"

    b "Uhh, no?"

    scene 28obpostdate with dissolve

    b "Whoa! Don't pull on those so aggressively!"
    b "They're my expensive pair."
    b "Damn, you got those down quick..."

    scene 29obpostdate

    o2 "My goodness, [player_name]!"
    o2 "This is quite impressive!"
    o2 "I did not expect it to be so... so..."

    scene 30obpostdate

    b "Be careful down there, alright?"
    b "The last girl that pulled my boxers down that fast took the full weight of
        my erection right to her face."
    b "It knocked her out cold."
    b "She never could say her R's right after that..."

    scene 31obpostdate

    o2 "I'm glad you're proud of your equipment, [player_name]."
    o2 "You should be."
    o2 "It's an impressive member."

    b "Thank you. Be gentle with it, I've only got the one."

    scene 32obpostdate with dissolve

    o2 "I don't think I could hurt it if I wanted to."
    o2 "Its rock hard, [player_name]!"
    o2 "All for me, hmm?"

    b "If... you want it."

    scene 33obpostdate with dissolve

    b "Ah! That's a good grip you have!"

    o2 "Mm."
    o2 "Yes."
    o2 "Let's see if we can stimulate it a bit, shall we?"

    show octaviahj with dissolve

    b "Yaah! Damn, that feels good."

    o2 "Oh you like that, huh?"
    o2 "I think it's getting harder!"
    o2 "When was the last time a woman pleased you, [player_name]?"

    b "It's actually-- Aaah. It's been a while."

    o2 "Has it?"

    scene 31obpostdate with dissolve

    o2 "How about we move this to the bed?"

    b "That... sounds fun."

    o2 "Lie down for me."

    scene 34obpostdate with fadefast

    b "Just like this or..?"

    o2 "That's perfect."

    scene 35obpostdate with dissolve

    o2 "Mm, I don't want to let go of this."
    o2 "I like it so much, I think I could hold onto it forever."

    b "Well, you can't. If it stays like that for more than four hours, I have to
        see a doctor according to an article I read."

    o2 "I guess I'll just have to enjoy it while it lasts then."

    scene 36obpostdate with dissolve

    o2 "Oh my!"
    o2 "It's really pressing against me hard."
    o2 "It's quite stimulating!"

    scene 1octaviagrind with dissolve

    o2 "Perhaps we warm up a little?"
    o2 "What do you think?"

    b "What do you mean?"
    b "How do we--"

    show octaviagrind with dissolve

    b "Ooh, God!"
    b "Keep going!"

    o2 "Mm, do you like that?"
    o2 "Can you feel my wet pussy grinding against you, [player_name]?"

    b "Yeah! I can, I really can!"

    scene 38obpostdate with dissolve

    o2 "I'm sufficiently lubricated now, [player_name]."
    o2 "Would you like me to put you inside of me now?"
    o2 "Go on, tell me what you want."

    b "Yes! That! I want that!"

    o2 "Say what you want, [player_name]."

    b "I... want to fuck you!"

    o2 "Oh! So aggressive!"
    o2 "Well if that's what you want,"

    scene 40obpostdate with dissolve

    o2 "that's what I'll give you."
    o2 "A good, hard ride."
    o2 "How about that?"

    b "You're killing me, Octavia!"
    b "You're so intense!"

    scene 39obpostdate with dissolve

    o2 "Tell me if you don't like something I'm doing."

    b "I love it. I love all of it."

    o2 "Let's see if we can fit this inside me."
    o2 "It's much larger than I've had before."

    scene 41obpostdate with dissolve

    b "Well, don't go further than you're comfortable with. I don't want to hurt you."

    o2 "Just a little bit at a time."
    o2 "I should be able to stretch to accommodate..."

    scene 43obpostdate with dissolve

    o2 "Ah! It's... it's a bit much."

    b "Gah! It's not... fitting. You're just bending me!"

    scene 42obpostdate with dissolve

    o2 "Just let me concentrate."
    o2 "Ooh!"
    o2 "It's... it's going."

    scene 44obpostdate with dissolve

    o2 "I've got the tip in."

    b "Just the tip?"

    o2 "Yes, for now."
    o2 "I'm going to drop a little."

    scene 45obpostdate

    o2 "Ah ah! Stop!"

    b "I'm not doing anything!"
    b "You're the one moving!"

    o2 "Okay, okay, just a moment."

    scene 46obpostdate with dissolve

    o2 "Your girth is considerable, [player_name]."
    o2 "I didn't think I'd have this much trouble."
    o2 "Mmgn. I think..."
    o2 "I think we'll do it like a bandaid."

    b "W-wait, don't do that!"

    scene 47obpostdate with vpunch

    o2 "Oww! Ow ow!"

    b "Arg! You came down too fast!"
    b "I think you broke me!"

    scene 48obpostdate

    o2 "Oh God! It's so deep!"
    o2 "It's stretching me too much!"

    b "You came down too hard!"
    b "Ow!"

    scene 49obpostdate with dissolve

    o2 "I'm sorry, [player_name]."
    o2 "Are you alright?"
    o2 "Do you want me to stop?"

    b "N-no. It's fine."

    o2 "I'm going to try to move now."
    o2 "Do you want that?"
    o2 "Do you still want to fuck me?"

    b "Yes! Absolutely! Ride away!"
    b "I will manage!"

    show octaviacowgirl with dissolve

    o2 "Oh this is dizzying!"
    o2 "It's absolutely filling me up."
    o2 "I can't believe how good it feels."

    b "D-don't clinch so hard."
    b "It's... it's too tight."

    o2 "I can't help it!"
    o2 "It's making me quiver!"

    b "Octavia, I'm... I'm going to..."

    o2 "Oh, cum. Please cum!"

    scene 50obpostdate with dissolve

    b "Aah! Fuck!"

    o2 "Ooh! There's so much!"
    o2 "There's {b}too{/b} much!"
    o2 "It's filling me up!"

    scene 49obpostdate with dissolve

    o2 "Oh my goodness!"
    o2 "I'm absolutely full, [player_name]!"

    scene 51obpostdate with dissolve

    b "Wow."
    b "That was intense. Really intense!"

    o2 "That was incredible."
    o2 "Thank you."

    b "You're... welcome?"

    scene 52obpostdate

    o2 "O-oh, it's... it's dripping out of me."
    o2 "I think I better go get cleaned up."
    o2 "I'll be right back, alright?"

    b "Oh, sure. I'll be here."

    scene 53obpostdate

    if persistent.considerablegirth == False:
        $ renpy.notify("You've unlocked 'Considerable Girth' in the Scene Gallery on the Main Menu!")
        $ persistent.considerablegirth = True

    bi "{i}Holy shit!{/i}"
    bi "{i}That was awesome!{/i}"
    bi "{i}I hope I didn't hurt her.{/i}"

    $ renpy.end_replay()
    scene 54obpostdate with dissolve

    bi "{i}Octavia.{/i}"
    bi "{i}You are an incredible woman.{/i}."
    bi "{i}How lucky are we to have found you?{/i}"

    jump octavia_night

    # DALLAS POST SEX WITH BYRON ##


    label dallas_night:

    scene 1dbpostnight with fade

    play music "audio/touching_moment.mp3"

    bi "{i}Dallas sleeps like the dead. She's out cold!{/i}"
    bi "{i}She almost looks sweet when she's unconscious.{/i}"
    bi "{i}I can't believe she just crawled into my lap and almost instantly was out
        like a light.{/i}"
    bi "{i}I guess even strong women like Dallas need affection.{/i}"
    bi "{i}This is probably my favorite moment with her, if I'm being honest.{/i}"

    scene 2dbpostnight

    ai3 "{i}Oh my gosh!{/i}"
    ai3 "{i}This is the cutest thing I've ever seen!{/i}"
    ai3 "{i}She looks so happy. And [player_name] seems like he's completely zen right now.{/i}"
    ai3 "{i}They must have had a great time. That's so wonderful!{/i}"

    scene 3dbpostnight with dissolve

    bi "{i}Hmm?{/i}"
    bi "{i}Oh, it's Avalon. How did I not hear her come in..?{/i}"
    bi "{i}I must have been really zoned out.{/i}"
    bi "{i}I'm glad to see she's grinning ear to ear. I guess I'm not in trouble. Yet...{/i}"

    scene 4dbpostnight with dissolve

    ai3 "{i}I'm going to go change. Hold on, [player_name]! I'll be back!{/i}"

    bi "{i}Oh, she wants me to hang on?{/i}"
    bi "{i}What's she doing?{/i}"

    scene 5dbpostnight with dissolve

    pause

    scene 6dbpostnight

    bi "{i}Maybe she's going to get ready for bed?{/i}"
    bi "{i}She looks so elegant in that dress.{/i}"
    bi "{i}I almost hate to see her out of it.{/i}"

    scene 7dbpostnight with dissolve

    bi "{i}Avalon and Dallas.{/i}"
    bi "{i}Two extraordinary women.{/i}"
    bi "{i}How fortunate am I?{/i}"

    scene 8dbpostnight with fadefast

    bi "{i}Oh, she's back.{/i}"
    bi "{i}I guess she was going to change.{/i}"

    scene 9dbpostnight

    b "Hey, Avalon."

    a "Shh."

    scene 10dbpostnight with dissolve

    bi "{i}Perhaps she wants to savor the moment and not wake Dallas just yet.{/i}"
    bi "{i}I have to be honest with myself, I'm fond of this moment as well.{/i}"

    ai3 "{i}She looks so blissful right now.{/i}"
    ai3 "{i}Well, I know exactly how she feels.{/i}"
    ai3 "{i}Because [player_name] makes me feel the same way every day.{/i}"
    ai3 "{i}Maybe now we can all feel that way every day.{/i}"

    scene 11dbpostnight with dissolve

    bi "{i}I wondered how long we could sit here like this?{/i}"
    bi "{i}I knew we would have to move to the bed eventually.{/i}"
    bi "{i}But I would savor every second of this for as long as it would last.{/i}"

    stop music fadeout 1.0

    jump outro5

    ## OCTAVIA POST SEX WITH BYRON ##

    label octavia_night:

    play music "audio/tomorrows_rain.mp3"

    scene 1obpostnight with fade

    ai3 "Oh my gosh!"
    ai3 "[player_name] is asleep with his head on Octavia's lap!"
    ai3 "They must have had a really great night."
    ai3 "This is so adorable, I might die from cuteness overload!"

    scene 2obpostnight with dissolve

    o2 "Hmm?"
    o2 "Oh!"

    show octavia_comeover with dissolve

    o2 "Hi, Avalon!"
    o2 "Come here!"

    scene 5obpostnight

    a3 "You're talking awful loud."
    a3 "Aren't you going to wake him up."

    o2 "I assure you, he won't wake up."
    o2 "Sit with me."

    scene 7obpostnight with dissolve

    o2 "Oh, Avalon. You look like such an elegant lady."
    o2 "How was your date with Penny?"

    scene 8obpostnight

    a3 "It was wonderful!"
    a3 "She's so interesting and fierce!"
    a3 "How was your date with [player_name]?"
    a3 "Did you... you know? Take care of him?"

    scene 9obpostnight

    o2 "I have to be honest with you, Avalon. It all kind of got away from me."
    o2 "We did engage in sexual intercourse."
    o2 "It wasn't my intention to go all the way like that but I'm afraid I just
        couldn't help myself."

    scene 10obpostnight

    a3 "That. Is. Epic!"
    a3 "You have to tell me everything."
    a3 "How did it feel? What's his penis look like?"

    scene 7obpostnight

    o2 "Well, that's not exactly the reaction I expected."
    o2 "You sure are a strange girl, Avalon. And I'm quite glad of it."
    o2 "I'll tell you what; instead of telling you, I'll help you get to that level with [player_name]."
    o2 "But not tonight."

    scene 8obpostnight

    a3 "You're the best, Octavia!"
    a3 "Thank you!"
    a3 "I'm going to go change, I'll be right back."

    scene 11obpostnight with dissolve

    o2 "What an unusual reaction."
    o2 "Most people would be insanely jealous, but her reaction is just the opposite."
    o2 "I wonder why that is..?"

    scene 12obpostnight with fadefast

    a3 "Okay, I'm back."

    scene 13obpostnight with dissolve

    o2 "Come here, Sweetie."
    o2 "Sit next to me."

    a3 "I'd love to."

    scene 14obpostnight with dissolve

    a3 "Mm. You feel nice, Octavia."
    a3 "Thank you for taking care of [player_name]. He really needed it."

    o2 "Yes, he did!"
    o2 "And it was my pleasure."

    scene 15obpostnight with dissolve


    o2 "Rest now, Avalon."

    stop music fadeout 2.0

    a3 "I am really tired all of the sudden."
    a3 "Mm. Goodnight, Octavia."

    o2 "Goodnight, Darling Avalon."

    jump outro5

    ## NIGHT AFTER PENNY DATE WITH BYRON AND AVALON IF ON THE MONO PATH ##

label mono_night:

    scene 1mononight with fade

    a3 "Yaaaw."
    ai3 "{i}That date with Penny was terrific!{/i}"
    ai3 "{i}But now I'm exhausted.{/i}"

    scene 2mononight with dissolve

    ai3 "{i}Hmm. I'm sure [player_name] is asleep.{/i}"
    ai3 "{i}I don't really want to sleep alone tonight.{/i}"
    ai3 "{i}I'm sure he wouldn't mind if I snuck into bed with him.{/i}"
    ai3 "{i}Right?{/i}"

    scene 3mononight with dissolve

    ai3 "{i}Aha! Just as I thought.{/i}"
    ai3 "{i}He's completely out!{/i}"

    scene 4mononight

    play music "audio/touching_moment.mp3"

    pause

    scene 5mononight with dissolve

    ai3 "{i}I have to be sneaky like a ninja!{/i}"
    ai3 "{i}I don't want to wake him.{/i}"

    scene 6mononight with dissolve

    bi "{i}Gah! Intruder!{/i}"
    bi "{i}A very affectionate intruder!{/i}"
    bi "{i}It's probably Avalon...{/i}"

    ai3 "{i}Mm. He's so warm.{/i}"

    scene 7mononight with dissolve

    bi "{i}I'd love to know how her date went.{/i}"
    bi "{i}But I don't want to ruin this moment.{/i}"
    bi "{i}I'll ask her tomorrow.{/i}"

    ai3 "{i}So sleepy...{/i}"

    scene 8mononight with dissolve

    ai3 "{i}Goodnight, Uncle [player_name].{/i}"

    bi "{i}Goodnight, My Avalon.{/i}"

    if octavia == True:
        label galleryScene3:
        if _in_replay:
            $ player_name = renpy.input("What would you like to name the MC?")
            if player_name.strip() == "":
              $ player_name = "Byron"

        scene 1opnight with fade

        pause

        scene 2opnight with dissolve

        play music "audio/secretly_spying_on_you.mp3"

        pause

        scene 3opnight with dissolve

        pause

        scene 4opnight with dissolve

        pause

        scene 5opnight with dissolve

        ps3 "Hmm. Gone again?"

        scene 6opnight with dissolve

        ps3 "I hope she's alright."
        ps3 "She's not usually--"

        scene 7opnight with dissolve

        ps3 "Huh?"

        scene 8opnight with dissolve

        ps3 "Awful stealthy, aren't we?"

        scene 9opnight with dissolve

        ps3 "But not stealthy enough!"

        scene 10opnight with dissolve

        ps3 "No quarter!"

        scene 11opnight with dissolve

        ps3  "Hiyaa!"

        scene 12opnight with dissolve

        pause

        scene 13opnight with dissolve

        ps3 "Eyaa!"

        scene 14opnight with dissolve

        ps3 "Too slow!"

        scene 15opnight with dissolve

        ps3 "A swift leg sweep..!"

        scene 16opnight with dissolve

        play sound "audio/bodyfallmat.mp3"

        ps3 "And down you go."

        scene 17opnight with dissolve

        ps3 "You won't be needing this mask anymore."

        scene 18opnight with dissolve

        ps3 "Ninja's don't garnish their fingernails with brightly colored nail polish."
        ps3 "Octavia!"

        scene 19opnight with dissolve

        o2 "I almost got you!"

        ps3 "You really didn't."

        o2 "I had you on the ropes, Penny!"

        ps3 "Not even close."

        scene 20opnight with dissolve

        o2 "'Oh, I'm Penny. I'm too cool to get beaten by a ninja.'"

        scene 21opnight with dissolve

        o2 "Ahaha."

        ps3 "You're being so silly tonight."

        scene 19opnight with dissolve

        o2 "I'm really excited to see you."
        o2 "That's all."

        ps3 "You know I knew it was you the whole time, right?"
        ps3 "The eyeliner was a dead giveaway."

        scene 22opnight with dissolve

        o2 "I wanted to look pretty for you."

        ps3 "Well, mission accomplished."

        stop music fadeout 2.0

        o2 "Let me go change into something more comfortable."
        o2 "Meet me in my room."

        ps3 "Okay. Goofball."

        scene 23opnight with fade

        ps3 "This bed is ginormous."
        ps3 "You could fit four people on it."
        ps3 "Why would she need it to be so large..?"

        scene 24opnight

        play music "audio/tomorrows_rain.mp3"

        o2 "Hi, Penny."
        o2 "I hope I didn't make you wait too long?"

        scene 25opnight

        ps3 "Not at all."
        ps3 "I have to say, the new look is really working for you."

        scene 24opnight

        o2 "Thank you, Penny."
        o2 "You're looking rather exceptional today yourself, if I may say so."
        o2 "Did something inspire you to gussy up today?"

        scene 29opnight

        ps3 "I wouldn't say some{b}thing{/b} but rather some{b}one{/b}."
        ps3 "You're not the only one that wanted to look good for tonight."
        ps3 "Also, I had a date with Avalon. Two birds, one stone."

        o2 "How was the date?"

        scene 27opnight with dissolve

        ps3 "She's a very positive person. It's easy to get drawn into her."
        ps3 "I can see why you're spending a lot of time around Avalon."

        scene 24opnight

        o2 "Well, I think tonight should be about you and I."
        o2 "Let me get comfortable first."

        scene 26opnight with dissolve

        pause

        scene 28opnight with dissolve

        o2 "There we are."
        o2 "Much better, don't you think?"

        scene 29opnight
        ps3 "I was hoping you were naked under that robe."
        ps3 "Lucky me."

        scene 31opnight with dissolve

        ps3 "I was feeling a bit underdressed over here."
        ps3 "Being only in my knickers and all."

        scene 30opnight

        o2 "How does it make you feel, Penny?"
        o2 "Does seeing me naked like this inspire certain..."
        o2 "Urges?"

        ps3 "Oh yes, I'm feeling an urge right now."
        ps3 "The urge to..."

        scene 33opnight

        ps3 "Pounce!"
        ps3 "Meow!"
        ps3 "Do you think you can handle this pussy, Octavia?"
        ps3 "Penny the Frisky Feline versus Octavia's Ningina!"
        ps3 "The best part about this fight; no matter what, we're both going to
        be winners."

        scene 32opnight with dissolve

        o2 "That was really clever, Penny!"
        o2 "And insinuating that my vagina practices the ancient art of Ninjitsu,
            that is hilarious!"

        ps3 "I'm just hoping you slash at me with your clitana!"
        ps3 "Wait, that one was awful. I can do better!"

        scene 34opnight with dissolve

        o2 "You know, that's what drew me to you."
        o2 "You're so darn clever, Penny."
        o2 "I really missed you."

        scene 35opnight

        ps3 "H-hey, knock it off."
        ps3 "We can be sentimental later."

        scene 38opnight with dissolve

        ps3 "Come on. Let's just play for now."
        ps3 "Alright?"

        o2 "If that's what you want."
        o2 "I'm sure I can accommodate."

        scene 37opnight with dissolve

        pause

        scene 38opnight with dissolve

        ps3 "Yeah, that's what I want."
        ps3 "I've been without your touch for too long."
        ps3 "I need it."

        scene 39opnight

        o2 "You never took on another lover?"
        o2 "You weren't waiting on me, were you Penny?"

        scene 40opnight

        ps3 "Stop talking and help me out of my underwear."
        ps3 "We can share our feelings after we share our 'feelings'."
        ps3 "And by 'feelings', I mean like, physical touching--"
        ps3 "Just take my panties off, Octavia."

        scene 39opnight

        o2 "You're usually so witty."
        o2 "Is something wrong?"

        ps3 "My head is fuzzy from my underwear being soaking wet."
        ps3 "Less talky, more undressy!"

        scene 41opnight with dissolve

        ps3 "Whoa! Gentle down there!"
        ps3 "You're going to pull my legs off tugging at my panties that hard."

        scene 42opnight

        o2 "Oh, Penny."
        o2 "I nearly forgot how adorable this little pussy is."
        o2 "Has it gotten even smaller?"

        scene 43opnight

        ps3 "Wow, you're so close."
        ps3 "I-I can feel you breathing onto me."

        o2 "Do you like it?"

        ps3 "It's intoxicating."
        ps3 "My brain is spinning."

        o2 "What if I do this?"

        scene 44opnight with dissolve

        ps3 "Gah!"
        ps3 "Nope nope!"
        ps3 "It's too much!"

        scene 45opnight

        o2 "Wha--? Did you just retreat away from me?"
        o2 "What are you doing, Penny?"

        scene 46opnight

        ps3 "It's a tactical retreat!"
        ps3 "I.. want to lead tonight."

        scene 45opnight

        o2 "Is that so?"
        o2 "Well, alright then."
        o2 "What would you like me to do, Penny?"

        scene 46opnight

        ps3 "I want you to come up here and lie down next to me."
        ps3 "And that's an order, General!"

        o2 "So commanding tonight!"

        scene 48opnight with dissolve

        o2 "Well, here I am."
        o2 "Are you satisfied, my little dinosaur girl?"

        scene 47opnight

        ps3 "I knew I shouldn't have told you about the T-rex thing!"
        ps3 "Avalon laughed when I told her too."
        ps3 "And you tease me about it."

        scene 48opnight

        o2 "I don't tease you."
        o2 "I think it's adorable."
        o2 "And if it works for you, that's great!"

        ps3 "You know what else works for me?"

        o2 "Wha--"

        scene 1opscissor with dissolve

        o2 "Oh!"
        o2 "So this is what you were after?"
        o2 "Just be gentle with me, Penny."

        ps3 "Oh no, I don't think so."
        ps3 "You've left me wanting for too long."
        ps3 "Brace yourself!"

        show opscissor

        o2 "Ooh, Penny!"
        o2 "Not so rough, please!"

        ps3 "Just a little rough."
        ps3 "I need this. Mmmff."

        o2 "I'm sensitive tonight."
        o2 "This is too stimulating!"

        ps3 "Are you going to cum for me, Octavia?"

        o2 "Yes! I am!"


        scene 49opnight with dissolve

        o2 "Oh my goodness!"
        o2 "M-my pussy is--"
        o2 "Oooh wow!"

        ps3 "I can feel you trembling!"
        ps3 "You must have really been excited tonight!"

        o2 "I was, I was, I was..."

        scene 50opnight with dissolve

        o2 "Ugn."
        o2 "That was amazing."
        o2 "You destroyed me tonight, Penny."

        scene 51opnight

        ps3 "Well, I'm glad I could bring you to climax but that was too quick."
        ps3 "Did I really get you that aroused?"

        o2 "You did!"

        ps3 "I guess you've kind of missed me, huh?"

        scene 52opnight with dissolve

        o2 "Yes, Penny. I have, actually."
        o2 "I've missed you quite a bit."

        ps3 "You won't have to miss me if you don't leave me again."

        scene 53opnight with dissolve

        o2 "I--!"
        o2 "I'm sorry, Penny..."
        o2 "I really hurt you, didn't I?"

        ps3 "Mhmm."

        scene 54opnight with dissolve

        if persistent.ninjina == False:
            $ renpy.notify("You've unlocked 'Ninjina' in the Scene Gallery on the Main Menu!")
            $ persistent.ninjina = True

        o2 "I just needed time to figure things out."
        o2 "But I should have let you be there for me while I did."
        o2 "I see that now..."

        $ renpy.end_replay()
        jump outro5

    else:
        label galleryScene4:
        if _in_replay:
            $ player_name = renpy.input("What would you like to name the MC?")
            if player_name.strip() == "":
              $ player_name = "Byron"

        scene 1pdnight with fade

        play music "audio/a_quiet_thought.mp3"

        play sound "audio/doorknock.mp3"

        pause

        scene 3pdnight

        d "Oh. Penny?"
        d "What are you doing here?"
        d "Did you forget something?"

        scene 2pdnight

        ps3 "No, I didn't forget anything."
        ps3 "I uhh, needed to talk to you about something."
        ps3 "It's uhm, quite urgent."
        ps3 "It has to do with your lips."

        scene 5pdnight

        d "My lips?"
        d "You mean the kiss earlier?"
        d "You're here, urgently, to talk to me about that?"

        scene 4pdnight

        ps3 "Uhm, yep. Uh huh."
        ps3 "I tasted a hint of almond."
        ps3 "So, that could be-- I mean, it could mean someone is, you know..."
        ps3 "Trying to poison you!"

        scene 5pdnight

        d "Is that so?"
        d "Well, I guess you should come on in and investigate then?"

        ps3 "Uhh, yep!"

        scene 7pdnight with dissolve

        d "So someone is trying to poison me with almonds?"

        scene 6pdnight

        ps3 "Mhmm."
        ps3 "But I could be mistaken!"
        ps3 "I had better, uhm, I had better be sure so..."
        ps3 "I guess you'll have to kiss me again."
        ps3 "Just to make sure you're safe!"

        scene 9pdnight

        d "Oh really?"
        d "You don't sound very sincere, Penny."
        d "Are you playing with me?"
        d "Is this one of your famous pranks?"

        scene 8pdnight

        ps3 "Alright, look, I'll be straight with you."
        ps3 "I'm trying to seduce you with roleplay."
        ps3 "I'm not exactly practiced at this so it's not going well."
        ps3 "If you're not into it, I can just--"

        scene 10pdnight

        ps3 "O-oh?"

        d "I have a confession, Penny."

        ps3 "Do you?"

        d "I put the poison on my lips."

        ps3 "Why would you do something like that?"

        scene 13pdnight with dissolve

        d "Because, Penny, I'm a supervillain."

        ps3 "Plot twist."

        d "And I'm here to stop you from meddling in my villainous affairs."

        ps3 "But I came over here to you though."

        scene 11pdnight with dissolve

        d "Hey, I'm trying!"
        d "I didn't exactly have time to prepare for this roleplay!"

        ps3 "You're doing so good!"
        ps3 "Keep going."

        scene 12pdnight with dissolve

        d "Mmh!"

        scene 13pdnight with dissolve

        d "It's as I thought."
        d "You're immune to my poison!"

        ps3 "Ah, yes, I've built up an immunity to almond-flavored lipstick."

        d "I guess I'll have to find another way to defeat you."
        d "But I've got to prepare."
        d "Hang out in my room down the hall for a minute and I'll be there soon."

        ps3 "Mm, alright."

        stop music fadeout 2.0

        d "And umm... there's a strict 'No Pants' policy in my room."

        ps3 "Of course there is."

        scene 12pdnight with dissolve

        pause

        scene 14pdnight with fadefast

        ps3 "This is very cozy."
        ps3 "Reminds me of my younger days, actually..."

        play music "audio/disturbed_mind.mp3"

        scene 15pdnight

        d "You've foiled my plans for the last time, Detective Penny!"
        d "I'm here to defeat you once and for all!"
        d "Any last words?"

        scene 16pdnight

        ps3 "I am dangerously aroused right now."
        ps3 "I could explode at any second all over your bedsheets."

        scene 17pdnight

        d "Strange last words."

        scene 15pdnight with dissolve

        d "But I'll be sure to put them on your tombstone!"
        d "After I, you know, put you in the ground!"
        d "As someone of my considerable villainous power is capable of doing!"

        scene 16pdnight

        ps3 "Wait, wait."
        ps3 "What's your supervillain name and powers?"

        scene 17pdnight with dissolve

        d "I'm Dark Whisper, the sexy and deadly seductress."
        d "And my superpower is, well, the kiss of death, of course!"

        scene 18pdnight with dissolve

        d "You're cornered, Penny."
        d "I've got you right where I want you."
        d "There's no escape this time."
        d "You might as well just surrender."

        scene 19pdnight

        ps3 "Oh I never surrender."
        ps3 "And I'm never cornered."
        ps3 "But sometimes I like to make my opposition think I am."

        scene 20pdnight

        d "Well, there's no way out behind you."
        d "And there's no way out beside you."
        d "The only way you're leaving here alive is, well..."
        d "Through me."

        ps3 "Okay."

        scene 21pdnight

        d "Eh?"

        scene 22pdnight with dissolve

        d "Whoa!"

        scene 23pdnight with vpunch

        d "Oof!"

        scene 24pdnight with dissolve

        d "Hot damn!"
        d "That was awesome!"
        d "I think I just came."

        ps3 "Now, Dark Whisper, there's a strict 'No Pants' policy."
        ps3 "So I'm afraid I'm going to have to remove your clothes for you."

        stop music fadeout 2.0

        d "Fuck. Yes."

        scene 25pdnight with fadefast

        play music "audio/no_goodbyes.mp3"

        pause

        scene 26pdnight with dissolve

        d "You're going to make me leave the mask on, huh?"

        ps3 "You're damn right I am."
        ps3 "Now there's a position I'm rather fond of."
        ps3 "Have you ever scissored with a girl before?"

        d "Nope. But it sounds exciting. Show me."

        scene 25pdnight with dissolve

        pause

        scene 26pdnight with dissolve

        ps3 "Okay."

        scene 27pdnight with dissolve

        ps3 "So this is one of my favorite positions."
        ps3 "I'm going to press myself into you and slide around."
        ps3 "How does that sound?"

        scene 28pdnight

        d "This moved forward really fast!"
        d "But alright, yeah, it sounds..."
        d "Interesting."

        scene 1dpscissor

        ps3 "Let me know if it gets too intense."

        d "A-alright."

        show dpscissor with dissolve

        d "Oh, Penny!"
        d "This is interesting!"
        d "Really, really interesting!"

        ps3 "Feels good, right?"

        d "Ooh, fuck yes!"
        d "Keep going!"

        ps3 "I can't believe how drenched you are."
        ps3 "It's soaking wet between us!"

        d "I'm..!"
        d "I'm about to..!"

        ps3 "Seriously??"

        d "Yes, yes, {b}yes{/b}!"

        scene 29pdnight

        d "I'm cumming!"
        d "Stop stop!"

        ps3 "I can feel your vagina quivering!"
        ps3 "Wow!"
        ps3 "You're finishing hard!"

        scene 30pdnight with dissolve

        d "I can see why you like that position."
        d "That really worked for me!"
        d "God damn!"

        ps3 "Right?"
        ps3 "I can't believe you finished so quickly though."
        ps3 "I didn't quite have time myself."

        scene 31pdnight with dissolve

        d "Well, I guess I still have some work to do then."
        d "How about it, Penny?"
        d "My turn to pick a position?"

        scene 32pdnight

        ps3 "Oh, such the generous lover!"
        ps3 "Well how can I say no to an offer like that?"
        ps3 "Just don't be gentle with me."
        ps3 "I like it a little rough!"

        scene 33pdnight

        ps3 "I do like to cuddle after though."
        ps3 "I'm into that cheesy shit."

        d "Just don't flip me over again while I'm trying to position you."

        ps3 "Right on."

        scene 1dpfingering with dissolve

        d "You've got the tiniest little pussy, Penny."
        d "It's kind of adorable."

        ps3 "T-thanks, just what I love to hear when I'm spread eagle like this."
        ps3 "Maybe focus on the task at hand?"

        d "Nice pun."


        scene 3dpfingering with dissolve

        d "Alright, I'm going in!"
        d "Let me know when you're about to climax so I can pull out
            before you clinch my fingers off inside of you."

        ps3 "That's dramatic."
        ps3 "But I probably would."

        show dpfingering

        ps3 "Ugn, yes!"
        ps3 "Faster!"
        ps3 "Careful with the nails!"

        d "Sorry!"
        d "Stop clenching so hard!"

        ps3 "I'm not!"

        d "Seriously? You're that tight??"

        ps3 "Oh, this is good. Keep going!"

        d "Are you--"

        ps3 "Yes! Keep going!"
        ps3 "Gaah!"

        scene 35pdnight with vpunch

        ps3 "I'm done, I'm done!"
        ps3 "Ah, ooh!"

        d "Fuck, that was sexy."

        scene 36pdnight with dissolve

        ps3 "Hnyaa..."

        d "Not bad, huh?"

        ps3 "Not bad at all."
        ps3 "Color me impressed."

        scene 37pdnight with dissolve

        d "So, I have to ask..."
        d "Was this just a one night stand?"
        d "It's cool if it was but, I don't know, maybe..."

        ps3 "I don't know what the hell was going through my mind when I came over."
        ps3 "But I'm really glad I did."
        ps3 "I haven't had this much fun in a long time!"
        ps3 "So, yeah, I don't know. Let's go on a date or something sometime."

        if persistent.darkwhisper == False:
            $ renpy.notify("You've unlocked 'Dark Whisper' in the Scene Gallery on the Main Menu!")
            $ persistent.darkwhisper = True

        d "Okay, yeah. That sounds fun. I'll even wear the mask for you, if you want."
        d "You wanna... stay the night?"

        ps3 "Only if we can keep the 'No Pants' policy."

        stop music fadeout 2.0

        d "Fuck pants!"

        $ renpy.end_replay()
        jump outro5

    label outro5:

    jump act_six_s

    play music "audio/licorice_song.mp3"

    scene 9xianne5 with fade

    x "So?"
    x "What'd you think?"
    x "That was a pretty hot sex scene, huh?"

    scene 8xianne5 with dissolve

    x "There's, uhm, three more sexy scenes."
    x "You can unlock them by playing through the other paths."
    x "You know, if you want."

    scene 10xianne5 with dissolve

    x "Unfortunately, you won't be seeing me do the Outro anymore."
    x "I got fired so this is my last one."
    x "Apparently, Lockheart wasn't so pleased with the sex scene I made."
    x "I guess there were some complaints about Pteri, the flying cock monster."

    scene 3xianne5 with dissolve

    x "But it's fine. I have my own story to get back to anyway!"
    x "We sure hope you enjoyed this update."
    x "And remember! There are four unique paths and they all have something
        to offer."
    x "So if you didn't get your fill of Avalon, be sure to try another path!"

    scene 6xianne5 with dissolve

    x "We... know this update took a while. We won't make you wait this long again."
    x "It was important for us to both learn how to do animations and to get out
        a decent amount of sexual content."
    x "But we did want to warn you that the next Act is going to be pretty heavy."
    x "We're going to focus on [player_name] and his trauma next."

    scene 4xianne5 with dissolve

    x "And there's gonna be a huge fire!"
    x "You're gonna have to choose who lives and who dies!"
    x "Because... reasons!"

    scene 3xianne5 with dissolve

    x "Nah, I'm just pullin' your chain."
    x "We over here on Lockheart's team like that cheesy, happy ending crap."
    x "There's two acts left to go; Act 6 and Act 7."

    scene 5xianne5 with dissolve

    x "Thank you so much for taking the time to enjoy Avalon!"
    x "It means the world to us to be able to write these visual novels."
    x "If you want to help us out, please consider supporting us on Patreon."
    x "You can also support Lockheart simply by letting him know how much you loved Avalon!"
    x "He's like an infant, he needs a lot of attention."
    x "So be sure to come hang out with us on Discord!"

    scene 7xianne5 with dissolve

    x "And that concludes Act 5!"
    x "Peace out, people!"

    return

    scene 2xianne5 with fade

    x "Oh my gosh!"
    x "It's time!"

    scene 3xianne5 with dissolve

    x "Ok, so, this is the end of the current content."
    x "But!"

    scene 8xianne5 with dissolve

    x "I umm, sort of made a little fantasy scene myself."
    x "It's not very long, but it's got a really hot animation."
    x "I worked pretty hard on it."

    scene 9xianne5 with dissolve

    x "Do you..."
    x "Do you wanna see it?"

    menu:
            "{b}Would you like to see Xianne's fantasy scene with Sun Mei?{/b}"
            "Umm, Fuck Yes!":

                x "Ehehe."
                x "Enjoy..."

                jump xsunmei

            "Nah, I don't like when cute girls bang.":

                scene 10xianne5 with dissolve

                x "Umm, okay."
                x "Whatever."
                x "I just worked really hard on it. But no, it's fine."
                x "It's just my feelings that you hurt."
                x "No big deal."

                jump xianneout

    label xsunmei:

    jump act_six

    scene 1xsunmei with fade

    play music "audio/licorice_song.mp3"

    x "Sun Mei."
    x "Wake up, Sun Mei."

    scene 2xsunmei with dissolve

    sm "Mm?"

    scene 3xsunmei with dissolve

    sm "What's going on?"

    scene 4xsunmei with dissolve

    sm "Xianne!?"
    sm "Is that you??"

    scene 5xsunmei

    x "Yeah, it's me."
    x "I came to visit you."

    scene 6xsunmei

    sm "You look so different!"
    sm "What happened to your skin color?"
    sm "You look like a person now."

    scene 5xsunmei

    x "It's a long story."
    x "But don't worry about that!"
    x "We have more important things to attend to."
    x "Like that pink little pussy of yours."

    scene 6xsunmei

    sm "Really??"
    sm "You came to fuck me?"
    sm "Ooh, please say yes!"

    scene 7xsunmei

    x "You're damn right I did."
    x "And I brought our mutual friend with me, too!"

    sm "Pteri!?"

    x "Yup."
    x "Come here, Pteri."

    scene 8xsunmei with dissolve

    pause (.3)

    show 9pteri with dissolve

    sm "Hey, Pteri!"
    sm "I missed you!"
    sm "Don't go easy on me today, okay?"

    show 11pteri with dissolve

    x "You heard the lady!"
    x "No mercy!"

    scene 13xsunmei with dissolve

    pause (.3)

    scene 7xsunmei with dissolve

    x "Alright, sit up so we can get started."

    sm "Okay!"

    scene 14xsunmei with fadefast

    sm "Oh!"
    sm "Hey, little buddy!"
    sm "You seem eager today."

    scene 16xsunmei

    x "I think he really missed you."
    x "Apparently, you just have the tightest little pussy."
    x "He can't get enough of you!"

    scene 15xsunmei with dissolve

    sm "Aw."
    sm "You know just how to flatter a girl, huh?"

    scene 18xsunmei

    sm "You look so big today!"
    sm "Have you grown?"

    x "He has!"
    x "Let's get some light in here."

    play sound "audio/snapfinger.mp3"

    scene 19xsunmei with dissolve

    sm "You really have grown."
    sm "I guess Xianne is taking good care of you."

    x "Enough flirting with Pteri."
    x "Xianne needs kisses!"

    scene 20xsunmei

    sm "Oh, mm!"
    sm "Mhmm."

    scene 21xsunmei

    sm "Mm!"

    scene pteri0 with dissolve

    sm "Ah!"
    sm "H-he's pushing in!"
    sm "He.. he's too big now!"

    x "Oh damn, he kind of is, isn't he?"

    show pteri

    sm "Oh. Oh! OOH!"
    sm "Oh fuck!"
    sm "Oow!"

    x "God damn, Pteri."
    x "Don't break her."

    sm "He's going to tear me in half!"
    sm "Oooh!"
    sm "I'm going to..!"
    sm "I'm going to explode!"

    scene 23xsunmei with dissolve

    sm "Aah!"

    x "Holy crap!"
    x "You squeezed so hard, you launched Pteri!"

    show 24pteri

    x "Are you alright??"
    x "Whew, yeah, you look alright."

    scene 26xsunmei

    x "I hope you enjoyed your dream, Sun Mei."
    x "Remember to wash your sheets tomorrow!"
    x "Bye bye, Cutie."
    $ renpy.end_replay()
    jump xianneout

    label xianneout:

    scene 6xianne5 with fade

    x "Alright, I know a lame fantasy scene isn't the same as canon sex scenes
        in the novel."
    x "We're building up to some really sexy stuff in Avalon."
    x "So..."

    scene 5xianne5 with dissolve

    x "Please just give us one more release!"
    x "The next one is gonna have a lot of hot stuff in it!"
    x "Promise!"

    scene 3xianne5 with dissolve

    x "Quite a few people have really enjoyed Avalon."
    x "But some people have expressed a strong dislike for it, too."
    x "The negative comments have been extremely taxing on Lockheart."
    x "So if you like Avalon, be sure to tell him!"
    x "He could really use it!"

    scene 8xianne5 with dissolve

    x "And if, you know, you think I'm sexy."
    x "Or whatever."
    x "You can see more of me in Myrabelle's novel."
    x "It's available to Patrons on Patreon."

    scene 6xianne5 with dissolve

    x "We... can't give a good estimate on the next release date."
    x "This one could take some time."

    scene 3xianne5 with dissolve

    x "Instead, we're going to try to keep you updated with our progress on Patreon."
    x "So if you want to know how much we have left to do, you can find out there!"

    scene 7xianne5 with dissolve

    x "Thanks for enjoying Avalon!"
    x "We'll see ya next time!"


    return
