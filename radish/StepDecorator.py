# -*- coding: utf-8 -*-

import re

from radish.StepRegistry import StepRegistry
from radish.Exceptions import StepLoadingError


def step(regex):
    def wrapper(func):
        try:
            re.compile(regex)
        except Exception:
            print StepLoadingError(regex)
            raise SystemExit(-2)
        StepRegistry().register(regex, func)
        return func
    return wrapper
