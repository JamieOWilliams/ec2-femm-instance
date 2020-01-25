import sys
import logging
from app import app as application

activate_this = '/home/ubuntu/ec2-femm-instance/venv/bin/activate_this.py'

with open(activate_this) as f:
    exec(f.read(), dict(__file__=activate_this))

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/html/ec2-femm-instance/")
