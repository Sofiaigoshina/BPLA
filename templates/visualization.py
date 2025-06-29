import cv2


def annotate_frame(frame, detections):
    for det in detections:
        x, y, w, h = det['box']
        label = f"{det['class']} {det['confidence']:.2f}"

        color = (0, 255, 0) if det['class'] == 'car' else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, label, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    return frame


# Пример использования
input_frame = cv2.imread('test_frame.jpg')
detections = [{'box': [100, 100, 200, 200], 'class': 'car', 'confidence': 0.89},
              {'box': [300, 300, 50, 50], 'class': 'shadow', 'confidence': 0.52}]

output_frame = annotate_frame(input_frame.copy(), detections)
cv2.imwrite('result_example.png', output_frame)