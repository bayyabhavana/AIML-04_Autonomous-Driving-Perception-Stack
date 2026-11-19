
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

from ultralytics import YOLO

import cv2
import traceback
from pathlib import Path


class PerceptionNode(Node):

    def __init__(self):
        super().__init__("autonomous_perception_node")

        self.bridge = CvBridge()

        # Find YOLO model in the perception_ws folder
        workspace_path = Path(__file__).resolve().parents[2]
        model_path = workspace_path / "yolov8n.pt"

        if not model_path.exists():
            raise FileNotFoundError(
                f"YOLO model not found: {model_path}"
            )

        # Load YOLO model
        self.model = YOLO(str(model_path))

        self.get_logger().info("YOLO model loaded successfully")

        # Subscribe to camera images
        self.subscription = self.create_subscription(
            Image,
            "/camera/image_raw",
            self.image_callback,
            10
        )

        # Publish processed images
        self.publisher = self.create_publisher(
            Image,
            "/perception/image",
            10
        )

        self.get_logger().info(
            "Autonomous Driving Perception Node started"
        )

        self.get_logger().info(
            "Waiting for camera images..."
        )

        self.error_reported = False

    def image_callback(self, msg):

        try:
            # Convert ROS image message to OpenCV image
            frame = self.bridge.imgmsg_to_cv2(
                msg,
                desired_encoding="bgr8"
            )

            if frame is None or frame.size == 0:
                raise ValueError("Received an empty camera image")

            # Run YOLO object detection
            results = self.model.predict(
                source=frame,
                conf=0.25,
                verbose=False
            )

            # Draw detection boxes and labels
            annotated_frame = results[0].plot()

            # Convert processed image back to ROS message
            output_msg = self.bridge.cv2_to_imgmsg(
                annotated_frame,
                encoding="bgr8"
            )

            output_msg.header = msg.header

            # Publish processed image
            self.publisher.publish(output_msg)

            # Log detection count
            object_count = len(results[0].boxes)

            self.get_logger().info(
                f"Objects detected: {object_count}"
            )

            self.error_reported = False

        except Exception as error:

            if not self.error_reported:
                self.get_logger().error(
                    f"ERROR TYPE: {type(error).__name__}"
                )

                self.get_logger().error(
                    f"ERROR DETAILS: {repr(error)}"
                )

                self.get_logger().error(
                    traceback.format_exc()
                )

                self.error_reported = True


def main(args=None):

    rclpy.init(args=args)

    node = None

    try:
        node = PerceptionNode()
        rclpy.spin(node)

    except KeyboardInterrupt:
        print("Perception node stopped by user")

    except Exception:
        traceback.print_exc()

    finally:
        if node is not None:
            node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
