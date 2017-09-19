"""Implements VERB-like objects that allow interction with DOM elements."""
import logging
import threading

from websmith.utils import perform_action_chain_move, wait_until_element_exists

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


class Action(object):
    data = threading.local()

    def __init__(self):
        LOGGER.info('ACTION: {} on {}'.format(
            self.__class__.__name__,
            self.__dict__
        ))
        self._run()

    def _run(self):
        raise NotImplementedError()


class Click(Action):

    def __init__(self, target):
        self.target = target

        super(Click, self).__init__()

    def _run(self):
        wait_until_element_exists(self.browser, self.target).click()


class Hover(Action):

    def __init__(self, target):
        self.target = target

        super(Hover, self).__init__()

    def _run(self):
        perform_action_chain_move(self.browser, self.target)


class Go(Action):

    def __init__(self, url):
        self.url = url

        super(Go, self).__init__()

    def _run(self):
        self.browser.get(self.url)


class SendKeys(Action):

    def __init__(self, target, value):
        self.target = target
        self.value = value

        super(SendKeys, self).__init__()

    def _run(self):
        self.browser.find_element(*self.target).send_keys(self.value)


class Wait(Action):

    def __init__(self, target):
        self.target = target

        super(Wait, self).__init__()

    def _run(self):
        return wait_until_element_exists(self.browser, self.target)


class WaitAndClick(Action):

    def __init__(self, target):
        self.target = target

        super(WaitAndClick, self).__init__()

    def _run(self):
        wait_until_element_exists(self.browser, self.target).click()