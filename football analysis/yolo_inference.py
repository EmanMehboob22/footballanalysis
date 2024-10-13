from ultralytics import YOLO

model = YOLO("/home/ahmed/football analysis/weights/best.pt")
results = model.predict ("/home/ahmed/football analysis/videos/08fd33_4.mp4", save = True)

print(results[0])

print("----------------------------------")


for box in results[0].boxes:
    print (box)
