from typing import Generator

from synth.param_config import ParamConfig
import numpy as np

from synth.score_writer import ScoreWriter


class BaseSynthesizer:

    def __init__(self):
        self._config_param: ParamConfig = ParamConfig()

    def synthesize(self, input_data: ScoreWriter) -> Generator[np.array, None, None]:
        """
        Synthesize the input data. While synthesizing values, you should yield in shape of (2, CHUNK_SIZE)

        :param input_data:
        :return:
        """
        raise NotImplementedError

    def set_config(self, config: ParamConfig):
        self._config_param = config

    def get_config(self) -> ParamConfig:
        return self._config_param

    def get_config_param(self, param_name: str):
        return self._config_param.get_config_param(param_name)

    def set_config_param(self, param_name: str, param_value):
        self._config_param.set_config_param(param_name, param_value)
