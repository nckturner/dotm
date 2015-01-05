dotfiles
========

This is my dotfiles management suite.  It is simple and opinionated when it can be, and customizable when it must be.  

Enjoy.


Getting Started
---------------

Clone dotfiles into ~/.dotfiles:
```
git clone https://github.com/rask0l/dotfiles.git ~/.dotfiles && ~/.dotfiles/bin/bootstrap
```

Adding dotfiles
---------------

Feel free to add any dotfiles that you would like into the dotfiles folder (~/.dotfiles/dotfiles).  It is recommended that you put them into a sub-folder, but it is not required.  When the `bootstrap` script is run, it will find certain file types and perform the following actions:

* \*rc and \*config files, such as vimrc and gitconfig, will be symlinked to the home directory and prefixed with a '.'.  
* \*.symlink files will also be symlinked, prefixed with '.', and the extension '.symlink' will be removed. 
* \*.zsh files will be sourced by the .zshrc file (using an intermediate file that is autogenerated so that .zshrc does not have to change)
* All other files are currently ignored. 

Ignoring dotfiles
-----------------

Todo
