# documentation
Documentation, HowTos and Best Practises for OneVizion integrations development

View wiki at https://github.com/ov-integrations/documentation/wiki

# Integration name

Description of what this integration does, what task it performs

## Requirments

Description of what is used in this integration, what should be additionally installed on the client's server

## Usage

Descriptions of what needs to be done for the integration to work:
1. Configure the service that this integration works with
2. Create dedicated account for integration with following privs:
   - Trackor_1 R (Read) 
   - Trackor_2 RE (Read and Edit)
3. Install this integration in Integration Hub
4. Fill the integartion settings file
   - For each parameter, you need to add a description of what should be written to it
5. Enable the integartion

Example of settings.json

```json
{
    "ovUrl": "https://test.onevizion.com",
    "ovAccessKey": "*****",
    "ovSecretKey": "*****",

    "fieldN": "*****"
}
```