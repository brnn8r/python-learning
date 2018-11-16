import logging
import yaml

with open("log_spec.yaml", "r") as log_spec_file:
    logging.config.dictConfig(yaml.load(log_spec_file))