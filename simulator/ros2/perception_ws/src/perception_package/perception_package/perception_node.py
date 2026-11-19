import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from pathlib import Path

import cv2
import numpy as np
from ultralytics import YOLO


class PerceptionNode(Node):

    def __init__(self):
        super().__init__("autonomous_perception_node")

        self.declare_parameter("image_topic", "/camera/image_raw")
        self.declare_parameter("output_topic", "/camera/image_processed")
        self.declare_parameter("confidence", 0.35)
        self.declare_parameter("image_size", 416)

        self.image_topic = self.get_parameter("image_topic").value
        self.output_topic = self.get_parameter("output_topic").value
        self.confidence = float(self.get_parameter("confidence").value)
        self.image_size = int(self.get_parameter("image_size").value)

        # Project model location
        model_path = Path(
            "/mnt/d/Autonomous-Driving-Perception/"
            "simulator/ros2/perception_ws/yolov8n.pt"
        )

        if not model_path.exists():
            raise FileNotFoundError(
                f"YOLO model not found: {model_path}"
            )

        self.get_logger().info(f"Loading YOLO model: {model_path}")
        self.model = YOLO(str(model_path))
        self.get_logger().info("YOLO model loaded successfully")

        self.publisher = self.create_publisher(
            Image, self.output_topic, 10
        )

        self.subscription = self.create_subscription(
            Image,
            self.image_topic,
            self.image_callback,
            10
        )

        self.frame_count = 0

        self.get_logger().info("AUTONOMOUS PERCEPTION NODE STARTED")
        self.get_logger().info(f"Subscribed: {self.image_topic}")
        self.get_logger().info(f"Publishing: {self.output_topic}")

    def convert_image(self, msg):
        height = msg.height
        width = msg.width
        encoding = msg.encoding.lower()

        if height <= 0 or width <= 0:
            raise ValueError("Invalid image dimensions")

        if encoding in ("bgr8", "rgb8"):
            channels = 3
        elif encoding in ("bgra8", "rgba8"):
            channels = 4
        elif encoding in ("mono8", "8uc1"):
            channels = 1
        else:
            raise ValueError(f"Unsupported encoding: {encoding}")

        rows = np.frombuffer(
            msg.data, dtype=np.uint8
        ).reshape(height, msg.step)

        image = rows[:, :width * channels].reshape(
            height, width, channels
        ).copy() if channels > 1 else rows[:, :width].copy()

        if encoding == "rgb8":
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        elif encoding == "rgba8":
            image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
        elif encoding == "bgra8":
            image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        elif channels == 1:
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

        return image

    def image_callback(self, msg):
        try:
            frame = self.convert_image(msg)

            results = self.model.predict(
                source=frame,
                conf=self.confidence,
                imgsz=self.image_size,
                device="cpu",
                verbose=False
            )

            annotated = results[0].plot()
            detected = len(results[0].boxes)

            output = Image()
            output.header = msg.header
            output.height = annotated.shape[0]
            output.width = annotated.shape[1]
            output.encoding = "bgr8"
            output.is_bigendian = 0
            output.step = annotated.shape[1] * 3
            output.data = np.ascontiguousarray(
                annotated
            ).tobytes()

            self.publisher.publish(output)

            self.frame_count += 1

            if self.frame_count % 5 == 0:
                self.get_logger().info(
                    f"Frames processed: {self.frame_count} | "
                    f"Objects detected: {detected}"
                )

        except Exception as error:
            self.get_logger().error(
                f"Processing error: {type(error).__name__}: {error}"
            )


def main(args=None):
    rclpy.init(args=args)
    node = None

    try:
        node = PerceptionNode()
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    except Exception as error:
        print(f"NODE FAILED: {type(error).__name__}: {error}")
        raise

    finally:
        if node is not None:
            node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
