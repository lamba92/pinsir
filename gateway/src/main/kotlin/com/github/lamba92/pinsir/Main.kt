package com.github.lamba92.pinsir

import io.grpc.ServerBuilder

fun main() = ServerBuilder.forPort(System.getenv("PORT")!!.toInt())
    .addService(GatewayService())
    .build()
    .run {
        start()
        awaitTermination()
    }
