try:
    with open("greeting.txt", "w") as file:
        file.write("Hello Good morning")
    print("File written successfully.")

except FileNotFoundError:
    print("Error: The file was not found.")

except IOError:
    print("Error: An I/O error occurred while writing to the file.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("File operation complete.")
