def turnLeft():
    maqueen.motor_stop(maqueen.Motors.ALL)
    basic.pause(200)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 20)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 20)
    basic.pause(1000)
    maqueen.motor_stop(maqueen.Motors.ALL)

def on_button_pressed_a():
    global state2
    basic.show_icon(IconNames.YES)
    state2 = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def trackLine():
    if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 32)
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 1 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 20)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 20)
    elif maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 1:
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 20)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 20)
def turnRight():
    maqueen.motor_stop(maqueen.Motors.ALL)
    basic.pause(200)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 20)
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 20)
    basic.pause(1000)
    maqueen.motor_stop(maqueen.Motors.ALL)

def on_button_pressed_b():
    global state2
    basic.show_icon(IconNames.NO)
    state2 = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

strip: neopixel.Strip = None
state2 = 0
basic.show_icon(IconNames.YES)
state2 = 0

def on_forever():
    global state2, strip
    if state2 == 1:
        trackLine()
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 32)
            basic.pause(100)
            turnLeft()
            if maqueen.ultrasonic() < 12:
                maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 32)
                basic.pause(100)
                turnRight()
                state2 = 2
            else:
                maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 32)
                basic.pause(200)
                state2 = 3
    elif state2 == 2:
        trackLine()
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            turnLeft()
            if maqueen.ultrasonic() < 12:
                turnRight()
                state2 = 5
            else:
                state2 = 4
    elif state2 == 3:
        trackLine()
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 32)
            basic.pause(100)
            turnLeft()
            state2 = 7
    elif state2 == 4:
        trackLine()
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            turnLeft()
            state2 = 6
    elif state2 == 5:
        trackLine()
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 32)
            basic.pause(200)
            state2 = 6
    elif state2 == 6:
        trackLine()
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 32)
            basic.pause(300)
            state2 = 7
            strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
            strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    elif state2 == 7:
        trackLine()
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            basic.pause(300)
            turnRight()
            state2 = 8
    elif state2 == 8:
        trackLine()
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            if maqueen.ultrasonic() < 12:
                turnLeft()
                state2 = 10
            else:
                maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 32)
                basic.pause(200)
                state2 = 9
    elif state2 == 9:
        trackLine()
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 32)
            basic.pause(200)
            state2 = 11
    elif state2 == 10:
        trackLine()
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            turnLeft()
            state2 = 11
    elif state2 == 11:
        trackLine()
        if maqueen.read_patrol(maqueen.Patrol.PATROL_LEFT) == 0 and maqueen.read_patrol(maqueen.Patrol.PATROL_RIGHT) == 0:
            maqueen.motor_stop(maqueen.Motors.ALL)
            state2 = 0
            basic.show_icon(IconNames.HAPPY)
            music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
    else:
        maqueen.motor_stop(maqueen.Motors.ALL)
basic.forever(on_forever)
