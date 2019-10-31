# -*- coding: utf-8 -*-

from . import app
from . import api
from . import graphql
from . import login
from . import webhooks


if __name__ == '__main__':
    app.api.run(address='0.0.0.0', port=5042)