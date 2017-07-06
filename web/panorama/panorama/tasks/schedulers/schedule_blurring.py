import logging
import time

from panorama.tasks.mixins import PanoramaTableAware
from panorama.tasks.queue import BaseScheduler
from datasets.panoramas.models import Panorama, Region
from panorama.regions import blur

log = logging.getLogger(__name__)


class BlurScheduler(BaseScheduler, PanoramaTableAware):
    _route_out = 'blur_task'

    def schedule(self):
        with self.panorama_table_present():
            while True:
                self.queue_result()
                time.sleep(15)

    def get_messages(self):
        messages = []
        for panorama in Panorama.detected_3.all()[:100]:
            log.info("Sending blur task: {}".format(panorama.pano_id))
            regions = []
            for region in Region.objects.filter(pano_id=panorama.pano_id).all():
                regions.append(blur.dict_from(region))

            messages.append({'pano_id': panorama.pano_id,
                             'panorama_path': panorama.get_intermediate_url(),
                             'regions': regions})

            panorama.status = Panorama.STATUS.blurring
            panorama.save()

        return messages
