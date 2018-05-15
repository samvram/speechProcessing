import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import os


def spectrogram(file_name):
    sample_rate, samples = wavfile.read(file_name)
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

    plt.pcolormesh(times, frequencies, spectrogram)
    plt.imshow(spectrogram)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time/44100[sec]')
    # plt.ylim(min(frequencies),max(frequencies))
    # plt.xlim(min(times),max(times))
    # plt.show()
    save_file_as = 'spectrograms/'+file_name.split('.')[0]+'_spectrogram.png'
    plt.savefig(save_file_as)

if __name__ == '__main__':
    files = ['ah.wav', 'ah_lrr.wav', 's5.wav', 'should.wav', 'test_16k.wav', 'vowel_ah_100Hz.wav']
    directories = ['digits_train', 'digits_train_raw']
    for directory in directories:
        for file in os.listdir(directory):
            files.append(directory+'/'+file)

    for file in files:
        spectrogram(file)
    print('End')