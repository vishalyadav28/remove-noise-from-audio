# 1. Basic Audio Cleaning:

first_output = f'ffmpeg -i Voice_001.m4a -af "highpass=f=200, lowpass=f=3000" output_cleaned_audio.wav'

# 2. Equalization (EQ):

second_output = f'ffmpeg -i output_cleaned_audio.wav -af "equalizer=f=1500:width_type=h:width=100:g=5" output_eq_audio.wav'

# 3. Dynamic Range Compression:


third_output = f'ffmpeg -i output_eq_audio.wav -af "compand=attacks=5:points=-70/-70|-25/-25|0/-5:soft-knee=6" output_compressed_audio.wav'

# 4. Noise Reduction:

fourth_output = f'ffmpeg -i output_compressed_audio.wav -af "highpass=f=200, lowpass=f=3000, afftdn" output_noise_reduced_audio.wav'
