function turnLeft () {
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 20)
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 20)
    basic.pause(1100)
    maqueen.motorStop(maqueen.Motors.All)
}
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Yes)
    state2 = 1
})
function trackLine () {
    if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 32)
    } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 1 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 20)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 20)
    } else if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 1) {
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 20)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 20)
    }
}
function turnRight () {
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 20)
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 20)
    basic.pause(1100)
    maqueen.motorStop(maqueen.Motors.All)
}
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.No)
    state2 = 0
})
let state2 = 0
basic.showIcon(IconNames.Yes)
state2 = 0
basic.forever(function () {
    if (state2 == 1) {
        trackLine()
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            turnLeft()
            if (maqueen.Ultrasonic() < 12) {
                turnRight()
                state2 = 2
            } else {
                state2 = 3
            }
        }
    } else if (state2 == 2) {
        trackLine()
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            turnLeft()
            if (maqueen.Ultrasonic() < 12) {
                turnRight()
                state2 = 5
            } else {
                state2 = 4
            }
        }
    } else if (state2 == 3) {
        trackLine()
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            turnLeft()
            state2 = 7
        }
    } else if (state2 == 4) {
        trackLine()
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            turnLeft()
            state2 = 6
        }
    } else if (state2 == 5) {
        trackLine()
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 32)
            basic.pause(200)
            state2 = 6
        }
    } else if (state2 == 6) {
        trackLine()
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 32)
            basic.pause(200)
            state2 = 7
        }
    } else if (state2 == 7) {
        trackLine()
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            turnRight()
            state2 = 8
        }
    } else if (state2 == 8) {
        trackLine()
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            if (maqueen.Ultrasonic() < 12) {
                turnLeft()
                state2 = 10
            } else {
                maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 32)
                basic.pause(200)
                state2 = 9
            }
        }
    } else if (state2 == 9) {
        trackLine()
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 32)
            basic.pause(200)
            state2 = 11
        }
    } else if (state2 == 10) {
        trackLine()
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            turnLeft()
            state2 = 11
        }
    } else if (state2 == 11) {
        trackLine()
        if (maqueen.readPatrol(maqueen.Patrol.PatrolLeft) == 0 && maqueen.readPatrol(maqueen.Patrol.PatrolRight) == 0) {
            maqueen.motorStop(maqueen.Motors.All)
            state2 = 0
            basic.showIcon(IconNames.Happy)
            music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        }
    } else {
        maqueen.motorStop(maqueen.Motors.All)
    }
})
