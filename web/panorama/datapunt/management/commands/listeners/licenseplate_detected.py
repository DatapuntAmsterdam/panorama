import logging
import json

from datapunt.management.queue import Listener
from datapunt.management.region_csv import region_writer
from datasets.panoramas.models import Panorama, Region

log = logging.getLogger(__name__)


class LicensePlateDone(Listener):
    _route = 'license_plate_done'

    def on_message(self, messagebody):
        message_dict = json.loads(messagebody.decode('utf-8'))

        panorama = Panorama.objects.get(message_dict['pano_id'])
        for region in message_dict['regions']:
            rg = Region()

            rg.panorama = panorama
            rg.region_type = 'N'
            rg.detected_by = region[-1]

            left_top, right_top, right_bottom, left_bottom = region[0:4]

            rg.left_top_x = left_top[0]
            rg.left_top_y = left_top[1]
            rg.right_top_x = right_top[0]
            rg.right_top_y = right_top[1]
            rg.right_bottom_x = right_bottom[0]
            rg.right_bottom_y = right_bottom[1]
            rg.left_bottom_x = left_bottom[0]
            rg.left_bottom_y = left_bottom[1]

            rg.save()

        region_writer(panorama, lp=True, detected_by=message_dict['detected_by'])

        log.warn("     Licenseplate done! %r" % message_dict['pano_id'])