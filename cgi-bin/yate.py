
from string import Template

def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')

def include_header2(the_title, the_query):
    with open('header2.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title, query=the_query))

def include_header(the_title):
    with open('header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))

def include_footer(the_links):
    with open('footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')

def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')

def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')

def select_list(sl_name, sl_items):
    u_string = '<label>' + sl_name + '</label>'
    u_string += '<select name="' + sl_name + '">'
    for item in sl_items:
        u_string += '<option>' + item + '</option>'
    u_string += '</select><br />'
    return(u_string)

def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')

def para(para_text):
    return('<p>' + para_text + '</p>') 

def text_input(label, name):
    return('<label>' + label + '</label><input type="text" name="' + name +
                             '"> <br />')


def html_table((list, headers)):
    tb = '<table>'
    tb += '<tr>'
    for head in headers:
        tb += '<th>' + head + '</th>'
    tb += '</tr>'
    
    for r in list:
        tb += '<tr>'
        for c in r:
            if isinstance(c, str):
                tb += '<td>' + c + '</td>'
            else:
                tb += '<td>' + str(c) + '</td>'
        tb += '</tr>'
    tb += '</table>'
    return tb
