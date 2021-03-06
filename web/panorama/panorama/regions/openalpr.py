import logging

# This dependency is available in the docker container, which also has the binaries installed
from openalpr.openalpr import Alpr

# paths after installation of OpenALPR in the docker
OPENALPR_DATA = "/usr/share/openalpr/runtime_data"
OPENALPR_CONF = "/etc/openalpr/openalpr.conf"
LICENSEPLATE_REGION = "eu"

log = logging.getLogger(__name__)


class OpenAlprError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class OpenAlpr(object):
    alpr = None

    def __init__(self):
        if not self.alpr:
            self.alpr = Alpr(LICENSEPLATE_REGION, OPENALPR_CONF, OPENALPR_DATA)
            if not self.alpr.is_loaded():
                raise OpenAlprError("Error loading OpenALPR")
            else:
                log.info("Using OpenALPR {}".format(self.alpr.get_version()))

