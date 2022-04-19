





label whatif:
    scene black

    $ player_name = renpy.input("What would you like to name the MC?")
    if player_name.strip() == "":
      $ player_name = "Byron"

    $ customised = True

    $ persistent.galleryName = "[player_name]"

    $ right_hand = Position(xpos=1.0, ypos=1.0)

    jump whatif_s

label whatif_s:


    scene myrabg with fade

    if persistent.whatif == False:
        $ renpy.notify("You've unlocked the Bonus Act in Act Select on the Main Menu!")
        $ persistent.whatif = True

    stop music

    play music "audio/touching_moment.mp3"

    pause

    show myrabelle serious with dissolve

    m "Do you believe in fate?"
    m "I wonder how much of our lives we're in control of and how much is
    just causality; one event leading into another perpetually through time."
    m "Perhaps time is a straight, predetermined line of events that cannot be altered."
    m "A story carved in stone and paved with permanence."
    m "But what if we could change something? What if we could reach into that
    timeline and nudge a decision in a different direction?"

    show myrabelle right closedfist with dissolve

    m "If you could go back in time, I wonder what you would change?"
    m "Whatever you would decide to alter, there would be a ripple of change
    that would wrap around the entire globe."

    show myrabelle right openhand with dissolve
    show earth1 with purpleflash

    m "This is the world Lockheart and I created."
    m "And into this world we birthed both wonderful and terrible characters who were all trying to
    recover from their individual trauma in their own ways."
    m "In telling their story, we watched as they fought to find joy despite their hardships
    and loss."
    m "Many of our beloved characters found happiness by the end, and some did not."

    show myrabelle right lookcam with dissolve

    m "But we can't help but wonder..."
    m "What if we changed something? What if we influenced just one of them in a different
    direction?"
    m "What would that world look like?"

    show myrabelle bothhands with dissolve
    show earth2 with purpleflash

    m "Could one decision affect the world so dramatically that a completely unique
    story would present itself?"
    m "Should we allow ourselves to indulge in this deviation?"
    m "Should we set aside the world we know..."

    show myrabelle right closehand
    hide earth1
    with dissolve

    m "and travel a different path in a world we don't?"
    m "What if it's a better story? What if we get to experience a tale with less
    suffering? With less pain?"
    m "What if we took... just a peek..."

    scene black with purpleflash

    stop music fadeout 1.0

    pause 1.0

    "What if..?" with dissolve

    jump distresscall

    label distresscall:

    scene distresscall01 with fade

    pause

    play sound "audio/cellvibe.mp3"

    scene distresscall001 with dissolve

    "*Bzzz* *Bzzz*"

    scene distresscall02 with dissolve

    "*Bzzz* *Bzzz*"

    b2 "Ugh..."

    scene distresscall03

    stop sound

    b2 "Erhm... Hello?"

    play music "audio/one_step_closer.mp3"

    a4 "Uncle [player_name]?"

    b2 "No, this is [player_name]'s message inbox."
    b2 "Leave a message after--"

    a4 "Were you asleep?! Jeez, you are such a bum. It's only nine thirty at night!"
    a4 "Anyway, listen, mom invited over some creepy guy and I'm really uncomfortable."

    b2 "That woman is incorrigible. One of these days, she's going to invite over the
    wrong person and they're going to do something terrible."

    a4 "That's what I'm afraid of, Uncle! I don't think I should stay here tonight."
    a4 "He keeps looking at me strangely, like he's groping me with his eyes."

    b2 "Stop. I can't hear this. Look, I'll come pick you up and you can stay with
    us tonight."

    a4 "Thank you, Uncle! You're the best! I knew I could count on you!"

    b2 "No more shouting. Uncle is still waking up."

    a4 "Okay, sorry, just be here soon. I can't be around this guy for much longer."
    a4 "He asked to see my teeth earlier. How weird is that? What a freak!"

    b2 "What is he? A vampire?"

    a4 "He said he's a dentist. Just hurry, Uncle! I don't want a root canal in the
    middle of the night!"

    b2 "Alright. I'm on my way. I'll see you soon."

    a4 "Thank you again, Uncle!"

    "*Click*"

    scene distresscall04 with dissolve

    "[player_name] sat up and let out a deep sigh."
    "His mind wandered to the possibilities of what might happen if that strange
    man actually did do something terrible to Avalon."
    "He shook his head and perished the thought."

    scene distresscall05 with dissolve

    l2 "Is something wrong, Bear? Who was that on the phone? It sounded like Avalon?"

    b2 "Yeah, Sharol has a booty call over. He's got Avalon spooked. Hell, he's
    got me spooked now."

    "Leah's eyes grew wide with concern. As a woman herself, she knew all too
    well how it felt being around strange and creepy men."

    scene distresscall06

    l2 "Oh no, that's not good at all! Well, we can't let her stay there tonight."
    l2 "We have to go get her! Right?"

    b2 "Of course. I'm sure she'll be alright
    until we get there but I don't want to take any risks. I want to get her quickly."

    l2 "Well, let's go then! What are you waiting for??"

    b2 "I'm waiting for you to get off me."

    scene distresscall07 with dissolve

    l2 "Huh? Oh, right!"
    l2 "Hang on, let me put some pants on and I'll go with you."

    b2 "You don't have to do that. I can collect her myself."

    l2 "No, I want to go too! I want to make sure she's alright."

    b2 "I appreciate you being so supportive like this. That means a lot to me."

    scene distresscall06 with dissolve

    l2 "She's family, [player_name]. Of course I support you helping her out."

    b2 "Not everyone would be so eager to drop everything to help someone they
    don't know yet."
    b2 "You're a selfless and caring person, it's one of my favorite parts about you."

    l2 "Aw, Teddy Bear..."

    l2 "Come on, you can spout your romantics to me later. We've got a damsel in distress to save!"

    stop music fadeout 1.0

    scene welcomeava01 with fade

    play music "audio/soft_reminder.mp3"

    b2 "I'm glad you're alright, Avalon. You had me worried."

    a4 "I'm used to Mom bringing home gross guys but this one was too much for me.
    He takes the cake!"

    l2 "You're always welcome to stay with us whenever you're uncomfortable at home."

    a4 "Aw, thank you, Leah! You're the best!"

    scene welcomeava02 with dissolve

    l2 "Why don't we sit on the couch and wind down for a bit?"

    b2 "Yeah, I'm awake now. A conversation might be just what I need to relax a bit."
    b2 "This whole thing had me worried."

    a4 "Sounds good to me! I've been staying up late since I graduated anyway."

    scene welcomeava12 with dissolve

    a4 "Uncle, I hope it's not too bold for me to say but you look so healthy today."
    a4 "You're all clean cut and your skin looks clear and youthful."
    a4 "What's your secret?"

    scene welcomeava05

    b2 "You think I'm looking healthier?"

    l2 "He was getting four hours of sleep every night before we started dating!"
    l2 "And his diet was junk food and protein shakes. He was a mess!"
    l2 "After we got together, I started forcing him to eat better and sleep more."

    scene welcomeava08

    a4 "Yeah, he's like a toddler! He can't take care of himself."

    scene welcomeava07 with dissolve

    a4 "I'm glad you convinced him to reach out to me. I don't know why we lost touch
    for so long."
    a4 "I kept meaning to call him myself but I was so busy with cheerleading
    and Dallas signed us up for extra classes."
    a4 "On the weekends I had to take care of Mom! I'd have to go grocery shopping
    for her and prepare a week's worth of food for her to eat."
    a4 "Not to mention all the cleaning just to keep the house from turning into
    a landfill!"

    scene welcomeava06

    b2 "I'm sorry, Avalon. I should have stayed in touch better. I especially could have
    helped you out with Sharol."
    b2 "After the pen incident, I figured she didn't want me around."
    b2 "I wasn't in a good place for a few years. I was struggling with some things."

    l2 "He used to talk about you a lot. After the first day we got together,
    I forced him to reach out to you."
    l2 "I just knew he'd be a lot happier if he did."

    scene welcomeava11

    a4 "I'm glad Leah made you call, Uncle. I've missed you."

    b2 "I've missed you too, Avalon."

    a4 "I know it's only been a week since we started talking again and this is
    the first time we're spending time together in person but..."
    a4 "It feels just like old times. It's as if we're picking back up right where we left
    off."

    b2 "It's so strange seeing you now. You're all grown up. It's only been two
    years but you're like a new person."

    a4 "Thank you! Dallas and I had to grow up fast. I mean, we basically have
    to take care of ourselves, you know?"

    scene welcomeava07 with dissolve

    a4 "And Leah, you are so much prettier than the picture [player_name] sent me."
    a4 "Like an Irish Cleopatra or something. I don't even know."

    l2 "Me? Look at you! I love your hair. I'm jealous over how lovely it is."

    a4 "I put too much effort into it but I love it! I think the only
    way I'd change it is if I became, like, an entirely different person!"
    a4 "I can't imagine what it would take for that to happen though."

    scene welcomeava06

    l2 "Avalon, does your mother bring home strange men often?"

    b2 "How are things at home lately? I don't assume Sharol has turned over a new
    leaf but has she at least been steady in her ways?"

    scene welcomeava14

    a4 "Mom has been drinking a lot more lately. She's also put on weight since
    the last time you saw her. Dallas says it might be her midlife crisis?"
    a4 "I'm not sure but she has gotten worse. I don't know how to help her.
    She won't listen to me, she is so stubborn!"

    scene welcomeava10 with dissolve

    a4 "And yes, she has been bringing more men home lately. They've been the worst
    yet!"
    a4 "She used to be moderately attractive so she could find lonely middle-class
    men on business trips or whatever at bars and bring them home for the night."
    a4 "Now it seems like it's always drug addicts, white trash or... worse."
    a4 "I typically stay over with Dallas when she brings someone home but she
    has work tomorrow so I didn't want to bother her."

    scene welcomeava06

    l2 "I know it's not my place and you are welcome to say so but I'd like to
    speak up because I'm concerned for your safety."
    l2 "It might be time to consider getting her help, Avalon. She could
    obviously benefit from therapy and perhaps even medication."

    a4 "I've tried telling her that! I can't convince her, Leah."

    b2 "She is a stubborn woman, you're right about that, Avalon. I tried to
    talk her into slowing down on the drinking to no avail."

    scene welcomeava10

    a4 "I appreciate your concern, Leah. I agree with you. I've tried everything
    I can think of though."
    a4 "If you have any ideas on how we can get her into therapy, I'm all ears."

    l2 "I'll think of something."

    scene welcomeava03

    b2 "Now that we know you're safe, my anxiety is settling down. Are you girls
    ready for bed?"

    a4 "Sure."

    l2 "Do you need to be home at a specific time tomorrow?"

    scene welcomeava10

    a4 "No, but I am worried about Mom so I'd like to be home sooner rather than later."
    a4 "I know it was her decision to invite that man over but I'm still a bit
    concerned for her safety."

    l2 "I understand. We'll have you home at a reasonable time tomorrow."

    a4 "Thank you, Leah. I'll see you both in the morning!"

    stop music fadeout 2.0

    b2 "Good night, Avalon."
    l2 "See you tomorrow."

    scene sleeptogether02 with fade

    play music "audio/a_quiet_thought.mp3"

    l2 "She's a sweet girl, [player_name]. You two seem to have had a strong
    connection before."
    l2 "I don't want your reconnection to start off on the wrong foot. I'm a little
    worried about us keeping our secret."
    l2 "Should I tell her that you're my [persistent.byron_rel] and I'm your [persistent.leah_rel]?"

    scene sleeptogether01

    b2 "Let's keep it to ourselves for now. We'll play it by ear."
    b2 "If we decide later on that it's something we could, or should, tell her, we will."
    b2 "But for now, it's not something I'd like to put out in the open. I don't
    think other people will understand, you know?"

    scene sleeptogether02

    l2 "Okay. I just want you to know that it's up to you and I support you either
    way."

    a4 "Uncle [player_name]? Leah?"

    scene sleeptogether03

    l2 "Avalon? Is everything alright?"

    a4 "That man freaked me out more than I realized. I don't want to sleep
    alone tonight. Would you mind if I..?"

    l2 "Not at all! [player_name], scootch over. Come lay next to me, Avalon."

    a4 "Are you sure? You really don't mind? I don't want to intrude."

    b2 "It's no bother at all. Sincerely, Avalon, you're welcome to join us.
    We want you to feel safe tonight."

    scene sleeptogether04 with dissolve

    a4 "I don't usually get like this. I watch horror movies all the time and I'm
    completely fine to go to sleep after!"
    a4 "But as soon as I turned the light off tonight, I kept imagining that
    man coming into my room while I slept and..."

    l2 "Nobody is going to hurt you, Avalon. Not while you're with us. That's a
    promise."

    a4 "Thank you, Leah. I guess Uncle [player_name] finally found a good woman, didn't
    he?"

    scene sleeptogether05

    l2 "He and I are both lucky we found each other. When I saw him for the first
    time, I thought he looked like a dumb meathead!"

    b2 "I'm right here, I can hear you talking about me."

    l2 "But he turned out to be a real sweetheart. Do you want to hear the story
    of how we got together?"

    a4 "Yes! Tell me!"

    b2 "Ugh! It's not even that interesting. I'm going to pass out from boredom."

    a4 "Quiet, Uncle! It's story time!"

    scene black with fade

    stop music fadeout 1.0

    l2 "So we decided to go swimming together and he tried to throw me in the pool.
    But I turned the tables on him!"

    scene 84leah2 with vpunch

    play music "audio/aint_it_funny.mp3"

    l2 "Gotchya, sucker!"

    scene 85leah2

    b2 "This betrayal will not be forgotten!"

    scene 86leah2

    play sound "audio/splash.mp3"

    l2"Oh yeah! You mess with the queen, you get the guillotine!"
    l2"Ahoo, ahoo, ahoo!"

    scene 87leah2 with dissolve

    b2 "Aw man, you got me good! I'm so damn proud of you right now."
    b2 "I can't even believe it."

    l2"You're too easy."

    scene 88leah2

    l2"I've noticed you have a weakness for girls in distress and it is so easy
    to play on that."
    l2"You're just a big ol' softy, [player_name]."

    scene 89leah2 with dissolve

    b2 "You were so convincing! You should take your act on the road, Leah. You're
    a natural!"

    l2"I took acting lessons in high school. I couldn't stand it though!"
    l2"In fact, I had a serious urge to burn the stage down!"

    b2 "You know, I have never had the urge to burn something down just to add shock
    value."

    l2"Shock value? What do you mean?"

    b2 "Oh, nothing. My brain must be scrambled, I'm not talking straight."

    stop music fadeout 2.0

    scene 90leah2 with dissolve

    b2 "I must be exhausted from having been brutally assaulted a
        moment ago."

    scene 91leah2 with dissolve

    b2 "Some crazy redhead pushed me into a big hole in the ground!"

    l2"At least that hole had water in it!"

    scene 92leah2 with dissolve

    play music "audio/soft_reminder.mp3"

    l2"[player_name], I have something to tell you. I've been meaning to tell
    you this for a while."

    b2 "Oh? What is it?"

    l2"It's a secret."

    scene 93leah2 with dissolve

    l2"I have to whisper it to you."

    b2 "Whoa, what are you--"

    l2"I like you, [player_name]."
    l2"These last few months that we've spent together, they've been some of the
        best days of my life."
    l2"After my foster parents left, I felt so alone. I didn't have anyone."
    l2"But now, with you, I'm happy. And I want us to be more than what we are."

    scene 96leah2

    b2 "This is a bad idea, Leah. We have a good thing going as we are now."
    b2 "Why would you want to change that?"

    scene 94leah2

    l2"We don't have anyone else, [player_name]."
    l2"Everyone else has abandoned us. We're all we have."

    b2 "But we're--"

    l2"Who cares??"
    l2"Nobody has to know we're [persistent.relationship]."
    l2"This could be our only chance for a relationship. It could be our only
    chance to be happy."
    l2"Let me make you happy, [player_name]."

    scene 97leah2 with dissolve

    l2"Mm."

    scene 98leah2 with dissolve

    pause (.5)

    scene sleeptogether06 with purpleflash

    b2 "S-stop. Listen to me, Leah. I'm not saying 'No'."
    b2 "But I can't jump into something like this without considering it first."
    b2 "You're moving too fast for me. Can we please slow down?"

    scene sleeptogether07 with dissolve

    l2 "I'm sorry, [player_name]. You're right, I don't know what came over me."
    l2 "I've been thinking about this for a while. I just don't think I could bear
    it if you rejected me."
    l2 "I decided to go all in. Put it all on the line. In hindsight, it may have
    come off as a bit aggressive. I'm sorry."

    b2 "Don't apologize, it was sexy as hell. But you have a career, you're successful
    and motivated. I'm always going to be a loser, Leah."

    scene sleeptogether08 with dissolve

    l2 "You're not a loser. You haven't found something you're passionate about
    doing yet. You will."

    b2 "After having those planets on top of me, I'm starting to consider astronomy!"

    l2 "W-what? What planets? Are you...?"

    scene sleeptogether09 with dissolve

    l2 "Are you talking about my breasts, [player_name]!?"
    l2 "I'm sensitive about their size. Don't make fun of my boobs!"

    b2 "Who's making fun? I'm just saying that if I was Elon, I'd be planning a
    colonization mission for your right breast. That's all!"

    l2 "Shut up! You're so dumb! What an outrageous thing to say! And don't
    make fun of Elon, he's the Columbus of our time!"

    scene sleeptogether10 with dissolve

    b2 "I don't know if it's a good idea for us to be together."
    b2 "But I am intrigued by the idea. I'd be a fool not to explore the possibility."
    b2 "So how about we go on a date? What do you say?"

    scene sleeptogether11 with dissolve

    l2 "I'd like that, [player_name]. Maybe we can get you some real swim wear
    while we're out."

    scene black with fade

    l2 "And the rest is history. [player_name] decided to give our relationship
    a chance and we've both never been happier."

    a4 "That's amazing. I hope I find love like that one day..."

    "Avalon felt her weary eyes grow heavier until she couldn't hold them open
    any longer."
    "She yawned softly before falling into a deep sleep, comforted by the presence
    of her Uncle and her new friend Leah."

    scene sleeptogether12 with fade

    "She fell asleep not entirely unaware of what egregious fate would have befallen her
    had she stayed home that night."
    "She would rest peacefully under the guardianship of [player_name] and Leah."
    "There was no threat of night terrors or haunting memories for her tonight."

    scene sleeptogether13

    l2 "Sleep tight, Avalon."

    scene sleeptogether14 with dissolve

    stop music fadeout 2.0

    "Leah felt immediately close to Avalon. She wasn't sure if it was because Avalon
    was so easy to get along with or..."
    "If she simply adopted the value of whatever [player_name] treasured."
    "Perhaps it was both."

    label morningwood:

    scene morningwood01 with fade

    play music "audio/a_quiet_thought.mp3"

    "Avalon slept soundly through the shuffling of Leah making her way out of bed
    and to the kitchen."
    "[player_name], only barely conscious, woke up as he normally did; horny."
    "With his eyes still shut, he clumsily reached for his partner unaware that
    she had already left the bed."

    scene morningwood02 with dissolve

    b2 "Good morning, Beautiful. I hope your beaver is ready for breakfast because
    I've got some morning wood that could dam up the nile!"

    "Avalon was still waking up. Her mind was trying to catch up to what was happening."

    b2 "Come on, Leah. You're usually so eager in the morning. Don't you want to
    hump your Teddy Bear?"

    "It suddenly occured to her that Uncle [player_name] thought she was Leah."

    menu:
        "Loudly alert Uncle [player_name] to his mistake.":
            $ wholesome += 1
            show screen notify("健康 +1", 2.0)
            jump itsmeava

        "Stay silent for a moment, see where things go.":
            $ lewd += 1
            show screen notify("淫荡 +1", 2.0)
            jump staysilent

    label itsmeava:

        scene itsmeava01 with dissolve

        a4 "Uncle, it's me, it's Avalon! I stayed the night, remember?"

        b2 "W-what? Where..? Where's Leah?"

        "[player_name]'s mind began to clear as Avalon's words shook him fully awake.
        He'd realized his mistake and felt a pang of regret."

        scene itsmeava02 with dissolve

        b2 "Oh shit, I didn't realize it was you, Avalon. I hope I didn't freak
        you out."
        b2 "Leah's been pushing me to be more adventurous in bed so I've been
        experimenting with dirty talk."

        a4 "You need more practice."

        scene itsmeava03 with dissolve

        b2 "It's not as easy as it sounds! I've never been that sexually charged
        but Leah is dialed to eleven. I'm trying to catch up to her."

        a4 "Oh, I hadn't pictured her that way. Do you like it?"

        b2 "Usually but she can be too extreme for me sometimes. You know me, I prefer
        a good cuddle over anything else."

        scene itsmeava04 with dissolve

        a4 "I remember cuddling up to you when I was younger. It was comforting being
        in your lap, wrapped up in your big arms. I felt safe there."
        a4 "Maybe I can be your cuddle buddy and Leah can be your sexy playmate!"
        a4 "If we reconnect to that point, I mean."
        a4 "It's weird, I feel like that kid all over again when I'm with you. Like
        we never missed a beat."
        a4 "Why, um, why did you stop coming around?"

        scene itsmeava05 with dissolve

        b2 "I don't have a satisfying answer for you right now, Avalon. But there
        is a reason."
        b2 "I'm glad you're here now though. After breakfast, I have some things
        for you."
        b2 "I smell something delicious cooking. I bet Leah is making breakfast."
        b2 "Do you want to go see?"

        a4 "Sure, yeah. Let's go eat."

        scene itsmeava06 with dissolve

        a4 "Don't forget about my cuddle proposal!"

        b2 "I won't! I'm going to take a shower before I join you and Leah.
        Save me some coffee!"

        stop music fadeout 2.0

        a4 "I love you, Uncle. Thank you for taking care of me last night."

        b2 "I love you, too. And you're welcome."

        jump omlete

    label staysilent:

        scene morningwood03 with dissolve

        b2 "I can take care of you first if you want. I know what you like,
        Gorgeous."
        b2 "You like it rough!"

        "[player_name] pressed his erection into Avalon's behind, situating it
        just in between her butt cheeks."

        scene morningwood04 with dissolve

        "Avalon let out a mild wimper as her head started to spin with arousal."
        "She had never imagined [player_name] as a sexual possibility before."
        "But feeling his huge hand grope her breast and his hard cock pressing firmly
        against her buttocks shone a new light on her Uncle."
        "She was enjoying this. She wanted more!"

        scene morningwood05 with dissolve

        b2 "I don't know what's with the silent treatment but your pussy is speaking
        plenty. Your juices are soaking right through your pajamas!"

        "Avalon finally came to her senses, playing out the consequences in her head of
        what could happen if she let this go further. She had to stop it."

        a4 "U-uncle, it's me! It's Avalon!"

        scene morningwood06 with dissolve

        b2 "Eh? That's an unusual role play idea..."

        "His current situation slowly began to take shape. The voice was all wrong,
        her hair was wrong. This wasn't Leah. This was his niece, Avalon!"

        scene morningwood07 with vpunch

        b2 "Oh shit, Avalon! I didn't mean to--"

        scene morningwood08 with dissolve

        b2 "Woah."

        "[player_name] had leapt up too fast and his momentum carried him right
        off the side of the bed."

        scene morningwood09 with vpunch

        play sound "audio/bodyfallmat.mp3"

        a4 "Oh my God, Uncle [player_name]!"

        scene morningwood10 with dissolve

        a4 "Are you alright? I've never seen you move that fast before."

        scene morningwood11

        b2 "Ow! My friggin' head. Am I bleeding? I think I broke my tail bone."

        scene morningwood12 with dissolve

        b2 "Avalon, I am so sorry. I forgot you were here! I would never do anything
        to hurt you."
        b2 "You know it was just an accident right? I stopped right when I realized!"

        scene morningwood10

        a4 "Are you always so handsy in the morning? And was the beaver comment
        really necessary?"
        a4 "I can't believe you're cheesy even when you're being intimate."
        a4 "You... you touched my vagina, Uncle..."

        scene morningwood12

        b2 "No! I mean, yeah, I did but I didn't feel anything! I swear!"
        b2 "Okay I felt it but I'll block it out! I'll erase the memory!"
        b2 "Can you forgive me?"

        stop music fadeout 2.0

        scene morningwood13

        l2 "What's going on in here? I heard a thud?"
        l2 "Are you alright, Avalon? Did something happen?"

        "Avalon knew how much [player_name] enjoyed a good prank. She wasn't
        sure if Leah would play along but she decided to roll the dice."

        scene morningwood14

        play music "audio/aint_it_funny.mp3"

        a4 "Uncle groped me while I was asleep and touched me in my no-no place."

        b2 "What!? No, I didn't! Okay, I did but that's not the whole story!"

        a4 "He thought I was you and asked me if I wanted to 'hump my Teddy Bear'."

        b2 "I am in so much trouble right now."

        scene morningwood16

        b2 "I would never cheat on you on purpose. I sincerely thought she was you."
        b2 "I will make this right. I will! Whatever I have to do!"
        b2 "Can you ever forgive me?"

        scene morningwood15

        l2 "Avalon, he wakes up like this every morning. It's constant, he's
        insatiable."
        l2 "I have not been on time to work once since I started staying over."
        l2 "The lines he spouts in bed are some of the corniest I've ever heard."
        l2 "But to be honest with you, he has never left me wanting. He always
        satisfies me."

        a4 "Leah, that sounds epic."

        scene morningwood17 with dissolve

        b2 "H-hey! Don't ignore me! I should be punished, right?"

        l2 "And his body is so ripped. I love to just run my hands all over him
        and feel his shredded abs."

        a4 "Oh my God, my friend Dallas is in magnificent shape too. You're right,
        toned is hot!"

        b2 "Am I not in trouble here? What's going on?"

        scene morningwood18 with dissolve

        b2 "Wait, what have you and Dallas gotten up to?"

        a4 "I'm super jealous, Leah. I wish I had someone like Uncle."

        l2 "You say that but [player_name] is actually into some pretty messed up stuff.
        I wouldn't be surprised if he knew it was you the whole time!"

        a4 "Really? Do you think he wants to bang his niece??"

        b2 "She's full of shit, Avalon! She's just trying to mess with you!"

        scene morningwood19 with dissolve

        a4 "What kind of sick pervert would be into his niece!? That's so gross!"

        a4 "Do you think he's going to try to take advantage of me again?"

        b2 "I would never!"

        scene morningwood21

        l2 "Oh yeah, I bet he's fantasizing about it right now!"
        l2 "I can't even imagine the kind of dirty, messed up stuff rolling around
        in that big head of his."
        l2 "He's probably thinking about you right now. In his mind, he's probably
        all..."

        scene morningwood22 with dissolve

        l2 "'Oh Avalon, your boobs are like Medusa; they're turning me rock hard!'"
        l2 "'I've got a shark in my pants and it wants to eat you up!'"
        l2 "'Touch my pee pee, Avalon! I want your cute little butt on my wiener!'"

        scene morningwood20

        a4 "Yeah! And I bet in his mind, I'm just all like..."

        scene morningwood23 with dissolve

        a4 "'Oh, step on me, Uncle! I'm your naughty little niece and I want you
        to do bad things to me!'"
        a4 "'I accidentally fell on your penis! With, you know, my vagina! Whatever
        will I do??'"

        scene morningwood24

        b2 "Alright, I get it. You girls are messing with me. I'm the goose."
        b2 "I'm glad you both have such a great sense of humor over something that I
        did that was obviously terrible."

        l2 "You're too hard on yourself. It was just an accident, you goon!"

        a4 "Yeah, I forgive you, Uncle! And I love you!"

        b2 "I love you too."

        stop music fadeout 2.0

        scene morningwood25 with dissolve

        b2 "I'm going to go take a shower."
        b2 "Though I don't think any amount of soap is going to wash away
        this guilt or this humiliation."

        l2 "Be strong, Teddy Bear! Momma Bear is going to take good care of you tonight.
        I promise!"

        b2 "You better!"

        scene morningwood28 with dissolve

        play music "audio/soft_reminder.mp3"

        play sound "audio/doorclose.mp3"

        "The girls both began laughing hysterically at their on-the-fly collaborated
        prank on [player_name]."

        a4 "Did you see how uncomfortable he was? We got him so good, Leah!"

        l2 "Did you see him apologizing to me? He's so adorable!"

        a4 "He really is a big ol' soft teddy bear, isn't he?"

        stop music fadeout 2.0

        scene morningwood26 with dissolve

        l2 "He didn't go too far, did he? I know we're joking about it but you're
        alright?"

        a4 "Oh yeah, I'm fine. I know he's my Uncle but it was actually kind of exciting!"
        a4 "I can't wait until I have a boyfriend that wakes me up like that."
        a4 "I don't have much experience with sex so I'm looking forward to
        experimenting one day."

        l2 "It can be so much fun! Just make sure your first time is with someone
        you're comfortable with."

        scene morningwood19 with dissolve

        a4 "I haven't met anyone I'd like to share that experience with!"
        a4 "All the boys at school were immature and lame. And the men
        Mom brings home are gross!"
        a4 "You got really lucky with [player_name]. I hope I find someone
        exactly like him!"

        scene morningwood21

        l2 "Oh, exactly like him? Sounds like you may have a crush on your Uncle!"

        a4 "You know what I mean. Don't make it weird, Leah!"

        "Leah was poking fun but she couldn't help but wonder
        if Avalon perhaps was developing intimate feelings for [player_name]."
        "Would it be so unusual for her to feel that way about [player_name]
        especially considering Leah's own situation of being [player_name]'s [persistent.leah_rel]?"
        "She decided to table the thought and proceed with the day for now."

        scene morningwood26 with dissolve

        l2 "I made breakfast! It's probably getting cold, we better hurry."
        l2 "We can talk more over a warm meal. Come on."

        a4 "I'm starving! Breakfast sounds delightful."

        l2 "Oh, let me put on some pants first."

        stop music fadeout 2.0

        jump omlete

    label omlete:

        if wholesome > lewd:

            scene omlete01 with fade

            a4 "Good morning, Leah. I didn't notice you sneak out of bed this morning."
            a4 "What smells so good? Have you been cooking?"

            scene omlete02

            play music "audio/no_goodbyes.mp3"

            l2 "Good morning, Avalon! I usually get up early to fix [player_name] breakfast."
            l2 "Like I said, his diet was terrible! He looks years younger now that
            he's been sleeping more and eating better."

            l2 "Come have a seat. I made plenty for all of us."

            scene omlete03

            a4 "Oh, waffles! They look delicious!"

            l2 "Those are omelets, Avalon. How unusual that you would see waffles.
            They're not even the same color as waffles."

            a4 "You're right, these are obviously omelets. My brain must have malfunctioned.
            Either way, it looks divine!"
            a4 "Thank you for preparing this for us, Leah."

            scene omlete05 with dissolve

            l2 "Did you sleep well? I tried not to hog the sheets."
            l2 "I normally have to fight [player_name] for them because he likes
            to wrap himself up like a burrito sometimes."
            l2 "He's like a tank though! Once he's got those sheets, it's impossible
            to get them back from him."

            a4 "I can only imagine!"

            scene omlete04

            a4 "I slept well except that [player_name] woke up and thought I was you."
            a4 "Apparently he wants your beaver to help him with his wood?"
            a4 "And he was wondering if you wanted to hump your Teddy Bear?"

            scene omlete09

            l2 "That would be my fault, I take full responsibility. He was a shy little
            puppy dog when we got together."
            l2 "I've been trying to get him to be more confident in taking what he wants from me."
            l2 "He was afraid to even touch me at first! I finally had to lay it out for
            him and tell him to take advantage of me any way he wants."

            scene omlete07

            a4 "What do you mean? Any way he wants? Does that mean you just let him
            do anything to you?"

            l2 "Oh I insist on it! I love being forced to do whatever my partner wants."

            a4 "That seems awfully extreme. What if he wants to hurt you? What if he
            goes too far?"

            l2 "When he goes too far is when I orgasm--"

            "Leah decided rather abruptly that she was revealing too much about her
            sexual side to someone who wasn't ready for such extremes."

            scene omlete10

            l2 "I shouldn't have said that. I apologize. I may have gotten carried away."
            l2 "[player_name] and I have been rather active lately in that department
            and it's gotten me thinking unclearly."
            l2 "You'll discover your own interests in the bedroom when you start your
            sexual journey."

            scene omlete08

            a4 "Don't treat me like a child, I'm an adult. I can handle this stuff!"
            a4 "Nothing you say or do could ever compare to the depravity I've seen
            while surfing the internet."
            a4 "There is some messed up stuff on there!"

            scene omlete05

            l2 "I'm not censoring myself because you're young, Avalon. Anyone might
            find this discussion inappropriate."
            l2 "But if you're truly interested, maybe we can talk more about it later."

            scene omlete06

            a4 "You might be right. Perhaps we should focus on things that are more
             wholesome for now."
            a4 "It's hard for me to imagine Uncle that way. I've never thought about
            him as a sexual creature before. He's just wholesome Uncle [player_name]."
            a4 "It's probably best I keep him that way in my head."

            scene omlete07 with dissolve

            a4 "I noticed your tattoo before. I've been meaning to ask about it."
            a4 "Why do you have a tattoo? Are you affiliated with the Japanese mafia
            known as the Yakuza?"

            scene omlete05

            l2 "No, silly! Members of Yakuza usually have a considerable amount of ink."
            l2 "I just have this one little tattoo."
            l2 "My own immune system attacked my heart when I was younger.
            I have this tattoo to remind me of what I'm working so hard for."

            a4 "What are you working hard for?"

            l2 "Well, my own personal longevity for one. My heart probably won't carry
            me into old age."
            l2 "But also millions of other people that need artificial limbs or organs."

            scene omlete06

            a4 "So you must work in the medical field?"

            l2 "More like research and development."

            a4 "Oh, I see. That's really cool, Leah."

            scene omlete11

            b2 "Good morning, ladies. Oh, we're having waffles this morning?!"

            l2 "No, they're omelets!"

            b2 "Oh, my mistake. But there's coffee? Come to papa!"

            l2 "Come sit with us."

            scene omlete12 with dissolve

            l2 "I heard you accidentally confused Avalon for me this morning."
            l2 "The whole 'beaver' bit is overused. You can do better, Teddy Bear."

            b2 "She told you about that, did she? It was an honest mistake!"

            scene omlete14

            a4 "It's alright, Uncle. I'm glad you found someone you're having so much fun with."

            scene omlete13 with dissolve

            stop music fadeout 2.0

            a4 "I'm all finished with breakfast. It was delicious, Leah. Thank you!"
            a4 "Would you mind if I took a shower next?"

            l2 "Not at all! Be my guest."

            a4 "I won't take too long, I promise."

        else:

            scene omlete02 with fade

            l2 "I've already laid it out for us. I was just about to come wake you
            and [player_name] when I heard him crash into the wall."
            l2 "Come have a seat. We'll eat together while [player_name] takes his
            shower."

            scene omlete03

            play music "audio/no_goodbyes.mp3"

            a4 "Wow, these waffles look delicious, Leah! Great work!"

            l2 "Those are omelets, Avalon. You're not having a stroke, are you?"

            a4 "Oh so they are! My mistake. I guess I'm still discombobulated
            from all the excitement this morning."

            l2 "Drink plenty of your orange juice then. That should perk you right up!"

            scene omlete04 with dissolve

            a4 "I'm glad you decided to go along with my prank this morning. I didn't
            know how you were going to react to the situation."
            a4 "I guess I thought making a joke about it was the best way to add levity."
            a4 "And Uncle was always a good sport when it came to being the butt of a joke."

            scene omlete05

            l2 "Oh I know! We've only been dating for a little over a week but we've been
            spending time together for months."
            l2 "What I love most about him is how playful he is! He's just such a fun
            person to be around."
            l2 "What exactly happened though? He woke up horny and got physical right
            away?"

            scene omlete06

            a4 "W-well, to be honest, I may have let it carry on longer than I should have."
            a4 "I could have told him it was me sooner but I wanted to see what he would
            do. Is that strange of me?"
            a4 "I've never woken up to a man that desired me like that before. I was curious
            to see it play out a little."
            a4 "And it's Uncle [player_name] so it's not like I was worried about him
            hurting me. I knew he'd stop once he knew it was me."
            a4 "I've never seen him like that before. It was like seeing a new and
            wild side of him."

            scene omlete05

            l2 "That's adventurous of you, Avalon! I'm impressed. It's unfortunate
            that [player_name] isn't more outgoing with sex."

            a4 "Is he not?"

            l2 "When we first started dating, he was awfully timid when it came to
            sex."
            l2 "He's improved considerably in a short time. We've been having a lot of
            fun and it just gets better and better."

            a4 "What have you been trying to get him to do exactly?"

            scene omlete10 with dissolve

            l2 "Er, well..."

            "Leah paused for a moment to debate whether it was a good idea to divulge
            her fetishes to Avalon."
            "She thought about how wild the morning had been. Avalon was clearly curious
            about sex and daring enough to explore it."
            "But perhaps it was best to keep things simple for now."

            l2 "My partner's pleasure is paramount to me. I derive my own pleasure
            from his pleasure."
            l2 "So right now I'm trying to convince him to do whatever he wants to me
            to satisfy himself."
            l2 "Does that make sense?"

            scene omlete07

            a4 "I understand. You said he's been timid though."
            a4 "I haven't known Uncle to have many partners in his life. His
            relationships don't seem to last long."
            a4 "How are you guiding him to be more adventurous and take what
            he wants?"

            scene omlete05

            l2 "He's actually been relatively simple and predictable in his requests
            so far. I push him to try new things."
            l2 "I expect he'll find his own fetishes and kinks in time."

            scene omlete06

            a4 "What if you and I were in a relationship? How would you find out
            what kinks I'm into?"
            a4 "And would you still get pleasure from pleasing another woman like
            me?"

            scene omlete10

            l2 "U-um, well..."

            "The question caught Leah off guard. Was this a strictly theoretical situation
            or was Avalon interested in her?"
            "She mentioned briefly something about an experience with her friend Dallas
            before. Perhaps Avalon has had experience with a female partner?"
            "If she's only been with a woman before, perhaps she's more comfortable
            with the idea of a female partner right now?"

            l2 "I'm sure I would enjoy playing with you, Avalon. Perhaps in a different
            way than I get enjoyment with [player_name] though."
            l2 "I guess we'd have to find your interests, wouldn't we?"

            scene omlete09 with dissolve

            l2 "What gets you horny, Avalon? Do you like toys? Do you like to be recorded
            playing with yourself or others?"
            l2 "Or do you like to watch other people have sex? That's called voyeurism."

            a4 "Er, I... don't know..."

            l2 "We would just have to start trying things then, wouldn't we?"

            scene omlete07

            a4 "Uhm, yeah, I guess we would."

            "Avalon wasn't sure what she expected when she posed her hypothetical question
            but it certainly wasn't this."
            "As Leah rattled off different kinks, there was a hunger in her eyes. A wanting."
            "Avalon felt butterflies in her stomach as her imagination drifted over each
            fetish that Leah listed."
            "She pictured Leah pressing her against a wall as she slid a vibrator in
            and out of her pussy."
            "She imagined a camcorder in the corner of the room as Leah sat her on
            the table, pressed her face into her crotch and ate her out."
            "She fantasized about watching from the doorway as [player_name] took Leah
            from behind and slammed into her over and over again."
            "Each scenario she imagined gave her a rush of excitement. She wanted
            them all!"

            scene omlete11

            b2 "Good morning again, ladies! I'm all done with my shower."
            b2 "Is that coffee I smell?"

            l2 "Come in. Sit with us."

            scene omlete12 with dissolve

            b2 "So what were you girls talking about? You're not planning your next
            attack against me, are you?"

            l2 "We were just talking about girl stuff."

            b2 "I'm happy to see you two getting along so well. I hope I didn't interrupt
            anything."

            scene omlete13

            a4 "We were just talking about our interests. It was a bonding moment!"
            a4 "Right, Leah?"

            l2 "Yeah, we're becoming fast friends."

            scene omlete14 with dissolve

            a4 "I'm all done eating. Would you mind if I used the shower next?"

            stop music fadeout 2.0

            b2 "Not at all, go right ahead. I wasn't in there long so you should
            have plenty of hot water."

            a4 "Thanks, Uncle!"

            scene omlete13 with dissolve

            l2 "And take your time, Avalon. You don't have to rush. Enjoy your shower."

            a4 "Alright, thank you, Leah."

            jump limitedtime

    label limitedtime:

        if _in_replay:
            $ lewd = 1
            $ player_name = renpy.input("What would you like to name the MC?")
            if player_name.strip() == "":
              $ player_name = "Byron"

        scene limitedtime01 with fade

        pause

        scene limitedtime02 with vpunch

        play sound "audio/dooropen.mp3"

        b2 "Woah! What are you doing, you nutty broad? What are you pushing me
        around for?"

        l2 "Come on, [player_name]! We only have a limited amount of time to
        fool around while Avalon is in the shower."
        l2 "We can't waste it! I know you were horny this morning and I didn't
        get to take care of you."
        l2 "I don't want you to have to go any longer without being satisfied."

        play music "audio/island_hopping.mp3"

        b2 "I didn't even get to finish my breakfast though."

        scene limitedtime03 with dissolve

        l2 "I'm going to make you forget food even exists, [persistent.byron_rel]."

        b2 "How are you going to do that? By clubbing me over the head with a
        nine iron?"

        l2 "No, with these!"

        scene limitedtime04 with dissolve

        b2 "Quick! Call NASA! I've just discovered two new stars in our solar system!"
        b2 "I wonder if they'll let me name them."

        l2 "Yeah, yeah. Get out all your nervous little jokes but do it quickly
        because we don't have a lot of time."

        b2 "Actually, that's all I have. I'm ready for this."

        scene limitedtime05 with dissolve

        l2 "Mm, looks like our week of passionately and sexually exploring each
        other has raised your confidence in the bedroom."

        b2 "I'm not the only one. You were shy about showing off your body the
        first time we fooled around."

        l2 "I'm bigger than most girls. I wasn't sure you'd appreciate my figure."

        show leahsqueeze with dissolve

        b2 "You're bigger in all the right places, [persistent.leah_rel]."

        l2 "Oh fuck, I love it when you call me that. Your hands are so big it feels
        like you could crush me and I hope you do!"
        l2 "Tell me what you want, [player_name]. Tell me what you want to do to me."

        b2 "I want to see how far I can get my cock down your throat."

        l2 "Yes! That's how I want you to talk to me!"
        l2 "We have to get your pants off first."

        scene limitedtime08 with dissolve

        "Leah knelt down in front of [player_name] and began pawing at the
        button and zipper on his pants."
        "She was ferociously eager to take his substantial cock in her mouth
        until he was satisfied."

        l2 "I can feel your erection through your pants, [persistent.byron_rel].
        You want me bad, don't you?"

        b2 "You're goddamn right I do."

        scene black with dissolve

        "Meanwhile..."

        scene limitedtime09 with fade

        "Avalon peered back at herself in the mirror as she thought back on the
        last time she stood before this mirror."
        "She was a young teenager back then still growing into the woman she would become."
        "Standing here now, she appreciated her new maturity. She wondered if anyone
        else did too?"
        "She was curious if Uncle [player_name] saw her differently now that she was
        all grown up."

        scene limitedtime10 with dissolve

        "Avalon instinctively reached for her toothbrush."
        "Noticing it wasn't atop the sink, she quickly realized she'd accidentally
        left it in her room."

        scene limitedtime11 with dissolve

        "She had a decision to make: should she get the toothbrush from her
        room clad in only a towel or brush her teeth later?"

        menu:

            "Go get the toothbrush.":
                $ lewd += 1
                show screen notify("淫荡 +1", 2.0)
                $ caughtncum = True

            "Wait until later.":
                $ wholesome +=1
                show screen notify("健康 +1", 2.0)
                $ caughtncum = False

        scene limitedtime13 with fadefast

        l2 "It gets bigger every time I see it! You really are my {b}big{/b}
        [persistent.byron_rel]!"
        l2 "Once I put this in my mouth, I don't want you to take any mercy on
        me. You get your satisfaction no matter what."
        l2 "If I gag, you keep going. If I choke, you don't stop. If I pass out,
        you have my permission to keep fucking my mouth until you're finished."

        b2 "If that's what you want, that's what you'll get. But remember,
        pinch my leg if I go too far."

        scene limitedtime14 with dissolve

        "Leah positioned her hands behind her rear and swore to herself that
        she wouldn't use them no matter what happened."

        l2 "Right, I'll pinch your leg if I want to stop."

        scene limitedtime15 with dissolve

        "She had no intention of stopping him, no matter how far he went."
        "Nothing gave her more pleasure than pleasing her partner. And all the
        training she had done with him had pushed him far past his limits."
        "Leah imagined herself as a helpless doll sewn together for the sole
        purpose of being his fuck toy."
        "She wanted him to do anything he desired to her."
        "Imagining his pleasure and his climax drenched her panties.
        Leah's excitement could be measured in fluid ounces."

        scene gagforme01 with dissolve

        b2 "Are you ready, Leah?"

        "She wiggled her head slightly and positioned her tongue under the
        tip of his penis, out of the way of the incoming cock."

        l2 "Mhmm."

        b2 "I want you to take the tip all the way into your mouth."

        show gagforme1

        "Leah felt the tip of his penis begin to fill her mouth until it was
        all the way in."
        "It was nearly enough to take up the entire area all by itself."

        b2 "Excellent. I can feel the tip of my dick pressing against your throat.
        You can handle more, though, can't you?"

        l2 "Mhmm."

        show gagforme2

        "[player_name] pulled her head foward, forcing his erection down her
        throat. She was able to successfully suppress an emerging gag."

        b2 "Oh yes, that's it. Good girl."
        b2 "Now I'm going to slide my cock out of your throat and then right
        back into it."

        l2 "Auk"

        "Unable to speak, Leah released the only noise she could; a mild choking
        sound."

        show gagforme3

        b2 "I can feel your mouth filling up with saliva."

        "Leah took hard inhales through her nose whenever his cock would leave
        her throat. She was only catching brief moments to breathe."

        "Her body would panic every now and again, instinctively pulling back
        in an attempt to remove the foreign object."
        "But [player_name]'s grip was firm and she didn't get far when
        she did."

        ## Lewd Path ##
        if caughtncum:

            scene limitedtime16 with dissolve

            "Enthralled by his lover's current devotion to his pleasure, [player_name]
            didn't notice his niece walking down the hall."

            b2 "I can't believe how far you can take my cock down your throat, Leah."

            scene limitedtime17 with dissolve

            "Avalon turned her head in curiosity at the sound of her Uncle's voice as
            she secured her towel."
            "What she saw made her leap back in shock, pulling loose the bit
            of towel she was tucking in."

            scene limitedtime18 with dissolve

            a4 "Uncle! Oh my God, I'm so sorry!"

            "Having been untucked, Avalon's towel found itself subject to gravity and
            fell towards the ground."
            "[player_name] looked up to find a panicked Avalon standing before his doorway."

            scene caughtncum01

            b2 "Oh shit! Avalon! You were supposed to be in the shower!"

            scene caughtncum02 with dissolve

            "Feeling a desperate need to cover himself, [player_name] used the
            only thing he had at hand; Leah's head."
            "He pulled her in towards himself hard, entirely forgetting that
            she was even there."
            "Leah gagged as [player_name] jammed his cock further down her throat
            than she could handle."

            scene limitedtime19

            "Avalon was also caught up in the moment and didn't yet notice her towel
            resting on the floor by her feet."
            "Her naked body was on full display to her Uncle and he couldn't help
            but notice."
            "His mind quickly drifted away from the moment, entranced by her youthful
            and petite features, perfectly toned from years of cheerleading."
            "He couldn't help but imagine sliding his hands across her smooth, bare
            skin."
            "He wanted to lay her on the bed, spread her legs and feel the tip of
            his penis slowly part her lips as he pressed his dick inside of her."

            scene caughtncum04

            "And with that last thought, he began to ferociously cum down Leah's
            throat, pulling her head even harder into himself."

            scene caughtncum03 with flash

            "Leah could feel his warm cum shooting down her esophagus straight into
            her stomach."
            "Her body began to convulse as she gagged, choked and tried to swallow
            all at the same time."
            "She instinctively began pushing back against [player_name], desperately
            trying to remove the object lodged in her throat."

            scene caughtncum03 with flash

            "She could feel herself losing conciousness as another wave of cum began
            firing down her throat."
            "There was so much semen entering into her stomach, she began to feel
            as if she'd just eaten a full meal."
            "Her stomach was filling up with her [persistent.byron_rel]'s seed."

            scene limitedtime20

            "Avalon finally came to her senses, realizing her situation."

            a4 "Oh shit, my towel!"

            scene limitedtime21 with dissolve

            a4 "I didn't mean to--"
            a4 "I should have said something! I'm so sorry, Uncle!"

            scene caughtncum04

            "[player_name]'s face was contorted in a weird, cross-eyed state as
            his intense climax scrambled his mind."
            "It occurred to Avalon that this may not be the best time for apologies."

            scene limitedtime22

            "She darted back to the bathroom as quickly as her feet would carry her,
            leaving behind her towel."
            "As soon as Avalon had gone, [player_name] snapped back to his senses
            as well and realized Leah's predicament. He let go of her head with haste."

            scene limitedtime23

            "Leah began to cough violently as she fell to the ground. Her throat
            felt sore and bruised from the ordeal."

            b2 "I didn't hurt you, did I? I forgot you were there."

            "She took deep breaths in between her coughing fits."

            b2 "Jesus, why didn't you pinch my leg?? I didn't know I was hurting
            you, Leah."

            scene limitedtime24 with dissolve

            "Leah spoke with a raspy voice."

            l2 "I'm pretty sure I came twice. That was perfect."

            scene limitedtime23 with dissolve

            "She continued coughing, her body still confused by having something
            poured directly into her stomach without having swallowed it."

            b2 "This was supposed to be a controlled, safe environment but it feels
            like we should have taken more precautions."
            b2 "I don't want you to get hurt, Leah."

            scene limitedtime24 with dissolve

            l2 "I'm fine, that was amazing. But what happened? You usually last
            so much longer."
            l2 "Was that Avalon's voice I heard? Did she forget something?"

            b2 "She popped out of the bathroom and saw you gobbling
            down on my knob."
            b2 "I guess we should have closed the door."

            scene limitedtime25 with dissolve

            l2 "Is that her towel on the ground? Did it fall when she saw us?"
            l2 "Is that... is that why you came so fast? You saw her naked?"

            b2 "Uhh, it's all a little hazy... I don't think that's what happened."
            b2 "It must have been the surprise of it all."

            l2 "Do you want her, [player_name]? I'll get her for you if you want her."

            scene limitedtime26 with dissolve

            b2 "What!? No! She's my niece, I don't want to have sex with her."
            b2 "That would be wrong, wouldn't it?"

            l2 "I'm your [persistent.leah_rel] and we've embraced that passionately.
            I'd even say we've developed a fetish for it."
            l2 "Having relations with your niece who you're not even related to
            would be mild in comparison."
            l2 "She's interested, [player_name]. I can tell. She's ready to start
            experimenting. Who better to do it with than us?"
            l2 "We'll keep her safe and teach her everything she needs to know."

            b2 "I don't want to do anything that would hurt her, Leah."

            l2 "We wouldn't! I swear, we could just put out the offer. We wouldn't
            do anything she doesn't want to do."
            l2 "Do you want her, [player_name]? Do you want to fuck your niece?"

            menu:
                "Yes, I'm sexually interested in Avalon.":
                    $ lewd += 1
                    show screen notify("淫荡 +1", 2.0)

                    l2 "It's going to take some time but I'll get her for you,
                    [persistent.byron_rel]."
                    b2 "You're not jealous? You're not mad?"

                    stop music fadeout 2.0

                    l2 "No, your pleasure is my paramount concern. I'll tear the
                    sun from the sky for you, my love."
                    l2 "I'll meet you in the kitchen soon. I have a towel to
                    deliver."

                    jump toweldelivery

                "No, I don't desire her sexually.":
                    $ lewd = 0
                    $ wholesome += 2
                    show screen notify("健康 +2", 2.0)

                    l2 "Okay, if you're sure then I won't chase her for you."

                    stop music fadeout 2.0

                    l2 "Let me put a shirt on and I'll bring her towel to her."
                    l2 "I'll meet you in the kitchen in a few minutes."

                    $ renpy.end_replay()

                    jump toweldelivery


        ## Wholesome Path ##
        else:

            "Sensing her difficulty to  breathe, [player_name] made an excuse to
            give her a rest."

            show gagforme_r with dissolve

            pause (.7)

            show breathenow

            b2 "Is that as far as you can take it? I thought you could handle
            more?"

            l2 "I'm sorry, [player_name]. I can't open my throat any wider."
            l2 "You'll have to just force your cock down my esophagus."

            b2 "Open your mouth and we'll try again. I'm going to push a little
            harder this time, [persistent.leah_rel]."

            l2 "Yes, big [persistent.byron_rel]."

            scene gagforme01

            "[player_name] positioned the tip of his penis back into Leah's mouth."

            show gagforme1

            b2 "Take the tip all the way into your mouth like a good girl."
            b2 "And now take a deep breath to help pull my cock into your throat."

            show gagforme2

            b2 "That's not far enough, Leah. You need to take more."

            "[player_name] began applying pressure to the back of her head, forcing
            his erection deeper into her throat."

            show gagforme4

            "As his dick slid further down, she began to gag reflexively. Her body
            twitched as it tried to pull back away from the foreign object."
            "[player_name] held her head more firmly each time she involuntarily
            writhed."

            b2 "We're so close now, Leah. Just a little bit more."
            b2 "Here, let me help you get over that last hump."

            scene gagforme59 with vpunch

            "With one strong pull, [player_name] forced himself as far down her
            throat as he could go."
            "Leah was choking harshly now, gagging and convulsing as her body
            desperately tried to dislodge the object."
            "Her airway was completely cut off and she could no longer draw breath."

            b2 "Oh that's perfect, Leah! Just like that! You have all of my cock
            now, [persistent.leah_rel]."
            b2 "Now I'm going to fuck your face until I climax."

            show gagforme5

            "[player_name] use his heavy grip to move her head back and forth on
            his dick, allowing her to take the entirety of it over and over again."
            "Her tight throat squeezed his erection while keeping it lubricated
            with her spit."
            "Her constant attempt to draw air into her lungs only served to give
            [player_name]'s cock more stimulation as she pulled him deeper down."
            "Leah had been holding her breath for too long now. She could feel panic
            begin to set in."

            b2 "Oh fuck, Leah, I'm cumming! Just hold on a little longer!"

            scene gagforme59 with vpunch

            "[player_name] yanked Leah's head forward as his dick began to quiver,
            readying itself for the climax."

            scene gagforme59 with flash

            b2 "Fuck yes, here it is! Take my cum, Leah! Swallow all of it!"

            "Leah could feel a warm, creamy liquid shooting straight down into her
            stomach."
            "She had been without air for so long now, she could feel herself
            becoming faint."

            scene caughtncum02 with flash

            "[player_name] used his second hand to push her head down onto his
            cock even harder as his climax continued."

            b2 "All of it, Leah! Drink all of me! Fuck yes, this feels so amazing!"

            "Another wave of cum exploded down her throat and she could feel her
            stomach filling up with his seed."
            "Just as she started to fall unconscious from the lack of oxygen,
            [player_name] finally released her."

            show breathenow with dissolve

            b2 "Oh fuck, are you okay? Did I take it too far?
            I get carried away when I ejaculate."
            b2 "I didn't hurt you, did I? You never pinched my leg."

            "Leah took deep, gasping breaths. She barely avoided passing out."

            l2 "It was perfect, [player_name]. My [persistent.byron_rel]'s cum
            is my favorite! I'd take more if you'd give it to me."
            l2 "I came at least twice myself. I love being your fuck toy! It gets
            me so horny."

            stop music fadeout 2.0

            b2 "Maybe it's my turn to get you off."

            l2 "We don't have time. Avalon will be done any minute. We'll have
            more fun tonight, Bear. I promise."

            if persistent.limitedtime == False:
                $ renpy.notify("You've unlocked Limited Time in the gallery!")
                $ persistent.limitedtime = True

            $ renpy.end_replay()

            scene baitset05 with fade

            b2 "That was incredible, Leah. Your throat must be sore now. Do you
            want some ice cream or a cold glass of water?"
            b2 "I'm sure I have some ibuprofen around here somewhere."

            scene baitset06

            play music "audio/soft_reminder.mp3"

            l2 "Nope! I'm fine. It's not bothering me too bad at all."
            l2 "I'm just happy I got to please you this morning. I was afraid
            I wouldn't get the chance."

            scene baitset04

            b2 "Your pleasure is important too, Leah. Even if you think it's not
            important to you, it's important to me."
            b2 "Let's make sure we take turns. Next time, I'm taking care of you."

            scene baitset08

            l2 "Well look at you taking charge. You know you can do whatever you
            want to me."
            l2 "I'm also still opening you up to new ideas, [player_name]. There
            will be plenty of time for me after we get you more confident with sex."
            l2 "There's got to be something you're interested in that you're
            not telling me, [player_name]."

            scene baitset07 with dissolve

            l2 "Whatever it is, I'll try it with you."

            scene baitset03

            menu:

                "I've been thinking about a threesome, namely with Avalon." if lewd >= wholesome:
                    $ lewd += 1
                    show screen notify("淫荡 +1", 2.0)
                    b2 "No no, I couldn't say. It's too crazy."

                    l2 "Whatever it is, no matter how crazy, we can at least
                    talk about it."

                    b2 "I don't know, Leah. I don't want you to think of me
                    differently."
                    b2 "What if it's something you're so opposed to that it
                    puts a wedge between us and drives us apart? I don't want that."

                    scene baitset07

                    l2 "[player_name], I know we've only been sexually involved
                    with each other for a week but listen to me."
                    l2 "My foster parents had the most boring sex life. They
                    barely ever even touched each other!"
                    l2 "I swore to myself that when I got older I would take
                    the opposite from my partner. I would try anything and everything!"

                    scene baitset09 with dissolve

                    l2 "My heart is doing well right now. It will probably last
                    many more years. But if something happens..."
                    l2 "I don't want to live with regrets. And I want my partner,
                    you, to enjoy every moment with me."
                    l2 "So that you can look back on your memories with me fondly
                    and know I gave you all that I could."

                    scene baitset05

                    b2 "Jesus, Leah. D-don't talk like that. That's what I want,
                    first and foremost!"
                    b2 "From what you've told me, you have decades before your
                    heart begins to fail. By then, who knows where technology will be!"

                    scene baitset04 with dissolve

                    b2 "But if that's really how you feel then I'll tell you.
                    No matter what happens, I don't want to lose you."
                    b2 "If you don't like anything I propose, we forget about it! Deal?"

                    l2 "Deal!"

                    scene baitset03 with dissolve

                    b2 "I was sort of thinking it might be interesting to bring
                    another player into the mix?"
                    b2 "Maybe we could experiement with more women?"
                    b2 "I mean, I picture you with another girl sometimes and it
                    thrills me considerably."

                    scene baitset08

                    l2 "Oh. I did not expect that. You want to see me fool around
                    with another woman?"
                    l2 "Do you want to fuck another woman too? I wouldn't mind getting
                    one for you. A threesome could be a lot of fun!"
                    l2 "Did you have someone in mind?"

                    b2 "W-well, I uhh..."

                    scene baitset07 with dissolve

                    l2 "Wait, don't tell me. You... are you interested in Avalon?
                    Is that what this is about?"

                    b2 "Err, wait, this went too far. I didn't--"

                    l2 "She looks like a princess straight out of a fairytale.
                    And she's technically your niece so it's a bit wrong, isn't it?"
                    l2 "But you and I know exactly how sweet forbidden fruit can be, don't we?"
                    l2 "I could shake that tree for you and see if any apples fall out of it."

                    scene baitset02

                    b2 "Oh shit, you're way more into this than I expected."
                    b2 "Look, I don't want to do anything that would damage her. She's
                    deeply important to me and I want the best for her."
                    b2 "I just feel like she's put it out there recently that she is
                    interested in sex and it got me thinking about her... naked."
                    b2 "Oh fuck, what's wrong with me?"

                    scene baitset09

                    l2 "We would never do anything to hurt her, [player_name].
                    I could just see if she's interested in fooling around with us."
                    l2 "She's ready to explore her sexuality and who safer to do
                    that with than us?"
                    l2 "And if she isn't interested, we'll drop it immediately! I promise!"

                    b2 "Okay, right, only if she's interested."

                    scene baitset06 with dissolve

                    l2 "And if Avalon isn't interested, we can always find someone
                    else if you want."
                    l2 "I'm sure there's plenty of women that would be interested in
                    fooling around with a couple like us!"
                    l2 "I think I heard the shower stop. I'm going to see if I
                    can switch places with her and start my shower now."
                    l2 "We can talk more about this later when we have more time."

                    scene baitset04

                    b2 "Hey, thanks for being so understanding about this. I feel
                    silly for being so worried about telling you now."
                    b2 "I'm going to be more open about what I want from now on."

                    l2 "I love you, my Teddy Bear! I'll give you anything I can!"
                    l2 "Shower time! I'll be out soon."

                    stop music fadeout 2.0

                    jump thering

                "I appreciate the simple things like cuddling and romantics.":
                    $ wholesome += 1
                    show screen notify("健康 +1", 2.0)

                    b2 "I'd like our relationship to be about more than just sex, Leah."
                    b2 "I enjoy our sexual ventures immensely and I don't want to
                    slow down at all but I'd like to cuddle more."

                    scene baitset04 with dissolve

                    b2 "I enjoy just watching movies with you or going on dates."
                    b2 "I want to shower you with attention, compliments, and gifts."
                    b2 "I want to see that beautiful smile every morning because
                    it sets up my entire day to be perfect."
                    b2 "I don't need anything else, Leah. Just those green eyes
                    looking affectionately up at me and I'm happy."

                    scene baitset06

                    l2 "Aw, Teddy Bear. You're going to make me cry if you
                    keep that up."
                    l2 "You're right, though. We have focused a lot on sex lately.
                    It may be more appropriate to say that I've focused more on sex lately."
                    l2 "I'll be more inclined to be more romantic and not so lustful
                    once we settle into our relationship."
                    l2 "The first month of a new relationship is always hyper-sexual, right?"

                    scene baitset04

                    b2 "We don't have to slow down on the sex. Ever! But the
                    other things are important too."
                    b2 "And after seeing Avalon again, I know I want her to be a
                    big part of my life again."
                    b2 "I want all of us to set aside some time to bond; go to the theater,
                    visit a musuem or just take a walk together."

                    scene baitset06

                    l2 "Those all sound like lovely things for us to do. It's a wonderful idea."
                    l2 "Avalon seems like a wonderful young lady, I'm eager to get to know her better."
                    l2 "If you plan something out for us, I'd be excited to do it together."

                    l2 "I think I heard the shower stop. I'm going to try to switch places
                    with Avalon and start my shower now."
                    l2 "I love you, Teddy Bear."

                    stop music fadeout 2.0

                    jump thering

                "I'd like to focus on starting a career." if lewd < wholesome:
                    $ wholesome += 1
                    show screen notify("健康 +1", 2.0)

                    b2 "I'm satisfied with the direction our sexual activities have been going."
                    b2 "There's nothing I can think of that I'd like to try in that respect."
                    b2 "But aside from that, I would like to focus on finding a career or hobby
                    I'm interested in."

                    scene baitset04 with dissolve

                    b2 "Watching you be so dedicated to your work has inspired me to find something
                    of my own. I'm not sure what that might be but I want to start looking."
                    b2 "Would you mind helping me find something in that area I'd be interested in?"

                    scene baitset08

                    l2 "Oh. I didn't expect that. I guess since it's the beginning of
                    our relationship, I've tunnel visioned in on the sexual aspect."
                    l2 "If you're eager to find a hobby or career you're passionate about,
                    I'd love to help you discovery it!"
                    l2 "Do you have any ideas currently on what you might be interested in?"

                    scene baitset02

                    b2 "Er, no, actually. I honestly have no idea!"

                    l2 "Would you like to learn a musical instrument? I could
                    teach you a little bit about knitting?"
                    l2 "Cooking? Painting? Dancing? Writing? Fishing--?"

                    b2 "L-let me think on it, I'm not sure yet."

                    scene baitset06

                    l2 "Oh, sweetie, I apologize. I didn't mean to push too hard."
                    l2 "I'll tell you what; you find something online that looks
                    interesting and we'll try it together!"
                    l2 "I'm proud of you for wanting to try new things. I'll support
                    you however I can."

                    scene baitset05

                    b2 "Really? That's wonderful to hear. Thank you, Leah."

                    l2 "Of course!"

                    b2 "Do you think I'm too old to start learning something new
                    though? I'm almost thirty now!"

                    scene baitset07

                    l2 "You are such a goon sometimes. You're not too old to start
                    learning a new trade or hobby."
                    l2 "Heck, a lot of people these days don't start a career
                    until well into their thirties! Sometimes even later!"

                    scene baitset06 with dissolve

                    l2 "You ponder on what you'd like to do. I'm pretty sure I
                    heard the shower stop."
                    l2 "I'm going to go trade places with Avalon and hop into
                    the shower myself."
                    l2 "I love you, you big goofy Teddy Bear!"

                    stop music fadeout 2.0

                    jump thering

        label toweldelivery:

        scene limitedtime27 with fadefast

        play sound "audio/doorknock.mp3"

        l2 "Avalon? Can I come in? I have your towel here."

        a4 "I didn't see anything, Leah! I promise! I uhh... I blacked out!
        Yeah. And there was something in my eye too!"

        l2 "I know you're just being polite but it was our fault for not closing
        the door. Please don't be embarrassed, we were just fooling around."

        a4 "You can... you can come in."

        if lewd > wholesome:

            scene limitedtime28 with dissolve

            play music "audio/soft_reminder.mp3"

            l2 "[player_name] and I have been excessively lustful lately. We
            can't seem to keep our hands off each other."
            l2 "He's getting so damn good at sex I just can't help myself."
            l2 "How much did you see, Avalon? We weren't too graphic for you,
            were we?"

            scene limitedtime30

            a4 "I've never seen two people being intimate with each other like that before.
            I mean, in movies and stuff but never in real life."
            a4 "What you and [player_name] were doing... that was a blowjob, right?"
            a4 "I heard you choking though. I thought he was hurting you. Are you alright?"

            scene limitedtime28

            l2 "[player_name] would never hurt me, Avalon. We like to push the
            limits of our sexual exploits."
            l2 "The more of him I can get down my throat, the more enjoyable it
            is for him. So I let him deep throat me whenever he wants."
            l2 "But we're always safe and we take precautions. We never do anything
            that the other isn't comfortable with."
            l2 "He would have stopped immediately if I'd have pinched his leg."

            scene limitedtime31

            l2 "Here is your towel back. You dropped it outside of [player_name]'s
            room."

            a4 "Oh, right. Thank you for bringing it back to me."
            a4 "I can't believe I didn't even notice it fell off."

            scene limitedtime32 with dissolve

            a4 "[player_name] saw me completely naked, didn't he?"
            a4 "After being with you, I bet I just look like a little girl to him."

            scene limitedtime33 with dissolve

            a4 "By the way, I think you forgot to put a shirt on before you came
            in here. Your breasts are on full display right now, Leah."

            l2 "I must have rushed in here without thinking. Silly me. But it's alright,
            isn't it? We're both girls after all."

            a4 "Your tatas are gimongous, Leah! Were you bitten by a radioactive
            boob spider or something?"
            a4 "How do you walk without toppling forward from being so top
            heavy?"

            scene limitedtime34

            l2 "I hear comments like that all the time but I'm just used to them
            now. They're totally normal to me."
            l2 "When I was fifteen, they grew seemingly overnight. I started
            getting a lot more attention from boys."
            l2 "Unfortunately, my heart condition started around that time so
            I never had a chance to date anyone."

            a4 "Probably for the best. Boys are stupid! We deserve proper gentlemen
            if you ask me."

            a4 "They, um... they look really firm but squishy at the same time.
            Are they real?"

            scene limitedtime35 with dissolve

            l2 "They're as real as they come. Do you want to touch them?"
            l2 "They feel even better than they look."

            a4 "Is that even possible? And how are you so thin with such big breasts?"

            scene limitedtime36 with dissolve

            l2 "I have to eat a healthy diet so I don't overstress my heart with
            extra weight and clogged arteries."
            l2 "I exercise regularly too in order to keep my heart as strong as
            it can be."
            l2 "And it's worth mentioning how important core strength is to
            be able to carry around the twins comfortably."

            a4 "Your heart condition has sort of defined your life, hasn't it?"

            a4 "Hey, are you sure [player_name] is alright with this?"
            a4 "I don't want to do anything that might cause trouble for you two."

            l2 "Trust me, if he were watching this right now, he'd be in Heaven."

            scene limitedtime37 with dissolve

            l2 "Go on, get yourself a handful."

            a4 "Well, if you're sure..."

            scene limitedtime38 with dissolve

            a4 "Wow! They really are firm but squishy at the same time! It fills
            up my whole hand and more!"

            l2 "You can't appreciate one without the other. Go ahead, feel the other
            one too."

            a4 "You don't have to ask me twice!"

            scene limitedtime39 with dissolve

            a4 "It's perfect just like the other one. This body is too good for
            mortal men, Leah."
            a4 "And your nipples are still hard from earlier?"

            l2 "To be honest, this is mildly arousing in itself."

            a4 "I can see why Uncle [player_name] can't keep his hands off you."
            a4 "I bet if I had a body like yours, he'd want to touch me all the time too."

            scene limitedtime40 with dissolve

            l2 "Don't sell yourself short, Avalon. You've got a magnificent body
            too!"

            a4 "What are you--?"

            scene limitedtime41 with dissolve

            a4 "Oh! You, uh, want to see mine now?"

            l2 "We're sharing, aren't we?"

            a4 "R-right, sure. But like I said, mine aren't very impressive."

            scene limitedtime42 with dissolve

            l2 "Actually, [player_name] usually lasts a lot longer when I'm giving
            him head."
            l2 "He climaxed as soon as he saw you naked, Avalon. It was quite a surprise!"

            scene limitedtime43 with dissolve

            a4 "No, he didn't. Come on. You're just saying that to flatter me."

            l2 "I'm being sincere, he told me himself. You have a petite frame which
            a lot of guys are actually fond of."
            l2 "And your breasts are plenty! A perfect handful."

            scene limitedtime42 with dissolve

            a4 "Did uncle really say he likes my body?"

            l2 "Can you blame him? You have smooth, youthful skin, a toned physique
            and those adorable freckles."
            l2 "And I bet you have a booty to die for after all those years of cheerleading."

            show nipplepull with dissolve

            l2 "Look at these adorable little nipples you have, Avalon."
            l2 "[player_name] would love to play with these, I'm sure!"

            a4 "Ooh, they're sensitive, Leah. Please be gentle."

            l2 "I can just imagine [player_name]'s rough hands feeling their way
            around your small, petite features."
            l2 "They would inevitably start heading south, down past your stomach
            and--"

            a4 "L-Leah, I'm beginning to get overwhelmed. I think we should maybe
            stop for now."

            scene limitedtime46 with dissolve

            l2 "Oh! I apologize, Avalon. I got carried away, didn't I?"
            l2 "I'm still fired up from earlier with [player_name]. I didn't mean
            to take things too far."

            a4 "Oh, no, really it wasn't too far. I just... I get nervous. I'm
            not very experienced with all this."

            l2 "I would never do anything you don't want me to, Avalon."

            a4 "Okay, right, of course not."

            "Leah felt as though she had set the course perfectly to entice
            Avalon into her's and [player_name]'s sexual endeavors."
            "Avalon was already curious and seemed eager enough with hardly
            any encouragement."
            "Now it was time for the final push."

            scene limitedtime47 with dissolve

            l2 "But if there ever is something you want me to do to you, all
            you have to do is ask."
            l2 "Anything at all. Do you understand what I'm saying, Avalon?"

            a4 "Y-yes, I understand."

            l2 "There's a whole world of pleasure you haven't seen yet. Say the
            word and I'll show it to you."

            "Avalon's eyes were glued to Leah's. She was utterly entranced by
            Leah's extremely forward proposal."
            "But anything? Would that include... [player_name]?"
            "She could feel herself being overcome by desire. She was simultaneously
            nervous and aroused. She wanted to both stop and continue."
            "But Leah wasn't here to play with Avalon. She only wanted to plant
            the seed of curiosity."

            scene limitedtime48

            l2 "Have a wonderful shower, Avalon! Shout if you need any extra shampoo."

            a4 "Oh, you're-- Yeah, okay. Shower. Right."

            scene limitedtime49

            play sound "audio/doorclose.mp3"

            "Leah went into the bathroom with a specific goal in mind and that
            goal was to seduce Avalon."
            "There was no doubt in her mind that everything went as well as
            it could have."
            "[player_name] would have what he desired in no time at all."

            scene limitedtime50

            "Avalon stood dazed as if spellbound. Her mind seemed to shut down
            all motor functions as it attempted to process what just happened."
            "Anything. Anything. Her mind kept playing the word over and over."
            "What would that include? The possibilities began shuffling through
            her brain. Would Leah really do... anything?"

            scene limitedtime51 with dissolve

            "The entire morning of events had left her concupiscent. She had never
            been so horny in her entire life."
            "She wanted it, all of it. Not just anything but {b}everything{/b}."
            "But could she work up the courage to say that to Leah? She was
            awfully timid after all."

            scene limitedtime52 with dissolve

            stop music fadeout 3.0

            "She finally decided to set aside the thought as she desperately needed
            a cold shower."
            "Her legs had become drenched from her pussy overflowing with her
            own juices. She had truly never been so aroused before."
            "The word continued to echo in her head as she headed into the shower:"
            "Anything."


            if persistent.limitedtime == False:
                $ renpy.notify("You've unlocked Limited Time in the gallery!")
                $ persistent.limitedtime = True

            $ renpy.end_replay()

            scene baitset01 with fade

            play music "audio/soft_reminder.mp3"

            l2 "There you are, Bear. I was expecting you to be in your room still.
            Did you finish your breakfast?"

            scene baitset02

            b2 "No, I've been worried about what was going on in there. I don't
            want to corrupt Avalon, Leah."
            b2 "I care about her, I'd do anything for her. I'm not sure a sexual
            relationship with her is something we should be pursuing."
            b2 "When I said 'Yes' earlier, I wasn't thinking straight. I was aroused.
            I don't want to push her into something that she doesn't want."

            scene baitset09

            l2 "I would never hurt her, [player_name]. She's expressed interested
            in sex while she's been here."
            l2 "And judging by how quickly you ejaculated down my throat earlier,
            you're interested in her."
            l2 "We can show her the pleasures of sex in a safe, controlled environment.
            And we won't ever make her do anything she doesn't want to do."
            l2 "I mean, she can have fun with us or some random frat boy when
            she goes off to college. Which do you think is better for her first time?"

            scene baitset03

            b2 "I hadn't really thought of it that way. You're right, she would be
            safer with us."
            b2 "I don't like the idea of some college punk getting her knocked up
            and ruining the rest of her life."
            b2 "We would always have her best interest in mind. And we could introduce
            her to advanced things slowly and at her pace."
            b2 "But all this is under the assumption that she even wants this with
            us, Leah. Did she... seem interested?"

            scene baitset07

            l2 "I presented the idea to her and I'm sure she's considering it now.
            I made sure to be subtle about it."
            l2 "Well, perhaps less subtle than I originally intended."

            b2 "What happened in there?"

            l2 "Let's just say we got a feel for each other. She was excited by
            the idea that you found her body enticing."
            l2 "I'm just sure she's interested in us, [player_name]. I can feel it!"

            scene baitset04

            b2 "I'm sure if you're the one guiding her into her sex life, she'll
            enjoy it considerably."
            b2 "I've never been adventurious or outgoing when it came to sex until
            you pushed me in the right direction. Now I'm enjoying it more than ever!"
            b2 "Whatever happens, I want her to be happy and well taken care of.
            Nothing is more important than that."

            scene baitset06

            l2 "I agree whole-heartedly, [player_name]! We'll make sure that no matter what
            she decides, she's safe and happy."
            l2 "I think I heard the shower stop. I'm going to see if I can go
            switch places with Avalon."
            l2 "I love you, Teddy Bear!"

            b2 "I love you too, Leah."

            stop music fadeout 2.0

            jump thering

        else:

            scene limitedtime29 with dissolve

            play sound "audio/doorclose.mp3"

            play music "audio/a_quiet_thought.mp3"

            l2 "I sincerely hope we didn't freak you out. [player_name] and I
            are still in the early stage of our relationship."
            l2 "We're having a lot of trouble keeping our hands off each other.
            We're just utterly consumed by lust right now."
            l2 "It should settle down in a month or two but that's no excuse. We
            should still have been considerate of you, Avalon."

            scene limitedtime30

            a4 "You don't have to apologize, Leah. I'm glad you and Uncle are
            enjoying each other."
            a4 "I just... I've never had a relationship that intimate with a boy
            before. I was surprised, that's all."
            a4 "I'll be more careful in the future not to stumble in on you."
            a4 "Can I, um... have my towel now?"

            l2 "Oh, yes, here you are."

            scene limitedtime31 with dissolve

            a4 "Thank you, Leah."

            l2 "When you finish your shower, I believe [player_name] has something
            for you."

            a4 "Oh? Did he say what it was?"

            scene limitedtime32 with dissolve

            l2 "It's a surprise. But it's something to look forward to and to take
            your mind off this fiasco."

            stop music fadeout 2.0

            a4 "Alright. I shouldn't be too long."

            l2 "Be sure to leave me some hot water."

            scene baitset01 with fade

            play music "audio/soft_reminder.mp3"

            l2 "There are you, Bear. I thought you'd still be in your room.
            What are you doing in here?"

            scene baitset02

            b2 "Ugh, I feel guilty for seeing Avalon naked like that and then
            ejaculating. I don't know what came over me."
            b2 "Is she alright? I didn't freak her out, did I?"

            scene baitset06

            l2 "She's fine, [player_name]! Don't feel guilty, there's a lot of reasons
            you might have finished when she caught us."
            l2 "Whatever the reason, I don't want you to worry about it. Avalon
            is a tough cookie."
            l2 "She's also at that age when she's ready to start looking for a partner
            and experiment sexually."
            l2 "Maybe we need to find her a date!"

            scene baitset02

            b2 "I don't like the idea of her hooking up with a boy! Can't
            we just... buy her a toy or something?"

            scene baitset03 with dissolve

            b2 "Or maybe we can convince her to be a lesbian. She did seem
            awfully close with her best friend Dallas."

            scene baitset08

            l2 "Or maybe we can let her decide her own path, [player_name]."
            l2 "We should be here to support her but planning her life for her
            doesn't feel right."

            scene baitset06 with dissolve

            l2 "She's an adult now, Bear. And for what I can deduce about her
            mother, she's turned out well!"
            l2 "I'm sure she'll make the right decisions when it comes to dating
            and sex."
            l2 "I think I heard the shower stop. I'm going to go trade places with
            Avalon."
            l2 "I love you, [player_name]!"

            scene baitset04

            b2 "You're right on all accounts. We'll let her decide her path."
            b2 "I love you too, Leah. Enjoy your shower but don't take too long.
            We need to get Avalon home."

            stop music fadeout 2.0

            jump thering

        ## After Towel Delivery ##
        label thering:

            scene thering23 with fade

            play music "audio/one_step_closer.mp3"

            "Avalon picked out an old outfit from the closet. She didn't usually wear
            darker clothing but there weren't many options to choose from."
            "Despite its lack of color, she still liked the style of it. She wondered
            if this could have been her style in another life?"

            play sound "audio/doorknock.mp3"

            "*Knock* *Knock*"

            scene thering22 with dissolve

            b2 "Avalon? Are you all dressed? I was hoping I could talk to you
            for a moment before we take you home."

            a4 "I'm decent, you can come in."

            scene thering21 with dissolve

            b2 "I haven't seen you in here for a long time. It's nostalgic having
            you back here."

            a4 "I sure miss it! I always loved this room. Thank you for keeping it
            for me."

            b2 "I see you found one of your old outfits. Is that the shirt I bought
            you? I must have gotten that for you five years ago."

            scene thering19

            a4 "Yeah, it still fits! I usually prefer a little more color in my outfits
            but this actually looks cute!"

            b2 "Your favorite color was always blue, wasn't it?"

            a4 "Is that strange? Blue is usually a boy's color, right? But whatever,
            I like it! Blue looks good on me."

            scene thering21

            b2 "Blue brings out the color in your eyes. It's the perfect color for you."
            b2 "I'm sure you could wear a brown burlap bag and still look incredible
            though, Avalon."

            a4 "You think I'm sexy, Uncle?"

            scene thering20 with dissolve

            b2 "In that outfit, I would use the word 'bewitching'. I hadn't seen
            you as sexy before, Avalon."
            b2 "Now that you're all grown up, you are quite a captivating young
            woman."
            b2 "Is that important to you now that you're an adult?"

            scene thering18

            a4 "I always liked to look cute but lately I've been thinking a lot
            about my future."
            a4 "Eventually I want to find a partner that I can, you know, try
            things with."
            a4 "I just want to be sure I look my best for them, whoever
            that someone might be."

            scene thering17 with dissolve

            a4 "Anyway, you wanted to talk to me? We can sit on the bed if you want?
            What did you want to talk about?"

            b2 "Right, I have two things for you that I've been meaning to give
            you for some time."

            a4 "Come on in, we can talk on my bed. Just like old times!"

            scene thering10 with dissolve

            b2 "When I told you and your mom that I designed a fitness app, I wasn't
            telling you the truth."
            b2 "I didn't want to tell you where I got the money for various reasons
            but I don't want to keep it from you anymore."

            scene thering12 with dissolve

            b2 "I found my father, Avalon. It was a rather awful experience meeting
            him. Needless to say, he wasn't too happy to see me."
            b2 "He gave me money to leave him alone. To him, it wasn't much but for me
            it was enough to live off of for decades."

            scene thering15

            a4 "That seems like an odd thing to keep from me, Uncle. I would
            have been happy to be there for you through that experience."
            a4 "I'm sorry your real dad turned out to be awful. That must have been
            difficult."
            a4 "You, um, never told me how much money you came into. Was it really
            that much?"

            scene thering13

            b2 "It was a significant amount. As soon as I had it, I immediately set
            aside a portion of it in a separate account."
            b2 "The money in that account is designated for the most important thing
            in my life. There's nothing better I could do with it."
            b2 "It's... it's yours, Avalon. For college, or traveling the world or
            just getting your life started. You can do whatever you want with it."

            scene thering15

            a4 "You don't need to do that, Uncle. I'm going to be just fine."
            a4 "How much did you set aside?"

            b2 "Well, it's a substantial amount. It's half a million dollars, Avalon."

            scene thering14 with dissolve

            a4 "What!? Half a million dollars!? I don't want that! What would I even
            do with it?!"
            a4 "No no, Uncle. That's too much! College doesn't even cost that much!"

            scene thering12

            b2 "It's a foundation for you to start your life on, Avalon. There is
            nothing better I could do with this extra money."
            b2 "This is what I want more than anything. For you, and for Johnny,
            I want to give you this."
            b2 "Leah and I are doing well. Her career is stable and she makes
            good money. And I don't need much."
            b2 "Take this. Spend it responsibly and build the life you want.
            Nothing would make me happier."

            scene thering15

            a4 "If that's truly what you want, I'll take it. But only if you and
            Leah help me use it the right way."
            a4 "I would have no idea what to do with it! I didn't make any
            plans for after High School. I'm not sure what to do with myself."

            scene thering13

            b2 "I'll help you find the right way to use it. And Leah is a lot
            smarter than me."
            b2 "She'll know the most optimum way to spend it so you get the most
            benefit from it."
            b2 "Heck, maybe we can even invest a portion of it."

            scene thering09 with dissolve

            b2 "I have one more thing for you here in my pocket, Avalon."

            a4 "I think you've given me enough, Uncle. I can't imagine what else
            you would want me to have."
            a4 "Are you going to give me one of your kidneys now?"

            b2 "When your father's guitar broke, I took some of the metal bits
            from it and had a ring fashioned out of them."

            scene thering08 with dissolve

            b2 "I was going to give it to him as a gift but he... he perished before
            I had a chance. I want you to have it now, Avalon."
            b2 "It's made from parts of something that your father loved. It should
            be united with the person he loved the absolute most;"
            b2 "You."

            scene thering07 with dissolve

            a4 "From his guitar? Mom told me about how he used to play. This is...
            this is wonderful, Uncle."
            a4 "Are you sure you want to give this to me? I know Dad was important
            to you too."

            b2 "I loved your father, Avalon. He was the best man I'd ever known.
            And I see so much of him in you."
            b2 "This was a gift to him. It's only right it goes to his child."
            b2 "Although, I had it fashioned for his finger and you're much smaller
            than he was. We might need to have it resized."

            scene thering06 with dissolve

            a4 "It might fit on my thumb! It's worth a try, right?"

            b2 "Your thumb? Hm, yeah. You do have a rather fat thumb. It might
            just work."

            scene thering05 with dissolve

            b2 "Well would you look at that. It's a great fit! What are the odds?"

            a4 "It's a little loose but I think it'll work just fine."
            a4 "I love it, Uncle. I'll never take it off."

            scene thering04 with dissolve

            b2 "I love you, Avalon. I'm sorry I fell off the map for a little while.
            I'll explain that better to you one day."
            b2 "But for now, let that ring represent my commitment to being there
            for you from now on. I won't leave again, I promise."

            a4 "Thank you, Uncle. I hope you weren't terribly unwell the last few
            years."
            a4 "Whatever happened, I'm glad you found Leah. You two seem like a smart
            match. I like her a lot!"
            a4 "And I love you too, Uncle [player_name]. I'm going to stay in touch
            better too!"

            scene thering03 with dissolve

            a4 "Bring it in! I want a big ol' Uncle bear hug!"

            b2 "Sure."

            scene thering02 with dissolve

            a4 "Thank you for everything, Uncle. I hate that I didn't get to grow up
            with my dad but at least I had you."
            a4 "I'm so glad you're back in my life. I don't want us to lose touch again."

            b2 "We won't, I promise."

            "Avalon wrapped around [player_name] and squeezed tightly with both
            her arms and her legs."
            "She had missed the feeling of having her Uncle around. She always
            felt safe in his arms."

            scene thering01 with dissolve

            l2 "Aw. You guys are so freakin' adorable, I could die!"
            l2 "I hate to be a party pooper but we should probably get you home,
            Avalon. I know you were worried about your mom."
            l2 "Are you two all ready to go?"

            stop music fadeout 2.0

            a4 "Yeah, I'm ready! I'm just giving a hug to my bestest Uncle ever!"

            b2 "I'm your only Uncle!"

            scene black with dissolve

            "[player_name] and Leah drove Avalon home, kissed their goodbyes and
            went their separate ways."
            "Avalon headed through the house to find her mother in the living area."

            scene shiner12 with dissolve

            "The television wasn't turned on, the lights were off and Sharol
            sat silently in the dark with an open bottle of liquor next to her."

            scene shiner11 with dissolve

            a4 "Good morning, Mom. Did you have a nice night with your friend?"
            a4 "He was a dentist, right? Did he clean your teeth with his tongue?
            Or, you know, something dentisty but still lewd?"

            s2 "Yeah, it was fuckin' peaches and cream, Avalon. Now leave me alone."

            a4 "Come on, Mom. Spill the beans! Did you at least have fun?"

            s2 "Just fuck off, Avalon!"

            scene shiner10 with dissolve

            a4 "Hey, there's no reason to be mean to me! I came home to check on
            you and spend time with you."
            a4 "Why are you being such a grumpy pants? You're usually in a good
            mood after a booty call."
            a4 "What's your problem?"

            s2 "Don't you have cheerleading practice or something? Go spend time
            with your girlfriend, Dallas."
            s2 "I don't care what you do, just as long as it ain't here!"

            scene shiner09 with dissolve

            a4 "I graduated, there is no more cheerleading practice. You know that!"
            a4 "Why are you being so dismissive?"

            scene shiner08

            play music "audio/a_way_out.mp3"

            s2 "You couldn't just leave well enough alone, could you?"
            s2 "Is this what you wanted? You want to see your mom like this? Huh?"
            s2 "When I tell you to leave me alone, I mean leave me the fuck alone, Avalon!"

            scene shiner07

            a4 "Oh my God, Mom. Did he do this to you? He hit you? W-why would you
            want to keep that from me?"
            a4 "He assaulted you. That's a serious crime, isn't it? We need to call
            the police, Mom."
            a4 "Why did he do that? What happened?"

            scene shiner06

            s2 "How the fuck should I know? Do I look like a mind reader?"
            s2 "I was drunk and passed out. Next thing I know, he starts shouting nonsense
            about 'Where is she?! Where is she?!' and then clocks me in the head. End of story."
            s2 "Now can you please leave me to lick my wounds in peace?!"

            scene shiner05

            a4 "The only other person that was in the house was me. I left after you
            two headed to your bedroom."
            a4 "He was... he was looking for me? Why would he be looking for me?"
            a4 "What would he have done to me if he'd found me?"

            scene shiner04 with dissolve

            s2 "Well I guess you don't have to worry about that, do you? Because
            you just do whatever the fuck you want, don't you?"
            s2 "You leave the house without my permission. You spend time with that
            loser brother of mine."
            s2 "You're wearing clothes I've never seen before. I have no idea what
            whore things you're doing to get free shit like this."
            s2 "And then you just mosy back into this house like you own the place!"

            a4 "I... I was afraid, Mom. I was afraid of the man you brought home.
            I just didn't want to be here while he was here. T-that's all."
            a4 "I'm an adult now, I can leave if I want to..."

            s2 "You want to be an adult? Get your own fuckin' place, Avalon! Then
            you can do whatever you want. How does that sound?"

            scene shiner02 with dissolve

            a4 "I can't believe you would treat me like this. I rushed home to check
            on you, and to spend time with you."
            a4 "Some man abuses you and you take out your frustration on me?
            What happened to you, Mom?"
            a4 "You're worse every day now. You need help, Mom. We need help..."

            scene shiner03

            s2 "You know where the door is, Avalon. Don't you come back
            into this house unless you're ready to live by my rules."
            s2 "Now get out."

            a4 "I don't even know what to say, Mom. I can't--"

            scene shiner01 with dissolve

            "Avalon's words were cut short as she began to sob uncontrollably.
            She hurried out of the room attempting to hide her cries from her mother."

            "Sharol's rage had turned into guilt and regret. Her words were fueled
            by an anger she could never seem to control."
            "She didn't want to push Avalon away but once the fire inside her is
            lit, she couldn't stop it from taking over."
            "Her burning rage was scorching her entire life and turning it to ash."

            stop music fadeout 1.0

            jump callforhelp

        label callforhelp:

            scene callforhelp02 with fade

            "Feeling unwelcome in her own home, Avalon sat outside weeping softly
            as she waited for help."
            "It wasn't any single thing that happened that had her upset, it was
            all the things together that had her defeated."
            "Her mother had been assaulted, she rejected Avalon's aid and then
            kicked her out of her home."
            "But worst of all, that man was looking for her in the night. What if
            he'd found her? What would he do to her..?"
            "She couldn't shake the thought. It terrified her."

            scene callforhelp01 with dissolve

            "She sought protection, she needed now more than ever to feel safe and
            secure."
            "So she called the person she trusted the most to keep her safe."

            scene callforhelp03 with dissolve

            play music "audio/soft_reminder.mp3"

            l2 "Avalon? We got your text message and came back as fast as we
            could. What happened?"

            a4 "H-how could she? How could she do this to me?"

            scene callforhelp04 with dissolve

            l2 "Why are you sitting outside? Did something happen between you and
            your mom?"

            a4 "She kicked me out, Leah. She said I'm not welcome here anymore. I
            didn't even do anything!"

            l2 "Did it have something to do with that man she brought over last night?"

            scene callforhelp05 with dissolve

            a4 "He hit her, Leah! He punched her in the face. She has a black eye
            and... and..."
            a4 "He was looking for me. In the middle of the night, he was looking
            for me."

            l2 "Thank goodness you stayed with us. We should probably inform
            the authorities, this sounds serious."

            a4 "I tried! I tried to help, Leah! She won't let me!"

            scene callforhelp06

            b2 "Your mother can be stubborn, Avalon. She's probably embarrassed, too."
            b2 "I know I was when I had a black eye. I didn't want anyone to see me."
            b2 "Let's give her some time to cool off and we'll--"

            a4 "No! She can rot here for all I care! I'm tired of being treated like
            this."

            b2 "Well, you're an adult now and you have some money. Let's get you
            your own place. How about that?"

            a4 "I don't want to live alone, Uncle."

            scene callforhelp07

            l2 "How about baby steps, [player_name]? For now, why don't we focus
            on the situation at hand."
            l2 "We have that meeting at my office in a few hours. I'm sure it would
            be fine if she joined us."
            l2 "We'll take care of her until we get everything figured out."

            scene callforhelp08

            b2 "That sounds like a good plan, Leah. She can stay in the room we
            have for her at our place for now."
            b2 "We'll have to figure out what to do about Sharol though. If Avalon
            isn't here, I doubt she'll be able to take care of herself."

            scene callforhelp10

            l2 "We'll figure it out. Every problem has a solution!"
            l2 "But for now, we have a few hours before our meeting. How about
            we go shopping?"
            l2 "New clothes always cheer me up! How about it, Avalon?"

            a4 "Really? I haven't been shopping in a while. That does sound nice."

            l2 "It's settled then!"

            scene callforhelp08

            b2 "We still should do something about the man that attacked Sharol."
            b2 "I wouldn't feel right if we didn't at least try to alert the authorities
            to stop him from hurting more people."
            b2 "Why don't we stop by the police station and file a report? It's the least
            we could do."

            scene callforhelp09

            a4 "Thank you for coming back for me, Uncle. I hope I didn't inconvenience
            you at all."
            a4 "What's the meeting you keep referring to? I didn't know about that."

            b2 "Well, we don't know what it's about yet. It has something to do with a project
            Leah turned down a little over a week ago."
            b2 "We'll find out more when we have the meeting, I suppose."

            a4 "Okay, well, thank you for coming back for me. I don't know what I
            would have done without your help, Uncle."

            stop music fadeout 1.0

            b2 "You're welcome, Avalon. Leah and I will always be happy to help.
            Come on, let's get our day started."
            b2 "We'll stop by the police department to file a report and then
            head off to the mall so we can do some shopping."

            scene report01 with fade

            play music "audio/violet_shimmer.mp3"

            a4 "Are we even allowed to just walk in here like this? You're sure
            we're not supposed to call or fill out something online?"

            l2 "Law enforcement are here to serve and protect us. We're not walking
            into a lion's den, police are here to help us."

            b2 "They have too much power, if you ask me. They're here to protect us
            as long as we don't disagree or contend with them."

            l2 "You're being silly. Police officers are held accountable for
            their actions just like everyone else."

            scene report02

            "[player_name] and Leah continued to bicker over law enforcement but
            Avalon was feeling a sense of dread walking in."
            "She felt a slight twinge of intimidation standing inside the police
            department. She had never been in trouble with the law before."
            "Standing there, she couldn't help but wonder what it would be like
            if she ever was arrested."
            "She imagined herself handcuffed and dragged through this hallway,
            protesting her innocence and pleading to be released."

            scene report03 with dissolve

            "In the midst of her unpleasant day dream, something off to the side
            caught her eye."
            "The fantasy in her mind faded as her vision focused in on the unusual
            person to her right."

            scene report04

            "A young woman was laying peacefully atop a sign. Avalon was sure this
            would be considered loitering and in the middle of a police department no less."
            "How could someone seem so relaxed blantantly breaking the law right in front
            of law enforcement? She must be incredibly audacious."
            "Avalon felt a pang of jealousy. She wished she could be so bold, so courageous."

            scene report05

            b2 "Avalon? ... Hey, Avalon. You're lagging behind."

            "Avalon was trapped inside her own head, oblivious to the world outside
            of herself and the young lady to her right."

            b2 "Hello? Earth to Avalon? You have your head in the clouds?"

            scene report06 with dissolve

            a4 "Huh? Oh, sorry! I'm right behind you, don't worry."

            b2 "What were you thinking about?"

            a4 "Uhm. Courage, I guess."

            b2 "Did I tell you about that time I fought a raccoon? I thought I was
            being courageous saving my garbage from a rodent. You know what I got?"
            b2 "Bit. I got bit, Avalon. Sometimes courage is synonymous with stupidity.
            Don't be courageous, be safe."

            a4 "Another life lesson brought to you by Uncle Sillypants! I'll file
            it under 'Weird life advice my Uncle gave me.'"

            "The trio continued their journey down the long corridor arriving at
            a counter with a rather enthusiastic officer behind it."

            scene report07

            oe "Welcome to your local police department, folks. How can I be
            of service today?"

            b2 "We'd like to report a crime. Is this where we do that?"

            oe "I can assist you here. Can you describe the incident to me?"

            scene report08

            b2 "My sister was--"

            scene report09 with dissolve

            a4 "Who is that woman back there laying on that billboard? Isn't that loitering?"
            a4 "Is she part of the department or something? She's not in uniform so
            maybe she's off duty?"

            scene report12

            oe "She is most certainly not a part of this department. She's a mischevious
            hoodlum is what she is!"
            oe "She's just bored so she's lollygagging about waiting for somethin'
            interesting to happen."
            oe "I've asked her four times today not to sit on that damn sign. You
            know how frustratin' it is to be ignored like this?"
            oe "I'm an officer of the law for cryin' out loud!"

            scene report10

            a4 "I don't understand. You're in a position of authority here, right?
            Can't you arrest her if she doesn't comply?"

            oe "It's complicated."

            scene report11 with dissolve

            l2 "It does seem rather sketchy. She's disrespecting your entire
            department and you're just letting her do it?"
            l2 "There has to be a story here or something. What's going on?"

            scene report13

            oe "Look. The department has a complicated relationship with her. She ain't
            always playin' by the rules, like she should, but..."
            oe "She's done a lot of good by us too. So yeah, we let some things
            slide once in a while."
            oe "Not to mention she's got someone behind the curtain protectin' her."

            scene report14 with dissolve

            oe "Er, you know what, I probably shouldn't have said all that."
            oe "Let's, uhh, keep all that between us. What did you say you were here
            for again?"

            scene report15

            b2 "Right. My sister was physically assaulted yesterday by a man she
            invited over."
            b2 "We're also confident he had the intention of sexually assaulting
            my niece. Fortunately she wasn't home last night."
            b2 "I'm not sure what steps we take from here but we'd like to make
            sure he doesn't hurt anyone else."

            scene report16

            oe "That sounds like quite the ordeal, I'm sorry you had to go through
            that."
            oe "Do you have any evidence of the assault? A video of the event or
            an audio clip? Anything we can go off of?"

            b2 "We know his first name and that he's a dentist. We weren't actually
            there when it happened."

            oe "I can make note of this but without anything to go off of, there
            isn't much we can do. I would recommend you avoid--"

            scene report18

            a4 "A man hit my mom and had the intention to rape me and you're not
            going to do anything about it?!"
            a4 "What do you even do here if you don't help people and stop criminals?"

            b2 "Isn't the investigation supposed to be your job? Collecting evidence,
            questioning individuals. Why would that be on us??"

            l2 "Seriously, what are our tax dollars paying for? For you to just
            sit on your ass here?"

            scene report17

            oe "I can see that you're all upset. But there has to be some evidence
            of a crime for us to pursue someone."
            oe "You've brought me a name and a location. The victim of the crime
            isn't even here."
            oe "How do you know there isn't more to the story than what she told you?"
            oe "We're not staffed nor funded well enough to chase every reported
            crime, especially ones with no evidence whatsoever."

            scene report18

            a4 "You know what? The next person he hurts isn't on us. They're on
            you!"
            b2 "Come on, Avalon. He isn't going to help us and the only thing
            we're going to do by arguing is get ourselves in trouble."

            scene report19 with dissolve

            a4 "I just can't believe it! I've never asked the police for help
            before. The one time I call on them, they do nothing?!"

            b2 "I bet if the assault happened to someone he knew, they'd do
            something about it."

            a4 "I'm furious, Uncle! I can't believe they won't stop a terrible
            man from hurting people. Can we... can we file a complaint or something?"

            b2 "Nope. This is how things are. The world isn't fair."

            scene report20

            stop music fadeout 2.0

            a4 "H-hey, that person is gone."

            b2 "Oh right, the person literally commiting a crime on police grounds
            and they did nothing about it."

            a4 "Jeez, I know, right?"

            scene report21 with dissolve

            play music "audio/sneaking_up_on_you.mp3"

            a4 "Oh. Well there she is. What's... what's she doing?"

            b2 "Looks like she's dancing around on the department's property, making
            a mockery of them."

            l2 "Maybe she's just goofing off?"

            scene report23

            pn "What was the verdict? Is the grand might of your local police department going to assist you with your situation?"

            b2 "Listen, we know all about you. We don't want any trouble. We're
            just heading to my vehicle and leaving peacefully."

            pn "If I were a betting woman, I'd wager trouble has already found you.
            Why else would you be here?"

            b2 "Well, we don't need {i}more{/i} trouble."

            pn "Sometimes you have to fight fire with fire. Maybe trouble is
            exactly what you need? Trouble pointed in the direction of a particular problem, perhaps?"

            scene report22

            a4 "Um, they said they couldn't help us. We don't have enough evidence
            and they won't investigate on our word alone."
            b2 "It's not any concern of yours though. It's a private matter."

            scene report24

            pause(.2)

            scene report25 with dissolve

            pause (.2)

            scene report26 with dissolve

            pause (.5)

            scene report27 with dissolve

            pn "Perhaps I can help. I'm a private investigator so private matters
            are my specialty! You can call me Penny."
            pn "Why don't you tell me what happened and I'll let you know if I can assist?"

            scene report28

            b2 "You know, from the ground you look a lot younger.
            Do you need us to call your parents to come get you?"
            b2 "Maybe we can get you some ice cream or something while
            we wait for them."

            scene report29

            pn "Don't make promises about ice cream that you can't keep, Sir! That stuff is delicious!"
            pn "I'm sure you've heard the old saying, haven't you? Big things,
            small packages? I'm plenty capable, I assure you."
            pn "There hasn't been much going on lately so I'm eager for work.
            Even if it's something small, I'll probably take the case."

            scene report30

            a4 "The officer inside did say you're a pretty incredible person.
            And you're our only hope now that they've rejected our plea."
            a4 "I guess we can tell you what happened but you have to promise you won't put yourself in danger.
            I don't want you to get hurt trying to help us."

            pn "I won't come to harm, you can have confidence in that."

            scene report31 with dissolve

            a4 "My mom invited a man over last night. I stayed at my Uncle's house because the guy creeped me out."
            a4 "He... he hit my mom. She has a black eye from it. And she said..."
            a4 "Well, she said he was looking for me in the middle of the night. When he couldn't find me, he became agitated and that's when he struck her."
            a4 "I think he meant to--"

            pn "That's plenty, I understand. Can you tell me anything about him? Name? Defining features?"

            a4 "He said his name is Seth. He's a dentist. He's tall, muscular, black. I... I don't really know anything else about him."

            scene report32

            pn "I am sorry to hear about your mother. I am happy, however, to hear you were unharmed."
            pn "This does sound like something worth looking into. We can't have a
            man like that continuing to hurt people, can we?"
            pn "I'll look into this for you. I'll contact you with my findings
            when my investigation is concluded."

            scene report33

            b2 "Before we speak any further on this, let's discuss pricing."
            b2 "You're a private investigator, right? So that means you must charge for this?"

            scene report34

            pn "A valid concern! Perhaps pricing should be left up to the customer
            in this case."
            pn "What price tag would you put on stopping a rapist, Sir?"

            scene report35 with dissolve

            pn "Penny for your thoughts?"

            scene report36 with dissolve

            play sound "audio/coinflip.mp3"

            pause

            scene report37

            b2 "What the hell? You're throwing crap at me now!?"

            a4 "Woah! Nice catch, Uncle. What is it?"

            scene report38 with dissolve

            b2 "It's... it's a penny."
            b2 "I thought I was supposed to be the one paying you? You're the
            one offering a service here, aren't you?"

            l2 "A penny? Because your name is Penny? Is that supposed to be some
            kind of play on words?"

            a4 "Huh. Seems pretty clever to me."

            b2 "Well, if I get to choose the price, then--"

            scene report39

            b2 "Wha..? Where'd she go? How am I supposed to give her money if she
            just disappears like that!?"
            b2 "Not that I would have. This whole thing feels like a scam to me."

            a4 "How can it be a scam if you didn't give her anything?"

            b2 "Fair point..."

            l2 "I wonder if she's actually going to look into this for us then..?"

            scene report40 with dissolve

            b2 "Well, not much we can do at this point. I just hope she doesn't
            get herself hurt."

            stop music fadeout 2.0

            a4 "She seemed confident enough. I still can't believe how small she
            was though. She looked like a kid but she sure didn't act like one."

            l2 "Maybe she knows how to use that to her advantage?"
            l2 "At any rate, it's time to enjoy ourselves a little. Are you
            ready to go shopping, Avalon?"

            a4 "Yeah! Let's go!"

            if wholesome > lewd:

                jump dressup

            else:

                jump lewdlingerie


        label dressup:

            scene dressup01 with fade

            play music "audio/one_step_closer.mp3"

            l2 "Hey, look at this. They have some nice stuff here, don't they?"

            a4 "It's all a little nicer than the stuff I usually buy. I saw the price
            tag on one of the outfits. Are you sure these aren't too expensive?"

            l2 "Financial responsibility is important but today we're treating ourselves."

            scene dressup02 with dissolve

            l2 "I have a great idea! You're eighteen now, right? That means you're
            going to start working and dating soon!"

            a4 "That's true. I don't know about the dating part but... working, yeah!"

            l2 "How about I pick out three outfits for you and you can try them on?"
            l2 "I'll get you one casual outfit, one business outfit and then something
            you can go on dates in!"

            a4 "Okay, that sounds fun! I'll go wait by the changing rooms."

            l2 "I'll send [player_name] to keep you company. I shouldn't be long!"

            scene dressup03 with dissolve

            l2 "Hey, [player_name]! What are you doing over there?"
            l2 "Don't buy anything from here. These clothes aren't your style."

            scene dressup04 with dissolve

            b2 "What do you mean it's not my style? It could be! I'm a big boy, I
            can wear whatever I want. I'll wear a dress if I want!"

            l2 "You better not wear a dress, [player_name]!"

            b2 "Make me!"

            l2 "No, I-- wait, what? Stop being silly and go hang out with Avalon
            while I pick out some outfits for her."

            b2 "Oh, is she by the changing rooms then? Alright, I'll keep her
            company. Pick out something amazing!"

            scene dressup05 with fadefast

            b2 "Leah said she's going to pick out some outfits for you? What has
            she got planned?"

            a4 "Yeah, she's going to pick out some situational attire, each one
            for a different occassion. It should be fun!"

            b2 "That does sound interesting. I'll be eager to see what she
            comes up with. How are you holding up after the police station?"

            scene dressup11 with dissolve

            a4 "Well, I've been thinking about it a little bit. We shouldn't have
            been so harsh to that officer. He was only doing his job."
            a4 "I don't like that they couldn't help us but I bet a lot of people
            come in there with complaints like that."
            a4 "I'm sure he's right, I'm sure they simply don't have the man
            power to chase every reported crime. And that's really not his fault."

            scene dressup08

            b2 "I know it's not his fault. I just... I get frustrated with the
            system in general."

            scene dressup07 with dissolve

            b2 "But that Penny character said she would see what she could do.
            I guess we'll put some faith in that for now."
            b2 "I don't want you to focus too much on that, Avalon. We're going to
            figure out how to help your mother."
            b2 "In the meantime, I want you to focus on getting your own
            life started. The money I gave you is a blank ticket."
            b2 "You can do anything you want. Or you can do nothing for a little
            while and just travel for a year."
            b2 "No matter what you choose, Leah and I will support you."

            scene dressup09

            a4 "Maybe I will take some time to plan things out for myself. I'd like
            it if you were around to help me figure things out for my future though."
            a4 "I didn't know I would have a jump start like this. Heck, even if
            I did, I still wouldn't know what to do with myself."

            scene dressup07

            b2 "I never found a career path. Now that I'm with Leah, it's something
            I'm going to start searching for too."
            b2 "Maybe we can search together for what we're passionate about?"

            a4 "I like that idea."

            scene dressup06 with dissolve

            b2 "Is there anything you think you might want to look into? Or
            is there anywhere you want to go for inspiration?"
            b2 "Maybe we can convince Leah to take some time off and we
            can visit another country? Maybe Ireland!"

            scene dressup10

            a4 "You recently found out you're part Irish, didn't you? It's rather
            obvious, really."
            a4 "Actually, Leah might be too. She's got to be the reddest redhead
            I've ever seen."

            scene dressup09 with dissolve

            a4 "But in all seriousness, that actually sounds like it could be a
            lot of fun. We should try to do that!"

            scene dressup11 with dissolve

            a4 "But... well, we do have to figure out something for Mom. She
            can't live by herself. Especially not the way she is now."

            scene dressup07

            b2 "Let's try to enjoy the rest of our day. We'll all put some
            thought into that and we'll come up with something."
            b2 "My priority, and so should yours be, is you. The most important
            thing is that we get your life started."
            b2 "Sharol chose her path and only she can choose to change it."

            scene dressup11

            a4 "I know that. And you're right. Still, she's my mom and I feel some
            responsibility to help her find a better path."

            scene dressup09 with dissolve

            a4 "I love you, Uncle. Thank you for being here for me. You're right,
            we need to focus on enjoying today."
            a4 "If we put our heads together, we'll find a solution for Mom. I'm
            sure of it!"

            l2 "I've found some outfits for you, Avalon."

            scene dressup12 with dissolve

            a4 "Oh, okay! I'll head into the changing room and you can pass them
            in to me."

            scene dressup13 with dissolve

            b2 "It seems you and Avalon are getting along rather well."

            l2 "There's something about her. It's hard not to adore her."
            l2 "She's like a puppy dog, you just want to cuddle
            with her and take care of her."
            l2 "And there's this positive charge that she carries around. It's
            utterly contagious and rather addicting."

            b2 "Yeah, her father was the same way. He was the kind of person
            you loved being around and when he wasn't near, you wished he was."

            l2 "I wish I could have met him."

            b2 "Me too..."

            scene dressup14 with dissolve

            a4 "I'm all ready! This isn't quite what I expected but I have to say,
            I kind of like it!"

            l2 "You like it? Great! Come show us, Avalon. Stand over here."

            scene dressup15 with dissolve

            a4 "It's a little more grown-up than what I usually wear, which is perfect!"

            menu:
                "The past meets the present; retro but cute.":
                    $ wholesome += 1
                    show screen notify("健康 +1", 2.0)
                    b2 "It has sort of a retro seventies look. I can dig it."

                "I'm getting a lame new aged hipster vibe.":
                    b2 "A tie dye headband and some special brownies is all
                    you need to complete this outfit."

                    l2 "Oh you're just jealous that I have taste, [player_name]!"

            l2 "It does look like a modernized outfit from the past."
            l2 "Okay, we'll buy it!"

            a4 "Really? You think I can pull it off? It seems a bit mature for me."

            l2 "That's the whole point. It's a smart buy, Avalon. Let's see
            the next one."

            scene dressup17 with dissolve

            a4 "Okay, I'll be out in just a moment!"

            "Avalon hurried back into the changing room and returned momentarily."

            scene dressup19 with dissolve

            a4 "I call this one 'All Business Avalon'! Can't you just imagine me
            as a big corporate boss when I'm wearing this?"

            l2 "It would be perfect for an interview. A must have for any
            young woman's wardrobe!"

            menu:


                "Those sexy boots don't exactly scream 'Business Woman'.":
                    b2 "Those boots were made for walking, if you know what I mean."
                    b2 "They make it look like you've got some crazy dominatrix
                    outfit on underneath your business outfit."

                    scene dressup18 with dissolve

                    a4 "Don't make this weird, Uncle! They're just regular boots!"
                    a4 "Okay, they're a little tall and... there's probably more
                    leather than is necessary."
                    a4 "Sexy boots can't hurt my chances in an interview though!"

                    scene dressup19 with dissolve

                    l2 "Don't use sex to get a job, Avalon. You're a smart girl, use your
                    head."

                    a4 "R-right, sorry. I was just kidding."

                    l2 "But [player_name] is right, they're kind of kinky. They'll be
                    perfect to wear when you're enticing a lover!"

                    a4 "Uhh... I'll keep that in mind. Anyway! Let me try on the last outfit."

                "You look professional yet stern.":
                    $ wholesome += 1
                    show screen notify("健康 +1", 2.0)
                    b2 "You look like a no nonsense business professional, Avalon."
                    b2 "Though I will say those boots might be inappropriate in
                    an office setting. They're rather risque, aren't they?"

                    scene dressup18 with dissolve

                    a4 "Sounds like your head is in the gutter, Mister!"

                    l2 "Yeah, they don't look slutty! They look..."
                    l2 "Alright, yeah, they might have a smidge too much leather.
                    We'll skip the boots but it's otherwise a solid choice!"

                    scene dressup19 with dissolve

                    a4 "Let me try on the last outfit. I'll just be another moment."


            scene dressup17 with dissolve

            "Avalon threw on the last outfit but hesitated before exiting the
            changing room."

            if wholesome >= 4:

                show screen notify("健康之路检查：通过！", 3.0)

                a4 "Um. I don't know about this one. It might be a little too sweet for me."

                l2 "Don't be shy, Avalon. Come show us so we can all judge together."

                a4 "Okay, I'm coming out."

                scene dressup20 with dissolve

                a4 "It's a little too fairy tale, isn't it? I feel like Cinderella or
                something."

                l2 "I would have to argue that the look fits you well, Avalon. You look
                like a princess so you should dress like one."

                a4 "You really think so?"

                scene dressup21 with dissolve

                menu:

                    "You look cute as a button.":
                        $ wholesome += 1
                        show screen notify("健康 +1", 2.0)
                        b2 "You look absolutely darling, Avalon. It's the perfect outfit
                        for a midday picnic or a day date."

                        a4 "They make my boobs look small though."

                        b2 "Good! People shouldn't be looking at your boobs. They should be
                        looking at your eyes. They're your best feature."

                        a4 "You think so?"

                    "You look like dinner for a big bad wolf.":

                        b2 "It makes you look too innocent. I thought the point was
                        to make you look more mature?"
                        b2 "This is an outfit I could see a much younger woman wear."

                        scene dressup22 with dissolve

                        a4 "You think it's that bad? It makes me look like a little girl?"

                        l2 "[player_name] just doesn't like that it shows off your boobs.
                        He's worried about predators."

                        scene dressup20 with dissolve

                        a4 "Do you think it's too revealing? I don't want creepy guys
                        approaching me all the time."

                        l2 "No, it's a darling outfit. [player_name] is over-protective."

                scene dressup22 with dissolve

                a4 "I feel like it makes me look a bit like a present day Dorthy.
                You know, from The Wizard of Oz."

                l2 "Is that a bad thing?"

                scene dressup23 with dissolve

                a4 "No, it's not a bad thing. It's growing on me."
                a4 "[player_name] can be my lion and you can be my tin man! You know, because
                [player_name] looks big and tough but really he's a big ol' softy."
                a4 "And you're looking for a new heart. It's perfect!"

                l2 "Who is the Scarecrow then?"

                scene dressup20 with dissolve

                a4 "Maybe we haven't met the Scarecrow yet. We have time."

                b2 "Well, I liked the analogy. Except the part where it makes me seem
                like a coward."

                scene dressup21 with dissolve

                a4 "Aren't you the one that told me to abandon the idea of courage and
                to instead stay safe?"

                b2 "You've got me there."

                scene dressup20 with dissolve

                l2 "We have that meeting at my office soon. Go ahead and change
                back into your clothes and we'll check out."

                a4 "Oh, how are we going to pay for these?"

                l2 "We'll take care of it! It's our treat, Avalon."

                a4 "Okay, wow, thank you. I'll be out in a minute."

                jump finishdressup

            else:
                $ renpy.notify("健康之路检查：失败！")

                a4 "No, no. This one is too fairytale. I can't wear this."

                l2 "It's alright, Avalon. I'm sure it's not that bad. Just show us."

                a4 "I don't want to, I don't like it. I want to skip this one."

                b2 "You don't have to show us anything you don't want to. Change
                back into your clothes and we'll go, alright Avalon?"

                a4 "Okay, thank you for understanding, Uncle. I'll be out in a second."

                jump finishdressup

            label finishdressup:

            scene dressup13 with dissolve

            b2 "You really don't know what this meeting is about? Or why I'm involved
            in it?"

            l2 "I can only venture a guess that it has something to do with the
            research project I passed up on last week."

            b2 "I'm still not sure how that involves me though, Leah. Are you
            sure you didn't misunderstand what they asked you in for?"

            l2 "I was asked to bring you along specifically. I didn't misunderstand,
            I assure you."
            l2 "We'll find out soon enough what it's about."

            scene dressup24 with dissolve

            l2 "There's our superstar! So how do you think I did, Avalon? Did
            you like all the outfits I picked out?"

            a4 "Yeah! I loved all of them! You've got a good eye, Leah. Thank
            you!"

            l2 "You're welcome. Do you feel better? I know we didn't solve any
            problems yet but did we get your mind off things for a while?"

            scene dressup25 with dissolve

            a4 "Yes, and I appreciate it more than you know!"

            l2 "Oh! You're mighty affectionate, aren't you? It was my pleasure,
            I assure you. You're a delight to spend time with, Avalon."

            a4 "I wish my mom was more like you, Leah. Wouldn't that be something?"

            l2 "Y-yeah, that's an interesting thought."

            scene dressup26 with dissolve

            b2 "We don't have to be your parents to want to spend time with you
            and to love you, Avalon."
            b2 "But if you're really insistent, I guess you can call me 'Daddy'.
            Leah already does sometimes."

            l2 "You just had to go and ruin the moment, didn't you? Why am I
            not surprised?"

            scene dressup27 with dissolve

            a4 "He always makes jokes when things get too serious. It's one of my
            favorite parts about him, actually."

            l2 "Yeah, he's not so bad. I guess we can keep him around."

            stop music fadeout 2.0

            "The trio spent a few more moments in a loving embrace before gathering
            themselves and heading out."
            "Their next stop was the corporate office of Pridwyn."

            jump meethenry

        label lewdlingerie:

            if _in_replay:
                $ lewd = 6
                $ player_name = renpy.input("What would you like to name the MC?")
                if player_name.strip() == "":
                  $ player_name = "Byron"


            scene lewdlingerie001 with fade

            "Avalon glared down at the provocative clothing lying on the table in front of her."
            "She had never worn anything like this before. Her most risqué outfit would
            simply be her bra and panties."
            "She stood both shocked and... curious."

            a4 "This isn't exactly what I imagined when you said we would go
            shopping, Leah."
            a4 "People actually wear this stuff? Isn't it awfully... lewd?"

            scene lewdlingerie002 with dissolve

            play music "audio/island_hopping.mp3"

            l2 "Everyone wants to be desirable, Avalon."
            l2 "There is nothing more arousing than seeing that glimmer in your
            partner's eye when you can tell he wants nothing more than to fuck you silly."
            l2 "And nothing makes you look better than a skimpy silk slip or a
            leather corset."
            l2 "When you look back at yourself in the mirror wearing nothing but
            a see-through fishnet, you'll start fantasizing about sex."

            scene lewdlingerie003 with dissolve

            l2 "Everytime you put on that outfit, your heart is going to race
            and your body is going to heat up."
            l2 "You're going to imagine your crush seeing you in it and
            what he might want to do to you because of how fucking sexy you look in it."
            l2 "You're mind is going to spin with all the possibilities. Your ankles
            behind your head, or your butt in the air, or your hands bound behind you."

            scene lewdlingerie004 with dissolve

            a4 "Oh! Holy crap..."

            l2 "And then, after your imagination is fired up, you're going to tear
            off those clothes and find yourself knuckle deep inside your own pussy."

            a4 "Wha--? I--"

            l2 "And just as your mind begins to weave the picture of your dream guy
            spilling his seed inside you, your body will erupt in orgasm."
            l2 "You'll forget all about your worries and your troubles when
            you're lying in a puddle of your own climax."
            l2 "That is why we're here, Avalon."

            a4 "W-wow. Um... alright."

            scene lewdlingerie005 with dissolve

            l2 "I'm going to look around for a bit. If you find anything you like,
            try it on! Don't concern yourself with price today."
            l2 "We're treating ourselves!"

            a4 "W-wait, where... but you were...?"

            "Avalon could feel herself becoming frustrated. She found herself
            enjoying the sexually tense moments Leah would start."
            "But just as quickly as she began them, she would abandon them leaving
            Avalon charged up with no relief."

            scene lewdlingerie006 with dissolve

            stop music fadeout 2.0

            "She began looking differently at the lingerie before her. Could these
            outfits really have that much of an effect?"
            "Leah made them sound magical in nature. Avalon felt intrigued, she wanted
            to know if Leah was right."
            "She decided she wanted to choose an outfit but she had no idea where to start.
            What should she pick..?"

            scene lewdlingerie007 with dissolve

            play music "audio/a_quiet_thought.mp3"

            "She thought perhaps something simple at first? A cute bra could be a nice jumping
            off point."
            "Avalon caught the attention of [player_name]. He wasn't sure what
            Leah was thinking bringing Avalon here."
            "He decided to check on her."

            scene lewdlingerie008

            b2 "Hey, Avalon. Have you found anything interesting?"
            b2 "I know this is probably not where you figured we'd be shopping.
            I'm just as surprised."

            scene lewdlingerie009 with dissolve

            a4 "I thought it was odd at first but the idea is growing on me."
            a4 "I haven't worn lingerie before so I have no idea what to try."

            b2 "I'm not sure what to try on either. They only seem to have banana
            hammocks and leather harnesses for men."

            a4 "There's plenty of lace panties you could try!"

            b2 "Hey, you joke but I bet I could rock that shit."
            b2 "Nothing at all has caught your eye so far?"

            scene lewdlingerie010 with dissolve

            a4 "Maybe I need a man's opinion. What do you think I would look sexy in,
            Uncle?"

            b2 "I'm not terribly imaginative myself. I'd have to see things on you
            to tell you if you look good in them or not."

            scene lewdlingerie011 with dissolve

            a4 "O-oh, you want me to model for you?"

            b2 "Not if you don't want to. I'm sure Leah has a better eye than--"

            a4 "I can do it. I... I can model some lingerie for you, Uncle."

            "Avalon had only one man in her life she was comfortable around. When
            she thought about who she wanted to find her desirable, she thought of [player_name]."
            "She knew that it was perhaps unusual for her to want her Uncle but
            she also knew he would always want the best for her."
            "He would protect her and be there for her when she needed him. She wanted
            him, she craved him, she loved him."
            "He'd only been back in her life a week but he already rescued her from
            a terrible fate. She saw him differently now than when she was younger."
            "Though she wasn't sure how Leah would feel about her enticing [player_name].
            She was confused about what exactly Leah wanted from her."
            "But the confusion only fueled her arousal. It was like a suspenseful
            mystery slowly revealing what was behind the curtain."
            "She wanted to see it play out."

            scene lewdlingerie010 with dissolve

            stop music fadeout 2.0

            a4 "I'll go see if Leah has found anything that might look good on me."
            a4 "You can, um, wait in the changing room if you want? I'm going
            to look around just a bit more."

            b2 "Alright. I'll meet you there."

            scene lewdlingerie012 with fadefast

            play music "audio/soft_reminder.mp3"

            "[player_name] used to be intimidated by sex and felt guilty when
            he would appreciate the beautiful curves of a woman's body."
            "But Leah had turned his view all the way around. When he ogled her,
            she would show more of herself to him."
            "When he took notice of her round, full buttocks, she'd reward him
            by rubbing it against him."
            "When he stared at her breasts, she would grab his hands and
            place them firmly on her chest."
            "And when he was horny, she would pull his cock out and let him
            do anything he wanted to her."
            "She rewarded him for being sexual and his guilt for desiring
            sex slowly slipped away."

            play sound "audio/cellvibe.mp3"

            "*Bzzt* *Bzzt*"

            scene lewdlingerie013 with dissolve

            b2 "Hm?"

            stop sound

            scene lewdlingerie014 with dissolve

            "The screen lit up with a notification of an incoming video chat
            request from Leah."
            "Confusion swept over him as he pondered why she would need to video
            call him when she was in the changing room ten feet away."

            b2 "Suzi, accept incoming call."

            scene lewdlingerie027

            l2 "Hey there, Teddy Bear. I have a super secret surprise for you."

            b2 "Whoa! What are you doing, Leah?"

            l2 "I'm going to let you enjoy the show."

            scene bg lewdlingerie017
            show rec
            with dissolve

            b2 "Show? What show? You mean... you changing??"

            l2 "Of course, [player_name]! I wouldn't want you to miss this."

            show bg lewdlingerie025 with dissolve

            l2 "There's so much I want you to see. What do you think of this outfit,
            Bear?"

            b2 "You look like a firecracker except I'm the one that's about to
            explode."
            b2 "Why don't you just step out of that room and show me instead
            of this video call?"

            show bg lewdlingerie017 with dissolve

            l2 "Because then you wouldn't get to see me change. You wouldn't
            get to see {b}us{/b} change."

            scene lewdlingerie018 with dissolve

            a4 "Hey, Uncle! Leah just texted me saying she has some outfits
            for me to try on. She asked me to join her in the changing room."

            b2 "Is that a fact?"

            a4 "What are you watching on your phone there?"

            scene lewdlingerie019 with dissolve

            b2 "Nothing! Just a rampaging wild fire that's totally out of control."

            a4 "I can tell when you're lying, Uncle. You're the worst at it."

            b2 "There is more truth in what I said than you know."

            a4 "Fine, keep your secrets then."

            scene lewdlingerie020 with dissolve

            l2 "Avalon? Is that you out there? Come join me in the changing room."

            a4 "Okay, I didn't really find anything I liked though. I hope you
            had better luck."

            l2 "I sure did! Come see!"

            scene lewdlingerie021 with dissolve

            a4 "I hope one of those outfits comes with bunny ears."

            menu:
                "Warn her.":

                    $ lewd += 1
                    show screen notify("淫荡 +1", 2.0)

                    "Of course [player_name] wanted to see her naked but it was more important
                    to him that he didn't break her trust. He had to warn her."

                    b2 "Avalon, wait a minute. I have to tell you something."

                    scene lewdlingerie022 with dissolve

                    a4 "Yes, Uncle?"

                    b2 "If the outfits that Leah picked out are too revealing,
                    you don't have to try them on."

                    scene lewdlingerie023 with dissolve

                    b2 "In fact, you don't have to try on anything if you
                    don't want to."

                    "[player_name] showed Avalon what he was watching on his phone,
                    trying not to alert Leah to his betrayel."
                    "Avalon watched for several seconds, not yet understanding what
                    exactly she was looking at."

                    scene lewdlingerie024 with dissolve

                    "She turned towards the changing room as she began to understand
                    what was going on."
                    "Leah was recording inside of the changing room? But why?"

                    scene lewdlingerie023 with dissolve

                    "Leah was showing off the recording to [player_name]. Avalon
                    wondered if Leah wants to let [player_name] watch them change?"
                    "If that were true, Leah doesn't just want Avalon for herself.
                    She wants her for [player_name], too!"

                    l2 "Avalon, are you coming? You're not going to make me wait
                    forever, are you?"

                    scene lewdlingerie026 with dissolve

                    a4 "Sorry, I'm on my way."

                    "She didn't say anything to [player_name]. She neither scolded
                    him nor acknowledged what was happening."
                    "Avalon simply turned and walked into the changing room."
                    "[player_name] wasn't sure exactly what was going to happen next
                    but at least his conscience was clear."

                    scene bg lewdlingerie028
                    show rec

                    a4 "Oh, you tried something on without me already? W-wow,
                    it's revealing."

                    l2 "That's the point. We're trying to show off our sexy curves
                    and lingerie helps exaggerate our features."
                    l2 "What I'm wearing now is smooth and shiny. Men are like
                    monkeys, they like shiny things."

                    l2 "I have an outfit I want you to try on. Go ahead and undress, I'll
                    grab it for you."

                    a4 "Um, yeah, okay."

                    show bg lewdlingerie029 with dissolve

                    a4 "What's your phone doing over here?"

                    l2 "I just set it down there while we try on some outfits.
                    There's no pockets on lingerie and I had to put it somewhere."

                    scene lewdlingerie030

                    "Avalon knew that Leah wasn't telling her the truth. She didn't
                    know what Leah was up to with this."
                    "Obviously she wanted [player_name] to see them changing; to
                    see them naked. But [player_name] could see Leah naked any time."
                    "Did she just want to to let [player_name] see her naked??
                    But why?"

                    jump recording

                "Don't warn her.":
                    "Too eager to see his niece naked, [player_name] decide to play along
                    with Leah's scheme."
                    "If he gets caught, it's Leah's fault after all, right? Avalon
                    can't blame him for Leah's actions, can she?"

                    scene bg lewdlingerie028
                    show rec

                    a4 "Oh, you tried something on without me already? W-wow,
                    it's revealing."

                    l2 "That's the point. We're trying to show off our sexy curves
                    and lingerie helps exaggerate our features."
                    l2 "What I'm wearing now is smooth and shiny. Men are like
                    monkeys, they like shiny things."

                    l2 "I have an outfit I want you to try on. Go ahead and undress, I'll
                    grab it for you."

                    a4 "Um, yeah, okay."

                    show bg lewdlingerie029 with dissolve


                    a4 "Oh, your phone is here?"

                    l2 "I just set it down there so I don't lose it while we're
                    changing."

                    scene lewdlingerie030

                    "Avalon took notice of how the cell phone was propped up,
                    as if the camera lens was pointed at them."
                    "Not only that but the red light was on. Doesn't that mean it's
                    recording?"
                    "It suddenly dawned on her what Uncle [player_name] was watching
                    on his phone; he was watching them change!"
                    "Her mind flooded with thoughts and questions. Why the secrecy?
                    Was this some sort of game? Was it a test?"

                    jump recording


        label recording:

        scene bg lewdlingerie031
        show rec

        "Did the reason even matter? Avalon wanted to show herself off
        to [player_name]. She wanted him to desire her."
        "And the idea of being recorded with someone watching her change was
        strangely arousing."
        "Avalon liked the idea of her Uncle watching her get undressed. She imagined
        his eyes glued to the screen, looking on with want as she slowly disrobed."

        show bg lewdlingerie032 with dissolve


        "Would he gaze at her perky breasts and realize how much he hungered
        for her? Would he imagine himself cupping them in his big, strong hands?"
        "Would he touch himself to her naked body with uncontrollable lust?"

        l2 "Aha! Here it is. I thought I'd lost the skirt to this outfit but
        it was just hiding under some other clothes."

        show bg lewdlingerie033 with dissolve

        l2 "This might be a little tricky to get on so I'll help you out."
        l2 "Oof, that body is to die for, Avalon. Maybe your true calling is
        in modeling."

        a4 "No way! I'm far too short. Models are supposed to be tall like you, Leah."

        l2 "You can model for us anytime, Avalon. I can think of a bunch of outfits
        I wouldn't mind seeing you in."

        a4 "Okay but only if the pay is good! I don't get out of bed for less
        than a grand."

        show bg lewdlingerie034 with dissolve

        a4 "Oh my Gosh, I've never worn something like this before, Leah. There
        isn't much to it, is there?"

        l2 "Leather is my favorite! It's so exotic, sleek and sexy. You have to
        get real leather though. There's simply no substitute."

        a4 "Real leather? From animals? Why not synthetic?"

        show bg lewdlingerie035 with dissolve

        l2 "Because real leather breaths. It keeps you cool and it feels like
        a second skin."
        l2 "And it tightly hugs your body so your partner can see all your curves
        without actually seeing you naked."
        l2 "It's enticing and tantalizing, teasing him until he can't take it anymore
        and he has to just rip it off of you."

        a4 "I mean, to me it just feels nice. You make everything sound so hot, Leah."

        l2 "It's a gift."
        l2 "Let's step into the show room and see what [player_name] thinks of it."

        scene lewdlingerie036

        "[player_name] quickly put his phone away as the girls prepared to step out
        of the changing room."
        "He wasn't sure where Leah's perverted scheme was going to lead but at this
        point, he was merely a spectator."

        scene lewdlingerie037 with dissolve

        "Perhaps the problem would work itself out and there would be no repercussions?"
        "Things had been going so well for him thus far that perhaps that's exactly
        what would happen. The problem might just solve itself."

        scene lewdlingerie038

        l2 "Here's our first lingerie picks, [player_name]. I decided to go with
        silky and smooth and Avalon is trying on leather."

        b2 "You put her in leather for her first lingerie outfit? You're not exactly
        easing her into this, are you?"

        l2 "We're trying on lingerie, not sneakers. It had to be something
        provocative!"

        scene lewdlingerie039 with dissolve

        l2 "So what do you think, [player_name]? Does this outfit get your engine
        started? Do you like it?"

        "Avalon peered up at Leah, taking mental notes of how she acted. She wasn't
        shy at all while showing off for her lover."
        "She didn't chastise him for gaping at her body. In fact, she did the opposite."
        "It wasn't jealousy that gripped Avalon but instead it was admiration. She also
        enjoyed watching Leah reward her partner."
        "Could Leah teach Avalon how to be so confident and outgoing? Would she?"

        l2 "Strike a sexy pose, Avalon. Show [player_name] how hot you are. Don't
        be shy!"

        a4 "O-oh, right. Um, I think I have a good pose idea."

        scene lewdlingerie040 with dissolve

        a4 "How about this? What do you think, Uncle? Do you like my outfit?"

        l2 "That's perfect, Avalon. You look so alurring, even I want to jump your bones."

        scene lewdlingerie041 with dissolve

        l2 "So tell us, [player_name]. What would you like to do to us right now?"
        l2 "Are you burning with desire? Is your heart beating a mile a minute?"
        l2 "Is your erection about to pop the button off your pants?"

        scene lewdlingerie042

        menu:
            "Compliment the girls.":
                b2 "Uhh, yeah, you both look very tempting. Those panties certainly
                don't leave much to the imagination, Leah."

                scene lewdlingerie041 with dissolve

                a4 "And what about my outfit, Uncle? Do you like it?"

                b2 "It shows off the outline of your body which is tantilizing. It
                looks uncomfortable though. Is it uncomfortable?"

                l2 "Don't worry about how it feels. How does it look?"

                scene lewdlingerie042

                b2 "It looks like it would get pretty unbearable if you were sweating."
                b2 "Wouldn't it just lock it all in and get all sticky and gross?"

                l2 "We'll try something else. Let's get back into the changing room, Avalon."

                if lewd >= 4:
                    $ renpy.notify("淫荡之路检查：通过！")

                    a4 "Huh, I really though he'd like these outfits. Alright,
                    let's try the next!"

                else:
                    $ renpy.notify("淫荡之路检查：失败！")

                    a4 "This is actually getting a little too intense for me.
                    Is it alright if we skipped the rest?"

                    l2 "Of course, Avalon! If you're not enjoying this, we'll
                    move on."

                    scene lewdlingerie046

                    b2 "No worries, Avalon. Let's grab our stuff and we'll be
                    off to the meeting at Leah's work."

                    jump lewdcheckfail



            "Play it cool.":

                $ lewd += 1
                show screen notify("淫荡 +1", 2.0)

                b2 "You both look pretty hot, I guess. I like the shiny outfit
                well enough."

                scene lewdlingerie043 with dissolve

                b2 "Is anyone else feeling a bit sleepy today? I could go for a nap."

                l2 "You're so full of crap, [player_name]!"

                b2 "I'm just so... I don't know, bored I guess."

                scene lewdlingerie044

                a4 "He's bored? I thought we looked amazing."

                l2 "He's just doing this to see if we'll try harder, goading us into
                being more lewd. It's a game."

                a4 "A game? How do we win?"

                l2 "We don't, Avalon. We let him win this time."
                l2 "How about this, [player_name]?"

                scene lewdlingerie045 with dissolve

                l2 "Uh oh, it looks like Avalon's strap fell down."
                l2 "Do you like her outfit more when it's coming off of her?"

                b2 "That's... actually enticing as hell. Especially watching you
                pull her strap down."

                a4 "You like when Leah shows off my body to you, Uncle?"

                scene lewdlingerie046

                b2 "It's more about my partner giving me permission to look at
                another woman's body. It's exciting for a lot of reasons this way!"
                b2 "Is that weird?"

                if lewd >= 4:

                    $ renpy.notify("淫荡之路检查：通过！")
                    scene lewdlingerie045

                    a4 "N-no, it's not weird, Uncle. I like when Leah shows me
                    off to you too."

                    l2 "She does, [player_name]. You should feel the heat radiating
                    off of her right now. She is burning with arousal."

                    scene lewdlingerie047 with dissolve

                    l2 "Are you ready to try on another outfit. I have a lace ensemble
                    you'll just love."

                    "Avalon became entranced by Leah's eyes staring back at her
                    and Leah's hand so close to her breast."

                    a4 "Um... Sorry, what did you say?"

                    l2 "Am I distracting you by being this close, Avalon? Is my hand
                    on your chest drawing your attention away from my words?"
                    l2 "I can feel your heart beating so fast, Avalon. Are you horny
                    right now?"

                    a4 "Y-yeah."

                    "Avalon forgot about everything else as her focus tunneled
                    in on Leah."

                    l2 "Come on, Gorgeous. Back into the changing room."

                    scene lewdlingerie046 with dissolve

                    "[player_name] himself was also in a trance. He couldn't believe
                    how Avalon responded to Leah."
                    "She was bringing out a side of Avalon that [player_name] didn't even
                    know existed."
                    "Perhaps she was right and Avalon was more sexually charged
                    than he'd thought."

                else:
                    $ renpy.notify("淫荡之路检查：失败！")

                    scene lewdlingerie047

                    a4 "Actually, all of this is getting a little too much for me."
                    a4 "Is it alright if we stop for today? This is going beyond
                    my comfort level."

                    l2 "Of course, Avalon. Let's get changed, we'll gather our
                    things and head to the meeting."

                    jump lewdcheckfail

        scene bg lewdlingerie049
        show rec
        with dissolve

        a4 "You were right, Leah. Wearing leather is sexy. I feel like a different
        person when I'm in this."
        a4 "Like a... a naughty person!"

        l2 "I can never get enough of that feeling. It's intoxicating, isn't it?"

        show bg lewdlingerie050 with dissolve

        l2 "There you are! That pesky thing was harder to untie than it should have been."

        a4 "O-oh, you surprised me. I didn't expect you to pull it off so fast."

        l2 "No time to dilly dally. Slip out of that skirt and we'll try on the next."

        show bg lewdlingerie051 with dissolve

        "Avalon didn't shy away from the camera as she began to remove her skirt."
        "She was finding herself more and more relaxed in front of it."

        show bg lewdlingerie052 with dissolve

        "Her eyes fixated on the camera as she showed off her body to her Uncle."
        "Avalon gazed seductively at the cell phone as she posed her naked body,
        turning slightly away to conceal her womanhood."
        "It was as if she was calling to [player_name]. Inviting him to look
        upon her form and imagine what naughty things he could do to her."

        scene lewdlingerie015

        "[player_name]'s eyes were locked onto the video, his mouth agape with
        shock and awe."
        "Avalon was looking directly into the camera. She knew she was being
        recorded, she knew he was watching her."
        "Yet she posed for him and teased him with her supple breasts and her round,
        full buttocks."
        "[player_name] couldn't help but fantasize about running his hands all over
        her perfect body, feeling her legs, her toned stomach and her small breasts."
        "He was overcome with desire. He was overcome with lust!"

        scene bg lewdlingerie053
        show rec

        l2 "Oh yes, this lace is exactly what your butt needed, Avalon. I even
        found it in blue. That's your color, isn't it?"

        a4 "You noticed? You must be very observant."

        l2 "This outfit is sort of mix between innocent and naughty. For you, it is
        just right."

        a4 "I don't think those two things mix very well."

        l2 "Oh but they do, Avalon. Something innocent is always so much more exciting
        to play with."

        show bg lewdlingerie054 with dissolve

        a4 "What? That can't be true. Why would something innocent be more enjoyable?"

        l2 "Because it's untainted, uncorrupt. It's pure and unsoiled."
        l2 "It's like the first bite from a  piece of strawberry cheesecake. A perfectly shaped
        wedge of delicious, white cake drizzled in a fruit syrup."
        l2 "Sliding your fork through it and scooping up the freshly cut slice.
        And then opening your mouth to receive the cake from upon the fork."
        l2 "Once your tongue tastes the sweet, creamy texture from that very
        first bite, it's no longer just a piece of cake, Avalon."
        l2 "It's {b}your{/b} piece of cake."

        "Avalon's breath leapt at the phrase, 'your piece of cake'. She liked the idea
        of being [player_name]'s piece of cake."

        a4 "Do you think--"

        show bg lewdlingerie055 with dissolve

        a4 "Oh! You're still naked. I... I didn't expect that."

        l2 "I haven't put on my outfit yet. Do you like what you see, Avalon?"

        a4 "Your body is so much more womanly than mine. I feel like a little girl
        next to you."
        a4 "Everything is so exaggerated on you, Leah. Your hourglass figure, your
        big boobs and even your abs look spectacular."
        a4 "I feel like I'm looking at a perfectly sculpted bust of the ideal female."

        l2 "You are absolutely flattering me right now. But I'll tell you a secret."

        a4 "Oh? What secret?"

        l2 "I feel much better than I look. Go on, Avalon. Put your hand on me."

        a4 "Well, maybe just a little bit..."

        show bg lewdlingerie056 with dissolve

        a4 "Mm, so firm yet smooth like marble wrapped in silk. I can imagine
        [player_name] must love exploring your curves, Leah."

        a4 "His fingers must drift around you frequently, mapping out all the
        fine details of your body."
        a4 "If I were him, I don't think I'd be able to help myself. I'd have to explore
        you entirely."

        show bg lewdlingerie057 with dissolve

        a4 "I bet you let him touch you anywhere, don't you? Even..."

        l2 "Where are you heading there, Avalon?"

        show bg lewdlingerie058 with dissolve

        a4 "Oh! Sorry, I got carried away. I sort of forgot you were even here."

        l2 "You forgot I was here? I'm standing right in front of you. You're
        running you hand over my body."

        a4 "I know, I must have gotten lost in my own head."

        l2 "Do you want to touch my pussy, Avalon?"

        a4 "No! I... I didn't mean to--"

        show bg lewdlingerie059 with dissolve

        l2 "It's alright, Avalon. I don't mind. You can touch me anywhere you want."
        l2 "Here, let me help you."

        a4 "Help me? What do you--?"

        scene bg lewdlingerie060 with dissolve

        a4 "Oh!"

        l2 "This is where you were going, wasn't it?"
        l2 "You can wriggle your fingers around to get a better feel for me if you want."
        l2 "Do you like this, Avalon? Do you enjoy touching my pussy?"

        a4 "Actually, yes. I... I like this. Quite a lot, honestly. I can't explain
        it, it's just so... arousing."
        a4 "I didn't think you would be so warm. Is this your clitorus right here?"

        l2 "Ooh! Yes, it is. Be gentle with that."

        show bg lewdlingerie061 with dissolve

        a4 "I can't believe your so wet. My fingers are soaked already and I've only
        just touched you."
        a4 "Do I... do I arouse you, Leah? Do you like it when I touch you here?"

        l2 "Considerably more than I thought I would, actually. You're just so
        willing to experiment and to try new things."
        l2 "You have this thirst in your eyes sometimes, I half expect you
        to jump on top of me and have your way with me."

        a4 "Really? I'm not that outgoing when it comes to these things. I'm
        still inexperienced."

        l2 "I guess we'll have to fix that then, won't we?"

        show bg lewdlingerie062 with dissolve

        l2 "Open your mouth, Avalon."

        a4 "W-what?"

        l2 "Now that your fingers are soaked with my juices,
        I want you to taste me. Open your mouth."

        a4 "T-taste you? Okay..."

        show bg lewdlingerie063 with dissolve

        a4 "Ahh."

        l2 "That's a good girl, Avalon."

        show bg lewdlingerie064 with dissolve

        a4 "Mm!"

        l2 "There we are. That's me inside of you, Avalon. My succulent juices
        inside of your mouth."
        l2 "Now suck all of my fluids off your fingers. Drink all of me."

        "Avalon began sucking on her fingers to take in all of Leah's juices
        and then swallowed gently, accepting Leah into her body."

        l2 "And tell me, Avalon, how do I taste?"
        l2 "No, wait. Don't tell me. Let me taste for myself."

        show bg lewdlingerie066 with dissolve

        "Leah pressed her lips against Avalon's. She then parted her lips to allow
        her tongue to sneak out and circle inside Avalon's mouth."
        "As she pulled her tongue back into her mouth, she gently sucked on Avalon's
        upper lip."

        l2 "Mm."

        show bg lewdlingerie065 with dissolve

        l2 "I taste so much better coming off your lips, Avalon. Did you enjoy that?"

        a4 "I like it when you take control like that and push me to try things."
        a4 "I get too nervous to initiate activities and stuff on my own. It's
        a lot easier for me when you take the reins."

        l2 "I'll keep that in mind. We better finish getting dressed before [player_name]
        suspects something."

        scene lewdlingerie015

        "[player_name] was once again able to bear witness to an event so erotic
        and sexual that he almost couldn't believe his eyes."
        "It was both wonderful and terrible. He was observing events in that
        changing room that were making him desperately horny."
        "But being in a public place like this, he couldn't relieve himself."

        scene bg lewdlingerie067
        show rec

        a4 "Okay, I've got you all hooked up here. This outfit does wonders for
        your backside, Leah."

        l2 "Let's get out there and show off to our Bear-Man, shall we?"

        a4 "Yeah, let's do it!"

        scene lewdlingerie068

        l2 "Alright, [player_name], we have outfit number two here for you!"

        b2 "That's a skin tight outfit, isn't it? Are you wearing that lingerie
        or is it wearing you?"

        l2 "Perhaps both!"

        scene lewdlingerie069 with dissolve

        b2 "You both look spectacular. The red outfit reminds me of blood, like
        what's rushing to my penis right now."

        l2 "An appropriate color then, isn't it?"

        b2 "The blue outfit that Avalon is wearing makes makes me think of the sky.
        And I'm not going to lie, my head feels like it's in the clouds looking at her."

        a4 "Aw, that's sweet, Uncle. Which head though?"

        b2 "Both."

        scene lewdlingerie070 with dissolve

        l2 "Avalon, turn around and show [player_name] your butt."

        a4 "My butt? You think he wants to see that?"

        l2 "Of course! Men love a nice ass. Some even like booty more than boobs!
        And you've kept up with your cheerleading training."
        l2 "All those exercises make for one fine tooshy, Avalon. Come on, show it off."

        a4 "It sounds more like you want to see my butt, Leah."

        scene lewdlingerie071 with dissolve

        a4 "How about this position? Is this good?"

        b2 "You should be a butt model, Avalon. Or maybe a butt double for famous
        actresses."

        a4 "You're ridiculous."

        l2 "You do have a stunning little behind, Avalon. Not bony or flat at all.
        Full, round and absolutely delectable."

        scene lewdlingerie073 with dissolve

        l2 "Oh, it's so firm too! With just the right amount of squish to it."
        l2 "Do you know why it's important to have a little bit of meat on the booty,
        Avalon?"

        a4 "So when you sit down, you've got some cushion?"

        l2 "No, a thick booty is great for sex! Isn't that right, [player_name]?"

        b2 "You don't want to be thrusting into a girl only for your hips to slam
        into a bony, flat rear."

        a4 "Ooh, I hadn't thought about that. I've never had sex before."

        scene lewdlingerie072 with dissolve

        l2 "It's a waste of a perfect ass then, isn't it?"

        a4 "You think so?"

        b2 "Don't let her goad you into anything you're not ready for, Avalon."

        l2 "I'm not goading, I'm just stating that an ass like this doesn't last
        forever. You wouldn't want to let it go to waste!"

        a4 "I wouldn't mind having sex. It just... has to be with the right person,
        you know?"

        scene lewdlingerie073 with dissolve

        l2 "[player_name], would you like to feel Avalon's ass? It really is quite
        remarkable to squeeze."

        scene lewdlingerie074 with dissolve

        a4 "I don't think you've ever grabbed my butt before, Uncle."

        l2 "He has no idea what he's missing. Why don't you enlighten him?"

        a4 "Hmm. I don't know..."

        if lewd >= 5:

            $ renpy.notify("淫荡之路检查：通过！")

            scene lewdlingerie075

            b2 "It's up to you. I'm sure it's a butt worth experiencing but I wouldn't
            be devastated if you decided that would be too far."
            b2 "You've looked incredible in both outfits you've tried on so far.
            I'm so proud of you for taking such great care of yourself."
            b2 "Your mom let herself go after school but I can tell that you're going
            to be a knockout your entire life."
            b2 "You've got something she didn't. Something so beautiful inside you
            it borders on magical. Maybe there's not even a word for it."

            scene lewdlingerie076

            a4 "Okay, that definitely earned you a butt squeeze. You probably
            just made my whole week, Uncle."

            l2 "You're such a cheeseball, [player_name]. You're lucky we're
            both suckers for that kind of talk."

            a4 "You do know how to make a girl melt."

            scene lewdlingerie078

            b2 "Oh, you're going to face me?"

            a4 "Yeah, I want to see your eyes when you have your hands on me, Uncle."
            a4 "I want to see your genuine reaction when you touch me."

            scene lewdlingerie077

            a4 "There haven't been any guys in my life that have treated me as well
            as you have."
            a4 "You took care of me when I was younger. Now that I'm older, you're
            here again making me feel like a desirable woman."
            a4 "I wish more men were like you. Caring, encouraging and loving."

            b2 "You're a special woman, Avalon. You deserve to be treated special."

            a4 "Thank you. For now though, I think you should treat yourself.
            Touch me, Uncle."

            show butt_squeeze

            a4 "Your hands are so big. You're like a beastman, Uncle!"

            b2 "Leah wasn't lying, you've got an ass to kill for."

            a4 "Do you think it's enough cushion?"

            b2 "What do you mean?"

            scene lewdlingerie077

            a4 "You said earlier a full butt is great for sex because it provides
            cushion when you're thrusting into a girl, right?"
            a4 "Would this be a good butt for sex, Uncle?"

            b2 "If there is one question with a definitive answer, Avalon, it's that
            this butt was assuredly made for sin."

            a4 "Oh my God, that's so devilishly bad! What happened to my
            cheesy, wholesome Uncle?"

            b2 "He's got a jaw-droppingly attractive woman between his legs and
            a perfect ass in his hands. That's what happened!"

            a4 "Maybe you'll have me between your legs more often. If you're lucky
            enough!"

            l2 "Don't get him too worked up, Avalon. We still have one more outfit
            to try on!"

            a4 "Do you want to see our next outfit, Uncle?"

            b2 "I'd love to. Did you save the best for last?"

            a4 "I guess you'll find out."

            scene lewdlingerie081 with dissolve

            l2 "See you in a minute, Bear!"

            b2 "I'm going to need to take a baby aspirin if you girls keep teasing
            me like this. My heart can't take it!"

        else:

            $ renpy.notify("淫荡之路检查：失败！")

            a4 "I think this might be a good place to stop for today.
            I'm feeling a little overwhelmed."

            l2 "That's fine, Avalon. We would never push you to do anything you're
            not ready for."
            l2 "Which outfit was your favorite though?"

            a4 "Um, I liked the first one. It felt nice against my skin and
            wasn't too revealing."

            scene lewdlingerie075

            b2 "You're a gorgeous gal, Avalon. You always have been. If you
            want to come back sometime and try on other outfits, just let us know."

            a4 "Okay, thank you for understanding."

            b2 "You're welcome. Now you girls go get dressed so we can go to this
            meeting. I'm awfully curious to see what it's about."

            jump lewdcheckfail

        scene bg lewdlingerie082
        show rec

        l2 "You and [player_name] got pretty intimate there, Avalon."

        a4 "Oh, yeah, I didn't go too far, did I? It's just that I've kind of seen
        him differently today. I know you two are a couple but--"

        l2 "I don't mind sharing a little bit, Avalon. He's interested in you too."
        l2 "There's no rule that a man can't enjoy other women once he's in a relationship,
        is there? There's no rule that says he can't love other women either."

        show bg lewdlingerie083 with dissolve

        a4 "Are you saying we both could have him?"

        l2 "It's too early to decide something like that but after knowing you
        briefly, I'm already intrigued by the idea."

        a4 "But that means we would get to be intimate together too, doesn't it?"
        a4 "I could have both you and [player_name]?"

        show bg lewdlingerie084 with dissolve

        l2 "How about we focus on enjoying ourselves for now. We don't have to define
        anything, do we?"

        a4 "Uhm... I guess not, no. I like how things are going right now though."

        "Avalon was so distracted by the idea of being sexually intimate with
        Leah and [player_name] she didn't notice her ring slip off her thumb."

        l2 "What exactly do you like, Avalon? Can you describe your
        fantasies to me?"

        show bg lewdlingerie085 with dissolve

        a4 "You're both so sexy. You and [player_name] are in great shape, you're
        both forward with want you want but respect boundaries."
        a4 "You make it easy to want more. I feel perpetually aroused by what you
        say to me, Leah. And when [player_name] touches me, I just get so horny."
        a4 "I can't stop imagining you and him having your way with me. Groping me,
        ravishing me, fucking me..."

        show bg lewdlingerie086 with dissolve

        a4 "Oh! You surprised me."

        l2 "Is that what you want, Avalon? Do you want to be fucked?"

        a4 "Well, it's been hard all my life. I desire sex, I get aroused just like
        anybody else. But I've always had to take care of myself."
        a4 "All the people I've been around, I haven't wanted to be sexual with."
        a4 "You and [player_name] are the first people I've been excited about the
        idea of being intimate with..."

        l2 "The feeling is mutual. I find myself thinking about you too, Avalon."

        a4 "Really?"

        l2 "You're a bundle of joy wrapped in a sexy, blue-eyed package. You're eager
        to try new things, you're playful and you're a walking positive charge."

        show bg lewdlingerie087 with dissolve

        l2 "Sometimes when you're around, I'm so attracted to you that I wonder
        if I'm going to lose control and my hands are going to move on their own."

        a4 "Oh I wish they would, Leah. I want you to lose control on me."

        l2 "Do you, Avalon? Do you want me to go further?"

        a4 "Yes, I want that. I want you to go further."

        "Leah leaned in a little closer to Avalon and whispered in her ear."

        l2 "Beg me. Beg for me to touch you, Avalon."

        a4 "Please, Leah. Please keep going. I want you to touch me. I want you
        to play with my pussy."

        l2 "That's a good girl."

        show bg lewd_pussy with dissolve

        l2 "Is this what you wanted, Avalon?"

        a4 "Y-yes. Oh my God, yes. That feels so good, don't stop."

        l2 "You've been frustrated for a while, haven't you? Nobody to help satisfy
        your urges for all these years."
        l2 "Would you like me to satisfy you, Avalon? Would you like [player_name]
        to spread you out and penetrate you with his huge, throbbing cock?"

        a4 "Oh, fuck. That sounds so amazing. Yes, I want that. Yes!"

        l2 "Do you want him thrusting himself into your soaking wet pussy, Avalon?
        Do you want to feel his seed exploding into you, filling up your--"

        a4 "Oh!"

        show bg lewdlingerie090 with dissolve

        "Avalon let out a unintentionally loud moan, almost certainly drawing
        attention to their activity."

        l2 "Shh! You're going to get us in trouble. You have to be quiet."

        a4 "I'm sorry, I couldn't help it. It just erupted out of me."

        show bg lewdlingerie091 with dissolve

        l2 "Let's just hope people think I was tickling you. We'll have to continue
        this another time, alright?"

        a4 "It's kind of more arousing knowing there are people close by though."

        l2 "Finding yourself to be a bit of an exhibitionist, are you? Unfortunately,
        we could get into a lot of trouble so let's explore that another time."

        a4 "Fair enough. I guess we should finish putting on our last outfit then?"

        scene lewdlingerie016

        "[player_name] sat outside the changing room utterly flabbergasted by
        the events he was both witnessing and hearing."
        "He just watched as his [persistent.leah_rel] masturbated his niece in the next room.
        His brain shut down and his body was in shock."
        "They both not only wanted each other, but they wanted him too."
        "He would have wondered if there was enough blood in his body to power
        an erection of this magnitude if he'd had the ability to think at this moment."

        scene bg lewdlingerie092
        show rec

        a4 "Is this even an outfit? There's... there's nothing here. It's just
        a mostly see-through piece of fabric."

        l2 "I wasn't sure if this one was too exotic but with everything
        that's happened since we started, I figured you'd be willing to try it."
        l2 "It covers up the naughty bits which is what most bathing suits do."

        a4 "That's true. I guess it's really not that much different than being in
        a swimsuit if you're just considering how revealing it is."

        show bg lewdlingerie093 with dissolve

        a4 "This is certainly an interesting choice, Leah. It's basically just
        leather straps!"

        l2 "I feel like a wild animal wearing this. Let me tell you something, Avalon;
        there is nothing better than raw, animalistic sex."
        l2 "Just you and your partner relentlessly screwing each other like
        primitive apes until you're both too exhausted to continue."

        a4 "Er... well, right now I'm just picturing apes so..."

        l2 "You'll see one day, Avalon. You'll see."

        scene lewdlingerie094

        l2 "Okay, Teddy Bear, this is the last outfit. I hope you like them."
        l2 "Mine is leather straps and a collar. Can you imagine me on a leash, [player_name]?
        Or tied up in a cage, roaring for you to let me out?"

        b2 "Tiger Leah does sound sexy, actually. I could get into that. We'll
        have to find you some cat ears to go with that ensemble."

        scene lewdlingerie096 with dissolve

        a4 "And I'm just wearing a thin piece of fabric that barely covers my naughty
        parts. What do you think of this, Uncle?"

        b2 "You're getting braver by the minute! That is an extremely provocative
        suit, Avalon."

        scene lewdlingerie095 with dissolve

        l2 "She is becoming more courageous, isn't she? I guess she likes
        to draw eyes more than she thought."

        a4 "Well, when it's Uncle's eyes, I don't mind."

        b2 "You ladies have definitely given me enough eye candy to last the rest
        of the year. I'm one lucky son of a bitch."

        scene lewdlingerie097 with dissolve

        l2 "What do you think, Avalon? Should we make him just a little bit luckier
        today?"

        a4 "W-what? What do you mean? Did you have something in mind?"

        l2 "This!"

        scene lewdlingerie098 with dissolve

        a4 "Oh! My breasts!"

        l2 "[player_name] hasn't had a great look at these yet, has he? I bet
        he'd like a better view of them."

        a4 "W-well, I guess it's okay."

        l2 "Actually, he'd probably like to see... All of you."

        scene lewdlingerie099 with vpunch

        "Leah swiftly yanked Avalon's mesh outfit down and off of her body."

        a4 "Oh my God! You're crazy!"

        l2 "There we go! Much better, Avalon."

        scene lewdlingerie100 with dissolve

        a4 "You are chaos incarnate, Leah. I never know what nutty thing you're
        going to do next!"

        l2 "You were the one that said you were interested in exhibitionism, weren't
        you? I'm giving you what you want."

        a4 "But you're the one that said it was a bad idea here!"

        scene lewdlingerie101 with dissolve

        l2 "Don't be shy now, Avalon. Show off your perfect and petite body
        to [player_name]. You want to, don't you?"

        a4 "Mm, yeah. I want him to see me."

        scene lewdlingerie102 with dissolve

        a4 "What do you think, Uncle? Do you like seeing me naked?"

        l2 "Doesn't she have a body to kill for, [player_name]? An innocent little
        teenager body. Yummy, right?"

        scene lewdlingerie075

        b2 "A sight to be sure. You're both incredibly gorgeous women. Naked or
        otherwise."
        b2 "I can't believe how wild you two are together though. Not that I'm complaining!"
        b2 "But what do you--"

        scene lewdlingerie103

        mi "Excuse me, what the hell is going on in here? You can't walk around
        the show room naked, Missy!"
        mi "This isn't your own personal strip club, you slutty hussies!"
        mi "You have no idea how much trouble you're in right now. I should call
        the police!"

        scene lewdlingerie104

        l2 "It's not our fault your lingerie is low quality crap! The clasp didn't hold and her outfit fell off."
        l2 "I have half a mind to call my lawyer and sue this place for indecent exposure!"
        l2 "I could have this whole place shut down!"

        "Leah spoke fast and aggressively. It didn't matter that what she was
        saying was a mostly jumbled mess of incoherent nonsense."

        scene lewdlingerie105

        mi "N-now wait just a minute. We don't have to get the authorities and
        lawyers involved. Let's be reasonable."
        mi "I can't allow naked women running around my store. I have a reputation
        to maintain here. This isn't a brothel!"
        mi "S-so just put your clothes back on and you can leave peacefully."

        scene lewdlingerie104

        l2 "Fine, we'll leave without further disturbing your establishment but
         I demand you check your products better before putting them on display."
        l2 "My poor friend is going to need therapy after accidentally exposing
        herself to her Uncle! Who is going to pay for this therapy!?"

        scene lewdlingerie105

        mi "Cheese and Rice, family dinner's are going to be awkward from now on."
        mi "I can't apologize enough. I'm very sorry you had to go through this, Ma'am."
        mi "Look, you can have the outfit you have on complimentary. It's on the house
        as my personal apology."
        mi "Now if you would please clothe yourselves and promptly leave."

        scene lewdlingerie106

        l2 "Come on, Avalon. Let's get dressed and we'll get out of here."

        a4 "That was really scary. What's it called when you're both terrified
        and aroused at the same time? Is there a word for that?"

        l2 "Uhh... Afrandy? Like, afraid and randy at the same time?"

        a4 "Yeah yeah, that sounds right. I'm very afrandy right now."

        l2 "Me too, Avalon. Me too."

        a4 "Oh shit, is that my ring on the ground? It must have fallen off early!"

        l2 "I'm glad you noticed it before we left."

        scene lewdlingerie107

        b2 "So, uh... sorry about all that. I guess we haven't been the best
        customers today have we?"
        b2 "You must have had worse before though, right? I bet you get some
        real degenerates in here sometimes, don't you?"
        b2 "Hey, maybe we can start over. My name is--"

        scene lewdlingerie108 with dissolve

        mi "Go fuck yourself."

        b2 "Okay, I can take a hint. I'll just leave you to your work then."
        b2 "Thanks for not calling the police, I guess."

        scene lewdlingerie014 with dissolve

        "[player_name] decided to watch the conclusion of this rather perverted and
        seriously messed up peep show that Leah started for him."
        "He didn't like the idea of spying on Avalon while she was changing but
        she seemed rather okay with the whole thing."
        "[player_name] was curious to see what would happen next."

        scene bg lewdlingerie109
        show rec

        a4 "This whole thing has been entirely bonkers, Leah. But to be honest,
        I enjoyed it. This was a lot of fun."

        l2 "I know we still have to figure out what to do about your mom but I'm
        glad we could cheer you up."
        l2 "Nothing takes your mind off your problems better than exploring
        your sexuality."

        a4 "Yeah, well, maybe we can explore more later?"

        show bg lewdlingerie110 with dissolve

        l2 "We've been moving extremely fast lately, Avalon. I've enjoyed every
        second of it but we might need to slow it down a bit."
        l2 "Let's analyze how we felt about everything today and we'll talk about
        it all tomorrow."
        l2 "I'm going to just grab my phone real quick and we'll be off."

        scene bg lewdlingerie111 with dissolve

        a4 "I appreciate your concern, Leah. I genuinely do. But I think I should
        have some say over how fast we move."

        l2 "That's true, Avalon. I didn't mean to discount your opinion on this.
        How do you feel about everything?"

        a4 "Hmm. I don't know. Maybe I'll be able to tell better after we watch
        this recording together?"

        scene bg lewdlingerie112 with dissolve

        "It immediately dawned on Leah that Avalon had known the whole time
        that she was being recorded."
        "But she never said anything or tried to stop it. What does that mean?"
        "Leah had been caught red-handed and wasn't sure what to say next."

        l2 "Y-you knew? How?"

        a4 "The red light is on and the camera is conveniently placed to aim
        right at us."
        a4 "Not to mention [player_name] is out there looking at his phone
        like a hungry lion watching an injured gazelle."

        l2 "Shit. I'm sorry, Avalon. I just thought he might want to watch, you know?
        I wasn't sure if you'd be okay with it."
        l2 "Are you mad at me?"

        scene bg lewdlingerie113 with dissolve

        a4 "I'm not mad at you. It was kind of sexy knowing [player_name] was
        watching us. I enjoyed being recorded."
        a4 "I'm kind of eager to watch it too. Especially the part when you
        were rubbing my pussy."

        l2 "Damn. You're going to be a lot of fun to play with, Avalon. I can tell
        already."

        a4 "You don't have to lie to me, Leah. Or trick me or con me. I want to try
        stuff. And I want you to try stuff on me."

        scene bg lewdlingerie114 with dissolve

        "Avalon took the initiative for the first time and lunged forward, pressing
        her lips hard against Leah's."
        "She had become enamored with Leah. It was exciting being thrust into a new,
        erotic world of pleasure and passion."
        "And with [player_name] in the mix, she knew she was safe and cared for."

        scene bg lewdlingerie113 with dissolve

        a4 "We can slow down or speed up. It doesn't matter to me, as long as we
        don't stop. I want this, Leah. I want it all."

        l2 "You are a diamond in the rough, aren't you? I'm sure glad I made
        [player_name] get back into contact with you."
        l2 "I can already tell we're going to have some wonderful experiences together."
        l2 "Come on, we're probably already late to this meeting I have."

        a4 "Okay, but just one more thing?"

        l2 "Yes? What is it?"

        scene bg lewdlingerie114 with dissolve

        "Avalon again lurched forward and mashed her lips into Leah's."
        "She didn't want the moment to end. This had all been so much fun
        and she was so grateful that Leah was part of her life now."
        "She felt glee and joy at the thought of what the future may hold for
        her and her new relationship with her Uncle and his girlfriend."

        $ renpy.end_replay()
        if persistent.lewdlingerie == False:
            $ renpy.notify("You've unlocked Lewd Lingerie in the gallery!")
            $ persistent.lewdlingerie = True


        stop music

        jump meethenry

        label lewdcheckfail:

            scene bg lewdlingerie109
            show rec

            a4 "I hope you're not mad at me, Leah. This is fun and all
            but it's also kind of scary sometimes too."

            l2 "Don't apologize, Avalon. [player_name] and I won't ever
            push you to do anything you don't want to do."

            show bg lewdlingerie110 with dissolve

            a4 "Thank you, Leah. It's not that I'm not interested in
            seeing where all this goes but..."
            a4 "Well, I just need to take a slow, you know?"

            l2 "[player_name] and I will move at your pace. Or stop
            completely if you ask."
            l2 "Let's gather the rest of our things and we'll head
            to the meeting."

        label meethenry:

            scene meethenry01 with fade

            play music "audio/empathy.mp3"

            "This was an important meeting. Henry's mind shuffled through conversation
            topics he needed to address and how best to do so."

            play sound "audio/doorknock.mp3"

            "A light knocking on the door echoed through the room."

            scene meethenry02 with dissolve

            l2 "Mr. West? We're here for the meeting."

            hw "Please come in."

            play sound "audio/dooropen.mp3"

            hw "I'm glad you all could make it. Welcome to my office."

            scene meethenry03

            l2 "I apologize for being late, Mr. West. We've had a rather
            eventful morning."
            l2 "I left a message with your receptionist to let you know I was
            bringing one more person."

            scene meethenry04

            hw "I should be the one apologizing for bringing you in on your day
            off. You're a picture of dedication to your craft, Miss Leah."
            hw "And I'm always happy to accommodate one more, especially a friend
            of yours."

            scene meethenry05 with dissolve

            hw "I hope the eventfullness of your morning that you speak of wasn't
            too unpleasant?"

            l2 "Personal issues but I believe we're finding solutions."

            hw "I would expect no less from my best problem solver."

            l2 "You flatter me. Let me introduce you to [player_name], my boyfriend."

            scene meethenry06 with dissolve

            hw "Yes, of course. It's delightful to finally meet you, [player_name].
            Leah speaks fondly of you."

            b2 "That's a relief, I was worried she was growing bored of me. I appreciate
            you employing her despite her being such a trouble-maker."
            b2 "Redheads, am I right?"

            l2 "You'll have to forgive him, Mr. West. Formality isn't in his vocabulary."

            scene meethenry07 with dissolve

            hw "Nonsense. Decorum is overrated, a sense of humor is far more valuable."
            hw "I'm glad you could make it out to this meeting today. We have much to discuss."

            b2 "I can't imagine what you would want to discuss with me present but
            I'll make sure I'm all ears."

            hw "Excellent. I won't keep you in the dark too much longer in regards
            to this meeting's purpose."

            scene meethenry08 with dissolve

            hw "But first, I'd like to properly greet the young Miss Avalon.
            I had not expected you to accompany Leah today."
            hw "This is an unexpected delight. It's a pleasure to finally meet you."

            scene meethenry09 with dissolve

            a4 "Oh, no, you must have me confused with someone else. I'm just [player_name]'s niece."
            a4 "Leah and I only just met today so I'm nobody, really. You must be confused."

            hw "On the contrary! I'm rarely mistaken when it comes to people.
            You're Joseph's daughter, are you not?"

            scene meethenry10 with vpunch

            b2 "What? What did you say? You knew Johnny? How?"

            l2 "Calm down, Bear. What's gotten into you? You're acting crazy all of the sudden."

            b2 "I knew Johnny worked for Pridwyn before he died but I thought it
            was a different department. H-how would you know him?"

            scene meethenry11 with dissolve

            a4 "Y-you knew my father? I know he had some association with Pridwyn
            at one time but that's all."

            scene meethenry12 with dissolve

            a4 "Mom didn't like to talk about my dad so I know very little."
            a4 "But [player_name] told me he worked as a sale's representative for a
            company that sold bottled water."
            a4 "I... I can't even remember what the company was called."

            scene meethenry13 with dissolve

            b2 "Before you were born, Johnny got clean. But it was only thanks to the support of Pridwyn."
            b2 "He worked for them from then on. Or, well, a subsidiary. I didn't know much about it."
            b2 "He didn't speak much about work but he seemed happy enough with it."

            scene meethenry14 with dissolve

            hw "I apologize, Miss Avalon. My intention wasn't to startle you or your Uncle."
            hw "I didn't know Joseph directly. My father is the one who hired him and paid for his rehabilitation."
            hw "I had heard through the grapevine he affectionately named his daughter in honor of my father's company."

            scene meethenry15 with dissolve

            b2 "He told me it was because of the legend. His life changed when his
            daughter was born. He said he felt like a new person."
            b2 "She was a new start for him and when he held her, I could see it.
            His scars disappeared, his trauma was gone and he was well."
            b2 "She wasn't named after a company, she was named after what she
            brought to our lives; a new beginning."

            scene meethenry16

            hw "One reason does not negate the other."
            hw "The Arthurian mythology is heavily ingrained in our company.
            Most people we bring on develop some level of interest in it for this reason."
            hw "I'm sure Avalon here was an integral part of his recovery."

            scene meethenry17 with dissolve

            hw "His name for you was appropriate. I'm sure you meant the world to him."

            a4 "Well, I wasn't enough forever, obviously. I don't know if you
            heard but he overdosed some time ago."

            scene meethenry18

            hw "Overdosed? No, Joseph--"

            "Henry paused to process the information. [player_name] quickly took
            notice of his short, but obvious, certainty that Johnny had not, in fact, overdosed."
            "It occured to [player_name] that Henry knew more than he was letting on about Johnny."
            "He couldn't confront him about it with Avalon around. He wasn't sure if he
            would have anyway. [player_name] wasn't sure he wanted to know how Henry knew of him."

            scene meethenry19 with dissolve

            hw "Yes, of course. I remember now. It was horrible to hear about his relapse. My condolences."
            hw "I apologize but I must redirect the conversation. There is much I must discuss with Leah."
            hw "Perhaps we can revisit this topic at a later time?"

            scene meethenry20

            a4 "R-right. Well, I'd be eager to hear more about my dad so I'd very
            much like it if we could talk again."
            a4 "[player_name] is the only one that used to talk about him. I'd like
            to hear more stories about my Dad if I could."
            a4 "When I've met other people that knew him, they always seem to have
            such wonderful things to say about him."

            hw "I'll certainly make time for that in the future, Miss Avalon."

            scene meethenry21 with dissolve

            hw "For now I'd like to discuss an opportunity that was passed on from
            our star employee. Would you all follow me this way?"
            hw "Leah has been an instrumental part of our growth in the field of medical advancements."

            scene meethenry22 with dissolve

            hw "Some of her innovative ideas will play a tremendous role in the future of our society."
            hw "But as brilliant as she is,  it's not as much her intelligence
            that sparks these innovations as it is her unique perspective."

            scene meethenry23

            hw "[player_name], do you see this sword here? Tell me,
            what do you believe is at the end of this weapon?"

            scene meethenry24

            b2 "A pointy edge, I'd imagine."

            hw "And Leah, what do you believe to be at the end of this sword?"

            scene meethenry25 with dissolve

            l2 "A rock."

            b2 "Wha--? A rock? I don't think that's what he meant."

            scene meethenry26

            hw "Leah often sees answers and solutions that others wouldn't have thought of."
            hw "Leah has brought many clever solutions to problems others thought
            impossible to solve."
            hw "This may be a simple example but it serves to prove my point."

            scene meethenry24

            b2 "Hey, if I pull this sword out of this stone, do I become the new CEO of Pridwyn?"

            scene meethenry23

            hw "You would serve only to ruin an expensive and favorite decor of mine, [player_name]."

            b2 "Right, of course, I apologize. I wouldn't do that."

            scene meethenry26 with dissolve

            hw "I jest, Mr. [player_name]. I am not as stiff and cold a businessman as you might assume."
            hw "That is only a cheap prop. I'm sure if you turned it over, a 'Made in China' label would present itself."
            hw "Would you all join me at the table?"

            scene meethenry28 with fadefast

            "As everyone chose their seating and made themselves comfortable,
            [player_name] couldn't help but notice the seat selection Henry chose."
            "He didn't sit at the head of the table as he would have expected."
            "Instead he sat across from them, as if to present himself as just another
            voice amongst them."
            "He was many tiers above Leah in terms of the corporate hierarchy but
            sitting across from them, it felt as though they were all on the same level."

            scene meethenry27 with dissolve

            l2 "What is it you wanted to discuss, Mr. West? The research project you proposed would require me to be gone longer than I'm comfortable with."
            l2 "I just started a new relationship that I'd have to all but abandon for a year-long project."
            l2 "And I've already explained that no matter what progress we make, there are limitations we can't yet surpass."

            scene meethenry28

            hw "I wouldn't press so hard if I didn't think it were imperative
            that you lead the project, Miss Ravenscroft."

            scene meethenry29 with dissolve

            a4 "Ravenscroft?"

            b2 "That's Leah's last name. She took her adoptive parents surname,
            just as I took Frank's and Wendy's last name."

            a4 "Oh. What's this about a research project? I feel out of the loop."

            scene meethenry30

            hw "I apologize, Miss Avalon. You're part of this meeting and you should be informed. Allow me to explain."

            a4 "I didn't mean to interrupt. I was just curious."

            hw "Never apologize for seeking information. Knowledge is essential
            for progress in every walk of life."
            hw "Regarding the current topic, several years ago Pridwyn invested
            in a biomedical research division."
            hw "Leah was one of our first hires and her ideas have not only been
            revolutionary, they've also been extrodinarily profitable."

            b2 "Of course it's all about the money."

            scene meethenry31 with dissolve

            hw "This is a common misunderstanding. While there are many companies
            just trying to make a dollar, we're investing our profits in innovations."
            hw "The research and development for these innovations takes years
            without producing any goods or services to recoup expenses."
            hw "And there are many expenses. A facility, equipment, employees, taxes.
            Without substantial financial gain, we couldn't do this research."
            hw "We've also re-invested a considerable amount of what we've made
            back into Leah's department."

            scene meethenry27

            l2 "You have. I have double the staff from when I started, a larger facility and all
            the equipment I ask for."
            l2 "Not to mention my own compensation which has risen steadily over
            the years, for which I am not ungrateful."

            scene meethenry32

            a4 "W-wait, Leah's department? She runs it?"
            a4 "That's incredible. She must be invaluable, right?"

            scene meethenry30

            hw "Absolutely! And this research project we've decided to invest in
            cannot work without her. We'll have to scrap the whole thing."
            hw "That's why I've asked her in here today. I'm attempting to convince
            her to take on a special assignment."

            scene meethenry27

            l2 "It's not the project I'm objecting to. I can't be shut off from
            the world for an entire year, Mr. West."
            l2 "Working late or coming in on a weekend is one thing but this is
            an entire year of work."
            l2 "I'm not sure I can work effectively in these conditions. Even if
            I were to say 'Yes', I may be wasting your time and money by being useless."

            scene meethenry32

            a4 "Shut off from the world? Is the research in space or something?"
            a4 "I know I'm young and I don't have any idea what's going on,
            I certainly don't mean to be a pest."
            a4 "But it just seems to me that all this is awfully extreme."
            a4 "Are you working on a virus that turns people into zombies?"

            scene meethenry30

            hw "Our logo is of a shield, Miss Avalon. Not of an umbrella."

            "Avalon felt a sensation of jubilation when he confirmed that he
            understood her reference."

            hw "We're attempting to develop an artificial organ. Specifically,
            an artificial heart. The issue is the competition."
            hw "Whoever releases the first functioning device will own the market.
            It will be worth billions."
            hw "We've set aside enough funding for a year of research for the project."
            hw "The catch is that whoever works on the project will be isolated
            to keep the research from leaking to competitors."

            scene meethenry33

            a4 "A whole year though? [player_name] wouldn't get to see her that entire time?
            That's... awfully harsh."
            a4 "And she wouldn't be able to leave, right? You can't go shopping
            among other people or go to the beach."
            a4 "I don't know, Mr. West. I see that it's for a cause but it's simply
            too extreme."
            a4 "I can't say I blame Leah for rejecting it."

            scene meethenry30

            hw "You're correct on all points, Miss Avalon. Your youth does not hinder
            your wisdom, it would seem."
            hw "Your words lead me to my proposal for today."

            scene meethenry31 with dissolve

            hw "I'd like to invite [player_name] to the facility for the duration
            of Leah's stay."
            hw "You'll both be locked into the contract, you won't be able to
            leave or contact anyone outside of the facility."
            hw "But you'll be together. And, might I add, assisting in the invention
            of a device that will save countless lives."

            scene meethenry34

            b2 "Well, that's quite a proposal. It would be hard to say 'No' to--"

            scene meethenry35 with vpunch

            a4 "No, y-you can't! We just started spending time together again. You can't leave me!"
            a4 "Not again..."

            b2 "Er, Avalon, we... I haven't..."
            b2 "Shit. You're right, I can't leave you again. This complicates things."

            scene meethenry28 with dissolve

            l2 "You'll have to give me time to consider this. I'll need to discuss
            it in depth with [player_name] and Avalon."
            l2 "How long do I have to give you an answer?"

            hw "I'll need a decision made by Monday. Please note that whatever you decide will not affect your relationship with Pridwyn."
            hw "You're a valued member of this company despite your choice in this matter."
            hw "Allow me to walk you out."

            scene meethenry36 with dissolve

            hw "Thank you all for coming out today. Your willingness to sacrifice
            time on a well earned day off is a testament to your dedication, Miss Ravenscroft."

            scene meethenry37 with dissolve

            l2 "I've been meaning to show [player_name] where I work so this worked well for all of us."

            hw "And it was a pleasure to meet you, Miss Avalon. I look forward to speaking more with you soon."

            scene meethenry38 with dissolve

            a4 "Oh, yeah, I'd like that. Maybe we can invite you over sometime for dinner so we can talk more about my father?"
            a4 "If that's okay with you, Leah?"

            l2 "Of course!"

            hw "I'd like that very much. Let me know when and where and I'll make time for it."

            stop music fadeout 2.0

            hw "[player_name], would you mind if I spoke to you privately for a moment?"
            b2 "Oh, uh, sure. Is that alright with you, ladies?"
            l2 "Come on, Avalon. They have a lunch bar here with a pudding that is to die for!"

            scene meethenry39 with fadefast
            play sound "audio/doorclose.mp3"

            b2 "You know about Johnny, don't you? That's what this is about?"

            hw "I know more about Robert Gladstone than I do your friend, Mr. [player_name]."

            scene meethenry40 with dissolve

            play music "audio/i_will_remember.mp3"

            hw "When my father founded Pridwyn, he had goals in mind. Not for
            the company but for humanity."
            hw "The shield, Pridwyn, represents the protection he meant to provide
            for the community. But this isn't the middle ages anymore."
            hw "We can't battle tyranny with swords, we can't stop villainy with
            arrows. Power today isn't what it was three hundred years ago."

            scene meethenry41

            b2 "I'm not sure I understand where you're going with this.
            Are you fighting someone? Is it... my father?"
            b2 "Why are you telling me this?"

            scene meethenry47

            hw "Avalon and I have more in common than would first meet the eye."
            hw "Just as your father murdered her father, he also murdered mine."

            scene meethenry42

            b2 "W-what!? That's... how? Why? I don't understand. What are the odds of that?"
            b2 "Is that why you wanted to speak to me? You're angry at me for being his son?"
            b2 "I'm not associated with my father. I've only met him once."

            scene meethenry45

            hw "Slow down, [player_name]. We are not our fathers. Leah spoke
            highly of you and our meeting today reinforced your good nature."
            hw "I know you know about Joseph. I assumed Avalon did too but it
            would appear you haven't told her."
            hw "It's none of my business, you can tell her in your own time."

            b2 "Why would he go after your father? This doesn't make sense."

            scene meethenry46 with dissolve

            hw "Pridwyn has had a rivalry with Gladstone since the beginning.
            My father tried on many occassions to shut him down, to stop him from hurting people."
            hw "He was... unsuccessful. And eventually, Gladstone got to him."
            hw "It was likely unnecessary for him to kill Joseph, he could have
            bribed him or threatened him instead."

            scene meethenry45 with dissolve

            hw "He may have killed him more out of spite for Pridwyn than any other
            reason. I'm sure his association with us played its part."
            hw "I have spent the better part of the last ten years chipping away
            at his illegal operation."

            scene meethenry48 with dissolve

            hw "But as I said before, fighting in the corporate world is different
            than a grand battle between soldiers in an open field."
            hw "I've been using clever tactics to tear down his business."
            hw "Many of his previous buyers are now loyal to me and as a handshake
            agreement, they won't do business with him per my request."

            scene meethenry46 with dissolve

            hw "His business is finally on the brink of collapse; he'll soon be
            no more than a beggar on the street."
            hw "I wanted to tell you this. I hope it brings some peace to you and
            to Avalon when you tell her."

            scene meethenry43

            b2 "This is a lot to process. I only found out about Johnny's murder a few years ago."
            b2 "Why didn't you tell me sooner? Why didn't you find me and tell me
            you were after my father?"

            scene meethenry49

            hw "There is a lot of risk in this for me. The fewer people that knew
            about my crusade, the less likely it would leak."
            hw "Not everything I've done in pursuit of Gladstone's ruination was legal."
            hw "I hope none of what we spoke of today will find the ears of anyone
            else? With the exception of Leah and Avalon, of course."

            scene meethenry43

            b2 "I need to think about all this. It's too much to take in all at once."
            b2 "I don't even know that much about my father's business. I think it
            has something to do with selling artifacts?"
            b2 "I guess it doesn't matter. He killed my best friend and Avalon's
            father. I'm glad someone is fighting back against him."

            scene meethenry49

            hw "My father was a good man. He founded Pridwyn on a strong moral
            platform. After his passing, I've maintained that foundation."
            hw "I hope you can find some solace knowing that there are people
            out there pushing back against tyrants like your father."
            hw "But I digress, my intention was not to upset you though I feel
            I've done just that."
            hw"If you gather yourself and would like to talk more, I'll make myself available."

            scene meethenry44

            b2 "W-wait, Leah... It can't be a coincidence that she works for you, can it?"
            b2 "How much do you actually know about her?"
            b2 "And for that matter, how much do you actually know about me?"

            scene meethenry46

            hw "Leah is an extrodinary woman, [player_name]. I stumbled on her
            through my investigation of Gladstone."
            hw "It did eventually lead me to realizing her potential and I scooped
            her up to work here as quickly as I could."
            hw "Her relationship to Gladstone does not diminish her talent."
            hw "My association with Gladstone led me to her but my employment of
            her has everything to do with her abilities."

            scene meethenry41

            b2 "Okay, good, I'm glad to hear that. I guess that means you know
            that we're [persistent.relationship] then..."
            b2 "It just... sort of happened. We found comfort in each other and
            it went further than we meant for it to."
            b2 "But we're happy and that's what matters most to me. I'd do anything
            for her, Mr. West. I'd die for her."

            scene meethenry46

            hw "Your circumstances are unique. I can't imagine it from your perspective.
            It's also none of my business."
            hw "One thing I do know, however, is what it's like to be in a relationship
            that isn't traditional."

            scene meethenry44

            b2 "Society is quick to reject unconventional relationships. It constantly
            worries me what people might think if they knew about her and I."
            b2 "I appreciate your understanding. And also your discretion?"
            b2 "We haven't told anyone yet and we may choose not to."

            scene meethenry48

            hw "Mum is the word. Now, I have much to do. I will be eager to hear
            your decision regarding the trip on Monday."
            hw "And please don't worry about Leah's relationship with this company
            being negatively impacted if your decision is less than desirable for me."
            hw "Her position here and my fondness for her will be unaffected."

            scene meethenry50 with dissolve

            hw "I'll allow you time to process everything I've told you and you
            can contact my secretary if you would like to discuss things further."

            b2 "Knowing my father is getting his comeuppance is a relief. I don't
            want him to do to anyone else what he did to Avalon and I..."

            stop music fadeout 2.0

            b2 "That... dinner that Avalon mentioned. We're supposed to give you
            our decision on Monday, right?"
            b2 "How about dinner on Monday at my place. We can discuss it there?"

            hw "I'll be there. Farewell for now, Mr. [player_name]."

            jump avaleahtalk


    label avaleahtalk:


        scene avaleahtalk02 with fade
        play music "audio/touching_moment.mp3"

        l2 "We sure had an eventful day today, didn't we? I'm glad you were able
        to spend time with us this weekend."
        l2 "And remember, you're welcome to stay with us as long as you'd like.
        We'll help you as much as you need to get your life started in a healthy direction."

        a4 "I appreciate that, Leah. I didn't mean to cause so much drama for
        you and [player_name]."
        a4 "I know you two are trying to enjoy the beginning of your relationship.
        It's not fair for me to come in and put this burden on you and him."

        scene avaleahtalk01 with dissolve

        l2 "You're a delight to have around, Avalon. You haven't burdened us, you've
        gifted us with a wonderful new roommate!"
        l2 "I could really use a girlfriend anyway. [player_name] is amazing but
        he's not going to enjoy shoe shopping like we will!"
        l2 "I've been meaning to ask you about the ring he gave you. He said it
        was something he originally had made for your father?"

        scene avaleahtalk09

        a4 "My father overdosed when I was just a child. I don't remember him very
        well. [player_name] used to tell me stories about him though."
        a4 "They were good friends. I think [player_name] looked up to him as
        a sort of male role model, you know?"
        a4 "My mom didn't handle dad's death well. She's been a mess ever since.
        But Uncle was there for me when I was growing."

        scene avaleahtalk05 with dissolve

        a4 "He taught me how to ride a bicycle, how to cook and even signed me
        up for cheerleading when I was old enough."
        a4 "When he had money, he would buy me nice things and treat me to ice cream
        or pie."
        a4 "I owe him everything. I can't even imagine who I'd be or where
        I would be without him."

        scene avaleahtalk04

        l2 "I don't understand something though. You both talk affectionately about
        one another but you went years without speaking?"
        l2 "What happened exactly?"

        scene avaleahtalk09

        a4 "Uncle was different after he got that money. He didn't come to the house
        often but when he did, he was... distant."
        a4 "He was there but not there at the same time. He just wasn't the same
        person."
        a4 "I guess I was too young and naive to inquire what was wrong. I wish I had..."
        a4 "After mom stabbed him with a pen, he stopped coming by at all. I never
        found the courage to call him to check on him. I'm a terrible niece, aren't I?"

        scene avaleahtalk01

        l2 "Don't carry that weight, Avalon. Life doesn't come with a manual.
        We can't always know what's best for ourselves, let alone other people."
        l2 "[player_name] and I spoke about what happened between the time he
        wasn't visiting you anymore and the time we met."
        l2 "He was in a dark place. It might have been better that you weren't around.
        That darkness may have spread to you."

        a4 "Or maybe I could have been there for him and helped him overcome it."

        scene avaleahtalk04 with dissolve

        l2 "Yeah, maybe. But you were just a kid, Avalon. It was his responsibility
        to take the initiative and reach out to you."

        scene avaleahtalk02 with dissolve

        a4 "I'm happy that you came along and convinced him to do just that.
        You talk about him being depressed before but I can't see it at all right now."
        a4 "He's so different now too. He used to be more awkward and goofy but
        he carries a confidence now that I hadn't seen in him before."

        l2 "We've only been dating for a week but we've been friends for several months.
        I gave him nudges here and there."

        a4 "You two are a smart match. He's lucky to have you."

        scene avaleahtalk03 with dissolve

        l2 "I've been thinking a lot about your mother today, Avalon. What if we
        got a sort of babysitter for her?"
        l2 "Just someone who stops by a few times a week to check on her, bring her
        food and clean the house."

        a4 "That sounds expensive, Leah."

        l2 "It's imperative that we find a way to also get her into therapy."
        l2 "I found a therapist on the internet with high ratings. I may have snuck off
        earlier today and given him a call."

        scene avaleahtalk01 with dissolve

        l2 "He has a granddaughter that could stop by a few times a week and
        she's confident she can slowly convince your mom to start therapy."
        l2 "They offered me a reasonable price, Avalon. They could look after her
        for a while."

        scene avaleahtalk08

        a4 "I shouldn't have to hire someone to look after her. She's a grown adult!"
        a4 "It was supposed to be her responsability to look after me. Not the other
        way around!"

        scene avaleahtalk01

        l2 "You're a good daughter, Avalon. Better than she deserves. I don't
        know what happened in her life to lead her to where she is now."
        l2 "I do know that if we don't do something for her, you'll carry at
        least a modicum of guilt for not trying harder to help her."
        l2 "I don't want to do this for her, Avalon. I want to do this for you."

        if lewd >= 5:

            show screen notify("淫荡的结局-已达成！", 2.0)
            scene avaleahtalk07

            a4 "You're totally into me, aren't you? You can't get enough of
            this sweet Avalon cheesecake!"
            a4 "I wonder how many times you're going to watch that video of us in
            the changing room and swoon over me."
            a4 "Probably like a million!"

            scene avaleahtalk03

            l2 "First, I said we should slow down. I'm afraid I've corrupted you
            too much already."
            l2 "And when did you become so outgoing? Such a bold assumption
            for you to make."

            scene avaleahtalk05

            a4 "You make it easy to be more outgoing and forward. I feel like I
            can be playful with you."
            a4 "I also feel different after everything that happened today. It's
            like you've kindled a new flame inside me."

            scene avaleahtalk09 with dissolve

            a4 "I'm just worried that we're on the brink of an amazing journey together
            but you're about to take [player_name] and go on a year-long business trip."
            a4 "I don't want to stop you because I know it's important but I
            selfishly want you to stay."

            scene avaleahtalk04

            l2 "We haven't made a decision yet, Avalon. It isn't fair for Henry
            to ask such a thing from me."
            l2 "He knows that. He also knows the consequences of not asking it of me."
            l2 "It's a tricky situation and I need time to consider all the options."

            a4 "All the options? I thought there were just two? Stay or go, right?"

            scene avaleahtalk03 with dissolve

            l2 "Those are the options he set in front of us. That doesn't mean there
            aren't more, it just means those are the only obvious ones."
            l2 "Always consider the possibility that there are more choices
            than the ones someone gives you, Avalon."

            scene avaleahtalk02

            l2 "Let's get some sleep for tonight. We'll talk more about
            this tomorrow."

            a4 "Okay, I like that advice, Leah. You're right, maybe there are
            more options. Thank you for cheering me up."

            stop music fadeout 2.0

            l2 "You're welcome! I'll see you in the morning for breakfast. Good
            night, Avalon."

            a4 "Good night, Leah."

            jump nightb

        else:

            show screen notify("健康的结局-已达成！", 2.0)

            scene avaleahtalk07

            a4 "Oh, are you going to take over and become my new mom, Leah?"
            a4 "You do buy me nice stuff so maybe you're actually my 'Sugar Momma'!"

            scene avaleahtalk06 with dissolve

            a4 "W-wait, that was a little weird. Let's scratch that
            and pretend I didn't say it."

            scene avaleahtalk03

            l2 "How about we stick to being roommates and friends for now? You're
            old enough that you don't need a mom, you need a role model."
            l2 "I'm a bio-mechanical engineer in a healthy relationship and
            I take good care of myself both physically and mentally."
            l2 "As far as role models go, you could do a lot worse."

            scene avaleahtalk05

            a4 "So you would teach me life skills and stuff? That sounds amazing!
            I'd like that very much!"

            scene avaleahtalk09 with dissolve

            a4 "But you can't do that if you leave for this business trip.
            I know it's important but I don't want you and [player_name] to leave me."

            scene avaleahtalk04

            l2 "I know how you feel. Henry asked me a week ago to take on this
            project and I said 'No'."
            l2 "Now he's asking me again but yet again, I have something to stay
            for."

            scene avaleahtalk01 with dissolve

            l2 "[player_name] and I are still discussing it though. We haven't
            made any decisions yet."
            l2 "And hey, how about tomorrow when we do talk about it, we bring
            you into the discussion. You should have a voice in this."

            a4 "Really?"

            l2 "Of course, [player_name] is family and you two should have the
            opportunity to put forward your opinions on the trip."

            scene avaleahtalk02

            a4 "You're so nice, Leah. I'm glad [player_name] found you instead
            of some mean skank. I'd say he got awfully lucky."

            l2 "We're all pretty darn lucky to have each other, Avalon."
            l2 "Let's get some rest for tonight. We all have lots to
            think about. And I'll make us breakfast in the morning!"

            stop music fadeout 2.0

            a4 "Okay, that sounds great! I'll see you in the morning then."

            l2 "Good night, Avalon."

            a4 "Good night, Leah."

            jump nightb

        label nightb:

        if _in_replay:
            $ player_name = renpy.input("What would you like to name the MC?")
            if player_name.strip() == "":
              $ player_name = "Byron"

            menu:
                "Lewd Path." if persistent.bonusnightlewd:
                    $ lewd = 6

                "Wholesome Path." if persistent.bonusnightwholesome:
                    $ wholesome = 6

        scene nightwholesome01 with fade

        "After [player_name] finished his shower, he made his way to the bedroom."
        "Spending the day with his niece for the first time in years had sparked
        a feeling of joy inside him that he thought he might never feel again."
        "And now with her moving in, he had a family of two wonderful girls
        instead of living as he'd imagined he would have to: alone."

        scene nightwholesome02 with dissolve

        "Avalon had grown into a beautiful and mature adult that any parent
        would be proud of."
        "And Leah was a supportive and playful fireball with grand career ambitions
        and so much love to give."
        "She was also..."

        scene nightwholesome03

        play music "audio/soft_reminder.mp3"

        "... Asleep."
        "[player_name] could imagine the day had been hard on her."
        "She had made a new friend today and had a business proposal
        she was surely considering with great internal conflict."

        scene nightwholesome04 with dissolve

        "Gazing down at her, he couldn't help but notice all the fine details
        that made her so captivatingly beautiful."
        "He thought about the night they went out for dinner. It was their
        first date, their first kiss and their first sexual endeavor."
        "As a romantic partner, she revealed so many new and incredible
        sides to herself. She was lustful and eager to please."

        scene nightwholesome05 with dissolve

        "[player_name] couldn't help himself and stole a kiss while Leah slept."
        "Caught by surprise, Leah inhaled sharply as she awoke and noticed her
        lover in front of her."

        scene nightwholesome06 with dissolve

        l2 "Hey there, Teddy Bear. I was waiting for you to finish your shower.
        Did I fall asleep?"

        b2 "I didn't mean to wake you but I couldn't resist a good night kiss. Those
        lips are too irresistable, Leah. Sometimes I can't help myself."

        l2 "I bet these aren't the only lips you can't resist, [player_name]."

        b2 "You're right, there are another set of lips I'd love to play with
        tonight."

        l2 "You can have any part of me you want any time you want. You know that, [player_name]."

        scene nightwholesome07 with dissolve

        b2 "Now seems like a good time. Let's see if we can get you out of these pesky
        pajamas, Leah."

        b2 "Are you sure you're not too exhausted? We can wait until tomorrow."

        l2 "No, I have plenty of energy for you, Bear. Avalon should be asleep
        so as long as we aren't too loud, we can fuck."

        scene nightwholesome08 with dissolve

        b2 "I have something much more devious in mind before we get to that."

        l2 "Do you? I bet it's not as despicable as what I have in mind."

        b2 "Absolutely not, I don't think I have the capacity to reach your level
        of depravity."
        b2 "Take your top off so I can more easily ravish you, Leah."

        scene nightwholesome09 with dissolve

        l2 "With pleasure, my love. I know how much you love my breasts."

        b2 "Look at how I'm circling around to the other side of you like I'm
        caught in your boobs' gravitational orbit."

        l2 "One of these days, [player_name]..."

        scene nightwholesome10 with dissolve

        b2 "Do you remember the first time we met? I showed up at your door,
        you let me in and we sat down at that table you stole?"

        l2 "I didn't steal it, I took it without permission. It's only stealing
        if you get caught!"

        b2 "Well, I got a haircut the day before. I cleaned up my facial hair and I
        took a lot of time to find the right shirt..."

        l2 "You wanted to look good for me?"

        b2 "It was the first time in a long time that I was excited about something.
        I never dreamed you would change my life like this."
        b2 "I'm sure glad it turned out this way though."

        scene nightwholesome12 with dissolve

        b2 "You've renewed me. I'm happy for the first time in so long and it's
        because of you. Because I found you."

        l2 "Aw, [player_name]. Stop it, you're going to make me cry."

        scene nightwholesome11 with dissolve

        l2 "It was when you carried me to bed. I remember looking up at you
        after you laid me down and... that's when I fell."
        l2 "I knew I had to have you after that. I didn't care that we were
        [persistent.relationship], I knew I loved you as more than that."

        scene nightwholesome13 with dissolve

        b2 "I remember you pressing these lips against mine at the pool. I'd
        wondered for a while what they would feel like."
        b2 "But I was far too afraid to pursue you. Afraid of rejection, afraid
        of what others would think of us if you didn't."

        b2 "As a matter of fact, I was terrified when you kissed me. I was freaking
        out inside. Then, suddenly, I wasn't... I can't explain it."

        scene nightwholesome11 with dissolve

        l2 "Whatever happened, I'm glad it did. I was so scared you wouldn't
        reciprocate my feelings. I don't know what I would have done if you hadn't."

        scene nightwholesome15 with dissolve

        b2 "You probably would have pulled your braid forward. You do that sometimes
        when you get nervous. It's sort of endearing."

        l2 "I do, don't I? It's my comfort braid! I hide behind it when I'm unsure
        or worried."

        b2 "You don't do it as much anymore."

        l2 "I'm not scared anymore. Not when I'm with you."

        scene nightwholesome16 with dissolve

        b2 "I didn't show it but when you told me about your heart condition, I
        was petrified. I made some stupid jokes to cover my fear."
        b2 "I couldn't bear it if I lost you so soon after meeting you."

        l2 "It's not going to affect me for years, Teddy Bear. And by then, who
        knows what kind of technology we'll have access to."

        b2 "You know, I don't worry anymore. You're so damn incredible, I don't
        think there's a force on Earth that could stop you."
        b2 "You're an inexhaustable flame, Leah."

        scene nightwholesome17 with dissolve

        b2 "Also, you have incredible boobs."

        l2 "Hey! What happened to you being all sweet and wholesome?"

        b2 "These things have been staring at me for a while now. I can only resist
        your feminine beauty for so long!"

        l2 "I'm yours, [player_name]. You don't have to resist temptation when
        you're with me. Just take me whenever you want me."

        b2 "You are one of a kind, Leah. I have never even heard of a woman like you."

        scene nightwholesome18 with dissolve

        "[player_name] slowly slid his hand down to Leah's stomach."

        b2 "When you talk to me like that, my heart flutters and my head spins."
        b2 "I can't think about anything other than tearing your clothes off, pushing
        you down and planting myself inside you like a wild animal."

        scene nightwholesome19 with dissolve

        l2 "That's why I say it! I want you to do that, [player_name]. I don't care
        if we're in a park, a shopping mall or a police station."
        l2 "I want you to know that you can drop me to the floor and fuck me
        anywhere you want!"

        scene nightwholesome20 with dissolve

        "Leah's legs flew apart as [player_name] placed his fingers on the top
        of her vagina."

        b2 "Is this where you want me to fuck you, Leah?"

        l2 "Yeah, right there! That's where I want it, [persistent.byron_rel]!"

        b2 "Rub it for me while I get these boxers off. I want to watch you play
        with yourself."

        l2 "Yes, sir!"

        show rubitforme

        l2 "Don't make me wait, [player_name]. I want to feel you inside me!"

        b2 "What part of me do you want inside of you, Leah? My fingers? My tongue?"

        l2 "Your fat, throbbing cock! That's what I want inside my pussy, [player_name]!"
        l2 "Don't tease me so much. After all that sweet talk, you've got me
        ferociously randy!"

        scene nightwholesome23

        b2 "You're going to have to come closer if you want this cock, Leah."

        l2 "What are you doing? Why are you grabbing my leg?"

        scene nightwholesome24 with vpunch

        l2 "Woah!"

        b2 "That's why!"

        scene nightwholesome25 with dissolve

        l2 "I love it when you show off your strength to me, Teddy Bear."
        l2 "And when you're rough with me! Don't take any mercy on me!"

        scene nightwholesome26 with dissolve

        "[player_name] brought his erect penis down onto Leah's stomach, showing
        off his impressive girth."

        l2 "I swear, it's bigger everytime I see your cock, [persistent.byron_rel]."
        l2 "I want you to stir up my insides with it. Scramble my eggs, [player_name]!"

        scene nightwholesome27 with dissolve

        l2 "Fuck me so deep you penetrate into my womb! And then go even further!"
        l2 "Cripple me, paralyze me! Fuck me until you utterly destroy me!"

        b2 "Jesus, Leah. You could make a pornstar blush."

        scene nightwholesome29 with dissolve

        b2 "How about we start with this?"

        l2 "Ugn! Oh shit, I think it {b}did{/b} get bigger! You're stretching me so much,
        [player_name]! Keep going!"

        b2 "Hmm. I think we'll go at my speed. How does that sound?"

        l2 "Don't tease me like that! I need it! Force it all the way into me! Break me if you have to!"

        show 1night_ani with dissolve

        l2 "Oh yes, that's it! Pull me apart, [player_name]!"

        b2 "I can't believe how tight you are, Leah. If you squeeze any harder,
        I won't be able to get inside you."

        l2 "Then force it! Tear me open! Don't stop!"

        "Leah whimpered softly everytime [player_name] reached his maximum insertion.
        She tried to be quiet in consideration of Avalon in the next room."
        "But with every thrust, she could feel herself losing more and more control."

        l2 "Oh fuck!"

        if lewd >= 5:

            scene nightlewd01

            "Alerted by the noise in the next room, Avalon decided to investigate."
            "She was confident the sounds were those of two lovers passionately
            entangling themselves with one another."
            "She'd thought about simply putting earplugs in and leaving them
            to enjoy each other."
            "But she had so much pent up sexual energy from all the teasing
            earlier in the day that it drove her to peek on them."

            scene nightlewd02

            "Sure enough, they were in the middle of what looked and sounded like a rather
            aggressive sexual bout."
            "Avalon had become enamored with Leah after having been shown so much
            attention from her, both caring and sexual."
            "Seeing her spread out in front of her Uncle's naked form waiting
            to be penetrated by him, Avalon felt herself again become aroused."

            scene nightlewd03 with dissolve

            "She had felt lust for both of them earlier in the day and now they
            were both naked and fucking right in front of her."
            "Avalon could see her Uncle's cock for the first time. She imagined
            what it could feel like in her hands, in her mouth and between her thighs."

            scene nightwholesome32

            l2 "I can feel your cock pressing against my lips, [player_name].
            Put it inside me. Drop me on your cock!"

            b2 "I love it when you spread your legs so far like this. It's as
            if you're inviting me inside you."

            l2 "I'm yours, my love. You can pull me apart and come inside of
            me anytime you want!"
            l2 "But I want you now! Please enter inside me now, [player_name]!
            I want you to fuck me as hard as you can!"

            scene nightlewd04

            "Hearing them talk dirty to each other had Avalon overflowing
            with sexual desire."
            "Her mind was filling with lust as she listened to their pornographic
            dialogue."

            scene nightlewd05 with dissolve
            "She groped herself as she imagined [player_name] instead spreading
            her legs apart and entering inside of her."
            "She wanted to know what it would be like to be Leah in that moment."
            "What would it feel like to have her Uncle's hard cock pressing against
            her exposed pussy."

            scene nightlewd06 with dissolve

            "Avalon pressed two fingers against her pussy, feeling her juices
            begin to seep through."
            "Her wet hole was practically crying for attention, yearning to be fingered.
            It needed to be fucked!"

            show 2night_ani

            l2 "Oh yes, [player_name]! You're tearing apart my walls! Don't stop!
            Don't ever stop!"

            b2 "Do you like being bounced up and down on this dick, Leah?"

            l2 "It feels so good. Hammer yourself into me over and over until
            I collapse!"

            scene nightlewd11

            "Avalon surrendered to her thirst, threw her panties aside and began
            masturbating to her Uncle fucking his lover."
            "She couldn't help herself. She needed release, she needed to touch herself."

            show surrender

            "Her fingers glided over her pussy ferociously, back and forth."
            "Pleasure engulfed her body with each passing rub. With every swipe
            she felt her desire grow, she wanted more friction, more bliss!"

            scene nightlewd12

            "When suddenly, an uncontrollable moan launched from her mouth."

            a4 "Oh!"

            scene nightlewd13 with dissolve

            "Avalon quickly covered her mouth but it was too late. Her joyous
            act of pleasuring herself was announced."

            l2 "Avalon? Is that you out there? What are you doing?"

            "She fell quiet, not sure what to do. She was caught and dreading the
            consequences."

            scene nightlewd14

            l2 "I can see your shadow in the hallway, Avalon. Were you watching us
            have sex?"

            a4 "No! I just... I had to pee! I was making my way to the bathroom.
            That's all!"

            l2 "I'm not upset, Avalon. Come in here for a second."

            scene nightlewd15

            l2 "Where are your panties, Avalon? You weren't walking around out there without them,
            were you?"

            a4 "Okay, look, I heard you guys having sex and I was just curious. I
            wanted to watch."
            a4 "But it was really sexy and I got carried away and started to masturbate
            a little."
            a4 "It's just that you teased me so much today and I've never been
            so worked up before in my whole life!"
            a4 "I wasn't thinking straight because I've been so horny today."

            scene nightlewd16

            l2 "Are you implying it's my fault you were masturbating to [player_name]
            and I having sex."

            a4 "I mean, yeah, a little bit."

            l2 "That's an awfully bold claim. You could have just as easily
            masturbated in your room, right?"

            scene nightlewd17

            b2 "Come on, Leah. You teased the hell out of her today. It is a bit
            your fault she's so charged up."
            b2 "I'm sure if the tables were turned and you were in her shoes,
            you would want to watch too, right?"

            l2 "You have a point. I guess there's only one thing to do then.
            Come here, Avalon."

            scene nightlewd19

            l2 "How much did you see and hear?"

            a4 "Not that much. I saw you and Uncle having sex and I heard you
            talking dirty to each other."
            a4 "You're really vulgar in the bedroom, Leah."

            scene nightlewd18

            l2 "It's more fun when you tell each other what you want and how
            you feel. Especially if you exaggerate and say it super naughty!"

            a4 "How did you get so good at it?"

            l2 "I have a vivid imagination. It's half of what makes me so good
            at my work."

            scene nightlewd22 with dissolve

            l2 "I wanted to slow things down with you, Avalon."
            l2 "I felt like we were moving a little fast and I didn't want to push
            you into things you may not be ready for."

            scene nightlewd19

            a4 "I'm old enough to make decisions for myself, Leah. I... I like you."
            a4 "You're so pretty and caring, I think I have a little bit of a crush
            on you."
            a4 "And I've seen [player_name] in a different way lately. I've always
            loved him but now I keep picturing him... you know..."

            l2 "You keep picturing him fucking you, Avalon?"

            a4 "W-well, yeah..."

            scene nightlewd21

            l2 "Trust me, I know exactly how that is."

            scene nightlewd18 with dissolve

            l2 "I know for a fact he's interested in you sexually too. He told me!"

            scene nightlewd25

            b2 "After I saw you naked, it was impossible not to be sexually interested
            in you."
            b2 "But Leah and I discussed it and said we would only carry forward
            with exploring the possibility if you were interested."
            b2 "Otherwise we would be here for you strictly as friends."

            scene nightlewd22

            l2 "So what do you say, Avalon? Do you want to join us for some fun tonight?"
            l2 "We won't do anything too crazy tonight and it will mostly just be
            us all getting used to each other."
            l2 "But I can assure you it'll be a lot of fun."

            scene nightlewd20

            a4 "Oh my God, really!? You would let me join? That would be epic!"
            a4 "I mean, I trust you and Uncle to treat me well so I can't imagine
            better people to start my sexual adventures with."

            scene nightlewd22

            l2 "We have to set some ground rules though."
            l2 "[player_name] and I have been pushing ourselves to try new things
             but we never want to go past the other person's comfort point."
            l2 "So we have a safeword. If you say the word 'Pineapple', we'll stop
            whatever we're doing immediately."

            a4 "'Pineapple'?"

            scene nightlewd23

            "Leah's hands shot up in surrender, showing off the power of the word."
            "Avalon gleamed at the spectacle as her understanding of the safe word
            took hold."

            a4 "Oh! It's like an abort code!"

            scene nightlewd24 with dissolve

            b2 "We don't mess around here, Avalon. Sex can be both wonderful
            and terrible."

            a4 "Terrible..?"

            scene nightlewd25

            b2 "It's the single most potent act people can perform together. You
            can lose yourself in the pleasure and find complete ecstasy."
            b2 "Sex is supposed to be enjoyable because it's so important to
            our survival. Some argue it's the single most important thing we do!"
            b2 "But it can also be harmful if performed on someone who doesn't want
            it or if you do something to a sexual partner they don't like."
            b2 "If you're not enjoying yourself absolutely then we're doing
            something wrong and we need to step back to evaluate things."
            b2 "You understand?"

            scene nightlewd24

            a4 "So if any of us get uncomfortable, we can just say the word and
            we'll stop. I get it."
            a4 "Have you ever used the safe word before, Uncle?"

            scene nightlewd21

            l2 "I put my pinkie in his bum a few days ago. I was shocked
            at how dramatic his reaction was."
            l2 "I've never heard a man cry out in such a high pitch before."
            l2 "You should have seen him run away from me. It was freakin'
            hilarious."

            scene nightlewd25

            b2 "We'll never judge you for saying the safe word, Avalon. We
            will always respect your preferences."
            b2 "But with that said, Leah and I are comfortable enough with
            each other that we can tease one another about these things."
            b2 "Also, don't try to put anything in my butt."

            scene nightlewd22

            l2 "Are you ready to get started, Avalon?"

            a4 "Yeah, I'm ready!"

            l2 "Okay, take off your bra then. This is a clothing free zone!"

            b2 "What happened to your ring, Avalon?"

            scene nightlewd26

            a4 "Oh, it's a little too loose so I took it off so I didn't lose
            it while I slept. I'll put it back on tomorrow."

            b2 "Maybe we need to have it resized."

            a4 "You know, I feel strange when I'm naked around you and [player_name]."
            a4 "You're both so much bigger than me. I'm like a little gnome
            to you guys."

            l2 "People come in all different shapes and sizes and everyone has
            their own preferences."
            l2 "I find your size quite sexy, Avalon. It projects a sense of innocence
            and youth."

            b2 "I agree, you're a freakin' knockout, Avalon."

            scene nightlewd27 with dissolve

            a4 "Well, I am innocent. I haven't done sex stuff before."
            a4 "But why would that be sexy? Wouldn't it be a turn off? I mean,
            I don't know how to please you guys as well as you know how to please each other."

            l2 "Do you want to take this one, Teddy Bear?"

            scene nightlewd28 with dissolve

            a4 "Oh, you're behind me? What are you--"

            b2 "I'm going to explain it to you, Avalon."
            b2 "I don't know the science behind it but when I'm standing close
            to you, and you're so small, I feel an urge to keep you safe."

            a4 "Why would that be sexy?"

            l2 "It could have to do with men's reward system. They protect you
            with a subconcious desire to be rewarded later."

            a4 "With sex?"

            l2 "What could be a better reward?"
            l2 "However, sometimes protecting someone and watching them grow and
            prosper is its own reward."

            scene nightlewd29 with dissolve

            b2 "You've grown into a beautiful and fun woman, Avalon. You're desirable
            for many reasons, not just because you're innocent."

            a4 "You desire me, Uncle? You want me?"

            b2 "I want you to enjoy your life, Avalon. I want to help make that happen."
            b2 "Leah has opened me up to a world of pleasure I never knew existed.
            And yeah, I wouldn't mind showing some of it to you."

            scene nightlewd30 with dissolve

            a4 "I can't imagine better people to experience that with. I love you,
            Uncle."

            b2 "I love you, too, Avalon. I'm glad you decided to join us on this
            journey."

            scene nightlewd31

            l2 "Do you want me to show you something spectacular, Avalon?"

            a4 "Um, sure, what is it?"

            l2 "It's probably my favorite thing in the whole world to play with right now.
            Let me get it for you."

            scene nightlewd32

            "Leah reached in between Avalon's legs and began groping around."

            a4 "Ugn. That's my vagina, Leah. You're-- you're touching me right now.
            I thought you were going to show me something."

            l2 "Hang on, all the sentimental talk made it retreat a bit."

            "With a little tugging, Leah was able to bring [player_name]'s cock
            back to it's former erect glory."

            scene nightlewd33 with dissolve

            l2 "There we are!"

            a4 "Oh! Oh my God, Uncle. Is that your penis? It's pressing into me!"

            b2 "Your thighs are squeezing my erection, Avalon. It's getting me
            even more turned on."

            a4 "You... you like it?"

            scene 4nightani01 with dissolve

            l2 "Men like to have their dick's tugged on, Avalon. Go on, move your
            hips back and forth."
            l2 "You'll jerk him off while he rubs his dick against your pussy."

            a4 "Okay, that sounds fun. Right, Uncle?"

            b2 "It sounds amazing! Let's give it a try."

            show thighjerk with dissolve

            a4 "O-oh, you're right, he's rubbing up against my pussy with his dick!"
            a4 "I... I like it! I like it a lot!"

            b2 "Ugn. I can tell, you're squeezing your thighs together so much
            harder now!"

            l2 "I can see the head of his cock rubbing against your clit, Avalon.
            That must be driving you wild!"

            a4 "Oh, it's so hard and warm! The friction is driving me crazy!"
            a4 "I think... I think I'm going to orgasm!"

            l2 "So soon?"

            a4 "I've never had a dick rub against me like this before. And it's
            my Uncle! Oh! It's too incredible, I can't take it!"

            scene nightlewd34

            a4 "I'm... I'm cumming! Ugn!"

            scene nightlewd34 with flash

            b2 "Ugn! I can feel your body convulsing on my dick, Avalon."

            "Avalon's eyes rolled back in her head and her legs began to fail
            her as her orgasm continued with extreme intensity."

            scene nightlewd34 with flash

            a4 "Ooh! I can't stop! I... I can't stand up anymore."

            scene nightlewd35

            "Avalon collapsed and fell over on top of Leah."

            l2 "Oh, goodness! You really did grow weak from orgasming so hard!"

            b2 "Damn, are you alright, Avalon?"

            scene nightlewd36 with dissolve

            "Avalon breathed heavily, attempting to catch her breath. She took
            comfort in Leah's bossom."

            a4 "It was amazing, Leah. You were right, it's so incredible."

            l2 "That wasn't even sex! That was just grinding!"

            a4 "I can't even imagine sex. I can't!"

            l2 "Your sensitivity must be so high, Avalon. I'm finding myself
            rather jealous right now!"

            scene nightlewd37 with dissolve

            l2 "Hey, you want to hear some great news?"

            a4 "I think so, y-yes."

            "Leah leaned in and whispered to Avalon."

            l2 "It gets even better. This is only the beginning. Just wait until
            we open up your wet pussy and start putting things inside it."

            scene nightlewd38 with dissolve

            a4 "Oh my God. Inside of me? What would you put inside of me, Leah?"

            l2 "How about we start simple with your Uncle's cock?"

            a4 "I think it's too big. I don't have enough room to take his penis,
            Leah."

            scene nightlewd41

            b2 "Oh I think we can make it work. The pussy is a magical thing;
            it can stretch to accommodate quite a bit."
            b2 "And with as wet as you are right now, I'd probably slide right in."

            scene nightlewd39

            a4 "Hey, what are you doing back there? I'm too sensitive right now.
            I just came!"

            b2 "Do you want to come again?"

            a4 "Yeah... but aren't you supposed to take a break after you cum?"

            b2 "I bet you can handle one or two more, Avalon. Let's see if we
            can make it happen."

            scene nightlewd41

            b2 "Can you feel me parting your lips, Avalon? Do you like it?"

            a4 "Y-yeah, it feels nice. My legs are still quivering from before."

            b2 "I can feel you shaking a little bit. But you're soaking wet.
            I bet with almost no effort, I could just..."

            scene nightlewd42 with vpunch

            a4 "Oh! Fuck! It's inside me. It's inside me!"

            b2 "You were right, Avalon. It is so tight! I can't believe it!"

            scene nightlewd40

            a4 "It's too much, it's too much! It feels so weird."

            l2 "Have you never had anything in your pussy before, Avalon?"

            a4 "N-no, just my fingers. Is it supposed to feel so strange?"

            l2 "[player_name], let's stop for a minute. Penetration is a little
            too much for her right now."

            scene nightlewd43

            b2 "Sorry, sorry! I might have gotten carried away. It's easy to
            do when you're with two magnificently beautiful women."
            b2 "I'll give you girls a moment. Don't mind me, I'll just be
            standing here with my... massive erection."

            scene nightlewd44

            l2 "Having a foreign object enter into your body can be both invasive
            and uncomfortable."

            b2 "You're telling me! No more fingers in my butthole, Leah!"

            l2 "Having someone inside you is the closest you can ever be to someone.
            You're literally merging two bodies to become one, if only for a moment."

            a4 "You're saying I shouldn't reject the feeling but instead embrace it."

            scene nightlewd45 with dissolve

            l2 "You and I are built to accept that which we love into our bodies.
            Ourself, our partners or even a fetus when we're pregnant."
            l2 "We want our partner inside of us. Allowing them into us is both the
            gift of acceptance and pleasure."
            l2 "[player_name] is a great man who we both love dearly. We can show
            that love in many ways but one of the most intimate is through intercourse."

            scene nightlewd46

            a4 "I've never really thought about it like that. I always thought
            sex was just... sex."
            a4 "But you're saying it's more of a bonding experience?"

            scene nightlewd45

            l2 "Of course it is! It can build trust, release stress and can
            be extremely enjoyable."
            l2 "Sharing the experience with another is a potent bonding experience."

            scene nightlewd47

            l2 "Come here, [player_name]. I want to introduce Avalon to our mutual
            friend more directly."
            l2 "I think we probably surprised her with it early."

            b2 "Looking down at you girls naked like that, he hasn't lost any potency
            at all!"

            scene nightlewd48 with dissolve

            l2 "The penis is an awesome male anatomical appendage. There's simply
            nothing else on Earth like it!"
            l2 "It's alive, Avalon! It throbs and moves and grows depending on
            its owner's feelings and what they're experiencing."
            l2 "You can feel its warmth, its reactions and its pulse of life."
            l2 "Take ahold of it, Avalon. Feel it in your grasp."

            a4 "Okay."

            scene nightlewd49 with dissolve

            l2 "That's part of [player_name]. The animalistic part that desires
            only one thing: pleasure!"

            a4 "It's so hard right now. I can feel it pulsing like you said. And
            the muscles keep contracting."

            b2 "You're tiny little hand feels amazing, Avalon. I can't explain it!"

            l2 "Perhaps God is just a penis."

            scene nightlewd50 with dissolve

            a4 "W-what? That's a weird thing to say. Why do you think that?"

            l2 "When a man ejactulates, he spews semen inside of us and the sperm
            within that semen fertilizes the eggs we have in our bodies."
            l2 "Those eggs can't grow without being fertilized so technically,
            the penis creates life."

            a4 "So maybe God is just a big life giving penis?"

            l2 "Obviously it's absurd but profound in a sort of warped way, isn't it?"

            a4 "Mostly just absurd. But... Yeah, I like the idea."

            scene nightlewd49 with dissolve

            a4 "So this... is supposed to go inside of me. If I accept it into
            my body, Uncle and I will build a stronger bond?"

            l2 "Sure, if you want to think about it like that. It also feels
            incredible!"

            a4 "I... want to try it. I want feel it inside me, Leah."

            l2 "Lay back and I'll help you."

            scene nightlewd51 with dissolve

            l2 "Before we start, remember the safe word. We can stop at any time."

            a4 "Right. I remember."

            l2 "You look really sexy laying there, Avalon. I kind of want to kick
            [player_name] to the curb and keep you all to myself!"

            b2 "You wound me!"

            l2 "Do you know what I can't get enough of, Avalon?"

            a4 "What?"

            show nippletug

            l2 "These cute, strawberry-colored nipples. I just can't control myself
            around your petite little body, Avalon."

            a4 "Oh! I like it when you talk to me like that, Leah. It really turns me
            on."

            l2 "Does it? Do you know what else might turn you on even more?"

            a4 "W-what?"

            l2 "[player_name] having his way with your little body. How about that?"

            a4 "Wow, you change a lot during sex."

            scene nightlewd54 with dissolve

            b2 "I know, right?! She's a completely different person when we're
            intimate. It's like she gets possessed or something!"

            a4 "O-oh! Uncle! Your... your penis is on me."

            b2 "It's size is sort of obnoxious, isn't it? Sometimes I'll turn too fast when
            I'm naked and put a hole in the wall."

            a4 "No you don't! You're ridiculous."

            scene nightlewd55 with dissolve

            b2 "So what do you think, Avalon? Are you ready to give it a try?"

            a4 "I'm a little nervous but I'm also so freakin' horny I could die."
            a4 "I... I want to try."

            scene nightlewd56 with dissolve

            a4 "Besides, thinking about your penis the way Leah described it is...
            sort of comforting in a way."
            a4 "I want it, Uncle. I want you inside me."

            b2 "We'll start with just the tip and then you can tell me if you're ready
            for me."

            a4 "S-slowly, please. Don't just--"

            scene nightlewd57 with vpunch

            a4 "Gah! Too fast, Uncle!"

            b2 "Shit, sorry! It just sort of slipped right in."

            scene nightlewd58 with dissolve

            a4 "It's okay, leave it in. I want to get used to it."

            a4 "Do you... do you like it, Uncle? Do you like being inside me?"

            b2 "I've always enjoyed being as close to you as possible. I can't
            be any closer than this so of course I like it."

            a4 "Is it supposed to hurt a little bit?"

            scene nightlewd59 with dissolve

            l2 "It won't for very long, I promise. Your body has to get used to
            accommodating something so large. But it quickly will."
            l2 "How does it feel otherwise? Do you like it?"

            a4 "It feels like there's something inside my vagina."

            "Leah chuckled lightly before responding."

            l2 "Yeah, it's better when it's moving in and out."

            scene nightlewd58 with dissolve

            a4 "Can you put it a little further in, Uncle?"

            b2 "Sure, tell me if it's too much."

            scene nightlewd57

            b2 "Erg, ehm. I'm pushing lightly but you're a little too tight, Avalon."
            b2 "I'm going to use just a little more force here..."

            scene nightlewd60 with vpunch

            a4 "Ah! Whoa whoa!"

            b2 "Sorry! That may have been too much force."

            scene nightlewd63

            a4 "Oh my God, Leah was right. It's better when there is friction."
            a4 "It feels so different now, like an electrical current of pleasure
            just fired through me."

            scene nightlewd60

            l2 "Trying rubbing your clitoris, Avalon. Really get your juices flowing
            so [player_name]'s cock slides in and out easier."

            a4 "O-okay, like this?"

            show clitrub

            a4 "Mm, yeah, you're right. This is making me so horny."
            a4 "Touching myself like this with my Uncle's cock inside me is so
            arousing!"

            l2 "Do you want more, Avalon?"

            a4 "Yeah. Yeah, I want more! Make me feel good, Uncle!"

            l2 "Tell us what you want. Tell [player_name] what you want him
            to do to you."

            a4 "I want you to fuck me, Uncle! I want you to fuck me until I cum
            again!"

            scene 5nightani11

            b2 "If you want it, you got it, Avalon. Here it comes!"

            show firstfuck

            a4 "Ahh! Oh my God, you're so deep! You're going so deep, Uncle!
            I'm gonna die!"

            l2 "Remember, Avalon. You're accepting him into you."

            a4 "He's going to break me, Leah! It feels so good and so weird
            at the same time!"
            a4 "My pussy is on fire! I'm going to melt!"

            l2 "Do you want to stop?"

            a4 "No, no, I don't want to stop. Not if Uncle likes it. I can handle
            it!"
            a4 "Do you like it, Uncle? Do you like fucking my pussy so deep?"

            b2 "It's turning me savage, Avalon! I can't get enough of your tight
            little cunt!"

            a4 "Oh fuck, I'm going to orgasm, Uncle! Cum with me, I want to feel
            you cum inside me!"

            b2 "Okay, Avalon, I'm about to explode! Just hold on!"
            b2 "Here it comes!"

            scene 5nightani31 with flash

            b2 "Oh fuck yes, Avalon! Take my cum! Take all of it!"

            a4 "Ugn, I can feel it shooting inside me! More, Uncle! Fill me up!"

            scene 5nightani31 with flash

            l2 "Yes, Avalon! Accept your Uncle's seed deep inside you!"

            scene nightlewd64

            "Just as [player_name] began pulling out..."

            scene nightlewd65 with dissolve

            a4 "No, Uncle! Stay inside me! Fill me up more!"
            a4 "Don't ever pull out of my pussy! I want it more!"
            a4 "I'm cumming so hard right now, it won't stop!"

            scene nightlewd67 with flash

            a4 "Oh fuck, my womb is so full right now! There's so much of you
            inside me right now, Uncle!"
            a4 "It feels like my stomach is going to burst!"

            "Avalon convulsed violently as her orgasm continued."
            "Her vision began to fade as she started to black out from
            exhaustion."

            $ renpy.end_replay()
            if persistent.bonusnightlewd == False:
                $ renpy.notify("You've unlocked Bonus Night (Lewd Path) in the gallery!")
                $ persistent.bonusnightlewd = True

            scene black with dissolve

            "..."

            l2 "Avalon?"

            scene nightlewd68 with fade

            l2 "Avalon? Wake up, Avalon."
            l2 "Are you still with us?"

            scene nightlewd69

            a4 "Ugn. Where...?"

            scene nightlewd70 with dissolve

            a4 "What happened? I feel so weak right now."

            l2 "You orgasmed so hard that you passed out. Are you alright?"

            scene nightlewd71 with dissolve

            a4 "I... passed out?"
            a4 "I do that sometimes when my orgasms are really intense but
            it doesn't happen very often."
            a4 "I didn't scare you, did I?"

            scene nightlewd72

            b2 "Your entire orgasm scared the shit out of me. You turned into
            something else there at the end."
            b2 "Like a werewolf or something. There was a complete transformation."
            b2 "You and Leah are going to have a lot of fun together, I can already tell."

            scene nightlewd68

            l2 "But for now, let's go get you cleaned up and then we'll hop into
            bed so you can rest after your extreme climax."

            a4 "That sounds good. Except I might need some help walking. I can't
            feel my legs..."

            l2 "Hehe. Come on, my little Wolfgirl. Let's get you to the bathroom."

            scene black with dissolve

            "Avalon and Leah took a few minutes to clean up before crawling into
            bed with their mutual lover, [player_name]."

            scene nightlewd74 with fade

            "Avalon's eyes fell as soon as her head hit the pillow. She was exhausted
            from a day of sexual exploration and couldn't wait for more."
            "Leah looked on at her new girlfriend with both love and lust. She
            was excited to bring Avalon into both her life and her sexual adventures."
            "[player_name] was asleep by the time they came back. But he certainly
            was excited too. An excitement he would show tomorrow, after much needed rest."

            scene nightlewd73 with dissolve

            a4 "I want to go with you, Leah."

            l2 "What was that, Avalon?"

            a4 "Your business trip. You said there are always more options
            than the ones presented."
            a4 "I want to go with you."

            scene nightlewd75

            "Leah pondered on the idea for a moment. An entire year away on a business
            retreat with her two lovers was an intriguing idea."
            "Henry seemed desperate enough to have Leah on the project. Perhaps
            a third person wouldn't be out of the question?"

            l2 "Okay. Yeah. Let's do it, Avalon. Let's all go together."

            scene nightlewd73

            a4 "You brought Uncle [player_name] back to me and saved me from
            that awful man."
            a4 "And now you're going to make something that saves millions of lives."
            a4 "You're my hero, Leah. Thank you."

            scene nightlewd75

            "Avalon's words caught Leah off guard. She never thought of herself as
            heroic."
            "But it felt good to hear. She enjoyed teaching Avalon, taking care of her
            and providing for her."
            "She couldn't help but look forward to being a mentor for her, excited
            to show her all the things she had learned over the years."
            "And Leah vowed to herself to keep Avalon safe from the evils of the
            world as best she could."

            l2 "You're welcome, my Avalon."

            stop music fadeout 2.0

            scene nightlewd76 with dissolve

            "Leah fell asleep dreaming of the possibilities her future might hold."

            jump epilogue

        else:

            scene 1nightani01 with dissolve

            b2 "Shh! Not so loud. You'll wake up my niece!"

            l2 "I can't help it. It's lighting up my brain with pleasure, [player_name]!"

            b2 "Let's switch positions then to point you away from her room at least."

            scene nightwholesome30 with dissolve

            b2 "Here, grab my hand."

            l2 "What position did you have in mind, Bear?"

            scene nightwholesome32

            l2 "Woah! You're going to hold me up and fuck me like this? You're so strong,
            [player_name]! This is going to be incredible."

            b2 "I'm not sure how well it's going to work but I so badly want to drop
            you down on my dick over and over again."

            l2 "Let's try it!"

            scene nightwholesome34 with dissolve

            "[player_name] lifted Leah up slightly and his dick fell right into place,
            penetrating her soft, wet hole."

            l2 "Nyeah! I feel your tip inside me. Go all the way, Bear. Penetrate
            deep inside me, [persistent.byron_rel]."

            b2 "You're wish is my command, [persistent.leah_rel]. Here we go!"

            show 2night_ani with dissolve

            l2 "Nya! You're pressing against my walls so hard, [player_name]! I'm
            going to burst!"

            "[player_name] grunted eagerly as he bounced Leah up and down on his
            erection. She squeeled with pleasure with every fall."

            l2 "Wonderful! Wonderful! More, [player_name]!"

            b2 "My legs are getting weak. I can't tell if it's from exhaustion or
            pleasure overload!"

            b2 "Your pussy is grabbing hold of my cock like a vice grip! I can
            feel myself bending everytime I go back into you."

            l2 "Then put me down and fuck me from behind. You can get so much deeper
            that way!"

            scene nightwholesome37 with vpunch

            l2 "Oof!"

            "[player_name] dropped Leah down onto the bed."

            scene nightwholesome38 with dissolve

            l2 "Throwing me around now, are you? Am I your rag doll, [player_name]?"
            l2 "Say it to me, [persistent.byron_rel]. Call me your little fuck toy!
            Make me your play thing!"

            b2 "My little fuck toy needs to get her ass in the air so I can finish off
            that naughty little pussy."

            l2 "Ooh, yes, sir!"

            scene nightwholesome39 with dissolve

            l2 "Is this want you want, my love? Do you want to mount me and dominate me
            like you own me?"
            l2 "Claim me, [player_name]. Make me yours by fucking me into submission!"

            b2 "It's my duty as your big [persistent.byron_rel] to take care of you,
            isn't it? Do you want your [persistent.byron_rel] to make you cum, Leah?"

            l2 "Yes! Ohh, fuck, that's so hot. Yes! Fuck your [persistent.leah_rel]
            until she orgasms! Punish me for eating your candy bar!"

            b2 "You ate my candy bar!?"

            l2 "Nevermind, just fuck me, [player_name]!"

            scene nightwholesome40

            b2 "This ass is almost too nice to defile, Leah. My dick fits snugly right
            between your cheeks. I want to keep it here forever!"

            b2 "There should be an award for an ass like this. Gold star!"
            b2 "And this hourglass figure you have makes getting ahold of you so
            easy. I can pull you into me with perfect grip."

            l2 "Do it, do it! You drive me crazy when you pause like this. Just take
            me, [player_name]!"

            b2 "I enjoy watching you squirm and hearing you beg."

            l2 "You shouldn't be so mean to your little [persistent.leah_rel], [player_name]!
            You should be a good big [persistent.byron_rel] and give her what she wants!"

            scene 3nightani01 with dissolve

            l2 "O-oh, is that the tip? I can feel you parting my lips. I want more,
            [player_name]. I want all of you inside me!"

            b2 "Ask nicely."

            l2 "Please! Please fuck my pussy until you're finished with me! Fuck me
            until you're satisfied! I beg you!"

            show 3night_ani with dissolve

            "[player_name] pulled Leah's rear firmly back until her butt slammed into
            his hips, thrusting his dick deep inside her."
            "Sound erupted from the collision, slapping rythmically with every pounding."

            b2 "Ugn! I am burying this cock so deep inside you, Leah, we might never
            get it out!"

            l2 "Pierce me! Impale me! Ruin me, [player_name]! Oh fuck, yes!"

            l2 "There's so much friction, my pussy is on fire! You ignite me, [player_name]!"

            b2 "I'm about to finish, Leah. Are you ready for my cum?"

            l2 "No, [player_name], don't! I want to taste it! I want it in my mouth!"

            b2 "Then turn around and come get your reward, Leah."

            scene nightwholesome41

            "Leah whipped around and hungrily wrapped her fingers around [player_name]'s
            cock, squeezing tightly as if she'd just caught her prey."

            b2 "Beg me for, Leah. Ask me for my cum."

            l2 "Please spill your seed inside my mouth, big [persistent.byron_rel].
            I want it so bad!"

            scene nightwholesome43

            b2 "Don't let any escape. I want you to drink it all!"

            "Leah moaned with delight as she gave [player_name]'s throbbing cock
            one more aggressive squeeze."

            show drinkme with dissolve

            "[player_name]'s cock erupted with ejaculate, firing cum into his
            [persistent.leah_rel]'s mouth so far it slammed into the back of her throat."

            b2 "Oh fuck, squeeze harder! Don't stop drinking it, Leah!"

            "Leah let out another thirsty moan as she gobbled up as much semen as he
            would provide for her."

            "She gulped down every squirt as soon as she could taste it in her mouth."

            show drinkitall with dissolve

            "As soon as the stream stopped, Leah wrapped her lips around the head of his
            dick to savor that last bit she could coax out of him."
            "Leah whimpered as if to beg for more as she sucked hard on the tip of his cock,
            desperately pulling out every last drop from [player_name]."

            b2 "Oh shit, that's... that's all I've got. That was fucking incredible.
            I gotta lay down before I fall down."

            $ renpy.end_replay()
            if persistent.bonusnightwholesome == False:
                $ renpy.notify("You've unlocked Bonus Night (Wholesome Path) in the gallery!")
                $ persistent.bonusnightwholesome = True

            scene black with dissolve

            "[player_name] and Leah crawled up on the bed together, exhausted from
            their intense sexual romp."

            scene nightwholesome48 with dissolve

            b2 "Leah, these sessions are getting so intense. I can't believe the shit
            we say to each other when we're having sex."

            l2 "It'll take more getting used to for you but you're getting much better at it."

            scene nightwholesome49 with dissolve

            l2 "Let's stay, [player_name]."

            b2 "What? Stay where?"

            l2 "Here. Let's tell Henry that we can't go on that trip. Let's build our
            relationship and take care of Avalon. I want to stay."

            b2 "Okay, yeah. We'll tell him it's just not the right time."

            "[player_name] didn't hate the idea of going on the trip but the idea
            of leaving Avalon after finally reunited would be unbearable."
            "He was going to refuse to go tomorrow but hearing Leah beat him
            to the punch made him fall even more in love with her."
            "They wanted the same things more than either of them knew."

            stop music fadeout 2.0

            b2 "Good night, my beautiful flame."

            l2 "Good night, Teddy Bear."

            $ renpy.end_replay()

            jump epilogue

        label epilogue:

            play music "audio/touching_moment.mp3"

            scene myrabg
            show myrabelle serious
            with fade

            m "As you can see, our story could have been quite different with just
            a small nudge to one of our characters."
            m "We hope you enjoyed this glimpse at another world and that you
            find some solace in experiencing it as it had much less drama."
            m "We wanted to show you this alternative reality as a gift to you, our fans,
            for supporting us and helping us grow."
            m "Lockheart and I looked a bit further and saw a few more interesting
            things happen."

            scene meetmorton with fade

            m "[player_name] took Avalon to Morton's shop to have her ring sized
            appropriately for her thumb."
            m "It also gave him the opportunity to introduce Avalon to the man
            who crafted her ring thirteen years ago."
            m "They spent an afternoon catching up with Morton and decided to stay
            in touch after."

            scene arrested with fade

            m "And yes, Penny was able to scrape up enough evidence to present to
            the police force to have Tyler arrested."
            m "In this timeline, however, Faith didn't have the support of Merc
            and Lance after her father was taken from her."

            scene babysitter with fade

            m "Sharol had a new friend thrust upon her. Sun Mei started stopping
            by several times a week to take care of her."
            m "Sun Mei eventually convinced Sharol to start therapy sessions with
            Dr. Yu where she did start to regain some control of her life."
            m "Randall would eventually bump into her at a local convenience store
            and ask her on a date several months later."

            scene myrabg
            show myrabelle explain
            with fade

            m "The multiverse of story-telling is a tricky beast. It may not
            be healthy to dwell on 'What if..?' scenarios."
            m "But this was a difficult story to tell and I'm sure a challenging read
            at some parts so we wanted to reward you with this happier alternate timeline."

            show myrabelle goodbye
            with dissolve

            m "Thank you for taking the time to read our novel and we genuinely
            hope your enjoyed Avalon."
            m "May you experience your best timeline."
            m "Farewell for now."





    return
