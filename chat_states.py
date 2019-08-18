# -*- coding: utf-8 -*-
from enum import Enum


class ChatState(Enum):
    FREE = 'FREE'
    ENTERING_NEWSLETTER_MESSAGE = "ENTERING_NEWSLETTER_MESSAGE"
    CONFIRMING_NEWSLETTER = 'CONFIRMING_NEWSLETTER'
