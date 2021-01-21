#!/usr/bin/python

from words import *

repo = WordRepository()

while True:
    reply = unicode(raw_input('\nWord to delete> '), 'utf8')
    
    if reply:
        deleted = repo.delete_word(reply)

        if deleted:
            print reply.encode('utf8'), 'deleted.'
        else:
            print reply.encode('utf8'), ' does not exist.'
    else:
        print 'Goodbye!'
        break
