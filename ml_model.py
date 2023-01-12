import openai


class ml_backend:
        
    openai.api_key = "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" #:))))

    def generate_email(self, user_input, max_tokens=200):
        """Returns a generated an email using GPT3 with a certain prompt and starting sentence"""
        
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt= f"complete this email professionally: {user_input}",
        temperature=0.71,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0.36,
        presence_penalty=0.75
        )
        return response.get("choices")[0]['text']

    def replace_spaces_with_pluses(self, sample):
        """Returns a string with each space being replaced with a plus so the email hyperlink can be formatted properly"""
        changed = list(sample)
        for i, c in enumerate(changed):
            if(c == ' ' or c =='  ' or c =='   ' or c=='\n' or c=='\n\n'):
                changed[i] = '+'
        return ''.join(changed)


    def generate_codeinfo(self, user_input):
        """Explains the code line by line"""
        response = openai.Completion.create(
          model="code-davinci-002",
          prompt=f"{user_input}\nHere's what the above code is doing\n1.",
          temperature=0,
          max_tokens=200,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0,
          stop=["\"\"\""]
        )
        message = response.get('choices')[0]['text']    
        return message
    def generate_document(self,user_input):

        response1 = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"enhance the text:\n\n{user_input}",
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        
        )
        response2 = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"write the technologies used::\n\n{user_input}\n\n1.",
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        
        )
        message = response1.get('choices')[0]['text']  
        technologies = response2.get('choices')[0]['text']


        return message, technologies

