import os

import requests
from tqdm import tqdm


def download_trained_weights(url, model_path, verbose=1):
    """Download COCO trained weights from Releases.

    coco_model_path: local path of COCO trained weights
    # """
    if verbose > 0:
        print("Downloading pretrained model to " + model_path + " ...")
    _dir = os.path.dirname(model_path)
    if os.path.isdir(_dir) is False:
        os.makedirs(_dir)

    # Streaming, so we can iterate over the response.
    with requests.get(url, stream=True) as r, open(model_path, 'wb') as f:
        # Total size in bytes.
        total_size = int(r.headers.get('content-length', 0))
        wrote = 0
        for data in tqdm(r.iter_content(), total=total_size, unit='KB',
                         unit_scale=True):
            wrote = wrote + len(data)
            f.write(data)
    if total_size != 0 and wrote != total_size:
        print("ERROR, something went wrong")
    elif verbose > 0:
        print("... done downloading pretrained model!")
