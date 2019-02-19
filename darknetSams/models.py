from darknetSams.settings import logo_conf
from darknetSams.yolo import DarknetSams


class Logo(DarknetSams):
    def __init__(self):
        config_path = logo_conf["config"]
        weight_path = logo_conf["weight"]
        meta_path = logo_conf["meta"]
        super().__init__(config_path=config_path, weight_path=weight_path, meta_path=meta_path)


class Cart(DarknetSams):
    def __init__(self):
        config_path = logo_conf["config"]
        weight_path = logo_conf["weight"]
        meta_path = logo_conf["meta"]
        super().__init__(config_path=config_path, weight_path=weight_path, meta_path=meta_path)


