#Life
This is an implementation of Conway's Game of Life: http://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

The application runs in the terminal and is configurable by the user (see below for instructions).


# Installation on OS X

##Install Homebrew:
- ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

##Install Python2.7:
This is necessary purely to run the Fabric tool as it has not been ported to Python3 yet!

- brew install python2.7

## Install Fabric:
- pip-2.7 install fabric

##Install Pythonbrew:
- sudo easy_install pythonbrew 
- pythonbrew_install
- add this to your shell profile (.bashrc, .zshrc): source ~/.pythonbrew/etc/bashrc

Instructions from: http://www.howopensource.com/2011/05/how-to-install-and-manage-different-versions-of-python-in-linux/
						
##Build the Life project:
- fab install


# Running Life

## Command Usage

### Help
- fab run:args="--help"

### Example
- fab run:args="100 30 100 0.1"


# Configuring Life
Run-time configuration is made using the command-line arguments.

Edit the settings.py file to change the starting configuration of cells. Examples are in that file as comments.