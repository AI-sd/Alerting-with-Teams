import pymsteams

class TeamsMessageSender():

    def __init__(self, config):
        """

        Args:
            config: config which contains webhook url
        """
        self.config = config

    def send_message_to_teams(self, message):
        """

         Args:
             message:message you want to send to teams channel

         Returns: None

         """
        my_teams_message = pymsteams.connectorcard(self.config['microsoft_teams_webhook_url'])
        my_teams_message.text(message)
        my_teams_message.send()

        return None
