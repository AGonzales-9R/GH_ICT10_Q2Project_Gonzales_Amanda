from pyscript import display, document

def calculateGWA(e):
    document.getElementById('gwaSummary').innerHTML= " "
    first_name = document.getElementById('inputFN').value
    last_name = document.getElementById('inputLN').value
    full_name = (first_name + " " + last_name)

    english = float(document.getElementById('inputENG').value)
    filipino = float(document.getElementById('inputFIL').value)
    math = float(document.getElementById('inputMATH').value)
    ss = float(document.getElementById('inputSS').value)
    sci = float(document.getElementById('inputSCI').value)
    ict = float(document.getElementById('inputICT').value)
    
    subjects = [english, filipino, math, ss, sci, ict]
    units = (5, 3, 5, 3, 5, 2)
    total_units = sum(units)
    gu_eng = (english * units[0])
    gu_fil = (filipino * units[1])
    gu_math = (math * units[2])
    gu_ss = (ss * units[3])
    gu_sci = (sci * units[4])
    gu_ict = (ict * units[5])
    gu_sum = (gu_eng + gu_fil + gu_math + gu_ss + gu_sci + gu_ict)
    gwa = (gu_sum / total_units)

    multiline_string = """
    Name: {}
    
    English: {}
    Filipino: {}
    Math: {}
    Social Studies: {}
    Science: {}
    ICT: {}

    Your General Weighted Average is {:.2F}

    """.format(full_name, english, filipino, math, ss, sci, ict, gwa)

    display(multiline_string, target="gwaSummary")