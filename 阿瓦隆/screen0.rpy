## This is the screen to choose which Mono Scene you'd like to see ##

label monopath0:

    call screen monoscenes

screen monoscenes():
    tag menu
    add gui.game_menu_background

    imagebutton:
        action Jump("opnight0")
        idle "extras/images/ninjaoctavia.png" at animatedZoom(0.8, 0.85)
        pos (100, 175)

    imagebutton:
        action Jump("stowaway0")
        idle "extras/images/militaryoctavia.png" at animatedZoom(0.8, 0.85)
        pos (570, 175)

    imagebutton:
        action Jump("pdnight0")
        idle "extras/images/darkwhisper.png" at animatedZoom(0.8, 0.85)
        pos (1000, 175)

    imagebutton:
        action Jump("senet0")
        idle "extras/images/egyptiandallas.png" at animatedZoom(0.8, 0.85)
        pos (1400, 175)

    imagebutton:
        action MainMenu(confirm=False)
        idle "extras/images/button.png"
        hover Transform(im.MatrixColor("extras/images/button.png", im.matrix.brightness(0.2)))
        pos(1684, 50)
    text "Back":
        style "buttonText"
        pos(1722, 61)

    imagebutton:
        action Jump("monohelp")
        idle "extras/images/questionmark.png" at animatedZoom(0.6, 0.75)
        pos (20, 20)


## Did this instead of an actual game menu, it's far less annoying to code, and I think it's greatly improved with Xianne - G3n.Zero
default code_input = ""
label unlockMenu:
    stop music fadeout 1.0

    scene 9xianne5 with fade

    play music "audio/something_good.mp3"

    x "Do you know the super secret code?"
    menu:
        "Of course!":
            $ code_input = renpy.input("Enter Unlock Code")
            if code_input == "megalodong":
                x "Oooh. I guess you're in the know! Thanks for supporting."

                $ persistent.monoUnlock = True
                $ persistent.actTwo = True
                $ persistent.actThree = True
                $ persistent.actFour = True
                $ persistent.actFive = True
                $ persistent.actSix = True
                $ persistent.actSeven = True
                $ persistent.whatif = True
                $ persistent.showme = True

                $ persistent.experimentation = True
                $ persistent.bunnygirl = True
                $ persistent.playhard = True
                $ persistent.lovefordallas = True
                $ persistent.closeyoureyes = True
                $ persistent.ninjina = True
                $ persistent.darkwhisper = True

                $ persistent.medusaboobs = True
                $ persistent.nakedman = True
                $ persistent.actitout = True
                $ persistent.goodvibrations = True
                $ persistent.likeitrough = True
                $ persistent.considerablegirth = True
                $ persistent.mre = True
                $ persistent.bunked = True

                $ persistent.pastthepanic = True
                $ persistent.meetthepussy = True
                $ persistent.rodehard = True
                $ persistent.alltheway = True
                $ persistent.twowet = True
                $ persistent.cosplay = True

                $ persistent.limitedtime = True
                $ persistent.lewdlingerie = True
                $ persistent.bonusnightlewd = True
                $ persistent.bonusnightwholesome = True

                x "All content is now unlocked! Have fun out there, Tiger."
                return
            elif code_input <> "megalodong":
                scene 10xianne5 with dissolve
                x "Go figure out the code and come back."
                x "The Megalodong is real!"
                return

        "What code?":
            scene 8xianne5 with dissolve
            x "Oh, you don't know it?"
            x "There's a lot of sexy stuff you're going to miss out on."
            x "Come back if you figure it out."
            x "The Megalodong is real!"
            return

        "Can you unlock the gallery?":
            scene 10xianne5 with dissolve
            x "That's an odd request. But alright, I'll unlock it up for you."

            $ persistent.galleryUnlock = True
            $ persistent.monoUnlock = True
            $ persistent.actTwo = True
            $ persistent.actThree = True
            $ persistent.actFour = True
            $ persistent.actFive = True
            $ persistent.actSix = True
            $ persistent.actSeven = True
            $ persistent.whatif = True

            $ persistent.showme = True
            $ persistent.experimentation = True
            $ persistent.bunnygirl = True
            $ persistent.playhard = True
            $ persistent.lovefordallas = True
            $ persistent.closeyoureyes = True
            $ persistent.ninjina = True
            $ persistent.darkwhisper = True

            $ persistent.medusaboobs = True
            $ persistent.nakedman = True
            $ persistent.actitout = True
            $ persistent.goodvibrations = True
            $ persistent.likeitrough = True
            $ persistent.considerablegirth = True
            $ persistent.mre = True
            $ persistent.bunked = True

            $ persistent.pastthepanic = True
            $ persistent.meetthepussy = True
            $ persistent.rodehard = True
            $ persistent.alltheway = True
            $ persistent.twowet = True
            $ persistent.cosplay = True

            $ persistent.limitedtime = True
            $ persistent.lewdlingerie = True
            $ persistent.bonusnightlewd = True
            $ persistent.bonusnightwholesome = True

            x "Have fun."
            return
