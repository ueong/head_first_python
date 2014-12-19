
from string import Template
"표준 string 라이브러리에서 Template 클래스를 임포트한다. 이 클래스는 문자열에서 하위 문자열을 교체할 수 있게 한다."

def start_response(resp="text/html"):
"이 함수는 하나의 선택적 인자를 받아 CGI의 Content-type: 라인을 생성한다. 'text/html'이 기본값이다."
    return('Content-type: ' + resp + '\n\n')

def include_header(the_title):
"""이 함수는 인자 하나를 받아 HTML 페이지의 시작 부분에 있는 제목으로 사용한다.
   페이지 자체는 templates/header.html이라는 별도 파일에 저장되어 있으며, 필요에 따라 제목만 바뀐다."""
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))

def include_footer(the_links):
""" include_header 함수와 비슷하지만, 이 함수는 받은 인자를 사용해서 HTML 페이지 끝부분을 만든다.
    이 페이지 자체는 templates/footer.html이라는 별도의 파일에 저장되어 있으며, 인자를 새용해서 HTML의 link 태그를 동적으로 만든다.
    사용한 형태를 보니, 인자는 딕셔너리 형이어야 할 것 같다. """
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

def start_form(the_url, form_type="POST"):
"이 함수는 HTML 폼 앞부분을 반환하고, 호출자가 폼의 데이터를 보낼 URL 뿐만 아니라 사용할 방법을 지정할 수 있게 한다."
    return('<form action="' + the_url + '" method="' + form_type + '">')

def end_form(submit_msg="Submit"):
"이 함수는 HTML 폼을 끝내는 태그를 반환한다. 이 함수의 호출자는 submit_msg에 사용할 문자열을 인자로 지정하여 'submit'이라고 되어 있는 버튼의 기본 텍스트를 바꿀 수 있다."
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')

def radio_button(rb_name, rb_value):
"인자로 받은 라디오 버튼의 이름과 값을 이용해서 HTML 라디로 버튼을 만든다. HTML 폼에는 라디오 버튼이 종종 들어간다. 두 인자 모두 필수 인자다."
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')

def u_list(items):
"리스트를 인자로 받아 HTML 순서 없는 리스트로 만든다. 간단한 for루프로 리스트에 있는 모든 항목을 LI(리스트 항목)로 변환한 후에 UL(순서 없는 리스트) 앨리먼트 안에 넣는다."
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

def header(header_text, header_level=2):
"HTML 헤더 태그(H1,H2,H3 등)를 만들어 반환한다. header_text 인자는 필수 인자이고, 레벨의 기본값은 2이다."
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')

def para(para_text):
"HTML 문장 태그 안에 텍스트 문장(문자열)을 집어넣는다. 굳이 이렇게 함수로 만들 필요가 있었을까?"
    return('<p>' + para_text + '</p>') 
