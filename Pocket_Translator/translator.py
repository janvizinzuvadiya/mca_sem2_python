# Step 1: Install the magic library
# pip install deep-translator --break-system-packages

from deep_translator import GoogleTranslator

# Step 2: Set your target language (e.g., 'hindi')
translator = GoogleTranslator(source='auto', target='hindi')

# Step 3: The "Magic" Translation
result = translator.translate("Python is a powerful language!")

print(result) # Output: पायथन शक्तिशाली है!