# Autonomous Driving Perception Stack

## 1. Project Overview

The Autonomous Driving Perception Stack is a computer vision project designed to analyze road scenes and identify important driving information using AI and deep learning techniques.

The system integrates object detection, object tracking, lane detection, semantic segmentation and depth estimation into a unified perception pipeline.

## 2. Objectives

- Detect vehicles, pedestrians and other road objects.
- Track detected objects.
- Identify road lanes.
- Perform semantic segmentation.
- Estimate relative scene depth.
- Integrate perception modules into a single pipeline.
- Optimize models using ONNX.
- Evaluate model performance.

## 3. Technologies Used

- Python
- PyTorch
- YOLOv8
- OpenCV
- SegFormer
- MiDaS
- NumPy
- ONNX
- Pytest
- Visual Studio Code

## 4. Project Structure

```text
Autonomous-Driving-Perception/
│
├── datasets/
│   ├── bus.jpg
│   └── road.jpg
│
├── docs/
├── models/
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
│   ├── lane_detection/
│   ├── lane_segmentation/
│   ├── object_detection/
│   ├── object_tracking/
│   └── optimization/
│       ├── benchmark.py
│       ├── export_onnx.py
│       └── pipeline.py
│
├── tests/
│   └── test_pipeline.py
│
├── requirements.txt
├── yolov8n.pt
├── yolov8.onnx
└── README.md
```

## 5. Installation

Activate the virtual environment:

```bash
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## 6. Running the Modules

### Object Detection

```bash
python src/object_detection/detect.py
```

### Object Tracking

```bash
python src/object_tracking/track.py
```

### Lane Detection

```bash
python src/lane_detection/lane.py
```

### Depth Estimation

```bash
python src/depth_estimation/depth.py
```

### Semantic Segmentation

```bash
python src/lane_segmentation/segmentation.py
```

### Model Optimization

```bash
python src/optimization/export_onnx.py
```

### Benchmarking

```bash
python src/optimization/benchmark.py
```

## 7. Running the Complete Pipeline

Execute:

```bash
python simulator/src/perception_pipeline.py
```

The pipeline integrates the major perception modules and generates output images.

## 8. Video Simulation

Execute:

```bash
python simulator/src/video_simulator.py
```

The simulator supports camera-based perception testing.

## 9. Testing

Run:

```bash
python -m pytest tests -v
```

## 10. Results

The project generates the following outputs:

- Object detection results
- Object tracking results
- Lane detection visualization
- Semantic segmentation results
- Depth estimation visualization
- Edge detection output
- Integrated perception result

## 11. Model Optimization

YOLOv8n is exported to ONNX format for model deployment and benchmarking.

The project compares PyTorch and ONNX inference performance.

## 12. Conclusion

The Autonomous Driving Perception Stack demonstrates the integration of multiple computer vision techniques into a unified autonomous driving perception system.

The project provides practical experience in deep learning, computer vision, model optimization, testing and real-time perception workflows.