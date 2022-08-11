import essentia.streaming as ess
import essentia

audio_file = "/home/ogulcan/PycharmProjects/MasterThesis/Songs/SeperationLocation/NafileTrimmed/bass.wav"

# Initialize algorithms we will use.
loader = ess.MonoLoader(filename=audio_file)
framecutter = ess.FrameCutter(frameSize=4096, hopSize=1024, silentFrames='noise')
windowing = ess.Windowing(type='blackmanharris62')
spectrum = ess.Spectrum()
spectralpeaks = ess.SpectralPeaks(orderBy='magnitude',
                                  magnitudeThreshold=0.00001,
                                  minFrequency=20,
                                  maxFrequency=1000,
                                  maxPeaks=60)

# Use default HPCP parameters for plots.
# However we will need higher resolution and custom parameters for better Key estimation.

hpcp = ess.HPCP()

# Use pool to store data.
pool = essentia.Pool()

# Connect streaming algorithms.
loader.audio >> framecutter.signal
framecutter.frame >> windowing.frame >> spectrum.frame
spectrum.spectrum >> spectralpeaks.spectrum
spectralpeaks.magnitudes >> hpcp.magnitudes
spectralpeaks.frequencies >> hpcp.frequencies
hpcp.hpcp >> (pool, 'tonal.hpcp')

# Run streaming network.
essentia.run(loader)

from essentia.standard import ChordsDetection

# Using a 2 seconds window over HPCP matrix to estimate chords
chords, strength = ChordsDetection(hopSize=512, windowSize=2)(pool['tonal.hpcp'])
print(chords)
len(chords)
