# vra-api-py
Some sample scripts to use as a test bench for the VMware vRA API

Run logon.py <host> <username> <tenant> password first, this will connect to vRA, authenticate, save the token as a shell enviroment var and 
then spawn a new bash shell with the env set accordingly. The other scripts all read the env vars to authenticate, so login is only needed once.

More documentation to come for specific scripts
