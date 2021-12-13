from midiutil.MidiFile import MIDIFile

MAX_COUNT = 500


def generate_midi_using_function(growthFunction, fileName):
    # create your MIDI object
    mf = MIDIFile(1)     # only 1 track
    track = 0            # the only track

    time = 0             # start at the beginning
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, 120)

    # add notes
    channel = 0
    volume = 100
    pitch = 20           # C4 (middle C)

    time = 0

    count = 0

    while (count < MAX_COUNT):
        duration = growthFunction(time)
        mf.addNote(track, channel, pitch % 255, time, duration, volume)
        time += duration
        pitch += 2
        count += 1

    # write it to disk
    with open(fileName, 'wb') as outf:
        mf.writeFile(outf)


def slowExponentialFunction(time):
    return pow(0.9, time)


def twoExponentialFunction(time):
    return pow(0.5, time)


def fiveExponentialFunction(time):
    return pow(0.2, time)


def tenExponentialFunction(time):
    return pow(0.1, time)


def twentyExponentialFunction(time):
    return pow(0.05, time)


def parabola(time):
    return time

# TODO NEXT NOTE FUNCTION


generate_midi_using_function(
    slowExponentialFunction, "slowExponentialFunction.mid")
generate_midi_using_function(
    twoExponentialFunction, "twoExponentialFunction.mid")
generate_midi_using_function(
    fiveExponentialFunction, "fiveExponentialFunction.mid")
'''
generate_midi_using_function(
    tenExponentialFunction, "tenExponentialFunction.mid")
generate_midi_using_function(
    twentyExponentialFunction, "twentyExponentialFunction.mid")
'''
generate_midi_using_function(parabola, "parabola.mid")
