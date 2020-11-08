import kotlin.random.Random

tasks {

    val generateDataset by registering {
        group = "preprocessing"
        inputs.property("seed", 100)
        inputs.file(file("identity_annotations.txt"))
        outputs.file(file("$buildDir/preprocessing/output.txt"))
        doLast {
            val seed = Random(inputs.properties["seed"] as Int)
            mutableMapOf<String, MutableList<String>>()
                .also { identitiesMap ->
                    file("identity_annotations.txt").useLines {
                        it.map { it.split(" ") }.forEach { (fileName, identityId) ->
                            if (identityId !in identitiesMap)
                                identitiesMap[identityId] = mutableListOf()
                            identitiesMap[identityId]!!.add(fileName)
                        }
                    }
                }.entries.asSequence()
                .filter { it.value.size >= 10 }
                .map { it.key.toInt() to it.value.subList(0, 10).toList() }
                .toMap()
                .let { identitiesMap ->
                    @OptIn(ExperimentalStdlibApi::class)
                    buildList {
                        identitiesMap.forEach { (identity, files) ->
                            files.combineWith(files).forEach { (f1, f2) ->
                                add(Triple(f1, f2, true))
                            }
                            identitiesMap.keys.extractRandom(
                                excludeElements = listOf(identity),
                                random = seed
                            )
                                .map { identitiesMap.getValue(it) }
                                .flatMap { it.combineWith(files) }
                                .forEach { (f1, f2) ->
                                    add(Triple(f1, f2, false))
                                }
                        }
                    }
                }
                .let { newData ->
                    file("$buildDir/preprocessing/output.txt").bufferedWriter().use { writer ->
                        newData.forEach { (file1, file2, clazz) ->
                            writer.write("$file1 $file2 ${if (clazz) "1" else "0"}")
                            writer.newLine()
                        }
                    }
                }
        }
    }

    register("printOutputStats") {
        group = "preprocessing"
        dependsOn(generateDataset)
        doLast {
            var zeros = 0
            var ones = 0
            file("$buildDir/preprocessing/output.txt").useLines {
                it.map { it.split(" ").last() }
                    .forEach {
                        when (it) {
                            "0" -> zeros++
                            "1" -> ones++
                            else -> throw IllegalArgumentException("Class $it should not be here")
                        }
                    }
            }
            println("zeros $zeros, ones $ones")
        }
    }
}

@OptIn(ExperimentalStdlibApi::class)
fun <T, R> Iterable<T>.combineWith(other: Iterable<R>) = buildList {
    this@combineWith.forEach { self ->
        other.forEach {
            add(self to it)
        }
    }
}

@OptIn(ExperimentalStdlibApi::class)
fun <T> Iterable<T>.extractRandom(
    elements: Int = 1,
    excludeElements: List<T> = emptyList(),
    random: Random = Random
) = buildList {
    var self = this@extractRandom.toList()
    repeat(elements) {
        if (self.isEmpty())
            return@repeat
        var done = false
        while (!done) {
            val (elem, newSelf) = self.extractAndRemove(random)
            if (elem !in excludeElements) {
                add(elem)
                done = true
            }
            self = newSelf
        }
    }
}

fun <T> List<T>.extractAndRemove(random: Random = Random): Pair<T, List<T>> {
    val elem = random(random)
    return elem to filter { it != elem }
}
