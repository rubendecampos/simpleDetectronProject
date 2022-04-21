from statistics import mode
from Detector import *

# MODFIY THE MODEL TYPE TO GET OTHER RESULTS
detector = Detector(model_type = "IS")

detector.onImage("./images/1.jpg")
