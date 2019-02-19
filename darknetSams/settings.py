import os

DARKNET_ROOT = os.path.dirname(os.path.abspath(__file__))
logo_conf_list = [
    {
        "config": os.path.join(DARKNET_ROOT, "cfg", "yolov3_100item_56_layer.cfg"),
        "meta": os.path.join(DARKNET_ROOT, "cfg", "Logo.data"),
        "weight": os.path.join(DARKNET_ROOT, "weights", "yolov3_100item_56_layer_190693.weights")
    }
]

logo_conf = logo_conf_list[0]