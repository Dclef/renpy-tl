label sceneMenu1:

    call screen sceneMenu1

screen sceneMenu1():
    tag menu
    add "gui/main_menu.png"

    text "画廊 - 第一页":
        style "header"
        font "georgia.ttf"
        size 110
        kerning 4
        outlines [ ( 3.5, "#000000", 3, 1) ]
        pos(400, 102)

    imagebutton:
        action MainMenu(confirm=False)
        idle "extras/images/button.png"
        hover Transform(im.MatrixColor("extras/images/button.png", im.matrix.brightness(0.2)))
        pos(1684, 50)
    text "退出":
        style "buttonText"
        pos(1725, 61)

    imagebutton:
        action Show("sceneMenu2"), Hide("sceneMenu1")
        idle "extras/images/button.png"
        hover Transform(im.MatrixColor("extras/images/button.png", im.matrix.brightness(0.2)))
        pos(1684, 145)
    text "下一页":
        style "buttonText"
        pos(1705, 155)

    vpgrid:
        anchor (-117, -364)
        rows 2
        cols 4
        xspacing 50
        yspacing 100

    text "演示给你看":
        style "galleryText"
        pos(195, 586)

    text "做实验":
        style "galleryText"
        pos(660, 586)

    text "兔女郎":
        style "galleryText"
        pos(1100, 586)

    text "玩得开心":
        style "galleryText"
        pos(1505, 586)

    text "达拉斯的爱":
        style "galleryText"
        pos(165, 902)

    text "闭上你的双眼":
        style "galleryText"
        pos(585, 902)

    text "忍者":
        style "galleryText"
        pos(1125, 902)

    text "黑暗低语":
        style "galleryText"
        pos(1505, 902)


    ## Show Me
    if persistent.showme:
        imagebutton:
            action Replay("toy_play", locked=False)
            idle Transform("images/actthree/thegift/19thegift.webp", zoom=0.2)
            hover Transform("images/actthree/thegift/19thegift.webp", zoom=0.21)
            pos (118, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (118, 365)

    ## Experimentation
    if persistent.experimentation:
        imagebutton:
            action Replay("polygamy3", locked=False)
            idle Transform("images/actthree/aroomdal/16aroomdal.webp", zoom=0.2)
            hover Transform("images/actthree/aroomdal/16aroomdal.webp", zoom=0.21)
            pos (551, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (551, 365)


    ## Bunny Girl
    if persistent.bunnygirl:
        imagebutton:
            action Replay("night_three", locked=False)
            idle Transform("images/actthree/nightthree/6nightthree.webp", zoom=0.2)
            hover Transform("images/actthree/nightthree/6nightthree.webp", zoom=0.21)
            pos (985, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (985, 365)


    ## Play Hard
    if persistent.playhard:
        imagebutton:
            action Replay("galleryScene1", locked=False)
            idle Transform("images/actfour/40wakeup4.webp", zoom=0.2)
            hover Transform("images/actfour/40wakeup4.webp", zoom=0.21)
            pos (1420, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (1420, 365)


    ## Love for Dallas
    if persistent.lovefordallas:
        imagebutton:
            action Replay("dallashouse_poly", locked=False)
            idle Transform("images/actfour/34dallashouse.webp", zoom=0.2)
            hover Transform("images/actfour/34dallashouse.webp", zoom=0.21)
            pos (118, 680)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (118, 680)


    ## Close Your Eyes
    if persistent.closeyoureyes:
        imagebutton:
            action Replay("octavia_poly_hair", locked=False)
            idle Transform("images/actfour/2octaviaplay.webp", zoom=0.2)
            hover Transform("images/actfour/2octaviaplay.webp", zoom=0.21)
            pos (551, 680)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (551, 680)


    ## Ninjina
    if persistent.ninjina:
        imagebutton:
            action Replay("galleryScene3", locked=False)
            idle Transform("images/actfive/opnight/37opnight.webp", zoom=0.2)
            hover Transform("images/actfive/opnight/37opnight.webp", zoom=0.21)
            pos (985, 680)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (985, 680)


    ## Dark Whisper
    if persistent.darkwhisper:
        imagebutton:
            action Replay("galleryScene4", locked=False)
            idle Transform("images/actfive/pdnight/12pdnight.webp", zoom=0.2)
            hover Transform("images/actfive/pdnight/12pdnight.webp", zoom=0.21)
            pos (1420, 680)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (1420, 680)

    ## Screen 2 ##

screen sceneMenu2():
    tag menu
    modal True
    add "#23272a"
    add "gui/main_menu.png"

    text "画廊 - 第二页":
        style "header"
        font "georgia.ttf"
        size 110
        kerning 4
        outlines [ ( 3.5, "#000000", 3, 1) ]
        pos(400, 102)

    imagebutton:
        action Show("sceneMenu1"), Hide("sceneMenu2")
        idle "extras/images/button.png"
        hover Transform(im.MatrixColor("extras/images/button.png", im.matrix.brightness(0.2)))
        pos(1684, 50)
    text "Back":
        style "buttonText"
        pos(1722, 61)

    imagebutton:
        action Show("sceneMenu3"), Hide("sceneMenu2")
        idle "extras/images/button.png"
        hover Transform(im.MatrixColor("extras/images/button.png", im.matrix.brightness(0.2)))
        pos(1684, 145)
    text "Next":
        style "buttonText"
        pos(1705, 155)


    text "美杜莎的乳房":
        style "galleryText"
        pos(145, 586)

    text "全裸":
        style "galleryText"
        pos(675, 586)

    text "演戏":
        style "galleryText"
        pos(1115, 586)

    text "良好的振动":
        style "galleryText"
        pos(1465, 586)

    text "喜欢粗暴点":
        style "galleryText"
        pos(165, 902)

    text "相当大的长度":
        style "galleryText"
        pos(575, 902)

    text "军粮":
        style "galleryText"
        pos(1115, 902)

    text "树屋":
        style "galleryText"
        pos(1545, 902)


    ## Medusa Boobs
    if persistent.medusaboobs:
        imagebutton:
            action Replay("galleryScene2", locked=False)
            idle Transform("images/actfour/61nightfour.webp", zoom=0.2)
            hover Transform("images/actfour/61nightfour.webp", zoom=0.21)
            pos (118, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (118, 365)

    ## Naked Man
    if persistent.nakedman:
        imagebutton:
            action Replay("adactout", locked=False)
            idle Transform("images/actsix/adactout/23adactout.webp", zoom=0.2)
            hover Transform("images/actsix/adactout/23adactout.webp", zoom=0.21)
            pos (551, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (551, 365)


    ## Act It Out
    if persistent.actitout:
        imagebutton:
            action Replay("aoactout", locked=False)
            idle Transform("images/actsix/aoactout/14aoactout.webp", zoom=0.2)
            hover Transform("images/actsix/aoactout/14aoactout.webp", zoom=0.21)
            pos (985, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (985, 365)


    ## Good Vibrations
    if persistent.goodvibrations:
        imagebutton:
            action Replay("avasolosix", locked=False)
            idle Transform("images/actsix/avasolosix/8avasolosix_vibe.webp", zoom=0.2)
            hover Transform("images/actsix/avasolosix/8avasolosix_vibe.webp", zoom=0.21)
            pos (1420, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (1420, 365)


    ## Like it Rough
    if persistent.likeitrough:
        imagebutton:
            action Replay("dallas_sex", locked=False)
            idle Transform("images/actfive/dbpostdate/7dbpostdate.webp", zoom=0.2)
            hover Transform("images/actfive/dbpostdate/7dbpostdate.webp", zoom=0.21)
            pos (118, 680)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (118, 680)


    ## Considerable Girth
    if persistent.considerablegirth:
        imagebutton:
            action Replay("octavia_sex", locked=False)
            idle Transform("images/actfive/obpostdate/24obpostdate.webp", zoom=0.2)
            hover Transform("images/actfive/obpostdate/24obpostdate.webp", zoom=0.21)
            pos (551, 680)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (551, 680)


    ## MRE
    if persistent.mre:
        imagebutton:
            action Replay("mre", locked=False)
            idle Transform("images/actseven/stowaway/stowsex/stowsex06.webp", zoom=0.2)
            hover Transform("images/actseven/stowaway/stowsex/stowsex06.webp", zoom=0.21)
            pos (985, 680)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (985, 680)


    ## Bunked
    if persistent.bunked:
        imagebutton:
            action Replay("bunked", locked=False)
            idle Transform("images/actseven/senet/43senet.webp", zoom=0.2)
            hover Transform("images/actseven/senet/43senet.webp", zoom=0.21)
            pos (1420, 680)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (1420, 680)

screen sceneMenu3():
    tag menu
    modal True
    add "#23272a"
    add "gui/main_menu.png"

    text "画廊 - 第三页":
        style "header"
        font "georgia.ttf"
        size 110
        kerning 4
        outlines [ ( 3.5, "#000000", 3, 1) ]
        pos(400, 102)

    imagebutton:
        action Show("sceneMenu2"), Hide("sceneMenu3")
        idle "extras/images/button.png"
        hover Transform(im.MatrixColor("extras/images/button.png", im.matrix.brightness(0.2)))
        pos(1684, 50)
    text "Back":
        style "buttonText"
        pos(1722, 61)

    imagebutton:
        action Show("sceneMenu4"), Hide("sceneMenu3")
        idle "extras/images/button.png"
        hover Transform(im.MatrixColor("extras/images/button.png", im.matrix.brightness(0.2)))
        pos(1684, 145)
    text "Next":
        style "buttonText"
        pos(1705, 155)

    text "走出恐慌":
        style "galleryText"
        pos(205, 586)

    text "和猫咪见面":
        style "galleryText"
        pos(595, 586)

    text "健身房骑马":
        style "galleryText"
        pos(1045, 586)

    text "一路同行":
        style "galleryText"
        pos(1495, 586)

    text "两个湿漉漉":
        style "galleryText"
        pos(615, 902)

    text "角色扮演":
        style "galleryText"
        pos(1070, 902)



    ## Past the Panic
    if persistent.pastthepanic:
        imagebutton:
            action Replay("nightsix", locked=False)
            idle Transform("images/actsix/nightsix/57nightsix.webp", zoom=0.2)
            hover Transform("images/actsix/nightsix/57nightsix.webp", zoom=0.21)
            pos (118, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (118, 365)

    ## Meet the Pussy
    if persistent.meetthepussy:
        imagebutton:
            action Replay("postcube_octavia", locked=False)
            idle Transform("images/actseven/octpostcube/16octpostcube.webp", zoom=0.2)
            hover Transform("images/actseven/octpostcube/16octpostcube.webp", zoom=0.21)
            pos (551, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (551, 365)


    ## Rode Hard
    if persistent.rodehard:
        imagebutton:
            action Replay("postcube_dallas", locked=False)
            idle Transform("images/actseven/dalpostcube/24dalpostcube.webp", zoom=0.2)
            hover Transform("images/actseven/dalpostcube/24dalpostcube.webp", zoom=0.21)
            pos (985, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (985, 365)


    ## All the Way
    if persistent.alltheway:
        imagebutton:
            action Replay("all_the_way", locked=False)
            idle Transform("images/actseven/nseven/38nseven.webp", zoom=0.2)
            hover Transform("images/actseven/nseven/38nseven.webp", zoom=0.21)
            pos (1420, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (1420, 365)


    ## Two Wet
    if persistent.twowet:
        imagebutton:
            action Replay("octpolyreplay", locked=False)
            idle Transform("images/actseven/nseven/octbeach/octpoly/octpoly02.webp", zoom=0.2)
            hover Transform("images/actseven/nseven/octbeach/octpoly/octpoly02.webp", zoom=0.21)
            pos (551, 680)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (551, 680)


    ## Cosplay
    if persistent.cosplay:
        imagebutton:
            action Replay("dalpolyreplay", locked=False)
            idle Transform("images/actseven/dalbeach/dalpoly/dalpoly01.webp", zoom=0.2)
            hover Transform("images/actseven/dalbeach/dalpoly/dalpoly01.webp", zoom=0.21)
            pos (985, 680)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (985, 680)

screen sceneMenu4():
    tag menu
    modal True
    add "#23272a"
    add "gui/main_menu.png"

    text "额外奖励 - 画廊":
        style "header"
        font "georgia.ttf"
        size 150
        kerning 4
        outlines [ ( 3.5, "#000000", 3, 1) ]
        pos(300, 102)

    imagebutton:
        action Show("sceneMenu3"), Hide("sceneMenu4")
        idle "extras/images/button.png"
        hover Transform(im.MatrixColor("extras/images/button.png", im.matrix.brightness(0.2)))
        pos(1684, 50)
    text "Back":
        style "buttonText"
        pos(1722, 61)

    text "有限时间内":
        style "galleryText"
        pos(350, 675)

    text "淫荡的内衣":
        style "galleryText"
        pos(830, 675)

    text "奖励之夜":
        style "galleryText"
        pos(1320, 675)

    ## Deep Throated
    if persistent.limitedtime:
        imagebutton:
            action Replay("limitedtime", locked=False)
            idle Transform("images/whatif/limitedtime/limitedtime15.webp", zoom=0.2)
            hover Transform("images/whatif/limitedtime/limitedtime15.webp", zoom=0.21)
            pos (300, 450)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (300, 450)

    ## Lewd Lingerie
    if persistent.lewdlingerie:
        imagebutton:
            action Replay("lewdlingerie", locked=False)
            idle Transform("images/whatif/lewdlingerie/lewdlingerie027.webp", zoom=0.2)
            hover Transform("images/whatif/lewdlingerie/lewdlingerie027.webp", zoom=0.21)
            pos (775, 450)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (775, 450)

    ## Bonus Act Night Scene
    if persistent.bonusnightlewd or persistent.bonusnightwholesome:
        imagebutton:
            action Replay("nightb", locked=False)
            idle Transform("images/whatif/nightlewd/nightlewd05.webp", zoom=0.2)
            hover Transform("images/whatif/nightlewd/nightlewd05.webp", zoom=0.21)
            pos (1250, 450)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (1250, 450)
