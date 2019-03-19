from unittest import TestCase

import WarbleSimulation.System.SpaceFactor as SpaceFactor
from WarbleSimulation.util import Logger
from WarbleSimulationTest import test_settings


class TestSpaceFactor(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger = Logger.get_logger(__name__)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.logger.info('')
        self.logger.info(test_settings.start_title_format(self._testMethodName))

        # Define the default dimension and resolution
        self.dimension = (5, 5, 5)
        self.resolution = 3

    def tearDown(self):
        self.logger.info(test_settings.end_title_format(self._testMethodName))
        self.logger.info('')

    # Enum Total
    def test_space_factor_enum_total(self):
        space_factors = SpaceFactor.SpaceFactor

        total_enum = len(space_factors)

        print('Total SpaceFactor = %d' % total_enum)
        print('List = %s' % [i for i in space_factors])

        self.assertEqual(total_enum, 5)

    def test_matter_enum_total(self):
        total_enum = len(SpaceFactor.Matter)
        self.assertEqual(total_enum, 1)

    def test_matter_type_enum_total(self):
        total_enum = len(SpaceFactor.MatterType)
        self.assertEqual(total_enum, 12)

    def test_temperature_enum_total(self):
        total_enum = len(SpaceFactor.Temperature)
        self.assertEqual(total_enum, 1)

    def test_humidity_enum_total(self):
        total_enum = len(SpaceFactor.Humidity)
        self.assertEqual(total_enum, 1)

    def test_luminosity_enum_total(self):
        total_enum = len(SpaceFactor.Luminosity)
        self.assertEqual(total_enum, 3)

    def test_air_movement_enum_total(self):
        total_enum = len(SpaceFactor.AirMovement)
        self.assertEqual(total_enum, 3)

    # generate()
    def test_generate_valid(self):
        for space_factor_type in SpaceFactor.SpaceFactor:
            print(space_factor_type)

            space_factor = SpaceFactor.generate(space_factor_type, self.dimension, self.resolution)

            print('- Testing space_factor has correct keys ...')
            if space_factor_type == SpaceFactor.SpaceFactor.MATTER:
                self.assertEqual(list(space_factor.keys()), [i for i in SpaceFactor.Matter])
            elif space_factor_type == SpaceFactor.SpaceFactor.TEMPERATURE:
                self.assertEqual(list(space_factor.keys()), [i for i in SpaceFactor.Temperature])
            elif space_factor_type == SpaceFactor.SpaceFactor.HUMIDITY:
                self.assertEqual(list(space_factor.keys()), [i for i in SpaceFactor.Humidity])
            elif space_factor_type == SpaceFactor.SpaceFactor.LUMINOSITY:
                self.assertEqual(list(space_factor.keys()), [i for i in SpaceFactor.Luminosity])
            elif space_factor_type == SpaceFactor.SpaceFactor.AIR_MOVEMENT:
                self.assertEqual(list(space_factor.keys()), [i for i in SpaceFactor.AirMovement])
            else:
                raise Exception('Unknown SpaceFactor: %s' % space_factor_type)

            print('- Testing each space factor matrices ...')
            for key, value in space_factor.items():
                self.assertEqual(value.shape, tuple([i * self.resolution for i in self.dimension]))

            print()
