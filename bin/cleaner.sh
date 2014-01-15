#!/bin/bash
date >> /cpm/projects/smapi/logs/cleaner.log 2>&1
/usr/bin/find /cpm/projects/smapi/data/bmarks -amin +180 -delete >> /cpm/projects/smapi/logs/cleaner.log 2>&1
/usr/bin/find /cpm/projects/smapi/data/bmarks -mmin +240 -delete >> /cpm/projects/smapi/logs/cleaner.log 2>&1

