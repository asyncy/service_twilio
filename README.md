# _GitHub_ Open Microservice
> GitHub API, GraphQL, Webhook and Login Server

[![Open Microservice Specification Version](https://img.shields.io/badge/Open%20Microservice-1.0-477bf3.svg)](https://openmicroservices.org) [![Open Microservices Spectrum Chat](https://withspectrum.github.io/badge/badge.svg)](https://spectrum.chat/open-microservices) [![Open Microservices Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](https://github.com/oms-services/.github/blob/master/CODE_OF_CONDUCT.md) [![Open Microservices Commitzen](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com) 
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Introduction

This project is an example implementation of the [Open Microservice Specification](https://openmicroservices.org), a standard originally created at [Storyscript](https://storyscript.io) for building highly-portable "microservices" that expose the events, actions, and APIs inside containerized software.

## Getting Started

The `oms` command-line interface allows you to interact with Open Microservices. If you're interested in creating an Open Microservice the CLI also helps validate, test, and debug your `oms.yml` implementation!

See the [oms-cli](https://github.com/microservices/oms) project to learn more!

### Installation

```
npm install -g @microservices/oms
```

## Usage

### Open Microservices CLI Usage

Once you have the [oms-cli](https://github.com/microservices/oms) installed, you can run any of the following commands from within this project's root directory:

#### Actions

##### api

> Make an API request to the GitHub REST API
##### Action Arguments

| Argument Name | Type | Required | Default | Description |
|:------------- |:---- |:-------- |:--------|:----------- |
| method | `string` | `false` | None | No description provided. |
| url | `string` | `true` | None | No description provided. |
| data | `map` | `false` | None | The data to post in the API request body. |
| params | `map` | `false` | None | No description provided. |
| headers | `map` | `false` | None | No description provided. |
| token | `string` | `false` | None | A oauth user access token to use during the request for authentication. |
| iid | `int` | `false` | None | The GitHub App installation ID to use during authentication. |
| APP_ID | `int` | `false` | None | Your GitHub App ID |
| APP_PRIVATE_KEY | `string` | `false` | None | Your GitHub App private key in PEM format |
| HOSTNAME | `string` | `false` | None | The GitHub Hostname (for GitHub Enterprise) |
| API_HOSTNAME | `string` | `false` | None | The GitHub API Hostname (for GitHub Enterprise) Default to "api.HOSTNAME"  |
| CLIENT_ID | `string` | `false` | None | The GitHub Oauth Client ID |
| CLIENT_SECRET | `string` | `false` | None | The GitHub Oauth Client Secret |
| OAUTH_TOKEN | `string` | `false` | None | A user oauth token to be used if not provided during an action. |
| WEBHOOK_SECRET | `string` | `false` | None | Used to check the webhook payload signature. |
| USER_AGENT | `string` | `false` | None | GitHub requires a the User-Agent header defined. |

``` shell
oms run api \ 
        -a method='*****' \ 
        -a url='*****' \ 
        -a data='*****' \ 
        -a params='*****' \ 
        -a headers='*****' \ 
        -a token='*****' \ 
        -a iid='*****' \ 
        -e APP_ID=$APP_ID \ 
        -e APP_PRIVATE_KEY=$APP_PRIVATE_KEY \ 
        -e HOSTNAME=$HOSTNAME \ 
        -e API_HOSTNAME=$API_HOSTNAME \ 
        -e CLIENT_ID=$CLIENT_ID \ 
        -e CLIENT_SECRET=$CLIENT_SECRET \ 
        -e OAUTH_TOKEN=$OAUTH_TOKEN \ 
        -e WEBHOOK_SECRET=$WEBHOOK_SECRET \ 
        -e USER_AGENT=$USER_AGENT 
```

##### graphql

> Query GitHub GraphQL
##### Action Arguments

| Argument Name | Type | Required | Default | Description |
|:------------- |:---- |:-------- |:--------|:----------- |
| query | `string` | `true` | None | No description provided. |
| headers | `map` | `false` | None | No description provided. |
| token | `string` | `false` | None | A oauth user access token to use during the request for authentication. |
| iid | `int` | `false` | None | The GitHub App installation ID to use during authentication. |
| APP_ID | `int` | `false` | None | Your GitHub App ID |
| APP_PRIVATE_KEY | `string` | `false` | None | Your GitHub App private key in PEM format |
| HOSTNAME | `string` | `false` | None | The GitHub Hostname (for GitHub Enterprise) |
| API_HOSTNAME | `string` | `false` | None | The GitHub API Hostname (for GitHub Enterprise) Default to "api.HOSTNAME"  |
| CLIENT_ID | `string` | `false` | None | The GitHub Oauth Client ID |
| CLIENT_SECRET | `string` | `false` | None | The GitHub Oauth Client Secret |
| OAUTH_TOKEN | `string` | `false` | None | A user oauth token to be used if not provided during an action. |
| WEBHOOK_SECRET | `string` | `false` | None | Used to check the webhook payload signature. |
| USER_AGENT | `string` | `false` | None | GitHub requires a the User-Agent header defined. |

``` shell
oms run graphql \ 
        -a query='*****' \ 
        -a headers='*****' \ 
        -a token='*****' \ 
        -a iid='*****' \ 
        -e APP_ID=$APP_ID \ 
        -e APP_PRIVATE_KEY=$APP_PRIVATE_KEY \ 
        -e HOSTNAME=$HOSTNAME \ 
        -e API_HOSTNAME=$API_HOSTNAME \ 
        -e CLIENT_ID=$CLIENT_ID \ 
        -e CLIENT_SECRET=$CLIENT_SECRET \ 
        -e OAUTH_TOKEN=$OAUTH_TOKEN \ 
        -e WEBHOOK_SECRET=$WEBHOOK_SECRET \ 
        -e USER_AGENT=$USER_AGENT 
```

##### events

> Server for GitHub webhooks
##### Action Arguments

| Argument Name | Type | Required | Default | Description |
|:------------- |:---- |:-------- |:--------|:----------- |
| APP_ID | `int` | `false` | None | Your GitHub App ID |
| APP_PRIVATE_KEY | `string` | `false` | None | Your GitHub App private key in PEM format |
| HOSTNAME | `string` | `false` | None | The GitHub Hostname (for GitHub Enterprise) |
| API_HOSTNAME | `string` | `false` | None | The GitHub API Hostname (for GitHub Enterprise) Default to "api.HOSTNAME"  |
| CLIENT_ID | `string` | `false` | None | The GitHub Oauth Client ID |
| CLIENT_SECRET | `string` | `false` | None | The GitHub Oauth Client Secret |
| OAUTH_TOKEN | `string` | `false` | None | A user oauth token to be used if not provided during an action. |
| WEBHOOK_SECRET | `string` | `false` | None | Used to check the webhook payload signature. |
| USER_AGENT | `string` | `false` | None | GitHub requires a the User-Agent header defined. |

``` shell
oms run events \ 
        -e APP_ID=$APP_ID \ 
        -e APP_PRIVATE_KEY=$APP_PRIVATE_KEY \ 
        -e HOSTNAME=$HOSTNAME \ 
        -e API_HOSTNAME=$API_HOSTNAME \ 
        -e CLIENT_ID=$CLIENT_ID \ 
        -e CLIENT_SECRET=$CLIENT_SECRET \ 
        -e OAUTH_TOKEN=$OAUTH_TOKEN \ 
        -e WEBHOOK_SECRET=$WEBHOOK_SECRET \ 
        -e USER_AGENT=$USER_AGENT 
```

## Contributing

All suggestions in how to improve the specification and this guide are very welcome. Feel free share your thoughts in the Issue tracker, or even better, fork the repository to implement your own ideas and submit a pull request.

[![Edit github on CodeSandbox](https://codesandbox.io/static/img/play-codesandbox.svg)](https://codesandbox.io/s/github/oms-services/github)

This project is guided by [Contributor Covenant](https://github.com/microservices/.github/blob/master/CODE_OF_CONDUCT.md). Please read out full [Contribution Guidelines](https://github.com/oms-services/.github/blob/master/CONTRIBUTING.md).

## Additional Resources

* [Install the CLI](https://github.com/microservices/oms) - The OMS CLI helps developers create, test, validate, and build microservices.
* [Example OMS Services](https://github.com/oms-services) - Examples of OMS-compliant services written in a variety of languages.
* [Example Language Implementations](https://github.com/microservices) - Find tooling & language implementations in Node, Python, Scala, Java, Clojure.
* [Storyscript Hub](https://hub.storyscript.io) - A public registry of OMS services.
* [Community Chat](https://spectrum.chat/open-microservices) - Have ideas? Questions? Join us on Spectrum.

## License

Unless attributed otherwise, everything is under the MIT License.
