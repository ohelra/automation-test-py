import cv2
import numpy as np
import requests


DLC_LOCATION_ANCHORS = {
    "1": (0.2481077994, 0.4381648846),
    "2": (0.1145911526, 0.4381371693),
    "3": (0.3760119438, 0.4381585382),
    "4": (0.3436500147, 0.2118977501),
    "5": (0.1485144170, 0.2119480810),
    "6": (0.4937240021, 0.3904173776),
    "7": (0.6011288311, 0.3899012509),
    "8": (0.5474269305, 0.8258057823),
    "9": (0.8041790884, 0.3177962340),
}


def detect_highlighted_dlc_location(image_bytes):
    """Return the DLC number highlighted inside the rendered locator diagram."""
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Could not decode DLC image screenshot")

    height, width = image.shape[:2]
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    blue_mask = cv2.inRange(
        hsv,
        np.array([90, 40, 40]),
        np.array([130, 255, 255]),
    )

    min_area = max(100, int(height * width * 0.005))
    label_count, _, stats, centroids = cv2.connectedComponentsWithStats(blue_mask)
    candidates = []
    for label_index in range(1, label_count):
        area = stats[label_index][4]
        if area >= min_area:
            candidates.append((area, centroids[label_index]))

    if not candidates:
        raise ValueError("Could not detect a highlighted DLC location marker in the image")

    area, centroid = max(candidates, key=lambda candidate: candidate[0])
    normalized_centroid = (centroid[0] / width, centroid[1] / height)
    location, distance = min(
        (
            (
                number,
                (
                    (normalized_centroid[0] - anchor[0]) ** 2
                    + (normalized_centroid[1] - anchor[1]) ** 2
                )
                ** 0.5,
            )
            for number, anchor in DLC_LOCATION_ANCHORS.items()
        ),
        key=lambda item: item[1],
    )

    if distance > 0.08:
        raise ValueError(
            f"Detected DLC marker is not close to a known location. "
            f"Centroid={normalized_centroid}, distance={distance:.3f}, area={area}"
        )

    return location


def detect_highlighted_dlc_location_from_url(image_url):
    response = requests.get(image_url, timeout=30)
    response.raise_for_status()
    return detect_highlighted_dlc_location(response.content)
