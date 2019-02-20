from darknetSams.settings import logo_conf, cart_conf, coco_conf
from darknetSams.yolo import DarknetSams


class Logo(DarknetSams):
    def __init__(self):
        config_path = logo_conf["config"]
        weight_path = logo_conf["weight"]
        meta_path = logo_conf["meta"]
        url = logo_conf["url"]
        super().__init__(config_path=config_path, weight_path=weight_path, meta_path=meta_path, url=url)


class Cart(DarknetSams):
    def __init__(self):
        config_path = cart_conf["config"]
        weight_path = cart_conf["weight"]
        meta_path = cart_conf["meta"]
        url = cart_conf["url"]
        super().__init__(config_path=config_path, weight_path=weight_path, meta_path=meta_path, url=url)


class Coco(DarknetSams):
    def __init__(self):
        config_path = coco_conf["config"]
        weight_path = coco_conf["weight"]
        meta_path = coco_conf["meta"]
        url = coco_conf["url"]
        super().__init__(config_path=config_path, weight_path=weight_path, meta_path=meta_path, url=url)

