package com.github.lamba92.fds

import io.ktor.application.*
import io.ktor.server.cio.*
import io.ktor.server.engine.*
import io.ktor.util.*
import java.lang.System.getenv

@KtorExperimentalAPI
fun main() {
    embeddedServer(
        factory = CIO,
        host = "localhost",
        port = getenv("SERVER_PORT")?.toInt() ?: 8084,
        module = Application::queryBuilderModule
    ).start(true)
}
