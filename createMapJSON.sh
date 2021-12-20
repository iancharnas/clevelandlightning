#!/usr/bin/env bash

cd ~/BlitzScraper
source env/bin/activate >>cron.log 2>&1
python3 mapBlitzortungLightningStrikes.py >>cron.log 2>&1
git add -A >>cron.log 2>&1
git commit -m "Update" >>cron.log 2>&1
git push >>cron.log 2>&1
