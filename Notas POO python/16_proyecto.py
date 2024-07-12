from textblob import TextBlob


class AnalisadorDeSentimientos:
    def analizar_sentimientos(self,texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "positivo"
        elif analisis.sentiment.polarity == 0:
            return "neutral"
        else:
            return"negativo"
        
analizador = AnalisadorDeSentimientos()
resultado= analizador.analizar_sentimientos("hello, i wnat to di")
print(resultado)

