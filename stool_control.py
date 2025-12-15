# from common import log_status, safe_sleep, pause_event, define_motors, home_button, motion_motor, motion_motor_both, mixer , last_mixer ,ENABLE_PINS , non_enable_pins 
import RPi.GPIO as GPIO
import timer_module
# stool_control.py
import common
import RPi.GPIO as GPIO

def run_motor_sequence_stool():
  
  
    
    log_status = common.log_status
    safe_sleep = common.safe_sleep
    pause_event = common.pause_event
    define_motors = common.define_motors
    home_button = common.home_button
    motion_motor = common.motion_motor
    motion_motor_both = common.motion_motor_both
    mixer = common.mixer
    last_mixer = common.last_mixer

    define_motors()
    try:
        log_status("Positioning home")
        if common.stop_flag: 
            return
        pause_event.wait()
        home_button()
        if common.stop_flag: 
            return
        safe_sleep(0.5)
 
        # Sequence (kept same as your original)
        if common.stop_flag: return
        pause_event.wait()
        motion_motor(2257, 3, 0.0004, 'right')
        if common.stop_flag: return
        safe_sleep(0.5)

        if common.stop_flag: return
        pause_event.wait()
        motion_motor(450, 3, 0.0004, 'right')
        if common.stop_flag: return
        safe_sleep(0.5)

        if common.stop_flag: return
        pause_event.wait()
        motion_motor(800, 2, 0.0004, 'down')
        if common.stop_flag: return
        safe_sleep(0.5)

        if common.stop_flag: return
        pause_event.wait()
        timer_module.start_timer(60)
        mixer(2,60)

        if common.stop_flag: return
        safe_sleep(0.5)

        if common.stop_flag: return
        pause_event.wait()
        motion_motor(820, 2, 0.0004, 'up')
        if common.stop_flag: return
        safe_sleep(0.5)

        if common.stop_flag: return
        pause_event.wait()
        motion_motor_both(1000, 1, 2, 0.0002, 'down')
        if common.stop_flag: return
        timer_module.start_timer(30)
        safe_sleep(30)

        if common.stop_flag: return
        pause_event.wait()
        motion_motor_both(400, 1, 2, 0.0002, 'down')
        if common.stop_flag: return
        timer_module.start_timer(30)
        safe_sleep(30)

        if common.stop_flag: return
        pause_event.wait()
        motion_motor_both(220, 1, 2, 0.0002, 'down')
        if common.stop_flag: return
        timer_module.start_timer(60)
        safe_sleep(60)

        if common.stop_flag: return
        pause_event.wait()
        motion_motor_both(1620, 1, 2, 0.0002, 'up')
        if common.stop_flag: return
        safe_sleep(0.5)

        if common.stop_flag: return
        pause_event.wait()
        motion_motor(225, 3, 0.0004, 'right')
        if common.stop_flag: return
        safe_sleep(0.5)

        if common.stop_flag: return
        pause_event.wait()
        motion_motor_both(1620, 1, 2, 0.0002, 'down')
        if common.stop_flag: return
        safe_sleep(0.5)

        if common.stop_flag: return
        pause_event.wait()
        motion_motor(800, 1, 0.0004, 'up')
        if common.stop_flag: return
        safe_sleep(0.5)

        if common.stop_flag: return
        pause_event.wait()
        timer_module.start_timer(60)
        mixer(2, 60)
        if common.stop_flag: return
        safe_sleep(0.5)

        if common.stop_flag: return
        pause_event.wait()
        motion_motor(820, 2, 0.0004, 'up')
        if common.stop_flag: return
        safe_sleep(0.5)

        if common.stop_flag: return
        pause_event.wait()
        motion_motor_both(1450, 1, 2, 0.0002, 'down')
        if common.stop_flag: return
        timer_module.start_timer(60)
        safe_sleep(60)

        if common.stop_flag: return
        pause_event.wait()
        motion_motor_both(170, 1, 2, 0.0002, 'down')
        if common.stop_flag: return
        timer_module.start_timer(60)
        safe_sleep(60)

        if common.stop_flag: return
        pause_event.wait()
        motion_motor_both(1620, 1, 2, 0.0002, 'up')
        if common.stop_flag: return
        safe_sleep(0.5)

        # Two passes loop
        for i in range(2):
            if common.stop_flag:
                return
            last_flag = (i == 1)
            if last_flag:
                log_status("last flag reached")
                if common.stop_flag: return
                pause_event.wait()
                motion_motor(230, 3, 0.0004, 'right')
                if common.stop_flag: return
                timer_module.start_timer(60)
                safe_sleep(60)

                if common.stop_flag: return
                pause_event.wait()
                motion_motor_both(1620, 1, 2, 0.0002, 'down')
                if common.stop_flag: return
                safe_sleep(0.5)

                if common.stop_flag: return
                pause_event.wait()
                motion_motor(800, 1, 0.0004, 'up')
                if common.stop_flag: return
                safe_sleep(0.5)

                if common.stop_flag: return
                pause_event.wait()
                timer_module.start_timer(60)
                last_mixer(2, 60)
                if common.stop_flag: return
                safe_sleep(0.5)

                if common.stop_flag: return
                pause_event.wait()
                motion_motor(820, 2, 0.0004, 'up')
                if common.stop_flag: return
                safe_sleep(0.5)

                if common.stop_flag: return
                pause_event.wait()
                motion_motor_both(1640, 1, 2, 0.0002, 'down')
                if common.stop_flag: return
                timer_module.start_timer(60)
                safe_sleep(60)

                if common.stop_flag: return
                pause_event.wait()
                motion_motor_both(1640, 1, 2, 0.0002, 'up')
                if common.stop_flag: return
                safe_sleep(0.5)

            else:
                if common.stop_flag: return
                pause_event.wait()
                motion_motor(220, 3, 0.0004, 'right')
                if common.stop_flag: return
                safe_sleep(0.5)

                if common.stop_flag: return
                pause_event.wait()
                motion_motor_both(1620, 1, 2, 0.0002, 'down')
                if common.stop_flag: return
                safe_sleep(0.5)

                if common.stop_flag: return
                pause_event.wait()
                motion_motor(800, 1, 0.0004, 'up')
                if common.stop_flag: return
                safe_sleep(0.5)

                if common.stop_flag: return
                pause_event.wait()
                timer_module.start_timer(60)
                mixer(2, 60)
                if common.stop_flag: return
                safe_sleep(0.5)

                if common.stop_flag: return
                pause_event.wait()
                motion_motor(820, 2, 0.0004, 'up')
                if common.stop_flag: return
                safe_sleep(0.5)

                if common.stop_flag: return
                pause_event.wait()
                motion_motor_both(1450, 1, 2, 0.0002, 'down')
                if common.stop_flag: return
                timer_module.start_timer(60)
                safe_sleep(60)

                if common.stop_flag: return
                pause_event.wait()
                motion_motor_both(170, 1, 2, 0.0002, 'down')
                if common.stop_flag: return
                timer_module.start_timer(60)
                safe_sleep(60)

                if common.stop_flag: return
                pause_event.wait()
                motion_motor_both(1620, 1, 2, 0.0002, 'up')
                if common.stop_flag: return
                safe_sleep(0.5)

        # Finish: home, then park motor 2 down
        if common.stop_flag: return
        pause_event.wait()
        home_button()
        if common.stop_flag: return
        safe_sleep(0.5)

        if common.stop_flag: return
        pause_event.wait()
        motion_motor(830, 2, 0.0004, 'down')
        if common.stop_flag: return
        safe_sleep(0.5)

    finally:
        # disable drivers then cleanup
        try:
            for pin in common.ENABLE_PINS:
                GPIO.output(pin, GPIO.HIGH)
        except Exception as e:
            print(f"Enable pin disable error: {e}")

        try:
            GPIO.cleanup(common.non_enable_pins)
        except Exception as e:
            print(f"GPIO cleanup error: {e}")
