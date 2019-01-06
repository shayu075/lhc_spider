import pymysql
qs_date = {}


def get_list_by_30m(_list):
    re = []
    for x in _list:
        if x.strip():
            tmp = x.split('.')
            for xx in tmp:
                c_tmp = xx.strip()
                if c_tmp.isdigit():
                    re.append(c_tmp)
    return re


def get_tuple_by_ws(_list):
    key = ''
    re = []
    for x in _list:
        c_tmp = x.strip()
        if c_tmp:
            if '期:六尾中特' in c_tmp:
                key = c_tmp.replace('期:六尾中特', '')
                continue
            c_tmp = c_tmp.replace('【', '').replace('】', '')
            for xx in c_tmp.split('-'):
                if xx.isdigit():
                    re.append(xx)
    return (key, re)


def get_tuple_by_bs(_list):
    key = ''
    re = []
    for x in _list:
        c_tmp = x.strip()
        if c_tmp:
            if '期-' in c_tmp:
                key = c_tmp.replace('期-', '')
                continue
            if c_tmp in ('红波', '蓝波', '绿波'):
                re.append(c_tmp)
    return (key, re)


def get_tuple_by_sx(_list):
    key = ''
    re = []
    for i, x in enumerate(_list):
        c_tmp = x.strip()
        if c_tmp:
            if '期:精准七肖中特' in c_tmp:
                key = c_tmp.replace('期:精准七肖中特', '')
                continue
            if '实力证明,期期公开' in c_tmp:
                for xx in range(6, i):
                    c_tmp = _list[xx].strip().replace('【', '').replace('】', '')
                    for xxx in c_tmp:
                        if xxx in '鼠牛虎兔龙蛇马羊猴鸡狗猪':
                            re.append(xxx)
    return (key, re)


def get_tuple_by_3t(_list):
    if _list[2] == '更新中':
        return None
    key = _list[0][:3]
    re = list(_list[2].replace('-', ''))
    if len(re) < 3:
        return None
    return (key, re)


def get_date_by_qs(qs):
    results = None
    db = pymysql.connect("localhost", "root", "123456", "my_study")
    cursor = db.cursor()
    sql = "select t.id,t.qs,t.`year`,t.`month`,t.`day` from lhc_result_record t where t.`year`=2019 and qs=" + qs
    try:
        cursor.execute(sql)
        results = cursor.fetchone()
    except:
        print("Error: unable to fetch data")
    finally:
        db.close()
    return results


if __name__ == '__main__':
    pass

