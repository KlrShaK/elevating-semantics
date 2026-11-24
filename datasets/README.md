# Explore AVDN dataset
Place the AVDN annotations in `datasets/AVDN/annotations/` and the xView images in `datasets/AVDN/train_images/`. Download links and pretrained weight locations are listed in the [project README](../README.md#run-the-image-augmentation-baseline).
```
datasets
├── AVDN
│   ├── annotations
│   │   ├── train_data.json
│   │   ├── val_seen_data.json
│   │   ├── val_unseen_data.json
│   │   ├── test_unseen_data.json
│   ├── pretrain_weights
│   ├── train_images
```

## Splits

We split our AVDN dataset into four splits: train, seen-validation, unseen-validation and unseen-test sets, where seen and unseen sets are pre-separated by making sure the visual scenes from the xView dataset used in the sets are not overlapped. There are in total 6,269 sub-trajectories corresponding to the dialog rounds. Please refer to AVDN paper section 3.4 for more dataset statistics.

## Data structure
For each sub-trajectories, we provide the following data.

* "instructions": the dialog utterance cooresponding to the current sub-trajectory. The dialog utterance is prefixed with `[QUE]` if from the follower and `[INS]` if from the commander.

* "pre_dialogs": a dialog utterance list corresponding to the previous dialog rounds.

* "gps_botm_left" and "gps_top_right": The GPS coordinates i.e. (latitude, longitude) for the bottom left and top right corner of the xView image corresponding to the current sub-trajectory.

* "lng_ratio" and "lat_ratio": a ratio between the GPS coordinates and image pixel coordinates. It is used to convert a GPS coordinate to a pixel coordinate on the image.

* "last_round_idx": total number of sub-trajectoies from the corresponding trajectory.

* "destination": the corners of the destination area in the anti-clock wise order. The corners are GPS coordinates (latitude, longitude).

* "gt_path_corners": the ground truth sub-trajectory represented by a list of view areas. Each view area is represented by GPS coordinates (latitude, longitude) of its four corners in the order of (front left, front right, back right, back left). So the forward direction of the view area can be retrieved. The first view area in the gt_path_corners is the inital view area for the sub-trajectory.

* "attention_list": a list of human attention areas where each area is a round geometry area. The list records the round center in GPS coordinates and the radius in pixel length. 

* "map_name": the name of the corresponding image in xView dataset. 

* "route_index": a unique index to the sub-trajectory in the data split.

* "angle": the direction (degree) of the inital view area. North is 0 degree and East is 90 degree. 

## Visualization
The visualizer opens an OpenCV window for exploring trajectories and dialog. Run it from the repository root after setting up the dataset.

```bash
python datasets/visualize_sub_traj.py \
  --xview_image_path datasets/AVDN/train_images/ \
  --avdn_annotation_path datasets/AVDN/annotations/val_seen_data.json
```
