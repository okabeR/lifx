#!/usr/bin/env python
# coding=utf-8

import lifxlan
from lifxlan import LifxLAN

lifxlan = LifxLAN()

lifxlan.set_power_all_lights("on", rapid=True)

