# -*- coding: utf-8 -*-

from app import api, GitHub


@api.route('/graphql')
async def graphql(req, resp):
    data = await req.media()
    resp.headers['Content-Type'] = 'application/json'
    resp.text = GitHub.graphql(**data)
