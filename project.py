from music21 import stream, note, tempo, key, meter, metadata

# Criar partitura principal
score = stream.Score()
score.insert(0, metadata.Metadata(title="See You Later - Melodia Karaoke", composer="Spring of Youth OST"))

# Configurações iniciais
part = stream.Part()
part.append(tempo.MetronomeMark(number=75))  # BPM suave
part.append(key.KeySignature(-3))  # F# menor
part.append(meter.TimeSignature('4/4'))

# Melodia (simplificada, representando o refrão em F#m)
melody_notes = [
    note.Rest(quarterLength=1.0),

        note.Note('F#4', quarterLength=1.0),
            note.Note('A4', quarterLength=1.0),
                note.Note('C#5', quarterLength=2.0),

                    note.Note('D5', quarterLength=1.0),
                        note.Note('E5', quarterLength=1.0),
                            note.Note('C#5', quarterLength=2.0),

                                note.Note('A4', quarterLength=1.0),
                                    note.Note('C#5', quarterLength=1.0),
                                        note.Note('B4', quarterLength=2.0),

                                            note.Note('E4', quarterLength=1.0),
                                                note.Note('F#4', quarterLength=1.0),
                                                    note.Note('G#4', quarterLength=2.0),

                                                        note.Note('F#4', quarterLength=1.0),
                                                            note.Note('A4', quarterLength=1.0),
                                                                note.Note('B4', quarterLength=2.0),
                                                                ]

                                                                # Adiciona notas à partitura
                                                                melody_stream = stream.Measure()
                                                                for n in melody_notes:
                                                                    melody_stream.append(n)

                                                                    part.append(melody_stream)
                                                                    score.append(part)

                                                                    # Exportar como PDF ou mostrar no MuseScore (se instalado)
                                                                    score.show()  # Abre a partitura visual no MuseScore, se estiver configurado