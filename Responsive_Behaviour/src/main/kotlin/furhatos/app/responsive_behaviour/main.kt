package furhatos.app.responsive_behaviour

import furhatos.app.responsive_behaviour.flow.*
import furhatos.skills.Skill
import furhatos.flow.kotlin.*

class Responsive_behaviourSkill : Skill() {
    override fun start() {
        Flow().run(Idle)
    }
}

fun main(args: Array<String>) {
    Skill.main(args)
}
