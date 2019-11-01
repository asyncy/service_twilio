# -*- coding: utf-8 -*-

import requests
from json import dumps
from urllib.parse import urlencode

from app import api, env


# only supports one listener atm
listener = {}


@api.route('/login/subscribe')
async def subscribe(req, resp):
    data = await req.media()
    global listener
    listener = data
    resp.text = 'Subscribed'


@api.route('/login/unsubscribe')
async def unsubscribe(req, resp):
    data = await req.media()
    global listener
    listener = None
    resp.text = 'Unsubscribed'


@api.route('/login/server')
async def login(req, resp):
    if req.params.get('code'):
        # trade code for token
        res = requests.post(
            f'https://{env.hostname}/login/oauth/access_token',
            data=dumps(dict(
                client_id=env.client_id,
                client_secret=env.client_secret,
                code=req.params['code']
            )),
            headers={
                'Content-Type': 'application/json; charset=utf-8',
                'Accept': 'application/json',
                'User-Agent': env.user_agent
            }
        )

        global listener

        requests.post(
            listener['endpoint'],
            headers={'Content-Type': 'application/json'},
            data=dumps(dict(
                eventType='github.login',
                cloudEventsVersion='0.1',
                contentType='text/plain',
                eventID='123abc',
                data=res.json()['access_token']
            ))
        )

        api.redirect(resp,
            location=listener['data']['redirect']
        )

    else:
        # redirect user to login at GitHub
        query = dict(
            scope='user', # ','.join(data['scope']) if data['scope'] else None,
            client_id=env.client_id,
            redirect_uri='http://127.0.0.1:5042/login/server'
        )
        api.redirect(resp,
            location=f'https://{env.hostname}/login/oauth/authorize?{urlencode(query)}'
        )
