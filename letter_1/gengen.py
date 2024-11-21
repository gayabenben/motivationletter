def read_template(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_custom_letter(receiver_info, sender_info, lobject, body, closing):
    preamble = read_template("preamble.tex")
    letter_body_template = read_template("body.tex")
    
    # Replace placeholders in the letter body template
    custom_letter = letter_body_template.replace("{{receiver_info}}", receiver_info) \
                                        .replace("{{sender_info}}", sender_info) \
                                        .replace("{{lobject}}", lobject) \
                                        .replace("{{body}}", body) \
                                        .replace("{{closing}}", closing)
    
    # Combine preamble and custom letter body
    full_letter = preamble + "\n" + custom_letter
    
    output = "tex/custom_letter.tex"
    # Save the customized letter to a .tex file
    with open(output, "w", encoding='utf-8') as file:
        file.write(full_letter)
        
        print(f"{output} Saved successfully")
    return 

def load_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

if __name__ == "__main__":
    # Load the necessary information
    my_info = load_txt("my_info.txt")
    lobject = "Job application for a Data Scientist position"
    receiver_info = load_txt("receiver_info.txt")
    
    # define specific company infos
    company_name = "\\textsc{Probayes}"
    destinataire = company_name
    code = "38~330"
    ville = "\\textsc{Montbonnot-Saint-Martin}"
    
    receiver_info = receiver_info.format(destinataire=destinataire,  ville=ville)
    
    body = load_txt("body_v2.txt").format(company_name=company_name)
    
    closing = load_txt("closing_v2.txt").format(company_name=company_name)
    
    generate_custom_letter(receiver_info, my_info, lobject, body, closing)
