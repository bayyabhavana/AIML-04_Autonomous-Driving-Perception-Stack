
import streamlit as st
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUTS = ROOT / "simulator" / "outputs"

st.set_page_config(
    page_title="Autonomous Driving Perception",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Autonomous Driving Perception")
st.subheader("AI-powered Road Scene Analysis")

st.write(
    "A computer vision project demonstrating object detection, "
    "lane detection, segmentation and relative depth estimation."
)

st.info(
    "This website displays previously generated project results. "
    "The full inference pipeline runs locally, not on this website."
)

st.header("Perception Results")

images = [
    ("Object Detection and Lane Detection", "perception_result.jpg"),
    ("MiDaS Relative Depth Map", "depth_result.jpg"),
    ("Lane Detection", "lane_result.jpg"),
    ("Edge Detection", "edge_result.jpg")
]

for title, filename in images:
    path = OUTPUTS / filename
    st.subheader(title)
    if path.exists():
        st.image(str(path), use_container_width=True)
    else:
        st.warning(f"Image not found: {filename}")

st.header("ONNX Performance Benchmark")

benchmark = ROOT / "outputs" / "benchmark" / "benchmark_results.csv"

if benchmark.exists():
    with benchmark.open("r", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))
    if rows:
        st.dataframe(rows, use_container_width=True)
    else:
        st.info("No benchmark records found.")
else:
    st.info("Benchmark results are available in GitHub.")

st.header("KITTI Dataset Analysis")

chart = ROOT / "outputs" / "dataset_analysis" / "kitti_class_distribution.png"

if chart.exists():
    st.image(str(chart), use_container_width=True)
else:
    st.info("KITTI class distribution chart is available in GitHub.")

st.header("Project Technologies")
st.markdown("""
- YOLOv8 object detection
- OpenCV lane detection
- MiDaS relative depth estimation
- SegFormer segmentation experiment
- ROS 2 image communication
- ONNX export and inference
""")

st.caption(
    "Academic project demonstration. "
    "Not a production autonomous-driving system."
)
