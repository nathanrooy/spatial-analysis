def m_to_km(m):
    '''convert meters to kilometers'''
    return m / 1000


def m_to_mi(m):
    '''convert meters to miles'''
    return m * 0.000621371


def m_to_ft(m):
    '''convert meters to feet'''
    return m_to_mi(m) * 5280.0


def m_to_nm(m):
    '''convert meters to nautical miles'''
    return m / 1852.0


def m_to_yd(m):
    '''convert meters to yards'''
    return m * 1.0936132983


conversion_dict = {
    'ft': m_to_ft,
    'km': m_to_km,
    'mi': m_to_mi,
    'nm': m_to_nm,
    'yd': m_to_yd
}
