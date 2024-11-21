import json
import sys
import logging


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
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

"""
def format_receiver_info(template, company_details):
    try:
        # Replace placeholders in the template with actual company details
        formatted_info = template.format(destinataire=company_details['destinataire'], ville=company_details['town'])
        return formatted_info
    except KeyError as e:
        print(f"Key error in formatting receiver info: {e}")
        return None
"""
def format_intro(template, company_details, position_name):
    try:
        formatted_intro = template.format(recruter_name=company_details['recruter_name'], 
                                          position_name=position_name, 
                                          company_name=company_details['company_name'],
                                          ref_offer=company_details['ref'])
        return formatted_intro
    except KeyError as e:
        print(f"Key error in formatting intro: {e}")
        return None

def format_specific(template, company_details):
    #print("company_details", company_details)
    try:
        formatted_specific = template.format(company_name=company_details['company_name'],
                                             position_name=company_details['position'])
        return formatted_specific
    except KeyError as e:
        print(f"Key error in formatting specific part: {e}")
        return None

def format_closing(template, company_details):
    try:
        formatted_closing = template.format(company_name=company_details['company_name'])
        return formatted_closing
    except KeyError as e:
        print(f"Key error in formatting closing: {e}")
        return None



def my_format(template, personal_info):
    #print("personal_info", personal_info)
    my_name = f"{personal_info['first_name']} \\textsc{{{personal_info['last_name']}}}"
    #print("my_name", my_name)
    if not template:
        return "Template could not be loaded."

    #print("personal_info:", personal_info)
    try:
        formatted_personal = template.format(
            my_title = "Mr. ",
            my_name=my_name, 
            my_address=personal_info['address'], 
            my_postcode=personal_info['postcode'], 
            my_town = personal_info['town'], 
            my_mail=personal_info['mail'], 
            my_phone=personal_info['phone']
        )
        return formatted_personal
    except KeyError as e:
        print(f"Key error in formatting personal info: {e}")
        return None
    
def it_format(template, it_info):
    try:
        formatted_it = template.format(
            it_name=it_info['company_name'], 
            #it_address=it_info['address'], 
            it_postcode=it_info['postcode'], 
            it_town=it_info['town']
            #it_mail=it_info['mail'], 
            #it_phone=it_info['phone']
        )
        return formatted_it
    except KeyError as e:
        print(f"Key error in formatting IT info: {e}")
        return None
    
def load_info(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        #return None
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} could not be decoded.")
        #return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        #return None

def format_personal_info(info):
    formatted_info = {
        "name": f"{info['first_name']} \\textsc{{{info['last_name']}}}",
        "mail": info["mail"],
        "phone": info["phone"],
        "address": info["address"],
        "postcode": info["postcode"],
        "town": f"\\textsc{{{info['town']}}}"
    }
    return formatted_info

def format_company_info(info):
    #redefine name if necessary
    if "recruter" not in info:
        print("Warning: recruter not found in company info. Using default value.")
        recruter = "Hiring Manager"
    else:
        recruter = info["recruter"].split(" ")  
        if len(recruter) > 1:
            recruter = f"{recruter[0]} \\textsc{{{recruter[1]}}}"
        elif len(recruter) == 1:
            recruter = f"\\textsc{{recruter[0]}}"
        
        recruter = "Hiring Manager"
    formatted_info = {
        #"destinataire": info["name"],
        "recruter_name": recruter,
        "company_name": info["company_name"],
        "town": f"\\textsc{{{info['town']}}}",
        "postcode": info["postcode"],
        "ref": info["ref"],
        "position": info["position"]
    }
    return formatted_info


def main():
    my_info = load_info("json/my_info.json")
    if my_info is None:
        return

    company_info = load_info("json/company_6.json")
    if company_info is None:
        return

    #print(company_info)
    personal_info = format_personal_info(my_info)
    company_details = format_company_info(company_info)

    position_name = "Data Scientist"
    lobject = f"Job application for a {position_name} position"
    
    
    #print(personal_info)
    #print(company_details)
    
    #print(company_details["recruter_name"])
    #sys.exit(1)
    # Load and format texts (details omitted for brevity)
    #receiver_info = format_compa_info(load_txt("receiver_info.txt"), company_details)
    receiver_info = company_details["recruter_name"]
    
    #print("here", receiver_info)
    #
    intro = format_intro(load_txt("txt/intro.txt"), company_details, position_name)
    specific = format_specific(load_txt("txt/specific_a.txt"), company_details)
    closing = format_closing(load_txt("txt/closing.txt"), company_details)
    
    #
    closing_a = format_closing(load_txt("txt/closing_a.txt"), company_details)
     
    #print(intro)
    #print(specific)
    #print(closing)
    #sys.exit(1)
    
    #personal_info = format_personal_info(my_info)
    #print(personal_info)
    #print("my_info", my_info)
    #print(type(my_info))
    #print(type(company_details))
    
            
    format_perso = my_format(load_txt("my_info.txt"), my_info)
    format_it = it_format(load_txt("it_info.txt"), company_info)
    #f"{personal_info['name']} \\\\ {personal_info['address']} \\\\ {personal_info['postcode']} {personal_info['town']} \\\\ {personal_info['mail']} \\\\ {personal_info['phone']}"
    #print("format_it", format_it)
    #print(format_persoo)
    body = intro + specific #+ closing
    #print(body)
    
    receiver_info = format_it
    
    generate_custom_letter(receiver_info, format_perso, lobject, body, closing_a)
    
    #logging
    #ret = logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    #print(ret)
if __name__ == "__main__":
    main()