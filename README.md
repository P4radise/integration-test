# documentation
Documentation, HowTos and Best Practises for OneVizion integrations development

View wiki at https://github.com/ov-integrations/documentation/wiki

# Имя интеграции

Описание того, что делает эта интеграция

## Требования

Описание того, что используется в этой интеграции, что должно быть дополнительно установлено на сервере клиента

## Как использовать интеграцию

Описания того, что должно быть сделано, чтобы интеграция заработала:
1. Настроить сервис, с которым работает данная интеграция
2. Создать специального пользователя для интеграции и выдать ему права для этой интеграции:
   - Чтение данных в Trackor_1
   - Чтение и изменение данных в Trackor_2
3. Установить интеграцию в Integration Hub
4. Заполнить файл настроек
5. Включить интеграцию

Пример заполнения файла настроек

```json
{
    "ovUrl": "https://test.onevizion.com",
    "ovAccessKey": "*****",
    "ovSecretKey": "*****",
    "ovIntegrationName": "Integration Name",

    "fieldN": "*****"
}
```