Summary
----------------
Welcome to isometric. To install this python isometric 2d engine, you will need python, and pygame installed. This project is cross platform compatible, for Windows 7 (tested), Linux, and Mac OS X (Yosemite tested).

For reading about good programming guidelines, see:
https://www.pygame.org/docs/tut/tom/MakeGames.html
http://pythonprogramming.net/pygame-start-menu-tutorial/

Installation
-----------------

Windows:
---------

Step 1:
You can download Python at the official site here:
https://www.python.org/downloads/windows/

Download and install version 2.7.x or 3.x.

Step 2:
Download pygame from here:
http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame

Once downloaded, open up a command prompt and install with pip, giving your custom path to the wh1 file below:
```ssh
py -m pip install C:/Path/to/pygame-1.9.2a0-cp34-none-win_amd64.whl
```

Step 3:
Run app.py with PyCharm or from the command line.


Mac:
----------
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


Ubuntu (14):
----------
Step 1:
Install all Pygame deps for Linux with yum / apt-get

```ssh
    sudo apt-get install python3 mercurial python3-pip libfreetype6-dev 
    sudo apt-get build-dep ptyhon-pygame
```

Step 2:
Install PyGame
```ssh
    sudo pip3 install hg+http://bitbucket.org/pygame/pygame
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


RoadMap
---------

~~Random Map~~

~~Health Bar~~

Load/Save Game

Inventory Menu

Inventory

Animated Character Sprite (walking, standing, attack)

Animated Enemy Sprite

Inventory Hot Bar

Tile placement function

Light Shadows

Decent BG Music

SFX Package

Draw Distance Detection and Rendering
