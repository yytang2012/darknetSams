import os

DARKNET_ROOT = os.path.dirname(os.path.abspath(__file__))

# Configuration for LOGO model
LOGO_ROOT = os.path.join(DARKNET_ROOT, "modelConfigs", "Logo")
logo_conf_list = [
    {
        "config": os.path.join(LOGO_ROOT, "cfg", "yolov3_100item_56_layer.cfg"),
        "meta": os.path.join(LOGO_ROOT, "cfg", "Logo.data"),
        "weight": os.path.join(LOGO_ROOT, "weights", "yolov3_100item_56_layer_190693.weights"),
        "url": "https://samsshrinkimages.blob.core.windows.net/models/logo/v1/weights/yolov3_100item_56_layer_190693.weights"
    }
]
logo_conf = logo_conf_list[0]

# Configurations for Cart model
CART_ROOT = os.path.join(DARKNET_ROOT, "modelConfigs", "Cart")
cart_conf_list = [
    {
        "config": os.path.join(CART_ROOT, "cfg", "yolov3_cart_resnet.cfg"),
        "meta": os.path.join(CART_ROOT, "cfg", "Cart.data"),
        "weight": os.path.join(CART_ROOT, "weights", "yolov3_cart_resnet_1022828.weights"),
        "url": "https://samsshrinkimages.blob.core.windows.net/models/cart/v1/weights/yolov3_cart_resnet_1022828.weights"
    }
]
cart_conf = cart_conf_list[0]

# Configurations for Coco model
COCO_ROOT = os.path.join(DARKNET_ROOT, "modelConfigs", "Coco")
coco_conf_list = [
    {
        "config": os.path.join(COCO_ROOT, "cfg", "yolov3.cfg"),
        "meta": os.path.join(COCO_ROOT, "cfg", "coco.data"),
        "weight": os.path.join(COCO_ROOT, "weights", "yolov3.weights"),
        "url": "https://pjreddie.com/media/files/yolov3.weights"
    }
]
coco_conf = coco_conf_list[0]