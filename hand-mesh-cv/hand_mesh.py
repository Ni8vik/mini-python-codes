"""
Hand Mesh Detection using MediaPipe
Detects human hands and draws a mesh overlay on live camera feed.
MediaPipe Tasks API only (no legacy `mediapipe.solutions` dependency).
"""

import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.vision import HandLandmarksConnections


class HandMeshDetector:
    """Detects hand landmarks and draws mesh overlay."""

    def __init__(self, max_hands=4, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        """Initialize MediaPipe hand detection."""
        base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')

        # Use IMAGE mode for frame-by-frame processing
        options_static = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=max_hands,
            min_hand_detection_confidence=min_detection_confidence,
            min_hand_presence_confidence=min_tracking_confidence,
            min_tracking_confidence=min_tracking_confidence,
            running_mode=vision.RunningMode.IMAGE
        )

        self.detector = vision.HandLandmarker.create_from_options(options_static)
        self._frame_count = 0

    def detect(self, frame):
        """Detect hands in a frame. Returns annotated frame and hand data."""
        # Convert to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create MediaPipe image
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

        # Detect hands
        result = self.detector.detect(mp_image)

        hand_data = []

        # Draw hand landmarks
        if result.hand_landmarks:
            for hand_landmarks in result.hand_landmarks:
                # Extract landmark points
                landmarks = []
                for landmark in hand_landmarks:
                    landmarks.append({
                        'x': landmark.x,
                        'y': landmark.y,
                        'z': landmark.z
                    })
                hand_data.append(landmarks)

                # Draw on frame
                self._draw_hand_mesh(frame, hand_landmarks)

        return frame, hand_data

    def _draw_hand_mesh(self, frame, hand_landmarks):
        """Draw hand mesh on the frame using manual OpenCV drawing."""
        h, w = frame.shape[:2]

        # Convert normalized landmarks to pixel coordinates
        points = [(int(lm.x * w), int(lm.y * h)) for lm in hand_landmarks]

        # Draw connections between landmarks
        for connection in HandLandmarksConnections.HAND_CONNECTIONS:
            start_idx = connection.start
            end_idx = connection.end
            cv2.line(frame, points[start_idx], points[end_idx], (0, 255, 0), 2)

        # Draw landmark points
        for point in points:
            cv2.circle(frame, point, 4, (0, 0, 255), -1)

    def close(self):
        """Release resources."""
        self.detector.close()


def main():
    """Run hand mesh detection on live camera feed."""
    detector = HandMeshDetector()

    # Open default camera (0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera")
        return

    print("Press 'q' to quit")
    print("Hand mesh detection running...")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to read frame")
                break

            # Flip frame horizontally for selfie view
            frame = cv2.flip(frame, 1)

            # Detect hands and draw mesh
            annotated_frame, hand_data = detector.detect(frame)

            # Display hand count
            if hand_data:
                cv2.putText(
                    annotated_frame,
                    f"Hands detected: {len(hand_data)}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

            # Show frame
            cv2.imshow('Hand Mesh Detection', annotated_frame)

            # Exit on 'q' press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        detector.close()
        print("Resources released")


if __name__ == "__main__":
    main()
