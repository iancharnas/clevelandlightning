#!/usr/bin/env bash

cd ~/BlitzScraper
source env/bin/activate >>cron.log 2>&1
python3 scrapeBlitzortungLightningStrikes.py >>cron.log 2>&1
