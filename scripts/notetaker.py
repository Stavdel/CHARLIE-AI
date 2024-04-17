# Trying to add functionality to convert Charlie's responses into files on computer. Bot responses returned in Markdown.

'''
      Idea: You're able to send image api calls to claude and it has the ability to understand text in an image. An idea
            I have is to have Charlie write out your notes and save them on your computer so you can view the raw text
            digitally. Naming the files based on the content and storing it into an appropriate folder based on the
            content type. (ex: Python notes will be put in separate folder such as "Variables", "Lists", "Dictionaries")

      Potential next step: This is for text only, however Claude can also generate images based on a prompt and has the
                           ability to explain the context of an image. Such as "A black cat sitting under a ladder"
                           Talk to claude on claude.ai and send it an image to test how accurate this would be and
                           if it's worth implementing.

                          Example: User: "Hello, given this image: [image] respond with all visable text on this image with a 
                                         similar format and explain any drawings or non-text important elements for context
                                         by including a lengthy description of the object inside "[]" multiple images recieve
                                         multiple pairs of brackets, each placed in the appropriate position of the image.
                                         (ex: "Text" [Image description] ...)

                                   Assistant: responds with text from the image and a description of imagine encapsulated in []

                                   User: "Print out input text I send you verbatim while keeping format of the text. Generate
                                   image based on the description of the image encapsulated in brackets ("[]")
'''



# Again keep in mind that Claude responds in Markdown so saving file as a txt could result in weird formatting issues.

def create_markdown(file_name, markdown_string):

    # Write the Markdown string to a file
    with open(file_name, "w") as file:
        file.write(markdown_string)

    print(f"Markdown content saved to {file_name}")



if __name__ == "__main__":
    main()
