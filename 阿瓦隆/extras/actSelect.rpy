
label actMenu1:

    call screen actMenu1

screen actMenu1():
    tag menu
    add "gui/main_menu.png"

    text "选择章节":
        style "header"
        font "georgia.ttf"
        size 110
        kerning 2
        outlines [ ( 3.5, "#000000", 3, 1) ]
        pos(635, 102)

    imagebutton:
        action MainMenu(confirm=False)
        idle "extras/images/button.png"
        hover Transform(im.MatrixColor("extras/images/button.png", im.matrix.brightness(0.2)))
        pos(1684, 50)
    text "退出":
        style "buttonText"
        pos(1730, 61)

    vpgrid:
        anchor (-117, -364)
        rows 2
        cols 4
        xspacing 50
        yspacing 100

    text "第一章节":
        style "galleryText"
        pos(215, 586)

    text "第二章节":
        style "galleryText"
        pos(645, 586)

    text "第三章节":
        style "galleryText"
        pos(1085, 586)

    text "第四章节":
        style "galleryText"
        pos(1515, 586)

    text "第五章节":
        style "galleryText"
        pos(215, 902)

    text "第六章节":
        style "galleryText"
        pos(645, 902)

    text "第七章节":
        style "galleryText"
        pos(1085, 902)

    text "如果..会怎样？":
        style "galleryText"
        pos(1465, 902)


    ## Act One
    if persistent.actOne:
        imagebutton:
            action Jump("start")
            idle Transform("images/Avalonactone.png", zoom=0.2)
            hover Transform("images/Avalonactone.png", zoom=0.21)
            pos (118, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (118, 365)

    ## Act Two
    if persistent.actTwo:
        imagebutton:
            action Jump("act_two")
            idle Transform("images/Avalonacttwo.png", zoom=0.2)
            hover Transform("images/Avalonacttwo.png", zoom=0.21)
            pos (551, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (551, 365)


    ## Act Three
    if persistent.actThree:
        imagebutton:
            action Jump("act_three")
            idle Transform("images/AvalonactThree.png", zoom=0.2)
            hover Transform("images/AvalonactThree.png", zoom=0.21)
            pos (985, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (985, 365)


    ## Act Four
    if persistent.actFour:
        imagebutton:
            action Jump("act_four")
            idle Transform("images/Avalonactfour.png", zoom=0.2)
            hover Transform("images/Avalonactfour.png", zoom=0.21)
            pos (1420, 365)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (1420, 365)


    ## Act Five
    if persistent.actFive:
        imagebutton:
            action Jump("act_five")
            idle Transform("images/Avalonactfive.png", zoom=0.2)
            hover Transform("images/Avalonactfive.png", zoom=0.21)
            pos (118, 680)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (118, 680)


    ## Act Six
    if persistent.actSix:
        imagebutton:
            action Jump("act_six")
            idle Transform("images/Avalonactsix.png", zoom=0.2)
            hover Transform("images/Avalonactsix.png", zoom=0.21)
            pos (551, 680)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (551, 680)


    ## Act Seven
    if persistent.actSeven:
        imagebutton:
            action Jump("act_seven")
            idle Transform("images/Avalonactseven.png", zoom=0.2)
            hover Transform("images/Avalonactseven.png", zoom=0.21)
            pos (985, 680)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (985, 680)


    ## What If..?
    if persistent.whatif:
        imagebutton:
            action Jump("whatif")
            idle Transform("extras/images/earth.webp", zoom=0.2)
            hover Transform("extras/images/earth.webp", zoom=0.21)
            pos (1420, 680)
    else:
        imagebutton:
            idle Transform("extras/images/locked.png", zoom=0.2)
            pos (1420, 680)
