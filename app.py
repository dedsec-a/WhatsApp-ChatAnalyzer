from utils.data_visualization import plot_values
from logger.logging import logging 
from logger.exception import CustomException
import sys

try :
    x = [2,3,4,5,6]
    y = [23,34,45,56,67]

    plot_values(x=x , y= y)
    logging.info("build a basic plot using matplot lib")
    logging.info("This is the Second Build")

except Exception as e :
    logging.info("Divide By Zero")
    raise CustomException(e,sys)
finally:
    logging.shutdown()

