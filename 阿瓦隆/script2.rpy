

## This will be the beginning of Act Two.

label act_two:

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

    jump act_two_s

label act_two_s:

    stop music fadeout 2.0

    scene avalon with fade

    if persistent.actTwo == False:
        $ renpy.notify("You've unlocked Act Two in Act Select on the Main Menu!")
        $ persistent.actTwo = True

    pause

    scene avalonacttwo with dissolve

    pause

    scene 2daytwowake with fade

    ai "{i}Uncle is asleep in the chair. It must be so uncomfortable.{/i}"
    ai "{i}This is the second day in a row I've kept him from a
        good night sleep in his own bed.{/i}"
    ai "{i}It's wonderful to have someone so devoted to caring for me again for
    a change, but I feel awful that I'm putting him out like this.{/i}"

    scene 1daytwowake


    ai "{i}I'd like to let him sleep longer but he looks pretty
    uncomfortable in that chair.{/i}"

    play music "audio/your_hand_in_mine.mp3"

    a "Um... Uncle [player_name]?"
    ai "{i}He's really out! I'll have to speak louder.{/i}"
    a "Wake up, Uncle!"

    scene 4daytwowake with vpunch

    b "Donut waffle!"
    b "Where... erm. What's going on? Avalon?"

    scene 3daytwowake

    a "Good morning! I didn't mean to startle you, Uncle."
    a "You sleep like the dead. I thought maybe you {b}were{/b} dead!"

    scene 6daytwowake

    b "Oh, good morning. I know, I sleep pretty hard."
    b "I tried to stay awake longer but at a certain point, my eyelids felt like
     they had bowling balls hanging from them."

    a "Er... wait, what? If you had bowling balls hanging from your eyelids,
    wouldn't the weight of the balls just rip your eyelids right off?"

    b "Ehem. Anyway, did you sleep well?"

    scene 3daytwowake

    a "I did. This bed is just as comfortable as I remember."
    a "Having you close by actually put my mind at ease too. I didn't have any
    more nightmares."

    scene 5daytwowake with dissolve

    a "I feel terrible though. You shouldn't have had to sleep in that uncomfortable
    chair just for me."
    a "I do appreciate it though. A lot! Thank you, Uncle."

    scene 6daytwowake

    b "Don't even worry about it. I can sleep anywhere. I even slept on a rollercoaster
    once."
    b "Or I passed out from fear on one. Who can say for sure?"

    scene 3daytwowake

    a "I was there that day, Uncle! I think that was the first time I'd seen a grown
    man cry."
    a "What's a donut waffle, by the way?"

    scene 6daytwowake

    b "Only the best thing ever!"
    b "I fried up a donut with a waffle maker once."
    b "Then I added a little bit of syrup."

    scene 4daytwowake2 with dissolve

    b "It was the most delicious thing I've ever eaten."
    b "But the sheer amount of sugar in that abomination should have killed me."
    b "I'm pretty sure my pancreas cried a little bit that day..."
    b "I can only dream about its deliciousness now."
    b "Because I'm pretty sure if I ever ate another one,"
    b "I'd slip into a sugar coma the likes of which I may never wake from."

    scene 5daytwowake

    menu:
            "{b}Additional Dialogue Choice{/b}"

            "Fitness":
                a "I thought you were all about fitness, Uncle?"

                b "Uhh, yeah, fitn' this whole waffle in my mouth!"

            "Diabetes":
                a "Wow! Something like that should come with its own insulin shot."
                a "And, like, a plastic surgeon's business card."
                a "You know, for liposuction."

    a "Anyway..."

    scene 4daytwowake2

    b "You were pretty shaken up last night, Avalon."
    b "After you told me what happened to you, I didn't realize how bad it--"
    b "Er, I mean, I think we should spend some time today helping you recover."
    b "Whatever it takes, I want to help you."

    scene 5daytwowake

    a "I have gotten a lot better. After it happened, I felt like a different
    person. It just changed me somehow, like I was... shattered."
    a "I wanted to crawl into a dark hole and never come out. That's why I changed
    my hair and my wardrobe. I guess I wanted to look like how I felt."
    a "After a few months, I thought I was getting better. I've tried so hard to pull myself out of
    the hole and out of the darkness."
    a "But then I have an episode like I did last night and I feel that gravity
    of despair and hate pull me back in."

    scene 4daytwowake2

    b "I... I know the darkness, Avalon. I know it all too well. I should have
    protected you from it. I'm sorry. I'm so sor--"

    a "Don't. Don't do that. It wasn't your fault."

    scene 5daytwowake

    a "What's done is done. You're here now and I want to focus on the future."

    scene 3daytwowake with dissolve

    a "Hey! There's a new burger joint not too far away. How about we go
    have breakfast there!"
    a "I still have that forty four dollars so I'm happy to pay!"

    scene 6daytwowake

    b "Yeah, that sounds great. But save your money, Avalon. I'll take
    care of breakfast."
    b "Before we eat, how about we go get some of your stuff from your mom's house?"

    a "Sounds like a plan."

    stop music fadeout 2.0

    b "I'll let you get changed. Let me know when you're ready."

    ## The phone call will be based on whose route we're on.

    if octavia == True:
        jump octavia_call

    else:
        jump dallas_call

    label octavia_call:

    scene 7daytwowake with fade

    bi "{i}Alright, I'm all changed and ready.{/i}"
    bi "{i}I'll give Octavia a call and see if she is available
        to join us for brunch. {/i}"
    bi "{i}She's a fascinating woman who has captivated my curiosity. She also has
    experience with helping people.{/i}"
    bi "{i}If anyone can assist me with Avalon's recovery, it's certainly her.{/i}"

    scene 8daytwowake with dissolve

    bi "{i}The phone is ringing. Let's hope that she answers. It's possible
    that she's working today.{/i}"

    play music "audio/tomorrows_rain.mp3"

    o "This is Octavia."

    b "Hey, it's [player_name] from the library. We went out for coffee yesterday."

    o "Oh [player_name], how are you?"

    scene 10daytwowake with dissolve

    b "Hey, I'm doing well but Avalon had a nightmare last night. She woke up screaming
    and it... Well, frankly, it scared the hell out of me."
    b "I think I'm out of my league here. I really have no idea how to help her."

    o "Oh that's awful, [player_name]. Is she doing better now? Did she get enough
    sleep?"

    b "She was inconsolable for a while but when she finally fell asleep, she seemed
    to sleep soundly enough."
    b "I stayed the night in a chair next to her bed. I didn't think she should be alone."

    o "You did the right thing, [player_name]. It seems her trauma from the assault
    is quite severe."

    scene 8daytwowake with dissolve

    b "She actually told me what happened and yes, it's pretty bad."
    b "I was hoping we could talk more about it over brunch?"
    b "Ava and I have a quick stop to make and then we're heading to the burger
        restaurant."
    b "I thought maybe we could brainstorm on an activity to do today to take
        her mind off things."
    b "I hope it's not too terribly inconsiderate, I know you've probably got your own
        things to deal with."

    o "I'd love to help, [player_name]. And a burger sounds great!"
    o "I'm not an expert when it comes to dealing with trauma, but I'm sure together
    we can find some ways to help her."
    o "You may consider a therapist as well. A professional would be much more
    capable than either of us."

    scene 10daytwowake with dissolve

    b "That's a good idea. I'll consider it. I'm not exactly sure how she would
    respond to that idea though."
    b "Perhaps we can try to help her ourselves first?"

    o "Let's see how today goes. I haven't met her yet so I can't say anything
    for certain."

    b "Right, of course. You don't work today?"

    o "[player_name], I should have mentioned this before. I'm not a librarian."

    scene 8daytwowake with dissolve

    b "Oh, I apologize. I just assumed."

    o "I suppose I did lead you to believe I worked there."
    o "I was curious about you and your situation so much so that I may
    have avoided talking about myself to focus on you."
    o "I'm rather bored of my own story but none the less, it was wrong of me
    not to correct your misunderstanding."

    scene 10daytwowake with dissolve

    b "You're a curious woman, Octavia. It's refreshing in a way."
    b "I have honestly never met someone as unique as you."
    b "If you're not a librarian, what do you do for work?"

    o "You're sweet, [player_name]. My story is rather bland and uninteresting,
    I'm afraid. But I'd be happy to tell you more about myself over brunch?"

    scene 9daytwowake with dissolve

    b "That sounds great, I'm excited to learn more about you. We're going to be
    there around eleven o'clock."

    o "Wonderful! I'll be sure to be punctual. Bye for now!"

    stop music fadeout 2.0

    b "See ya then."

    scene 7daytwowake with dissolve

    bi "{i}That could not have gone any smoother. Normally I'm nervous around new people
    but she has a way of putting me at ease.{/i}"
    bi "{i}I'm excited to learn more about her.{/i}"

    scene 11daytwowake with dissolve

    bi "{i}I did not rest well at all last night. My body feels so heavy right now.{/i}"
    bi "{i}Perhaps while Avalon gets ready, I'll rest my eyes.{/i}"
    bi "{i}But only for a moment...{/i}"

    jump byron_sleeping

