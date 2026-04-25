"""
Simple tracing utility for request flow.
"""

import time

class Tracer:
    def start(self):
        return time.time()

    def end(self, start_time):
        return time.time() - start_time