import pymysql
import datetime
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
            if '期:七肖中特' in c_tmp:
                key = c_tmp.replace('期:七肖中特', '')
                continue
            if '实力证明,期期公开！' in c_tmp:
                for xx in range(6, i):
                    c_tmp = _list[xx].strip().replace('【', '').replace('】', '')
                    for xxx in c_tmp:
                        if xxx in '鼠牛虎兔龙蛇马羊猴鸡狗猪':
                            re.append(xxx)
    return (key, re)


def get_date_by_qs(qs):
    _cur_Max = 0
    if not qs_date.get(qs):
        print('=================开始查询2018期数==================')
        db = pymysql.connect("localhost", "root", "123456", "my_study")
        cursor = db.cursor()
        sql = "select t.id,t.qs,t.`year`,t.`month`,t.`day` from lhc_result_record t where t.`year`=2018"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                qs_date[row[1]] = row
                int_qs = int(row[1])
                _cur_Max = int_qs if int_qs > _cur_Max else _cur_Max
            _next_qs = _cur_Max + 1
            _cur_Max_date = datetime.datetime.strptime('-'.join((qs_date[str(_cur_Max)][2],
                                                                qs_date[str(_cur_Max)][3],
                                                                qs_date[str(_cur_Max)][4])),
                                                       '%Y-%m-%d')
            _days = 0
            if _cur_Max_date.weekday() in (1, 3):
                _days = 2
            if _cur_Max_date.weekday() in (5,):
                _days = 3
            _next_day = _cur_Max_date + datetime.timedelta(days=_days)
            _n_qs = str(_next_qs)
            _n_year = str(_next_day.year)
            _n_month = str(_next_day.month)
            _n_day = str(_next_day.day)
            qs_date[_n_qs] = (_n_year+_n_month+_n_day+_n_qs, _n_qs, _n_year, _n_month, _n_day)
        except:
            print("Error: unable to fetch data")
        finally:
            db.close()
    return qs_date[qs]


if __name__ == '__main__':
    aa = ['\r\n\t\t\t\t\t\t\t', '\r\n\t\t\t\t\t', '美猴王论坛【', '七肖中特', '】已免费公开∝∝用心找，料才好.', '\r\n\t\t\t\t\t\t']
    bb = ['\r\n\t\t\t\t\t\t\t', '\r\n\t\t\t\t\t\t\t', '\r\n\t\t\t\t\t\t\t', '\r\n\t\t\t\t\t\t\t135期:七肖中特', '\r\n\t\t\t\t\t\t\t', '\r\n\t\t\t\t\t\t\t', '【狗猪鸡', '猴', '羊马兔】', '实力证明,期期公开！', '\r\n\t\t\t\t\t\t\t', '\t', '\r\n\t\t\t\t\t\t\t', '特开:猴39准', '\r\n\t\t\t\t\t\t']
    print(get_tuple_by_sx(aa))
    print(get_tuple_by_sx(bb))
    pass

