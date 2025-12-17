from music21 import *

# Set the path to LilyPond executable
us = environment.UserSettings()
us['lilypondPath'] = '/Library/lilypond-2.24.4/bin/lilypond'

# Set up a percussion clef stream object
clef = clef.PercussionClef()
melody = stream.Stream()
melody.append(clef)
# Specify tempo and time signature
melody.append(tempo.MetronomeMark(number=100))
melody.append(meter.TimeSignature('4/4'))

# Add some notes to the melody
melody.repeatAppend(note.Note("C4",type='16th'),4)
melody.append(note.Rest("C4",type='quarter'))
melody.append(note.Note("C4",type='eighth'))
melody.repeatAppend(note.Note("C4",type='16th'),2)

# Display the melody using LilyPond, this will create and display a .png file
melody.show('lily')

# Write a little melody to a MIDI file
littleMelody = converter.parse("tinynotation: 3/4 c4 d8 f g16 a g f# e8 e g g a a g4 f8 f e e 2/4 d d c4")
with open("midiFile.mid", "w"):
    littleMelody.write('midi', fp="midiFile.mid")