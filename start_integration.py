import sys
import subprocess

subprocess.Popen([sys.executable, '-m', 'pip', 'install', '-r', 'python_dependencies.txt'], start_new_session=True)


from onevizion import IntegrationLog, LogLevel
from integration import Integration
from jsonschema import validate
import json
import re


with open('settings.json', "rb") as PFile:
    settings_data = json.loads(PFile.read().decode('utf-8'))

with open('settings_schema.json', "rb") as PFile:
    data_schema = json.loads(PFile.read().decode('utf-8'))

try:
    validate(instance=settings_data, schema=data_schema)
except Exception as e:
    raise Exception("Incorrect value in the settings file\n{}".format(str(e)))

ov_url = re.sub('^http://|^https://', '', settings_data['ovUrl'][:-1])
ov_access_key = settings_data['ovAccessKey']
ov_secret_key = settings_data['ovSecretKey']

field_n = settings_data['fieldN']

with open('ihub_parameters.json', "rb") as PFile:
    ihub_data = json.loads(PFile.read().decode('utf-8'))

process_id = ihub_data['processId']
log_level = ihub_data['logLevel']

integration_log = IntegrationLog(process_id, ov_url, ov_access_key, ov_secret_key, None, True, log_level)
integration = Integration(integration_log)

try:
    integration.start()
except Exception as e:
    integration_log.add(LogLevel.ERROR, str(e))
    raise e
