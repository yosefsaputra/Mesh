import os

from MeshTest import test_settings

if not os.path.exists(test_settings.actual_path):
    os.makedirs(test_settings.actual_path)
