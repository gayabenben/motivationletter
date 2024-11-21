import json

def load_template_from_json(file_path):
    with open(file_path, 'r') as file:
        templates = json.load(file)
    return templates["letter_template"]

print(load_template_from_json("templates.json"))
#def load_text_file(file_path):
    

def generate_custom_letter(receiver_info, objet, body, closing, template_file):
    templates = load_template_from_json(template_file)
    print("templates", templates)
    # Extract the preamble and letter template
    #preamble = templates["preamble"]
    letter_template = templates#["letter_template"]
    
    # Combine the preamble with the customized part of the letter
    full_letter =  letter_template.format(
        receiver_info=receiver_info,
        objet=objet,
        body=body,
        closing=closing
    )
    
    # Save the customized letter to a .tex file
    with open("custom_letter.tex", "w") as file:
        file.write(full_letter)



# Example usage
template_file = "templates.json"
receiver_info = "M. \\textsc{Destinataire}\\\\Entreprise XYZ\\\\123 Avenue des Exemples\\\\75000 \\textsc{Paris}"
objet = "Demande de Stage"
body = "\\hspace{.7cm}Cher Monsieur/Madame,\\\\..."
closing = "Cordialement,"

generate_custom_letter(receiver_info, objet, body, closing, template_file)
