# python

This will ask for otp while ssh login 

#Add the file location in /home/${USER}/.bashrc

if [[ -n $SSH_CONNECTION ]] ; then
 /home/${USER}/otp.py
fi
