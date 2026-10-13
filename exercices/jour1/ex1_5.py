def normaliser_notes(notes):
    """Transforme des notes sur 20 en notes entre 0 et 1."""
    notes = notes.copy()
    for i in range(len(notes)):
        notes[i] = notes[i] / 20
    return notes
notes_brutes = [12, 15, 9, 18]
notes_normalisees = normaliser_notes(notes_brutes)

print("Brutes :", notes_brutes)
print("Normalisées :", notes_normalisees)
