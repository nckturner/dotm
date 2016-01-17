#!/usr/bin/python

import yaml
import os
import sys
import config

red = "\033[1;31m" 
green = "\033[1;32m" 
crimson = "\033[1;38m" 
color_end = "\033[1;m"

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def link_module(module_name, bool_link):

    with open(config.dotfiles_dir + module_name + "/" + "module.yaml", 'r') as stream:
        module = yaml.load(stream)
  
    if not module:
        return

    files = module['files']
    file_names = module['files'].keys()
    for file in file_names:
        
        src_file_name, dest_file_name = file, files[file]
        src = os.path.abspath(find( src_file_name, config.dotfiles_dir))
        dest = config.home + dest_file_name
       
        # pass true to link, false to unlink
        if bool_link: 
            path, fn = os.path.split(dest)
            # lexists returns true for broken links, we could replace those links but 
            # for simplicity we just ignore them.  Passing -u will unlink them and 
            # they can be readded correctly with another run of -l.  
            if not os.path.lexists(path):
                print("Creating dirs in path: " + path)
                os.makedirs(path)
            print("Linking " + dest + " to " + src + ".")
            if os.path.isfile(dest):
                print(red + "- Skipping " + color_end + dest + ", it already exists") 
            else:
                os.symlink(src, dest)
                print(green + "+ Success!" + color_end) 
        else:
            print("Unlinking" + dest + " from " + src + ".")
            # lexists returns true for broken links
            if os.path.lexists(dest):
                os.unlink(dest)
                print(green + "+ Success!" + color_end) 
            else:
                print(red + "- Skipping " + color_end + dest + ", it does not exist") 


def link_all(bool_link):

    with open(config.dotfiles_conf, 'r') as stream:
        modules = yaml.load(stream)

    link_module("default", bool_link)

    for module in modules["modules"]:
        link_module(module, bool_link)


def usage():
    print("link_files.py -u | -l")
    print("-l: Symlinks files in dotfiles directory to home directory.")
    print("-u: Reverses process by unlinking symlinks.")
    exit(1)       

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
    
    if sys.argv[1] == "-u":
        link_all(False)
    elif sys.argv[1] == "-l":
        link_all(True)
    else:
        usage()
 


