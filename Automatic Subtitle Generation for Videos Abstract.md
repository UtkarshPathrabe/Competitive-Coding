Automatic Subtitle Generation For Videos
========================================  

### Problem and Motivation:  
Every time we watch a movie we have to search for  subtitles, download them and add it manually to the video player. Further, if the sync and quality  aren't good, we have to repeat the process. And for other videos such as lectures, conference or informational talks we seldom find subtitles. If the subtitles can be made from the audio content of the videos, it will be very convenient for the users.  

### Process Flow:
![Process Flow](https://github.com/UtkarshPathrabe/Competetive-Coding/blob/master/Abstract01.png)  

### Implementation Details:  

#### Audio Extraction From Videos:  
For creating subtitles/ captions for videos, we decided to use audio component from the videos due to the following reasons:  
* Video may not give information relevant to making subtitles. Also the source of speech may not be in focus or video quality maybe bad for effective analysis. Audio gives much of the relevant information for making subtitles, robust to situations like source of speech out of video frame.  
e.g. Background narrations.  
* Speech-to-text is a widely researched domain. Primarily applied in voice command control, there are many libraries and algorithms developed for this purpose. Hence there is good support for this process.  
* Audio data is much lesser than video data in complexity, hence this is simpler data giving more effective results.  
We have used VLC media player's feature to extract the audio content of all supported video formats in the form of original audio or other audio formats (such as .flac & .wav). This can be done by using the GUI or VLC command line tool.  

#### Audio To Text Conversion:
There are several libraries providing functions for Speech-to-Text conversion. We have chosen CMU Sphinx library for this purpose. Sphinx is a java library with functions for real time audio or speech to text conversion. We have used `StreamSpeechRecognizer` for recognizing the text from audio. Using Hidden Markov Model algorithm on a dataset of audiobooks from an online digital library LibriVox, newspaper reading of Herald dataset by Centre for Speech Technology Research and collection of videos from YouTube, a classification model is created. First, the audio file is processed and converted to phonemes (phonetic sounds in English). Using this and a dataset of phoneme representations of English words (referred as acoustic file), a Hidden Markov Model is used to form the English words. The Sphinx library has an added advantage that a language model is used for creating meaningful sentences from the words.  

#### Subtitle Generation From Text:  
Once the captions/ subtitles are formed from analyzing the audio file, it is converted to a supported subtitle format (like .srt) for use. Dvd subtitle ripper, Xilisoft Dvd subtitle creator can be used to create subtitles from text. We also considered looking at the latest Sphinx version that has functionality for making subtitle and syncing it with the audio for better results.  

### Brief Code Walkthrough:  
1. Extracting the audio from videos using JAVE. It is a Java library that is a wrapper around ffmpeg. VideoToAudio class handles the conversion process.  
Brief working:  
  1. Open source and destination files.  
  2. Set AudioAttributes for the output file. Program set to encode audio in 16 kHz, 16 bit mono wav format.  
  3. Encoder class used for extracting audio from source with AudioAttributes into destination file. Encode() in encoder class takes these 3 parameters and does the extraction procedure.  
2. Extracting speech from audio using Sphinx4 Java library. Transcriber class handles audio to text conversion.  
Brief working:
  1. Every speech recognition process requires 4 attributes- the dictionary, language model, acoustic model and speech source.  
  2. Set dictionary, language model and acoustic model as described in Dataset description.  
  3. StreamSpeechRecognizer class takes in audio source from a stream for recognition. StreamSpeechRecognizer object is made with earlier set configuration.  
  4. SpeechResult container is used for holding result of recognition performed by StreamSpeechRecognizer object. The recognition is performed till no more result is obtained from input stream.  
  5. SpeechResult gives words along with the timestamp in a format used by subtitle files.  

### Dataset Used:  
* Online digital library of audiobooks and their text from LibriVox.com.  
* Readings of the Herald newspaper.  
* A collection of random videos with subtitles from YouTube.com.  
* Acoustic data of Phoneme representation of English words by CMU. (This is part of the speech recognition library, not an individual dataset.)  

### Trained Models Used:  
There are 3 trained models required for Audio to text translation:  

1. <b>Language Model</b> -> It comprises of  
  * <i>Language Model</i>: Language model used is en-us.lm.dmp. It is created by 13000 words from WSJ (Wall Street Journal) text after pre-processing the text by converting numbers to words, short forms to full forms and punctuation marks being removed. .dmp format has data in binary format which makes loading of trained models very fast.  
  * <i>Grammar Model</i>: Structure of words according to English grammar rules is specified in this model. E.g. (Good morning | Hello) (Bhiksha | Evandro | Paul | Philip | Rita | Will) implies that Good morning | Hello precedes Biksha | Evandro | Paul | Philip | Rita | Will. For the large vocabulary, the search space is configured differently. Grammars are not effective to describe very big word lists. Instead, n-gram language models are used. This is specified in alphabet.arpaformat file.

2. <b>Dictionary Model</b> -> English language already has a carefully prepared language dictionary which is fine tuned for best performance. It comprises of alpha.dict, digits.dict and cmudict.0.6d files.  
  * <i>Alphabet Dictionary (alpha.dict)</i>: It comprises of letter as key and set of phonemes as the value corresponding to the key. There can be more than one phoneme for a particular letter.  
E.g. (A EY), (B B I Y), (B (2) B IH)  
  * <i>Digit Dictionary (digits.dict)</i>: Digits are represented as text and not as numbers. Dictionary comprises of numbers as keys and corresponding set of phonemes as values. There can be more than one phoneme for a particular digit.  
E.g. (ONE HH W AH N), (ONE (2) W AH N)  
  * <i>Word Dictionary (cmudict.0.6d)</i>: It comprises of a word as key and pronounced spelling of word as value. 13000 key value pairs are specified in cmudict.0.6d.  
E.g. (ABRAMO AA B R AA M OW), (ACCENT AE K S EH N T)

3. <b>Acoustic Model</b> -> US English acoustic models for microphone is prepared using Wall Street Journal by varying number of senones, continuous/non-continuous attribute, HMM topology and number of gaussians per state. Acoustic model used for project is WSJ_8gau_13dCep_16k_40mel_130Hz_6800Hz which can be downloaded from https://code.google.com/p/motenav/downloads/detail?name=WSJ_8gau_13dCep_16k_40mel_130Hz_6800Hz-1.12_r8.jar&can=2&q=  

### Some Theory Behind The Recognition Process:  
Speech Recognition performed has the following components:  
* Classifying Audio segments to phonetic sounds in a language. The target set of phonetic sounds in a language are specified by the Acoustic model.  
* Combining phonetic sounds to words. This is done by using Dictionary model. HMM is used for time series analysis of phonetic sounds to recognize set of target words.  
* Forming sentence from words through semantic analysis. This is done using Language model. Every sequence of phonetic sounds can result in a set of words e.g. odyssey | ought to see | O to C, all these sounds similar, one may be more appropriate than another based on context.  
![Recognition of phonetic sounds called as phonemes into words.](https://github.com/UtkarshPathrabe/Competetive-Coding/blob/master/Abstract02.png)  
Recognition of phonetic sounds called as phonemes into words.  
Hidden Markov Models (HMMs) provide a simple and effective framework for modelling time-varying spectral vector sequences. As a consequence, almost all present day large vocabulary continuous speech recognition (LVCSR) systems are based on HMMs.  
![The Principal Components of a Large Vocabulary Continuous Speech Recogniser](https://github.com/UtkarshPathrabe/Competetive-Coding/blob/master/Abstract03.png)  
The principal components of a large vocabulary continuous speech recogniser are illustrated in Figure above. The input audio waveform from a microphone is converted into a sequence of fixed size acoustic vectors in a process called feature extraction. The decoder then attempts to find the sequence of words which is most likely to have generated the feature vector. However, since P(word|Feature vector) is difficult to model directly, Bayes Rule is used.  
The likelihood p(Feature vector|word) is determined by an acoustic model and the prior P(word) is determined by a language model. The basic unit of sound represented by the acoustic model is the phone. For example, the word "bat" is composed of three phonemes /b/ /ae/ /t/. About 40 such phonemes are required for English. For any given word, the corresponding acoustic model is synthesized by concatenating phoneme models to make words as defined by a pronunciation dictionary. The parameters of these phoneme models are estimated from training data consisting of speech waveforms and their transcriptions. The language model is typically an N-gram model in which the probability of each word is conditioned only on its N - 1 predecessors. The N-gram parameters are estimated by counting N-tuples in appropriate text corpora. The decoder operates by searching through all possible word sequences using pruning to remove unlikely hypotheses thereby keeping the search tractable. When the end of the utterance is reached, the most likely word sequence is output. Alternatively, modern decoders can generate lattices containing a compact representation of the most likely hypotheses.  

### Requirements For Running Programs:  
1. Video to audio requires JAVE library, steps to set this up are:  
  1. Download JAVE source 1.0.2 from http://www.sauronsoftware.it/projects/jave/download.php and add all JAVA classes in it to your eclipse package.  
  2. Go to temp folder (start->run->(type) %temp%).  
  3. Create new folder jave-1.  
  4. Add ffmpeg application and pthreadGC2.dll to jave-1. Both files are found in java 1.0.2 folder.  
2. Audio to text requires sphinx setup as follows:
  1. Download sphinx4 from http://sourceforge.net/projects/cmusphinx/files/sphinx4/5%20prealpha/  
  2. Go to `File > Import > Existing Project` into Workspace and choose the sphinx4 zip file downloaded in the previous step.  
  3. Right click on build.xml file in the project and choose run as Ant build.  
In case of missing jar errors, add jar files manually from extracted content of sphinx4 zip folder.  