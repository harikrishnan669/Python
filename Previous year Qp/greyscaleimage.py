def grey_scale(image):
    for y in range(image.get_height()):
        for x in range(image.get_width()):
            (r,g,b)=image.getPixel(x,y)
            r=int(r*0.299)
            g=int(g*0.587)
            b=int(b*0.114)
            lum=r+g+b
            image.setPixel(x,y,(lum,lum,lum))
