import time
from random import randrange
import argparse
from pydub import AudioSegment
from pydub.playback import play

parser = argparse.ArgumentParser("silence-interrupted-by-random-sound")
parser.add_argument("-s", dest='file', help="Path to the sound file.", type=str)
parser.add_argument("-w", dest='wait_time', help="The max amount of seconds to wait in between sounds.", type=int)
args = parser.parse_args()

while True:
    audio = AudioSegment.from_file(args.file)
    play(audio)
    time.sleep(randrange(args.wait_time))