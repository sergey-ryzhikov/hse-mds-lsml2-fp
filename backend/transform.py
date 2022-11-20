import random
import torch
import time
import numpy as np

import logging


from celery import Celery
from pathlib import Path
from PIL import Image

from srgan_model import Generator


MODEL_PATH = "./model.pt"
RESULTS_PATH = '/site-data/results/'  # TODO: env

results_path = Path(RESULTS_PATH)

celery = Celery(
    "transform",
    broker="redis://redis",
    backend="redis://redis"
)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")




def load_model():
    model = Generator(img_feat = 3, n_feats = 64, kernel_size = 3, num_block = 16);
    model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
    model = model.to(device)
    model.eval();
    return model



def eval_image(model, file_path):
    img = np.array(Image.open(file_path))
    batch1 = torch.tensor(((img / 127.5) - 1.0).transpose(2, 0, 1).astype(np.float32)).unsqueeze(0).to(device)
    with torch.no_grad():
        output, _ = model(batch1)
    output = output[0].cpu().detach().numpy()
    output = (output + 1.0) / 2.0
    output = output.transpose(1,2,0)
    result = Image.fromarray((output * 255.0).astype(np.uint8))
    return result


@celery.task(name='transform', autoregister=True)  # named task
def transform(file_path, *args):
    model = load_model()
    image = eval_image(model, file_path)
    filename = str(Path(file_path).name)
    save_path = results_path / filename[:2] / filename
    save_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(save_path)
    # TODO: make the filename less predictable
    file_url = '/results/' + filename[:2] + '/' + filename
    return {'result-url': file_url}
