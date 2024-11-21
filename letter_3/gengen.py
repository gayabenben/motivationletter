import json


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
        #print(f"{output} Saved successfully")
    return 

def load_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

"""def load_info(filename):
    try:
        #print(f"Loading {filename}")
        with open(filename, 'r') as file:
            data = json.load(file)
            print(data)
        return data
    except Exception as e:
        print(f"Error loading {filename}: {e}")
"""
def load_info(filename):
    try:
        #print(f"Loading {filename}")
        with open(filename, 'r') as file:
            data = json.load(file)
            print(data)
        return data
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return None
    
if __name__ == "__main__":
    
    # my_info 
    my_info = load_info("json/my_info.json")
    print("dict", my_info)
    
    my_first_name = my_info["first_name"]
    my_last_name = my_info["last_name"]
    my_name = f"{my_first_name} \\textsc{{{my_last_name}}}"
    my_mail = my_info["email"]
    my_phone = my_info["phone"]
    my_address = my_info["address"]
    my_postcode = my_info["postal_code"]
    my_city = my_info["city"]
    my_town = f"\\textsc{{{my_city}}}"
    
    # define specific company infos
    
    print("dict", my_info)
    
    position_name = "Data Scientist"
    
    
    it_info = load_info("json/company_a.json")
    destinataire = it_info["name"]
    
    
    recruter_name = it_info["recruter"]
    company_name = it_info["company_name"]
    it_city = it_info["city"]
    it_postcode = it_info["postcode"]
    it_town =  f"\\textsc{{{it_city}}}"
    it_ref = it_info["ref"]
    
    
    print("dict", it_info)
    # Load the necessary information
    my_info = load_txt("txt/my_info.txt").format(my_title="Mr", my_name=my_name, my_mail=my_mail, my_phone=my_phone, my_address=my_address, my_postcode=my_postcode, my_town=my_town)
    
    it_info = load_txt("txt/company_a.txt").format(destinataire=destinataire, recruter_name=recruter_name, company_name=company_name, it_city=it_city, it_postcode=it_postcode, it_town=it_town, it_ref=it_ref)
    
    lobject = f"Job application for a {position_name} position"
    receiver_info = load_txt("receiver_info.txt")
    
    print("it city", it_city)
    
    receiver_info = receiver_info.format(destinataire=destinataire,  ville=it_city)
    
    intro = load_txt("txt/intro.txt").format(recruter_name=recruter_name, position_name=position_name, company_name=company_name)
    specific = load_txt("txt/specific_a.txt").format(company_name=company_name)
    closing = load_txt("txt/closing.txt").format(company_name=company_name)
    
    # Combine the intro and specific parts
    body = intro + specific + closing
    
    
    generate_custom_letter(receiver_info, my_info, lobject, body, closing)
