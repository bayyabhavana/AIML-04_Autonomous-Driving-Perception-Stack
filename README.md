# Autonomous Driving Perception System

## Project Overview

The Autonomous Driving Perception System is a computer vision-based project designed to analyze road environments and identify important driving conditions using deep learning and image processing techniques.

The system integrates object detection, object tracking, lane detection, semantic segmentation and monocular depth estimation into a unified perception pipeline.

## Key Features

- **Object Detection:** YOLOv8 for detecting vehicles and other road objects.
- **Object Tracking:** Tracking detected objects across video frames.
- **Lane Detection:** Identifying road lane boundaries using OpenCV.
- **Semantic Segmentation:** SegFormer-B0 for road scene segmentation.
- **Depth Estimation:** MiDaS for estimating relative depth from images.
- **Model Optimization:** Exporting YOLOv8 to ONNX format.
- **Performance Benchmarking:** Comparing PyTorch and ONNX inference performance.
- **Perception Pipeline:** Integrating multiple perception modules.

## Technologies Used

- Python
- PyTorch
- YOLOv8
- OpenCV
- Hugging Face Transformers
- SegFormer
- MiDaS
- ONNX
- NumPy
- Matplotlib
- Pytest

## Project Architecture

```text
Autonomous-Driving-Perception/
│
├── datasets/
│   ├── bus.jpg
│   └── road.jpg
│
├── models/
│   └── yolov8n.onnx
│
├── outputs/
│
├── simulator/
│   ├── docs/
│   ├── outputs/
│   ├── recordings/
│   └── src/
│       ├── perception_pipeline.py
│       └── video_simulator.py
│
├── src/
│   ├── depth_estimation/
│   │   └── depth.py
│   ├── lane_detection/
│   │   └── lane.py
│   ├── lane_segmentation/
│   │   └── segmentation.py
│   ├── object_detection/
│   │   └── detect.py
│   ├── object_tracking/
│   │   └── track.py
│   └── optimization/
│       ├── benchmark.py
│       └── export_onnx.py
│
├── tests/
│   └── test_pipeline.py
│
├── requirements.txt
├── README.md
├── .gitignore
├── yolov8n.pt
└── yolov8n.onnx
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/bayyabhavana/Autonomous-Driving-Perception.git
```

### 2. Navigate to the Project

```bash
cd Autonomous-Driving-Perception
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

## Execution

Run individual modules:

**Object Detection**
```bash
python src/object_detection/detect.py
```

**Object Tracking**
```bash
python src/object_tracking/track.py
```

**Lane Detection**
```bash
python src/lane_detection/lane.py
```

**Semantic Segmentation**
```bash
python src/lane_segmentation/segmentation.py
```

**Depth Estimation**
```bash
python src/depth_estimation/depth.py
```

**ONNX Export**
```bash
python src/optimization/export_onnx.py
```

**Benchmarking**
```bash
python src/optimization/benchmark.py
```

**Integrated Perception Pipeline**
```bash
python simulator/src/perception_pipeline.py
```

## Performance Benchmark Results

| Model | Average Latency | FPS |
|---|---:|---:|
| PyTorch YOLOv8n | 68.44 ms | 14.61 |
| ONNX YOLOv8n | 168.24 ms | 5.94 |

*Benchmark results obtained in the project's CPU environment. Performance depends on hardware and execution conditions.*

## Testing

Run the project tests:

```bash
python -m pytest tests -v
```

Test results:

- Bus image existence – Passed
- Road image existence – Passed
- Bus image loading – Passed
- Road image loading – Passed

**Total: 4 tests passed.**

## Output Results

The integrated pipeline generates:

- perception_result.jpg
- depth_result.jpg
- lane_result.jpg
- edge_result.jpg

Additional outputs are saved in their respective module output folders.

## Hardware and Environment

- Operating System: Windows 11
- Python: 3.13.5
- Execution Device: CPU
- Processor Graphics: Intel HD Graphics 620

## Project Objective

The objective of this project is to develop an integrated autonomous driving perception pipeline capable of understanding road environments through computer vision and deep learning.

## Author

**Bhavana Goud**

GitHub: https://github.com/bayyabhavana

## License

This project is intended for educational and research purposes.