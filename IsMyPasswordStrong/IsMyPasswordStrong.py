import requests

GUI = True


def output_message(status):
    output_msg = "=============\n\n"
    verify = {
        'lower_case': "Minimum 1 lower Character",
        'upper_case': "Minimum 1 upper Character",
        'special_character': "Minimum 1 Special Character",
        'digits': "Minimum 1 decimal Character",
        'length': "Minimum length of 8 Character",
        'un_pwned': "Shouldn't be compromised password",
        'full_un_pwned': "Password shouldn't be subset/part of any compromised password",
        'no_consecutive': "Avoid more than 2 consecutive same character",
    }

    for k in status.keys():
        output_msg += verify[k] + " ✅ \n" if status[k] else verify[k] + " ❌ \n"

    output_msg += "\n\nGiving Equal Weightage to each condition. Your Password Score is: \t" + str(
        sum(status.values()) / 8 * 100)
    output_msg += '' if status["un_pwned"] else "\nVERY RISKY [AS ITS COMPROMISED]"
    output_msg += "\nMAY BE RISKY [AS ITS PARTIALLY COMPROMISED]" if status["un_pwned"] and (not status[
        "full_un_pwned"]) else ""

    return output_msg


def validations(password):
    verify = dict.fromkeys(
        ['lower_case', 'upper_case', 'special_character', 'digits', 'length', 'un_pwned', 'full_un_pwned',
         'no_consecutive'], False)

    risky = requests.request('GET', "https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt")
    all_words = str(risky.text).split('\r\n')
    all_words = set(all_words[len(all_words) - 100000:])

    verify['length'] = True if len(password) >= 8 else False
    verify['un_pwned'] = True

    for word in all_words:
        if password == word:
            verify['un_pwned'] = False
            print("MATCHES WITH COMPROMISED PASSWORD: ", word)
            break

    verify['full_un_pwned'] = verify['un_pwned']
    part_of = []
    for word in all_words:
        if len(str(word)) > 3 and str(word) in str(password):
            part_of.append(word)
            verify['full_un_pwned'] = False
    print("IS-SUPERSET OF COMPROMISED PASSWORD(s):", part_of)

    res = any([len(set(password[i: i + 3])) == 1 for i in range(len(password) - 2)])
    verify['no_consecutive'] = False if res else True

    for c in password:
        verify['lower_case'] = True if c.islower() or verify['lower_case'] else False
        verify['upper_case'] = True if c.isupper() or verify['upper_case'] else False
        verify['special_character'] = True if not c.isalnum() or verify['special_character'] else False
        verify['digits'] = True if c.isdigit() or verify['digits'] else False

    return verify


if GUI:
    from tkinter import *

    window = Tk()
    Label(window, text='Enter Password').pack()
    sv = StringVar()


    def process(event):
        if e1.get() != '':
            input_string = e1.get()
            check_ = validations(input_string)
            text = output_message(check_)
            T.delete(1.0, END)
            T.insert(1.0, text)


    e1 = Entry(window, textvariable=sv)
    e1.bind("<Return>", process)
    e1.pack()
    T = Text(window, height=15, width=80)
    T.pack()
    mainloop()
else:
    check_status = validations(input("Enter your Password: \t"))
    print(check_status)
    print(output_message(check_status))
