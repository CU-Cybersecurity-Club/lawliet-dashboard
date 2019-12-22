import os
import random

from django.test import TestCase
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from dashboard.models import LabEnvironment

from dashboard.tests.utils import random_docker_image

BASE_DIR = settings.BASE_DIR

STATIC_IMG_PATH = os.path.join(BASE_DIR, "assets", "img")
STATIC_IMG_PATH = os.path.abspath(STATIC_IMG_PATH)

"""
---------------------------------------------------
LabEnvironment tests
---------------------------------------------------
"""


class LabEnvironmentTestCase(TestCase):
    def setUp(self):
        self.rd = random.Random()
        self.rd.seed(0)

        with open(os.path.join(STATIC_IMG_PATH, "cutter.svg"), "rb") as img:
            self.cutter_image = SimpleUploadedFile(
                name="cutter.svg", content=img.read(), content_type="image/svg"
            )

        labenv = LabEnvironment.objects.create(
            name="Cutter + Radare2",
            description="Cutter & Radare2 desktop",
            url=random_docker_image(self.rd),
            header_image=self.cutter_image,
        )
        print(labenv.url)

    def test_can_retrieve_basic_environment(self):
        cutter_lab = LabEnvironment.objects.get(name="Cutter + Radare2")
        path = cutter_lab.header_image.path
        self.assertEqual(cutter_lab.description, "Cutter & Radare2 desktop")
        self.assertTrue(path.startswith(settings.MEDIA_ROOT))
        self.assertTrue(
            path.startswith(os.path.join(settings.MEDIA_ROOT, "labs", "img"))
        )
