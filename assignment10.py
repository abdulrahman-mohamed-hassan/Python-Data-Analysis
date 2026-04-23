intro = input("Please introduce yourself: ")
education = input("Please tell us about your school: ")
with open("info.txt", "w") as file:
    file.write(intro + "\n")
    file.write(education + "\n")
print("Ok. Your data is saved in document info.txt")


try:
    with open("doc1.txt", "r") as doc1, open("doc2.txt", "r") as doc2:
        content1 = doc1.read()
        content2 = doc2.read()
    with open("doc3.txt", "w") as doc3:
        doc3.write(content1 + "\n" + content2)
    print("Data from doc1.txt and doc2.txt saved into doc3.txt")
except FileNotFoundError as e:
    print("ERROR: One of the input files is missing:", e)


date_end = input("Please enter today's date (for end): ")
with open("info.txt", "a") as file:
    file.write("Date: " + date_end + "\n")
print("Changes are saved to the file info.txt")


date_start = input("Please enter today's date (for beginning): ")
with open("info.txt", "r") as file:
    content = file.read()
with open("info.txt", "w") as file:
    file.write("Date: " + date_start + "\n" + content)
print("Date added to the beginning of info.txt")