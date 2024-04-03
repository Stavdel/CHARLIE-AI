def create_markdown(file_name, markdown_string):

    # Write the Markdown string to a file
    with open(file_name, "w") as file:
        file.write(markdown_string)

    print(f"Markdown content saved to {file_name}")



if __name__ == "__main__":
    main()