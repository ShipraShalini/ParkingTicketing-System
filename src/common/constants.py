
INDEX = "parking"
DOC_TYPE = "slot_info"
ANALYSER = "not_analyzed"

STATUS_FREE ="Free"
STATUS_OCCUPIED ="Occupied"

SLOT_NO = "slot_no"
SLOT_NO_DESC = "-slot_no"
SLOT_INFO = "slot_info"

BLANK = None
MAX_NO_OF_SLOTS = 10

LABEL_FREE = "Free"
LABEL_OCCUPIED = "Occupied"
LABEL_STATUS_TITLE = "Status of Parking area"


OCCUPIED_MESSAGE="All Parking Slots Occupied"
ALREADY_PARKED_MESSAGE="This car is already parked"
FORMAT = "png"

HTML_CODE=html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>chart</title>
</head>
<body>

    <div>
         <h1> piechart </h1>

        <img src="data:image/png;base64,{0}"/>
    </div>

    <div>

        <h1> barchart </h1>

        <img src="data:image/png;base64,{1}"/>
    </div>

</body>
</html>
'''