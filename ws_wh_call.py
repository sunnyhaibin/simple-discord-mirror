#!/usr/bin/env python3
# The MIT License
#
# Copyright (c) 2023-, Haibin Wen, Jason Wen, sunnyhaibin, and a number of other of contributors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import argparse
import json
import requests
import time
import threading
import websocket


class MirrorBot:
  def __init__(self):
    self.ws = websocket.WebSocket()
    self.event = None
    self.heartbeat_interval = None

  def send_json_request(self, request):
    self.ws.send(json.dumps(request))

  def receive_json_response(self):
    response = self.ws.recv()
    if response:
      return json.loads(response)

  def heartbeat(self, interval, ws):
    print("Heartbeat begins")
    while True:
      time.sleep(interval)
      heartbeat_json = {
        "op": 1,
        "d": "null"
      }
      self.send_json_request(heartbeat_json)
      print("Heartbeat sent")

  def mirror_thread(self, source_server, source_channel, webhook_url, webhook_name, auth_token):
    self.ws.connect("wss://gateway.discord.gg/?v=6&encording=json")
    self.event = self.receive_json_response()

    self.heartbeat_interval = self.event["d"]["heartbeat_interval"] / 1000
    threading._start_new_thread(self.heartbeat, (self.heartbeat_interval, self.ws))

    payload = {
      "op": 2,
      "d": {
        "token": auth_token,
        "properties": {
          "$os": "windows",
          "$browser": "chrome",
          "$device": "pc",
          "$referer": f"https://discord.com/channels/{source_server}/{source_channel}"
        }
      }
    }
    self.send_json_request(payload)
    while 1:
      self.event = self.receive_json_response()
      try:
        channel_id = f"{self.event['d']['channel_id']}"
        message = f"{self.event['d']['author']['username']}: {self.event['d']['content']}"
        print(message)
        if self.event['d']['author']['username'] != webhook_name and channel_id == source_channel:
          requests.post(f"{webhook_url}", data={'content': message})
        op_code = self.event('op')
        if op_code == 11:
          print("Heartbeat received")
      except KeyboardInterrupt:
        break
      except:
        pass


def main(source_server, source_channel, webhook_url, webhook_name, auth_token):
  mirror = MirrorBot()
  mirror.mirror_thread(source_server, source_channel, webhook_url, webhook_name, auth_token)


if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Mirror and log Discord messages from a defined source channel")
  parser.add_argument("--source_server", required=True, help="Source channel's Server ID (required)")
  parser.add_argument("--source_channel", required=True, help="Source channel's Channel ID (required)")
  parser.add_argument("--webhook_url", required=True, help="The webhook URL to send mirrored messages to the target channel (required)")
  parser.add_argument("--webhook_name", required=True, help="The webhook name used for the webhook URL (required)")
  parser.add_argument("--auth_token", required=True, help="Authentication Token (required)")

  args = parser.parse_args()

  main(args.source_server, args.source_channel, args.webhook_url, args.webhook_name, args.auth_token)
