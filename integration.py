from onevizion import LogLevel


class Integration:
    def __init__(self, ov_integration_log):
        self._integration_log = ov_integration_log

    def start(self):
        self._integration_log.add(LogLevel.INFO, 'Starting Integration')

        self._integration_log.add(LogLevel.INFO, 'Integration has been completed')