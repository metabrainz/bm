Needs "requests" library, so:

    sudo apt-get install python-virtualenv
    mkdir ~/ve
    virtualenv ~/ve/bm
    ~/ve/bm/bin/pip install requests
    ~/ve/bm/bin/python ./bm.py | tee results.$HOSTNAME.txt

