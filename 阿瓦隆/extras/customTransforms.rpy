transform animatedZoom(zoomIdle, zoomHover):
    on idle:
        zoom zoomIdle
    on hover:
        linear 0.1 zoom zoomHover
