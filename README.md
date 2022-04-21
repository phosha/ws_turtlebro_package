# ws_turtlebro_package
roslaunch turtlebro_heat_excursion heat_excursion.launch waypoints_data_file:=/home/pavel/Robot_ws/src/ws_turtlebro_package/data/goals.xml


#include <ros.h>
#include <std_msgs/Bool.h>
#include <FastLED.h>

#define NUM_LEDS 2
#define DATA_PIN A1
CRGB leds[NUM_LEDS];




void messageCb( const std_msgs::Bool& toggle_msg) {
  if (toggle_msg.data) {
    for (byte i = 0; i <= NUM_LEDS; i++) {
      leds[i] = CRGB::Red;
    }
    FastLED.show();
  }
  else {
    for (byte i = 0; i <= NUM_LEDS; i++) {
      leds[i] = CRGB::Green;
    }
    FastLED.show();
  }
}


ros::NodeHandle_<ArduinoHardware, 5, 5, 256, 256> nh; // recieve/publish
ros::Subscriber<std_msgs::Bool> sub("heat_sensor_output", messageCb );


void setup() {
  // put your setup code here, to run once:
  nh.initNode();
  nh.subscribe(sub);
  FastLED.addLeds<WS2812, DATA_PIN, GRB>(leds, NUM_LEDS);

}

void loop() {
  // put your main code here, to run repeatedly:
  nh.spinOnce();
  delay(50);
}

