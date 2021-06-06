from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, response
from datetime import datetime, date


# Create your views here.
def hello1(request):
    # 사용자에게 현재 날짜와 시간을 알려준다.
    current = datetime.now()
    day = date.today().day
    txt = """
    <html>
        <body>
            안녕하세요. <br>
            현재일시: {} <br>
            날짜:{}
        </body>
    </html>
    """
    res_txt = txt.format(current, day)
    response = HttpResponse(res_txt)
    return response


def hello2(request):
    curr = datetime.now()
    curr_txt = curr.strftime('%Y-%m-%d %H:%M:%S')
    return render(request, "exam/greeting.html", {"current": curr_txt})
