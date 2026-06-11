def on_button_pressed_a():
    global state2
    basic.show_icon(IconNames.YES)
    state2 = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global state2
    basic.show_icon(IconNames.NO)
    state2 = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

state2 = 0
state2 = 0
basic.show_icon(IconNames.NO)

def on_forever():
    if state2 == 1:
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 64)
        elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 40)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 40)
        elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 40)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 40)
    else:
        maqueen.motor_stop(maqueen.Motors.ALL)
basic.forever(on_forever)
