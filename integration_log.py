from enum import Enum
from datetime import datetime
import json
import requests


class IntegrationLog:

    def __init__(self, process_id, url, username, password, integration_name, ov_token=False):
        self._url = url
        self._process_id = process_id
        if ov_token == True:
            self._auth = HTTPBearerAuth(username, password)
        else:
            self._auth = requests.auth.HTTPBasicAuth(username, password)
        self._integration_name = integration_name
        self._integration_params = self.get_integration_params()
        self._ov_log_level = LogLevel.get_log_level_by_name(self._integration_params["log_level"])

    def get_integration_params(self):
        headers = {'content-type': 'application/json'}
        url = self._url + "/api/v3/integrations/" + self._integration_name
        curl = Curl('GET', url, headers=headers, auth=self._auth)
        if len(curl.errors) > 0:
            raise Exception(curl.errors)
        return curl.jsonData

    def add(self, log_level, message, description=""):
        if log_level.log_level_id <= self._ov_log_level.log_level_id:
            parameters = {'message': message, 'description': description, 'log_level_name': log_level.log_level_name}
            json_data = json.dumps(parameters)
            headers = {'content-type': 'application/json'}
            url_log = self._url + "/api/v3/integrations/runs/" + str(self._process_id) + "/logs"
            curl = Curl('POST', url_log, data=json_data, headers=headers, auth=self._auth)
            if len(curl.errors) > 0:
                raise Exception(curl.errors)
            return curl.jsonData


class LogLevel(Enum):
    ERROR = (0, "Error")
    WARNING = (1, "Warning")
    INFO = (2, "Info")
    DEBUG = (3, "Debug")

    def __init__(self, log_level_id, log_level_name):
        self.log_level_id = log_level_id
        self.log_level_name = log_level_name

    @staticmethod
    def get_log_level_by_name(ov_log_level_name):
        for log_level in list(LogLevel):
            if log_level.log_level_name == ov_log_level_name:
                return log_level
        raise Exception("Cannot find the log level called '{}'".format(ov_log_level_name))
    

class HTTPBearerAuth(requests.auth.AuthBase):
	def __init__(self, ov_access_key, ov_secret_key):
		self.access_key = ov_access_key
		self.secret_key = ov_secret_key

	def __call__(self, request):
		request.headers['Authorization'] = 'Bearer ' + self.access_key + ':' + self.secret_key
		return request


class Curl:

    def __init__(self, method='GET', url=None, **kwargs):
        self.method = method
        self.url = url
        self.params = None
        self.data = None
        self.headers = None
        self.cookies = None
        self.files = None
        self.auth = None
        self.timeout = None
        self.allow_redirects = True
        self.proxies = None
        self.hooks = None
        self.stream = None
        self.verify = None
        self.cert = None
        self.json = None
        self.request = None
        self.errors = []
        self.jsonData = {}
        self.args = {}
        self.duration = None
        self.sentUrl = None
        self.sentArgs = None
        for key, value in kwargs.items():
            self.args[key] = value
            setattr(self, key, value)

        if self.url is not None:
            self.runQuery()

    def setArg(self, key, value):
        if value is not None:
            self.args[key] = value

    def runQuery(self):
        self.setArg('params', self.params)
        self.setArg('data', self.data)
        self.setArg('headers', self.headers)
        self.setArg('cookies', self.cookies)
        self.setArg('files', self.files)
        self.setArg('auth', self.auth)
        self.setArg('timeout', self.timeout)
        self.setArg('allow_redirects', self.allow_redirects)
        self.setArg('proxies', self.proxies)
        self.setArg('hooks', self.hooks)
        self.setArg('stream', self.stream)
        self.setArg('verify', self.verify)
        self.setArg('cert', self.cert)
        self.setArg('json', self.json)

        self.errors = []
        self.jsonData = {}
        self.sentUrl = self.url
        self.sentArgs = self.args
        before = datetime.utcnow()
        try:
            self.request = requests.request(self.method, self.url, **self.args)
        except Exception as e:
            self.errors.append(str(e))
        else:
            if self.request.status_code not in range(200, 300):
                self.errors.append(
                    str(self.request.status_code) + " = " + self.request.reason + "\n" + str(self.request.text))
            try:
                self.jsonData = json.loads(self.request.text)
            except Exception:
                pass

        after = datetime.utcnow()
        delta = after - before
        self.duration = delta.total_seconds()
