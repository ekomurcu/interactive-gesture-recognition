package furhatos.app.responsive_behaviour.flow

import furhatos.nlu.common.*
import furhatos.flow.kotlin.*
import furhatos.app.responsive_behaviour.nlu.*
import furhatos.gestures.Gestures

val Start : State = state(Interaction) {

    onEntry {
        furhat.ask("What were you doing with your hand?")
    }

    onResponse(OpenPalm) {
        furhat.gesture(Gestures.Smile(duration = 2.0, strength = 5.0))
        furhat.say("Greetings")
    }

    onResponse(DorsalPalm) {
        furhat.gesture(Gestures.ExpressSad(duration = 3.0, strength = 5.0))
        furhat.say("Goodbye")
    }

    onResponse(OpenFist) {
        furhat.gesture(Gestures.Nod(duration = 2.0, strength = 5.0))
        furhat.say("Solidarity!")
    }

    onResponse(DorsalFist) {
        furhat.gesture(Gestures.ExpressAnger(duration = 2.0, strength = 10.0))
        furhat.say("Rude!")
    }

    onResponse(OpenThreeFingers) {
        furhat.gesture(Gestures.Thoughtful(duration = 2.0, strength = 5.0))
        furhat.say("One")
        delay(200)
        furhat.say("Two")
        delay(200)
        furhat.say("Three")
    }

    onResponse(DorsalThreeFingers) {
        furhat.gesture(Gestures.CloseEyes(duration = 2.0, strength = 5.0))
        furhat.say("Three")
        delay(200)
        furhat.say("Two")
        delay(200)
        furhat.say("One")
    }
}




