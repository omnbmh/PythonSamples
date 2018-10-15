#!/usr/bin/env python
# -*- coding: utf-8 -*-

# detetime
import datetime

print(datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"))
# out Monday 15 October 2018 02:38:25PM
print(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
# out 20181015143825
