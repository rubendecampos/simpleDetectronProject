from statistics import mode
from Detector import *

# MODFIY THE MODEL TYPE TO GET OTHER RESULTS
detector = Detector(model_type = "OD")

detector.onImage("./images/1.jpg")
