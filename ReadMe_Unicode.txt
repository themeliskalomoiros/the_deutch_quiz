Unicode and Python 2.7

The type 'str' in Python 2.7 represents bytes and not strings as in other languages such as Java, C#, or Python 3.
To read unicode strings you have to

    uni_string = unicode(raw_input('Enter unicode text '), 'utf-8')
    
