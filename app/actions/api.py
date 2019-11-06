# -*- coding: utf-8 -*-

from app import api, GitHub

@api.route('/api')
async def _api(req, resp):
    data = await req.media()
    resp.headers['Content-Type'] = 'application/json'
    resp.text = GitHub.api(**data)