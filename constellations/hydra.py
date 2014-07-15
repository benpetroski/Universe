'''
@author: bpetroski
'''
# Converts hex characters to ascii for first Twitter tweet.

if __name__ == "__main__": 
    handle='62656e'
    print 'My real name is:'
    print handle.decode('hex')