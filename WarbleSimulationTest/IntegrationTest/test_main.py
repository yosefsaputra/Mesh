import filecmp
import os
import uuid
from unittest import TestCase

import WarbleSimulation.System.SpaceFactor as SpaceFactor
from WarbleSimulation.System.Entity.Concrete.AirConditioner import AirConditioner
from WarbleSimulation.System.Entity.Concrete.Light import Light
from WarbleSimulation.System.Entity.Concrete.SmokeDetector import SmokeDetector
from WarbleSimulation.System.Entity.Concrete.Table import Table
from WarbleSimulation.System.Entity.Concrete.Thermostat import Thermostat
from WarbleSimulation.System.Entity.Concrete.Wall import Wall
from WarbleSimulation.System.System import System
from WarbleSimulation.util import Logger, Plotter
from WarbleSimulationTest import test_settings


class TestMain(TestCase):
    def setUp(self):
        self.logger = Logger.get_logger(__name__)

    def test_main(self):
        test_name = 'test_main'

        # Create System
        self.system = System('MyNewSystem')

        # Put Space on the System
        self.system.put_space(dimension=(40, 30, 10), resolution=1,
                              space_factor_types=[i for i in SpaceFactor.SpaceFactor])

        # Put Entity on the Space
        table1 = Table(uuid=uuid.uuid4(), dimension_x=(2, 1, 1))
        self.system.put_entity(table1, (0, 0, 0))
        light1 = Light(uuid=uuid.uuid4(), dimension_x=(1, 1, 1))
        self.system.put_entity(light1, (19, 14, 7))
        ac1 = AirConditioner(uuid=uuid.uuid4())
        self.system.put_entity(ac1, (37, 10, 7), unit_orientation=(-1, 0, 0))
        sd1 = SmokeDetector(uuid=uuid.uuid4())
        self.system.put_entity(sd1, (0, 10, 8), unit_orientation=(1, 0, 0))
        thermostat1 = Thermostat(uuid=uuid.uuid4())
        self.system.put_entity(thermostat1, (30, 0, 5))

        # Compare Space Factor Matter
        self.system.space.space_factors[SpaceFactor.SpaceFactor.MATTER][SpaceFactor.Matter.MATTER].tofile(
            os.path.join(test_settings.actual_path, test_name + '_space_matter.txt'))
        self.assertTrue(filecmp.cmp(os.path.join(test_settings.expected_path, test_name + '_space_matter.txt'),
                                    os.path.join(test_settings.actual_path, test_name + '_space_matter.txt')))

        # Plot
        Plotter.plot_scatter_3d(
            array3d=self.system.space.space_factors[SpaceFactor.SpaceFactor.MATTER][SpaceFactor.Matter.MATTER],
            zero_value=SpaceFactor.MatterType.ATMOSPHERE.value,
            filename=os.path.join(test_settings.actual_path, test_name + '_plot.html'),
            auto_open=test_settings.auto_open)

    def test_main_1(self):
        test_name = 'test_main_1'

        # Create System
        self.system = System('MyNewSystem')

        # Put Space on the System
        self.system.put_space(dimension=(20, 10, 5), resolution=4,
                              space_factor_types=[i for i in SpaceFactor.SpaceFactor])
        self.logger.info('\n' + str(self.system.space))

        # Put Entity on the Space
        # Put Walls
        wall_1 = Wall(uuid=uuid.uuid4(), dimension_x=(20, 0.25, 5))
        self.system.put_entity(wall_1, (0, 9.75, 0))
        wall_2 = Wall(uuid=uuid.uuid4(), dimension_x=(20, 0.25, 5))
        self.system.put_entity(wall_2, (0, 0, 0))
        wall_3 = Wall(uuid=uuid.uuid4(), dimension_x=(0.25, 9.5, 5))
        self.system.put_entity(wall_3, (0, 0.25, 0))
        wall_4 = Wall(uuid=uuid.uuid4(), dimension_x=(0.25, 9.5, 5))
        self.system.put_entity(wall_4, (19.75, 0.25, 0))

        # Compare Space Factor Matter
        self.system.space.space_factors[SpaceFactor.SpaceFactor.MATTER][SpaceFactor.Matter.MATTER].tofile(
            os.path.join(test_settings.actual_path, test_name + '_space_matter.txt'))
        self.assertTrue(filecmp.cmp(os.path.join(test_settings.expected_path, test_name + '_space_matter.txt'),
                                    os.path.join(test_settings.actual_path, test_name + '_space_matter.txt')))

        # Plot
        Plotter.plot_scatter_3d(
            array3d=self.system.space.space_factors[SpaceFactor.SpaceFactor.MATTER][SpaceFactor.Matter.MATTER],
            zero_value=SpaceFactor.MatterType.ATMOSPHERE.value,
            filename=os.path.join(test_settings.actual_path, test_name + '_plot.html'),
            auto_open=test_settings.auto_open)
