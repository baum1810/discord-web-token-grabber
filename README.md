# Deleted because github doesnt like grabbers and bans creators now

# Discord Web Token Grabber Version 1.2
A tool for grabbing Discord tokens using a redirect bypass technique.

## discord
- https://dsc.gg/project-asura

## Description
This tool consists of a JavaScript/Python script that allows you to grab Discord tokens by bypassing the block on requests to webhooks. It works by uploading the server.py script to a hosting service and using the builder.py script to generate a payload that can be pasted into the browser console while Discord is open in the tab. The token will then be sent to the specified webhook.

## Setup
1. Upload the server.py script to a hosting service such as Replit or any other hosting service of your choice.
2. Replace the text YOUR WEBHOOK in the server.py script with the webhook you want the token to be sent to.
3. Start the hosting service and copy the URL of the server.py script.
4. Start the builder.py script and input the URL of the server.py script.
5. Copy the generated payload and paste it into the browser console while Discord is open in the tab. The token will be sent to the specified webhook.


## Dependencies
Python 3
## Disclaimer
This tool is intended for educational and research purposes only. It is not intended to be used for illegal activities. The creators and maintainers of this tool are not responsible for any misuse or illegal activities that may be carried out with it. Use at your own risk.


## Changelog

### version 1.2
- added storing tokens in txt file
- added a try statement to send webhook
- added anti duplicate for the txt file

### version 1.1
- added the sending ip
- added redirect to /app instead of just discord
- added redirect at starting page of the server
- removed token check because replit caused many issues with it

### Version 1.0
- added server.py
- added builder.py
