import sys
sys.path.append('./components')
import speech_to_text1
import part2
from async_llama2 import llama_get_category
from playFiles import playAudioFile

chat_history = []
while True:
    query = speech_to_text1.transcribe_stream()  # Captures spoken input from the user.
    
    category_filler = llama_get_category(query)  # Processes the query to categorize and determine the filler response.
    
    # Assuming playAudioFile is adapted to handle the new structure and returns relevant information.
    type_value, filler_no, Category, Sub_Category, QuestionType = playAudioFile(category_filler)
    print('category_filler:', category_filler)
    print('type_value:', type_value)
    print('filler_no:', filler_no)
    print('Category:', Category)
    print('Sub_Category:', Sub_Category)
    print('QuestionType:', QuestionType)

    # Assembling the category information into a dictionary for further processing.
    category = {
        'Category': Category,
        'Sub Category': Sub_Category,
        'QuestionType': QuestionType
    }

    # Processes the user query and updates chat history accordingly.
    chat_history = part2.response_type(query, category, type_value, chat_history)
