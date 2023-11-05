# This code purpose is to get details about song and save it as a json file.

import numpy as np
import librosa
import json
import os

# Get the features of a song


def get_features(song):
    y, sr = librosa.load(song)
    # print(y.shape)
    # print(sr)

    # length
    length = y.shape[0]/sr
    # print(length)

    # chroma_stft
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    chroma_stft_mean = np.mean(chroma_stft)
    chroma_stft_var = np.var(chroma_stft)
    # print(chroma_stft_mean)
    # print(chroma_stft_var)

    # rms
    rms = librosa.feature.rms(y=y)
    rms_mean = np.mean(rms)
    rms_var = np.var(rms)
    # print(rms_mean)
    # print(rms_var)

    # spectral_centroid
    spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    spectral_centroid_mean = np.mean(spectral_centroid)
    spectral_centroid_var = np.var(spectral_centroid)
    # print(spectral_centroid_mean)
    # print(spectral_centroid_var)

    # spectral_bandwidth
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    spectral_bandwidth_mean = np.mean(spectral_bandwidth)
    spectral_bandwidth_var = np.var(spectral_bandwidth)
    # print(spectral_bandwidth_mean)
    # print(spectral_bandwidth_var)

    # rolloff
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    rolloff_mean = np.mean(rolloff)
    rolloff_var = np.var(rolloff)
    # print(rolloff_mean)
    # print(rolloff_var)

    # zero_crossing_rate
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y)
    zero_crossing_rate_mean = np.mean(zero_crossing_rate)
    zero_crossing_rate_var = np.var(zero_crossing_rate)
    # print(zero_crossing_rate_mean)
    # print(zero_crossing_rate_var)

    # harmony
    harmony = librosa.effects.harmonic(y)
    harmony_mean = np.mean(harmony)
    harmony_var = np.var(harmony)
    # print(harmony_mean)
    # print(harmony_var)

    # perceptr
    perceptr = librosa.effects.percussive(y)
    perceptr_mean = np.mean(perceptr)
    perceptr_var = np.var(perceptr)
    # print(perceptr_mean)
    # print(perceptr_var)

    # tempo
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    # print(tempo)

    # mfcc
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    mfcc1_mean = np.mean(mfcc[0])
    mfcc1_var = np.var(mfcc[0])
    mfcc2_mean = np.mean(mfcc[1])
    mfcc2_var = np.var(mfcc[1])
    mfcc3_mean = np.mean(mfcc[2])
    mfcc3_var = np.var(mfcc[2])
    mfcc4_mean = np.mean(mfcc[3])
    mfcc4_var = np.var(mfcc[3])
    mfcc5_mean = np.mean(mfcc[4])
    mfcc5_var = np.var(mfcc[4])
    mfcc6_mean = np.mean(mfcc[5])
    mfcc6_var = np.var(mfcc[5])
    mfcc7_mean = np.mean(mfcc[6])
    mfcc7_var = np.var(mfcc[6])
    mfcc8_mean = np.mean(mfcc[7])
    mfcc8_var = np.var(mfcc[7])
    mfcc9_mean = np.mean(mfcc[8])
    mfcc9_var = np.var(mfcc[8])
    mfcc10_mean = np.mean(mfcc[9])
    mfcc10_var = np.var(mfcc[9])
    mfcc11_mean = np.mean(mfcc[10])
    mfcc11_var = np.var(mfcc[10])
    mfcc12_mean = np.mean(mfcc[11])
    mfcc12_var = np.var(mfcc[11])
    mfcc13_mean = np.mean(mfcc[12])
    mfcc13_var = np.var(mfcc[12])
    mfcc14_mean = np.mean(mfcc[13])
    mfcc14_var = np.var(mfcc[13])
    mfcc15_mean = np.mean(mfcc[14])
    mfcc15_var = np.var(mfcc[14])
    mfcc16_mean = np.mean(mfcc[15])
    mfcc16_var = np.var(mfcc[15])
    mfcc17_mean = np.mean(mfcc[16])
    mfcc17_var = np.var(mfcc[16])
    mfcc18_mean = np.mean(mfcc[17])
    mfcc18_var = np.var(mfcc[17])
    mfcc19_mean = np.mean(mfcc[18])
    mfcc19_var = np.var(mfcc[18])
    mfcc20_mean = np.mean(mfcc[19])
    mfcc20_var = np.var(mfcc[19])
    # print(mfcc1_mean)
    # print(mfcc1_var)
    # print(mfcc2_mean)
    # print(mfcc2_var)
    # print(mfcc3_mean)



    return [length, chroma_stft_mean, chroma_stft_var, rms_mean, rms_var,
            spectral_centroid_mean, spectral_centroid_var,
            spectral_bandwidth_mean, spectral_bandwidth_var, rolloff_mean,
            rolloff_var, zero_crossing_rate_mean, zero_crossing_rate_var,
            harmony_mean, harmony_var, perceptr_mean, perceptr_var, tempo,
            mfcc1_mean, mfcc1_var, mfcc2_mean, mfcc2_var, mfcc3_mean,
            mfcc3_var, mfcc4_mean, mfcc4_var, mfcc5_mean, mfcc5_var,
            mfcc6_mean, mfcc6_var, mfcc7_mean, mfcc7_var, mfcc8_mean,
            mfcc8_var, mfcc9_mean, mfcc9_var, mfcc10_mean, mfcc10_var,
            mfcc11_mean, mfcc11_var, mfcc12_mean, mfcc12_var, mfcc13_mean,
            mfcc13_var, mfcc14_mean, mfcc14_var, mfcc15_mean, mfcc15_var,
            mfcc16_mean, mfcc16_var, mfcc17_mean, mfcc17_var, mfcc18_mean,
            mfcc18_var, mfcc19_mean, mfcc19_var, mfcc20_mean, mfcc20_var]


# when user gives a song, divide in it 10 parts of 3 seconds each
# and get the features of each part and finally take the average of
# all the parts and return it as a list

def divide_song(song):
    y, sr = librosa.load(song)
    # print(y.shape)
    # print(sr)
    length = y.shape[0]//sr # length of song in seconds
    # print(length)
    features = []
    for i in range(10):
        y1 = y[i*3*sr:(i+1)*3*sr]
        features.append(get_features(y1))
    features = np.array(features)
    # print(features.shape)
    features = np.mean(features, axis=0)
    # print(features.shape)
    return features

# append this to song_data.json file
def append_to_json(song):
    data = {}
    data['song'] = song
    data['features'] = divide_song(song).tolist()
    with open('song_data.json', 'a') as outfile:
        json.dump(data, outfile)
        outfile.write('\n')