import cv2
import dlib
import numpy as np

class FocusMonitor:
    def __init__(self, threshold=0.25):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(
            "shape_predictor_68_face_landmarks.dat"  # download required model
        )
        self.threshold = threshold  # eye aspect ratio threshold
        self.focus_score = 100      # start with 100%

    def eye_aspect_ratio(self, eye):
        # compute EAR = (||p2-p6|| + ||p3-p5||) / (2*||p1-p4||)
        A = np.linalg.norm(eye[1] - eye[5])
        B = np.linalg.norm(eye[2] - eye[4])
        C = np.linalg.norm(eye[0] - eye[3])
        ear = (A + B) / (2.0 * C)
        return ear

    def monitor_focus(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.detector(gray)

            for face in faces:
                landmarks = self.predictor(gray, face)
                landmarks_points = np.array(
                    [[p.x, p.y] for p in landmarks.parts()]
                )

                left_eye = landmarks_points[36:42]
                right_eye = landmarks_points[42:48]

                left_ear = self.eye_aspect_ratio(left_eye)
                right_ear = self.eye_aspect_ratio(right_eye)
                ear = (left_ear + right_ear) / 2.0

                if ear < self.threshold:
                    self.focus_score -= 1
                else:
                    self.focus_score = min(100, self.focus_score + 0.1)

                cv2.putText(frame, f"Focus Score: {int(self.focus_score)}", 
                            (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 
                            (0, 255, 0), 2)

            cv2.imshow("Focus Monitor", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    fm = FocusMonitor()
    fm.monitor_focus()

