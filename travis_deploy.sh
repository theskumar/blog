#!/bin/bash
ghp-import ${OUTPUTDIR} -m "Blog updated"
git push --force --quiet "https://${GH_TOKEN}@${GH_REF}" master:gh-pages > /dev/null 2>&1
