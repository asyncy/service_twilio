# -*- coding: utf-8 -*-

import hmac
import json
import requests
from hashlib import sha1
from urllib.parse import parse_qs

from app import api, env


def match_any_if_any(event, events):
    return events is None or event in events


class Subscription:
    def __init__(self, data):
        self.data = data
        self.events = data['data'].get('events')  # user defined
    
    def __getitem__(self, config):
        return self.data[config]


class Subscriptions:
    store = {}

    @classmethod    
    def add(cls, sub):
        Subscriptions.store[sub['id']] = Subscription(sub)
    
    @classmethod
    def is_listening_for(cls, event):
        for id, sub in Subscriptions.store.items():
            if match_any_if_any(event, sub.events):
                return True
        return False
    
    @classmethod
    def publish(cls, eventid, event, data):
        for id, sub in Subscriptions.store.items():
            if match_any_if_any(event, sub.events):
                requests.post(
                    sub['endpoint'],
                    headers={'Content-Type': 'application/json'},
                    data=json.dumps(dict(
                        eventType=event,
                        cloudEventsVersion='0.1',
                        contentType='application/vnd.omg.object+json',
                        eventID=eventid,
                        data=data
                    ))
                )

    @classmethod
    def remove(cls, eventid):
        Subscriptions.store.pop(eventid, None)


@api.route('/webhooks/subscribe')
async def subscribe(req, resp):
    data = await req.media()
    Subscriptions.add(data)
    resp.text = 'Subscribed'


@api.route('/webhooks/unsubscribe')
async def unsubscribe(req, resp):
    data = await req.media()
    Subscriptions.remove(data['id'])
    resp.text = 'Unsubscribed'


@api.route('/webhooks')
async def webhooks(req, resp):
    """
    Handle incoming GitHub webhooks
    """
    data = await req.content
    
    eventid = req.headers.get('X-GitHub-Delivery')
    event = req.headers.get('X-GitHub-Event')
    content_type = req.headers.get('Content-Type')

    if not Subscriptions.is_listening_for(event):
        resp.text = f'Accepted, but not listening for {event} events.'
        return

    if env.webhook_secret:
        signature = req.headers.get('X-Hub-Signature')
        assert signature, 'X-Hub-Signature not found in the header.'

        sha_name, signature = signature.split('=')
        assert sha_name == 'sha1'

        key = env.webhook_secret.encode()
        mac = hmac.new(key, data, 'sha1')
        assert hmac.compare_digest(mac.hexdigest(), signature)

    decoded_data = data.decode()
    if content_type == 'application/x-www-form-urlencoded':
        payload = json.loads(parse_qs(decoded_data)["payload"][0])
    elif content_type == 'application/json':
        payload = json.loads(decoded_data)
    else:
        raise Exception('Unknown content-type %s' % content_type)

    Subscriptions.publish(
        eventid, event,
        {'event': event, 'payload': payload})
    
    resp.text = 'Accepted'
