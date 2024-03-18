## -----------------------YOLO-V5---------------------------------------

----------------------------PYTHON-----------------------------
class yolov5x_backbone(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.add_module('0', Conv(3, 80, 6, 2, 2))
        self.add_module('1', Conv(80, 160, 3, 2))
        self.add_module('2', C3(160, 160, 4))
        self.add_module('3', Conv(160, 320, 3, 2))
        self.add_module('4', C3(320, 320, 8))
        self.add_module('5', Conv(320, 640, 3, 2))
        self.add_module('6', C3(640, 640, 12))
        self.add_module('7', Conv(640, 1280, 3, 2))
        self.add_module('8', C3(1280, 1280, 4))
        self.add_module('9', SPPF(1280, 1280, 5))

    def forward(self, x):
        x = getattr(self, '0')(x)
        x = getattr(self, '1')(x)
        x = getattr(self, '2')(x)
        x = getattr(self, '3')(x)
        x = getattr(self, '4')(x)
        x = getattr(self, '5')(x)
        x = getattr(self, '6')(x)
        x = getattr(self, '7')(x)
        x = getattr(self, '8')(x)
        x = getattr(self, '9')(x)

        return x


-----------------------------YAML--------------------------------------
# YOLOv5 v6.0 backbone
backbone:
  # [from, number, module, args]
  [
    [-1, 1, Conv, [64, 6, 2, 2]], # 0-P1/2
    [-1, 1, Conv, [128, 3, 2]], # 1-P2/4
    [-1, 3, C3, [128]],
    [-1, 1, Conv, [256, 3, 2]], # 3-P3/8
    [-1, 6, C3, [256]],
    [-1, 1, Conv, [512, 3, 2]], # 5-P4/16
    [-1, 9, C3, [512]],
    [-1, 1, Conv, [1024, 3, 2]], # 7-P5/32
    [-1, 3, C3, [1024]],
    [-1, 1, SPPF, [1024, 5]], # 9
  ]



## -----------------------YOLO-V8---------------------------------------
~# Ultralytics YOLO 🚀, AGPL-3.0 license
~# YOLOv8 object detection model with P3-P5 outputs. For Usage examples see https://docs.ultralytics.com/tasks/detect

~# Parameters
nc: 80 # number of classes
scales: # model compound scaling constants, i.e. 'model=yolov8n.yaml' will call yolov8.yaml with scale 'n'
  ~# [depth, width, max_channels]
  n: [0.33, 0.25, 1024] # YOLOv8n summary: 225 layers,  3157200 parameters,  3157184 gradients,   8.9 GFLOPs
  s: [0.33, 0.50, 1024] # YOLOv8s summary: 225 layers, 11166560 parameters, 11166544 gradients,  28.8 GFLOPs
  m: [0.67, 0.75, 768] # YOLOv8m summary: 295 layers, 25902640 parameters, 25902624 gradients,  79.3 GFLOPs
  l: [1.00, 1.00, 512] # YOLOv8l summary: 365 layers, 43691520 parameters, 43691504 gradients, 165.7 GFLOPs
  x: [1.00, 1.25, 512] # YOLOv8x summary: 365 layers, 68229648 parameters, 68229632 gradients, 258.5 GFLOPs

~# YOLOv8.0n backbone
backbone:
  ~# [from, repeats, module, args]
  - [-1, 1, Conv, [64, 3, 2]] # 0-P1/2
  - [-1, 1, Conv, [128, 3, 2]] # 1-P2/4
  - [-1, 3, C2f, [128, True]]
  - [-1, 1, Conv, [256, 3, 2]] # 3-P3/8
  - [-1, 6, C2f, [256, True]]
  - [-1, 1, Conv, [512, 3, 2]] # 5-P4/16
  - [-1, 6, C2f, [512, True]]
  - [-1, 1, Conv, [1024, 3, 2]] # 7-P5/32
  - [-1, 3, C2f, [1024, True]]
  - [-1, 1, SPPF, [1024, 5]] # 9


