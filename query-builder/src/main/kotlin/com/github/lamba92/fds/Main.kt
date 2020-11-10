package com.github.lamba92.fds

import io.grpc.ServerBuilder

fun main() = ServerBuilder.forPort(50051)
    .addService(GatewayService())
    .build()
    .run {
        start()
        awaitTermination()
    }
