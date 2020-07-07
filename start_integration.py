from integration_log import IntegrationLog, LogLevel
from integration import Integration
import json
import traceback

with open('settings.json', "rb") as SFile:
    settings_data = json.loads(SFile.read().decode('utf-8'))

ov_url = settings_data['ovUrl']
ov_access_key = settings_data['ovAccessKey']
ov_secret_key = settings_data['ovSecretKey']
ov_integration_name = settings_data['ovIntegrationName']

field_n = settings_data['dataN']

with open('ihub_parameters.json', "rb") as PFile:
    ihub_data = json.loads(PFile.read().decode('utf-8'))

process_id = ihub_data['processId']

integration_log = IntegrationLog(process_id, ov_url, ov_access_key, ov_secret_key,
                                 ov_integration_name, ov_token=True)

integration = Integration(integration_log)

try:
    integration.start()
except Exception as e:
    if type(e).__name__ == 'IntegrationError':
        error_message = str(e.message)
        description = str(e.description)
    else:
        error_message = repr(e)
        description = traceback.format_exc()

    integration_log.add(LogLevel.ERROR, error_message, description)
    raise Exception(error_message)
