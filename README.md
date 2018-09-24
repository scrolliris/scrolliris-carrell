# Scrolliris Carrell

Code Name: `Rapperswil-Jona`

[![pipeline status][pipeline]][commit] [![coverage report][coverage]][commit]

[pipeline]: https://gitlab.com/scrolliris/scrolliris-carrell/badges/master/pipeline.svg
[coverage]: https://gitlab.com/scrolliris/scrolliris-carrell/badges/master/coverage.svg
[commit]: https://gitlab.com/scrolliris/scrolliris-carrell/commits/master

## Overview

```txt
 , __                                            _
/|/  \                                       o  | |     /\
 |___/  __,    _    _   _   ,_    ,             | |    |  |  __   _  _    __,
 | \   /  |  |/ \_|/ \_|/  /  |  / \_|  |  |_|  |/ ----|  | /  \_/ |/ |  /  |
 |  \_/\_/|_/|__/ |__/ |__/   |_/ \/  \/ \/  |_/|__/    \_|/\__/   |  |_/\_/|_/
            /|   /|                                      /|
            \|   \|                                      \|

Rapperswil-Jona; carRell APPs for readER aS WebsItes pLatform rapperswil-JONA
```

The application of [https://scrolliris.com/](https://scrolliris.com/).

### Repositories

* https://gitlab.com/scrolliris/scrolliris-carrell (GitLab.com)
* https://github.com/scrolliris/scrolliris-carrell (Mirror)

### Issues

https://gitlab.com/scrolliris/scrolliris-carrell/issues (GitLab.com)


## Requirements

* Python `>= 3.6.6`
* PostgreSQL `>= 9.6.3`
  * hstore
  * plpgsql
  * (pg_stat_statements)
* Node.js `>= 8.11.4` (build)
* GNU gettext `>= 0.19.8.1` (translation)


## Setup

```zsh
% cd /path/to/rapperswil-jona

: use python\'s virtualenv
% python3.6 -m venv venv
% source venv/bin/activate
(venv) % pip install --upgrade pip setuptools

: Node.js (e.g. nodeenv)
(venv) % pip install nodeenv
(venv) % nodeenv --python-virtualenv --with-npm --node=8.11.4
: re-activate for node.js at this time
(venv) % source venv/bin/activate
(venv) % npm install --global npm
(venv) % npm --version
6.4.1
```

Then, check `make help`.

```zsh
(venv) % make help
...
```

### Dependencies

See [Scrolliris Console](https://gitlab.com/scrolliris/scrolliris-console).



## Development

Use `waitress` as wsgi server.  
Check `Makefile`

```zsh
% cd /path/to/rapperswil-jona
% source venv/bin/activate

: set environment variables
(venv) % cp .env.sample .env

: install python packages
(venv) % make setup

: install node modules
(venv) % npm install --global rollup
(venv) % npm install --ignore-scripts

: run rollup
(venv) % make pack

(venv) % make serve
```

### Migration

See [Scrolliris Console](https://gitlab.com/scrolliris/scrolliris-console).

### Styling and Code Analysis

* pycodestyle
* pydocstyle
* pylint
* eslint

#### Python

```zsh
(venv) % make vet:style
(venv) % make vet:lint

: run both
(venv) % make vet
```

for codequality check

```zsh
: run codeclimate in docker
(venv) % make vet:quality
```

#### JavaScript

```zsh
(venv) % npm install eslint -g

(venv) % eslint rollup.config.js
(venv) % eslint rapperswil-jona/assets
```


## Deployment

Setup production environment.

Use `CherryPy` as wsgi server.

```zsh
: run install and start server for production
(venv) % ./bin/serve --env production --config config/production.ini --install

: use Procfile (via `bin/start` command)
(venv) % honcho start
```

### Docker

### App Engine

```zsh
: take latest sdk from https://cloud.google.com/sdk/downloads
% cd lib
(venv) % curl -sLO https://dl.google.com/dl/cloudsdk/channels/rapid/ \
  downloads/google-cloud-sdk-<VERSION>-linux-x86_64.tar.gz

: check sha256 checksum
(venv) % echo "CHECKSUM" "" ./google-cloud-sdk-<VERSION>-linux-x86_64.tar.gz \
  | sha256sum -c -
./google-cloud-sdk-<VERSION>-linux-x86_64.tar.gz: OK
(venv) % tar zxvf google-cloud-sdk-<VERSION>-linux-x86_64.tar.gz

: setup lib/ as a root for sdk
(venv) % CLOUDSDK_ROOT_DIR=. ./google-cloud-sdk/install.sh
(venv) % cd ../
```

### Heroku


## Testing

Run unit and functional tests.
See also `.gitlab-ci.yml`.

```zsh
(venv) % ENV=test make setup
: or manually install packages
(venv) % pip install -e ".[testing]" -c constraints.txt

: build assets
(venv) % make pack

: use make (unit tests and functional tests)
(venv) % make test

: run a test case
(venv) % ENV=test py.test -c config/testing.ini \
  test/route_test.py -k test_routing_to_robots -v
```

Check test coverage

```zsh
(venv) % make test:coverage
```

### CI

You can check it by yourself using `gitlab-runner` on local machine.
It requires `docker`.

```zsh
% ./bin/setup-gitlab-runner

: use script
% ./bin/ci-runner test
```

#### Links

See documents.

* https://docs.gitlab.com/runner/
* https://docs.gitlab.com/runner/install/linux-manually.html


## License

This project is distributed as various licenses by parts.

```txt
Scrolliris Carrell
Copyright (c) 2018 Lupine Software LLC
```

### Documents

`GFDL-1.3`

The files in the `rapperswil-jona/doc` directory are distributed as
GNU Free Documentation License. (version 1.3)

```txt
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3
or any later version published by the Free Software Foundation;
with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in the section entitled "GNU
Free Documentation License".
```

Check the [GNU Free Documentation License](
https://www.gnu.org/licenses/fdl-1.3.en.html).

### Images

`CC-BY-NC-SA-4.0`

The illustration and photos in this project are licensed under the
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
License.

[![Creative Commons License](
https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](
http://creativecommons.org/licenses/by-nc-sa/4.0/)

Check the [Legalcode](
https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode).

### Programs (Software)

`AGPL-3.0`

```txt
This is free software: You can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
```

See [LICENSE](LICENSE).
