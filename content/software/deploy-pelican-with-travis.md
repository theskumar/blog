Title: Deploy pelican using Travis-ci on github
Date: 2014-04-05 12:43
Tags: travis-ci, github, blogging
Summary: How to a host pelican blog on github with gh-pages having automacially complied and updated with travis-ci.


## Generating Secret deploy key for travis

Obtain your github personal token[1], and generate a secret environment variable using `travis-encrypt`.

[1] [gh:settings/tokens/new](https://github.com/settings/tokens/new)

    :::shell
    npm install travis-encrypt -g
    travis-encrypt -r [repository slug] -k GH_TOKEN -v [the token you created before]
    # e.g travis-encrypt -r theskumar/blog -k GH_TOKEN -v AAaAdw...UyT

**.travis.yml** 

    :::yaml
    branches:
      only:
      - master
    language: python
    python:
    - 2.7
    install:
    - pip install -r requirements.txt --use-mirrors
    script:
    - make publish
    notifications:
      email:
        on_failure: always
    env:
      global:
      - OUTPUTDIR: output
      - GH_REF: github.com/username/repo.git
      - secure: [put secure generated key here]
    after_success: bash travis_deploy.sh

In `.travis.yml`, add the secure key generated above in the `env > global` section and replace `GH_REF` with your github details.

**travis_deploy.sh**

    :::shell
    #!/bin/bash
    ghp-import ${OUTPUTDIR} -m "Blog updated using Travis"
    git push --force --quiet "https://${GH_TOKEN}@${GH_REF}" gh-pages:gh-pages
    echo 'Deployed to gh-pages'
