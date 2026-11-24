# Elevating Semantics

Aerial vision-and-dialog navigation research built on the Target-Grounded Graph-Aware Transformer (TG-GAT). The task, Aerial Navigation from Dialog History (ANDH), asks a simulated drone to find a destination using aerial images, its heading, and a conversation with a human guide. [AVDN benchmark paper](https://arxiv.org/abs/2205.12219)

**Shaurya Kishore Panwar, Ajeet Kumar, and Anil Singh Parihar** · Delhi Technological University

[Read the project report](docs/elevating-semantics.pdf)

## Method

The report replaces TG-GAT's visual feature extractor with a YOLOv9 backbone based on the Generalized Efficient Layer Aggregation Network (GELAN) and Programmable Gradient Information (PGI). Multi-head cross-attention aligns the aerial features with RoBERTa dialog embeddings. A graph-aware transformer uses observations from earlier steps to predict navigation actions, with auxiliary heads for target grounding and human attention. [Project report, §3](docs/elevating-semantics.pdf#page=2) · [YOLOv9 paper](https://arxiv.org/abs/2402.13616)

## Reported results

| Model | Seen SPL ↑ | Seen SR ↑ | Seen GP ↑ | Unseen SPL ↑ | Unseen SR ↑ | Unseen GP ↑ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| HAA-LSTM | 11.6 | 13.0 | 50.3 | 18.3 | 20.0 | 54.4 |
| HAA-Transformer | 14.7 | 17.3 | 56.3 | 16.5 | 20.4 | 55.2 |
| TG-GAT | 15.2 | 18.3 | 58.5 | 18.4 | 22.6 | 54.3 |
| **Elevating Semantics** | 14.3 | **18.7** | **59.8** | 17.8 | **23.3** | **57.9** |

The proposed model improves success rate (SR) and goal progress (GP) over TG-GAT on both validation splits. TG-GAT scores higher on success weighted by path length (SPL) on both splits. [Project report, Table 2](docs/elevating-semantics.pdf#page=5)

## Code availability

This checkout contains the upstream TG-GAT variants and experimental backbones including YOLOv8, SwiftFormer, and ViT. The reported YOLOv9/GELAN/PGI integration and its trained checkpoint are absent from this checkout, so the commands below run the inherited baseline. [Experiment sources](src/) · [Upstream TG-GAT training logs](tg-gat-logs/)

The YOLOv5x variants load `models/yolov5x_backbone.pth` from their experiment directory. [Converted xView-pretrained YOLOv5x weights](https://drive.google.com/file/d/1G3m2KTKt3EWnvR24d5fZlLnjisADzkzp/view)

## Run the image-augmentation baseline

The baseline uses Python 3.8 and a CUDA-capable NVIDIA GPU. From the repository root, install the original PyTorch versions and the baseline dependencies.

```bash
python3.8 -m venv .venv
source .venv/bin/activate
python -m pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 \
  --extra-index-url https://download.pytorch.org/whl/cu113
python -m pip install -r requirements.txt albumentations==1.3.1
```

1. Place the xView imagery (`.tif` files) in `datasets/AVDN/train_images/`. [xView download](https://challenge.xviewdataset.org/data-download)
2. Place `train_data.json`, `val_seen_data.json`, and `val_unseen_data.json` in `datasets/AVDN/annotations/`. Add `test_unseen_data.json` if you plan to generate a test submission. [AVDN downloads](https://sites.google.com/view/aerial-vision-and-dialog/home) · [Dataset guide](datasets/README.md)
3. Place the xView-pretrained YOLOv3 files `best.pt` and `yolo_v3.cfg` in `datasets/AVDN/pretrain_weights/`. [Upstream AVDN weight downloads](https://github.com/UCSB-AI/Aerial-Vision-and-Dialog-Navigation#training-and-evaluation)

Run the launcher from its experiment directory so its relative paths resolve.

```bash
cd src/0_et_imga
bash train.sh
```

The launcher uses GPU 0 and writes checkpoints, training logs, and predictions under the experiment's `logs/` directory. The first run also fetches the pretrained `bert-base-uncased` text model. [Baseline launcher](src/0_et_imga/train.sh)

## Citation and credits

When citing the project, use the authors and title listed in the [project report](docs/elevating-semantics.pdf).

> Shaurya Kishore Panwar, Ajeet Kumar, and Anil Singh Parihar. *Elevating Aerial Vision-Language Navigation with enhanced feature extraction backbone using GELAN and PGI*.

This project builds on [TG-GAT](https://arxiv.org/abs/2308.11561), [AVDN](https://arxiv.org/abs/2205.12219), [DUET](https://github.com/cshizhe/VLN-DUET), and [YOLOv9](https://arxiv.org/abs/2402.13616).
