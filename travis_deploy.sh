#!/bin/bash
ghp-import ${OUTPUTDIR} -m "Blog updated with travis"
git push --force --quiet "https://${GH_TOKEN}@${GH_REF}" gh-pages:gh-pages
echo 'Deployed to gh-pages'
