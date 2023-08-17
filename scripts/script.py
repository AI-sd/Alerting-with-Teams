import sys
import os
from os.path import abspath, dirname

HERE = abspath(dirname(__file__))
sys.path.append(os.path.dirname(HERE))

from src.alerting.teams_alerting.teams_alerting import TeamsMessageSender
import yaml
import argparse
import requests
import logging


def main():
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("config_path")
    args = parser.parse_args()
    config_path = args.config_path

    try:

        logging.info('call a fake api to generate and error')
        url = 'https://fake_api.com'
        myobj = {'somekey': 'somevalue'}
        x = requests.get(url, json=myobj)

    except requests.exceptions.ConnectionError as error:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)

        teams_message_sender = TeamsMessageSender(config=config)
        logging.info('send error to teams channel')
        teams_message_sender.send_message_to_teams(message=str(error))
        logging.info('Error alert of a pipeline sent to teams')


if __name__ == "__main__":
    main()
