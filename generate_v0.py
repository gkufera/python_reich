#!/usr/bin/env python

from midiutil.MidiFile import MIDIFile
import random

MAX_COUNT = 500
D_DORIAN_SCALE = [62, 64, 65, 67, 69, 71, 72]
D_PENTATONIC_SCALE = [62, 64, 67, 69, 71]
BIAS_TOWARD_PENTATONIC_NOTES = 0.1
NUM_TRACKS = 4
MIDI_FILE = MIDIFile(NUM_TRACKS)
TEMPO = 200 # beats per minute
TIME_SIGNATURE = 4 # beats per measure
NUM_SUBDIVISIONS = 8 # subdivisions per measure
DURATION_OF_SUBDIVISION = TIME_SIGNATURE / NUM_SUBDIVISIONS
LENGTH_OF_SONG_IN_MEASURES = 20

class Measure:
    def __init__(self, numSubdivisions, pitches, durations, orders):
        self.numSubdivisions = numSubdivisions
        self.pitches = pitches
        self.durations = durations
        self.orders = orders

sample_measure = Measure(8, [62, 64, 62, 64, 67, 69, 71, 67], [1, 1, 1, 1, 1, 1, 1, 1], [0, 3, 2, 4, 1, 5, 6, 7])

def get_random_note_from_scale(scale):
    return scale[random.randrange(len(scale))]

def get_random_note():
    if (random.random() < BIAS_TOWARD_PENTATONIC_NOTES):
        return get_random_note_from_scale(D_PENTATONIC_SCALE)
    else:
        return get_random_note_from_scale(D_DORIAN_SCALE)

def generate_measure():
    pitches = []
    durations = []
    while len(pitches) < NUM_SUBDIVISIONS:
        random_note = get_random_note()
        pitches.append(random_note)
        durations.append(1)
    orders = [0, 1, 2, 3, 4, 5, 6, 7]
    random.shuffle(orders)
    return Measure(NUM_SUBDIVISIONS, pitches, durations, orders)

def generate_midi_track(track_number, measure):
    time = 0
    MIDI_FILE.addTrackName(track_number, time, "Marimba")
    MIDI_FILE.addTempo(track_number, time, TEMPO)

    channel = 0
    volume = 100
    measure_count = 0
    while (measure_count < LENGTH_OF_SONG_IN_MEASURES):
        subdivision_count = 0
        while (subdivision_count < NUM_SUBDIVISIONS):
            pitch = measure.pitches[subdivision_count]
            duration = measure.durations[subdivision_count] * DURATION_OF_SUBDIVISION
            MIDI_FILE.addNote(track_number, channel, pitch, time, duration, volume)
            time += duration
            subdivision_count += 1
        measure_count += 1


track_count = 0
while track_count < NUM_TRACKS:
    generate_midi_track(track_count, generate_measure())
    track_count += 1

with open("test.mid", 'wb') as outfile:
    MIDI_FILE.writeFile(outfile)
