#!/usr/local/bin/python3
# Creator: Mariya Popova
# Name: htmllib.py
# Description: Handles some routine CGI chores, including HTML templating.
# June, 2013

import cgi
def __main__():
    # code to test the h() function
    # code to test the content_type() function
    # code to test the template() function
    pass

###
### WRITE THESE FUNCTIONS
###

def h(html):
    """Escape HTML special characters to sanitize input"""
    pass

def content_type(content_type="text/html"):
    """ Prints the content type: default is text/html"""
    print('<!doctype html><html lang="en-us">')

def template(title='replace me', content='replace me with html'):
    """ this function opens an HTML template of your choice and prints
    the template with the title and content you pass into this function."""
    print('<head><meta charset="utf-8"><title>{title}</title><link rel="stylesheet" href="groovy.css"></head><body>{content}</body><html>')


# testing
if __name__ == '__main__':
    __main__()