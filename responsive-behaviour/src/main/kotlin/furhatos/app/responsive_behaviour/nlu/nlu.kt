package furhatos.app.responsive_behaviour.nlu

import furhatos.nlu.*
import furhatos.nlu.common.Number
import furhatos.util.Language

/*
class Hand : EnumEntity(stemming = true, speechRecPhrases = true){
    override fun getEnum(lang: Language): List<String> {
        return listOf("Open Palm", "Dorsal Palm", "Open Fist", "Dorsal Fist", "Open Three Fingers", "Dorsal Three Fingers")
    }
}

class ChooseHand(val hand: Hand? = null): Intent(){
    override fun getExamples(lang: Language): List<String> {
        return listOf("@hand", "I want @hand")
    }
}
*/

val OpenPalm = SimpleIntent("Open Palm" )
val DorsalPalm = SimpleIntent("Dorsal Palm" )
val OpenFist = SimpleIntent("Open Fist" )
val DorsalFist = SimpleIntent("Dorsal Fist" )
val OpenThreeFingers = SimpleIntent("Open Three Fingers" )
val DorsalThreeFingers = SimpleIntent("Dorsal Three Fingers" )