label dallas_call:

    scene 7daytwowake with fade

    bi "{i}Alright, I'm all dressed and ready to go. {/i}"
    bi "{i}Let's give Dallas a call and see if she's available for brunch.{/i}"
    bi "{i}I hope her phone number is still the same one she called me
        from a few years ago.{/i}"
    bi "{i}She wanted to throw a birthday party for Avalon so we collaborated
        on something together.{/i}"
    bi "{i}Wow, I'd forgotten all about that...{/i}"

    scene 8daytwowake

    bi "{i}It's ringing. That's a good sign.{/i}"

    play music "audio/disturbed_mind.mp3"

    d "Good morning, Sunshine! I didn't expect to hear from you so soon."

    b "Hey, Dallas. I didn't interrupt you at work, did I?"

    d "Nope! I'm off today. What's up?"

    b "Avalon had an episode last night. I was hoping I could take you up on your
    offer last night?"
    b "Maybe we can work together and figure out how to help her recover?"

    d "Of course! I haven't got any plans today. Did you have something in mind?"

    b "We're going to meet up at the new fast food place at eleven. Join us?"

    d "I'll be there."

    scene 9daytwowake with dissolve

    b "Hey, what the hell happened to you last night? You came out of the bathroom
    with your breasts hangin' out, spoutin' nonsense."

    d "Oof, that spanking scrambled my brain, [player_name]!"
    d "You should have seen your face though. It looked like your brain malfunctioned
    and you were about to stroke out!"

    b "I was reasonably shocked, yes. But only because it caught me off guard!"

    d "So what did you think?"

    b "Of your being crazy?"

    d "No! Of my breasts, doofus!"

    scene 10daytwowake with dissolve

    b "Uhh, well. I didn't get a real good look."
    b "I think I'd have to see them again. You know, up close."

    d "Uh huh. Well maybe you'll get the chance, [player_name]."
    d "But enough about my breasts, ya pervert! How did you handle the situation
    with Avalon?"

    scene 8daytwowake with dissolve

    b "I stayed with her until she fell asleep. And then I slept in the chair next
    to her bed."
    b "I don't know what to do, Dallas. I don't know how to help her."

    d "She's actually gotten a little better over the past few months. Perhaps our
    support will be enough to push her in the right direction."
    d "If not, we might need to think about a counselor. You know, like the one
    I had."

    b "That might not be a bad idea. But you're right, we should do what we can first
    before we put our trust in a stranger."
    b "We can do some more brainstorming later. We're going to pick up some of her
    things from her moms house first. She's going to stay with me for a while."
    b "Meet us at the burger joint at eleven."

    d "Right on, [player_name]. See you there!"

    b "Bye, Dallas."

    stop music fadeout 2.0

    scene 7daytwowake with dissolve

    bi "{i}Maybe Dallas will have some ideas on activities that will help Avalon recover.{/i}"
    bi "{i}I've known her for a while through Avalon. She's always been a bit flirtatious
    with me but it used to be more innocent.{/i}"
    bi "{i}Now that she's grown, it feels as if she's flirting a bit more intensely.{/i}"
    bi "{i}I do find her exceptionally fun to be around. Perhaps I should continue
    to try to develop things with her..?{/i}"

    scene 11daytwowake with dissolve

    bi "{i}Putting that thought aside, I did not sleep well at all last night. My
    mind is clouded by exhaustion.{/i}"
    bi "{i}Perhaps I could rest my eyes for a moment while Avalon gets ready...{/i}"

    label byron_sleeping:

    scene 12daytwowake with fade

    ai "{i}I'm all done changing and Uncle told me to come get him when I was done.{/i}"
    ai "{i}I don't want to walk in on him while he's indecent but he's had ample time
    to get ready himself.{/i}"
    ai "{i}Perhaps he left the door open to let me know he was ready?{/i}"

    play music "audio/temporary_solution.mp3"

    scene 13daytwowake with dissolve

    ai "{i}I'll just take a quick peek... {/i}"
    ai "{i}What's this? He's sleeping!{/i}"
    ai "{i}He must be so tired from sleeping in that chair. Now I feel even
    worse for making him feel like he needed to sleep close to me.{/i}"

    scene 14daytwowake with dissolve

    ai "{i}He looks so peaceful. As if he were a bear in hibernation.{/i}"
    ai "{i}I'd love to let him sleep longer but I'm starving! Perhaps I can
    wake him up gently somehow.{/i}"
    ai "{i}When I was younger, I used to cuddle up in his arms. He'd tell me
    stories about my father or we'd just watch TV together.{/i}"
    ai "{i}I bet he'd like to be reminded of those times. Maybe just a quick cuddle!{/i}"

    scene 15daytwowake with dissolve

    ai "{i}Let me get my leg over him so I can get on the bed-- er, wait, what am I doing? I didn't plan
    this out very well. I should have gone around.{/i}"
    ai "{i}Well it's too late now! He's too big for me to get over him. I guess I'll just
    sit on him-- Oh shit, I'm wearing a skirt!{/i}"
    ai "{i}He's going to see my panties!{/i}"

    scene 20daytwowake with vpunch

    b "Ooof! What's going on? Am I under attack!?"

    scene 29daytwowake

    ai "{i}Oh no! I can't sit up or else he'll see my panties! But bent over like this,
    I'm way too close to his face!{/i}"
    ai "{i}He must be so weirded out right now!{/i}"
    ai "{i}I have to play it off, just be cool as a cucumber, Avalon!{/i}"
    ai "{i}Wait, no, don't think about cucumbers while sitting on top of him!{/i}"

    scene 22daytwowake

    b "What are you doing, Avalon? Why are you on top of me?"

    scene 17daytwowake

    a "You promised me breakfast and then you fell asleep. As punishment, I decided
    to sit on you!"
    a "Don't make promises you can't keep or else you'll have to face the wrath of
    my awesome weight! All one hundred and ten pounds of it!"

    scene 25daytwowake

    b "One hundred and ten pounds? Are you training to become a sumo wrestler?"

    a "Careful, Mister!"

    b "You came down so hard on me, I think you ruptured one of my kidneys!"
    b "Consider me properly repremanded. I can see dialysis in my future now."


    scene 18daytwowake

    a "Don't be so dramatic, Uncle! You're huge! I doubt a little girl like me could
    actually do any harm to a big ol' bear like you."
    a "I'm surprised you even felt me on top of you!"

    scene 25daytwowake

    b "A woman like you is what men are most vulnerable to."
    b "You could destroy a guy like me without even trying!"

    scene 18daytwowake

    a "How? I'd need like, a rocket launcher or something to take you out!"
    a "I'm pretty sure you need a permit for one of those."

    scene 25daytwowake

    b "I didn't mean literally, Dorkface."
    b "The worst pain for any man always comes from a beautiful woman."

    scene 19daytwowake

    a "You think I'm beautiful?"
    a "Stop it, Uncle. You're going to make me blush."

    scene 20daytwowake

    b "That's all you heard from that? You need to open up your ears better, Avalon."

    scene 21daytwowake

    pause (.5)

    scene 20daytwowake

    b "Shit, sorry! I didn't mean to touch your legs."

    scene 17daytwowake

    a "It's alright, you can touch my legs if you want."
    a "I shaved them this morning while you slept like a sloth."
    a "They're as smooth as butter!"

    scene 21daytwowake

    b "Oh are they? Let me feel."
    b "You're right, Avalon. They're very smooth! Like a cactus or a porcupine."

    scene 31daytwowake

    pause (.5)

    scene 30daytwowake

    a "You jerk! You know I have silky smooth skin. Don't even lie, Uncle!"

    b "I was kidding! They're butter smooth and very soft! You must moisturize."
    b "You wanna feel my legs?"

    a "Oh I've felt your legs before, Uncle. They're like sandpaper! How do you
    live like that?"

    scene 19daytwowake

    a "But thank you for the compliments!"

    scene 18daytwowake with dissolve

    menu:
        "{b}Additional Dialogue Choice{/b}"
        "Regular Cheese":
            a "I guess I'll have to start calling you... Chester Cheesy!"
        "Good Cheese":
            "*In an Italian accent.*"
            a "It was a Gouda compliment!"
        "Super Cheese":
            a "Your compliments are so cheesy, I think I'll start calling you... Captain Cheesypants!"

    scene 25daytwowake

    b "Don't mention cheese right now, Avalon. I'm starving!"
    b "How about you hop off me so we can go eat?"

    scene 19daytwowake

    a "I've been trying to avoid telling you this but, um, I can't."
    a "I forgot I was wearing a skirt when I sat on you."

    scene 23daytwowake

    b "Oh. Why is that a proble--"

    scene 22daytwowake with dissolve

    b "Oh! If you get up, I'll see--"

    scene 25daytwowake with dissolve

    b "Okay, yep, I understand now."
    b "How about I close my eyes so you can dismount?"
    scene 19daytwowake

    a "Uhm... Okay."

    scene 17daytwowake with dissolve

    a "But no peeking, Mister! I'm trusting you!"

    scene 15daytwowake

    b "Okay, my eyes are closed and I've even put my arm over my face for
    added assurance."

    scene 14daytwowake with dissolve

    a "Okay, I'm all done. Thank you for not peeking, Uncle."

    stop music fadeout 2.0

    b "You're welcome, Avalon."

    scene 1sharolhouse with fade

    a "Are you coming, Uncle?"

    b "Give me a moment. It's been a while since I've been here. To be honest,
    I'm dreading seeing Sharol."
    b "Let's get this over with quickly, alright?"
    b "And don't give your mom anything sharp!"

    scene 2sharolhouse with dissolve

    a "Uncle [player_name], why do you still have the beat-up ol' junker truck?"

    b "She's not a junker. That's a fresh paint job!"

    a "Yeah but can't you afford something better? You're doing well financially
    now, aren't you?"

    b "It's not important to me to have a fancy vehicle. I don't even much care
    for driving."
    b "To me, a car is just a tool. The same as a wrench or a hammer."
    b "I just need something to get me from 'Point A' to 'Point B'."
    b "That old truck does that just fine. And besides, that truck has memories
    attached to it."

    a "Fair enough."

    scene 3sharolhouse with dissolve


    a "I wonder if Mom is going to be glad I'm not living under her roof anymore?"

    b "Well, before we had our falling out, you were the one taking care of her
    every day and not the other way around, Avalon."
    b "I'm sure she will miss you when you're gone, if not only because she
    doesn't have someone to grocery shop for her anymore."
    b "She wasn't so bad a decade ago. She just slowly got worse and worse."

    a "She's been drinking more since you left. She gets ornery when I ask her
    to slow down on it."
    a "And she's been dating a lot more. Well, I don't know if you'd call it dating..."

    b "I know what you mean. Booty calls, right?"

    a "Mhmm."

    b "Well, let's get this over with."

    scene 4sharolhouse

    play sound "audio/doorknock.mp3"

    b "*Knock* *Knock*"
    b "Sharol? You in there?"

    scene 6sharolhouse with dissolve

    play music "audio/natural.mp3"

    r "Aw shoot, sorry 'bout this! Sharol dun asked me ta get tha door."
    r "She's a tad busy with her TV show."

    scene 5sharolhouse

    bi "{i}Of course she has some boy toy over! Dammit!{/i}"

    b "I'm just here to collect some things for my niece. I don't want any trouble."

    scene 7sharolhouse

    r "No trouble at all, friend! I'm Randall. I tend the farm down the road."
    r "You must be Sharol's brother?"

    scene 8sharolhouse

    bi "{i}I can feel Avalon's hand on my arm. She must be nervous.{/i}"


    b "My name is [player_name]. As I said, I'm just here to collect some things.
    I won't be long."

    scene 9sharolhouse

    r "You're welcome to stay as long as you'd like, I'm sure!"
    r "Though Sharol been hittin' the sauce pretty early this mornin'."

    b "I had a feeling she would be..."

    scene 7sharolhouse with dissolve

    r "Well hey, I love makin' new friends! And since we're already acquaintances
    now, we're half way there!"
    r "I best get back to my farm 'fore the chicken's start hasslin' my Lillian again."

    scene 8sharolhouse

    b "Lillian? You must be awfully popular with the ladies, Randall..."

    scene 9sharolhouse

    r "Lillian is my heifer. She likes me well enough, I suppose! Mostly 'cause
    I keep her fed and milked."

    scene 11sharolhouse with dissolve

    r "Anyhow, why don't you two come on in and I will head on out."
    r "Nice meetin' you folks! Hope to see you again!"

    scene 10sharolhouse

    b "I appreciate it, Randall. See ya around."

    scene 12sharolhouse with dissolve

    r "Bye, you two!"

    b "H-hey. Did you forget your shirt?"

    r "Had ta throw it away. Sharol got awfully rough last night, if ya know what I'm sayin'."
    r "Woo dog!"

    stop music fadeout 2.0

    scene 13sharolhouse with dissolve

    play sound "audio/doorclose.mp3"

    b "Are you alright, Avalon? I could feel your hand on my arm. Were you
    a bit nervous?"

    a "Hmm?"

    scene 14sharolhouse with dissolve

    a "I've tend to despise the men mom brings over. I usually just lock myself
    in my room now when she has a guy in the house."
    a "But Randall seemed nice. I haven't seen her bring over anyone like him before."

    b "He certainly seems like an interesting character. When he opened the door, I
    was just sure there was going to be trouble. "
    b "Now I feel like a jerk to make such an assumption!"

    a "You weren't unpleasant though, Uncle. You were polite."

    b "You think so? Perhaps we'll see him again and we'll introduce ourselves properly."
    b "Why don't you grab what you want from your room? We'll go get breakfast
    as soon as your all packed and ready to go."

    scene 15sharolhouse

    a "Okay, I'm also going to change my clothes so I'll be a moment. But I'll be back as
    soon as I can!"

    scene 17sharolhouse

    play music "audio/evil_aliens.mp3"

    s "Well, if it ain't my baby brother in the flesh. I haven't seen you in so
    long, I thought maybe you were dead."
    s "I guess fate ain't so kind, is it?"

    scene 18sharolhouse with dissolve

    s "You know you ain't welcome here, [player_name]. So what the fuck are you doing
    in my home?"

    scene 20sharolhouse

    b "Are you seriously drunk already? It's still morning, ya fuckin' booze hound!"

    scene 21sharolhouse

    s "Who the fuck are you to judge me? And in my own house, no less!"
    s "And you brought Avalon, didn't you? I told you, and I told her, she ain't
    welcome here if she's going to continue being a little cunt!"

    scene 22sharolhouse

    b "Hey! Watch it! I don't care how drunk you are, you don't call her that!"

    scene 23sharolhouse

    s "She's my daughter, I'll call her whatever I want. Now you better have a real
    good reason for bein' in my house."
    s "I am seconds away from callin' the cops to have 'em drag your dumbass
    off my propery!"

    scene 22sharolhouse

    b "I'm giving you what you want, Sharol! I'm removing Avalon from your home."
    b "She's grabbing some of her things and she's going to come stay with me
    until she gets on her feet."

    scene 25sharolhouse

    s "Not for free, you ain't. That ain't her stuff up there, [player_name]."
    s "That's my stuff! You want it, you gotta pay for it."

    b "Fine. How much do you want?"

    s "One thousand dollars."

    scene 26sharolhouse

    b "You must be out of your fuckin' mind. I doubt everything in this house combined is
    worth one thousand dollars."
    b "You know what? You give me Seth's last name, and I'll give you half that
    amount."

    scene 24sharolhouse

    s "Seth!? How do you know about that crazy fuck?"
    s "And why the fuck would you give two shits about him?"

    scene 27sharolhouse

    b "He raped your daughter, you daft slut!"

    s "For fuck's sake, not this again."

    scene 26sharolhouse with dissolve

    b "You knew about this? What the fuck, Sharol?! Why didn't you tell me?"
    b "She needs help, goddammit! She is seriously traumatized."
    b "I should have called child services a long time ago, Sharol! You're
    a real piece of shit!"

    scene 34sharolhouse

    s "Watch your fuckin' mouth, [player_name]. You abandon her for two years
    and then have the audacity to say that shit to me. Fuck you!"
    s "And she wasn't raped, you gullible cocksucker! Seth was with me the whole
    night."

    scene 26sharolhouse

    b "How would you know!? You were probably in a drunken coma! You're
    lucky she's still alive!"
    b "You know what? She ain't your problem anymore. She's eighteen, she can
    make her own decisions."
    b "She's coming to live with me."

    scene 25sharolhouse

    s "I don't give a fuck what she does. As long as she ain't here!"

    scene 28sharolhouse with dissolve

    a "Uncle? I'm all packed and ready to go."

    ai "{i}I could hear them shouting at each other all the way in my room.{/i}"
    ai "{i}Mom is obviously drunk. I don't know why he gets into spats with her
    when she's been drinking.{/i}"
    ai "{i}She doesn't listen to reason when she's drunk and she doesn't care
    about anyone else but herself when she's been drinking either.{/i}"

    b "That's all you've got?"

    a "Yeah, I don't need much."

    scene 33sharolhouse with dissolve

    a "You bought me plenty of stuff that's still in my room at your house anyway!"

    b "You look gorgeous in that outfit. It looks great on you."

    a "Thank you, Uncle!"

    scene 34sharolhouse

    s "Aw that's just fuckin' great. You're lookin' at my daughter like she's
    your next meal."
    s "Are you fucking my daughter, [player_name]?"

    scene 31sharolhouse

    a "What the hell, Mom!? Why would you even say that?"
    a "He's just being nice! God! Why do you have to be such a bitch!?"

    scene 34sharolhouse

    s "You ungrateful brat! You know what?! Go on then!"
    s "But mark my words, he's gonna want somethin' in return for helpin' you, Avalon!"
    s "Don't come crawlin' back to me when your naive little ass really {b}does{/b} get raped!"

    scene 31sharolhouse

    a "Oh my God, Mom! How could you say that about [player_name]!?"

    b "You're just determined to push everyone away, aren't you? Well congratulations,
    you're officially a fuckin' monster."

    scene 35sharolhouse

    s "You two deserve each other. I better see that cash real soon, [player_name]."
    s "Now get the fuck out of my house!"

    stop music fadeout 2.0

    b "With pleasure!"

    scene 9burgera with fade

    bi "{i}We promptly left Sharol's house and made our way to the restaurant.{/i}"
    bi "{i}I was fuming with rage when we left but Avalon helped calm me down.{/i}"
    bi "{i}It was as if my vision tunneled in on her when she was around.{/i}"
    bi "{i}The rest of the world just melted away.{/i}"

    play music "audio/aint_it_funny.mp3"

    scene 2burgera

    a "I don't think it works quite like that, Uncle [player_name]."

    scene 6burgera

    b "I'm tellin' you, Avalon!"
    b "A sound of 1100 dB would create a singularity as large as the galaxy!"

    scene 2burgera

    a "But there is nothing that could generate a sound of that caliber!"
    a "It's simply impossible."

    scene 5burgera

    b "What if God was like, jammin' out one day."
    b "And he was like 'Aw yeah Jesus, crank it up to eleven!'"
    b "And Jesus was like 'How about eleven {b}HUNDRED{/b}!'"
    b "And God was like 'No that'll create a black ho--!'"
    b "But it was too late."

    scene 4burgera

    menu:
            "{b}Additional Dialogue Choice{/b}"
            "Bananas.":
                a "Uncle, I don't know what that story was about."
                a "But it sounded both blasphemous and bananas."
                a "I love you, Uncle, but you're a special kind of strange."

            "You're an unusual person.":
                a "Your brain goes to weird places sometimes, Uncle."
                a "I'm worried that one day your brain is going to go off into
                crazy town, set down roots and never come back."
                a "Maybe your next coffee needs to be decaf."

            "Involve Satan.":
                a "Oh yeah? And then what, Uncle?"
                a "Did the Devil show up and compare this new black hole to
                    Jesus' mom's butthole?"
                a "'Yo mamma is so fat, her anus ate the whole galaxy!'"

                b "Too far, Avalon! That got way too weird!"

    scene 7burgera

    stop music fadeout 2.0

    b "I noticed you took out your eyebrow piercing?"
    b "Any particular reason or did you just get bored of it?"

    scene 3burgera

    play music "audio/a_quiet_thought.mp3"

    a "I was in a dark place when I got it. I've been thinking about taking it
    out for a while."
    a "Spending time with you made me remember who I used to be. I don't like
    the person I am now."
    a "And, well, I want to like myself again. I was thinking I could try to get
    back to that person."

    scene 5burgera

    b "I liked the person you were and I like the person you are now. If you want
    to change though, I support that."

    a "Plus, I think I looked ugly with the eyebrow piercing."

    b "Do you know what the definition of beauty is?"
    b "I think I heard it best like this;"
    b "Beauty is a summation of the parts working together in such a way that
        nothing needs be added, taken away or altered."
    b "I prefer you without the piercing because I think you're beautiful just
        the way you are."

    scene 1burgera

    a "I don't remember ordering my burger with extra cheese!"

    scene 6burgera

    b "I read that qoute on a candy wrapper."

    scene 5burgera with dissolve

    b "Honestly though, you should wear, pierce or tattoo whatever you want."
    b "Some beauty can't be diminished no matter what you add or subtract."

    stop music fadeout 1.0

    a "That's sweet, Uncle. Thank you."

    if octavia == True:
        jump octavia_burger

    else:
        jump dallas_burger

    label octavia_burger:

    play music "audio/tomorrows_rain.mp3"

    scene 1burgero

    b "I forgot to tell you something, Avalon. I met someone at the library yesterday."
    b "We got so wrapped up in other things, it slipped my mind. But she's meeting
    us here for breakfast."

    a "You met some random person at the library and invited them to have brunch
    with us?"
    a "And you didn't tell me until we're now literally having brunch??"

    scene 7burgera

    b "Er, yeah. I sometimes forget the rest of the world exists when you're around."
    b "Listen, her name is Octavia. She's had some experience with helping people."
    b "I told her about your situation and she offered to help."
    scene 3burgera

    a "You told a complete stranger about intimate details of my past?"
    a "Uncle, what were you thinking?"

    scene 8burgera

    b "I don't know how to help you, Avalon. I was desperate. And she seemed
    geniune enough."
    b "Do you think you can give her a chance? The worst that happens is you
    don't care for her and we won't see her again."
    b "She's quite captivating though! I think you'll really like her."

    scene 3burgera

    a "I don't like that you didn't ask me first. I know you're just trying to help
    though."
    a "I'll give her a chance but please talk to me first before inviting strangers
    into our private life."

    b "I will! I promise!"

    a "I don't like peoples first impression of me to be as a victim. You know?"
    a "I'm more than just that one event. Well, most of the time..."

    scene 7burgera with dissolve

    b "Of course. I'm still learning about this. I didn't mean to be insensitive."

    scene 9burgera with dissolve

    a "What's done is done. I think we're both still learning about recovery.
    Let's give Olivia a chance and we'll see how it goes."

    b "Octavia. Her name is Octavia."

    a "Right! Silly me. I have a feeling I'm not the only one that gets those
    mixed up."

    b "You might be right."

    scene 7burgero

    play music "audio/tomorrows_rain.mp3"

    o "Hello, [player_name]. It's wonderful to see you again."

    b "The pleasure is mine. Thank you for joining us today."

    o "I'm not usually one for fast food but it's important to indulge in guilty
    pleasures once in a while, isn't it?"

    b "Guilty pleasures? I never feel guilty after a burger. Should I..?"

    scene 13burgero with dissolve

    o "An argument could be made that life is too short to worry about heart disease."
    o "Especially if you shorten your life even further by introducing food that
    causes heart disease."
    o "What a fascinating quandry. I will ponder on this and get back to you, [player_name]!"

    scene 15burgero

    b "Right..."

    ai "{i}What a fascinating woman. She's kind of a nerd but in just the most
    adorable way ever. And she's cute as a button!{/i}"

    scene 9burgero

    o "And you must be Avalon. [player_name] has such wonderful things to say about
    you."
    o "His eyes light up like stars in the night sky when he talks about you!"
    o "I'm Octavia. It's a pleasure to finally meet you."

    scene 3burgero

    a "Likewise! I heard you met Uncle at the Library?"

    scene 10burgero

    o "So there I am at the top of a ladder picking out a new novel to read when
    suddenly your Uncle shouts up at me, 'Excuse me!'."
    o "It was so startling that I fell! I thought for sure I was going to be
    severly injured."

    scene 7burgero with dissolve

    o "Fortunately for me, [player_name] didn't hesistate. He planted himself just
    below me and I landed right in his arms!"

    scene 6burgero

    a "So you made her fall and then played hero? Doesn't the former
    cancel out the latter?"

    b "You would think."

    scene 5burgero with dissolve

    b "I do apologize for being rather loud in the library. I certainly did
    not intend to startle you."

    scene 7burgero

    o "All is forgiven! I'm just glad you were there to catch me."

    scene 4burgero with dissolve

    o "You're very lucky to have such a strong and heroic Uncle, Avalon."
    o "Have you two always been so close?"

    scene 6burgero

    a "Well, we were up until a few years ago. We lost touch for a while."

    b "But we're falling back into old rhythms. I think we just had our own
    things going on for a while."

    a "It's only been a day so we still have some catching up to do."

    scene 5burgero with dissolve

    b "You mentioned on the phone that you don't actually work at the library?"
    b "What's your line of work, if I may ask?"

    scene 7burgero with dissolve

    o "I'm currently taking a leave of absence from the United States Air Force."

    b "Oh, were you a pilot?"

    o "Nope."

    scene 15burgero

    bi "{i}I waited a few moments for more details. From what little I knew about her,
    she wasn't usually prone to such short responses.{/i}"
    bi "{i}But after a few seconds, I realized that's all I was going to get for now.{/i}"

    b "Uhh. Alright then."

    bi "{i}It seemed Avalon wasn't afraid to poke further though.{/i}"

    scene 16burgero with dissolve

    a "So you're not a pilot but you didn't correct Uncle on what you actually do
    in the military."
    a "Are you a spy, Octavia? Are you just here to gather information on us?"
    a "Do you suspect us of being terrorists? You'll never take me alive!"

    scene 9burgero

    o "Oh that would be such a thrilling career, wouldn't it?"
    o "Unfortunately I lack the finesse as [player_name] can tell you from my
    fall at the library."
    o "I am quite proficient at martial combat when required though!"

    scene 17burgero

    a "R-really? Could you take Uncle in a fight?"

    b "That's absurd, Avalon. I'm twice her size!"

    o "Oh I absolutely could! I can tell by the way you carry yourself that you're
    not a capable fighter, [player_name]."

    b "I-- That's not true. I can handle myself!"

    scene 7burgero

    o "I meant no offense. I'm sure in a street fight, you'd do quite well!"
    o "But I've had extensive training in both martial combat and firearms."
    o "Even so, my ex is immeasurably more capable in all areas of physical
    confrontation."

    scene 3burgero

    a "I wish I knew how to fight. Maybe then I wouldn't have been--"
    a "Er, I mean, then I could protect myself better."

    scene 11burgero

    o "Your Uncle told me what happened. We don't know each other very well yet but
    I've had some experience with trauma."
    o "Do you know what the difference is between a victim and a survivor, Avalon?"

    a "N-no. Should I?"

    o "A victim will isolate themself, suppress their pain and become discouraged.
    They often have a tendency to begin hating who they are."
    o "A survivor finds the courage to persevere and the strength to push forward.
    They strive to recover and they do whatever it takes to find joy and laughter again."
    o "You're not a victim, Avalon. You're a survivor. Do you understand?"

    a "Y-yes, Ma'am."

    scene 8burgero with dissolve

    o "I still have some magnificent perks I can take advantage of through the
    military. They allow me several relaxing retreats every year."

    scene 9burgero with dissolve

    o "How about a spa day? My treat!"

    bi "{i}She switched gears so quickly, it spun my head around. She wanted
    to get a message to Avalon but not dwell on it.{/i}"
    bi "{i}But how did Avalon take it, I wonder?{/i}"

    scene 6burgero

    a "That sounds like a lot of fun. I could use some rest and relaxation!"
    a "What do you think, Uncle? Would you like to go?"

    b "Uhh. Sure."

    scene 7burgero

    o "I was thinking Avalon and I could visit the pool while you spend some time
    in the steam room."
    o "So her and I can get to know each other better."

    scene 5burgero

    b "That sounds like a great idea. I'm sure you two could use some girl time."
    b "Let's get some grub in us and we'll head out."

    ai "{i}I couldn't get what Octavia said out of my head. The word just kept
    repeating in my mind over and over again.{/i}"
    ai "{i}Survivor. Survivor. I'm a... survivor. Not a victim.{/i}"
    ai "{i}I hadn't thought about it that way before. I felt a new strength growing
    inside me. I wanted to do exactly what she said; perservere and find joy again.{/i}"
    ai "{i}Maybe Octavia really can help me recover...{/i}"

    scene 3spaday with fade

    o "Here we are! An indoor pool aesthetically designed to put your mind
    at ease while floating in clean, rejuvenating waters."

    a "Rejuvenating waters?"

    scene 1spaday with dissolve

    o "Certainly! Water is a powerful life essence for us. We utilize it in
    all parts of our bodies."
    o "And it's a key part of our filtration system too. We build off of it,
    we clean ourselves with it and we keep cool thanks to it!"

    scene 2spaday with dissolve

    a "I hadn't thought about it like that. I knew water was important to our survival
    but you make it sound like it's magical."

    scene 5spaday with dissolve

    a "On the subject of survival, you said earlier that... I'm a survivor?"
    a "I felt inspired by that. Can you tell me more?"

    o "Of course!"

    scene 4spaday with dissolve

    o "But I think I should probably explain myself and my motives to you first."
    o "You see, I'm what most people would consider an unrealistic dreamer."
    o "I fantasize about a world where kindness and community are even more prevalent.
    A utopia where everyone selflessly assists each other in every walk of life."

    scene 6spaday with dissolve

    a "That sounds really nice but it's unrealistic, isn't it? It's in our nature
    to be selfish, vengeful and angry, right?"

    o "Are you selfish, vengeful and angry, Avalon?"

    scene 5spaday with dissolve

    a "I like the idea of other people getting things they want that make them happy."
    a "Despite what happened to me, I don't feel vengeful or angry. Mostly just
    sad."
    a "I suppose my answer is 'No' but everyone is different, aren't they? Some people
    are just predisposed to being good or evil."

    scene 4spaday

    o "Fewer than you might think. People are more often conditioned to be heinous
    rather than born that way."
    o "The society we built has some responsibility in pushing people in the right direction."

    a "How would society push people?"

    o "We are most susceptible to influence when we're young. By my estimation,
    our public education system has the highest level of influence on society."
    o "Improving that system would likely be the best way to reduce crime and increase
    community wellness."

    scene 6spaday with dissolve

    a "That sounds really smart, Octavia. Is that what you did in the military?
    Were you a teacher?"

    scene 7spaday with dissolve

    o "These days, I prefer to help people one on one. It's much more fulfilling for me."
    o "What do you say we test the waters here, Avalon?"
    o "We can talk more once we're swimming."

    a "Oh, right, okay!"

    o "I don't get to come here with friends very often so this is a wonderful
    change for me."

    scene 8spaday with dissolve

    o "Come on in, Avalon. The water is perfect!"

    a "It seems a little cold."

    o "The pool is heated a few degrees below the average body temperature. You'll
    adjust to it rather quickly once you're in."
    o "But you're welcome to ease into the water at your own pace, of course!"

    scene 9spaday with dissolve

    a "Gah! It is a little chilly. But you're right, I can feel myself adjusting
    already."
    a "I don't get to swim very often. In fact, I think it's been a few years."

    scene 10spaday with dissolve

    o "You never forget how."

    scene 12spaday with dissolve

    o "You look like you're in rather good shape, Avalon. Do you exercise regularly?"

    scene 13spaday with dissolve

    a "I was in cheerleading throughout high school. We had to stay in great shape
    for that."
    a "I have a friend that I used to train with. She pushed me, and herself, hard.
    We were in pretty darn good shape!"

    o "Were?"

    a "She still is. I don't train as hard these days. I still do yoga once in a
    while though."

    scene 12spaday

    o "Yoga is a great way to clear the mind and relieve stress."
    o "You know what else is great for stress relief? Meditation."
    o "I actually happen to know a neat technique for water meditation. Would you
    like to try it with me?"

    scene 13spaday

    a "Sure, that sounds great! I've been especially stressed lately so that might
    help a great deal."
    a "How do we start?"

    o "All you have to do is lean back and float on top of the water with your arms
    outstretched."

    a "That sounds easy enough."

    scene 14spaday

    a "Like thi-- Woah! Er, I didn't know you were going to be holding me up."

    o "I didn't mean to startle you. I'll help you stay above water while you
    float here."

    a "Won't you get tired eventually?"

    o "You're nearly weightless in the water so I shouldn't have any trouble
    holding you up at all."

    o "Now I want you to take three deep breaths very slowly."
    o "Concentrate on each inhale and each exhale. Take your time."
    o "Feel your body floating on the water. Release all the tension in all
    your muscles."

    scene 16spaday

    a "Y-your hands are warm. I'm trying to focus on the water but my mind keeps
    getting drawn back to your hands. And your touch..."

    o "Do you make physical contact with people often, Avalon?"

    a "No. I've always tended to shy away from people. Physical contact makes me
    uncomfortable. Especially after what happened to me..."
    a "Although I have been rather comfortable with Uncle now."

    o "Are you uncomfortable with me touching you?"

    scene 17spaday with dissolve

    stop music fadeout 2.0

    a "No. It feels wonderful, actually. You have a welcoming presence, like a summer
    breeze. I feel relaxed with you."
    a "Is that strange for me to say?"

    o "I want you to take another deep breath and then close your eyes, Avalon."

    scene 18spaday with dissolve

    a "I feel so tired all of the sudden. Maybe I'll shut my eyes for just a moment."

    scene 19spaday with dissolve

    play music "audio/let_her_go.mp3"

    a "Just for... a moment..."

    o "Would you mind if I asked you a few questions, Avalon? You don't have to
    answer any of them that you don't feel comfortable with."

    a "Sure, go ahead. I don't mind at all."

    o "Can you tell me about your relationship with [player_name]? How does
    he make you feel when he's around?"

    a "We used to spend more time together when I was younger."
    a "We're only ten years apart in age but he was much like a best friend
    and a father figure to me while I was growing up."

    o "Do you know why he distanced himself from you, Avalon?"

    scene 20spaday with dissolve

    a "I know it had something to do with his real father and the money he'd made
    from his fitness app."
    a "He drifted from me rapidly after he made his fortune. When I did see him,
    he gave me concerned looks and stayed rather quiet."

    o "That is fascinating. It sounds like there might be more to his money than
    you know. Let's focus on present day; how is your relationship with him now?"

    scene 19spaday with dissolve

    a "It's wonderful seeing him again. I alway felt safe when I was around him
    and having him around again, that same feeling is still there."

    o "He mentioned you lashed out at him last night. What happened there?"

    scene 21spaday with dissolve

    a "Every time a man gets close to me now, I feel like a cornered mouse.
    I don't want to submit again, I don't want someone else to take advantage of me."
    a "I told myself I wouldn't let it happen again. I said I'd fight back so hard
    that he'd have to kill me to have his way with me!"

    o "Do you think your Uncle was trying to take advantage of you?"

    a "He was just trying to say 'Goodnight' to me. And I knew that! I don't
    know what came over me."
    a "I've felt so guilty ever since. He wasn't trying to hurt me, he didn't
    deserve to be yelled at like that."

    o "It sounds as if you've had negative experiences with the opposite sex.
    Would that be accurate to say?"

    scene 20spaday with dissolve

    a "Mom is always bringing home gross, perverted men. I know she's lonely but
    does she have to settle for the scum of the Earth?"
    a "They're always grabbing at me, calling me pet names and staring at my butt
    or my breasts."

    scene 22spaday with dissolve

    a "One even snuck into my room, pulled my pants down and... and..."
    a "I felt so broken after that. Why would someone do that? It hurt so bad,
    Octavia..."

    o "Let's focus back on some of the good men in your life. Has there been
    anyone else like [player_name]?"

    scene 21spaday with dissolve

    a "[player_name] speaks highly of my father. He died from a drug overdose when
    I was only a small child so I never got to know him."
    a "But Mom and [player_name] tell me he was a wonderful man. He was kind and
    decent to everyone."
    a "I wish I'd gotten to know him like [player_name] knew him."

    o "And your mother? How is your relationship with her?"

    scene 20spaday with dissolve

    a "Mom never recovered from Dad's death. She just can't seem to find the
    strength to move on."
    a "It's gotten worse in recent years though. After [player_name] stopped coming
    around, she started drinking more."
    a "Every time I see her now, she's got a bottle in her hand. I don't know how
    to help her."

    o "How are you feeling right now, Avalon?"

    scene 19spaday with dissolve

    a "I feel magnificent, actually. These topics have been weighing heavily on me.
    It's nice to get them out in the open instead of bottling them up."
    a "I'm also feeling aroused by your touch. I like your hands on me, Octavia."
    a "The way you speak and what you say to me is magnetic."

    o "You mean 'Magnificent'?"

    a "No, I mean that I'm drawn to you like a magnet. We just met but already
    I'm entranced by you."

    o "This has been informative, Avalon. I'd like you to wake up now. Open your
    eyes slowly and take a deep breath."

    scene 18spaday with dissolve

    stop music fadeout 2.0

    a "Hmm..? I'm floating..."

    scene 17spaday with dissolve

    a "I'm in water?"
    a "Right. We went swimming. I must have dozed off?"

    scene 14spaday with dissolve

    o "I put you in a trance to help you relax and so I could ask you a few questions."

    a "Questions?"

    o "You might think of it as a purge. I helped you release some of your worries
    and feelings."

    scene 17spaday with dissolve

    a "There's not an ounce of stress in my whole body. I feel like a new woman."
    a "Thank you, Octavia."

    o "You're quite welcome!"

    scene 14spaday

    o "How about we go see how [player_name] is doing in the steam room?"

    a "Alright, yeah, let's go see."

    scene 1steamroom with fade

    bi "{i}This was a splendid idea. I've been using weight lifting to reduce
    stress for years. It's about time I finally let my muscles relax.{/i}"
    bi "{i}Though I sure am glad Johnny introduced me to weight lifting. If I
    didn't have that to fall back on, I don't know where I'd be right now.{/i}"
    bi "{i}I hope Avalon is finding her time similarly restful.{/i}"
    bi "{i}Perhaps I should allow myself to sleep for a moment. They'll wake
    me when they're done...{/i}"

    scene 2steamroom with dissolve

    a "Uncle [player_name]? Did you fall asleep, you lazy bum?"
    a "Come on, wake up. It's time to go home. We can't stay here all day."

    b "Erm? Avalon?"

    scene 3steamroom with dissolve

    b "Oh. I dozed off for a bit. Did you have a nice time?"

    a "Octavia and I swam for a bit. They have an incredible pool here, Uncle."
    a "The water is so calming and healing. I feel like I could take on the
    world now!"

    b "That's excellent, I'm glad to hear it."

    scene 6steamroom

    a "It looks like you rested well too! You could sleep anywhere, huh?"

    b "Yeah, well, it's easy to do when you're always exhausted. I push myself
    pretty hard at the gym and rarely get enough sleep at night."

    a "You should change that."

    scene 4steamroom

    b "Huh? Octavia? Is everything alright?"

    scene 8steamroom

    o "Yes, everything is fine, [player_name]."
    o "May I speak with your Uncle in private for a moment, Avalon?"

    a "Sure, I'll go change and get ready to go. Don't be too long."

    scene 10steamroom with fade

    play music "audio/tomorrows_rain.mp3"

    b "I'm not going to lie, you kind of freaked me out with the shocked expression
        you had a moment ago."
    b "Is everything alright? Did I do something wrong?"

    scene 14steamroom

    o "I spoke with Avalon for a while about herself and her past. She told me about
    her parents, you and her assault."
    o "When I first met her, I was expecting someone more reclusive and depressed."
    o "She's a remarkable woman to be handling such tragedy with such strength."

    scene 11steamroom

    b "Her father was the same way; he was a beacon of positivity. He was the
    greatest man I ever knew."

    scene 13steamroom with dissolve

    b "Avalon has that same positivity. Before, it was almost supernatural! Now,
    it's so dim and faint in comparison..."
    b "I really let her down, didn't I?"

    scene 15steamroom

    o "Do not be so quick to take responsibility for Avalon's abuse, [player_name]."
    o "You have your own demons you're fighting, I can tell. There's more to the
    money you came into than you're telling me, isn't there?"
    o "Listen to me, [player_name]. You both have a chance right now to lean on
    each other for support. It's a new start."

    scene 14steamroom with dissolve

    o "I expected her affection for you to be more paternal in nature."
    o "Her body language and expressions tell a different story. I believe she
    may have more intimate feelings towards you."
    o "That's why I was surprised when I saw her with you a moment ago."

    b "She has been affectionate lately. Unusually so. But before--"

    scene 15steamroom with dissolve

    o "Before she was just a girl. As far as I can tell, you're the only man in
    her life that has been good to her."
    o "Avalon is a woman now and she is the type that relies on others for
    safety and protection. Her mother failed her in that."
    o "She's looking to you to be that shield for her now. It's also exactly the type
    of man she desires as a partner; a protector."

    scene 10steamroom

    b "I guess I should tell her that's a bad idea, right?"

    scene 15steamroom with dissolve

    o "Is it? You're both in vulnerable places right now and could use someone
    to lean on."
    o "You both get along well and know each other inside and out."
    o "If you're happy together, it would seem a natural direction to take your
    relationship."

    scene 10steamroom

    b "But she's my niece. It would be weird, wouldn't it?"

    scene 16steamroom

    o "[player_name], life is hard enough without denying yourself the things you want."
    o "You should do what makes you happy as long as whatever that is doesn't harm
        yourself or others."
    o "If you desire her and she desires you, then there's no harm in it."
    o "A healthy relationship could be rehabilitative for both of you."
    o "It is unfortunate, though. I was becoming rather interested in you myself."

    scene 11steamroom

    b "I imagine you would get bored of me rather quickly, Octavia."
    b "I don't think I could keep up with your intellect."
    b "You were also in the military. I'm sure my life would be dull and uninspired
    compared to yours. You can't possibly want that, right?"

    scene 16steamroom

    o "You and I are more interested in the same things than you think, [player_name]."
    o "I've had my adventures, enough for two lifetimes. I'm ready to settle down
    and live a calm and peaceful life."
    o "I don't want any more excitement, I don't want any more adventures."
    o "I want to lounge around for hours at a time, read books and perhaps
    help the occasional neighbor."
    o "I want a simple life now, [player_name]."

    scene 10steamroom

    b "That is almost exactly how I've lived my entire life. You're right,
    it can be peaceful in its own way."
    b "This is only our second meeting but I've enjoyed your company immensely."
    b "Whatever happens, I hope you'll allow me to continue to get to know you."

    scene 16steamroom

    o "I'd like that very much!"
    o "For now, however, I'm feeling rather overwhelmed by everything that I've
    learned today."
    o "I'd like to go home and reflect on it all."
    o "Will you call me tomorrow?"

    scene 11steamroom

    b "Sure, that sounds great. Let's head out."

    stop music fadeout 2.0

