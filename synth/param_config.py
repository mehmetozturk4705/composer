class ParamConfig:
    def __init__(self):
        self.__param_config = {}
        self.__config_schema = {}
        self.__param_defaults = {}

    def get_config_param(self, param_name: str):
        if param_name not in self.__param_config and param_name in self.__config_schema:
            if param_name in self.__param_defaults:
                return self.__param_defaults[param_name]
            elif self.__config_schema[param_name] == float:
                return 0.0
            elif self.__config_schema[param_name] == int:
                return 0

        return self.__param_config[param_name]

    def set_config_param(self, param_name: str, param_value):
        if param_name not in self.__config_schema:
            raise Exception(f"Invalid parameter name {param_name}")
        if not isinstance(param_value, self.__config_schema.get(param_name)):
            raise Exception(f"Invalid type for parameter {param_name}")
        self.__param_config[param_name] = param_value

    def set_config_schema(self, schema: dict):
        validation_errors = self.__validate_config_schema(schema)
        if len(validation_errors) > 0:
            raise Exception(validation_errors)
        self.__config_schema = schema

    def __validate_config_schema(self, config_schema: dict):
        validation_errors = []
        for param_name, param_schema in config_schema.items():
            if param_schema not in [float, int]:
                validation_errors.append(f"Invalid schema for parameter {param_name}")
        return validation_errors
