import json

def read_request(request):
    if request.method == "POST"  :
        data = json.loads(request.body)
        reg_no = data['reg_no']
        try:
            colour = data['colour'].title()
        except KeyError:
            return reg_no
        else:
            return  reg_no, colour

    elif request.method == "GET":
        print "Body",request.body
        reg_no = request.GET.get('reg_no', None)
        print "reg", reg_no
        colour = request.GET.get('colour', None)
        if colour:
                colour= colour.title()
        return reg_no, colour

    elif request.method == "DELETE":
        data = json.loads(request.body)
        id = data['id']
        return id