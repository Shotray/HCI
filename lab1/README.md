# Lab1

## Installation

- install conda environment

  ```
  conda env create -f speech.yaml
  conda activate speech
  ```
  
  If the installation fails, please use `pip` to install or download wheel file to install manually

## Run

```
conda activate speech
python asr.py
```

## Modifications to GUI&Codes

- Implemented the program using threads and signals

  ```python
  class RecognizeThread(QThread):
      trigger = pyqtSignal(str)
  
      def __init__(self):
          super(RecognizeThread, self).__init__()
  ```

- First read the information of the microphone, throw an exception if there is an error in recognition, and in the rest of the cases find the most similar command to operate on it. 

  Commands include

  - play music
  - open notepad
  - open canvas

  ```python
      def run(self):
          COMMANDS = ["play music", "open notepad", "open canvas"]
          OPEN = [r"res\Mozart.mp3","notepad.exe","mspaint.exe"]
          
          recognizer = sr.Recognizer()
          microphone = sr.Microphone()
  
          while True:
              guess = self.recognize_speech_from_mic(recognizer,microphone)
  
              if guess["error"]:
                  self.trigger.emit("ERROR: {}".format(guess["error"]))
                  break
  
              self.trigger.emit("You said {}".format(guess["transcription"]))
  
              similarity = [self.get_similarity(guess["transcription"],command) for command in COMMANDS]
  
              if max(similarity) < 0.4 :
                  self.trigger.emit("I didn't catch that. What did you say?\n")   
                  continue
  
              idx = similarity.index(max(similarity))
              os.system(OPEN[idx])
              time.sleep(5)
  ```

- Recognize speech from microphone

  ```python
      def recognize_speech_from_mic(self,recognizer, microphone):
          if not isinstance(recognizer, sr.Recognizer):
              raise TypeError("`recognizer` must be `Recognizer` instance")
  
          if not isinstance(microphone, sr.Microphone):
              raise TypeError("`microphone` must be `Microphone` instance")
  
          with microphone as source:
              recognizer.adjust_for_ambient_noise(source)
              audio = recognizer.listen(source)
  
          response = {
              "success": True,
              "error": None,
              "transcription": None
          }
  
          try:
              response["transcription"] = recognizer.recognize_sphinx(audio)
          except sr.RequestError:
              response["success"] = False
              response["error"] = "API unavailable"
          except sr.UnknownValueError:
              response["error"] = "Unable to recognize speech"
  
          return response
  ```

- Get the similarity between audio and command

  ```python
      def get_similarity(self,s1,s2):
          return difflib.SequenceMatcher(None,s1,s2).ratio()
  ```
  
- Using message box to show the text

  ```python
      def exectue(self):
          self.work.start()
          self.work.trigger.connect(self.show_message)
  
      def show_message(self,message):
          self.ui.mes_box.setText(message)
          self.ui.mes_box.show()
  ```

  

## Improve the accuracy of speech recognition

- Using external API, such as Google Speech API ![image-20220427222324431](C:/Users/69529/AppData/Roaming/Typora/typora-user-images/image-20220427222324431.png)
- Using self-trained model