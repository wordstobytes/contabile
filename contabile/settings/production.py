from contabile.settings.staging import *

# There should be only minor differences from staging

DATABASES['default']['NAME'] = 'contabile_production'
DATABASES['default']['USER'] = 'contabile_production'

EMAIL_SUBJECT_PREFIX = '[Contabile Prod] '

# Uncomment if using celery worker configuration
# BROKER_URL = 'amqp://contabile_production:%(BROKER_PASSWORD)s@%(BROKER_HOST)s/contabile_production' % os.environ