# _GitHub_ OMG Microservice

[![Open Microservice Guide](https://img.shields.io/badge/OMG%20Enabled-👍-green.svg?)](https://microservice.guide)

<!-- ### <img src="https://user-images.githubusercontent.com/4370550/56803568-460e5800-6823-11e9-8a70-25ab4b7e32ea.png" width="40" align="center"> Storyscript example -->

## Direct usage in [Storyscript](https://storyscript.io/):

```coffee
# Make GitHub API requests
res = github api url:'/users/stevepeak'

# Make GitHub GraphQL requests
res = github graphql query:'{user}'

# Webhooks made easy.
when github events webhooks events:['push'] as event
    repo = event.payload['repository']
```

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMG CLI](https://www.npmjs.com/package/omg)

##### API
```shell
$ omg run api -a method=<METHOD> -a url=<URL> -a data=<DATA_IN_MAP_TYPE> -a params=<PARAMS_IN_MAP_TYPE> -a header=<HEADER_IN_MAP_TYPE>  -a token=<ACCESS_TOKEN> -a iid=<INSTALLATION_ID> -e APP_ID=<APP_ID> -e APP_PRIVATE_KEY=<APP_PRIVATE_KEY> -e HOSTNAME=<HOSTNAME> -e API_HOSTNAME=<API_HOSTNAME> -e CLIENT_ID=<CLIENT_ID> -e CLIENT_SECRET=<CLIENT_SECRET> -e OAUTH_TOKEN=<OAUTH_TOKEN> -e WEBHOOK_SECRET=<WEBHOOK_SECRET> -e USER_AGENT=<USER_AGENT>
```
##### Graphql
```shell
omg run graphql -a query=<QUERY> -a header=<HEADER_IN_MAP_TYPE>  -a token=<ACCESS_TOKEN> -a iid=<INSTALLATION_ID> -e APP_ID=<APP_ID> -e APP_PRIVATE_KEY=<APP_PRIVATE_KEY> -e HOSTNAME=<HOSTNAME> -e API_HOSTNAME=<API_HOSTNAME> -e CLIENT_ID=<CLIENT_ID> -e CLIENT_SECRET=<CLIENT_SECRET> -e OAUTH_TOKEN=<OAUTH_TOKEN> -e WEBHOOK_SECRET=<WEBHOOK_SECRET> -e USER_AGENT=<USER_AGENT>
```
##### Events
```shell
omg subscribe events webhooks -a events=<LIST_OF_EVENTS> -e APP_ID=<APP_ID> -e APP_PRIVATE_KEY=<APP_PRIVATE_KEY> -e HOSTNAME=<HOSTNAME> -e API_HOSTNAME=<API_HOSTNAME> -e CLIENT_ID=<CLIENT_ID> -e CLIENT_SECRET=<CLIENT_SECRET> -e OAUTH_TOKEN=<OAUTH_TOKEN> -e WEBHOOK_SECRET=<WEBHOOK_SECRET> -e USER_AGENT=<USER_AGENT>
```

**Note**: The OMG CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/github/blob/master/LICENSE).


