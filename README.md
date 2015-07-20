I had the same issue, thanks the Cynikal's post I was finally able to resolve this. You can ignore step2 if you have already installed pygame. Also change pip3 to pip and remove python3 from the brew install list if you plan to use python27 or something

Step 1:
Install all Pygame deps for Mac with Brew (if you don't have brew, look up how to install first)

    brew install python3 hg sdl sdl_image sdl_ttf portmidi smpeg 

Step 2:
Install PyGame

    pip3 install hg+http://bitbucket.org/pygame/pygame

Step 3:
Download sdl-mixer source code from: https://www.libsdl.org/projects/SDL_mixer/release-1.2.html

Untar the tar.gz file with tar zxvf:

    tar zxvf SDL_mixer-1.2.12.tar.gz
    cd SDL_mixer-1.2.12
    ./configure
    make
    sudo make install

Step 4:
Run your pygame code and see if it fixes your dependency issue


I hope this helps others who come to this with the same issue I had on OS X Yosemite

