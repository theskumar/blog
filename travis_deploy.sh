#!/bin/bash
ghp-import ${OUTPUTDIR} -m "Blog updated with travis"
git push --force --quiet "https://${GH_TOKEN}@${GH_REF}" master:gh-pages > /dev/null 2>&1
echo 'Deployed to gh-pages'
