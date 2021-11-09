import unittest


class TestParamConfig(unittest.TestCase):
    def test_param_config(self):
        from synth.param_config import ParamConfig

        # Test ParamConfig
        param_config = ParamConfig()
        with self.assertRaises(Exception):
            param_config.get_config_param('test')

        with self.assertRaises(Exception):
            param_config.set_config_schema({'test': str})

        param_config.set_config_schema({'test': int})
        self.assertEqual(param_config.get_config_param('test'), 0)

        param_config.set_config_schema({'test': float})
        self.assertEqual(param_config.get_config_param('test'), 0.0)

        param_config.set_config_param('test', 1.5)
        self.assertEqual(param_config.get_config_param('test'), 1.5)
