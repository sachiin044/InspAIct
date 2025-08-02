# model.py

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import sys
import torch

# Add PatchCore repo path
patchcore_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../patchcore-inspection/src"))
sys.path.insert(0, patchcore_path)

from patchcore.patchcore import PatchCore
import patchcore.backbones as backbones

def load_patchcore_model(device=torch.device("cpu")):
    backbone_name = "resnet18"
    backbone, feature_dimensions = backbones.load(backbone_name)

    model = PatchCore(device=device)
    model.load(
        backbone=backbone,
        layers_to_extract_from=["layer2", "layer3"],
        device=device,
        input_shape=(3, 256, 256),
        pretrain_embed_dimension=feature_dimensions,
        target_embed_dimension=1024,  # standard latent size
    )
    
    print("✅ PatchCore model loaded successfully")
    return model

if __name__ == "__main__":
    load_patchcore_model()
