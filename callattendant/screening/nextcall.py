#!/usr/bin/env python
#
# file: nextcall.py
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Implement routines that set a flag indicating the next incoming call should
# be permitted, and testing/clearing that flag

import os

class NextCall(object):
    """Track state of the next call flag"""
    def __init__(self, config):
        self.flag_file = config.get("PERMIT_NEXT_CALL_FLAG")
        self.enabled = config.get("PERMIT_NEXT_CALL_ENABLED")
        self.next_permitted = os.path.exists(self.flag_file)

    def is_enabled(self):
        return self.enabled

    def is_next_call_permitted(self):
        return self.next_permitted

    def toggle_next_call_permitted(self):
        if self.next_permitted:
            os.remove(self.flag_file)
            self.next_permitted = False
        else:
            with open(self.flag_file, 'w') as file:
                file.write('Permit')
            self.next_permitted = True

        return self.next_permitted
