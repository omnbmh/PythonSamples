#!/usr/bin/env python
# -*- coding: utf-8 -*-
a = []

a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)

for i in a:
    if i == 3:
        a.remove(i)

print a