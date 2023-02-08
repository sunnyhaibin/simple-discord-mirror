# Simple Discord Mirror## AboutSimple Discord Mirror is a tool that can be deployed to mirror a Discord channel's messages to another Discord's channel. This tool can also be deployed to log Discord messages in realtime. It utilizes Discord API, WebSocket, Discord Webhook and Python.## Features- Mirror normal message(s)- Log messages in realtime## Requirements- [Python](https://www.python.org/downloads/) (3.6 or higher)- [websocket-client](https://pypi.org/project/websocket-client/)## Setup1. Clone Simple Discord Mirror:```bashcd ~git clone https://github.com/sunnyhaibin/simple-discord-mirror.gitcd simple-discord-mirror```or, simply download `ws_wh_call.py`.2. Install the following packages in your environment:   - [Python](https://www.python.org/downloads/)   - [WebSocket](https://pypi.org/project/websocket-client/)## Usage Instructions```bash$ python ./ws_wh_call.py -husage: ws_wh_call.py [-h] --source_server SOURCE_SERVER --source_channel SOURCE_CHANNEL --webhook_url WEBHOOK_URL --webhook_name WEBHOOK_NAME --auth_token AUTH_TOKENMirror and log Discord messages from a defined source channeloptional arguments:  -h, --help            show this help message and exitrequired arguments:  --source_server SOURCE_SERVER                        Source channel's Server ID (required)  --source_channel SOURCE_CHANNEL                        Source channel's Channel ID (required)  --webhook_url WEBHOOK_URL                        The webhook URL to send mirrored messages to the target channel (required)  --webhook_name WEBHOOK_NAME                        The webhook name used for the webhook URL (required)  --auth_token AUTH_TOKEN                        Authentication Token (required)```Licensing------Simple Discord Mirror is released under the MIT license. Some parts of the software are released under other licenses as specified.Any user of this software shall indemnify and hold harmless sunnyhaibin and its directors, officers, employees, agents, stockholders, affiliates, subcontractors and customers from and against all allegations, claims, actions, suits, demands, damages, liabilities, obligations, losses, settlements, judgments, costs and expenses (including without limitation attorneys’ fees and costs) which arise out of, relate to or result from any use of this software by user.**THIS IS ALPHA QUALITY SOFTWARE FOR RESEARCH PURPOSES ONLY. THIS IS NOT A PRODUCT.YOU ARE RESPONSIBLE FOR COMPLYING WITH LOCAL LAWS AND REGULATIONS.NO WARRANTY EXPRESSED OR IMPLIED.**---<img src="https://d1qb2nb5cznatu.cloudfront.net/startups/i/1061157-bc7e9bf3b246ece7322e6ffe653f6af8-medium_jpg.jpg?buster=1458363130" width="75"></img> <img src="https://cdn-images-1.medium.com/max/1600/1*C87EjxGeMPrkTuVRVWVg4w.png" width="225"></img>