import cv2

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
PINK = (255, 182, 193)


def draw_result(image, detections, limit=10, color=None, thickness=2):
    __image = image.copy()

    for detect in detections:
        class_name, prob, bbox = detect

        up, left, down, right = bbox
        assert type(left) == int and type(right) == int and type(up) == int and type(down) == int
        cv2.rectangle(__image, (left, up), (right, down), BLUE, thickness)
        # cv2.putText(_image, "{}:{}:{}".format(hp, item_id, showup_count), (left, up),
        #             cv2.FONT_HERSHEY_SIMPLEX, 1, RED)

    return __image