## End of Octavia Day Two


    jump night_two


    label dallas_burger:

    play music "audio/disturbed_mind.mp3"

    scene 1burgerd

    a "Is that Dallas over there waving at us? What a coincidence that she
    would be here."

    b "Oh, no, I invited her. I forgot to mention it."

    scene 2burgerd with dissolve

    a "What a great idea! Thanks for setting this up."

    b "Do all her jeans have holes in them? What an unusual trend."

    a "I don't think she does it as a fashion statment, Uncle. She has to be
    especially frugal with her money."

    scene 1burgera

    a "You know she's always had a bit of a crush on you, Uncle."

    b "I figured that out after I spanked her bottom yesterday."

    scene 2burgera with dissolve

    a "You spanked Dallas? What kind of kinky crap happened between you two
    while I took a nap yesterday, Uncle?"

    scene 5burgera

    b "I got her back for punching me in the plums. She looked at the circle
    so I spanked her. And hard!"

    scene 7burgera with dissolve

    b "In hindsight, she may have enjoyed being spanked."
    b "She is fit as a fiddle too. That butt was so firm and round. She's got
    the perfect little--"

    scene 8burgera with dissolve

    b "Er, I shouldn't have said that."

    scene 2burgera

    a "No, it's fine. You're totally right. She works out like a mad woman and has
    a rockin' bod to show for it."
    a "And you should see her breasts! It's as if the Gods themselves shaped them!"

    b "I have, they're amazing. Er, wait, I shouldn't have said that either."

    scene 4burgera with dissolve

    a "Seriously?? What the hell happened last night!?"

    b "Nothing! I swear!"

    scene 10burgerd

    d "Hey, Girlfriend! You've finally got color in your face again. You feelin'
    better?"
    d "I heard about the nightmare. Sounded like it was a bad one. How are you doin'?"

    scene 3burgerd

    a "It was a rough night but Uncle was there to take care of me. He stayed with
    me all night to make sure I was okay."

    d "Aw, what a sweetheart."

    scene 7burgerd with dissolve

    a "He told me you flashed your boobs at him last night. Dallas, you dirty slut."

    scene 8burgerd

    d "I don't even know what came over me! My brain was scrambled after he
    spanked me."
    d "It kind of got my engine revving, if you know what I mean?"

    a "Stahp!"

    scene 5burgerd with dissolve

    d "Why you gotta rat me out, dude?"

    b "I didn't mean to! Avalon is disarming, she's like a professional interrogator
    or something!"

    d "You just melt around pretty girls, don't you [player_name]?"

    scene 4burgerd with dissolve

    d "You should have seen him stumble over his words after seeing my chest."
    d "I thought something in his brain popped!"

    scene 6burgerd

    b "Hey, I was caught off guard. That's all!"
    b "Can we move off the subject of your breasts for a moment?"

    scene 11burgerd with dissolve

    b "Seriously, what have you been doing these days? You graduated, right?"

    a "You're still working at the cafe, aren't you?"

    scene 12burgerd

    d "I've been working at the local cafe for years now. I've gotten several
    promotions. I practically run the place now!"
    d "The owners are almost never there. They just leave all the details to me."
    d "It's been freakin' great!"

    scene 11burgerd

    b "It sounds like you're crushin' it at work. That's excellent to hear."
    b "Do you enjoy all that responsibility? Running a cafe would be overwhelming
    for most people your age."

    a "That's Dallas for you. Work hard, play hard!"

    scene 5burgerd

    d "Hard work might not be in your vocabulary, [player_name]."
    d "You lazy couch potato!"

    scene 6burgerd

    b "Hey, look at these muscles, Dallas. See these guns? You don't get
    pecs like these from being lazy!"

    scene 7burgerd with dissolve

    a "He's not even offended. He's fine with being a bum."

    scene 4burgerd

    d "How did things go with your mom this morning? [player_name] said you
    were going over there to pick up some things?"
    d "She's been a mess lately. She didn't give you any trouble, did she?"

    scene 9burgerd

    a "It didn't go well. She was drunk and belligerent. Her and Uncle got into
    an argument and then she made some unprovoked accusations."

    b "Yeah, she called me a predator and claimed I was only inviting Avalon into
    my home so I could take advantage of her."

    a "It was so warped. I don't know what has gotten into her lately."
    a "[player_name] would never do that, you know?"

    scene 4burgerd

    d "I mean, you guys do have some chemistry. Have you guys thought about taking
    things to the next level?"

    a "Why do you have to make things weird, Dallas!?"

    scene 12burgerd with dissolve

    d "You're only ten years apart in age and you're not actually related."
    d "What's so weird about it? I'm just putting it out there as a possibility,
    you know?"

    scene 7burgerd

    a "Enough with your craziness, Dallas. Let's move on."
    a "We haven't decided what to do after brunch yet. You want to hang out with us?"

    scene 10burgerd

    d "Sure! I haven't actually worked out today though. You guys want to head to the
    gym after this?"

    scene 12burgerd with dissolve

    d "Oh, you know what we should do? Combat training!"
    d "You know some moves, right, [player_name]?"

    scene 11burgerd

    b "That sounds like a great idea. It could boost Avalon's confidence and
    help her learn to defend herself if she ever needs to."

    a "Yeah, I guess I'd be up for that. As long as no one actually gets hurt."

    d "Let's do it!"

    b "Alright, after we finish eating."

    stop music fadeout 2.0

    scene 1fitnesstraining with fade

    b "Over here, girls. I found us an empty room."
    b "Let's post up here and we'll get started."

    scene 2fitnesstraining

    play music "audio/bored_to_death.mp3"

    b "Now I've been working out for over fifteen years."
    b "I've picked up a few things here and there about self-defense
        and kinesiology."

    scene 6fitnesstraining

    a "What's... kinesiology?"

    scene 2fitnesstraining

    b "Kinesiology is the study of the human body."
    b "More specifically, the way it moves."
    b "The body is a complex and capable machine but it has its limitations
    and restrictions."

    scene 5fitnesstraining

    d "Like the elbow, right? It's a hinge joint."
    d "We were cheerleaders so we have some knowledge on body movement."

    scene 3fitnesstraining

    b "Excellent. And yes, that's correct, Dallas."
    b "The elbow is a hinge joint; it can only move up or down. You can exploit that limitation."
    b "But we're going to focus on more basic and practical combat."
    b "First, we have to limber up. Let's start with some stretching."

    scene 8fitnesstraining

    b "You two were cheerleaders back in school."
    b "Do whatever stretching techniques you're comfortable with."

    scene 9fitnesstraining

    d "That's not stretching, [player_name]. You're just showing off."
    d "You need to actually {i}stretch{/i} your muscles, not just flex them real hard."
    scene 8fitnesstraining

    b "This is how I get the blood pumping, Dallas. "
    b "Try not to look directly at my muscles. We need to get  through this without
    you drooling all over the place."

    d "There's no risk of that, I assure you."

    scene 10fitnesstraining with dissolve

    a "Seriously, Uncle, that's not stretching. You're just showboating right now."

    b "Sorry, what was that? I couldn't hear you over these guns firing."

    scene 11fitnesstraining

    d "So this is what testosterone does to people?"
    d "Makes them obsessed with themselves?"

    b "This is just a consequence of being awesome, Dallas. "
    b "Now, let's do some Upward Rhinoceros."

    scene 12fitnesstraining with dissolve

    d "You mean the yoga move Upward Dog?"
    d "Rhinoceros isn't a pose in like, any exercise routine."

    b "It totally is when you're built like a rhinoceros."

    scene 13fitnesstraining

    b "I didn't even know the body could bend like that, Avalon."
    b "Good work! You make Gumby look like an amateur."

    scene 2fitnesstraining

    b "Alright, now that we're stretched out, we'll start with some basic lessons on self-defense."
    b "Now which body part do you think is the most important to protect in a fight?"

    scene 6fitnesstraining

    a "Your head, right?"

    scene 2fitnesstraining

    b "While virtually every organ is vital, the one in our dome takes priority in a fight."
    b "If we're disoriented or unconscious, we can't defend ourselves."
    b "Great answer, Avalon."

    scene 14fitnesstraining with dissolve

    b "So we'll use our hands to help protect our head by keeping them up near our face."
    b "We can deflect, guard and retaliate this way."

    scene 7fitnesstraining

    b "Exceptional, yes! Just like that."

    b "You both look very intimidating. Like a couple of angry gazelles."

    d "Jackass."

    scene 16fitnesstraining

    b "If we want to attack our opponent, we want to thrust forward with our fist, right?"

    scene 17fitnesstraining

    pause (.3)

    scene 16fitnesstraining

    pause (.3)

    scene 17fitnesstraining

    pause (.3)

    scene 16fitnesstraining

    b "But what are we aiming at? Likely our opponent's head is our target."
    b "The skull is thick and hard. If we smash our fists into it,
    we're just going to break our hands."

    b "Instead, use the flat part of your palm."

    scene 18fitnesstraining

    pause (.3)

    scene 16fitnesstraining

    pause (.3)

    scene 18fitnesstraining

    pause (.3)

    scene 16fitnesstraining

    b "That's going to do a lot less damage to us and a lot more damage to them."
    b "Especially if you aim at the nose or jaw."

    scene 15fitnesstraining

    b "Alright, let Avalon and I train one on one for a moment."

    d "Sure, [player_name]."

    scene 19fitnesstraining

    b "Now take a swing at me just like I taught you."

    a "Are you sure, Uncle? These cheerleader muscles aren't just for show."
    a "I could seriously hurt you. Fair warning!"

    scene 20fitnesstraining

    b "Don't hold back! Use your palm and strike at my head."

    scene 21fitnesstraining

    a "Hyaa!"

    b "Good! A little slow though."
    b "Your opponent isn't just going to stand there while you smash their face in."

    scene 19fitnesstraining

    a "You're too fast, Uncle."

    scene 20fitnesstraining

    b "Then be faster! Don't hold back!"
    b "In a fight, don't worry about your opponent. Worry about yourself!"
    b "Attack like your life depends on it!"

    scene 21fitnesstraining

    a "Eyaah!"

    b "Better! Keep your guard up, don't leave yourself open."

