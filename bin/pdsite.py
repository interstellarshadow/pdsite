#!/usr/bin/env python3

import os
import argparse
import shutil
import http.server as hs

#######################################################################################################
#         Setup                                                                                       #
#######################################################################################################

scriptdir = os.path.dirname(os.path.realpath(__file__))
themesdir = os.path.join(scriptdir, '..', 'themes')
defaultconfig = os.path.join(scriptdir, '..', '.pdsite.yml.default')

main_parser = argparse.ArgumentParser(description='Build a static website with Pandoc and Markdown.')
main_parser.add_argument('--debug', action='store_true',
        help='Runs in debug mode and prints debug messages when option is specified.')
main_subparser = main_parser.add_subparsers();

init_parser = main_subparser.add_parser('init', 
        description='Initialize a project for use with ' + main_parser.prog + '.')
build_parser = main_subparser.add_parser('build', description='Generates website files')
build_parser.add_argument('path', nargs='?', default='.html', 
        help='Path to the root directory where the website should be generated.')
serve_parser = main_subparser.add_parser('serve', 
        description='Runs a python webserver to provide access to the website.')
serve_parser.add_argument('-p','--port', type=int, default=8080,
        help='Specifies which port the webserver should be opened on. Default is 8080.')

######################################################################################################
#                    Run Script                                                                      #
######################################################################################################

args = main_parser.parse_args()

debug = False

if args.debug:
    debug = True


if debug:
    print('Script Directory: ' + scriptdir);
    print('Themes Directory: ' + themesdir);
    print('Default Config: ' + defaultconfig);

def init():
    '''Initializes the current directory to have a simple pdsites project.'''

    if debug:
        print('Initializing in: ' + os.cwd)

    shutil.copy2(defaultconfig, os.path.join('.','.pdsite.yml'))

    if debug:
        print('Initialation successful')

if args.init:
    init()
    exit(0)

# TODO set output dir.


def build():
    '''Uses pandoc to generate the website from markdown files in current directory'''

    if debug:
        print('Beginning build')

def serve(port=8080, rebuild):
    '''Creates a webserver using the website that is in the following directory structure'''
    if rebuild:
        build()

    if debug:
        print('Starting Webserver')
    
    server_addr = ('127.0.0.1', port)

    httpd = hs.HTTPServer(server_addr,hs.BaseHTTPRequestHandler)
    httpd = server_forever()

    input


