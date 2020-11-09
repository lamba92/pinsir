package com.github.lamba92.fds

import com.github.lamba92.fds.detection.DetectionResponse
import com.github.lamba92.fds.embedding.EmbeddingResponse
import com.github.lamba92.fds.extraction.ExtractionRequest
import com.github.lamba92.fds.extraction.ExtractionResponse
import io.ktor.application.*
import io.ktor.client.*
import io.ktor.client.engine.apache.*
import io.ktor.client.features.json.*
import io.ktor.client.features.json.serializer.*
import io.ktor.client.request.*
import io.ktor.features.*
import io.ktor.http.*
import io.ktor.request.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.serialization.*
import io.ktor.util.*
import it.lamba.ktor.utils.AllHeaders
import it.lamba.ktor.utils.any
import kotlinx.coroutines.flow.*
import kotlinx.coroutines.flow.toList
import kotlinx.serialization.Serializable
import kotlinx.serialization.encodeToString
import kotlinx.serialization.json.Json
import org.slf4j.event.Level
import java.lang.System.getenv
import java.util.*
import kotlin.collections.flatMap
import kotlin.collections.map
import kotlin.collections.zip

@Suppress("LocalVariableName")
@KtorExperimentalAPI
fun Application.queryBuilderModule() {

    val httpClient by lazy {
        HttpClient(Apache) {
            install(JsonFeature) {
                serializer = KotlinxSerializer()
            }
        }
    }

    val b64Encoder by lazy { Base64.getEncoder()!! }

    val DETECTOR_HOSTNAME: String = envOrThrow("DETECTOR_HOSTNAME")
    val EXTRACTOR_HOSTNAME: String = envOrThrow("EXTRACTOR_HOSTNAME")
    val EMBEDDER_HOSTNAME: String = envOrThrow("EMBEDDER_HOSTNAME")

    install(CallLogging) {
        level = Level.DEBUG
    }

    install(Compression) {
        gzip()
    }

    install(CORS) {
        any()
        allowSameOrigin = true
        allowCredentials = true
        allowNonSimpleContentTypes = true
        allowXHttpMethodOverride()
        HttpHeaders.AllHeaders.forEach {
            exposeHeader(it)
        }
    }
    install(ContentNegotiation) {
        json()
    }
    install(StatusPages) {
        exception<Throwable> {
            log.error(it)
            call.respond(HttpStatusCode.InternalServerError, mapOf(
                "error" to it.message,
                "stack" to it.stackTrace.map { it.toString() }.let { Json.encodeToString(it) }
            ))
        }
    }

    routing {
        route("elaborate") {
            post("file") {
                call.receiveStream()
                    .let { b64Encoder.encodeToString(it.readBytes()) }
                    .let {
                        httpClient.elaborateImage(
                            listOf(it),
                            DETECTOR_HOSTNAME,
                            EXTRACTOR_HOSTNAME,
                            EMBEDDER_HOSTNAME
                        )
                    }
                    .let { call.respond(it) }
            }
            post {
                call.receive<List<String>>()
                    .let { httpClient.elaborateImage(it, DETECTOR_HOSTNAME, EXTRACTOR_HOSTNAME, EMBEDDER_HOSTNAME) }
                    .let { call.respond(it) }
            }
            route("embeddingOnly") {
                post {
                    call.receive<List<String>>()
                        .let {
                            httpClient.elaborateImage(
                                it,
                                DETECTOR_HOSTNAME,
                                EXTRACTOR_HOSTNAME,
                                EMBEDDER_HOSTNAME,
                                call.parameters["facesPerImage"]?.toInt() ?: 0
                            )
                        }
                        .map { it.data.map { it.embedding } }
                        .let { call.respond(it) }
                }
                post("flattened") {
                    call.receive<List<String>>()
                        .let {
                            httpClient.elaborateImage(
                                it,
                                DETECTOR_HOSTNAME,
                                EXTRACTOR_HOSTNAME,
                                EMBEDDER_HOSTNAME,
                                call.parameters["facesPerImage"]?.toInt() ?: 0
                            )
                        }
                        .flatMap { it.data.map { it.embedding } }
                        .let { call.respond(it) }
                }
            }

        }

    }
}

suspend fun HttpClient.elaborateImage(
    b64Images: List<String>,
    DETECTOR_HOSTNAME: String,
    EXTRACTOR_HOSTNAME: String,
    EMBEDDER_HOSTNAME: String,
    facesPerImage: Int = 0
) =
    post<DetectionResponse>("$DETECTOR_HOSTNAME/detect") {
        header(HttpHeaders.ContentType, ContentType.Application.Json.toString())
        body = b64Images
    }
        .asFlow()
        .map { (image, annotations) ->
            ExtractionRequest(
                image,
                annotations.subList(0, if (facesPerImage > 0) facesPerImage else annotations.size)
            )
        }
        .toList()
        .let { request ->
            post<List<ExtractionResponse>>("$EXTRACTOR_HOSTNAME/extract/array") {
                header(HttpHeaders.ContentType, ContentType.Application.Json.toString())
                body = request
            }
        }
        .asFlow()
        .map {
            val embeddings = post<EmbeddingResponse>("$EMBEDDER_HOSTNAME/embed") {
                header(HttpHeaders.ContentType, ContentType.Application.Json.toString())
                body = it.extracted.map { it.image }
            }
            it.originalImage to embeddings.zip(it.extracted).map { (embedding, portrait) ->
                PortraitWithEmbedding(embedding, portrait)
            }
        }
        .map { (originalImage, extractedData) ->
            ImageWithExtractedData(originalImage, extractedData)
        }
        .toList()


@Serializable
data class ImageWithExtractedData(
    val originalImage: String,
    val data: List<PortraitWithEmbedding>
)

@Serializable
data class PortraitWithEmbedding(
    val embedding: DoubleArray,
    val portrait: ExtractionResponse.AnnotatedPortrait
) {
    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (javaClass != other?.javaClass) return false

        other as PortraitWithEmbedding

        if (!embedding.contentEquals(other.embedding)) return false
        if (portrait != other.portrait) return false

        return true
    }

    override fun hashCode(): Int {
        var result = embedding.contentHashCode()
        result = 31 * result + portrait.hashCode()
        return result
    }
}

fun envOrThrow(
    name: String,
    default: String? = null
) =
    getenv(name)
        ?: default
        ?: throw IllegalArgumentException("$name not found in environment")
