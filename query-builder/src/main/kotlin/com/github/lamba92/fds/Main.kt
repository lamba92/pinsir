package com.github.lamba92.fds

import io.ktor.application.*
import io.ktor.server.cio.*
import io.ktor.server.engine.*
import io.ktor.util.*

@KtorExperimentalAPI
fun main() {
    embeddedServer(CIO,host = "localhost", port = 8083, module = Application::queryBuilderModule).start(true)
}
