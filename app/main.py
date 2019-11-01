# -*- coding: utf-8 -*-

import app
from actions import api, graphql, login, webhooks

if __name__ == '__main__':
    app.api.run(address='0.0.0.0', port=5042)