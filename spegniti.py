#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pypid.pid import *
from time import sleep
import os

channels = [
  37: {
    "channel": "A",
    "status": 1,
    'name': 'pompa 1',
    'events': {
      0: {
        'send': True,
        'message': 'POMPA 1 ON',
      },
      1: {
        'send': True,
        'message': 'pompa 1 off',
      }
    }
  },
]



try:
  logging.debug('loading {0}'.format(channel))
  gpio.setmode(gpio.BOARD)
  gpio.setup(pin, gpio.IN, gpio.PUD_UP)
except:
  logging.error('ERROR LOADING {0}, MODE {1}'.format(channel, mode))
  logging.exception('')
  os._exit(1)



while True:

  # leggo lo status
  status = gpio.input(pin)

  if status != 1:

   before = datetime.now()
   logging.info("Premuto pulsante {}".format(now))

    while status != 1:
      pass

    after = datetime.now()
    delta = after - before

    if delta.seconds > 7:
      logging.info('Shutting down rasp!')
      os.system("shutdown now -h")

  sleep(2)
