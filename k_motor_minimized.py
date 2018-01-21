from microbit import pin0,pin8,pin12,pin16,display,Image
class KMotor:
 FORWARD=0
 REVERSE=1
 MOTOR_1=0
 MOTOR_2=1
 def __init__(self):
  self.motor_off(KMotor.MOTOR_1)
  self.motor_off(KMotor.MOTOR_2)
  display.clear()
 def motor_on(self,motor,direction,speed=100):
  if not 0<=speed<=100:
   display.show(Image.NO)
   return
  speed=self._scale(speed)
  if direction==KMotor.FORWARD:
   if motor==KMotor.MOTOR_1:
    pin8.write_analog(speed)
    pin12.write_digital(0)
   elif motor==KMotor.MOTOR_2:
    pin0.write_analog(speed)
    pin16.write_digital(0)
  else:
   if motor==KMotor.MOTOR_1:
    pin12.write_analog(speed)
    pin8.write_digital(0)
   elif motor==KMotor.MOTOR_2:
    pin16.write_analog(speed)
    pin0.write_digital(0)
 def motor_off(self,motor):
  if motor==KMotor.MOTOR_1:
   pin8.write_analog(0)
   pin12.write_analog(0)
  else:
   pin0.write_analog(0)
   pin16.write_analog(0)
 def motor_brake(self,motor):
  if motor==KMotor.MOTOR_1:
   pin8.write_digital(1)
   pin12.write_digital(1)
  else:
   pin0.write_digital(1)
   pin16.write_digital(1)
 def _scale(self,value):
  new_value=(1023/100)*value
  return int(new_value)
