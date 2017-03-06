from django.http import HttpResponse

import logging
import site_vars
import sys

logging.basicConfig(level=logging.INFO)

def dark_launch(orig_func):
  def new_func(*args, **kwargs):
    if hasattr(site_vars, 'NOT_LAUNCHED') and orig_func.func_name in site_vars.NOT_LAUNCHED:
      logging.info('DARK: Toggle for %s is off. Remove it from NOT_LAUNCHED to enable.' % orig_func.func_name)
      pass
    else:
      logging.info('DARK: Toggle for %s is on. Add it to NOT_LAUNCHED to disable.' % orig_func.func_name)
      return orig_func(*args, **kwargs)
  return new_func
