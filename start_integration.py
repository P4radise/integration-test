import sys
import subprocess


try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'python_dependencies.txt'])
except Exception as e:
    raise Exception(f'Failed to install package. Exception [{str(e)}]')


from onevizion import IntegrationLog, LogLevel
from integration import Integration
from jsonschema import validate
import json

with open('settings.json', "rb") as PFile:
    settings_data = json.loads(PFile.read().decode('utf-8'))

with open('settings_schema.json', "rb") as PFile:
    data_schema = json.loads(PFile.read().decode('utf-8'))

try:
    validate(instance=settings_data, schema=data_schema)
except Exception as e:
    raise Exception("Incorrect value in the settings file\n{}".format(str(e)))

ov_url = settings_data['ovUrl']
ov_access_key = settings_data['ovAccessKey']
ov_secret_key = settings_data['ovSecretKey']

field_n = settings_data['dataN']

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
