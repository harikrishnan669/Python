def black_white(image):
    blackPixel=(0,0,0)
    whitePixel=(255,255,255)
    for y in range(image.get_height()):
        for x in range(image.get_width()):
            (r,g,b)=image.getPixel(x,y)
            average=(r+g+b)//3
            if average< 128:
                image.setPixel(x,y,blackPixel)
            else:
                image.setPiexel(x,y,whitePixel)
