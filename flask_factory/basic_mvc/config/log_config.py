from pathlib import Path

from config.log_config_basic import config_basic


log_file_path = Path(__file__).resolve().parent.parent.joinpath('log_file')

config_basic['handlers']['access']['filename'] = str(log_file_path.joinpath('access', 'access.log'))
config_basic['handlers']['warning']['filename'] = str(log_file_path.joinpath('warning', 'warning.log'))
config_basic['handlers']['error']['filename'] = str(log_file_path.joinpath('error', 'error.log'))
config_basic['handlers']['critical']['filename'] = str(log_file_path.joinpath('critical', 'critical.log'))