label fitnesstraining:
    if _in_replay:
        $ player_name = renpy.input("What would you like to name the MC?")
        if player_name.strip() == "":
          $ player_name = "Byron"

    scene 22fitnesstraining

    b "Let's mix it up a little."
    b "If you can't land a punch, use your legs."
    b "Try to plant your knee into my abdomen."

    scene 25fitnesstraining

    d "It looks like someone could use a serving of humble pie."

    scene 22fitnesstraining

    b "Attack when you're ready, Avalon."

    d "Hey [player_name], what about using a distraction to catch your opponent off guard?"

    scene 23fitnesstraining with dissolve

    b "Hmm?"
    b "Yes, I suppose--"

    scene 24fitnesstraining

    b "Whuh!"

    scene 26fitnesstraining

    pause

    scene 27fitnesstraining

    a "Iyaah!"

    b "Ugh! My other kidney!"

    scene 28fitnesstraining

    a "Oh shit, I'm so sorry Uncle!"
    a "Are you okay??"

    d "Bahah!"
    d "You went down like a sack of potatoes!"
    d "Taken out by a ninety-pound girl!"
    d "Oh fuck, your pride must be destroyed right now!"

    b "God dammit, Dallas..."
    $ renpy.end_replay()
    stop music fadeout 2.0

    scene 21fitnesstraining

    bi "{i}We trained for a while longer.{/i}"
    bi "{i}The truth was, no matter how hard she trained, she was small.{/i}"
    bi "{i}It was unlikely that any amount of training was really going to make
        a difference in a situation where she was attacked by someone twice her size.{/i}"
    bi "{i}My hope was that this exercise would help her release some pent-up anger
        and perhaps gain a bit of confidence.{/i}"

    scene 27fitnesstraining with dissolve

    bi "{i}Judging by the bruise on my abdomen, I'd say she definitely had some
        rage built up.{/i}"

    scene 2daytwoad with fade

    play music "audio/disturbed_mind.mp3"

    d "I can't believe he went down so hard."
    d "You have to admit though, that must have felt pretty great."
    d "Taking down a guy that has at least a hundred and forty pounds on you?"
    d "I bet you're feeling much more confident in your abilities now, aren't you?"

    scene 9daytwoad

    a "I feel just terrible for kneeing him so hard in the stomach. He might
    be seriously hurt."
    a "I should have held back but he kept telling me to go all out!"

    scene 2daytwoad

    d "[player_name] is a tough cookie, Avalon. Just look at how hard he and I
    play together sometimes."
    d "He can take some serious phsyical abuse and laugh it off. It's one of my
    favorite things about him!"
    d "He's just so damn playful and fun."

    scene 7daytwoad

    a "I don't understand though. Why didn't he block?"
    a "He was so quick before, I couldn't even come close to hitting him."
    a "Do you think he got distracted?"

    scene 4daytwoad

    d "Oh I know he did. I flashed my tits at him to give you an opening."
    d "He might be a gentleman, but he's still a man."
    d "No man can resist the awesome distractive powers of these magnificent mammaries."

    scene 8daytwoad

    a "What!? You distracted him with your breasts so I could hurt him??"
    a "Why would you do that? That's so messed up, Dallas."
    a "And now he's going to associate your breasts with physical pain!"

    scene 4daytwoad

    d "I can't help it! I love the way he looks at me when I flash him."
    d "I think I'm addicted to that facial expression now."
    d "I bet he'd go crazy over yours, too, Avalon. You've got some cute little
    tatas, Girl!"

    scene 5daytwoad

    a "Hey, don't call my breasts little! They're the perfect size for my body type."
    a "And to retort, absolutely not! I wouldn't flash my Uncle just to get some
    shocked reaction from him."
    a "You're mental, Dallas!"

    scene 10daytwoad

    a "H-hey! Stop that! What're you doing, Dallas?"

    d "No, you're totally right, I called it wrong. These aren't small at all."
    d "There's plenty of meaty goodness here!"

    a "Knock it off, you perv!"

    d "Oh my God, I can feel your nipple getting hard against my palm, Avalon."

    scene 11daytwoad with dissolve

    d "Are you getting excited right now? You're remembering when we used to
    fool around, aren't you?"

    a "That was a long time ago! We didn't even know what we were doing!"

    d "Do you think about it sometimes?"

    a "Er... Yeah, sometimes..."

    scene 1nipplestim with dissolve

    d "Are you thinking about it right now? Because your nipple is getting even
    harder."

    a "M-maybe..."

    d "How hard can it get, Avalon? Let's find out."

    show nipplestim

    a "Come on, Dallas! You're getting me excited. What has gotten into you?"

    d "I'm telling you, that spanking your Uncle gave me last night triggered the
    hot spot in my brain. I can't get it out of my head."

    a "R-really? You liked it that much?"

    d "Yeah, you want me to show you how awesome it is?"

    scene 12daytwoad

    a "No! I don't wanna be spanked! You got issues, Girl!"

    d "I know! I'm sorry! I can't help it."

    scene 4daytwoad

    d "I've been so horny lately. Even before your Uncle decided to discpline me
    with his open-palm butt slaps!"

    scene 13daytwoad

    a "Dammit, Dallas. Now my boob is super sensitive."
    a "I can still feel your finger touching my nipple. Why do you have to bring
    me into your world?"
    a "I'm not like you, I want to avoid sex for a while."

    scene 4daytwoad

    d "I know. I'm being insensitive."
    d "I want you to know that I'm proud of you for how far you've come."
    d "You had me worried for a while but today you really seem a lot more like
    your old self."

    scene 6daytwoad

    a "Thanks, Dallas. You've been supportive over the last several months. You
    have no idea how much that means to me."
    a "It's been hard living with Mom. I was staying in the same room where that
    man hurt me."
    a "Staying with Uncle is giving me the opportunity at a fresh start. I'm actually
    excited about the future for the first time in a while."

    scene 2daytwoad

    d "You deserve a fresh start, Girlfriend. You're one of the best people I know."
    d "I hope this new beginning works out for you. Sincerely."
    d "On the subject of [player_name], if you're not interested in him,
    would you mind if I chased him?"

    scene 8daytwoad

    a "I lied to you! Er, I'm sorry but I just didn't want to be frank in front
    of [player_name]."
    a "After last night... I don't know, things are just different now."
    a "You're right, he and I do have a certain chemistry."
    a "Do you think... do you think he'd be open to the idea of dating me?"
    a "Jeez, that sounds so weird to say out loud. Don't judge me!"

    scene 2daytwoad

    d "I think you should do whatever makes you happy, Avalon. Your Uncle is
    a good dude and you two mesh well."
    d "I don't know if he would be open to the idea but I do think it's worth
    exploring."
    d "Ask him for a goodnight kiss or something tonight."

    scene 6daytwoad

    a "Alright, yeah, that sounds like an interesting idea. I'll try it."
    a "Thanks, Dallas. You're a good friend."

    scene 10daytwoad

    d "How good?"

    a "No!"

    stop music fadeout 1.0

    ## END OF DALLAS DAY TWO

    jump night_two


    label night_two:

    scene 1nighttwo with fade

    bi "{i}I've spent some time pondering on the subject of Seth the Dentist.{/i}"
    bi "{i}I have no evidence to prove what he did, so I can't go to the police.{/i}"
    bi "{i}I certainly don't have the expertise myself to deal with this. There's got
    to be professionals that help with this sort of thing, right?{/i}"
    bi "{i}Let's see if we can find someone who can dig up some dirt on this guy.{/i}"
    bi "{i}Or at least find him.{/i}"

    bi "{i}'Private Investigators in my area.'{/i}"
    bi "{i}Searching...{/i}"

    show pennycard:
        xalign 0.1
        yalign 0.1
        linear 0.5 xpos .75

    bi "{i}Penny for Your Thoughts? That's a fascinating name for a business.
    It says professional investigator here.{/i}"
    bi "{i}And there's an e-mail address as well. It's worth a shot.{/i}"

    hide pennycard

    bi "{i}'Dear Investigator, I'm interested in hiring someone to help on a sensitive
        matter.'{/i}"
    bi "{i}'I'd like to request a consultation regarding your services.'{/i}"
    bi "{i}I'll keep it short and simple. Now we wait for a response.{/i}"

    scene 6nighttwo

    play music "audio/no_goodbyes.mp3"

    a "Uncle? I just finished getting ready for bed and noticed you were in here."
    a "May I ask what you're up to?"

    scene 2nighttwo

    b "Hey there, Avalon! I was just doing some research."
    b "Did you know the Unicorn is the national animal of Scotland?"
    b "That place must be a utopia filled with fabled creatures,
        bottomless pints and some of the most rugged men on the planet."
    b "It must be the greatest place ever!"

    scene 9nighttwo

    a "You recently found out you're part Scottish, didn't you?"

    scene 5nighttwo

    b "Maybe."

    scene 8nighttwo

    a "I know you're probably lying to protect me from something
        you think I shouldn't know,"
    a "but I'd rather you just say you don't want to tell me..."

    menu:
        "{b}Additional Dialogue Choice{/b}"
        "Naughty Websites?":
            a "Are you... are you looking at porn?"

        "Dance Classes?":
            a "Are you trying to find dancing classes in your area?"
            a "The dance you did at the motel was a little too good, Uncle."
            a "Like, maybe you're into guys kind of good..."

    scene 4nighttwo

    b "What!? No! How do you know I'm lying??"

    scene 8nighttwo

    a "You tell jokes for a lot of reasons. Usually it's because you're nervous."
    a "Sometimes it's to hide something or cause a distraction away from a topic."

    scene 4nighttwo

    b "How would you even know that??"

    scene 9nighttwo

    a "It'd be hard to miss, Uncle! It's like you play poker with transparent cards.
    You're an open book!"


    scene 2nighttwo

    b "Alright, Smarty-Pants, you got me. I'm trying to hire an investigator."

    scene 8nighttwo

    a "Hire an investigator? If this is about the man that hurt me, I don't want
    to dwell on that."
    a "There's always going to be people like him in the world."
    a "You can't stop them all, Uncle [player_name]."
    a "But you can spend time with your favorite niece."
    a "As much time as you want..."

    scene 5nighttwo

    b "Favorite niece??"
    b "You're my {b}only{/b} niece!"

    scene 9nighttwo

    a "How about a movie? I've got a great one picked out!"
    a "It's called..."

    scene 10nighttwo with dissolve

    a "Child's Play!"

    scene 3nighttwo

    b "Child's Play? Well, that sounds like a nice, innocent film."
    b "Is it like Toy Tale? Where that wooden doll falls in love with a space
    marine?"

    scene 8nighttwo

    a "Well, sort of. Except the toy that's alive..."

    scene 10nighttwo with dissolve

    a "Is possessed by a serial killer!"
    a "Masked as an innocent doll, he invades the home of a young boy and murders
    people with a kitchen knife!"
    a "It's epic."

    scene 5nighttwo

    b "You are seriously disturbed, Avalon. I worry about you sometimes."

    scene 9nighttwo

    a "Come on! It'll be fun! I'll get you a stuffed animal to cuddle with for
    when you get scared."

    scene 2nighttwo

    b "I guess I'll be sleeping with the closet light on tonight!"
    b "Do you have it all setup in the living room?"

    scene 8nighttwo

    a "I was actually thinking we could watch it in my room."
    a "I've already got it ready to watch in there."

    scene 3nighttwo

    b "Alright, that sounds fine. Let me just finish up here and I'll be right in."

    scene 9nighttwo

    a "Okay. I'll leave the door open for you. Don't be long!"

    stop music fadeout 2.0

    scene 1nighttwo

    bi "{i}A response already! That was awfully fast.{/i}"
    bi "{i}It looks like it's just a time and location. Tomorrow morning at a
    lingerie store? That's peculiar.{/i}"
    bi "{i}I hope I don't end up regretting this.{/i}"
    bi "{i}I'll reply with a confirmation and we'll see what happens tomorrow.{/i}"

    scene 11nighttwo with fade

    b "Avalon? Do you have everything ready?"

    scene 12nighttwo

    a "It's starting, come sit next to me! Hurry before you miss something!"

    scene 11nighttwo

    b "Don't rush me! I have to mentally prepare myself for the horrors I'm about
    to witness."

    scene 13nighttwo

    b "You put your television on two cardboard boxes and this is how we're
        going to watch the movie?"
    b "This is literally the most white trash thing I've ever experienced."
    b "And I absolutely adore it. This is great."

    scene 15nighttwo

    a "I had to get creative. You wouldn't believe it but my setup at home is
    similar."
    a "Do you remember when I told you a good horror movie is great to cuddle
        up to someone while watching?"

    scene 14nighttwo

    b "Sure, I remember that. You were convincing me how amazing scary movies are."
    b "And then we watched one that is going to haunt my nightmares for years to come."

    scene 16nighttwo

    a "Well, I was thinking maybe we can cuddle up together for this one?"

    b "Uhh, sure, I think that would be alright."
    b "I'll let you move into the position you want to be in."
    b "Whatever you're comfortable with."

    a "Okay, hold still!"

    scene black with fade

    a "Okay, now put your arm here..."
    a "Yes, good. Move your leg over."
    a "Stop.. stop squirming!"

    b "You're pushing me in weird directions!"
    b "My leg can't move like that!"

    a "Okay okay!"
    a "Just relax and get your knee up."
    a "There, perfect!"

    scene 18nighttwo with fade

    play music "audio/a_quiet_thought.mp3"

    bi "{i}I could feel the warmth of her body pressing into my chest.{/i}"
    bi "{i}Every place on my skin that she made contact with was hypersensitive.{/i}"
    bi "{i}It was as if a gentle electrical current was passing through those parts of me.{/i}"
    bi "{i}Her touch was exhilarating.{/i}"

    ai "{i}He's so big, I feel like his body is completely wrapped around me.{/i}"
    ai "{i}It was as if I were a turtle tucked away in its shell.{/i}"
    ai "{i}Like nothing could hurt me and I was completely protected by him.{/i}"
    ai "{i}There was no safer place in the world for me than right here in his arms.{/i}"

    scene 17nighttwo with dissolve

    a "Are you comfortable? I'm not pressing into you too harshly, am I?"
    a "We can move around a bit if you want."

    scene 19nighttwo with dissolve

    b "No, this is very cozy."
    b "I can't imagine being more comfortable than this."

    scene 20nighttwo with dissolve

    a "We haven't cuddled up together like this in a long time. I missed it."
    a "We should do it more often. I feel safe in your arms."
    a "Anyway... Let's watch the movie."

    scene 21nighttwo with dissolve

    bi "{i}So that's what we did. We watched the movie.{/i}"
    bi "{i}A psychopathic little doll ran around stabbing people with
    kitchen cutlery.{/i}"
    bi "{i}It was terrifying!{/i}"
    bi "{i}But having Avalon right here with me was soothing.{/i}"
    bi "{i}I felt her every time she twitched, every time she shifted
        and even every time she breathed.{/i}"
    bi "{i}And every time I felt her, I fell more in love with her.{/i}"
    bi "{i}She possessed every quality I loved in her father.{/i}"
    bi "{i}And more...{/i}"

    scene 22nighttwo with dissolve

    a "Umm, Uncle [player_name]?"

    scene 23nighttwo with dissolve

    b "Hmm?"

    a "I know we're watching the movie but..."
    a "I remember when you used to tell me stories about my dad."
    a "Can you tell me some of those stories again?"

    scene 24nighttwo with dissolve

    stop music fadeout 1.0

    b "Sure, I can tell you about your father."
    b "I was actually just thinking about him."

    scene 23nighttwo with dissolve

    a "What were you thinking about?"

    scene 24nighttwo with dissolve

    b "I was thinking about how much of him I see in you."

    scene 25nighttwo with dissolve

    play music "audio/no_goodbyes.mp3"

    b "You call him dad but I always knew him as Johnny."
    b "His name was Joseph so I don't know why he went by Johnny instead of Joe.
    But that's neither here nor there."
    b "I was pretty young when he and Sharol started dating."
    b "I think my fondest memory of him was around that time when they first got together."
    b "Sharol didn't want to pick me up from school one day but Johnny said he didn't mind."
    b "He came looking for me when he couldn't find me at the child pick up area."
    b "I was getting beaten up by a few older kids when he found me."
    b "I remember him scaring them off and then looking down at me..."

    scene johnny1 with flash

    j "Hey there, kiddo."
    j "Looks like you got into a little scuffle there."
    j "Here, let me help you up."
    j "We'll get you home and put a bag of frozen peas on that shiner."
    j "You'll be feelin' better in no time."

    scene 25nighttwo with flash

    b "Johnny was compassionate and decent to everyone he met. He was truly
    an inspiration."

    b "Not long after the school incident, he found out Sharol was pregnant with you."
    b "I was there at the hospital the day you were born."
    b "Johnny was holding you in his arms, looking affectionately down at you."
    b "Then, while looking at you, he started talking to me."
    b "He said..."

    scene johnnyhospital with flash

    j "Have you ever heard the story of King Arthur?"
    j "I was captivated by the story when I read it. Do you know what my favorite
    part was?"
    j "King Arthur was mortally wounded in battle. He wasn't going to survive his injuries."
    j "So they rushed him off to a magical land of healing where he recovered."
    j "And he lived on forever there in that new land, healed of all his trauma."
    j "That's what she is, [player_name]. Holding her right now, I feel it."
    j "She is a new start for me. She's my savior, my salvation."
    j "My Avalon."

    scene 25nighttwo with fade

    b "When you were born, he turned his life around for you."
    b "He started working a real job, exercised regularly to keep healthy."

    stop music fadeout 1.0

    b "And he gave up drugs cold turkey, right on the spot."
    b "He said time with you was the only high he'd ever need."

    scene 26nighttwo2 with dissolve

    a "Until I wasn't enough anymore and he overdosed."
    a "And abandoned me."

    scene 27nighttwo with dissolve

    b "Yeah, until he overdosed..."
    b "We all have our demons. Sometimes they get the better of us."

    scene 26nighttwo2 with dissolve

    a "I'd like to go to bed now, Uncle [player_name]."

    scene 27nighttwo with dissolve

    b "Okay, I'll help you get tucked in."

    scene 30nighttwo with fade

    a "Thank you for telling me about my father and for tucking me in."
    a "I wish I'd known him better but at least I have you back in my life."

    scene 32nighttwo

    b "I'm glad to have you back too. I'm not going to leave again, I promise."

    scene 31nighttwo

    a "Before you go, can I..."
    a "Can I have a goodnight kiss?"

    scene 32nighttwo

    b "Sure."

    scene 33nighttwo


    bi "{i}I knew this moment was a tipping point. I could walk away now and our
    relationship would remain platonic.{/i}"
    bi "{i}But I couldn't let history repeat itself. I love her, I know I do. And
    the possibility of our relationship moving forward was enticing.{/i}"
    bi "{i}I wish I had more time to consider it. More time to decide if this is
    truly a beneficial transition for her.{/i}"

    scene 34nighttwo

    bi "{i}But what if I deny her now and she runs away forever? I can't let that
    happen again. Not with her...{/i}"
    bi "{i}I know I want this too. I just have to find the courage to take the leap.
    No more thinking, no more indecisions!{/i}"
    bi "{i}Just like with any serious situation, though, I had to make a joke first.{/i}"

    scene 35nighttwo with dissolve

    b "Mwah!"

    scene 36nighttwo with dissolve

    a "No, Uncle! Not on the nose!"

    b "Eck, your nose is all moist like a dog's nose."
    b "Do you have a cold or something?"

    a "Gross, Uncle! Don't say the word 'moist' to me, I don't like it!"
    a "And my nose is not wet, your lips are!"
    a "Come on, kiss me seriously. Kiss me on the lips."

    bi "{i}So that's what I did and this would be the kiss that would fundamentally
        and permanently change our relationship.{/i}"

    scene 38nighttwo with dissolve

    pause

    bi "{i}Her head tilted back slightly and I could hear her take a deep, passionate breath.{/i}"
    bi "{i}My heart was racing a mile a minute.{/i}"
    bi "{i}I held my lips to hers, stretching this wonderful moment out as long as I could.{/i}"
    bi "{i}Everything terrible that had ever happened to me washed away.{/i}"
    bi "{i}As if this one kiss was enough to mend my every scar, my every pain.{/i}"
    bi "{i}This was the start of something new, something magical.{/i}"

    scene 37nighttwo with dissolve

    a "Mm. That was amazing."
    a "Thank you, Uncle [player_name]."

    b "You're welcome."
    b "Sleep well,"
    b "My Avalon."

    jump act_three_s






    ## Return ends the game.


return
