# Museum_attendance

ML Model to correlate the tourist attendance at their museums with the population of the respective cities.

## Deployement

In order to build the image in Docker run the following scrip
```python
run ./deploy.sh
```
Or you can simply pull the image 

```python
docker pull francoismasson/museum_attendance_prediction:latest
```

## Results

The model can be visualized after building the image
```python
docker run -d -p 80:80 --name museum-attendance-api museum-attendance-ml-build
```
See the results at http://127.0.0.1:5000/docs
