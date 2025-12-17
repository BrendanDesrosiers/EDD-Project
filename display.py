from music21 import *

us = environment.UserSettings()
us['lilypondPath'] = '/Library/lilypond-2.24.4/bin/lilypond'

clef = clef.PercussionClef()
melody = stream.Stream()
melody.append(clef)
melody.append(tempo.MetronomeMark(number=100))
melody.append(meter.TimeSignature('4/4'))


melody.repeatAppend(note.Note("C4",type='16th'),4)
melody.append(note.Rest("C4",type='quarter'))
melody.append(note.Note("C4",type='eighth'))
melody.repeatAppend(note.Note("C4",type='16th'),2)
# melody.repeatAppend(note.Note("C4",duration=eighthTriplet),3)
melody.show('lily')

# littleMelody = converter.parse("tinynotation: 3/4 c4 d8 f g16 a g f# e8 e g g a a g4 f8 f e e 2/4 d d c4")
# with open("midiFile.mid", "w"):
#     littleMelody.write('midi', fp="midiFile.mid")

# littleMelody.show('lily')