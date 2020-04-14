# SSH tunneling and Ngrok

## SSH tunneling for VNC server through NGROK

Run ngrok on your server: `./ngrok tcp 22`

`ssh -L 5901:localhost:5902 dishank@0.tcp.ngrok.io -p 11940`

Explanation: We connect to our nrgrok through port 11940 which basically connects to port 22 of our machine. This command basically forward the port 5902 of our remote machine through the ssh \(which we connected using ngrok on port 11940\) to port 5901 of our local machine.

Now access the vnc screen on `localhost:5901` which is on out local machine.

