docker build -t museum-attendance-ml-build .
docker tag museum-attendance-ml-build francoismasson/museum_attendance_prediction
docker run -d -p 80:80 --name museum-attendance-api museum-attendance-ml-build