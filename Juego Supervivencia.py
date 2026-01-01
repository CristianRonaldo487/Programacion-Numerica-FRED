jugar_supervivencia <- function() {
 jugador <- sample(tipos, 2, replace = TRUE)
 chupetines <- 0
 iteracion <- 1
 repeat {
 conteo <- contar(jugador)

 # Regla 2: 2 de cada tipo
 if (all(conteo >= 2)) {
 chupetines <- chupetines + 2
 # Quitar 2 de cada tipo
 for (t in tipos) {
 jugador <- jugador[-which(jugador == t)[1:2]]
 }
 # Agregar 1 caramelo al azar
 jugador <- c(jugador, sample(tipos, 1))
 }
 # Regla 1: 1 de cada tipo
 else if (all(conteo >= 1)) {
 chupetines <- chupetines + 1
 for (t in tipos) {
 jugador <- jugador[-which(jugador == t)[1]]
 }
 } else {
 break
 }

 iteracion <- iteracion + 1
 }

 return(list(chupetines = chupetines, iteraciones = iteracion - 1))
}
Estudio:
# JUEGO DE SUPERVIVENCIA - MÉTODOS ITERATIVOS
# Simulación con 30 participantes + GRÁFICO
if(!require(ggplot2)) install.packages("ggplot2", dependencies = TRUE)
library(ggplot2)
set.seed(123) # Reproducibilidad
# --- Tipos de caramelos ---
tipos <- c("amarillo", "blanco", "redondito")
# --- Función para contar caramelos ---
contar <- function(caramelos) {
 table(factor(caramelos, levels = tipos))
}
# --- Función que simula el juego de un jugador ---
jugar_supervivencia <- function() {
 jugador <- sample(tipos, 2, replace = TRUE)
 chupetines <- 0
 iteracion <- 1

 repeat {
 conteo <- contar(jugador)

 # Regla 2: 2 de cada tipo
 if (all(conteo >= 2)) {
 chupetines <- chupetines + 2
 # Quitar 2 de cada tipo
 for (t in tipos) {
 jugador <- jugador[-which(jugador == t)[1:2]]
 }
 # Agregar 1 caramelo al azar
 jugador <- c(jugador, sample(tipos, 1))
 }
 # Regla 1: 1 de cada tipo
 else if (all(conteo >= 1)) {
 chupetines <- chupetines + 1
 for (t in tipos) {
 jugador <- jugador[-which(jugador == t)[1]]
 }
 } else {
 break
 }

 iteracion <- iteracion + 1
 }

 return(list(chupetines = chupetines, iteraciones = iteracion - 1))
}
# --- Simular 30 participantes ---
n_participantes <- 30
resultados <- data.frame(
 Participante = paste("Jugador", 1:n_participantes),
 Chupetines = integer(n_participantes),
 Iteraciones = integer(n_participantes)
)
for (i in 1:n_participantes) {
 juego <- jugar_supervivencia()
 resultados$Chupetines[i] <- juego$chupetines
 resultados$Iteraciones[i] <- juego$iteraciones
}
# --- Mostrar tabla de resultados ---
print(resultados)
# --- Mostrar el ganador ---
mejor <- resultados[which.max(resultados$Chupetines), ]
cat("\n El ganador es:", mejor$Participante,
 "con", mejor$Chupetines, "chupetines!\n")
# --- Crear gráfico ---
grafico <- ggplot(resultados, aes(x = Participante, y = Chupetines, fill = Chupetines)) +
 geom_bar(stat = "identity") +
 theme_minimal(base_size = 13) +
 labs(
 title = "Resultados del juego 'Supervivencia'
 ",
 x = "Participantes",
 y = "Chupetines obtenidos"
 ) +
 scale_fill_gradient(low = "yellow", high = "red") +
 theme(axis.text.x = element_text(angle = 60, hjust = 1))
# --- Mostrar el gráfico ---
print(grafico)
