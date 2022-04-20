#!/usr/bin/env python3



from turtlebro_patrol.srv import PatrolPointCallback, PatrolPointCallbackRequest, PatrolPointCallbackResponse 
from turtlebro_heat_excursion.srv import ArucoDetect, ArucoDetectResponse, ArucoDetectRequest
import rospy
import subprocess

def say_text(text):    
    rospy.loginfo(f"Start speech: {text}")
    subprocess.call('echo '+text+'|festival --tts --language russian', shell=True)
    rospy.loginfo("Speech end")

def handle_request(req:PatrolPointCallbackRequest):

    point_name = req.patrol_point.name
    
    text = "Местоположение неизвестно"
    
    if point_name == "1":
        text = "Наша первая картина"

    elif point_name == "2":
        text = "Наша вторая картина"
    
    elif point_name == "3":
        text = "Наша третья картина"
    elif point_name == "4":
        text = "Наша последняя картина"

    elif point_name == "home":
        text = "Экскурсия окончена всем спасибо"

    aruco_result = aruco_detect.call(ArucoDetectRequest())

    if aruco_result.id > 0:
        if aruco_result.id == 22:
            text += ". Сальвадор Дали Постоянство памяти"
        elif aruco_result.id == 32:
            text += ". Сальвадор Дали Постоянство памяти"
        elif aruco_result.id == 42:
            text += ". Сальвадор Дали Постоянство памяти"
        elif aruco_result.id == 52:
            text += ". Сальвадор Дали Постоянство памяти"

    else : 
        text += ". Картину украли"    

    say_text(text)

    return PatrolPointCallbackResponse(1, "Speech end")


rospy.init_node('excursion_point_service')
s = rospy.Service('turtlebro_heat_excursion', PatrolPointCallback, handle_request)
aruco_detect = rospy.ServiceProxy('aruco_detect', ArucoDetect)
rospy.loginfo("Ready to speak points")
rospy.spin()
