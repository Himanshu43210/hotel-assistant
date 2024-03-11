import json
import sounddevice as sd
import soundfile as sf

def getjson(text):
    print('Processing text to extract details...')
    type_value, filler_no, Category, Sub_Category, QuestionType = '', '', '', '', ''
    for item in text:
        # Since 'item' is already a dictionary, we work with it directly
        category_dict = item  # No need to use json.loads on an already decoded dictionary

        # Extract relevant information from the dictionary
        type_value = category_dict.get('Type', type_value)
        filler_no = category_dict.get('FillerNo', filler_no)
        Category = category_dict.get('Category', Category)
        Sub_Category = category_dict.get('Sub Category', Sub_Category)
        QuestionType = category_dict.get('QuestionType', QuestionType)
           
    return type_value, filler_no, Category, Sub_Category, QuestionType



def playAudioFile(answer):
    # Extract category details from the answer
    type_value, filler_no, Category, Sub_Category, QuestionType = getjson(answer)
    
    # Dynamically construct the file name based on the extracted details
    # Assuming 'assets/fillers/' directory contains appropriately named files.
    # Note: Adjust the naming convention as per your actual file names and paths.
    file_name = f'assets/fillers/cat{type_value}fillerno{filler_no}.wav'
    print(f'Playing audio file: {file_name}')
    
    # Play the selected audio file
    play_audio(file_name)
    
    # Return the extracted details for further processing if needed
    return type_value, filler_no, Category, Sub_Category, QuestionType

def play_audio(filename):
    # Read and play the specified audio file
    try:
        data, fs = sf.read(filename)
        sd.play(data, fs)
        sd.wait()  # Wait until the audio file has finished playing
    except Exception as e:
        print(f"Error playing audio file {filename}: {e}")

