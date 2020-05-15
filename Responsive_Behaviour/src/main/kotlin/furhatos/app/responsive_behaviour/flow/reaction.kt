package furhatos.app.responsive_behaviour.flow

import furhatos.flow.kotlin.*
import furhatos.gestures.Gestures
import furhatos.util.*
import java.net.ServerSocket
import java.util.*

val Reaction : State = state(Idle){

    onEntry {
        val server = ServerSocket(9999)
        println("Server running on port ${server.localPort}")
        var handGesture = "break"
        while (true) {
            val client = server.accept()
            println("Client connected : ${client.inetAddress.hostAddress}")
            val scanner = Scanner(client.inputStream)
            while (scanner.hasNextLine()) {
                handGesture = (scanner.nextLine())
                if (handGesture == "Open Palm") {
                    furhat.gesture(Gestures.Smile(duration = 2.0, strength = 5.0))
                    furhat.say("Greetings")
                }
                if (handGesture == "Dorsal Palm") {
                    furhat.gesture(Gestures.ExpressSad(duration = 3.0, strength = 5.0))
                    furhat.say("Goodbye")
                }
                if (handGesture == "Open Fist") {
                    furhat.gesture(Gestures.Nod(duration = 2.0, strength = 5.0))
                    delay(100)
                    furhat.say("Solidarity!")
                }
                if (handGesture == "Dorsal Fist") {
                    furhat.gesture(Gestures.ExpressAnger(duration = 2.0, strength = 10.0))
                    delay(100)
                    furhat.say("Rude!")
                }
                if (handGesture == "Open Three Fingers") {
                    furhat.gesture(Gestures.Thoughtful(duration = 2.0, strength = 5.0))
                    furhat.say("One")
                    delay(200)
                    furhat.say("Two")
                    delay(200)
                    furhat.say("Three")
                }
                if (handGesture == "Dorsal Three Fingers") {
                    furhat.gesture(Gestures.CloseEyes(duration = 1.0, strength = 2.0))
                    furhat.say("Three")
                    delay(200)
                    furhat.say("Two")
                    delay(200)
                    furhat.say("One")
                    furhat.gesture(Gestures.OpenEyes(duration = 1.0, strength = 2.0))
                break
                }
            }
            if (handGesture == "break") {
                break
            }
        }
        print("Closing Server")
        server.close()
    }
}