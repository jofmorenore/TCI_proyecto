def plot_sounds_and_specgrams(infos):
    """
    """
    fig = plt.figure(figsize=(15, 30))
    subfigs = fig.subfigures(nrows=len(infos), ncols=1)
    
    for row, (subfig, info) in enumerate(zip(subfigs, infos)):
        (label, subject, trial) = info
        subfig.suptitle(f'Dígito {label}, Sujeto {subject}, Intento {trial}')
        
        axs = subfig.subplots(nrows=1, ncols=2)
        
        file = f"audio-mnist/data/{subject}/{label}_{subject}_{trial}.wav"
        # Lectura del archivo de audio
        sound, sample_rate = librosa.load(file, sr=None) # sr=None, trabaja en el clásico 44100 Hz (native sampling rate)
        
        # Aplica Short-Time-Fourier-Transformer para tranformar los datos
        D = librosa.stft(sound)
        # Convierte frecuencia a decibel
        S_db = librosa.amplitude_to_db(np.abs(D),ref=np.min)
        
        # Grafica la forma de onda 'waveform'
        #axs[0].plot(sound)
        librosa.display.waveshow(y=sound, sr = sample_rate, ax=axs[0])
        axs[0].set_title('Waveform')
        axs[0].set_ylabel('Amplitude')
        
        # Grafica el espectrograma
        fig = librosa.display.specshow(S_db,x_axis='time',y_axis='log',ax=axs[1])
        # Agrega la barra del color de la escala en dB
        plt.colorbar(fig,format ='%+2.0f dB')
        axs[1].set_title('Spectrogram')
        axs[1].set_ylabel('Frequency (Hz)')
        
        for ax in axs.flat:
            ax.set(xlabel='Time (s)')
