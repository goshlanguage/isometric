Welcome to isometric. To install this python isometric 2d engine, you will need python, and pygame installed. This project is cross platform compatible, for Windows 7 (tested), Linux, and Mac OS X (Yosemite tested).

For reading about good programming guidelines, see:
https://www.pygame.org/docs/tut/tom/MakeGames.html

Mac:
Step 1:
Install all Pygame deps for Mac with Brew (if you don't have brew, look up how to install first)

```ssh
    brew install python3 hg sdl sdl_image sdl_ttf portmidi smpeg 
```

Step 2:
Install PyGame
```ssh
    pip3 install hg+http://bitbucket.org/pygame/pygame
```

Step 3:
Download sdl-mixer source code from: https://www.libsdl.org/projects/SDL_mixer/release-1.2.html

Untar the tar.gz file with tar zxvf:
```ssh
    tar zxvf SDL_mixer-1.2.12.tar.gz
    cd SDL_mixer-1.2.12
    ./configure
    make
    sudo make install
```

Step 4:
Run app.py and see if everything works!
```ssh
python app.py
```



