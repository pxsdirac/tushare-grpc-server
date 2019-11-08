from tushare_pb2 import *
def date_to_str(date):
    print(date)
    if date.year == 0 or date.month == 0 or date.day == 0:
        return None
    else:
        year = str(date.year)
        if date.month < 10:
            month = "0" + str(date.month)
        else:
            month = str(date.month)
        if len(date.day) < 10:
            day == "0" + str(date.day)
        else:
            day = str(date.day)
        return year + "-" + month + "-" + day

def ktype_to_str(kType):
    if kType == D:
        return 'D'
    elif kType == M:
        return 'M'
    elif kType == W:
        return 'W'
    elif kType == m5:
        return '5'
    elif kType == m15:
        return '15'
    elif kType == m30:
        return '30'
    elif kType == '60':
        return '60'
    else:
        return 'D'

def result(df):
    return Dataframe(json = df.to_json(orient='split'))
