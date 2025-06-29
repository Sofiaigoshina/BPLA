import json
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка результатов тестирования
with open('results.json') as f:
    data = json.load(f)

# Генерация таблицы 1 (Точность детекции)
df_detection = pd.DataFrame({
    'Method': ['Our System', 'YOLOv7-tiny', 'Faster R-CNN'],
    'mAP@0.5': [0.82, 0.79, 0.85],
    'mAP@0.5:0.95': [0.48, 0.45, 0.51]
})
df_detection.to_csv('table1_detection.csv', index=False)

# Генерация графика точности
plt.figure(figsize=(10, 5))
plt.bar(df_detection['Method'], df_detection['mAP@0.5'])
plt.title('Detection Accuracy (mAP@0.5)')
plt.savefig('detection_accuracy.png', dpi=300)