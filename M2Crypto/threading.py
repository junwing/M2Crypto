"""M2Crypto threading support. 

Copyright (c) 1999-2003 Ng Pheng Siong. All rights reserved."""

RCS_id='$Id: threading.py,v 1.2 2002/12/23 03:47:55 ngps Exp $'

# M2Crypto
import m2

def init():
    m2.threading_init()

def cleanup():
    m2.threading_cleanup()

