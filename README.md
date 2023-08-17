# Alert through Microsoft Teams

This project is a simple solution for sending messages to teams using Webhooks. It can be used for alerting someone in case there is an error in one of his scheduled python code executions.

### Dependencies

Create a venv then use pip:

```shell script
pip install -r requirements
```

### Testing the module

In order to test this module, you have to:
    1- Create your own Incoming Webhook. Follow the instructions on this link : https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=dotnet
    2- Copy the Webhook url and paste It to the parameter in config/config.yml file.
    3- run python scripts/script.py config/config.yml
